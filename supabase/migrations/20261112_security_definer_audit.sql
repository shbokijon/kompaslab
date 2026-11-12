-- SECURITY DEFINER auditi (2026-11-12)
-- HOLAT: TAYYORLANGAN, BAZAGA QOʻLLANMAGAN. Asoschi tasdigʻidan keyin bitta tranzaksiyada qoʻllanadi.
--
-- Audit natijasi (12.11.2026, oddiy talaba hisobi bilan sinaldi: set local role authenticated
-- + request.jwt.claims, fn_is_admin() = false):
--   Admin funksiyalarning hammasi boshida rad etadi (raise, 42501): fn_admin_cancel_installment,
--   fn_admin_confirm_installment_item, fn_admin_delete_users, fn_admin_installments, fn_recount_lessons,
--   fn_set_module_access, fn_upsert_lesson_content, kompas_admin_grant_by_email, kompas_admin_list_grants,
--   kompas_admin_m0_overview, kompas_admin_manage_user, kompas_admin_request_deletion,
--   kompas_admin_revoke_access, kompas_admin_usage, kompas_pwa_stats.
--   Istisno: kompas_admin_user_state rad etmaydi, NULL qaytaradi (maʼlumot chiqmaydi) — 3-band.
--   Topilgan zaiflik: fn_donation_status ref ketma-ket (D1, D2…), anon har donatning holati va
--   summasini koʻra oladi (sinovda D1 = pending 100000, D2 = pending 2000 qaytdi) — 2-band.
--   kompas_track_visit / kompas_pwa_event: tezlik cheklovi yoʻq, tasodifiy visitor_id bilan
--   saytdagi jonli hisobni sunʼiy oshirish mumkin — 4-band.
--
-- Ataylab ochiq qoladi (RLS siyosatlari anon/authenticated nomidan chaqiradi, revoke qilinsa darslar
-- darvozasi buziladi): fn_module_position, kompas_module_permitted, kompas_account_active, fn_is_admin.
-- Ochiq va kerak: kompas_public_stats, fn_create_donation (oʻz cheklovi bor), fn_my_*, fn_paid_page,
-- fn_create_pending_payment, kompas_save_onboarding, kompas_staff_can, fn_tg_link_token.

begin;

-- 1. Boʻlib toʻlash (installment): saytda chaqirilmaydi (rpc qidiruvi 12.11.2026), jadvallar boʻsh
--    (installments = 0). Talaba fn_create_installment orqali on_sale tekshiruvisiz buyurtma ochishi
--    mumkin edi. Hammasi yopiladi; kerak boʻlsa service_role / SQL orqali.
revoke execute on function public.fn_create_installment(text, text, text, public.payment_method) from public, anon, authenticated;
revoke execute on function public.fn_installment_pay_next(uuid, public.payment_method)          from public, anon, authenticated;
revoke execute on function public.fn_installment_quote(text, text, text)                       from public, anon, authenticated;
revoke execute on function public.fn_my_installments()                                         from public, anon, authenticated;
revoke execute on function public.fn_admin_installments(text)                                  from public, anon, authenticated;
revoke execute on function public.fn_admin_cancel_installment(uuid, text)                      from public, anon, authenticated;
revoke execute on function public.fn_admin_confirm_installment_item(uuid, public.payment_method, text) from public, anon, authenticated;

-- 2. Donat holati: ref + maxfiy token. Token buyurtma ochilganda qaytadi, js/donat.js uni
--    localStorage da saqlaydi. Kirgan donor oʻz donatini tokensiz ham koʻradi.
alter table public.donations add column if not exists view_token uuid not null default gen_random_uuid();

drop function if exists public.fn_create_donation(bigint);
create function public.fn_create_donation(p_amount bigint)
returns table(order_ref text, amount bigint, view_token uuid)
language plpgsql security definer set search_path to 'public', 'pg_temp'
as $function$
#variable_conflict use_column
declare v_no bigint; v_tok uuid;
begin
 if p_amount is null or p_amount < 1000 or p_amount > 10000000 then raise exception 'BAD_AMOUNT'; end if;
 if (select count(*) from public.donations d where d.status='pending' and d.created_at > now() - interval '1 minute') >= 30 then
   raise exception 'TOO_MANY_REQUESTS';
 end if;
 v_no := public.fn_next_ref('D','order');
 insert into public.donations(order_no, amount, user_id) values (v_no, p_amount, auth.uid())
 returning donations.view_token into v_tok;
 return query select 'D'||v_no, p_amount, v_tok;
end; $function$;
revoke all on function public.fn_create_donation(bigint) from public;
grant execute on function public.fn_create_donation(bigint) to anon, authenticated;

