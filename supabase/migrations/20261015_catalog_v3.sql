-- ═══════════════════════════════════════════════════════════════
--  Kompas Lab — katalog v3 migratsiyasi (2026-10-15)
--  Manba: Bachelor Lab v3.0, Master Lab v3.0, GKS Lab v3.0,
--         USA Lab v3.0, Tadbirkor Talaba Lab v1.0, Musofir Lab spetsifikatsiyalari
--
--  Nima qiladi:
--    1. bachelor/master/gks eski modul, dars va dars kontentini
--       archive.catalog_backup_20261015 jadvaliga zaxiralaydi
--    2. courses: obuna narxi ustunlari (oylik/yillik), hisob modeli, spec versiyasi
--    3. modules: track va planned_lessons ustunlari; enrollments: track
--    4. Bachelor, Master, GKS ma'lumotlari spetsifikatsiyaga moslanadi
--    5. usa-lab, tadbirkor-talaba, miggo kurslari qo'shiladi (draft); phd-lab v3.1 narxi (999 000 / 129 000)
--    6. Modul xaritalari spetsifikatsiyadan yoziladi (darslar keyin)
--    7. coming_soon yangilanadi
--
--  Qaytarish: archive.catalog_backup_20261015 dan tiklanadi (pastdagi izoh).
--  Kurs holati o'zgarmaydi: barcha kurslar draft.
-- ═══════════════════════════════════════════════════════════════

begin;

-- ── 1. Zaxira ────────────────────────────────────────────────
create schema if not exists archive;
revoke all on schema archive from anon, authenticated;

create table if not exists archive.catalog_backup_20261015 (
  kind         text not null,          -- 'course' | 'module' | 'lesson' | 'lesson_content'
  course_slug  text not null,
  row_data     jsonb not null,
  backed_up_at timestamptz not null default now()
);

insert into archive.catalog_backup_20261015 (kind, course_slug, row_data)
select 'course', c.slug, to_jsonb(c) from courses c
where c.slug in ('bachelor-lab','master-lab','gks-lab','phd-lab');

insert into archive.catalog_backup_20261015 (kind, course_slug, row_data)
select 'module', c.slug, to_jsonb(m) from modules m join courses c on c.id = m.course_id
where c.slug in ('bachelor-lab','master-lab','gks-lab','phd-lab');

insert into archive.catalog_backup_20261015 (kind, course_slug, row_data)
select 'lesson', c.slug, to_jsonb(l) from lessons l
join modules m on m.id = l.module_id join courses c on c.id = m.course_id
where c.slug in ('bachelor-lab','master-lab','gks-lab','phd-lab');

insert into archive.catalog_backup_20261015 (kind, course_slug, row_data)
select 'lesson_content', c.slug, to_jsonb(lc) from lesson_contents lc
join lessons l on l.id = lc.lesson_id
join modules m on m.id = l.module_id join courses c on c.id = m.course_id
where c.slug in ('bachelor-lab','master-lab','gks-lab','phd-lab');

-- ── 2. Sxema kengaytmalari ───────────────────────────────────
alter table courses add column if not exists price_monthly bigint;
alter table courses add column if not exists price_yearly  bigint;
alter table courses add column if not exists billing_model text
  check (billing_model in ('subscription','one_time','free'));
alter table courses add column if not exists access_months int;
alter table courses add column if not exists spec_version  text;

alter table modules add column if not exists track text not null default 'core'
  check (track in ('core','U','M','D','B','BM','MD','KR','UK','DE','PL'));
alter table modules add column if not exists planned_lessons int;

alter table enrollments add column if not exists track text
  check (track in ('U','M','D','B','KR','UK','DE','PL'));
alter table enrollments add column if not exists track_changed_at timestamptz;

-- ── 3. Mavjud kurslar ────────────────────────────────────────
update courses set
  title = 'Bachelor Lab',
  description = 'Xorijiy bakalavriatga hujjat topshirish: universitet portfeli, testlar, insho, tavsiya xatlari, moliya va topshirish. Natija — oʻquvchining oʻzi tayyorlagan ariza paketi va 4 yillik moliyaviy reja.',
  emoji = '🎓',
  price = 699000, price_starter = 699000, price_scholar = 699000, price_elite = 699000,
  price_monthly = 99000, price_yearly = 699000,
  billing_model = 'subscription', access_months = 12, spec_version = 'v3.0',
  total_modules = 17, total_lessons = 86, updated_at = now()
