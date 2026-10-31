-- 2026-10-31 · Narxlar sahifasidagi "Holat" ustuni admin paneldan tahrirlanadi
-- courses.holat: saytda koʻrinadigan qisqa matn (masalan "Tayyor", "Kutish roʻyxati").
-- NULL boʻlsa sahifadagi statik matn qoladi. courses.status (draft/active) bilan aralashtirilmaydi.
-- RLS oʻzgarmaydi: courses UPDATE faqat admin.

alter table public.courses add column if not exists holat text;
alter table public.courses drop constraint if exists courses_holat_len;
alter table public.courses add constraint courses_holat_len check (holat is null or char_length(holat) between 1 and 40);

update public.courses set holat = v.h from (values
  ('bachelor-lab', 'Kutish roʻyxati'), ('master-lab', 'Tayyor'), ('phd-lab', 'Kutish roʻyxati'),
  ('gks-lab', 'Tayyor'), ('usa-lab', 'B trek: sikl kutilmoqda'), ('daad-lab', 'Kutish roʻyxati'),
  ('tadbirkor-talaba', 'Ishlab chiqilmoqda'), ('miggo', 'M0 tayyorlanmoqda')
) as v(s, h) where slug = v.s and holat is null;

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
    'prices', coalesce((select json_object_agg(slug, json_build_object('y', coalesce(price_yearly, price), 'm', price_monthly, 's6', price_6m, 'h', holat)) from courses where slug <> 'test-lab'), '{}'::json),
    'at', now()
  );
$function$;
