-- UTM va kanal oʻlchovi (2026-11-12)
-- HOLAT: TAYYORLANGAN, BAZAGA QOʻLLANMAGAN. Asoschi tasdigʻidan keyin qoʻllanadi.
-- 20261112_security_definer_audit.sql dan KEYIN qoʻllang (kompas_track_visit ning oʻsha versiyasi asos).
--
-- Mijoz tomoni (js/utm.js, js/live-bar.js, register.html) bu migratsiyasiz ham ishlaydi:
--   · roʻyxatdan oʻtishda UTM auth.users.raw_user_meta_data->'utm' ga darhol yoziladi (baza oʻzgarishi kerak emas);
--   · kompas_track_visit(p_vid, p_utm) xato bersa, live-bar.js eski chaqiruvga qaytadi.
-- Bu migratsiya qoʻshadi: site_visits.utm, payments.utm (trigger bilan), admin hisobot funksiyasi.

begin;

-- 1. Tashrif: birinchi kelishdagi kanal
alter table public.site_visits add column if not exists utm jsonb;

drop function if exists public.kompas_track_visit(text);
create function public.kompas_track_visit(p_vid text, p_utm jsonb default null)
returns json
language plpgsql security definer set search_path to 'public'
as $function$
declare
  d date := (now() at time zone 'Asia/Tashkent')::date;
  r json;
  u jsonb;
begin
  -- Faqat maʼlum kalitlar, har biri 60 belgigacha
  if p_utm is not null and jsonb_typeof(p_utm) = 'object' and (p_utm ? 'source') then
    select jsonb_object_agg(k, left(p_utm->>k, 60)) into u
    from unnest(array['source','medium','campaign','content','term','page','at']) k
    where p_utm ? k and jsonb_typeof(p_utm->k) = 'string';
  end if;
  if p_vid is not null and p_vid ~ '^[a-z0-9]{8,40}$'
     and (select count(*) from site_visits where first_at > now() - interval '1 minute') < 120 then
    insert into site_visits(visitor_id, visited_on, utm) values (p_vid, d, u)
    on conflict (visited_on, visitor_id) do update set utm = coalesce(site_visits.utm, excluded.utm);
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
revoke all on function public.kompas_track_visit(text, jsonb) from public;
grant execute on function public.kompas_track_visit(text, jsonb) to anon, authenticated;

-- 2. Toʻlov buyurtmasi: kanal toʻlovchining roʻyxatdan oʻtgandagi UTM idan (fn_create_pending_payment oʻzgarmaydi)
alter table public.payments add column if not exists utm jsonb;

create or replace function public.fn_payment_set_utm()
returns trigger
language plpgsql security definer set search_path to 'public', 'auth', 'pg_temp'
as $function$
begin
  if new.utm is null and new.user_id is not null then
    select u.raw_user_meta_data->'utm' into new.utm from auth.users u where u.id = new.user_id;
  end if;
  return new;
end $function$;
revoke all on function public.fn_payment_set_utm() from public, anon, authenticated;

drop trigger if exists trg_payment_set_utm on public.payments;
create trigger trg_payment_set_utm before insert on public.payments
for each row execute function public.fn_payment_set_utm();

-- 3. Admin hisobot: manba → tashrif → roʻyxatdan oʻtish → M0 boshlash → toʻlov
--    Toʻlov: faqat paid/confirmed, sinov (kind = 'S') kirmaydi.
create or replace function public.kompas_admin_channels(p_days int default 30)
returns jsonb
language plpgsql stable security definer set search_path to 'public', 'auth', 'pg_temp'
as $function$
declare v_from timestamptz := now() - make_interval(days => greatest(1, least(coalesce(p_days, 30), 365)));
begin
  if not public.fn_is_admin() then raise exception 'ACCESS_DENIED' using errcode = '42501'; end if;
  return coalesce((
    with v as (
      select coalesce(utm->>'source', '(belgisiz)') src, count(distinct visitor_id) n
      from site_visits where first_at >= v_from group by 1
    ), u as (
      select au.id, coalesce(au.raw_user_meta_data->'utm'->>'source', '(belgisiz)') src
      from auth.users au where au.created_at >= v_from
    ), r as (
      select src, count(*) n,
             count(*) filter (where exists (select 1 from kompas_m0_events e where e.user_id = u.id)) m0
      from u group by 1
    ), p as (
      select coalesce(pm.utm->>'source', '(belgisiz)') src, count(*) n, sum(pm.amount) s
      from payments pm
      where pm.created_at >= v_from and pm.status in ('paid','confirmed') and coalesce(pm.kind, 'T') <> 'S'
      group by 1
    ), k as (select src from v union select src from r union select src from p)
    select jsonb_agg(jsonb_build_object(
      'source', k.src, 'visits', coalesce(v.n, 0), 'registered', coalesce(r.n, 0),
      'm0_started', coalesce(r.m0, 0), 'paid', coalesce(p.n, 0), 'revenue', coalesce(p.s, 0))
      order by coalesce(p.n, 0) desc, coalesce(r.n, 0) desc, coalesce(v.n, 0) desc)
    from k left join v using (src) left join r using (src) left join p using (src)
  ), '[]'::jsonb);
end $function$;
revoke all on function public.kompas_admin_channels(int) from public, anon;
grant execute on function public.kompas_admin_channels(int) to authenticated;

commit;
