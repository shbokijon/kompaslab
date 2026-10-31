-- 2026-10-31 · GKS Lab katalogi: M0 (bepul) + M1–M8, 41 dars, 4 faza (asoschi qarori, 2026-10-31)
-- Eski 6 modul / 20 dars (2026-04 tuzilmasi) oʻchiriladi. 2026-10-31 tekshiruvi: gks-lab uchun
-- enrollments 0, progress 0, notes 0, materials 0, lesson_contents 0 (FK lar cascade).
-- fn_paid_page(): modules.order_index = M raqami (M0 = 0, M1 = 1 …), fn_module_position M0 = 1-oʻrin.
-- Narx oʻzgarmaydi: 20261031_price_6m.sql (oylik 99 000, 6 oylik 499 000, yillik 899 000).
-- RLS va policy oʻzgarmaydi. Pullik HTML alohida: python3 tools/modules/paid_upload.py gks-lab-m1 … gks-lab-m8.

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
  values (v_course, 'M1. Hujjatlar infratuzilmasi', 'Artefakt: Hujjatlar nazorat jadvali.', 1, false, false) returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('GKS hujjatlari xaritasi', 'GKS toʻplami ikki qismdan iborat: oʻzingiz toʻldiradigan formalar (apostilsiz) va rasmiy guvohnomalar (apostil bilan). Roʻyxatni yoʻriqnomadan bandma-band jadvalga koʻchiring.', 1),
    ('Apostil, tarjima va nusxa qoidalari', 'Guvohnomalar apostil yoki konsullik tasdigʻi bilan; oddiy va notarial nusxa oʻtmaydi. Tarjimani oʻzingiz tekshiring va legallashtirishni ariza oynasidan kamida 2 oy oldin boshlang.', 2),
    ('Baholar: GPA talabi va konvertatsiya', 'Talab: 80/100, yuqori 20 foiz yoki 2.64/4.0 (3.23/5.0) dan bittasi. Bahoni asl shkalada yozing; konvertatsiyani muassasa tasdiqlaydi.', 3),
    ('Til strategiyasi: TOPIK va ingliz tili', 'TOPIK ixtiyoriy, lekin ball va til yiliga taʼsir qiladi. Bitta tilni tanlab, unga sana qoʻying.', 4)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M2. Universitet va dastur tanlash', 'Artefakt: Universitet tanlovi va moslik dalilnomasi.', 2, false, false) returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Elchixona treki yoki universitet treki', 'Elchixona treki: elchixona → NIIED → universitet, 3 tagacha universitet. Universitet treki: universitet → NIIED, bitta universitet. Kvota raqamlari yoʻlga qarab keskin farq qiladi.', 1),
    ('A va B turdagi universitetlar', 'Elchixona trekida 3 tagacha universitet, kamida bittasi B turidan; R-GKS da faqat B turi. Turni joriy yil ilovasidan tekshiring.', 2),
    ('Dastur va fakultetni oʻqish', 'Tanlov fakultet, dastur va (M, D uchun) laboratoriya darajasida qilinadi. Har universitet uchun tekshiriladigan bitta moslik dalili yozing.', 3),
    ('Saralangan roʻyxat va xavf taqsimoti', 'Har universitetni bir xil mezon bilan ballang; qoidaga zid tanlov chiqadi, qolganlari orasida xavfni taqsimlang.', 4),
    ('Kvota va raqobatni toʻgʻri oʻqish', 'Kvota raqobatchilar sonini aytmaydi. Imkon foizini taxmin qilmang; tayyorgarlik sifatini oshiring va ikkala yoʻlni koʻrib chiqing.', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M3. Nomzod profili va dalillar', 'Artefakt: Dalillar inventari va profil izohi.', 3, false, false) returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Dalillar inventari: STAR usuli', 'Har tajribani Vaziyat → Vazifa → Harakat → Natija qatoriga keltiring; natija tekshiriladigan boʻlsin, shaxsiy hissangiz aniq koʻrinsin.', 1),
    ('Faoliyat va yutuqlarni formaga tayyorlash', 'Har qator tegishli, yaqin, tasdiqlangan boʻlsin. Joy kam boʻlsa, kamroq lekin kuchliroq yutuqni qoldiring.', 2),
    ('Zaif tomonlarni boshqarish', 'Zaif tomonni fakt → tuzatish → hozirgi dalil tartibida qisqa tushuntiring; yashirmang va markazga ham qoʻymang.', 3),
    ('Oʻsish traektoriyasi va profil izohi', 'Profil izohi: bugungi nuqta → traektoriya → boʻshliq → keyingi qadam. Bu paragraf keyingi hujjatlarning umurtqasi.', 4)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M4. Tavsiya xati va professor bilan aloqa', 'Artefakt: Aloqa paketi.', 4, false, false) returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('GKS tavsiya xati: talablar va tanlov', 'GKS da bitta tavsiya xati; sanasi muddatdan oldingi bir yil ichida. Tavsiya beruvchini lavozim emas, yaqinlik va aniq dalil boʻyicha tanlang.', 1),
    ('Yutuqlar varaqasi va soʻrash tartibi', 'Tavsiya beruvchiga faktlar beriladi, matn emas. 6–8 hafta oldin soʻrang, forma va muddatni bitta xatda yuboring.', 2),
    ('Professorga dastlabki xat (Cold email)', 'Professorga xat: kimsiz, nega u (aniq ish), dalil, bitta savol. Ommaviy xat emas, 3–5 ta shaxsiy xat.', 3),
    ('Kuzatuv, javob va etik chegaralar', 'Bitta eslatma, keyin toʻxtash; kafolat, sovgʻa va vositachi yoʻq. Har xatni jurnalga yozing.', 4)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M5. Shaxsiy bayonot', 'Artefakt: Shaxsiy bayonot.', 5, false, false) returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Forma savollari va baholovchi mantiqi', 'Bayonot formaning savollariga javob beradi; shablon va hajm chegarasini avval oʻqing. Har bosqichdagi baholovchi bitta savolga javob izlaydi.', 1),
    ('Kimlik → Dalil → Maqsad → Moslik', 'Toʻrt blok: Kimlik, Dalil, Maqsad, Moslik. "Nega Koreya" javobi umumiy sabab emas, aniq soha, dastur va qaytgandan keyingi reja.', 2),
    ('Birinchi qoralama', 'Qoralama: har blok bir paragraf, har paragrafda bitta aniq fakt, ochilish aniq voqea yoki savol. Avval toʻliq, keyin yaxshi.', 3),
    ('Tahrir: faktga almashtirish', 'Tahrir uch oʻtishda: mazmun, aniqlik, til. Har sifatni faktga almashtiring, tekshirib boʻlmaydigan daʼvoni oʻchiring.', 4),
    ('Oʻzaro tahrir va yakuniy versiya', 'Yakuniy versiya 5 mezon boʻyicha baholanadi; tahrirchi izoh beradi, matnni siz oʻzgartirasiz va qaydini yuritasiz.', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M6. Oʻquv rejasi', 'Artefakt: Oʻquv rejasi.', 6, false, false) returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Oʻquv rejasi nima uchun markaziy hujjat', 'Oʻquv rejasi "qanday" savoliga javob beradi: aniq vaqt, aniq fan yoki tadqiqot va aniq keyingi qadam.', 1),
    ('Hozirgi holat → Boʻshliq → Strategiya → Vaqt', 'Hozirgi holat → Boʻshliq → Strategiya → Vaqt: har qism oldingisidan kelib chiqadi va keyingisini asoslaydi.', 2),
    ('Til yili va daraja yillari rejasi', 'Reja til yilidan boshlanadi va har davrga aniq oʻqish va oʻlchanadigan natija beradi. Fanlar rasmiy oʻquv rejasidan olinadi.', 3),
    ('Tadqiqot savoli yoki oʻqish yoʻnalishi', 'M va D: mavzudan oʻlchanadigan savolga, Muammo → Yechim → Yangilik → Taʼsir. U: fanlar, koʻnikmalar va loyihalar rejasi.', 4),
    ('Bitiruvdan keyingi yoʻl va izchillik', 'Bitiruvdan keyingi yoʻl aniq, bogʻliq va halol. Bayonot va reja soha, maqsad va dasturda bir xil gapiradi.', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M7. Paketni yigʻish va topshirish', 'Artefakt: Topshirish paketi va taqvim.', 7, false, false) returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Onlayn ariza va muddatlar', 'Muddatlar KST bilan: Toshkentdan 4 soat oldin yopiladi. Oʻz muddatingizni rasmiydan kamida 3 kun oldin qoʻying.', 1),
    ('Fayl, format va nusxalar', 'Paket yoʻriqnoma tartibida, aniq skanerlar, tushunarli fayl nomlari va imzolar bilan. Hamma narsaning zaxirasi sizda qoladi.', 2),
    ('Ikkinchi shaxs tekshiruvi va xatolar filtri', 'Xatolar filtri va ikkinchi odam: ism, nomlar, shablon qoldiqlari, sanalar, hajm, dalilsiz daʼvo.', 3),
    ('Teskari taqvim', 'Har ishni muddatdan orqaga joylang; eng uzoq jarayonlar (apostil, tavsiya) birinchi. Shaxsiy muddat rasmiydan 3 kun oldin.', 4)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M8. Intervyu, natija va joʻnash', 'Artefakt: Intervyu kartochkalari va joʻnash rejasi.', 8, false, false) returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Intervyu mantiqi', 'Intervyu hujjatlaringizning ogʻzaki tekshiruvi: muallif ekaningiz, aniqlik, uddalash va maqsad.', 1),
    ('Savollar va javob tuzilmasi', 'Har javob: bir jumlada javob, bitta aniq misol, dasturga bogʻlash. Yodlamang, kalit soʻzlar bilan mashq qiling.', 2),
    ('Natijalar va universitet tanlovi', 'Natija sanalarini va universitet tanlovi muddatini oldindan taqvimga qoʻying; tanlovni M2 mezonlari bilan tez qiling.', 3),
    ('Joʻnash oldi tayyorgarlik va majburiyatlar', 'Taklifnoma → viza → tibbiy → chipta → sugʻurta → moliya. Stipendiya qoidalari (chiqish, mutaxassislik) birinchi kundan amal qiladi.', 4),
    ('Rad javobidan keyingi reja', 'Rad javobidan keyin: qaysi bosqich, qaysi hujjat, qaysi muqobil yoʻl. Muvofiqlikni yangi yoʻriqnoma bilan qayta tekshiring.', 5)) as x(t, d, o);
end $$;

select order_index, title, (select count(*) from public.lessons l where l.module_id = m.id) as darslar
  from public.modules m where course_id = (select id from public.courses where slug = 'gks-lab') order by order_index;

commit;
