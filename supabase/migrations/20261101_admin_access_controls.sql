-- Kompas Lab admin controls v1. Additive migration: existing roles, payments and enrollments remain intact.
-- Apply only after review. No user deletion and no payment mutation.
create table if not exists public.kompas_staff_roles (
 user_id uuid primary key references public.profiles(id) on delete cascade,
 role text not null check (role in ('support','content','finance')),
 active boolean not null default true,
 assigned_by uuid references public.profiles(id),
 assigned_at timestamptz not null default now()
);
create table if not exists public.kompas_account_state (
 user_id uuid primary key references public.profiles(id) on delete cascade,
 status text not null default 'active' check (status in ('active','restricted','suspended')),
 reason text,
 changed_by uuid references public.profiles(id),
 changed_at timestamptz not null default now()
);
create table if not exists public.kompas_access_grants (
 id uuid primary key default gen_random_uuid(),
 user_id uuid not null references public.profiles(id) on delete cascade,
 course_id uuid not null references public.courses(id) on delete cascade,
 module_id uuid references public.modules(id) on delete cascade,
 expires_at timestamptz,
 revoked_at timestamptz,
 reason text not null,
 granted_by uuid not null references public.profiles(id),
 created_at timestamptz not null default now(),
 constraint kompas_grant_expiry check (expires_at is null or expires_at > created_at)
);
create index if not exists kompas_grant_active_lookup on public.kompas_access_grants(user_id,course_id,module_id,expires_at) where revoked_at is null;
create table if not exists public.kompas_admin_audit (
 id bigint generated always as identity primary key,
 actor_id uuid references public.profiles(id) on delete set null,
 target_id uuid references public.profiles(id) on delete set null,
 action text not null,
 detail jsonb not null default '{}'::jsonb,
 created_at timestamptz not null default now()
);
create index if not exists kompas_audit_time on public.kompas_admin_audit(created_at desc);
alter table public.kompas_staff_roles enable row level security;
alter table public.kompas_account_state enable row level security;
alter table public.kompas_access_grants enable row level security;
alter table public.kompas_admin_audit enable row level security;
revoke all on public.kompas_staff_roles,public.kompas_account_state,public.kompas_access_grants,public.kompas_admin_audit from public,anon,authenticated;
grant select on public.kompas_staff_roles,public.kompas_account_state,public.kompas_access_grants,public.kompas_admin_audit to authenticated;
-- Account and staff status checks are always derived from the server-side auth.uid().
create or replace function public.kompas_staff_can(p_scope text) returns boolean
language sql stable security definer set search_path = public, pg_temp as $$
 select auth.uid() is not null and (
   public.fn_is_admin() or exists (
    select 1 from public.kompas_staff_roles r where r.user_id=auth.uid() and r.active
    and ((r.role='support' and p_scope in ('users.read','users.manage','audit.read'))
      or (r.role='content' and p_scope in ('content.read','content.manage'))
      or (r.role='finance' and p_scope in ('payments.read','audit.read'))))
 );
$$;
revoke all on function public.kompas_staff_can(text) from public,anon;
grant execute on function public.kompas_staff_can(text) to authenticated;
create or replace function public.kompas_account_active() returns boolean
language sql stable security definer set search_path = public, pg_temp as $$
 select auth.uid() is not null and not exists (
  select 1 from public.kompas_account_state s where s.user_id=auth.uid() and s.status <> 'active'
 );
$$;
revoke all on function public.kompas_account_active() from public,anon;
grant execute on function public.kompas_account_active() to authenticated;
create or replace function public.kompas_module_permitted(p_module_id uuid) returns boolean
language sql stable security definer set search_path = public, pg_temp as $$
 select public.kompas_account_active() and (
  public.fn_is_admin() or exists (
   select 1 from public.kompas_access_grants g
   join public.modules m on m.id = p_module_id
   where g.user_id = auth.uid() and g.course_id = m.course_id
    and (g.module_id is null or g.module_id = m.id)
    and g.revoked_at is null and (g.expires_at is null or g.expires_at > now())
  )
 );
