-- 2026-10-30 · admin.html tuzatishlari uchun RLS
-- 1) payments: admin qoʻlda toʻlov yozuvi yarata oladi (avval INSERT policy yoʻq edi,
--    admin "Talaba qoʻshish" toʻlovsiz enrollment yaratardi).
-- 2) enrollments: admin talabani kursdan chiqara oladi (avval DELETE policy yoʻq edi,
--    oʻchirish 0 qatorga taʼsir qilib, "chiqarildi" deb koʻrsatardi).
-- 3) daad-lab oylik narxi 99 900 → 99 000 (boshqa Lablar bilan bir xil).
-- Talaba (authenticated, admin emas) uchun hech narsa ochilmaydi.

drop policy if exists "payments: faqat admin yaratadi" on public.payments;
create policy "payments: faqat admin yaratadi"
  on public.payments for insert
  with check (public.fn_is_admin());

drop policy if exists "enrollments: faqat admin oʻchiradi" on public.enrollments;
create policy "enrollments: faqat admin oʻchiradi"
  on public.enrollments for delete
  using (public.fn_is_admin());

update public.courses
   set price_monthly = 99000, updated_at = now()
 where slug = 'daad-lab' and price_monthly = 99900;
