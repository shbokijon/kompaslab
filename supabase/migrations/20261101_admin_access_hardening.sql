-- Follow-up hardening, retains existing enrollment and payment semantics.
create or replace function public.fn_is_admin() returns boolean
language sql stable security definer set search_path=public,pg_temp as $$
 select auth.uid() is not null and exists (
  select 1 from public.profiles p where p.id=auth.uid() and p.role='admin'
 );
$$;
-- Manual grants are included in dashboard summaries, but exact module access is
-- still decided by kompas_my_module_access() and fn_paid_page() independently.
create or replace function public.fn_my_access(p_course_slug text) returns jsonb
language plpgsql stable security definer set search_path=public,pg_temp as $$
declare
 v_user uuid:=auth.uid(); v_c public.courses%rowtype;
 v_e public.enrollments%rowtype; v_i public.installments%rowtype;
 v_mods int; v_granted int; v_global boolean; v_paid boolean; v_manual boolean;
begin
 select * into v_c from public.courses where slug=p_course_slug;
 if not found then raise exception 'COURSE_NOT_FOUND'; end if;
 select count(*) into v_mods from public.modules where course_id=v_c.id;
 if v_user is null or not public.kompas_account_active() then
  return jsonb_build_object('access',false,'level','none','total_modules',v_mods,'unlocked_modules',0);
 end if;
 select exists(select 1 from public.kompas_access_grants g
   where g.user_id=v_user and g.course_id=v_c.id and g.module_id is null
    and g.revoked_at is null and (g.expires_at is null or g.expires_at>now())) into v_global;
 select count(distinct g.module_id) into v_granted from public.kompas_access_grants g
   where g.user_id=v_user and g.course_id=v_c.id and g.module_id is not null
    and g.revoked_at is null and (g.expires_at is null or g.expires_at>now());
 v_manual:=v_global or v_granted>0;
 select * into v_e from public.enrollments
   where user_id=v_user and course_id=v_c.id;
 if not found then
  return jsonb_build_object('access',v_manual,'level',case when v_manual then 'manual' else 'none' end,
   'total_modules',v_mods,'unlocked_modules',case when v_global then v_mods else v_granted end,
   'manual_grants',v_granted,'manual_all_modules',v_global);
 end if;
 v_paid:=v_e.payment_status in ('paid','partial') and v_e.frozen_at is null
   and (v_e.expires_at is null or v_e.expires_at>now());
 if v_e.installment_id is not null then
  select * into v_i from public.installments where id=v_e.installment_id;
 end if;
 return jsonb_build_object(
  'access',v_paid or v_manual,
  'level',case when v_paid and v_e.payment_status='paid' then 'full'
    when v_paid then 'partial' when v_manual then 'manual' else 'none' end,
  'frozen',v_e.frozen_at is not null,'expires_at',v_e.expires_at,
  'total_modules',v_mods,
  'unlocked_modules',case when v_paid then coalesce(v_e.unlocked_modules,v_mods)
    when v_global then v_mods else v_granted end,
  'manual_grants',v_granted,'manual_all_modules',v_global,
  'installment',case when v_i.id is null then null else jsonb_build_object(
    'installment_id',v_i.id,'status',v_i.status,'total_amount',v_i.total_amount,
    'paid_amount',v_i.paid_amount,'remaining',v_i.total_amount-v_i.paid_amount,
    'next_due',(select jsonb_build_object('seq',it.seq,'amount',it.amount,'due_date',it.due_date)
      from public.installment_items it
      where it.installment_id=v_i.id and it.status in ('pending','overdue')
      order by it.seq limit 1)) end
 );
end; $$;
create table if not exists public.kompas_deletion_requests(
 user_id uuid primary key references public.profiles(id) on delete cascade,
 requested_by uuid not null references public.profiles(id),
 reason text not null,
 status text not null default 'pending' check (status in ('pending','reviewed','completed','cancelled')),
 created_at timestamptz not null default now(),
 updated_at timestamptz not null default now()
);
alter table public.kompas_deletion_requests enable row level security;
revoke all on public.kompas_deletion_requests from public,anon,authenticated;
grant select on public.kompas_deletion_requests to authenticated;
drop policy if exists kompas_deletion_read on public.kompas_deletion_requests;
create policy kompas_deletion_read on public.kompas_deletion_requests
 for select to authenticated using(public.fn_is_admin() or user_id=auth.uid());
-- This creates a review request; it NEVER deletes the Auth record or financial evidence.
create or replace function public.kompas_admin_request_deletion(p_target uuid,p_reason text)
returns jsonb language plpgsql security definer set search_path=public,pg_temp as $$
declare v_actor uuid:=auth.uid();v_role text;
begin
 if not public.fn_is_admin() then raise exception 'SUPER_ADMIN_REQUIRED' using errcode='42501'; end if;
 if p_reason is null or length(trim(p_reason))<8 or length(p_reason)>400 then raise exception 'REASON_REQUIRED'; end if;
 select role::text into v_role from public.profiles where id=p_target for update;
 if not found then raise exception 'USER_NOT_FOUND'; end if;
 if v_actor=p_target or v_role='admin' then raise exception 'PROTECTED_ACCOUNT' using errcode='42501';end if;
 insert into public.kompas_deletion_requests(user_id,requested_by,reason)
 values(p_target,v_actor,p_reason)
 on conflict(user_id) do update set requested_by=excluded.requested_by,reason=excluded.reason,
  status='pending',updated_at=now();
 insert into public.kompas_account_state(user_id,status,reason,changed_by)
 values(p_target,'suspended','Deletion review pending: '||p_reason,v_actor)
 on conflict(user_id) do update set status='suspended',reason=excluded.reason,
  changed_by=v_actor,changed_at=now();
 insert into public.kompas_admin_audit(actor_id,target_id,action,detail)
 values(v_actor,p_target,'request_deletion',jsonb_build_object('reason',p_reason,'hard_deleted',false));
 return jsonb_build_object('ok',true,'status','pending','hard_deleted',false);
end; $$;
revoke all on function public.kompas_admin_request_deletion(uuid,text) from public,anon;
grant execute on function public.kompas_admin_request_deletion(uuid,text) to authenticated;
