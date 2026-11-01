-- Suspend staff privileges immediately, even if an access token remains valid.
create or replace function public.kompas_staff_can(p_scope text) returns boolean
language sql stable security definer set search_path=public,pg_temp as $$
 select auth.uid() is not null and
   not exists(select 1 from public.kompas_account_state s
     where s.user_id=auth.uid() and s.status <> 'active')
   and (
     public.fn_is_admin() or exists (
       select 1 from public.kompas_staff_roles r
       where r.user_id=auth.uid() and r.active
       and ((r.role='support' and p_scope in ('users.read','users.manage','audit.read'))
         or (r.role='content' and p_scope in ('content.read','content.manage'))
         or (r.role='finance' and p_scope in ('payments.read','audit.read'))))
   );
$$;
