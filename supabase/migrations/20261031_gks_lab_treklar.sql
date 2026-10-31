-- 2026-10-31 · GKS Lab katalogi saytdagi tuzilma bilan: M0 (bepul) + M1, M2 (umumiy oʻzak)
-- + U/M/D treklari boʻyicha M3–M5 = 12 modul, 54 dars (tools/landing/mods.json).
-- order_index = gks-lab-o.html dagi MODS: M0 0, M1 1, M2 2, M3-U 3, M4-U 4, M5-U 5, M3-M 6, M4-M 7,
-- M5-M 8, M3-D 9, M4-D 10, M5-D 11. paid_pages.module_index ham shu raqam.
-- Eski 6 modul / 20 dars (2026-04 tuzilmasi) oʻchiriladi. 2026-10-31 tekshiruvi: gks-lab uchun
-- enrollments 0, progress 0, notes 0, materials 0, lesson_contents 0 (FK lar cascade).
-- DIQQAT (toʻlovdan oldin hal qilinadi): fn_paid_page() oylik qulfni modul pozitsiyasi bilan tekshiradi
-- (fn_module_position). Trek modullarida pozitsiya ≠ faza (M3-M = 7-oʻrin). Oylik obuna ochilishidan oldin
-- GKS uchun faza = modul raqami (I: M1–M2, II: M3, III: M4, IV: M5) qoidasi serverga yoziladi.
-- 6 oylik va yillikda (unlocked_modules NULL) va admin uchun hozirgi holatda ham toʻgʻri ishlaydi.

begin;

do $$
declare
  v_course uuid;
  v_mod uuid;