drop function if exists public.fn_donation_status(text);
create function public.fn_donation_status(p_ref text, p_token uuid default null)
returns table(status text, amount bigint)
language sql stable security definer set search_path to 'public', 'pg_temp'
as $function$
  select d.status, d.amount from public.donations d
  where d.order_no = case when p_ref ~ '^D[0-9]{1,18}$' then substr(p_ref,2)::bigint end
    and ( (p_token is not null and d.view_token = p_token)
       or (auth.uid() is not null and d.user_id = auth.uid()) );
$function$;
revoke all on function public.fn_donation_status(text, uuid) from public;
grant execute on function public.fn_donation_status(text, uuid) to anon, authenticated;

-- 3. kompas_admin_user_state: ruxsatsiz chaqiruv endi xato beradi (NULL emas).
create or replace function public.kompas_admin_user_state(p_target uuid)
returns jsonb
language plpgsql stable security definer set search_path to 'public', 'pg_temp'
as $function$
begin
 if not public.kompas_staff_can('users.read') then
   raise exception 'ACCESS_DENIED' using errcode = '42501';
 end if;
 return jsonb_build_object(
  'status',coalesce((select status from public.kompas_account_state where user_id=p_target),'active'),
  'staff',coalesce((select role from public.kompas_staff_roles where user_id=p_target and active),'student'),
  'grants',coalesce((select jsonb_agg(jsonb_build_object('id',g.id,'course_id',g.course_id,'module_id',g.module_id,'expires_at',g.expires_at,'created_at',g.created_at)) from public.kompas_access_grants g where g.user_id=p_target and g.revoked_at is null and (g.expires_at is null or g.expires_at>now())),'[]'::jsonb)
 );
end; $function$;

-- 4. Jonli hisob spamiga cheklov. Eng yuqori haqiqiy oqim (12.11.2026 gacha): 10 yangi tashrif/daqiqa,
--    128/kun. Chegara: 120 yangi tashrif/daqiqa, 3000 PWA voqeasi/kun. Chegaradan oshganda yozuv
--    jim tashlanadi, hisob qaytaveradi.
create index if not exists site_visits_first_at_idx on public.site_visits (first_at);

create or replace function public.kompas_track_visit(p_vid text)
returns json
language plpgsql security definer set search_path to 'public'
as $function$
declare
  d date := (now() at time zone 'Asia/Tashkent')::date;
  r json;
begin
  if p_vid is not null and p_vid ~ '^[a-z0-9]{8,40}$'
     and (select count(*) from site_visits where first_at > now() - interval '1 minute') < 120 then
    insert into site_visits(visitor_id, visited_on) values (p_vid, d)
    on conflict do nothing;
  end if;
  select json_build_object(
    'day',   count(*) filter (where visited_on = d),
    'week',  count(*) filter (where visited_on >= date_trunc('week', d)::date),
    'month', count(*) filter (where visited_on >= date_trunc('month', d)::date),
    'year',  count(*) filter (where visited_on >= date_trunc('year', d)::date),
    'since', (select min(visited_on) from site_visits)
  ) into r
  from site_visits
  where visited_on >= date_trunc('year', d)::date;
  return r;
end $function$;

create or replace function public.kompas_pwa_event(p_vid text, p_event text, p_platform text default null)
returns void
language plpgsql security definer set search_path to 'public'
as $function$
begin
  if p_vid ~ '^[a-z0-9]{8,40}$' and p_event in ('prompt','installed','standalone')
     and (select count(*) from pwa_events where day = (now() at time zone 'Asia/Tashkent')::date) < 3000 then
    insert into pwa_events(visitor_id, event, platform)
    values (p_vid, p_event, case when p_platform in ('android','ios','desktop') then p_platform end)
    on conflict do nothing;
  end if;
end $function$;

-- 5. Advisor: search_path oʻrnatilmagan funksiyalar (SECURITY DEFINER emas, lekin qoida bir xil).
alter function public.update_updated_at()          set search_path = public, pg_temp;
alter function public.fn_updated_at()              set search_path = public, pg_temp;
alter function public.fn_auto_complete_lesson()    set search_path = public, pg_temp;
alter function public.fn_update_course_stats()     set search_path = public, pg_temp;
alter function public.fn_update_waitlist_count()   set search_path = public, pg_temp;
alter function public.fn_get_course_progress(uuid, uuid) set search_path = public, pg_temp;

commit;

-- Qoʻllangandan keyingi tekshiruv (har biri orqaga qaytariladigan DO blokda):
--   anon: select * from fn_donation_status('D1')                -> 0 qator
--   anon: fn_create_donation(5000) -> token; fn_donation_status(ref, token) -> 1 qator
--   talaba: select kompas_admin_user_state(gen_random_uuid())    -> 42501
--   talaba: select fn_installment_quote('master-lab','x',null)   -> 42501 permission denied
--   get_advisors(security): function_search_path_mutable = 0
