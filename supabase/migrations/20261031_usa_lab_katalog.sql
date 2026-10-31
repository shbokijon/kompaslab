-- 2026-10-31 · USA Lab v4.0 katalogi: M0 (bepul) + M1–M8 = 9 modul, 46 dars (tools/landing/mods.json).
-- order_index = modul raqami = paid_pages.module_index (usa-lab-o.html?m=N).
-- Oylik obuna: 1 toʻlov = 1 faza = 2 modul (I M1–M2, II M3–M4, III M5–M6, IV M7–M8); webhook unlocked_modules ni +2 qiladi (Master kabi).

begin;

do $$
declare
  v_course uuid;
  v_mod uuid;
begin
  select id into v_course from public.courses where slug = 'usa-lab';
  if v_course is null then raise exception 'usa-lab topilmadi'; end if;
  if exists (select 1 from public.lessons l join public.modules m on m.id = l.module_id where m.course_id = v_course) then
    raise exception 'usa-lab da darslar bor: toʻxtatildi';
  end if;
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M0. AQSh yoʻllari va qaror', 'Artefakt: Yoʻllar xaritasi + yoʻl tanlovi + tayyorgarlik koʻrsatkichi + kalendar.', 0, true, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, true, 'published' from (values
    ('AQSh yoʻllari xaritasi', 'Beshta yoʻl: bakalavr (universitet yordami), Global UGRAD, Fulbright, magistratura, PhD; har birining puli va vizasi', 1),
    ('Eng keng tarqalgan miflar', '"Faqat grant bilan", "Fulbright bilan PhD", "UGRAD diplom beradi", "ishlab oʻqish toʻlovini qoplayman"', 2),
    ('Pul haqiqati', 'Federal yordam xalqaro talabaga yopiq; toʻliq yordam beradigan universitetlar kam; oila byudjeti chegarasi', 3),
    ('Yoʻl tanlagich', 'Holatingiz, tajriba, oila byudjeti va rejangiz boʻyicha yoʻl; qizil bayroqlar', 4),
    ('Rasmiy manbalarni oʻqish', '6 savollik oʻqish usuli; faqat universitet va masʼul tashkilot sahifalari', 5),
    ('Tayyorgarlik, kalendar va shartlar', 'Koʻrsatkich, muddatdan orqaga kalendar, obuna shartlari', 6)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M1. AQSh oliy taʼlimi: tizim va universitetni tekshirish', 'Artefakt: Universitet tekshiruv kartasi.', 1, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Universitet turlari', 'Toʻrt tur: ikki yillik kollej, liberal sanʼat kolleji, tadqiqot universiteti, davlat va xususiy', 1),
    ('Akkreditatsiya va SEVP sertifikati', 'Akkreditatsiya (CHEA yoki DAPIP) va SEVP sertifikati (Study in the States) tekshirilmagan muassasa roʻyxatga kirmaydi', 2),
    ('AQSh darajalari qanday tuzilgan', 'Bakalavriatda major koʻpincha keyinroq tanlanadi; magistratura dissertatsiyali yoki dissertatsiyasiz; PhD ga bakalavrdan keyin ham kirish mumkin', 3),
    ('Soha boʻyicha kuchli joyni topish', 'Soha boʻyicha kuchni HERD ilmiy xarajat jadvali va kafedra sahifasi bilan tekshiring', 4),
    ('Universitetni raqamlar bilan oʻqish', 'College Navigator va CDS bir xil shablondagi raqamlarni beradi', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M2. Xarajat va pul oqimi', 'Artefakt: AQSh pul xaritasi.', 2, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Toʻliq narx: Cost of Attendance', 'Toʻliq narx: oʻqish va yigʻimlar, yashash, sugʻurta, kitob va shaxsiy xarajatlar, bir martalik toʻlovlar', 1),
    ('I-20 uchun pul dalili', 'I-20 uchun kamida birinchi yil taxminiy xarajati ishlatsa boʻladigan pul bilan koʻrsatiladi', 2),
    ('Sizga ochiq va yopiq pul manbalari', 'Federal yordam xalqaro talabaga yopiq', 3),
    ('Ehtiyojga va natijaga asoslangan yordam', 'Ehtiyojga asoslangan yordam oila toʻlay olmaydigan farqni qoplaydi; natijaga asoslangan yordam yutuq uchun beriladi va koʻpincha qisman', 4),
    ('Oilaviy byudjet chegarasi va yoʻl xulosasi', 'Oila chegarasini dollarda, yillik raqam bilan aniqlang', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M3. Yordam beradigan universitetlarni topish', 'Artefakt: Yordam boʻyicha saralangan roʻyxat.', 3, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Toʻrt xil yordam siyosati', 'A: xalqaro talabaga ham need-blind va toʻliq ehtiyoj; B: rasmiy soʻzlar aniqlashtirishni talab qiladi; C: need-aware; D: yordam juda cheklangan', 1),
    ('Rasmiy sahifa soʻzlarini oʻqish', 'Kuchli iboralar: need-blind for all applicants (xalqaro talaba aniq koʻrsatilgan), regardless of citizenship, meets 100% of demonstrated need, no-loan', 2),
    ('Common Data Set: H6 bandi', 'H6: xalqaro bakalavrlarga grant siyosati, olganlar soni, oʻrtacha va jami summa', 3),
    ('Net Price Calculator va natijaga asoslangan grantlar', 'Net Price Calculator yordamdan keyingi taxminiy narxni beradi; xalqaro talabaga ishlashini tekshiring', 4),
    ('Yordam boʻyicha saralangan roʻyxat', 'Roʻyxat ikki oʻq bilan tuziladi: qabul ehtimoli va toʻlay olish', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M4. Moliyaviy yordam arizasi', 'Artefakt: Moliyaviy yordam arizasi paketi.', 4, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Formalar xaritasi', 'CSS Profile koʻp universitetlarda asosiy forma; baʼzilari oʻz formasini va daromad hujjatlarini rasmiy tarjima va dollar kursi bilan soʻraydi', 1),
    ('Oʻzbekistondan oila daromadini hujjatlash', 'Har daromad turi uchun rasmiy hujjat, bitta sana va kurs, barcha formalarda bir xil raqam', 2),
    ('Yordam formasi toʻlovi va ozod qilish', 'CSS Profile toʻlovidan ozod qilish xalqaro talabaga hamma joyda qoʻllanmaydi', 3),
    ('Yordam xatini oʻqish', 'Yordam xatini grant, kredit, ish va oila hissasiga ajrating', 4),
    ('Qayta koʻrib chiqish va oʻzgargan holat', 'Haqiqiy oʻzgarish yoki xato boʻlsa, universitet tartibi boʻyicha hujjatli va qisqa soʻrov qiling', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M5. Global UGRAD va almashinuv dasturlari', 'Artefakt: Almashinuv dasturi kartasi.', 5, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Global UGRAD nima', 'Global UGRAD: bir semestr, daraja yoʻq, universitetni dastur tanlaydi, kredit oʻtkazish sizning ishingiz', 1),
    ('Muvofiqlik shartlari', 'Asosiy shartlar: 18+, Oʻzbekistonda yashash va kunduzgi oʻqish, kamida bir yil oʻqish qolishi, ingliz tili, qaytish', 2),
    ('Sikl holatini kuzatish', 'UGRAD sikli rasman eʼlon qilinmaguncha muddat yoʻq', 3),
    ('Ariza va tanlov', 'Ariza onlayn, ingliz tilida, muddatdan keyin oʻzgarmaydi', 4),
    ('Boshqa almashinuv dasturlari va J-1', 'UGRAD dan tashqari maktab, yozgi, kasbiy va ilmiy almashinuvlar bor', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M6. Fulbright magistraturasi', 'Artefakt: Fulbright muvofiqlik va reja kartasi.', 6, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Dastur va Oʻzbekiston uchun shartlar', 'Fulbright Oʻzbekiston uchun: magistratura, 2 yilgacha; bakalavr diplomi, 2 yillik tajriba, Oʻzbekistonda yashash', 1),
    ('Tanlov bosqichlari va joylashtirish', 'Bosqichlar: texnik tekshiruv, oʻquvchilar paneli, elchixonada intervyu, nomzodlik, testlar, kengash tasdigʻi va joylashtirish', 2),
    ('Ariza tarkibi va halollik', 'Ariza: onlayn shakl, original insholar, rezyume, elchixona formasidagi tavsiya, nomzodlar uchun testlar', 3),
    ('Sikl kalendari', '2027–2028 muddati 30.06.2026 da yopilgan; keyingi sikl eʼlon qilinmagan', 4),
    ('J-1 va 2 yillik vatanda yashash talabi', 'Fulbright J-1 bilan: grantdan keyin kamida 2 yil vatanda yashash talabi', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M7. Magistratura va PhD moliyasi', 'Artefakt: Moliya paketi taqqoslagichi.', 7, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Magistratura va PhD: pul qayerdan', 'Magistratura koʻpincha oʻz hisobidan, PhD koʻpincha kafedra paketi bilan', 1),
    ('PhD moliya paketi', 'PhD paketi: stipendiya, oʻqish va yigʻimlardan ozod qilish, sugʻurta, kafolatlangan yillar, TA yoki RA majburiyati', 2),
    ('Kafedra sahifasini oʻqish', 'Har kafedrada 10 savolga javob toping: moliya kafolati, yillar, summa, xalqaro talaba, GRE, til, toʻlov, muddat, professor, fellowship', 3),
    ('Tashqi grantlar: kimga ochiq', 'Har grantni fuqarolik qatori bilan filtrlang', 4),
    ('Takliflarni solishtirish va 15-aprel', 'Takliflarni oylik sof qoldiq, yozgi moliya, kafolat yillari va majburiyat boʻyicha solishtiring', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M8. Viza, maqom va ishlash huquqi', 'Artefakt: Viza va maqom nazorat roʻyxati.', 8, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('F-1 va J-1: qaysi viza, qaysi hujjat', 'F-1: daraja uchun, I-20 bilan', 1),
    ('Toshkentda viza arizasi', 'Toshkentda: DS-160, yigʻim, navbat, hujjatlar, suhbat', 2),
    ('Maqomni saqlash', 'Maqom: toʻliq yuklama, hujjatlar toʻgʻri, ruxsatsiz ish yoʻq, oʻzgarishlar haqida xabar', 3),
    ('F-1 da ishlash huquqi', 'F-1: kampusda semestr davomida haftasiga 20 soatgacha; kampusdan tashqarida faqat yozma ruxsat bilan; OPT 12 oy, STEM OPT qoʻshimcha 24 oy', 4),
    ('Siyosat oʻzgarishini kuzatish', 'Siyosatni faqat rasmiy manba va sana bilan kuzating: elchixona, Davlat departamenti, universitet xalqaro boʻlimi', 5)) as x(t, d, o);
  update public.courses set total_modules = 9,
    description = 'AQShda oʻqish yoʻllari: universitet tizimi, xarajat va I-20, xalqaro talabaga yordam, moliyaviy yordam arizasi, Global UGRAD, Fulbright, PhD moliyasi, viza va ishlash huquqi. 9 modul, 46 dars.',
    holat = 'Tayyor', updated_at = now() where id = v_course;
end $$;

commit;
