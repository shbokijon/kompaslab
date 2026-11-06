-- Hamkor, mentor va jamoa aʼzolari uchun qoʻlda ruxsat (2026-11-06). Additiv migratsiya.
-- 1) kompas_access_grants.kind: ruxsat turi. 2) kompas_pending_grants: hali roʻyxatdan oʻtmagan
-- odam uchun email boʻyicha oldindan ruxsat; email tasdiqlangach (email_confirmed_at) avtomatik faollashadi.
-- 3) Admin RPC: email boʻyicha berish, roʻyxat, bitta ruxsatni bekor qilish. Toʻlov va obunaga tegmaydi.
-- Kirishni baribir kompas_my_module_access() / fn_paid_page() serverda tekshiradi.

alter table public.kompas_access_grants
  add column if not exists kind text not null default 'manual'
  check (kind in ('manual','team','partner','mentor'));

create table if not exists public.kompas_pending_grants (
 id uuid primary key default gen_random_uuid(),
 email text not null check (email = lower(email) and email ~ '^[^@\s]+@[^@\s]+\.[^@\s]+$' and length(email) <= 254),
 course_id uuid not null references public.courses(id) on delete cascade,
 module_id uuid references public.modules(id) on delete cascade,
 expires_at timestamptz,
 kind text not null default 'partner' check (kind in ('team','partner','mentor')),
 reason text not null check (length(trim(reason)) >= 3 and length(reason) <= 400),
 granted_by uuid not null references public.profiles(id),
 created_at timestamptz not null default now(),
 claimed_at timestamptz,
 cancelled_at timestamptz
);
create unique index if not exists kompas_pending_unique_open
  on public.kompas_pending_grants (email, course_id, coalesce(module_id,'00000000-0000-0000-0000-000000000000'::uuid))
  where claimed_at is null and cancelled_at is null;
alter table public.kompas_pending_grants enable row level security;
revoke all on public.kompas_pending_grants from public,anon,authenticated;
grant select on public.kompas_pending_grants to authenticated;
drop policy if exists kompas_pending_read on public.kompas_pending_grants;
create policy kompas_pending_read on public.kompas_pending_grants for select to authenticated
using (public.kompas_staff_can('users.read'));

-- Email boʻyicha ruxsat berish. Foydalanuvchi bor boʻlsa darhol, boʻlmasa kutilayotgan ruxsat sifatida.
create or replace function public.kompas_admin_grant_by_email(
 p_email text, p_course uuid, p_module uuid default null, p_expires timestamptz default null,
 p_kind text default 'partner', p_reason text default null
) returns jsonb language plpgsql security definer set search_path=public,pg_temp as $$
declare v_actor uuid:=auth.uid(); v_email text:=lower(trim(coalesce(p_email,'')));
 v_target uuid; v_role text; v_c uuid; v_gid uuid; v_pid uuid;
