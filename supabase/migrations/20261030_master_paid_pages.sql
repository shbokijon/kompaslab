-- 2026-10-30 · Master Lab: pullik modullarni toʻlov ochilishiga tayyorlash
-- 1) Xavfsizlik: fn_set_module_access anonim chaqiruvchiga ochiq edi (auth.uid() NULL boʻlsa tekshiruv oʻtkazilardi)
-- 2) paid_pages + fn_paid_page(): pullik modul HTML faqat server tekshiruvidan keyin
-- 3) Master kurs tuzilmasi: M0–M8, 59 dars (tools/landing/mods.json bilan bir xil); eski 10 qoralama dars arxivga (oʻchirilmaydi)
-- courses.status oʻzgarmaydi (draft): toʻlov ochilmagan.

begin;

-- ── 1. Xavfsizlik ──
create or replace function public.fn_set_module_access(p_course_slug text, p_module_order integer, p_is_free boolean)
returns integer language plpgsql security definer set search_path = public as $$
declare v_count int;
begin
  if not (coalesce(auth.role(), '') = 'service_role' or public.fn_is_admin()) then
    raise exception 'ADMIN_ONLY' using errcode = '42501';
  end if;
  update lessons l set is_free = p_is_free, updated_at = now()
    from modules m, courses c
   where l.module_id = m.id and m.course_id = c.id and c.slug = p_course_slug and m.order_index = p_module_order;
  get diagnostics v_count = row_count;
  update modules m set is_free = p_is_free, updated_at = now()
    from courses c where m.course_id = c.id and c.slug = p_course_slug and m.order_index = p_module_order;
  return v_count;
end $$;
revoke execute on function public.fn_set_module_access(text, integer, boolean) from public, anon;
grant execute on function public.fn_set_module_access(text, integer, boolean) to authenticated, service_role;

-- ── 2. Pullik sahifalar ──
create table if not exists public.paid_pages (
  course_slug  text    not null,
  module_index integer not null check (module_index >= 1),
  html         text    not null,
  sha256       text    not null,
  version      text    not null,
  updated_at   timestamptz not null default now(),
  primary key (course_slug, module_index)
);
comment on table public.paid_pages is 'Pullik modulning toʻliq HTML sahifasi. Toʻgʻridan-toʻgʻri oʻqish faqat admin; talabaga fn_paid_page() orqali.';
alter table public.paid_pages enable row level security;
drop policy if exists "paid_pages: faqat admin" on public.paid_pages;
create policy "paid_pages: faqat admin" on public.paid_pages for all
  using (public.fn_is_admin()) with check (public.fn_is_admin());
revoke all on public.paid_pages from anon;

create or replace function public.fn_paid_page(p_course_slug text, p_module_index integer)
returns jsonb language plpgsql stable security definer set search_path = public as $$
declare
  v_uid uuid := auth.uid();
  v_course uuid;
  v_mod uuid;
  v_pos int;
  e enrollments%rowtype;
  v_html text;
  v_ver text;
begin
  if v_uid is null then return jsonb_build_object('ok', false, 'reason', 'auth'); end if;
  select id into v_course from courses where slug = p_course_slug;
  if v_course is null then return jsonb_build_object('ok', false, 'reason', 'no_course'); end if;
  select id into v_mod from modules where course_id = v_course and order_index = p_module_index;
  if v_mod is null then return jsonb_build_object('ok', false, 'reason', 'missing'); end if;

  if not public.fn_is_admin() then
    select * into e from enrollments where user_id = v_uid and course_id = v_course;
    if not found or e.payment_status not in ('paid', 'partial') then
      return jsonb_build_object('ok', false, 'reason', 'no_access');
    end if;
    if e.frozen_at is not null then return jsonb_build_object('ok', false, 'reason', 'frozen'); end if;
    if e.expires_at is not null and e.expires_at <= now() then return jsonb_build_object('ok', false, 'reason', 'expired'); end if;
    v_pos := public.fn_module_position(v_mod);
    if e.unlocked_modules is not null and v_pos > e.unlocked_modules then
      return jsonb_build_object('ok', false, 'reason', 'locked', 'unlocked_modules', e.unlocked_modules);
    end if;
  end if;

  select html, version into v_html, v_ver from paid_pages where course_slug = p_course_slug and module_index = p_module_index;
  if v_html is null then return jsonb_build_object('ok', false, 'reason', 'missing'); end if;
  return jsonb_build_object('ok', true, 'html', v_html, 'version', v_ver);
