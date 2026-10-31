-- 2026-10-31 · PhD Lab v4 katalogi: M0 (bepul, 5 dars) + M1–M8 (50 dars) = 9 modul, 55 dars.
-- Manba: tools/modules/src/phd-lab-m0.src.html, tools/modules/phd/mods/m<N>.py. Generator: qoʻlda (bir martalik).
-- order_index = modul raqami = paid_pages.module_index (phd-lab-o.html?m=N).
-- Oylik: 1 toʻlov = 1 faza = 2 modul (I M1–M2, II M3–M4, III M5–M6, IV M7–M8); webhook unlocked_modules ni +2 qiladi.
-- DIQQAT: ASOSCHI TASDIGʻISIZ QOʻLLANMAYDI. Eski PhD darslari boʻlsa, skript toʻxtaydi.
-- Eski katalogni almashtirish uchun avval: set local kompas.phd_replace = 'yes'; (eski darslar oʻchiriladi, qaytarib boʻlmaydi).

begin;

do $$
declare
  v_course uuid;
  v_mod uuid;
begin
  select id into v_course from public.courses where slug = 'phd-lab';
  if v_course is null then raise exception 'phd-lab topilmadi'; end if;
  if exists (select 1 from public.lessons l join public.modules m on m.id = l.module_id where m.course_id = v_course) then
    if coalesce(current_setting('kompas.phd_replace', true), '') <> 'yes' then
      raise exception 'phd-lab da darslar bor: toʻxtatildi (kompas.phd_replace kerak)';
    end if;
    delete from public.lessons where module_id in (select id from public.modules where course_id = v_course);
    delete from public.modules where course_id = v_course and order_index > 8;
  end if;
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M0. PhD yoʻli menga mosmi?', 'Artefakt: Shaxsiy yoʻl kartasi, tayyorgarlik koʻrsatkichi va qaror bayonoti.', 0, true, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, true, 'published' from (values
    ('PhD nima va kim uchun?', 'Doktorantura ish va tadqiqot sifatida: kimga mos, kimga hozircha mos emas', 1),
    ('Doktorantura yoʻllari xaritasi', 'Loyiha oʻrni, oʻz taklifing bilan ariza, ish shartnomali PhD, davlat stipendiyasi', 2),
    ('Tayyorgarlikni halol baholash', 'Tayyorgarlik koʻrsatkichi: Lab sahifasidagi test bilan bir xil mezon', 3),
    ('Xavflar, moliya va oilaviy qaror', 'Toʻliq xarajat, oila byudjeti, toʻxtatish mezonlari', 4),
    ('Shaxsiy yoʻl kartasi va birinchi qadam', 'Vaqt chizigʻi, kimga mos emasligi, birinchi 14 kunlik qadam', 5)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M1. Ilmiy yoʻnalish va tadqiqot savoli', 'Artefakt: Ilmiy yoʻnalish qisqa bayoni.', 1, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Qiziqishdan ilmiy muammoga', '"Sunʼiy intellekt", "geotermal energiya", "taʼlim" bu mavzular, hali ilmiy muammo emas.', 1),
    ('Adabiyot qidirish tizimi', 'Kuchli PhD gʻoyasi blog yoki videodan emas, tekshiriladigan adabiyot xaritasidan boshlanadi.', 2),
    ('Ilmiy boʻshliqni dalil bilan koʻrsatish', '"Bu mavzuda ish yoʻq" degan gap koʻpincha notoʻgʻri chiqadi va komissiyada ishonchni pasaytiradi.', 3),
    ('Savol, gipoteza, maqsad va vazifalar', 'Tadqiqot savoli, maqsad, vazifalar va gipoteza bir xil narsa emas.', 4),
    ('Bajarilishi mumkinlik va resurslar', 'Juda yaxshi ilmiy savol ham kerakli maʼlumot yoki uskuna boʻlmasa, 3–4 yillik rejaga sigʻmaydi.', 5),
    ('2 sahifalik ilmiy yoʻnalish qisqa bayoni', 'Mavzuni boshqa odam bir daqiqada tushunmasa, uni qayta tuzish kerak.', 6)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M2. Doktorantura tizimlari va universitet tanlash', 'Artefakt: Saralangan roʻyxat va 4 ta ustuvor ariza.', 2, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Doktoranturaning toʻrt modeli', 'Bitta mamlakat ichida ham PhD turlicha tashkil qilinadi.', 1),
    ('Oʻrinlarni qidirish tizimi', 'Tasodifiy Telegram kanallari oʻrniga qayta ishlatiladigan qidiruv tizimini quring.', 2),
    ('Universitet va ilmiy muhitni baholash', 'Universitet reytingi rahbarlik sifatini va ish sharoitini toʻliq koʻrsatmaydi.', 3),
    ('Muvofiqlik va rasmiy talablar', 'Bitta majburiy talab bajarilmasa, kuchli ilmiy moslik ham arizani saqlab qolmasligi mumkin.', 4),
    ('Muddatlar va teskari kalendar', 'Kafedra arizasi, moliyalashtirish va kollej muddatlari bir xil boʻlmasligi mumkin.', 5),
    ('Ustuvor arizalar va B reja', 'Arizalar soni sifat va moliyaviy xavfsizlik oʻrnini bosmaydi.', 6)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M3. Ilmiy rahbar va laboratoriya bilan aloqa', 'Artefakt: Rahbar moslik kartalari va aloqalar jurnali.', 3, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Rahbar topish usullari', 'PhD uchun mos professor mashhur olim boʻlishi shart emas: u aynan sizning savolingizdagi ishni boshqara oladigan odam boʻlishi kerak.', 1),
    ('Rahbar bilan moslik jadvali', 'Moslik bahosini "yoqdi, yoqmadi" hisidan dalilga oʻtkazing.', 2),
    ('Professorga dastlabki xat tuzilmasi', 'Xatning vazifasi oʻzingizni maqtash emas, aniq ilmiy aloqani boshlash.', 3),
    ('Portfel va ilovalar', 'Rahbar siz haqingizdagi dalilni tez topa olishi kerak.', 4),
    ('Qayta yozish va muloqot odobi', 'Ketma-ket xat yozish va bosim oʻtkazish akademik aloqani buzadi.', 5),
    ('Rahbar bilan suhbat', 'Birinchi 20 daqiqalik suhbat rasmiy intervyu boʻlmasligi mumkin, lekin unda moslik va bajarilishi mumkinlik aniqlanadi.', 6),
    ('Ikkinchi rahbar va qoʻllab-quvvatlash', 'Ilmiy muvaffaqiyat koʻpincha bitta rahbardan tashqari muhitga ham bogʻliq.', 7)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M4. Ilmiy loyiha taklifi va metodologiya', 'Artefakt: Ilmiy loyiha taklifi v1–v3.', 4, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Loyiha taklifi va uning vazifasi', 'Ilmiy loyiha taklifi savolni sotadigan reklama matni emas, tekshiriladigan ish rejasi.', 1),
    ('Ilmiy asos va ahamiyat', 'Boʻshliqni koʻrsatishdan oldin nimalar maʼlum ekanini adolatli bayon qiling.', 2),
    ('Savol va vazifalar', 'Savol va metodni ajratmasangiz, natija oldindan tayyorlangan xulosaga aylanadi.', 3),
    ('Metod va tekshiruv', 'Yaxshi metod chiroyli algoritm nomi emas, savolga mos dalil yigʻish jarayoni.', 4),
    ('Ish rejasi va natijalar', 'Doktorantura vaqt rejasi ilmiy xavfni boshqarish vositasi.', 5),
    ('Etika, maʼlumot va ochiqlik', 'Ilmiy halollik loyiha taklifining oxirgi rasmiyatchiligi emas: u metod sifatini belgilaydi.', 6),
    ('Tahrir va baholash mezoni', 'Birinchi qoralama ilmiy natija emas: sifat fikr-mulohaza va qayta yozish bilan oshadi.', 7)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M5. Akademik profil va ariza hujjatlari', 'Artefakt: Akademik hujjatlar toʻplami va tavsiya varaqalari.', 5, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Akademik CV: dalil tuzilmasi', 'PhD uchun CV ish joylari roʻyxati emas: u ilmiy qobiliyatingizni dalil bilan koʻrsatadi.', 1),
    ('Ilmiy portfel va kod ombori', 'Ishingizni koʻrsatish ilmiy va texnik ishonchni oshiradi, lekin maxfiylikni buzmasligi kerak.', 2),
    ('Tavsiya beruvchilar bilan ishlash', 'Tavsiya xatining kuchi uni kim yozgani va sizning ishingizni qanchalik yaqindan koʻrganiga bogʻliq.', 3),
    ('Maqsad bayonnomasi va ilmiy bayon', 'Loyiha taklifi "nima va qanday?" savoliga, maqsad bayonnomasi esa "nega aynan siz va nega shu guruh?" savoliga javob beradi.', 4),
    ('Transkript va rasmiy hujjatlar', 'Hujjatning ishonchliligi tarjima, shakl va qabul tizimi koʻrsatmasiga bogʻliq.', 5),
    ('Sunʼiy intellekt va akademik halollik', 'Sunʼiy intellekt matnni tushuntirish yoki tahrirlashda yordam berishi mumkin, lekin mualliflik va faktlar uchun javobgarlik sizda qoladi.', 6)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M6. Moliyalashtirish va moliyaviy qaror', 'Artefakt: Moliyalashtirish taqqoslamasi va 12 oylik pul oqimi.', 6, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Moliyalashtirish turlari', '"Toʻliq moliyalashtirilgan" (fully funded) iborasi har eʼlonda bir xil qamrovni anglatmaydi.', 1),
    ('Buyuk Britaniyada doktorlik oʻrinlari', 'Buyuk Britaniyada moliyalashtirilgan PhD koʻpincha universitet orqali beriladigan doktorlik oʻrni (studentship) shaklida boʻladi.', 2),
    ('MSCA va Yevropadagi maoshli doktorantura', 'Yevropadagi ayrim PhD lar stipendiya emas, mehnat shartnomasi orqali moliyalanadi.', 3),
    ('Xarajatlar va boshlangʻich pul', 'Kuchli stipendiyada ham dastlabki oylar xarajati muammo boʻlishi mumkin: depozit, viza, chipta birinchi stipendiyadan oldin toʻlanadi.', 4),
    ('Taklif shartlarini tekshirish', 'Moliyalashtirish taklifi akademik taklif bilan bir vaqtda yoki undan keyin kelishi mumkin.', 5),
    ('Moliyaviy qaror', 'Moliyalashtirish kamomadi ilmiy qaror va hayot sifati bilan birga baholanadi.', 6)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M7. Ariza, intervyu va qaror', 'Artefakt: Topshirilgan arizalar reyestri, intervyu banki va qaror jadvali.', 7, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Topshirishdan oldingi sifat nazorati', 'Yaxshi hujjatlar toʻplami notoʻgʻri portal yoki notoʻgʻri fayl sabab kechikishi mumkin.', 1),
    ('Tavsiya beruvchi va portal kuzatuvi', 'Tavsiya jarayonini hurmat bilan kuzatish mumkin.', 2),
    ('Ilmiy intervyu', 'PhD intervyusida fakt yodlashdan koʻra savolingizni ilmiy himoya qila olish tekshiriladi.', 3),
    ('Taqdimot va qiyin savollar', 'Baʼzi intervyularda ilmiy taqdimot yoki oldingi dissertatsiyangizni muhokama qilish soʻraladi.', 4),
    ('Taklif, kutish roʻyxati va rad javobi', 'Qabul javobi har doim oddiy "ha" yoki "yoʻq" boʻlmaydi.', 5),
    ('Yakuniy qaror', 'Qabul qarorini nom emas, ilmiy moslik, moliya va yashash sharoiti birgalikda hal qiladi.', 6)) as x(t, d, o);
  insert into public.modules (course_id, title, description, order_index, is_free, is_locked)
  values (v_course, 'M8. Qabuldan keyingi tayyorgarlik va birinchi 90 kun', 'Artefakt: Joʻnash oldi nazorat roʻyxati va 90 kunlik reja.', 8, false, false)
  on conflict (course_id, order_index) do update set title = excluded.title, description = excluded.description, is_free = excluded.is_free, is_locked = false, updated_at = now()
  returning id into v_mod;
  insert into public.lessons (module_id, title, description, order_index, is_free, status)
  select v_mod, t, d, o, false, 'published' from (values
    ('Taklif shartlarini yopish', 'Taklifni qabul qilish dasturga yozilishning oxirgi qadami boʻlmasligi mumkin.', 1),
    ('Viza, ATAS va immigratsiya', 'Viza va tadqiqot ruxsatnomasi qoidalari shaxsiy holatga, fanga va davlatga bogʻliq.', 2),
    ('Uy, xavfsizlik va boshlangʻich xarajat', 'Birinchi oyda ilmiy ishni boshlash uchun asosiy ehtiyojlar oldindan hal qilingan boʻlishi kerak: uy, aloqa, bank, sogʻliq.', 3),
    ('Tadqiqotga kirishish tizimi', 'Doktoranturani boshlash "tadqiqotni boshladim" degan mavhum his boʻlmasligi kerak.', 4),
    ('90 kunlik ilmiy ritm', 'Ilmiy ishda bandlik emas, tekshiriladigan natija va fikr-mulohaza muhim.', 5),
    ('Karyera va foydali tadqiqot', 'PhD davomida ham akademik, ham boshqa professional yoʻllar ochiq qolishi kerak.', 6)) as x(t, d, o);
end $$;

-- Tekshiruv: 9 modul, 55 published dars (total_lessons triggeri hisoblaydi)
select m.order_index, m.title, count(l.id) as darslar from public.modules m left join public.lessons l on l.module_id = m.id
where m.course_id = (select id from public.courses where slug = 'phd-lab') group by 1, 2 order by 1;

commit;