$$;
revoke all on function public.kompas_module_permitted(uuid) from public,anon;
grant execute on function public.kompas_module_permitted(uuid) to authenticated;
drop policy if exists kompas_staff_self_read on public.kompas_staff_roles;
create policy kompas_staff_self_read on public.kompas_staff_roles for select to authenticated
using (user_id=auth.uid() or public.fn_is_admin());
drop policy if exists kompas_state_read on public.kompas_account_state;
create policy kompas_state_read on public.kompas_account_state for select to authenticated
using (user_id=auth.uid() or public.kompas_staff_can('users.read'));
drop policy if exists kompas_grants_read on public.kompas_access_grants;
create policy kompas_grants_read on public.kompas_access_grants for select to authenticated
using (user_id=auth.uid() or public.kompas_staff_can('users.read'));
drop policy if exists kompas_audit_read on public.kompas_admin_audit;
create policy kompas_audit_read on public.kompas_admin_audit for select to authenticated
using (actor_id=auth.uid() or public.fn_is_admin());
-- Support staff can browse profiles to fulfil their assigned duties, not write role/email/payment.
drop policy if exists kompas_support_profiles_read on public.profiles;
create policy kompas_support_profiles_read on public.profiles for select to authenticated
using (public.kompas_staff_can('users.read'));
-- Atomic audited mutations: only super admins assign staff; support can grant access to non-admins.
create or replace function public.kompas_admin_manage_user(
 p_action text, p_target uuid, p_course uuid default null, p_module uuid default null,
 p_value text default null, p_expires timestamptz default null, p_reason text default null
) returns jsonb language plpgsql security definer set search_path = public, pg_temp as $$
declare v_actor uuid:=auth.uid(); v_super boolean; v_target_role text; v_c uuid;
begin
 v_super:=public.fn_is_admin();
 if v_actor is null or not (v_super or public.kompas_staff_can('users.manage')) then
  raise exception 'ACCESS_DENIED' using errcode='42501';
 end if;
 if p_reason is null or length(trim(p_reason)) < 3 or length(p_reason)>400 then
  raise exception 'REASON_REQUIRED';
 end if;
 select role::text into v_target_role from public.profiles where id=p_target for update;
 if not found then raise exception 'USER_NOT_FOUND'; end if;
 if v_actor=p_target or v_target_role='admin' then
  raise exception 'PROTECTED_ACCOUNT' using errcode='42501';
 end if;
 perform public.kompas_check_staff_target(p_target);
 if p_action='set_status' then
  if p_value not in ('active','restricted','suspended') then raise exception 'INVALID_STATUS'; end if;
  insert into public.kompas_account_state(user_id,status,reason,changed_by,changed_at)
  values(p_target,p_value,p_reason,v_actor,now())
  on conflict(user_id) do update set status=excluded.status,reason=excluded.reason,
    changed_by=excluded.changed_by,changed_at=now();
 elsif p_action='set_staff' then
  if not v_super then raise exception 'SUPER_ADMIN_REQUIRED' using errcode='42501'; end if;
  if p_value='none' then
   delete from public.kompas_staff_roles where user_id=p_target;
  elsif p_value in ('support','content','finance') then
   insert into public.kompas_staff_roles(user_id,role,active,assigned_by)
   values(p_target,p_value,true,v_actor)
   on conflict(user_id) do update set role=excluded.role,active=true,assigned_by=v_actor,assigned_at=now();
  else raise exception 'INVALID_ROLE'; end if;
 elsif p_action='grant' then
  if p_course is null then raise exception 'COURSE_REQUIRED'; end if;
  if p_expires is not null and (p_expires <= now() or p_expires > now()+interval '5 years') then
   raise exception 'INVALID_EXPIRY'; end if;
  if p_module is not null then
   select course_id into v_c from public.modules where id=p_module;
   if v_c is distinct from p_course then raise exception 'MODULE_COURSE_MISMATCH'; end if;
  end if;
  insert into public.kompas_access_grants(user_id,course_id,module_id,expires_at,reason,granted_by)
  values(p_target,p_course,p_module,p_expires,p_reason,v_actor);
 elsif p_action='revoke' then
  if p_course is null then raise exception 'COURSE_REQUIRED'; end if;
  update public.kompas_access_grants set revoked_at=now()
   where user_id=p_target and course_id=p_course and module_id is not distinct from p_module
     and revoked_at is null;
 else raise exception 'INVALID_ACTION'; end if;
 insert into public.kompas_admin_audit(actor_id,target_id,action,detail)
 values(v_actor,p_target,p_action,jsonb_build_object('course_id',p_course,'module_id',p_module,'value',p_value,'expiry',p_expires,'reason',p_reason));
 return jsonb_build_object('ok',true,'action',p_action,'target',p_target);
