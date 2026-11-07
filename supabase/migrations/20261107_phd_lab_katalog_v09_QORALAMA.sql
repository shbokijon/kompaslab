-- 2026-11-07 · PhD Lab katalogi (v0.9 kontenti → sayt andozasi): M0 (bepul, oʻzgarmaydi) + M1–M8 = 9 modul, 56 dars.
-- QORALAMA: hali qoʻllanmagan. Asoschi tasdigʻi kerak, chunki:
--   1) M1–M9 dagi eski darslar (M1–M8 qayta yoziladi) va M9 moduli oʻchiriladi;
--   2) course_phases 2026-11-07 dagi {1,2,3},{4,5},{6,7},{8,9} oʻrniga {1,2},{3,4},{5,6},{7,8} boʻladi.
-- order_index = modul raqami = paid_pages.module_index (phd-lab-o.html?m=N). on_sale bu faylda oʻzgarmaydi.
begin;
do $$
declare v_course uuid; v_mod uuid;
begin
  select id into v_course from public.courses where slug = 'phd-lab';
  if v_course is null then raise exception 'phd-lab topilmadi'; end if;
  if exists (select 1 from public.enrollments e where e.course_id = v_course) then
    raise exception 'phd-lab da obunalar bor: qoʻlda koʻrib chiqing';
  end if;
  delete from public.lessons where module_id in (select id from public.modules where course_id = v_course and order_index >= 1);
  delete from public.modules where course_id = v_course and order_index >= 9;
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M1. Ilmiy yoʻnalish va tadqiqot savoli', 'Artefakt: Tadqiqot yoʻnalishi bayoni.', 1, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = false, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Qiziqishdan muammoga', 'Mavzu emas, savol kerak: fenomen, joy, boʻshliq va oʻlchanadigan natija aniq boʻlsa, savolga dalil bilan javob berish mumkin.', 1),
    ('Adabiyot izlash strategiyasi', 'Adabiyot qidiruvi qaytarib boʻladigan jarayon: soʻrov, sana va filtr yozilgan jurnal va 12 manbalik jadval.', 2),
    ('Tadqiqot boʻshligʻini isbotlash', 'Boʻshliq turi nomlangan va kamida ikkita manba bilan cheklangan boʻlsa, u daʼvo emas, dalilga aylanadi.', 3),
    ('Savol, maqsad, vazifa va gipoteza', 'Maqsad bitta, vazifalar 2–3 ta va har biri oʻlchanadigan; gipoteza faqat rad etish mumkin boʻlsa qoʻyiladi.', 4),
    ('Bajarilishi mumkinlik va resurslar', 'Har resurs uchun “bor / soʻraladi / yoʻq” holatini yozing; asosiy va zaxira usul boʻlsa, reja bajariladi.', 5),
    ('2 sahifalik yoʻnalish bayoni', 'Yaxshi bayon 90 soniyada aytib beriladi va “qanday isbotlayman” savoliga javob beradi.', 6)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M2. Doktorantura tizimlari va universitet tanlash', 'Artefakt: Saralangan roʻyxat va teskari kalendar.', 2, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = false, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Toʻrtta PhD modeli', 'Avval model aniqlanadi: ariza kimga, rahbar qachon, moliya qaysi bosqichda hal boʻladi.', 1),
    ('Imkoniyat qidirish tizimi', '4 ta rasmiy manba, aniq soʻrovlar va har eʼlon uchun tekshirilgan sana: bu takrorlanadigan qidiruv tizimi.', 2),
    ('Universitet va ilmiy muhit', 'Har mezon uchun rasmiy dalil yozing: maqola, uskuna sahifasi, guruh roʻyxati. Reyting faqat bitta signal.', 3),
    ('Muvofiqlik va rasmiy talablar', 'Har “majburiy” band uchun javob yoki rasmiy manba boʻlsin; nomaʼlum band savolga aylanadi.', 4),
    ('Muddatlar va teskari kalendar', 'Har ariza uchun tashqi muddat, 2 ta ichki nazorat nuqtasi va 7 kunlik zaxira yoziladi.', 5),
    ('Tanlov va B reja', '4 ta ustuvor ariza, har biriga bitta murosa (trade-off) va keyingi sikl uchun B reja.', 6)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M3. Ilmiy rahbar va laboratoriya bilan aloqa', 'Artefakt: Rahbar moslik kartalari va aloqalar jurnali.', 3, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = false, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Ilmiy rahbar topish usullari', '12 ta nom toping, 6 tasiga moslik kartasi yozing; har biri uchun “yangi doktorant oladimi?” savolini tekshiring.', 1),
    ('Rahbar moslik matritsasi', 'Matritsa “nimani bilmayman” degan roʻyxatni beradi; xat va suhbat shu boʻshliqlarni yopadi.', 2),
    ('Birinchi xat tuzilmasi', 'Qisqa xat: bitta real ish, bitta aniq savol, bitta dalil va bitta aniq soʻrov.', 3),
    ('Portfolio va ilovalar', 'Ilovalar kam, aniq va tekshiriladigan: CV, bayon va bitta ochiq dalil.', 4),
    ('Qayta yozish va muloqot odobi', 'Bitta xat, bitta qayta xat, keyin boshqa yoʻl: barchasi aloqalar jurnalida sana bilan.', 5),
    ('Rahbar bilan suhbat', 'Suhbatga 90 soniyalik bayon va 6 ta savol bilan kiring; keyin yozma xulosa yuboring.', 6),
    ('Ikkinchi rahbar va qoʻllab-quvvatlash', 'Jamoa sxemasi: rahbar, ikkinchi rahbar, talaba xizmatlari va muammo chiqqandagi kanal.', 7)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M4. Ilmiy loyiha taklifi va metodologiya', 'Artefakt: Ilmiy loyiha taklifi (Research Proposal).', 4, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = false, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Taklif va uning haqiqiy roli', 'Avval dastur talabini oʻqing: taklif kerakmi, qancha soʻz, qaysi boʻlimlar va qanday baholanadi.', 1),
    ('Fon va ahamiyat', 'Fon qismi boʻshliqni adabiyotning oʻzidan chiqaradi; ahamiyat bitta aniq jumlada.', 2),
    ('Tadqiqot savoli va vazifalar', 'Bitta savol, 3 ta vazifa va har biriga kutilgan dalil: salbiy natija ham javob boʻla oladi.', 3),
    ('Usul va tekshiruv', 'Usul = maʼlumot + asos + tekshiruv + noaniqlik. Asos boʻlmasa, qoʻshimcha qiymatni isbotlab boʻlmaydi.', 4),
    ('Vaqt rejasi va natijalar', 'Gantt jadvali bosqichlar, natijalar va kechikishdagi zaxira bilan; muddat dastur davomiyligiga mos.', 5),
    ('Etika, maʼlumot va ochiqlik', '8 bandlik etika tekshiruvi va qisqa DMP taklifni ishonchli qiladi.', 6),
    ('Tahrir va baholash mezoni', 'v1 → mezon bilan 5 ta zaif joy → v2 → v3 → dastur shakli. Har versiya saqlanadi.', 7)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M5. Akademik profil va ariza hujjatlari', 'Artefakt: Akademik hujjatlar toʻplami.', 5, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = false, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Akademik CV dalil tuzilmasi', 'Har CV bandi: nima qildim, qaysi usul bilan, qanday natija va qayerda tekshirsa boʻladi.', 1),
    ('Tadqiqot portfeli va kod', 'Bitta toza, qayta ishga tushadigan va maxfiy maʼlumotsiz omborxona oʻnta tartibsiz fayldan kuchliroq.', 2),
    ('Tavsiya beruvchilar strategiyasi', 'Tavsiya beruvchi sizning ishingizga guvoh boʻlgan odam; unga faktlar varaqasi va aniq muddat beriladi.', 3),
    ('Maqsad bayonnomasi va tadqiqot bayoni', 'Bayonnoma klishe emas, qilingan ish va undan olingan saboq asosida yoziladi va har laboratoriyaga moslanadi.', 4),
    ('Transkript va rasmiy hujjatlar', 'Har ariza uchun hujjat, format, fayl nomi va holat jadvali; bogʻliq muddatlar alohida belgilanadi.', 5),
    ('Sunʼiy intellekt va akademik halollik', 'Arizadagi har gapni intervyuda dalil bilan himoya qila olsangiz, hujjat sizniki.', 6)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M6. Moliya, doktorlik oʻrni va moliyaviy qaror', 'Artefakt: Moliya taqqoslash va 12 oylik pul oqimi.', 6, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = false, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Moliyalashtirish turlarining farqi', 'Har paketni qismlarga ajrating va har qismga “yozma tasdiqlangan / shartli / nomaʼlum” belgisini qoʻying.', 1),
    ('Buyuk Britaniyada doktorlik oʻrinlari', 'UK da asosiy savol: xalqaro toʻlov farqi kimning zimmasida? Javob yozma boʻlishi kerak.', 2),
    ('Yevropa: maoshli PhD va MSCA', 'Maoshli PhD da yalpi va sof summa, soliq va shartnoma muddati alohida tekshiriladi.', 3),
    ('Xarajatlar va dastlabki pul', 'Uch stsenariy (minimal, kutilgan, qiyin) va bir martalik xarajatlar bilan dastlabki 60 kunlik naqd pul hisoblanadi.', 4),
    ('Taklif shartlarini oʻqish', 'Har noaniq band uchun aniqlik soʻrovi yoziladi va yozma javob saqlanadi.', 5),
    ('Moliyaviy yakuniy qaror', 'Eng yomon stsenariy hisoblangan va B reja yozilgan boʻlsa, qaror asosli.', 6)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M7. Ariza, intervyu va qaror', 'Artefakt: Arizalar reyestri, intervyu banki va qaror jadvali.', 7, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = false, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Topshirishdan oldingi sifat nazorati', '12 bandli nazorat, ochib koʻrilgan PDF lar va saqlangan tasdiq: shundan keyingina ariza “yuborilgan”.', 1),
    ('Tavsiya va portal kuzatuvi', 'Har tavsiya beruvchi uchun holat, bitta xushmuomala eslatma rejasi va zaxira yoʻl.', 2),
    ('Ilmiy intervyu', 'Savollar banki va ikki marta yozib olingan mashq intervyusi zaif usul joylarini ochadi.', 3),
    ('Taqdimot va qiyin savollar', '5 slayd, 5 ta qarshi savol va har biriga dalil chegarasi bilan javob.', 4),
    ('Taklif, kutish roʻyxati va rad javobi', 'Har taklif uchun shartlar matritsasi va muddat; rad javobi uchun 30 kunlik reja.', 5),
    ('Yakuniy qaror', '4 mezonli qaror xati, hal boʻlmagan xavflar va qabul / kechiktirish / rad qadamlari.', 6)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M8. Qabuldan keyingi tayyorgarlik va birinchi 90 kun', 'Artefakt: Joʻnash oldi nazorat roʻyxati va 90 kunlik reja.', 8, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = false, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Taklif shartlarini yopish', 'Har shart uchun egasi, sanasi va yopilganini isbotlaydigan hujjat yoziladi.', 1),
    ('Viza, ATAS va immigratsiya', 'Viza va ATAS talabini rasmiy sahifadan tekshiring va ATAS uchun kamida 6 haftani rejaga qoʻying.', 2),
    ('Uy, xavfsizlik va dastlabki xarajat', '60 kunlik naqd pul rejasi, 3 ta ishonchli yordam aloqasi va oʻqilgan ijara shartnomasi.', 3),
    ('Tadqiqotga kirishish tizimi', 'Kirishish roʻyxati, birinchi uchrashuv kun tartibi va trening talablari: birinchi oyning asosi.', 4),
    ('90 kunlik ilmiy ritm', '30/60/90 bosqichlari natija bilan yoziladi va haftalik jurnal bilan kuzatiladi.', 5),
    ('Karyera va foydali tadqiqot', '3 yillik koʻnikma xaritasi va 2 ta karyera yoʻli: birinchi 90 kunda bitta koʻnikma tanlanadi.', 6)) as x(t, d, o);
end $$;
insert into public.course_phases(course_slug, phase, track, module_indexes) values
 ('phd-lab',1,'','{1,2}'),('phd-lab',2,'','{3,4}'),('phd-lab',3,'','{5,6}'),('phd-lab',4,'','{7,8}')
on conflict (course_slug, phase, track) do update set module_indexes = excluded.module_indexes;
-- tekshiruv: M1–M8 = 50 dars; bazadagi M0 da 5 dars (saytda 6), total_lessons trigger faqat published darslarni sanaydi
select c.total_lessons, (select count(*) from public.modules m where m.course_id = c.id) modullar from public.courses c where c.slug = 'phd-lab';
commit;