begin
 if v_actor is null or not (public.fn_is_admin() or public.kompas_staff_can('users.manage')) then
  raise exception 'ACCESS_DENIED' using errcode='42501'; end if;
 if p_reason is null or length(trim(p_reason))<3 or length(p_reason)>400 then raise exception 'REASON_REQUIRED'; end if;
 if v_email !~ '^[^@\s]+@[^@\s]+\.[^@\s]+$' or length(v_email)>254 then raise exception 'INVALID_EMAIL'; end if;
 if p_kind is null or p_kind not in ('team','partner','mentor') then raise exception 'INVALID_KIND'; end if;
 if p_course is null then raise exception 'COURSE_REQUIRED'; end if;
 if not exists(select 1 from public.courses where id=p_course) then raise exception 'COURSE_NOT_FOUND'; end if;
 if p_expires is not null and (p_expires<=now() or p_expires>now()+interval '5 years') then raise exception 'INVALID_EXPIRY'; end if;
 if p_module is not null then
  select course_id into v_c from public.modules where id=p_module;
  if v_c is distinct from p_course then raise exception 'MODULE_COURSE_MISMATCH'; end if;
 end if;
 select id, role::text into v_target, v_role from public.profiles where lower(email)=v_email limit 1;
 if v_target is not null then
  if v_actor=v_target or v_role='admin' then raise exception 'PROTECTED_ACCOUNT' using errcode='42501'; end if;
  perform public.kompas_check_staff_target(v_target);
  select id into v_gid from public.kompas_access_grants
   where user_id=v_target and course_id=p_course and module_id is not distinct from p_module and revoked_at is null
     and (expires_at is null or expires_at>now()) limit 1;
  if v_gid is not null then
   update public.kompas_access_grants set expires_at=p_expires, kind=p_kind, reason=p_reason, granted_by=v_actor where id=v_gid;
  else
   insert into public.kompas_access_grants(user_id,course_id,module_id,expires_at,reason,granted_by,kind)
   values(v_target,p_course,p_module,p_expires,p_reason,v_actor,p_kind);
  end if;
  insert into public.kompas_admin_audit(actor_id,target_id,action,detail)
  values(v_actor,v_target,'grant_by_email',jsonb_build_object('course_id',p_course,'module_id',p_module,'kind',p_kind,'expiry',p_expires,'reason',p_reason,'email',v_email,'pending',false));
  return jsonb_build_object('ok',true,'status','granted','target',v_target);
 end if;
 select id into v_pid from public.kompas_pending_grants
  where email=v_email and course_id=p_course and module_id is not distinct from p_module
    and claimed_at is null and cancelled_at is null limit 1;
 if v_pid is not null then
  update public.kompas_pending_grants set expires_at=p_expires, kind=p_kind, reason=p_reason, granted_by=v_actor where id=v_pid;
 else
  insert into public.kompas_pending_grants(email,course_id,module_id,expires_at,kind,reason,granted_by)
  values(v_email,p_course,p_module,p_expires,p_kind,p_reason,v_actor) returning id into v_pid;
 end if;
 insert into public.kompas_admin_audit(actor_id,target_id,action,detail)
 values(v_actor,null,'grant_by_email',jsonb_build_object('course_id',p_course,'module_id',p_module,'kind',p_kind,'expiry',p_expires,'reason',p_reason,'email',v_email,'pending',true));
 return jsonb_build_object('ok',true,'status','pending','pending_id',v_pid);
end; $$;
revoke all on function public.kompas_admin_grant_by_email(text,uuid,uuid,timestamptz,text,text) from public,anon;
grant execute on function public.kompas_admin_grant_by_email(text,uuid,uuid,timestamptz,text,text) to authenticated;

-- Faol va kutilayotgan ruxsatlar roʻyxati (admin va support).
create or replace function public.kompas_admin_list_grants() returns jsonb
language plpgsql stable security definer set search_path=public,pg_temp as $$
begin
 if not public.kompas_staff_can('users.read') then raise exception 'ACCESS_DENIED' using errcode='42501'; end if;
 return jsonb_build_object(
  'grants', coalesce((select jsonb_agg(to_jsonb(x) order by x.created_at desc) from (
    select g.id, p.email, nullif(trim(coalesce(p.first_name,'')||' '||coalesce(p.last_name,'')),'') as name,
     c.slug as course_slug, c.title as course_title, m.order_index as module_index, m.title as module_title,
     g.expires_at, g.kind, g.reason, g.created_at
    from public.kompas_access_grants g join public.profiles p on p.id=g.user_id
    join public.courses c on c.id=g.course_id left join public.modules m on m.id=g.module_id
    where g.revoked_at is null and (g.expires_at is null or g.expires_at>now())) x),'[]'::jsonb),
  'pending', coalesce((select jsonb_agg(to_jsonb(y) order by y.created_at desc) from (
    select q.id, q.email, c.slug as course_slug, c.title as course_title, m.order_index as module_index,
     m.title as module_title, q.expires_at, q.kind, q.reason, q.created_at
    from public.kompas_pending_grants q join public.courses c on c.id=q.course_id
    left join public.modules m on m.id=q.module_id
    where q.claimed_at is null and q.cancelled_at is null and (q.expires_at is null or q.expires_at>now())) y),'[]'::jsonb)
 );
