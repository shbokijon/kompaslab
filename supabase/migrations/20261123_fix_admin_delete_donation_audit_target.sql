-- Fix donation deletion audit target: target_id references profiles(id), not donations(id).
create or replace function public.fn_admin_delete_donation(
  p_donation_id uuid,
  p_reason text
)
returns jsonb
language plpgsql
security definer
set search_path = public, auth, pg_temp
as $function$
declare
  v_actor uuid := auth.uid();
  v_donation public.donations%rowtype;
begin
  if not public.fn_is_admin() then
    raise exception 'Ruxsat yoʻq' using errcode = '42501';
  end if;

  if p_donation_id is null then
    raise exception 'Donat ID majburiy';
  end if;

  if p_reason is null or char_length(btrim(p_reason)) < 3 or char_length(btrim(p_reason)) > 300 then
    raise exception 'Sabab 3–300 belgi oraligʻida boʻlishi kerak';
  end if;

  select * into v_donation
  from public.donations
  where id = p_donation_id
  for update;

  if not found then
    raise exception 'Donat topilmadi';
  end if;

  if v_donation.status = 'paid' then
    raise exception 'Toʻlangan donatni oʻchirish bloklangan. Moliyaviy tarix saqlanishi kerak.';
  end if;

  insert into public.kompas_admin_audit (actor_id, target_id, action, detail)
  values (
    v_actor,
    null,
    'delete_donation',
    jsonb_build_object(
      'donation_id', v_donation.id,
      'order_no', v_donation.order_no,
      'amount', v_donation.amount,
      'status', v_donation.status,
      'user_id', v_donation.user_id,
      'provider_trans_id', v_donation.provider_trans_id,
      'provider_state', v_donation.provider_state,
      'receipt_no', v_donation.receipt_no,
      'created_at', v_donation.created_at,
      'paid_at', v_donation.paid_at,
      'reason', btrim(p_reason)
    )
  );

  delete from public.donations where id = v_donation.id;

  return jsonb_build_object(
    'deleted', true,
    'donation_id', v_donation.id,
    'order_no', v_donation.order_no
  );
end;
$function$;

revoke all on function public.fn_admin_delete_donation(uuid, text) from public, anon;
grant execute on function public.fn_admin_delete_donation(uuid, text) to authenticated;
