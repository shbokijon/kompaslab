-- Admin-only deletion for test payment rows.
-- Linked enrollments are reset to pending; installment-linked payments are blocked.
create or replace function public.fn_admin_delete_payment(
  p_payment_id uuid,
  p_reason text
)
returns jsonb
language plpgsql
security definer
set search_path = public, auth, pg_temp
as $$
declare
  v_actor uuid := auth.uid();
  v_payment public.payments%rowtype;
  v_reset_enrollments integer := 0;
begin
  if not public.fn_is_admin() then
    raise exception 'Ruxsat yoʻq' using errcode = '42501';
  end if;
  if p_payment_id is null then
    raise exception 'Toʻlov ID majburiy';
  end if;
  if p_reason is null or char_length(btrim(p_reason)) < 3 or char_length(btrim(p_reason)) > 300 then
    raise exception 'Sabab 3–300 belgi oraligʻida boʻlishi kerak';
  end if;

  select * into v_payment from public.payments where id = p_payment_id for update;
  if not found then raise exception 'Toʻlov topilmadi'; end if;

  if v_payment.installment_item_id is not null
     or exists (select 1 from public.installment_items where payment_id = v_payment.id) then
    raise exception 'Bu toʻlov boʻlib toʻlash jadvaliga bogʻlangan. Uni alohida installment amali orqali tuzating.';
  end if;

  update public.enrollments
     set payment_status = 'pending',
         payment_id = null,
         enrolled_at = null,
         expires_at = null,
         unlocked_modules = 0,
         frozen_at = null,
         phase = null,
         track = null,
         updated_at = now()
   where payment_id = v_payment.id;
  get diagnostics v_reset_enrollments = row_count;

  insert into public.kompas_admin_audit (actor_id, target_id, action, detail)
  values (
    v_actor, null, 'delete_payment',
    jsonb_build_object(
      'payment_id', v_payment.id,
      'user_id', v_payment.user_id,
      'course_id', v_payment.course_id,
      'amount', v_payment.amount,
      'status', v_payment.status,
      'method', v_payment.method,
      'kind', v_payment.kind,
      'ref_no', v_payment.ref_no,
      'receipt_no', v_payment.receipt_no,
      'reason', btrim(p_reason),
      'reset_enrollments', v_reset_enrollments
    )
  );

  delete from public.payments where id = v_payment.id;
  return jsonb_build_object('deleted', true, 'payment_id', v_payment.id, 'reset_enrollments', v_reset_enrollments);
end;
$$;

revoke all on function public.fn_admin_delete_payment(uuid, text) from public, anon;
grant execute on function public.fn_admin_delete_payment(uuid, text) to authenticated;

comment on function public.fn_admin_delete_payment(uuid, text)
is 'Admin-only hard delete for test payments; records audit and resets a directly linked enrollment. Installment payments are blocked.';
