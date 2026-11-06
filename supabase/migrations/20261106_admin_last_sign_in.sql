-- Admin: foydalanuvchilarning oxirgi kirish vaqti (auth.users.last_sign_in_at).
-- Faqat oʻqiydi; faqat admin (fn_is_admin) chaqira oladi, anon/public yopiq.
create or replace function public.kompas_admin_last_sign_ins()
returns table (user_id uuid, last_sign_in_at timestamptz)
language plpgsql
stable
security definer
set search_path = public, auth, pg_temp
as $$
begin
  if not public.fn_is_admin() then
    raise exception 'Ruxsat yoʻq' using errcode = '42501';
  end if;
  return query select u.id, u.last_sign_in_at from auth.users u;
end;
$$;

revoke all on function public.kompas_admin_last_sign_ins() from public, anon;
grant execute on function public.kompas_admin_last_sign_ins() to authenticated;