where slug = 'bachelor-lab';

update courses set
  title = 'Master Lab',
  description = 'Xorijiy magistraturaga hujjat topshirish: ilmiy yoʻnalish, universitet va stipendiya tanlash, akademik CV, tavsiya xatlari, maqsad bayonnomasi, ilmiy loyiha taklifi, intervyu. Natija — toʻliq ariza paketi.',
  emoji = '🔬',
  price = 699000, price_starter = 699000, price_scholar = 699000, price_elite = 699000,
  price_monthly = 99000, price_yearly = 699000,
  billing_model = 'subscription', access_months = 12, spec_version = 'v3.0',
  total_modules = 9, total_lessons = 59, updated_at = now()
where slug = 'master-lab';

update courses set
  title = 'GKS Lab',
  description = 'Global Korea Scholarship: umumiy oʻzak va uchta trek — bakalavriat (GKS-U), magistratura va doktorantura (GKS-G). 54 noyob dars; bitta oʻquvchi umumiy oʻzak va oʻz trekini (26–27 dars) oʻtadi.',
  emoji = '🇰🇷',
  price = 699000, price_starter = 699000, price_scholar = 699000, price_elite = 699000,
  price_monthly = 99000, price_yearly = 699000,
  billing_model = 'subscription', access_months = 12, spec_version = 'v3.0',
  total_modules = 12, total_lessons = 54, updated_at = now()
where slug = 'gks-lab';

update courses set
  title = 'PhD Lab',
  description = 'Xorijdagi moliyalashtirilgan doktoranturaga hujjat topshirish: ilmiy savol, ilmiy rahbar tanlash, professorga xat, ilmiy loyiha taklifi, akademik CV, moliyalashtirish atlasi, intervyu va birinchi yil.',
  emoji = '⚗️',
  price = 999000, price_starter = 999000, price_scholar = 999000, price_elite = 999000,
  price_monthly = 129000, price_yearly = 999000,
  billing_model = 'subscription', access_months = 12, spec_version = 'v3.1',
  total_modules = 9, total_lessons = 65, updated_at = now()
where slug = 'phd-lab';

-- ── 4. Yangi kurslar (draft) ─────────────────────────────────
insert into courses (slug, title, description, emoji, status,
  price, price_starter, price_scholar, price_elite,
  price_monthly, price_yearly, billing_model, access_months, spec_version,
  total_modules, total_lessons)
values
  ('usa-lab', 'USA Lab',
   'AQShda oʻqishning uchta moliyalashtirilgan yoʻli: Global UGRAD almashinuvi (B), Fulbright magistraturasi (M), universitet moliyalashtirgan doktorantura (D). B trek uchun toʻlov UGRAD sikli rasman eʼlon qilingandan keyin qabul qilinadi.',
   '🇺🇸', 'draft', 699000, 699000, 699000, 699000,
   99000, 699000, 'subscription', 12, 'v3.0', 12, 72),
  ('tadbirkor-talaba', 'Tadbirkor Talaba Lab',
   'Universitet talabasi uchun kichik, qonuniy va oʻlchanadigan biznes sinovi: muammo, birinchi mijoz, pul hisobi, huquqiy shakl va soliq. Loyiha maqomida; narx taklif.',
   '💼', 'draft', 299000, 299000, 299000, 299000,
   49000, 299000, 'subscription', 12, 'v1.0', 10, 54),
  ('miggo', 'Musofir Lab',
   'Koreya, Buyuk Britaniya, Germaniya va Polshada faqat rasmiy yoʻllar orqali ishlash va firibgarlikdan himoya. M0 bepul va ochiq; toʻliq kurs loyiha maqomida. Kompas ish topib bermaydi.',
   '🧳', 'draft', 149000, 149000, 149000, 149000,
   null, 149000, 'one_time', 12, 'v1.0', 8, 44)