end $$;
revoke execute on function public.fn_paid_page(text, integer) from public, anon;
grant execute on function public.fn_paid_page(text, integer) to authenticated;

-- ── 3. Master kurs tuzilmasi ──
-- eski qoralama darslar: oʻchirilmaydi, arxivga (status draft qoladi, tartib raqami 100+)
update lessons l set order_index = l.order_index + 100,
       title = case when l.title like '[arxiv]%' then l.title else '[arxiv] ' || l.title end
  from modules m
 where l.module_id = m.id and m.course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and l.order_index < 100;

insert into modules (course_id, title, order_index, is_free, is_locked) values ('aaaaaaaa-0003-0000-0000-000000000003', 'M0. Qaror darvozasi', 0, true, false)
  on conflict (course_id, order_index) do update set title = excluded.title, is_free = excluded.is_free, is_locked = false, updated_at = now();
insert into modules (course_id, title, order_index, is_free, is_locked) values ('aaaaaaaa-0003-0000-0000-000000000003', 'M1. Ilmiy yoʻnalish va universitet tanlash', 1, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, is_free = excluded.is_free, is_locked = false, updated_at = now();
insert into modules (course_id, title, order_index, is_free, is_locked) values ('aaaaaaaa-0003-0000-0000-000000000003', 'M2. Muddatlar arxitekturasi va ish tizimi', 2, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, is_free = excluded.is_free, is_locked = false, updated_at = now();
insert into modules (course_id, title, order_index, is_free, is_locked) values ('aaaaaaaa-0003-0000-0000-000000000003', 'M3. Akademik CV', 3, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, is_free = excluded.is_free, is_locked = false, updated_at = now();
insert into modules (course_id, title, order_index, is_free, is_locked) values ('aaaaaaaa-0003-0000-0000-000000000003', 'M4. Tavsiya xatlari va professor bilan aloqa', 4, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, is_free = excluded.is_free, is_locked = false, updated_at = now();
insert into modules (course_id, title, order_index, is_free, is_locked) values ('aaaaaaaa-0003-0000-0000-000000000003', 'M5. Maqsad bayonnomasi', 5, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, is_free = excluded.is_free, is_locked = false, updated_at = now();
insert into modules (course_id, title, order_index, is_free, is_locked) values ('aaaaaaaa-0003-0000-0000-000000000003', 'M6. Ilmiy loyiha taklifi', 6, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, is_free = excluded.is_free, is_locked = false, updated_at = now();
insert into modules (course_id, title, order_index, is_free, is_locked) values ('aaaaaaaa-0003-0000-0000-000000000003', 'M7. Stipendiyalar atlasi', 7, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, is_free = excluded.is_free, is_locked = false, updated_at = now();
insert into modules (course_id, title, order_index, is_free, is_locked) values ('aaaaaaaa-0003-0000-0000-000000000003', 'M8. Viza, intervyu va joʻnash', 8, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, is_free = excluded.is_free, is_locked = false, updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 0.1. Master Lab qanday ishlaydi', 'Fazalar, artefaktlar, haftalik yuklama, nima beriladi va nima berilmaydi', 1, true, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 0
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 0.2. Magistratura dunyosi', 'Oʻquv (taught) va tadqiqot (research) magistraturasi; 1 va 2 yillik dasturlar; mamlakatlar boʻyicha tuzilma farqi', 2, true, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 0
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 0.3. Ariza paketi anatomiyasi', 'Ariza qaysi qismlardan iborat: CV, maqsad bayonnomasi, tavsiya xatlari, transkript, til sertifikati, ilmiy loyiha taklifi (talab qilinsa); komissiya har birida nimani qidiradi', 3, true, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 0
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 0.4. Tayyorgarlik diagnostikasi', '6 yoʻnalish boʻyicha oʻz-oʻzini baholash (2.5-boʻlim)', 4, true, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 0
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 0.5. Qaror: boshlash, kechiktirish yoki boshqa Lab', 'Kimga mos emas roʻyxati; toʻlov va bekor qilish shartlari toʻliq matnda; rozilik', 5, true, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 0
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 1.1. Tadqiqotchi sifatida men kimman', 'Oʻtgan kurslar, loyihalar va qiziqishlardan ilmiy profil chiqarish', 1, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 1
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 1.2. Qiziqish sohasini toraytirish', 'Keng soha → yoʻnalish → aniq savol; "Men energetikaga qiziqaman" va "Men past haroratli geotermal tizimlar modellashtirishga qiziqaman" farqi', 2, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 1
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 1.3. Reytinglarni toʻgʻri oʻqish', 'QS, THE, ARWU qanday hisoblanadi; umumiy va fan boʻyicha reyting farqi; reyting nimani koʻrsatmaydi', 3, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 1
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 1.4. Ilmiy moslik (Research fit)', 'Dastur tarkibi, kafedra, laboratoriya, professorlar ishlari; moslikni dalil bilan koʻrsatish', 4, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 1
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 1.5. Uch darajali saralangan roʻyxat', 'Orzu (Dream), Moʻljal (Target), Ishonchli (Safety) darajalari; har darajada nechta dastur', 5, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 1
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 1.6. Moliyalashtirish turlari', 'Toʻliq stipendiya, qisman grant, universitet chegirmasi, assistentlik, oʻz hisobidan; har birining saralangan roʻyxatga taʼsiri', 6, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 1
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 1.7. Profilning izchil hikoyasi (Coherent narrative)', 'Oʻtmish, hozir va maqsadni bir chiziqqa keltirish; hikoya keyingi barcha hujjatlar uchun asos', 7, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 1
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 2.1. Ariza sikli qanday ishlaydi', 'Universitet muddati va stipendiya muddati ikki alohida sana; stipendiya koʻpincha qabuldan oldin yopiladi; muddatlarni faqat rasmiy sahifadan olish', 1, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 2
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 2.2. Teskari reja', 'Muddatdan orqaga: til sertifikati, tavsiya xatlari, hujjat tarjimasi, yozish bloklari', 2, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 2
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 2.3. Asosiy nazorat jadvali (Master Tracker)', 'Har bir dastur: holat, muddat, hujjatlar, toʻlov, natija', 3, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 2
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 2.4. Parallel ariza portfeli', '3 stipendiya va 6–10 universitetga bir vaqtda; ustma-ust tushgan muddatlarni boshqarish', 4, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 2
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 2.5. I faza sintezi', 'Strategik hujjat: kim, qayerga, qachon, qanday moliyalashtirish bilan', 5, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 2
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 3.1. Akademik CV va ishchi rezyume farqi', 'Hajm, tartib, boʻlimlar; Yevropa, AQSh va Buyuk Britaniya kutganlari; Europass qachon talab qilinadi', 1, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 3
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 3.2. Taʼlim va mukofotlar', 'GPA, baholash shkalasini tushuntirish, tegishli kurslar, olimpiadalar', 2, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 3
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 3.3. Tadqiqot tajribasi va STAR', 'Vaziyat, Vazifa, Harakat, Natija (STAR) usuli; "tajribam yoʻq" muammosi: kurs loyihasi, bitiruv ishi, amaliyot', 3, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 3
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 3.4. Nashrlar, taqdimotlar, loyihalar', 'Iqtibos formati, konferensiya tezislari, GitHub va maʼlumotlar loyihalari', 4, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 3
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 3.5. Koʻnikmalar, tillar, sertifikatlar', 'Texnik koʻnikmalarni dalil bilan yozish; til darajasi (CEFR)', 5, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 3
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 3.6. Tahrir va yakunlash', '3 bosqich: mazmun, tuzilma, imlo; 2 sahifa chegarasi; fayl nomi', 6, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 3
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 4.1. Tavsiya xati anatomiyasi', 'Komissiya xatda nimani qidiradi: kuzatilgan dalil, solishtirma baho, aniq epizodlar', 1, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 4
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 4.2. Kimdan, qachon, qanday soʻrash', 'Akademik va professional tavsiya beruvchi; muddatdan 8 hafta oldin soʻrash; rad etilsa nima qilish', 2, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 4
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 4.3. Yutuqlar varaqasi (Brag Sheet)', '6 boʻlim: kim/qayerga/qachon, aloqa tarixi, nega bu dastur, faktlar, 2–3 STAR epizod, taʼkidlanishi soʻralgan sifatlar', 3, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 4
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 4.4. Professorga dastlabki xat (cold email)', 'Kimga yoziladi; mavzu qatori; 150–200 soʻzlik tuzilma; professor ishini oʻqiganini koʻrsatish; nimalar yozilmaydi', 4, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 4
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 4.5. Javob, qayta yozish va suhbat', 'Javob kelmasa qachon qayta yozish; ijobiy javobdan keyin onlayn suhbatga tayyorlanish', 5, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 4
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 4.6. Aloqalar jadvali (Outreach Log)', 'Tavsiya va xatlarni bitta jadvalda boshqarish: sana, holat, eslatma', 6, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 4
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 5.1. Maqsad bayonnomasi nima', 'SoP, shaxsiy bayonot (Personal Statement) va motivatsion xat farqi; qaysi dastur qaysi birini soʻraydi; soʻz chegarasi va savolli formatlar', 1, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 5
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 5.2. Tuzilma: Kimlik → Dalil → Maqsad → Moslik', 'Toʻrt qismli freymvork; har qismning vazifasi va hajmi', 2, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 5
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 5.3. "Nega aynan shu dastur?"', 'Dastur kurslari, professorlar, laboratoriyalar orqali aniq javob; umumiy maqtov iboralaridan qochish', 3, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 5
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 5.4. Dalil bilan yozish', 'Sifat emas, hodisa: "qiziquvchanman" oʻrniga aniq loyiha va natija; raqamlar', 4, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 5
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 5.5. Birinchi qoralama', 'Yozish tartibi: avval oʻrta qism, keyin kirish; 90 daqiqalik bloklar', 5, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 5
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 5.6. Tahrir', 'Keng tarqalgan xatolar: bolalikdan boshlash, CV''ni qayta aytish, klishe, mavhum maqsad; 3 bosqichli tahrir', 6, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 5
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 5.7. Namuna tahlili', 'Kompas tomonidan tuzilgan oʻquv namunalari (haqiqiy talabalar matni emas): kuchsiz va kuchli versiya tahlili', 7, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 5
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 6.1. Ilmiy loyiha taklifi kimga kerak', 'Tadqiqot magistraturasi, baʼzi stipendiyalar va professorga xat; oʻquv magistraturasida koʻpincha talab qilinmaydi', 1, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 6
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 6.2. Muammo bayoni', 'Global → mintaqaviy → aniq boʻshliq; Muammo → Yechim → Yangilik → Taʼsir freymvorki', 2, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 6
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 6.3. Adabiyotlar sharhi (Literature Review)', 'Manba topish: Google Scholar, Scopus, kutubxona; oʻqish tartibi; iqtibos boshqaruvchi (Zotero)', 3, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 6
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 6.4. Metodologiya', 'Tadqiqot dizayni, maʼlumot, usul, cheklovlar; magistratura miqyosiga mos boʻlishi', 4, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 6
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 6.5. Ish rejasi va Gantt jadvali', 'Vaqt boʻyicha bosqichlar; real hajm', 5, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 6
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 6.6. Kutilayotgan natija va ahamiyati', 'Ilmiy va amaliy hissa; Oʻzbekiston uchun ahamiyat (mavjud boʻlsa, dalil bilan)', 6, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 6
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 6.7. Tahrir, format, iqtibos uslubi', 'APA, IEEE, Harvard uslublari; sahifa va soʻz chegarasi; plagiat va AI vositalaridan foydalanish qoidalari', 7, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 6
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 7.1. Stipendiya turlari va muvofiqlik', 'Davlat, universitet, xalqaro tashkilot dasturlari; muvofiqlik (eligibility) shartlarini oʻqish: fuqarolik, ish tajribasi, qaytish majburiyati', 1, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 7
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 7.2. Buyuk Britaniya', 'Chevening (ish tajribasi talabi, 2 tavsiya beruvchi, qaytish majburiyati), universitet stipendiyalari', 2, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 7
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 7.3. AQSh', 'Fulbright (Oʻzbekistondagi AQSh elchixonasi orqali), universitet moliyalashtirishi va assistentlik', 3, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 7
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 7.4. Yevropa Ittifoqi', 'Erasmus Mundus qoʻshma magistraturalari, milliy dasturlar (masalan, Vengriya Stipendium Hungaricum); Germaniya — qisqa tavsif va DAAD Lab''ga havola', 4, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 7
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 7.5. Osiyo', 'Koreya (GKS) va Yaponiya (MEXT) — qisqa tavsif va tegishli Lablarga havola; Xitoy hukumati stipendiyasi (CSC)', 5, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 7
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 7.6. Turkiya va boshqa yoʻnalishlar', 'Türkiye Bursları; xalqaro tashkilotlar dasturlari (muvofiqlik har yili tekshiriladi)', 6, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 7
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 7.7. Oʻzbekiston dasturlari va universitet grantlari', 'El-yurt umidi jamgʻarmasi; universitetlarning oʻz grantlari va toʻlov chegirmalarini topish usuli', 7, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 7
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 7.8. Stipendiya portfeli', '3 dasturni tanlash mezoni: muvofiqlik, moslik, muddat, raqobat; har biriga SoP moslashtirish rejasi', 8, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 7
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 8.1. Intervyu turlari', 'Motivatsion, panel, ilmiy, texnik; onlayn intervyu texnikasi', 1, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 8
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 8.2. 10 asosiy savol', '"Oʻzingiz haqingizda", "Nega shu dastur", "5 yildan keyin" va boshqalar; STAR asosida javob', 2, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 8
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 8.3. Stipendiya intervyulari', 'Chevening (yetakchilik, tarmoq, maqsad), Fulbright va boshqalar; komissiya mantiqi', 3, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 8
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 8.4. 5 daqiqalik ilmiy taqdimot', 'Muammo, usul, natija, ahamiyat; slaydsiz va slayd bilan', 4, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 8
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 8.5. Oʻz-oʻzini yozib olish va baholash', 'Telefon orqali yozib olish, mezon boʻyicha baholash, ixtiyoriy oʻzaro tahrir', 5, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 8
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 8.6. Qabul xati keldi: birinchi 2 hafta', 'Shartli va shartsiz qabul; javob muddati; depozit; CAS (UK) yoki I-20 (AQSh) kabi hujjatlar nima', 6, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 8
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 8.7. Viza, sugʻurta, uy-joy, bank', 'Talaba vizasi bosqichlari; tibbiy sugʻurta talablari (mamlakatga qarab); yotoqxona va ijara; moliyaviy hujjatlar', 7, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 8
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();
insert into lessons (module_id, title, description, order_index, is_free, status)
  select id, 'Dars 8.8. Birinchi 90 kun va oʻqishdan keyingi yoʻllar', 'Ilmiy rahbar bilan birinchi uchrashuvlar, akademik madaniyat; oʻqishdan keyin ishlash huquqi va qaytish majburiyatlari (mamlakat va stipendiyaga qarab)', 8, false, 'published' from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and order_index = 8
  on conflict (module_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, status = 'published', updated_at = now();

-- total_lessons triggerda faqat published darslarni sanaydi; tekshiruv uchun qoʻlda ham:
update courses set total_lessons = (select count(*) from lessons l join modules m on m.id = l.module_id where m.course_id = 'aaaaaaaa-0003-0000-0000-000000000003' and l.status = 'published'),
                   total_modules = (select count(*) from modules where course_id = 'aaaaaaaa-0003-0000-0000-000000000003'), updated_at = now()
 where id = 'aaaaaaaa-0003-0000-0000-000000000003';

do $$ declare n int; begin
  select total_lessons into n from courses where id = 'aaaaaaaa-0003-0000-0000-000000000003';
  if n <> 59 then raise exception 'Master darslar soni 59 emas: %', n; end if;
end $$;

commit;