begin
  select id into v_course from public.courses where slug = 'gks-lab';
  if v_course is null then raise exception 'gks-lab topilmadi'; end if;
  if exists (select 1 from public.enrollments where course_id = v_course) then
    raise exception 'gks-lab da enrollments bor: eski modullarni oʻchirish toʻxtatildi';
  end if;
  delete from public.modules where course_id = v_course;
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M0. GKS tizimi va qaror darvozasi', 'Artefakt: Muvofiqlik jadvali + tanlangan trek + boshlash sanasi + rozilik qaydi.', 0, true, false) returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, true, 'published' from (values
    ('GKS nima va kimga beriladi', 'NIIED, dastur maqsadi, darajalar (GKS-U, GKS-G), stipendiya tarkibi mantigʻi va majburiyatlar', 1),
    ('Ikki trek va tanlov bosqichlari', 'Elchixona va universitet treki; har bosqichda kim baholaydi', 2),
    ('Muvofiqlik tekshiruvi', 'Fuqarolik, yosh, akademik daraja, baho talabi, sogʻliq, oldingi stipendiyalar; yoʻriqnomani band-band oʻqish', 3),
    ('Trek tanlovi', 'U, M yoki D; elchixona yoki universitet treki — 5 mezon boʻyicha', 4),
    ('Vaqt chizigʻi, toʻlov va rozilik', 'Ariza oynasidan orqaga 8–12 oylik reja; obuna shartlari; Trek U uchun ota-ona tasdigʻi', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M1. Hujjatlar infratuzilmasi', 'Artefakt: Hujjatlar nazorat jadvali + legallashtirish yoʻl xaritasi + til rejasi + tavsiya beruvchilar uchun varaqalar.', 1, false, false) returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Hujjatlarning toʻliq xaritasi', 'Ariza formasi, shaxsiy bayonot, oʻquv rejasi, tavsiya xatlari, diplom va transkript, fuqarolik hujjatlari, sogʻliq formasi, til sertifikati; har birining formati va imzo talabi', 1),
    ('Apostil, tarjima va tasdiq', 'Oʻzbekistonda diplom va transkriptni legallashtirish yoʻli; tarjima talablari; asl nusxa va nusxa; real muddatlar', 2),
    ('Tavsiya xatlari (Core + GKS formasi)', 'Tavsiya beruvchi tanlash, yutuqlar varaqasi; GKS tavsiya formasi talablari va topshirish usuli', 3),
    ('Til strategiyasi: TOPIK va ingliz tili', 'Koreys tili kursi mantigʻi, TOPIK darajalari taʼsiri, ingliz tilidagi dasturlar, sertifikat amal muddati', 4)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M2. Universitet va dastur tanlash', 'Artefakt: 3 ta asoslangan universitet tanlovi + har biri uchun moslik dalilnomasi.', 2, false, false) returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('GKS universitetlari tizimi', 'Yoʻriqnoma ilovalaridagi universitet va dastur roʻyxatlarini oʻqish; universitet turlari (yoʻriqnomadagi A/B kabi guruhlar); kvota, til va yoʻnalish filtrlari', 1),
    ('Saralangan roʻyxat', 'Ilmiy moslik, til talabi, joylashuv, dastur mazmuni; xavf taqsimoti', 2),
    ('Ilmiy moslik', 'Fakultet va laboratoriya sahifalari, professorlarning soʻnggi nashrlari', 3),
    ('Keng tarqalgan xatolar filtri', 'Shablon matn, mubolagʻa, tekshirilmaydigan daʼvo, format xatosi, kech hujjat, mos kelmaydigan yoʻnalish', 4)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M3-U. Nomzod profili', 'Artefakt: Faoliyat vaqt chizigʻi + akademik profil izohi + zaif tomonlar javoblari.', 3, false, false) returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Potensial qanday isbotlanadi', 'Olimpiada, mustaqil loyiha, oʻz-oʻzini oʻqitish, jamoaviy tashabbus; oʻsish traektoriyasi', 1),
    ('Qiziqishning kelib chiqishi', 'Kuzatuv → savol → harakat zanjiri', 2),
    ('Baholarni taqdim etish', 'Oʻzbek baholash tizimini tushuntirish, yoʻriqnomadagi konvertatsiya jadvalidan foydalanish, sinfdagi oʻrin', 3),
    ('Zaif tomonlarni boshqarish', 'Past baho, tanaffus yili, yoʻnalish oʻzgarishi — javobgarlik va tuzatish harakati', 4)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M4-U. Shaxsiy bayonot', 'Artefakt: Yakuniy shaxsiy bayonot (GKS formasi talablariga mos) + tahrir qaydi.', 4, false, false) returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('GKS shaxsiy bayonoti formasi', 'Forma savollari, hajm chegarasi, baholovchi nimani izlaydi', 1),
    ('Kimlik → Dalil → Maqsad → Moslik', 'Toʻrt blok; "nega Koreya, nega shu universitet"', 2),
    ('Birinchi qoralama', 'Skeletdan matnga; umumiy iboralardan qochish', 3),
    ('Tahrir', 'Sifatni faktga almashtirish, mubolagʻani olib tashlash, tekshirib boʻlmaydigan daʼvoni oʻchirish', 4),
    ('Oʻzaro tahrir va yakuniy versiya', 'Mezon boʻyicha baholash, moderatsiyali oʻzaro tahrir', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M5-U. Oʻquv rejasi, topshirish va intervyu', 'Artefakt: Oʻquv rejasi + yigʻilgan paket + intervyu javoblari yozuvi.', 5, false, false) returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Bakalavr oʻquv rejasi', 'Til yili, 1–4-kurs fanlari va koʻnikmalar rejasi, bitiruvdan keyingi yoʻl va uning GKS maqsadiga aloqasi', 1),
    ('Paketni yigʻish va nazorat', 'Fayl nomlari, format, nusxalar, onlayn yuklash; ikkinchi shaxs tekshiruvi', 2),
    ('Intervyu', 'Elchixona intervyusi mantigʻi, keng tarqalgan savollar, qisqa javob tuzilmasi', 3),
    ('Natijadan keyin', 'Bosqich natijalari, universitet qabuli, joʻnash oldi hujjatlar; rad javobidan keyingi reja', 4)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M3-M. Magistratura nomzodining pozitsiyasi', 'Artefakt: STAR inventari + akademik CV v1.0 + yoʻnalish koʻprigi matni (kerak boʻlsa).', 6, false, false) returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Bakalavrdan magistraturaga', '"Oʻqishni xohlayman"dan "nimani oʻrganmoqchiman"ga; bakalavr ishlaridagi takrorlanuvchi mavzu', 1),
    ('Dalillar inventari', 'Kurs ishi, bitiruv ishi, tezis, laboratoriya, dasturiy vositalar — STAR formatida', 2),
    ('Akademik CV (Core)', 'Boʻlimlar tartibi, STAR bandlari, natijani raqam bilan', 3),
    ('Yoʻnalish oʻzgarishini asoslash', 'Eski sohadan olib kelinadigan koʻnikma, toʻldiriladigan boʻshliq, reja', 4)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M4-M. Oʻquv rejasi', 'Artefakt: Yakuniy oʻquv rejasi (GKS formasi boʻyicha) + semestrlar jadvali + 12 manbali annotatsiyalangan roʻyxat.', 7, false, false) returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Nega oʻquv rejasi markaziy hujjat', 'GKS formasidagi savollar, kuchli va kuchsiz reja farqi', 1),
    ('Tadqiqot savolini shakllantirish', 'Mavzudan tor savolga; oʻlchanadigan, javob beriladigan, ahamiyatli; Muammo → Yechim → Yangilik → Taʼsir', 2),
    ('Adabiyot bilan ishlash minimumi', 'Manba qidirish, tez oʻqish tartibi, 10–15 manbali baza, boʻshliqni aniqlash', 3),
    ('Toʻliq oʻquv rejasi', 'Fon → savol → metod → semestrlar boʻyicha reja → natija → uzoq muddatli maqsad', 4),
    ('Tahrir va oʻzaro tahrir', 'Mutaxassis boʻlmagan oʻquvchi tushunadimi; hajm va atamalar', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M5-M. Professor, paket va intervyu', 'Artefakt: Shaxsiy bayonot + 2 professorga xat + izchillik auditi jadvali + 60 soniyalik taqdimot yozuvi.', 8, false, false) returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Professorni tanlash', 'Laboratoriya sahifasi, nashrlar, joriy loyihalar, guruh', 1),
    ('Professorga dastlabki xat (Core)', 'Tuzilma, aniq ishga havola, soʻrov, biriktirma; universitet trekida ayniqsa muhim', 2),
    ('GKS-G shaxsiy bayonoti', 'Forma savollari; oʻquv rejasi bilan takrorlanmaslik', 3),
    ('Izchillik auditi', 'CV, bayonot, oʻquv rejasi va tavsiyalardagi faktlarning mosligi', 4),
    ('Intervyu va keyingi bosqich', '"Nega aynan shu tadqiqot?"; savolni 60 soniyada tushuntirish; rad javobida B reja', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M3-D. Doktorantura nomzodining ilmiy pozitsiyasi', 'Artefakt: Portfel auditi + PhD darajasidagi CV + 3 ta potensial doktorlik savoli.', 9, false, false) returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('PhD nomzodi nimani taklif qiladi', 'Laboratoriyaga keltiriladigan qiymat; magistratura va doktorantura arizasi farqi', 1),
    ('Ilmiy portfel auditi', 'Nashr, konferensiya, preprint, magistrlik ishi, kod va maʼlumotlar', 2),
    ('PhD darajasidagi CV (Core)', 'Nashrlar formati, mualliflik tartibi, metodik koʻnikmalar', 3),
    ('Magistrlik ishidan doktorlik yoʻnalishiga', 'Cheklovlar va javobsiz savollardan kengaytirish', 4)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M4-D. Ilmiy reja', 'Artefakt: GKS formasiga moslangan ilmiy reja (oʻquv rejasi boʻlimi) + 30 manbali baza + 3–4 yillik Gantt jadvali.', 10, false, false) returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Tuzilma: Muammo → Yechim → Yangilik → Taʼsir', 'Bloklar vazifasi va GKS formasi boʻlimlariga joylash', 1),
    ('Muammo va adabiyotdagi boʻshliq', '25–40 manbali baza; boʻshliqni dalil bilan koʻrsatish', 2),
    ('Metodologiya', 'Maʼlumot, usul, vositalar, cheklovlar, xavflar; Koreyadagi laboratoriya resurslari bilan moslik', 3),
    ('Yangilik va taʼsir', 'Yangilik turlari; Oʻzbekiston va Koreya hamkorligi bilan aloqa (dalil bilan)', 4),
    ('Vaqt va resurs rejasi', 'Bosqichlar, nashr va konferensiya rejasi, til kursi yili hisobga olingan', 5),
    ('Tahrir va oʻzaro tahrir', 'Mezon, atama izchilligi, iqtibos uslubi, hajm', 6)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M5-D. Professor bilan muloqot va yakunlash', 'Artefakt: 3 professorga xat va 1 sahifalik reja konspekti + suhbat tayyorgarligi + yakuniy paket.', 11, false, false) returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Professor tahlili va ilmiy xat (Core)', 'Nashr trendi, guruh, sigʻim; maqolaga texnik izoh, hamkorlik nuqtasi', 1),
    ('Onlayn ilmiy suhbat', 'Rejani 5 daqiqada bayon qilish, tanqidga javob, oʻz savollari', 2),
    ('Shaxsiy bayonot va izchillik auditi', 'GKS-G bayonoti; barcha hujjatlarda faktlar mosligi', 3),
    ('Intervyu, natija va joʻnash', 'Intervyu savollari; natijadan keyingi hujjatlar va joʻnash oldi roʻyxat', 4)) as x(t, d, o);
end $$;

select order_index, title, (select count(*) from public.lessons l where l.module_id = m.id) as darslar
  from public.modules m where course_id = (select id from public.courses where slug = 'gks-lab') order by order_index;

commit;