on conflict (slug) do update set
  title = excluded.title, description = excluded.description, emoji = excluded.emoji,
  price = excluded.price, price_starter = excluded.price_starter,
  price_scholar = excluded.price_scholar, price_elite = excluded.price_elite,
  price_monthly = excluded.price_monthly, price_yearly = excluded.price_yearly,
  billing_model = excluded.billing_model, access_months = excluded.access_months,
  spec_version = excluded.spec_version,
  total_modules = excluded.total_modules, total_lessons = excluded.total_lessons,
  updated_at = now();

-- ── 5. Modul xaritalari ──────────────────────────────────────
-- Eski modullar (va ularga bog'liq darslar, kontent) zaxiradan keyin o'chiriladi.
delete from modules where course_id in (
  select id from courses where slug in ('bachelor-lab','master-lab','gks-lab','phd-lab','usa-lab','tadbirkor-talaba','miggo')
);

insert into modules (course_id, order_index, title, is_free, is_locked, track, planned_lessons)
select c.id, v.ord, v.title, v.ord = 0, v.ord <> 0, v.track, v.n
from courses c
join (values
  -- Bachelor Lab v3.0 — 17 modul, 86 dars
  ('bachelor-lab', 0,  'M0 — Qaror darvozasi', 'core', 5),
  ('bachelor-lab', 1,  'M1 — Qabul qanday qaror qabul qiladi', 'core', 5),
  ('bachelor-lab', 2,  'M2 — Universitet tanlash va ariza portfeli', 'core', 5),
  ('bachelor-lab', 3,  'M3 — Yoʻnalish va akademik kimlik', 'core', 5),
  ('bachelor-lab', 4,  'M4 — Muddatlar arxitekturasi va ish tizimi', 'core', 5),
  ('bachelor-lab', 5,  'M5 — Baholar va testlar', 'core', 5),
  ('bachelor-lab', 6,  'M6 — Yutuqlar, CV va hujjatlar', 'core', 5),
  ('bachelor-lab', 7,  'M7 — Darsdan tashqari faoliyat', 'core', 5),
  ('bachelor-lab', 8,  'M8 — Tavsiya xatlari', 'core', 5),
  ('bachelor-lab', 9,  'M9 — Shaxsiy bayonot va insholar', 'core', 5),
  ('bachelor-lab', 10, 'M10 — Insho tahriri va yakuniy versiya', 'core', 5),
  ('bachelor-lab', 11, 'M11 — Davlat stipendiyalari', 'core', 5),
  ('bachelor-lab', 12, 'M12 — Universitet grantlari va moliyaviy reja', 'core', 5),
  ('bachelor-lab', 13, 'M13 — Ariza platformalari', 'core', 5),
  ('bachelor-lab', 14, 'M14 — Mintaqaviy yoʻnalishlar: Xitoy, Italiya, Singapur', 'core', 6),
  ('bachelor-lab', 15, 'M15 — Intervyu va qabul qarori', 'core', 5),
  ('bachelor-lab', 16, 'M16 — Qabuldan keyin: viza va joʻnash', 'core', 5),
  -- Master Lab v3.0 — 9 modul, 59 dars
  ('master-lab', 0, 'M0 — Qaror darvozasi', 'core', 5),
  ('master-lab', 1, 'M1 — Ilmiy yoʻnalish va universitet tanlash', 'core', 7),
  ('master-lab', 2, 'M2 — Muddatlar arxitekturasi va ish tizimi', 'core', 5),
  ('master-lab', 3, 'M3 — Akademik CV', 'core', 6),
  ('master-lab', 4, 'M4 — Tavsiya xatlari va professor bilan aloqa', 'core', 6),
  ('master-lab', 5, 'M5 — Maqsad bayonnomasi', 'core', 7),
  ('master-lab', 6, 'M6 — Ilmiy loyiha taklifi', 'core', 7),
  ('master-lab', 7, 'M7 — Stipendiyalar atlasi', 'core', 8),
  ('master-lab', 8, 'M8 — Intervyu, qabul va joʻnash', 'core', 8),
  -- GKS Lab v3.0 — umumiy oʻzak + 3 trek, 54 noyob dars
  ('gks-lab', 0,  'M0 — GKS tizimi va qaror darvozasi', 'core', 5),
  ('gks-lab', 1,  'M1 — Hujjatlar infratuzilmasi', 'core', 4),
  ('gks-lab', 2,  'M2 — Universitet va dastur tanlash', 'core', 4),
  ('gks-lab', 3,  'M3-U — Nomzod profili', 'U', 4),
  ('gks-lab', 4,  'M4-U — Shaxsiy bayonot', 'U', 5),
  ('gks-lab', 5,  'M5-U — Oʻquv rejasi, topshirish va intervyu', 'U', 4),
  ('gks-lab', 6,  'M3-M — Magistratura nomzodining pozitsiyasi', 'M', 4),
  ('gks-lab', 7,  'M4-M — Oʻquv rejasi', 'M', 5),
  ('gks-lab', 8,  'M5-M — Professor, paket va intervyu', 'M', 5),
  ('gks-lab', 9,  'M3-D — Doktorantura nomzodining ilmiy pozitsiyasi', 'D', 4),
  ('gks-lab', 10, 'M4-D — Ilmiy reja', 'D', 6),
  ('gks-lab', 11, 'M5-D — Professor bilan muloqot va yakunlash', 'D', 4),
  -- PhD Lab v3.1 — 9 modul, 65 dars
  ('phd-lab', 0, 'M0 — Qaror darvozasi', 'core', 6),
  ('phd-lab', 1, 'M1 — Ilmiy identitet va yoʻnalish', 'core', 6),
  ('phd-lab', 2, 'M2 — Ilmiy rahbar va laboratoriya strategiyasi', 'core', 7),
  ('phd-lab', 3, 'M3 — Professorga yoziladigan dastlabki xat va aloqa', 'core', 7),
  ('phd-lab', 4, 'M4 — Ilmiy loyiha taklifi muhandisligi', 'core', 9),
  ('phd-lab', 5, 'M5 — Ilmiy natijalar: CV, chiqishlar va tavsiya', 'core', 7),
  ('phd-lab', 6, 'M6 — Moliyalashtirish atlasi', 'core', 9),
  ('phd-lab', 7, 'M7 — PhD intervyusi va loyihani himoya qilish', 'core', 6),
  ('phd-lab', 8, 'M8 — Taklif, relokatsiya va PhDʼning birinchi yili', 'core', 8),
  -- USA Lab v3.0 — 12 modul, 72 dars (trek darslar darajasida belgilanadi)
  ('usa-lab', 0,  'M0 — AQSh yoʻllari va qaror darvozasi', 'core', 6),
  ('usa-lab', 1,  'M1 — Trek strategiyasi', 'core', 5),
  ('usa-lab', 2,  'M2 — Muvofiqlik va diskvalifikatsiya sabablari', 'core', 6),
  ('usa-lab', 3,  'M3 — AQSh oliy taʼlimi va pul oqimi', 'core', 6),
  ('usa-lab', 4,  'M4 — Liderlik izi va jamiyatga taʼsir', 'core', 6),
  ('usa-lab', 5,  'M5 — Shaxsiy bayonot', 'core', 7),
  ('usa-lab', 6,  'M6 — Maqsad va tadqiqot bayoni', 'core', 8),
  ('usa-lab', 7,  'M7 — Tavsiya xatlari', 'core', 5),
  ('usa-lab', 8,  'M8 — Joylashtirish va professorlar bilan aloqa', 'core', 7),
  ('usa-lab', 9,  'M9 — Testlar', 'core', 5),
  ('usa-lab', 10, 'M10 — Intervyu', 'core', 6),
  ('usa-lab', 11, 'M11 — Viza, joʻnash va qaytish', 'core', 5),
  -- Tadbirkor Talaba Lab v1.0 — 10 modul, 54 dars
  ('tadbirkor-talaba', 0, 'M0 — Qaror darvozasi', 'core', 5),
  ('tadbirkor-talaba', 1, 'M1 — Muammo topish', 'core', 6),
  ('tadbirkor-talaba', 2, 'M2 — Yechim va MVP', 'core', 6),
  ('tadbirkor-talaba', 3, 'M3 — Birinchi mijozlar va sotuv', 'core', 6),
  ('tadbirkor-talaba', 4, 'M4 — Pul hisobi', 'core', 6),
  ('tadbirkor-talaba', 5, 'M5 — Huquqiy shakl va soliq', 'core', 6),
  ('tadbirkor-talaba', 6, 'M6 — Raqamli infratuzilma', 'core', 5),
  ('tadbirkor-talaba', 7, 'M7 — Moliyalashtirish', 'core', 5),
  ('tadbirkor-talaba', 8, 'M8 — Oʻqish bilan muvozanat', 'core', 5),
  ('tadbirkor-talaba', 9, 'M9 — Yakuniy loyiha', 'core', 4),
  -- Musofir Lab — 8 modul, 44 dars
  ('miggo', 0, 'M0 — Rasmiy yoʻl va firibgarlikdan himoya', 'core', 6),
  ('miggo', 1, 'M1 — Koreya: EPS', 'KR', 7),
  ('miggo', 2, 'M2 — Buyuk Britaniya: mavsumiy ish', 'UK', 6),
  ('miggo', 3, 'M3 — Germaniya', 'DE', 6),
  ('miggo', 4, 'M4 — Polsha', 'PL', 5),
  ('miggo', 5, 'M5 — Hujjatlar va xavfsizlik', 'core', 6),
  ('miggo', 6, 'M6 — Moliya', 'core', 4),
  ('miggo', 7, 'M7 — Hayot va qaytish', 'core', 4)
) as v(slug, ord, title, track, n) on v.slug = c.slug;

-- ── 6. Tez kunda bloki ───────────────────────────────────────
update coming_soon set is_visible = false, updated_at = now() where slug = 'gks-lab';

insert into coming_soon (slug, title, description, emoji, is_visible, launch_date, order_index)
select v.* from (values
  ('tadbirkor-talaba', 'Tadbirkor Talaba Lab',
   'Oʻqishni toʻxtatmasdan kichik, qonuniy biznes sinovi', '💼', true, null::text, 4),
  ('miggo', 'Musofir Lab',
   'Xorijda faqat rasmiy yoʻl bilan ishlash va firibgarlikdan himoya. M0 bepul.', '🧳', true, null::text, 5)
) as v(slug, title, description, emoji, is_visible, launch_date, order_index)
where not exists (select 1 from coming_soon cs where cs.slug = v.slug);

-- ── 7. Tekshiruv ─────────────────────────────────────────────
do $$
declare bad text;
begin
  select string_agg(c.slug || ' (' || c.total_lessons || ' != ' || coalesce(s.n,0) || ')', ', ')
  into bad
  from courses c
  left join (select course_id, sum(planned_lessons) n from modules group by course_id) s on s.course_id = c.id
  where c.slug in ('bachelor-lab','master-lab','gks-lab','phd-lab','usa-lab','tadbirkor-talaba','miggo')
    and c.total_lessons <> coalesce(s.n,0);
  if bad is not null then
    raise exception 'total_lessons mos emas: %', bad;
  end if;
end $$;

commit;

-- ── Qaytarish (kerak bo'lsa) ─────────────────────────────────
-- Modullar va darslarni zaxiradan tiklash:
--   delete from modules where course_id in (select id from courses where slug in ('bachelor-lab','master-lab','gks-lab','phd-lab'));
--   insert into modules  select * from jsonb_populate_recordset(null::modules,
--     (select jsonb_agg(row_data - 'track' - 'planned_lessons') from archive.catalog_backup_20261015 where kind='module'));
--   insert into lessons  select * from jsonb_populate_recordset(null::lessons,
--     (select jsonb_agg(row_data) from archive.catalog_backup_20261015 where kind='lesson'));
--   insert into lesson_contents select * from jsonb_populate_recordset(null::lesson_contents,
--     (select jsonb_agg(row_data) from archive.catalog_backup_20261015 where kind='lesson_content'));
