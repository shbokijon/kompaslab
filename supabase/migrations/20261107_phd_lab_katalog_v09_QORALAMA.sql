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
    ('Qiziqishdan savolga', 'Savolda toʻrt narsa boʻlsin: nima oʻrganiladi, qayerda, nima nomaʼlum va javob nimada koʻrinadi.', 1),
    ('Adabiyot qidirish', 'Har qidiruv daftarga yoziladi: baza, soʻrov, sana va filtr. Natijada 12 manbali jadval boʻladi.', 2),
    ('Tadqiqot boʻshligʻini koʻrsatish', 'Boʻshliqning turi aytilgan va kamida ikkita manba bilan cheklangan boʻlsa, unga ishonish mumkin.', 3),
    ('Savol, maqsad, vazifa va gipoteza', 'Bitta maqsad, 2–3 ta vazifa, har birining natijasi oʻlchanadi. Gipoteza faqat uni rad etsa boʻladigan holda qoʻyiladi.', 4),
    ('Reja amalga oshadimi', 'Har resurs yoniga yozing: bor, soʻraladi yoki yoʻq. Asosiy va zaxira usul boʻlsa, reja ishlaydi.', 5),
    ('Ikki betlik yoʻnalish bayoni', 'Yaxshi bayonni 90 soniyada ogʻzaki aytib berish mumkin va unda “qanday isbotlayman” savoliga javob bor.', 6)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M2. Doktorantura tizimlari va universitet tanlash', 'Artefakt: Saralangan roʻyxat va teskari kalendar.', 2, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = false, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Toʻrtta PhD modeli', 'Avval modelni aniqlang: ariza kimga, rahbar qachon tanlanadi, moliya qaysi bosqichda hal boʻladi.', 1),
    ('Imkoniyat qidirish', '4 ta rasmiy manba, aniq soʻrovlar va har eʼlon yonida tekshirilgan sana: shu tartib har yili qayta ishlaydi.', 2),
    ('Universitet va laboratoriya muhiti', 'Har mezon uchun rasmiy dalil yozing: maqola, uskuna sahifasi, guruh roʻyxati. Reytingni qoʻshimcha maʼlumot sifatida koʻring.', 3),
    ('Talablar va rasmiy shartlar', 'Har majburiy talab uchun javobingiz yoki rasmiy manba boʻlsin. Tushunarsiz talab qabul boʻlimiga savol boʻlib ketadi.', 4),
    ('Muddatlar va teskari kalendar', 'Har ariza uchun tashqi muddat, 2 ta ichki nazorat sanasi va 7 kunlik zaxira yoziladi.', 5),
    ('Tanlov va zaxira reja', '4 ta asosiy ariza, har biri uchun bitta murosa (trade-off) va keyingi yil uchun zaxira reja.', 6)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M3. Ilmiy rahbar va laboratoriya bilan aloqa', 'Artefakt: Rahbar kartalari va aloqalar daftari.', 3, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = false, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Ilmiy rahbarni qayerdan topish', '12 ta nom toping, 6 tasiga karta yozing va har biri yangi doktorant olishini tekshiring.', 1),
    ('Rahbar mosligini baholash', 'Jadval nimani bilmasligingizni koʻrsatadi. Xat va suhbat shu boʻshliqlarni toʻldiradi.', 2),
    ('Birinchi xat tuzilmasi', 'Qisqa xat: bitta real ish, bitta aniq savol, bitta dalil va bitta aniq soʻrov.', 3),
    ('Portfolio va ilovalar', 'Ilovalar kam va aniq: CV, bayon va tekshirsa boʻladigan bitta dalil.', 4),
    ('Eslatma xat va muloqot odobi', 'Bitta xat, bitta eslatma, keyin boshqa yoʻl. Hammasi sana bilan aloqalar daftariga yoziladi.', 5),
    ('Rahbar bilan suhbat', 'Suhbatga 90 soniyalik bayon va 6 ta savol bilan kiring, keyin yozma xulosa yuboring.', 6),
    ('Ikkinchi rahbar va yordam tizimi', 'Jamoangizni chizib chiqing: rahbar, ikkinchi rahbar, talabalar xizmatlari va muammo chiqqanda kimga borish.', 7)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M4. Ilmiy loyiha taklifi va metodologiya', 'Artefakt: Ilmiy loyiha taklifi (Research Proposal).', 4, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = false, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Taklif nima uchun kerak', 'Avval dastur talabini oʻqing: taklif kerakmi, necha soʻz, qaysi boʻlimlar va qanday baholanadi.', 1),
    ('Fon va ahamiyat', 'Fon qismida boʻshliq adabiyotning oʻzidan kelib chiqadi; ahamiyat bitta aniq jumlada yoziladi.', 2),
    ('Tadqiqot savoli va vazifalar', 'Bitta savol, 3 ta vazifa va har biri uchun kutilgan dalil. Kutilmagan natija ham javob boʻla oladi.', 3),
    ('Usul va tekshiruv', 'Usul: maʼlumot, taqqoslash nuqtasi, tekshiruv va noaniqlik. Taqqoslash nuqtasi boʻlmasa, yangi usulning foydasini koʻrsatib boʻlmaydi.', 4),
    ('Ish rejasi va natijalar', 'Gantt jadvalida bosqichlar, ularning natijasi va kechikish uchun zaxira bor; muddat dastur davomiyligiga mos.', 5),
    ('Etika, maʼlumot va ochiqlik', '8 bandlik etika tekshiruvi va qisqa maʼlumot rejasi taklifga ishonch qoʻshadi.', 6),
    ('Tahrir va baholash mezoni', 'v1 → mezon boʻyicha 5 ta zaif joy → v2 → v3 → dastur shakli. Har versiya saqlanadi.', 7)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M5. Akademik profil va ariza hujjatlari', 'Artefakt: Akademik hujjatlar toʻplami.', 5, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = false, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Akademik CV', 'Har CV bandi: nima qildim, qaysi usul bilan, qanday natija chiqdi va buni qayerdan tekshirsa boʻladi.', 1),
    ('Tadqiqot portfeli va kod', 'Bitta toza, ishga tushadigan va maxfiy maʼlumotsiz omborxona tartibsiz oʻnta fayldan foydaliroq.', 2),
    ('Tavsiya beruvchilar', 'Tavsiya beruvchi ishingizni koʻrgan odam boʻlsin; unga faktlar varaqasi va aniq muddat bering.', 3),
    ('Maqsad bayonnomasi va tadqiqot bayoni', 'Bayonnoma qilgan ishingiz va undan olgan saboqqa tayanadi va har laboratoriyaga alohida moslanadi.', 4),
    ('Transkript va rasmiy hujjatlar', 'Har ariza uchun hujjat, format, fayl nomi va holat jadvali boʻlsin; bir-biriga bogʻliq muddatlar alohida belgilanadi.', 5),
    ('Sunʼiy intellekt va akademik halollik', 'Arizadagi har jumlani intervyuda dalil bilan himoya qila olsangiz, hujjat haqiqatan sizniki.', 6)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M6. Moliya, doktorlik oʻrni va moliyaviy qaror', 'Artefakt: Moliya taqqoslash va 12 oylik pul oqimi.', 6, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = false, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Moliyalashtirish turlari', 'Har paketni qismlarga ajrating va har biriga belgi qoʻying: yozma tasdiqlangan, shartli yoki nomaʼlum.', 1),
    ('Buyuk Britaniyada doktorlik oʻrinlari', 'Buyuk Britaniyada asosiy savol: xalqaro toʻlov farqini kim toʻlaydi? Javob yozma boʻlishi kerak.', 2),
    ('Yevropa: maoshli PhD va MSCA', 'Maoshli PhD da soliqdan oldingi va qoʻlga tegadigan summa, soliq va shartnoma muddati alohida tekshiriladi.', 3),
    ('Xarajatlar va dastlabki pul', 'Uch holat (eng kam, kutilgan, qiyin) va bir martalik xarajatlar bilan dastlabki 60 kunlik naqd pul hisoblanadi.', 4),
    ('Taklif shartlarini oʻqish', 'Har tushunarsiz band uchun savol yozing va yozma javobni saqlang.', 5),
    ('Moliyaviy qaror', 'Eng yomon holat hisoblangan va zaxira reja yozilgan boʻlsa, qaror asosli.', 6)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M7. Ariza, intervyu va qaror', 'Artefakt: Arizalar roʻyxati, intervyu savollari va qaror jadvali.', 7, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = false, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Topshirishdan oldingi tekshiruv', '12 bandli tekshiruv, ochib koʻrilgan PDF lar va saqlangan tasdiq: shundan keyingina ariza yuborilgan hisoblanadi.', 1),
    ('Tavsiya va portalni kuzatish', 'Har tavsiya beruvchining holati, bitta odobli eslatma va zaxira yoʻl yozib qoʻyiladi.', 2),
    ('Ilmiy intervyu', 'Savollar toʻplami va ikki marta yozib olingan mashq intervyusi usuldagi zaif joylarni koʻrsatadi.', 3),
    ('Taqdimot va qiyin savollar', '5 ta slayd, 5 ta qarshi savol va har biriga dalil qayergacha yetishini aytadigan javob.', 4),
    ('Taklif, kutish roʻyxati va rad javobi', 'Har taklif uchun shartlar jadvali va muddat; rad javobi uchun 30 kunlik reja.', 5),
    ('Yakuniy qaror', '4 mezonli qaror xati, hal boʻlmagan xavflar va keyingi qadamlar: qabul qilish, kechiktirish yoki rad etish.', 6)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M8. Qabuldan keyingi tayyorgarlik va birinchi 90 kun', 'Artefakt: Joʻnash oldi nazorat roʻyxati va 90 kunlik reja.', 8, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = false, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Taklif shartlarini bajarish', 'Har shart uchun kim bajarishi, qachongacha va bajarilganini koʻrsatadigan hujjat yoziladi.', 1),
    ('Viza, ATAS va immigratsiya', 'Viza va ATAS talabini rasmiy sahifadan tekshiring; ATAS uchun rejada kamida 6 hafta qoldiring.', 2),
    ('Turar joy, xavfsizlik va dastlabki xarajat', '60 kunlik naqd pul rejasi, 3 ta ishonchli yordam aloqasi va oʻqib chiqilgan ijara shartnomasi.', 3),
    ('Tadqiqotni boshlash', 'Boshlash roʻyxati, birinchi uchrashuv rejasi va oʻquv talablari birinchi oyning asosini tashkil qiladi.', 4),
    ('90 kunlik ish tartibi', '30, 60 va 90 kunlik bosqichlar natijasi bilan yoziladi va haftalik yozuv bilan kuzatiladi.', 5),
    ('Karyera va foydali tadqiqot', '3 yillik koʻnikmalar rejasi va 2 ta karyera yoʻli; birinchi 90 kunda bitta koʻnikma tanlanadi.', 6)) as x(t, d, o);
end $$;
insert into public.course_phases(course_slug, phase, track, module_indexes) values
 ('phd-lab',1,'','{1,2}'),('phd-lab',2,'','{3,4}'),('phd-lab',3,'','{5,6}'),('phd-lab',4,'','{7,8}')
on conflict (course_slug, phase, track) do update set module_indexes = excluded.module_indexes;
-- tekshiruv: M1–M8 = 50 dars; bazadagi M0 da 5 dars (saytda 6), total_lessons trigger faqat published darslarni sanaydi
select c.total_lessons, (select count(*) from public.modules m where m.course_id = c.id) modullar from public.courses c where c.slug = 'phd-lab';
commit;
