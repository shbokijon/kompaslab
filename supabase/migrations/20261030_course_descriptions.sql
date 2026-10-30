-- 2026-10-30 · courses.description ni saytdagi haqiqiy holatga moslash (asoschi tasdigʻi: 2026-10-30)
-- Eski matnlarda: "42 ta video dars" (video yoʻq), "EPSRC PhD tajribasi" (tasdiqlanmagan, asoschi nomi bilan),
-- eskirgan modul/dars sonlari. Raqamlar tools/landing/mods.json va saytdagi Lab kartalaridan.
-- RLS: faqat description ustuni yangilanadi, policy oʻzgarmaydi.
begin;
update public.courses as c set description = v.d, updated_at = now()
from (values
  ('bachelor-lab',     'Xorijiy bakalavriatga tayyorgarlik: universitet tanlash, testlar rejasi, insho, tavsiya xatlari va moliyaviy reja. 17 modul, 86 dars.'),
  ('master-lab',       'Xorijiy magistraturaga tayyorgarlik: akademik CV, tavsiya xatlari, maqsad bayonnomasi, ilmiy loyiha taklifi, stipendiya va viza. 9 modul, 59 dars.'),
  ('phd-lab',          'Moliyalashtirilgan doktoranturaga tayyorgarlik: ilmiy savol, ilmiy rahbar, professorga xat, ilmiy loyiha taklifi va moliyalashtirish. 9 modul, 65 dars.'),
  ('gks-lab',          'Koreya hukumati stipendiyasi (GKS): muvofiqlik, hujjatlar va intervyu; bakalavriat, magistratura va doktorantura treklari. 54 dars.'),
  ('daad-lab',         'Germaniya va DAAD: professor topish, motivatsion xat, tadqiqot rejasi, DAAD portali va joʻnash. 9 modul, 51 dars.'),
  ('usa-lab',          'AQSh: Global UGRAD, Fulbright va doktorantura; muvofiqlik, insholar, intervyu va viza. 12 modul, 72 dars.'),
  ('tadbirkor-talaba', 'Oʻqish bilan birga kichik, qonuniy biznes sinovi: muammo, birinchi mijoz, pul hisobi, huquqiy shakl va soliq. 10 modul, 54 dars.'),
  ('miggo',            'Xorijda faqat rasmiy yoʻl bilan ishlash va firibgarlikdan himoya. Kompas ish yoki viza topib bermaydi. 8 modul, 44 dars.')
) as v(slug, d)
where c.slug = v.slug;
select slug, description from public.courses where slug in ('bachelor-lab','master-lab','phd-lab','gks-lab','daad-lab','usa-lab','tadbirkor-talaba','miggo') order by slug;
commit;
