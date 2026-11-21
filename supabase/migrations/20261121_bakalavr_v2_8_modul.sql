-- 2026-11-21 · Bakalavr dasturi v2: 16 → 8 modul (asoschi tasdigʻi, 2026-11-21). Tahlil: Project hujjati claude/32_Bakalavr_tahlil.md.
-- 1) Eski holat arxivga: modules, lessons, paid_pages (bachelor-lab) nusxasi archive_bachelor_v1_* jadvallarida (oʻchirilmaydi).
-- 2) M1–M8 nomi va tavsifi yangilanadi, darslar mods.json dagi yangi darslar bilan almashtiriladi.
-- 3) M9–M16: paid_pages va modules qatorlari olib tashlanadi (arxivda bor; kirish grantlari 0 ta, obunachi yoʻq).
-- 4) course_phases: 4 bosqich × 2 modul (I M1–M2, II M3–M4, III M5–M6, IV M7–M8).
-- paid_pages M1–M8 yangi HTML i alohida yuklanadi (admin-paid.html yoki paid_upload.py).
begin;

create table if not exists public.archive_bachelor_v1_modules as select m.* from public.modules m join public.courses c on c.id = m.course_id where c.slug = 'bachelor-lab';
create table if not exists public.archive_bachelor_v1_lessons as select l.* from public.lessons l join public.modules m on m.id = l.module_id join public.courses c on c.id = m.course_id where c.slug = 'bachelor-lab';
create table if not exists public.archive_bachelor_v1_paid_pages as select * from public.paid_pages where course_slug = 'bachelor-lab';
create table if not exists public.archive_bachelor_v1_phases as select * from public.course_phases where course_slug = 'bachelor-lab';
alter table public.archive_bachelor_v1_modules enable row level security;
alter table public.archive_bachelor_v1_lessons enable row level security;
alter table public.archive_bachelor_v1_paid_pages enable row level security;
alter table public.archive_bachelor_v1_phases enable row level security;
revoke all on public.archive_bachelor_v1_modules, public.archive_bachelor_v1_lessons, public.archive_bachelor_v1_paid_pages, public.archive_bachelor_v1_phases from anon, authenticated;
comment on table public.archive_bachelor_v1_paid_pages is 'Bakalavr v1 (M1–M16) pullik sahifalari, 2026-11-21 dagi 16 → 8 oʻtishdan oldingi nusxa';

do $$
declare
  v_course uuid;
  v_mod uuid;
