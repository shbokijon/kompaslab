-- 2026-11-19 · Admin → Vebsayt: blok oʻlchami va shrift oʻlchami (jonli muharrir)
-- site_edits.kind ga 'style' qoʻshiladi. value = JSON matn:
--   {"fs":1.15}            shu blok va ichidagi matn oʻlchami (koʻpaytuvchi, 0.7–1.6)
--   {"w":560}              blok kengligi px (avtomatik markazda, telefonda 100% dan oshmaydi)
--   {"sym":true}           bir qatordagi bir xil qoʻshni bloklarga ham shu kenglik
-- Saytda qoʻllash: js/kompas-ui.js (KSiteEdits.style). Maʼlumot oʻchirilmaydi, RLS oʻzgarmaydi.

alter table public.site_edits drop constraint if exists site_edits_kind_check;
alter table public.site_edits add constraint site_edits_kind_check check (kind in ('hide', 'html', 'style'));

alter table public.site_edits drop constraint if exists site_edits_style_value_check;
alter table public.site_edits add constraint site_edits_style_value_check
  check (kind <> 'style' or (value is not null and char_length(value) <= 300));