end; $$;
revoke all on function public.kompas_admin_manage_user(text,uuid,uuid,uuid,text,timestamptz,text) from public,anon;
grant execute on function public.kompas_admin_manage_user(text,uuid,uuid,uuid,text,timestamptz,text) to authenticated;
create or replace function public.kompas_admin_user_state(p_target uuid) returns jsonb
language sql stable security definer set search_path=public,pg_temp as $$
 select case when not public.kompas_staff_can('users.read') then null else jsonb_build_object(
  'status',coalesce((select status from public.kompas_account_state where user_id=p_target),'active'),
  'staff',coalesce((select role from public.kompas_staff_roles where user_id=p_target and active),'student'),
  'grants',coalesce((select jsonb_agg(jsonb_build_object('id',g.id,'course_id',g.course_id,'module_id',g.module_id,'expires_at',g.expires_at,'created_at',g.created_at)) from public.kompas_access_grants g where g.user_id=p_target and g.revoked_at is null and (g.expires_at is null or g.expires_at>now())),'[]'::jsonb)
 ) end;
$$;
revoke all on function public.kompas_admin_user_state(uuid) from public,anon;
grant execute on function public.kompas_admin_user_state(uuid) to authenticated;
create or replace function public.kompas_admin_usage() returns jsonb
language plpgsql stable security definer set search_path=public,pg_temp as $$
begin
 if not public.fn_is_admin() then raise exception 'ACCESS_DENIED' using errcode='42501'; end if;
 return jsonb_build_object('database_bytes',pg_database_size(current_database()),
   'course_count',(select count(*) from public.courses),
   'module_count',(select count(*) from public.modules),
   'lesson_count',(select count(*) from public.lessons),
   'profiles_count',(select count(*) from public.profiles),
   'source','database_sql','sampled_at',now());
end; $$;
revoke all on function public.kompas_admin_usage() from public,anon;
grant execute on function public.kompas_admin_usage() to authenticated;
-- Individual module grants are checked in addition to payment entitlements.
create or replace function public.kompas_my_module_access(p_course_slug text,p_module_index integer)
returns boolean language plpgsql stable security definer set search_path=public,pg_temp as $$
declare v_mod uuid; v_en public.enrollments%rowtype;
begin
 if not public.kompas_account_active() then return false; end if;
 select m.id into v_mod from public.modules m join public.courses c on c.id=m.course_id
 where c.slug=p_course_slug and m.order_index=p_module_index;
 if v_mod is null then return false; end if;
 if public.kompas_module_permitted(v_mod) then return true; end if;
 select e.* into v_en from public.enrollments e join public.modules m on m.course_id=e.course_id
 where e.user_id=auth.uid() and m.id=v_mod;
 return found and v_en.payment_status in ('paid','partial') and v_en.frozen_at is null
    and (v_en.expires_at is null or v_en.expires_at>now())
    and (v_en.unlocked_modules is null or public.fn_module_position(v_mod)<=v_en.unlocked_modules);
end; $$;
revoke all on function public.kompas_my_module_access(text,integer) from public,anon;
grant execute on function public.kompas_my_module_access(text,integer) to authenticated;
-- Ensure the protected HTML reader uses exactly the same server-side entitlement.
create or replace function public.fn_paid_page(p_course_slug text,p_module_index integer)
returns jsonb language plpgsql stable security definer set search_path=public,pg_temp as $$
declare v_uid uuid:=auth.uid(); v_html text; v_ver text; f record;
begin
 if v_uid is null then return jsonb_build_object('ok',false,'reason','auth'); end if;
 if not public.kompas_account_active() then return jsonb_build_object('ok',false,'reason','suspended'); end if;
 if not public.kompas_my_module_access(p_course_slug,p_module_index) then
  return jsonb_build_object('ok',false,'reason','no_access'); end if;
 select html,version into v_html,v_ver from public.paid_pages
 where course_slug=p_course_slug and module_index=p_module_index;
 if v_html is null then return jsonb_build_object('ok',false,'reason','missing'); end if;
 for f in select old_text,new_text from public.text_fixes
   where status='active' and page='paid:'||p_course_slug||':'||p_module_index order by id loop
   v_html:=replace(v_html,f.old_text,f.new_text);
 end loop;
 return jsonb_build_object('ok',true,'html',v_html,'version',v_ver);
