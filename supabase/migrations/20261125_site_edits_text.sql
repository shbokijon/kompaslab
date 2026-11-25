-- 2026-11-25 · Admin → Vebsayt: murakkab bloklarda matn boʻlaklarini tahrirlash (jonli muharrir)
-- site_edits.kind ga 'text' qoʻshiladi. value = JSON matn:
--   {"n":12,"c":{"3":"yangi matn"}}  n: blokdagi boʻsh boʻlmagan matn tugunlari soni,
--                                    c: oʻzgargan tugunlar (tartib raqami → matn, amaldagi alifboda)
-- Tuzilma (tugma, ikonka, forma, ⓘ) tegilmaydi. Saytda qoʻllash: js/kompas-ui.js (KSiteEdits.textApply).
-- Maʼlumot oʻchirilmaydi, RLS oʻzgarmaydi.

alter table public.site_edits drop constraint if exists site_edits_kind_check;
alter table public.site_edits add constraint site_edits_kind_check check (kind in ('hide', 'html', 'style', 'text'));

alter table public.site_edits drop constraint if exists site_edits_text_value_check;
alter table public.site_edits add constraint site_edits_text_value_check
  check (kind <> 'text' or (value is not null and value like '{%'));
