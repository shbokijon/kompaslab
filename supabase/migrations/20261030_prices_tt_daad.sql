-- 2026-10-30 · Narxlarni saytdagi qaror bilan tenglashtirish (asoschi tasdigʻi: 2026-10-30)
-- Tadbirkor Talaba: 399 000 / 39 900 → 299 000 / 29 900
-- DAAD Lab oylik: 99 900 → 99 000 (20261030_admin_rls_fix.sql dagi 3-band bilan bir xil, takrorlansa zarar yoʻq)
-- price_starter / price_scholar / price_elite — generated ustunlar, qoʻlda yozilmaydi.
-- RLS: faqat courses ustunlari yangilanadi, policy oʻzgarmaydi.

begin;

update public.courses
   set price = 299000, price_yearly = 299000, price_monthly = 29900, updated_at = now()
 where slug = 'tadbirkor-talaba';

update public.courses
   set price_monthly = 99000, updated_at = now()
 where slug = 'daad-lab';

-- Tekshiruv: anon roli koʻradigan jonli narxlar
set local role anon;
select (public.kompas_public_stats() -> 'prices') -> 'tadbirkor-talaba' as tt,
       (public.kompas_public_stats() -> 'prices') -> 'daad-lab'         as daad;
reset role;

commit;