end; $$;
-- Additive RLS for individually approved *published* lessons and content.
drop policy if exists kompas_granted_lesson_read on public.lessons;
create policy kompas_granted_lesson_read on public.lessons for select to authenticated
using (status='published' and public.kompas_module_permitted(module_id));
drop policy if exists kompas_granted_lesson_content_read on public.lesson_contents;
create policy kompas_granted_lesson_content_read on public.lesson_contents for select to authenticated
using (exists(select 1 from public.lessons l where l.id=lesson_id and l.status='published'
 and public.kompas_module_permitted(l.module_id)));
comment on function public.kompas_admin_usage() is 'Database footprint and counts only; not Supabase billing, Vercel quota or egress.';

-- All published lesson metadata remains available as intended; paid lesson data
-- respects suspended/restricted status for subscriptions as well as individual grants.
drop policy if exists "lessons: kirish darvozasi" on public.lessons;
create policy "lessons: kirish darvozasi" on public.lessons for select to public
using (
 (status='published' and is_free=true) or public.fn_is_admin()
 or (public.kompas_account_active() and status='published'
   and exists(select 1 from public.enrollments e join public.modules m on m.course_id=e.course_id
     where e.user_id=auth.uid() and m.id=lessons.module_id
     and e.payment_status in ('paid','partial') and e.frozen_at is null
     and (e.expires_at is null or e.expires_at>now())
     and (e.unlocked_modules is null or public.fn_module_position(m.id)<=e.unlocked_modules)))
);
drop policy if exists "lesson_contents: gate" on public.lesson_contents;
create policy "lesson_contents: gate" on public.lesson_contents for select to public
using (
 public.fn_is_admin()
 or exists(select 1 from public.lessons l where l.id=lesson_id and l.status='published' and l.is_free)
 or (public.kompas_account_active() and exists(
   select 1 from public.lessons l join public.modules m on m.id=l.module_id
    join public.enrollments e on e.course_id=m.course_id
   where l.id=lesson_id and l.status='published' and e.user_id=auth.uid()
    and e.payment_status in ('paid','partial') and e.frozen_at is null
    and (e.expires_at is null or e.expires_at>now())
    and (e.unlocked_modules is null or public.fn_module_position(m.id)<=e.unlocked_modules)))
);
-- Safe for anon queries: these functions only return false when auth.uid() is absent.
grant execute on function public.kompas_account_active() to anon;
grant execute on function public.kompas_module_permitted(uuid) to anon;
drop policy if exists kompas_content_courses_read on public.courses;
create policy kompas_content_courses_read on public.courses for select to authenticated
using (public.kompas_staff_can('content.read'));
drop policy if exists kompas_content_lessons_manage on public.lessons;
create policy kompas_content_lessons_manage on public.lessons for all to authenticated
using (public.kompas_staff_can('content.manage'))
with check (public.kompas_staff_can('content.manage'));
drop policy if exists kompas_content_lesson_contents_manage on public.lesson_contents;
create policy kompas_content_lesson_contents_manage on public.lesson_contents for all to authenticated
using (public.kompas_staff_can('content.manage'))
with check (public.kompas_staff_can('content.manage'));
drop policy if exists kompas_finance_payments_read on public.payments;
create policy kompas_finance_payments_read on public.payments for select to authenticated
using (public.kompas_staff_can('payments.read'));
drop policy if exists kompas_finance_enrollments_read on public.enrollments;
create policy kompas_finance_enrollments_read on public.enrollments for select to authenticated
using (public.kompas_staff_can('payments.read'));
drop policy if exists kompas_finance_profiles_read on public.profiles;
create policy kompas_finance_profiles_read on public.profiles for select to authenticated
using (public.kompas_staff_can('payments.read'));
-- Forbid support staff from changing other staff accounts through the public RPC.
create or replace function public.kompas_check_staff_target(p_target uuid)
returns void language plpgsql stable security definer set search_path=public,pg_temp as $$
begin
 if not public.fn_is_admin() and exists(select 1 from public.kompas_staff_roles where user_id=p_target and active)
 then raise exception 'PROTECTED_STAFF_ACCOUNT' using errcode='42501'; end if;
end; $$;
revoke all on function public.kompas_check_staff_target(uuid) from public,anon,authenticated;

-- Expose draft course names only to staff who need them for access or finance workflows.
drop policy if exists kompas_staff_courses_read on public.courses;
create policy kompas_staff_courses_read on public.courses for select to authenticated
using (public.kompas_staff_can('users.read') or public.kompas_staff_can('payments.read'));