begin
  select id into v_course from public.courses where slug = 'bachelor-lab';
  if v_course is null then raise exception 'bachelor-lab topilmadi'; end if;
  if exists (select 1 from public.kompas_access_grants g join public.modules m on m.id = g.module_id where m.course_id = v_course and m.order_index > 8) then
    raise exception 'M9–M16 ga kirish grantlari bor: toʻxtatildi';
  end if;
  delete from public.paid_pages where course_slug = 'bachelor-lab' and module_index > 8;
  delete from public.modules where course_id = v_course and order_index > 8;
  delete from public.lessons l using public.modules m where m.id = l.module_id and m.course_id = v_course and m.order_index between 1 and 8;
  update public.modules set title = 'M1. Qabul mantigʻi va universitet roʻyxati', description = 'Natija: Sizning saralangan roʻyxatingiz: 8–12 universitet, uch daraja va arizalar budjeti.', is_free = false, is_locked = false, updated_at = now()
   where course_id = v_course and order_index = 1 returning id into v_mod;
  if v_mod is null then raise exception 'M1 topilmadi'; end if;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Arizani kim oʻqiydi va qanday qaror qiladi?', 'Avval universitetning qabul modelini aniqlang, keyin vaqtingizni shu model talab qilgan qismga sarflang', 1),
    ('Attestatingiz xorijda', 'Har nishon mamlakat uchun attestat talabini rasmiy manbadan tekshiring va havolasini saqlang', 2),
    ('Reytingni toʻgʻri oʻqish', 'Reyting saralashga yordam beradi, tanlovni esa dastur tarkibi va moslik hal qiladi', 3),
    ('Fizika, muhandislik, informatika: farqi nima?', 'Sohani tanlashdan oldin birinchi kurs oʻquv rejasini oching va shu sohada ishlaydigan odam bilan 15 daqiqa gaplashing', 4),
    ('Soha va mamlakat xaritasi', 'Kam tanlanadigan mamlakatda dastur sifatini soha reytingi, akkreditatsiya va bitiruvchilar qayerga ketishi bilan tekshiring', 5),
    ('Uch darajali roʻyxat va moslik bali', 'Roʻyxatda 2–3 orzu, 3–5 moʻljal va 2–3 ishonchli universitet boʻlsin', 6),
    ('Arizalar budjeti', 'Budjet yetmasa, avval moslik bali eng past universitetni olib tashlang', 7)) as x(t, d, o);
  v_mod := null;
  update public.modules set title = 'M2. Muddatlar va testlar rejasi', description = 'Natija: Sizning vaqt jadvalingiz va test kalendaringiz.', is_free = false, is_locked = false, updated_at = now()
   where course_id = v_course and order_index = 2 returning id into v_mod;
  if v_mod is null then raise exception 'M2 topilmadi'; end if;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Ariza oynalari: ED, EA, RD, UCAS', 'Har sanani universitetning rasmiy sahifasidan oling va yonida manba bilan tekshirilgan kunni yozing', 1),
    ('Baholar va transkript', 'Baholarni asl shkalada, izoh bilan yozing', 2),
    ('Ingliz tili testi', 'Birinchi urinish muddatdan kamida 3–4 oy oldin boʻlsin, qayta topshirishga vaqt qolsin', 3),
    ('SAT, ACT va test siyosati', 'Test siyosatini har yili universitet sahifasidan tekshiring va ixtiyoriy siyosatda qarorni CDS oraligʻi bilan qabul qiling', 4),
    ('Teskari reja va nazorat jadvali', 'Teskari rejani bir marta tuzasiz, nazorat jadvalini esa har hafta bir xil kunda yangilaysiz', 5),
    ('Maktab bilan muvozanat', 'Reja 3 hafta ketma-ket bajarilmasa, rejani qisqartiring: universitetlar sonini yoki qoʻshimcha ishni kamaytiring', 6)) as x(t, d, o);
  v_mod := null;
  update public.modules set title = 'M3. Yutuqlar, faoliyat va CV', description = 'Natija: Sizning 10 ta faoliyat yozuvingiz, CV va hikoya xaritangiz.', is_free = false, is_locked = false, updated_at = now()
   where course_id = v_course and order_index = 3 returning id into v_mod;
  if v_mod is null then raise exception 'M3 topilmadi'; end if;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Men kim sifatida ariza beryapman?', 'Profil soha, sabab va ikkita dalildan iborat', 1),
    ('Nima faoliyat hisoblanadi?', 'Faoliyat ichiga ish va oilaviy majburiyat ham kiradi', 2),
    ('Olimpiada, kurs va loyiha', 'Bitta chuqur va davomli ish oʻn ta qisqa ishdan kuchliroq', 3),
    ('Yetakchilik va yozgi dasturlar', 'Yetakchilikni natija bilan yozing: siz tufayli nima oʻzgardi va buni qanday tasdiqlaysiz?', 4),
    ('Faoliyatlar roʻyxati: 10 yozuv', 'Har tavsif feʼl bilan boshlanadi va raqam yoki natijani koʻrsatadi', 5),
    ('CV: STAR usuli', 'Bakalavr CV da taʼlim va loyihalar birinchi turadi', 6),
    ('Izchil hikoya xaritasi', 'Boʻsh qolgan katak keyingi oylardagi ishingiz', 7)) as x(t, d, o);
  v_mod := null;
  update public.modules set title = 'M4. Tavsiya xatlari va hujjatlar', description = 'Natija: Sizning yutuqlar varaqangiz, aloqalar jadvali va hujjatlar zanjiri.', is_free = false, is_locked = false, updated_at = now()
   where course_id = v_course and order_index = 4 returning id into v_mod;
  if v_mod is null then raise exception 'M4 topilmadi'; end if;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Kuchli tavsiya xati qanday boʻladi?', 'Tavsiyachini lavozimiga qarab tanlamang', 1),
    ('Oʻqituvchidan qanday soʻrash kerak?', 'Oʻqituvchi «oʻzing yozib kel, men imzolayman» desa, rad eting va faktlar varaqasini taklif qiling', 2),
    ('Yutuqlar varaqasi', 'Varaqaga faqat oʻqituvchi tasdiqlay oladigan faktni yozing', 3),
    ('Platformada tavsiya va maktab maslahatchisi', 'Maslahatchi hisobini oʻzingiz ochib toʻldirmang: rasmiy hujjatni maktab vakili yuboradi', 4),
    ('Tarjima, notarius, apostil', 'Har universitet nima soʻrashini aniqlang va zanjirni muddatdan 8–10 hafta oldin boshlang', 5)) as x(t, d, o);
  v_mod := null;
  update public.modules set title = 'M5. Insho: yozish va tahrir', description = 'Natija: Sizning yakuniy inshongiz va tahrir qaydingiz.', is_free = false, is_locked = false, updated_at = now()
   where course_id = v_course and order_index = 5 returning id into v_mod;
  if v_mod is null then raise exception 'M5 topilmadi'; end if;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Shaxsiy bayonot va qiziqish bayoni', 'Bitta matnni hamma platformaga yubormang', 1),
    ('Hikoya va mavzu', 'Avval hikoyani toping, keyin unga mos mavzuni tanlang', 2),
    ('Birinchi qoralama', 'Birinchi qoralamani bir oʻtirishda, tahrirsiz yozing', 3),
    ('UCAS: uch savol', 'UCAS bayonotida qiziqishni dalil bilan koʻrsating: oʻqigan kitob, qilgan tajriba, yechgan masala va undan nima oʻrgandingiz', 4),
    ('Qoʻshimcha insholar: «Nega aynan biz?»', 'Har faktni oʻz soʻzingiz bilan va oʻzingizga bogʻlab yozing', 5),
    ('Tahrir: mazmun, tuzilma, til', 'Har bosqichni alohida oʻtishda bajaring va har yirik oʻzgarishdan keyin yangi versiyani saqlang', 6),
    ('Fikr olish, AI chegarasi va yakuniy versiya', 'AI dan savol va tekshiruv uchun foydalanishingiz mumkin, matnni esa oʻzingiz yozasiz', 7)) as x(t, d, o);
  v_mod := null;
  update public.modules set title = 'M6. Stipendiya va 4 yillik moliyaviy reja', description = 'Natija: Sizning 4 yillik moliyaviy rejangiz va ustuvor stipendiyalar.', is_free = false, is_locked = false, updated_at = now()
   where course_id = v_course and order_index = 6 returning id into v_mod;
  if v_mod is null then raise exception 'M6 topilmadi'; end if;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Stipendiya qayerdan keladi?', 'Avval olti shartni tekshiring', 1),
    ('Davlat stipendiyalari: saralash jadvali', 'Har dasturni muvofiqlik, qoplov, kanal, muddat, raqobat va majburiyat boʻyicha baholang', 2),
    ('Universitet yordami va grantlari', 'Faqat birinchi yilga beriladigan stipendiya 4 yillik rejada katta boʻshliq qoldiradi', 3),
    ('Toʻliq xarajat modeli', 'Hisobni asl valyutada yuriting va 10–15 foiz zaxira qoʻshing', 4),
    ('4 yillik reja', 'Reja boʻshligʻi 0 dan katta yil bilan tugasa, bu universitet hozircha real variant hisoblanmaydi', 5),
    ('Firibgarlikdan himoya', 'Kafolat, oldindan toʻlov, norasmiy email va shoshirish: bittasini koʻrsangiz, toʻlovni toʻxtatib, rasmiy manzil orqali tekshiring', 6)) as x(t, d, o);
  v_mod := null;
  update public.modules set title = 'M7. Topshirish: platformalar va mamlakat yoʻllari', description = 'Natija: Sizning kamida bitta topshirilgan ariza va arizalar jurnalingiz.', is_free = false, is_locked = false, updated_at = now()
   where course_id = v_course and order_index = 7 returning id into v_mod;
  if v_mod is null then raise exception 'M7 topilmadi'; end if;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Common App', 'Toʻlovdan ozod qilishni universitetning oʻzidan soʻring', 1),
    ('UCAS', '5 tanlov bitta fan atrofida boʻlsin: 3 ta informatika va 2 ta fizika bayonotni zaiflashtiradi', 2),
    ('Universitet portallari', 'Login va parolni xavfsiz joyda saqlang, hisob email ini har kuni tekshiring va yoʻriqnomani oxirigacha oʻqing', 3),
    ('Xitoy, Italiya, Singapur: kimga qaysi yoʻl?', 'Yoʻlni sohangizdagi kuchli dastur va uning tili boʻyicha tanlang, keyin bosqichlarni rasmiy sahifadagi sanalar bilan yozing', 4),
    ('Topshirish va oxirgi tekshiruv', 'Muddatdan kamida 3–5 kun oldin topshiring: oxirgi kuni platforma sekinlashadi', 5)) as x(t, d, o);
  v_mod := null;
  update public.modules set title = 'M8. Intervyu, qaror va joʻnash', description = 'Natija: Sizning 3 ta yozib olingan javobingiz, qaror jadvali va joʻnash roʻyxati.', is_free = false, is_locked = false, updated_at = now()
   where course_id = v_course and order_index = 8 returning id into v_mod;
  if v_mod is null then raise exception 'M8 topilmadi'; end if;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Intervyu turlari va «Oʻzingiz haqingizda»', 'Javobda roʻyxat emas, bitta yoʻnalish va dalil boʻlsin', 1),
    ('Akademik intervyu', 'Bilmasangiz, toʻqimang: «Buni bilmayman, lekin shunday oʻylayman …» deb taxminingizni asoslang', 2),
    ('Yozib olish va baholash', 'Ikki urinish balini solishtiring', 3),
    ('Qabul, rad, kutish roʻyxati', 'Qaror mezonlarini va ularning ulushini natijalardan oldin yozing', 4),
    ('Qabul xati va talaba vizasi', 'Birinchi 2 hafta ichida javob bering, depozitni rasmiy kanal orqali toʻlang va viza hujjati uchun talablarni bajaring', 5),
    ('Uy, sugʻurta, joʻnash va birinchi yil', 'Asl hujjatlar qoʻl yukida, skan nusxalar bulutda tursin', 6)) as x(t, d, o);
  v_mod := null;
end $$;

delete from public.course_phases where course_slug = 'bachelor-lab';
insert into public.course_phases (course_slug, phase, track, module_indexes) values
  ('bachelor-lab', 1, '', '{1,2}'), ('bachelor-lab', 2, '', '{3,4}'), ('bachelor-lab', 3, '', '{5,6}'), ('bachelor-lab', 4, '', '{7,8}');

commit;