end; $$;
revoke all on function public.kompas_admin_list_grants() from public,anon;
grant execute on function public.kompas_admin_list_grants() to authenticated;

-- Bitta faol ruxsatni bekor qilish (p_kind: 'grant' yoki 'pending').
create or replace function public.kompas_admin_revoke_access(p_kind text, p_id uuid, p_reason text)
returns jsonb language plpgsql security definer set search_path=public,pg_temp as $$
declare v_actor uuid:=auth.uid(); v_target uuid; v_email text; v_n int;
begin
 if v_actor is null or not (public.fn_is_admin() or public.kompas_staff_can('users.manage')) then
  raise exception 'ACCESS_DENIED' using errcode='42501'; end if;
 if p_reason is null or length(trim(p_reason))<3 or length(p_reason)>400 then raise exception 'REASON_REQUIRED'; end if;
 if p_kind='grant' then
  select user_id into v_target from public.kompas_access_grants where id=p_id and revoked_at is null for update;
  if v_target is null then raise exception 'NOT_FOUND'; end if;
  perform public.kompas_check_staff_target(v_target);
  update public.kompas_access_grants set revoked_at=now() where id=p_id and revoked_at is null;
 elsif p_kind='pending' then
  update public.kompas_pending_grants set cancelled_at=now()
   where id=p_id and claimed_at is null and cancelled_at is null returning email into v_email;
  get diagnostics v_n = row_count;
  if v_n=0 then raise exception 'NOT_FOUND'; end if;
 else raise exception 'INVALID_KIND'; end if;
 insert into public.kompas_admin_audit(actor_id,target_id,action,detail)
 values(v_actor,v_target,'revoke_access',jsonb_build_object('kind',p_kind,'id',p_id,'email',v_email,'reason',p_reason));
 return jsonb_build_object('ok',true);
end; $$;
revoke all on function public.kompas_admin_revoke_access(text,uuid,text) from public,anon;
grant execute on function public.kompas_admin_revoke_access(text,uuid,text) to authenticated;

-- Email tasdiqlangach kutilayotgan ruxsatlar faollashadi (tasdiqlanmagan email ruxsat olmaydi).
-- Nomi "zz_" bilan: bir hodisada trg_create_profile dan keyin ishlaydi.
create or replace function public.fn_claim_pending_grants() returns trigger
language plpgsql security definer set search_path=public,pg_temp as $$
declare r public.kompas_pending_grants%rowtype;
begin
 if new.email is null or new.email_confirmed_at is null then return new; end if;
 if not exists(select 1 from public.profiles where id=new.id) then return new; end if;
 for r in select * from public.kompas_pending_grants
   where email=lower(new.email) and claimed_at is null and cancelled_at is null for update loop
  if r.expires_at is not null and r.expires_at<=now() then
   update public.kompas_pending_grants set cancelled_at=now() where id=r.id;
  else
   insert into public.kompas_access_grants(user_id,course_id,module_id,expires_at,reason,granted_by,kind)
   values(new.id,r.course_id,r.module_id,r.expires_at,r.reason||' (email boʻyicha oldindan berilgan)',r.granted_by,r.kind);
   update public.kompas_pending_grants set claimed_at=now() where id=r.id;
   insert into public.kompas_admin_audit(actor_id,target_id,action,detail)
   values(r.granted_by,new.id,'pending_grant_claimed',jsonb_build_object('pending_id',r.id,'course_id',r.course_id,'module_id',r.module_id,'kind',r.kind));
  end if;
 end loop;
 return new;
end; $$;
revoke all on function public.fn_claim_pending_grants() from public,anon,authenticated;
drop trigger if exists zz_claim_pending_grants on auth.users;
create trigger zz_claim_pending_grants after insert or update of email_confirmed_at on auth.users
 for each row when (new.email_confirmed_at is not null) execute function public.fn_claim_pending_grants();
