-- 2026-11-06: admin paneldan foydalanuvchilarni oʻchirish (spam, sinov emaillari).
-- Faqat admin chaqira oladi (fn_is_admin), anon/public yopiq.
-- Oʻchirilmaydi: adminlar, adminning oʻzi, toʻlangan (paid) toʻlovi yoki boʻlib toʻlash yozuvi bor hisoblar.
-- auth.users oʻchiriladi: profiles va unga boglangan jadvallar ON DELETE CASCADE bilan ketadi,
-- donations va kompas_admin_audit da user_id/target_id NULL boʻladi.
-- Har oʻchirish kompas_admin_audit ga yoziladi (email va ism detail da qoladi).

create or replace function public.fn_admin_delete_users(p_ids uuid[])
returns jsonb
language plpgsql
security definer
set search_path = public, auth, pg_temp
as $$
declare
  v_actor   uuid := auth.uid();
  r         record;
  v_deleted int := 0;
  v_skipped jsonb := '[]'::jsonb;
  v_why     text;
begin
  if not public.fn_is_admin() then
    raise exception 'Ruxsat yoʻq' using errcode = '42501';
  end if;
  if p_ids is null or cardinality(p_ids) = 0 then
    return jsonb_build_object('deleted', 0, 'skipped', v_skipped);
  end if;
  if cardinality(p_ids) > 200 then
    raise exception 'Bir martada 200 tadan koʻp oʻchirib boʻlmaydi';
  end if;

  for r in
    select pr.id, pr.email, pr.role,
           nullif(btrim(concat_ws(' ', pr.first_name, pr.last_name)), '') as nm
    from public.profiles pr
    where pr.id = any (p_ids)
  loop
    v_why := null;
    if r.id = v_actor then
      v_why := 'oʻzingizning hisobingiz';
    elsif r.role = 'admin' then
      v_why := 'admin hisobi';
    elsif exists (select 1 from public.payments where user_id = r.id and status = 'paid') then
      v_why := 'toʻlangan toʻlov yozuvi bor';
    elsif exists (select 1 from public.installments where user_id = r.id) then
      v_why := 'boʻlib toʻlash yozuvi bor';
    end if;

    if v_why is not null then
      v_skipped := v_skipped || jsonb_build_array(
        jsonb_build_object('id', r.id, 'email', r.email, 'reason', v_why));
      continue;
    end if;

    insert into public.kompas_admin_audit (actor_id, target_id, action, detail)
    values (v_actor, r.id, 'delete_user',
            jsonb_build_object('email', r.email, 'name', r.nm));

    delete from auth.users where id = r.id;
    v_deleted := v_deleted + 1;
  end loop;

  return jsonb_build_object('deleted', v_deleted, 'skipped', v_skipped);
end;
$$;

revoke all on function public.fn_admin_delete_users(uuid[]) from public, anon;
grant execute on function public.fn_admin_delete_users(uuid[]) to authenticated;
