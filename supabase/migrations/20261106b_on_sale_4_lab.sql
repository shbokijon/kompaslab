-- 2026-11-06 · Asoschi tasdigʻi bilan bazaga qoʻllangan (17:48).
-- 20261106_lab_visibility_on_sale.sql hamma Labni on_sale=false qilgan edi; oʻsha kuni ommaviy oferta bilan
-- sotuv ochilgan 4 Lab (e3d402d) sotuvga qaytarildi.
update public.courses set on_sale = true, updated_at = now()
 where slug in ('bachelor-lab','master-lab','usa-lab','gks-lab') and status = 'active';
