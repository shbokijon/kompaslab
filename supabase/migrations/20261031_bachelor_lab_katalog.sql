-- 2026-10-31 · Bachelor Lab katalogi saytdagi tuzilma bilan: M0 (bepul) + M1–M16 = 17 modul, 86 dars (tools/landing/mods.json).
-- order_index = modul raqami = paid_pages.module_index (bachelor-lab-o.html?m=N).
-- Eski 8 qoralama modul (0–7, darslarsiz) oʻchirilmaydi: nomi va tavsifi yangilanadi (on conflict), 8–16 qoʻshiladi.
-- Oylik obuna: 1 toʻlov = 1 faza = 4 modul (I M1–M4, II M5–M8, III M9–M12, IV M13–M16); webhook unlocked_modules ni +4 qiladi
-- (M0 = 1-oʻrin, faza k → 1+4k). fn_paid_page() pozitsiya bilan tekshiradi, Bachelor tartibi chiziqli, shuning uchun mos.

begin;

do $$
declare
  v_course uuid;
  v_mod uuid;
begin
  select id into v_course from public.courses where slug = 'bachelor-lab';
  if v_course is null then raise exception 'bachelor-lab topilmadi'; end if;
  if exists (select 1 from public.lessons l join public.modules m on m.id = l.module_id where m.course_id = v_course) then
    raise exception 'bachelor-lab da darslar bor: toʻxtatildi';
  end if;
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M0. Qaror darvozasi', 'Artefakt: Tayyorgarlik koʻrsatkichi + shaxsiy boshlash sanasi + rozilik qaydi (18 yoshgacha — ota-ona tasdigʻi bilan).', 0, true, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, true, 'published' from (values
    ('Bachelor Lab qanday ishlaydi', 'Fazalar, artefaktlar, haftalik yuklama; nima beriladi, nima berilmaydi', 1),
    ('Xalqaro bakalavr qabuli — umumiy manzara', 'Mamlakatlar, qabul mantiqlari, raqobat; raqamlar faqat rasmiy manbadan', 2),
    ('Tayyorgarlik diagnostikasi', '6 yoʻnalish boʻyicha baholash (2.5)', 3),
    ('Bachelor Lab sizga mos emas, agar…', 'Ochiq roʻyxat; muqobil yoʻllar', 4),
    ('Vaqt chizigʻi, toʻlov va rozilik', 'Birinchi muddatdan orqaga hisoblangan boshlash sanasi; obuna shartlari toʻliq matnda; ota-ona tasdigʻi', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M1. Qabul qanday qaror qabul qiladi', 'Artefakt: 3 universitetning rasmiy talablari jadvali va qabul modeli belgisi.', 1, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Qabul komissiyasi qanday ishlaydi', 'Kim oʻqiydi, nimani koʻradi, qaror qanday chiqadi', 1),
    ('Yaxlit va ball asosidagi qabul', 'Ikki mantiq; qaysi mamlakatda qaysi biri; universitet modelini rasmiy sahifa va AQShda Common Data Set orqali aniqlash; vaqtni ball yoki hikoyaga taqsimlash', 2),
    ('Mamlakatlar boʻyicha kirish talablari', '11 yillik maktab attestati xorijda qanday baholanadi: UK tayyorlov yili (foundation year), Germaniyada Studienkolleg, AQShda toʻgʻridan-toʻgʻri kirish; har biri rasmiy manbadan tekshiriladi', 3),
    ('Reyting tuzogʻi', 'Umumiy va fan boʻyicha reyting; reyting nimani koʻrsatmaydi', 4),
    ('QS, THE va US News''ni oʻqish', 'Metodologiya farqi, koʻrsatkichlar, cheklovlar', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M2. Universitet tanlash va ariza portfeli', 'Artefakt: Saralangan roʻyxat v1.0 — 8–12 universitet (daraja, talab, xarajat, stipendiya imkoniyati, qabul modeli).', 2, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Uch darajali roʻyxat', 'Orzu, moʻljal, ishonchli darajalar; har darajada nechta', 1),
    ('Moslik tahlili', 'Dastur tarkibi, laboratoriyalar, shahar, iqlim, xavfsizlik, xarajat', 2),
    ('Anʼanaviy yoʻnalishlar', 'AQSh, Buyuk Britaniya, Germaniya, Koreya, Yaponiya: tizim, til, xarajat mantigʻi', 3),
    ('Boshqa yoʻnalishlar', 'Xitoy, Italiya, Vengriya, Turkiya, Singapur', 4),
    ('Ariza portfeli', '8–12 universitetni xavf boʻyicha muvozanatlash; har ariza narxini hisobga olish', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M3. Yoʻnalish va akademik kimlik', 'Artefakt: Qiziqish sohasi bayoni (1 sahifa) + bir jumlali profil.', 3, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Men kim sifatida ariza beryapman', 'Fanlar, loyihalar, qiziqishlardan profil', 1),
    ('Fizika, muhandislik, informatika — real farq', 'Oʻqish tarkibi, ish turi, keyingi yoʻllar; STEM ichida tanlash', 2),
    ('Mutaxassislik va keyingi yoʻl', 'Bakalavrdan keyingi variantlar umumiy koʻrinishda (tafsilot Master Lab''da)', 3),
    ('Qiziqish sohasi bayoni', 'Keng qiziqishdan aniq savolga; dalil bilan', 4),
    ('Izchil hikoya', 'Fanlar, faoliyat va insho bitta yoʻnalishni koʻrsatishi', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M4. Muddatlar arxitekturasi va ish tizimi', 'Artefakt: Asosiy nazorat jadvali + teskari Gantt jadvali + Strategik hujjat v1.0.', 4, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Ariza oynalari', 'Erta qaror (ED), erta ariza (EA), oddiy muddat (RD), UCAS muddatlari, toʻgʻridan-toʻgʻri portallar; sanalar faqat Qobiq sahifasidan', 1),
    ('Teskari reja', 'Muddatdan orqaga: testlar, tavsiyalar, tarjimalar, insholar', 2),
    ('Asosiy nazorat jadvali', 'Har universitet: holat, muddat, hujjatlar, toʻlov, natija', 3),
    ('Maktab bilan muvozanat', 'Haftalik ritm, imtihon davrlari, dam olish; haftasiga 3–5 soat', 4),
    ('I faza sintezi', 'Kim, qayerga, qachon, qanday moliyalashtirish bilan', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M5. Baholar va testlar', 'Artefakt: Test kalendari + baholar jadvali (universitet talablari bilan solishtirilgan).', 5, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Attestat baholarini taqdim etish', 'Baholash shkalasini tushuntirish; universitetlar oʻzi qanday qayta hisoblaydi; oʻzboshimchalik bilan "GPA" toʻqimaslik', 1),
    ('Transkript va attestat', 'Qanday hujjat, kim beradi, tarjima va tasdiq', 2),
    ('Ingliz tili testi strategiyasi', 'IELTS, TOEFL, Duolingo English Test: qaysi universitet qaysini qabul qiladi; qayta topshirish', 3),
    ('SAT va ACT', 'Kimga kerak; tayyorgarlik vaqti; topshirish joyi', 4),
    ('Test talabi siyosatlari', 'Talab qilinadi, ixtiyoriy, hisobga olinmaydi; siyosat har yili oʻzgarishi mumkin, rasmiy sahifadan tekshirish', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M6. Yutuqlar, CV va hujjatlar', 'Artefakt: Bakalavr CV v1.0 (1–2 sahifa) + hujjatlar nazorat roʻyxati.', 6, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Olimpiadalar va tanlovlar', 'Qaysi darajalar signal beradi; natijani toʻgʻri yozish', 1),
    ('Onlayn kurslar va sertifikatlar', 'Qachon foydali, qachon shovqin', 2),
    ('Maktab yoshida ilmiy loyiha', 'Mavzu topish, ustoz topish, natijani hujjatlash', 3),
    ('Bakalavr CV (STAR usuli)', 'Vaziyat, Vazifa, Harakat, Natija; 1–2 sahifa', 4),
    ('Tarjima, notarius, apostil', 'Oʻzbekistonda hujjatlarni tayyorlash tartibi; qaysi mamlakat nima talab qiladi', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M7. Darsdan tashqari faoliyat', 'Artefakt: Faoliyatlar roʻyxati (10 yozuv, qisqa tavsif bilan) + izchil hikoya xaritasi.', 7, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Nima darsdan tashqari faoliyat hisoblanadi', 'Toʻgarak, sport, ish, oilaviy majburiyat, loyiha, koʻngillilik', 1),
    ('STEM uchun kuchli faoliyatlar', 'Chuqurlik va davomiylik; kenglikdan ustunligi', 2),
    ('Ijtimoiy faoliyat va yetakchilik', 'Natija bilan koʻrsatish', 3),
    ('Yozgi dasturlar', 'Tanlovli va pullik dasturlar farqi; pullik dastur oʻzi signal emas', 4),
    ('Faoliyatlar roʻyxatini yozish', 'Qisqa, feʼl bilan boshlanadigan, raqamli tavsiflar; Common App formatiga moslash', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M8. Tavsiya xatlari', 'Artefakt: Yutuqlar varaqasi + 2–3 tavsiya soʻrovi + Aloqalar jadvali.', 8, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Kuchli tavsiya xati', 'Kuzatilgan dalil, aniq epizodlar; kuchsiz va kuchli xat', 1),
    ('Oʻqituvchidan soʻrash', 'Kimdan, qachon (muddatdan 6–8 hafta oldin), qanday; ingliz tilida xat kerak boʻlsa nima qilish', 2),
    ('Yutuqlar varaqasi', 'Oʻqituvchiga beriladigan faktlar va epizodlar', 3),
    ('Platformalarda tavsiya jarayoni', 'Common App (maktab hisoboti, maslahatchi va oʻqituvchi baholari), UCAS tavsiyasi, toʻgʻridan-toʻgʻri portallar', 4),
    ('Maktab maslahatchisi boʻlmasa', 'Oʻzbekiston maktablarida bu rolni kim bajaradi; maktabni qanday tayyorlash', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M9. Shaxsiy bayonot va insholar', 'Artefakt: Asosiy insho qoralamasi v1 (Common App) + UCAS shaxsiy bayonoti qoralamasi v1 (kerak boʻlsa) + qoʻshimcha insholar rejasi.', 9, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Shaxsiy bayonot nima', 'Insho, shaxsiy bayonot va motivatsion xat farqi; qaysi platforma qaysi birini soʻraydi', 1),
    ('Common App asosiy inshosi', 'Yettita mavzu varianti; 250–650 soʻz; mavzu emas, hikoya muhim (manba)', 2),
    ('Hikoya topish va birinchi qoralama', 'Kichik epizoddan katta maʼnoga; "koʻrsat, aytma" tamoyili', 3),
    ('UCAS shaxsiy bayonoti', '2026-yil qabulidan boshlab uchta savol, har biri kamida 350 belgi, jami 4 000 belgigacha (QUB); bitta bayonot barcha UK tanlovlariga boradi', 4),
    ('Qoʻshimcha insholar', '"Nega aynan biz?", "Nega bu mutaxassislik?" — universitet manbalari bilan aniq javob', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M10. Insho tahriri va yakuniy versiya', 'Artefakt: Yakuniy insholar + tahrir qaydi (v1 → yakuniy).', 10, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Uch bosqichli tahrir', 'Mazmun → tuzilma → til', 1),
    ('Klishelar va ortiqcha soʻzlar', '"Bolaligimdan…" boshlanishi, maqtov, mavhum iboralar', 2),
    ('Oʻzaro tahrir', 'Kimga koʻrsatish, qanday fikr soʻrash, qaysi fikrni qabul qilish', 3),
    ('AI davrida insho', 'Universitet va UCAS qoidalari; fikr va tekshiruv uchun foydalanish va matn yozdirish farqi; oʻxshashlik tekshiruvlari', 4),
    ('Yakuniy versiya', 'Soʻz/belgi chegarasi, fayl, platformaga joylash', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M11. Davlat stipendiyalari', 'Artefakt: Stipendiya roʻyxati (5–8 dastur, muvofiqlik tekshiruvi va rasmiy havolalar bilan).', 11, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Stipendiyalar manzarasi', 'Davlat, universitet, xalqaro tashkilot; toʻliq va qisman; muvofiqlik shartlarini oʻqish', 1),
    ('Koreya va Yaponiya', 'GKS va MEXT bakalavriat yoʻnalishlari — umumiy mantiq va GKS Lab, MEXT Lab''ga havola', 2),
    ('Xitoy hukumati stipendiyasi (CSC)', 'Ariza kanallari, hujjatlar, universitet tanlash', 3),
    ('Vengriya va Italiya', 'Stipendium Hungaricum; Italiyadagi mintaqaviy taʼlim huquqi stipendiyalari (DSU) — ehtiyojga asoslangan', 4),
    ('Turkiya va boshqalar', 'Türkiye Bursları; boshqa dasturlarni muvofiqlik mezoni bilan tekshirish', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M12. Universitet grantlari va moliyaviy reja', 'Artefakt: 4 yillik moliyaviy reja (xarajat, qoplanadigan qism, boʻshliq, zaxira manba).', 12, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('AQSh moliyaviy yordami', 'Ehtiyojga asoslangan yordam, toʻlov qobiliyatiga qaramaydigan (need-blind) va qaraydigan (need-aware) siyosatlar, CSS Profile; xalqaro talabalarga qaysi universitet yordam beradi — rasmiy sahifadan', 1),
    ('Universitet stipendiyalari', 'Avtomatik va ariza bilan beriladigan grantlar; ularni qidirish usuli', 2),
    ('Toʻliq xarajat modeli', 'Oʻqish toʻlovi, yashash, sugʻurta, viza, yoʻl, ariza toʻlovlari, yashirin xarajatlar', 3),
    ('4 yillik moliyaviy reja', 'Har yil uchun manba va boʻshliq; valyuta xavfi; zaxira', 4),
    ('Firibgarlikdan himoya', 'Soxta stipendiyalar, "kafolatli" agentlar, oldindan toʻlov talabi belgilari', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M13. Ariza platformalari', 'Artefakt: Kamida bitta topshirilgan ariza + 40 bandli topshirish oldi nazorat roʻyxati.', 13, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Common App', 'Boʻlimlar, universitetga xos qism, toʻlov va undan ozod qilish', 1),
    ('UCAS', 'Tanlovlar soni, bayonot, tavsiya, kuzatuv', 2),
    ('Toʻgʻridan-toʻgʻri portallar', 'uni-assist (Germaniya), Universitaly (Italiya), CSC portali, universitet portallari', 3),
    ('Amaliy topshirish', 'Hujjat yuklash, fayl nomi, tasdiq xati, keyingi kuzatuv', 4),
    ('Topshirish oldi tekshiruv', '40 bandli nazorat roʻyxati', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M14. Mintaqaviy yoʻnalishlar: Xitoy, Italiya, Singapur', 'Artefakt: Tanlangan yoʻnalish boʻyicha ariza paketi.', 14, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Xitoyda STEM universitetlari', 'Universitetlar xaritasi, til (ingliz yoki xitoy), dasturlar', 1),
    ('Xitoyga ariza va motivatsion xat', 'CSC va universitet ariza bosqichlari; xat formati', 2),
    ('Italiyada STEM', 'Politexnika universitetlari, ingliz tilidagi dasturlar, kirish testlari', 3),
    ('Italiyaga ariza va viza', 'Universitaly orqali oldindan roʻyxatdan oʻtish, talaba vizasi bosqichlari', 4),
    ('Singapur universitetlari', 'NUS va NTU: talablar, raqobat', 5),
    ('Singapurga ariza strategiyasi', 'Hujjatlar, testlar, insholar, moliyaviy yordam', 6)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M15. Intervyu va qabul qarori', 'Artefakt: 3 ta yozib olingan javob + mezon bali.', 15, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Intervyu turlari', 'Bitiruvchi bilan suhbat, akademik intervyu, stipendiya intervyusi; onlayn texnika', 1),
    ('"Oʻzingiz haqingizda" — 3 daqiqa', 'Tuzilma va misol tahlili', 2),
    ('Akademik intervyu', 'Masalani ovoz chiqarib yechish, fikrlash jarayonini koʻrsatish', 3),
    ('Oʻz-oʻzini yozib olish va baholash', 'Telefon orqali yozish, 8 bandli mezon, ixtiyoriy moderatsiyali oʻzaro tahrir', 4),
    ('Natijalar: qabul, rad, kutish roʻyxati', 'Bir nechta qabuldan tanlash, kutish roʻyxatida xat, rad javobidan keyingi reja', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M16. Qabuldan keyin: viza va joʻnash', 'Artefakt: Joʻnash oldi nazorat roʻyxati + birinchi yil rejasi.', 16, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Qabul xati: birinchi 2 hafta', 'Shartli va shartsiz qabul, javob muddati, depozit, CAS yoki I-20 kabi hujjatlar', 1),
    ('Talaba vizasi', 'Mamlakat boʻyicha bosqichlar; voyaga yetmaganlar uchun qoʻshimcha talablar boʻlishi mumkin — rasmiy sahifadan', 2),
    ('Uy-joy, sugʻurta va bank', 'Yotoqxona, ijara xavflari, tibbiy sugʻurta talablari, pul oʻtkazish', 3),
    ('Joʻnash oldi tayyorgarlik', '30 kunlik roʻyxat: hujjatlar, dorilar, aloqa, birinchi kun', 4),
    ('Birinchi yil', 'Akademik madaniyat, yordam xizmatlari, ruhiy salomatlik, onlayn ilmiy profil boshlash', 5)) as x(t, d, o);
end $$;

select order_index, title, (select count(*) from public.lessons l where l.module_id = m.id) as darslar
  from public.modules m where course_id = (select id from public.courses where slug = 'bachelor-lab') order by order_index;

commit;
