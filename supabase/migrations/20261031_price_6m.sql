-- 2026-10-31 · 6 oylik tarif (Mavsum, 4 oy oʻrniga)
-- courses.price_6m: admin har Lab uchun qoʻlda kiritadi (formula yoʻq).
-- NULL boʻlsa saytda 6 oylik tarif koʻrsatilmaydi.
-- kompas_public_stats().prices[slug] ga 's6' kaliti qoʻshiladi.
-- RLS oʻzgarmaydi: courses UPDATE faqat admin (mavjud policy).

alter table public.courses add column if not exists price_6m bigint;
alter table public.courses drop constraint if exists courses_price_6m_pos;
alter table public.courses add constraint courses_price_6m_pos check (price_6m is null or price_6m > 0);

create or replace function public.kompas_public_stats()
 returns json
 language sql
 stable security definer
 set search_path to 'public'
as $function$
  select json_build_object(
    'registered', (select count(*) from profiles where role is distinct from 'admin'),
    'last_signup', (select max(created_at) from profiles where role is distinct from 'admin'),
    'waitlist', (select count(distinct email) from waitlist),
    'waitlist_by_lab', coalesce((select json_object_agg(course_slug, n) from (select course_slug, count(*) as n from waitlist group by course_slug) t), '{}'::json),
    'prices', coalesce((select json_object_agg(slug, json_build_object('y', coalesce(price_yearly, price), 'm', price_monthly, 's6', price_6m)) from courses where slug <> 'test-lab'), '{}'::json),
    'at', now()
  );
$function$;
