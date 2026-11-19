-- 2026-11-19 (asoschi qarori): kompas_user_state endi modul javoblarini ham saqlaydi
-- (tanlovlar, yozma matn). Admin talaba oynasida "Javoblar" tabida koʻradi (RLS: fn_is_admin).
-- Bitta yozuv chegarasi 16 KB → 128 KB (CV, insho matnlari uchun). Mijoz 120 000 belgidan
-- oshsa faqat jarayonni yuboradi (js/kompas-sync.js full()).
alter table public.kompas_user_state drop constraint if exists kompas_user_state_value_check;
alter table public.kompas_user_state add constraint kompas_user_state_value_check
  check (jsonb_typeof(value) = 'object' and pg_column_size(value) < 131072);
comment on table public.kompas_user_state is
  'Modul holati: jarayon (xp, done, seen, open, lv) va javoblar (2026-11-19 dan). Foydalanuvchi oʻzinikini, admin hammasini oʻqiydi.';
