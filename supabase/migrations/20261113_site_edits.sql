-- 2026-11-13 · Admin → Vebsayt: sahifa boʻlimlarini yashirish va matnini tahrirlash
-- site_edits: bitta qator = bitta sahifadagi bitta elementga bitta oʻzgarish.
--   page : fayl nomi ('index.html', 'master-lab-narxlar.html')
--   sel  : CSS yoʻli (#id yoki body > section:nth-of-type(3) …), js/kompas-ui.js dagi KSiteEdits.path() yasaydi
--   guard: elementning asl matni boshidan 60 harf (normallashgan, alifboga bogʻliq emas).
--          Manba oʻzgarib, yoʻl boshqa elementga tushsa, oʻzgarish qoʻllanmaydi yoki guard boʻyicha topiladi.
--   kind : 'hide' (koʻrinmaydi) · 'html' (ichki matn; faqat matn va b/i/em/strong/br/a/span, mijozda tozalanadi)
--   value: 'html' uchun yangi matn, amaldagi alifboda (oʻ, gʻ, sh, ch); saytda alifbo.js oʻgiradi
--   status: active (saytda) · off (bekor qilingan, tarix uchun qoladi)
-- Saytda: js/kompas-ui.js (anon faqat active ni oʻqiydi). Muharrir: js/site-editor.js (?kedit=1, faqat admin).

create table if not exists public.site_edits (
  id         bigint generated always as identity primary key,
  page       text not null check (page ~ '^[a-z0-9][a-z0-9._-]*\.html$' and char_length(page) <= 120),
  sel        text not null check (char_length(sel) between 1 and 500),
  kind       text not null check (kind in ('hide', 'html')),
  guard      text not null default '' check (char_length(guard) <= 80),
  label      text check (label is null or char_length(label) <= 160),
  value      text check (value is null or char_length(value) <= 20000),
  status     text not null default 'active' check (status in ('active', 'off')),
  note       text check (note is null or char_length(note) <= 300),
  created_at timestamptz not null default now(),
  created_by uuid default auth.uid(),
  updated_at timestamptz not null default now(),
  updated_by uuid default auth.uid(),
  check (kind <> 'html' or value is not null)
);
-- Bir element uchun bitta faol oʻzgarish (har tur boʻyicha)
create unique index if not exists site_edits_one_active
  on public.site_edits (page, sel, kind) where status = 'active';
create index if not exists site_edits_page_idx on public.site_edits (page, status);

alter table public.site_edits enable row level security;

drop policy if exists "site_edits: faol oʻzgarishlar ochiq" on public.site_edits;
create policy "site_edits: faol oʻzgarishlar ochiq"
  on public.site_edits for select
  using (status = 'active' or public.fn_is_admin());

drop policy if exists "site_edits: faqat admin yozadi" on public.site_edits;
create policy "site_edits: faqat admin yozadi"
  on public.site_edits for insert with check (public.fn_is_admin());

drop policy if exists "site_edits: faqat admin yangilaydi" on public.site_edits;
create policy "site_edits: faqat admin yangilaydi"
  on public.site_edits for update using (public.fn_is_admin()) with check (public.fn_is_admin());

-- Oʻchirish yoʻq: bekor qilish = status 'off' (tarix qoladi)
revoke all on public.site_edits from anon, authenticated;
-- Anon faqat qoʻllash uchun kerakli ustunlarni oʻqiydi (kim yozgani koʻrinmaydi)
grant select (id, page, sel, kind, guard, value, status) on public.site_edits to anon;
grant select (id, page, sel, kind, guard, label, value, status, note, created_at, updated_at) on public.site_edits to authenticated;
grant insert (page, sel, kind, guard, label, value, status, note) on public.site_edits to authenticated;
grant update (sel, guard, label, value, status, note) on public.site_edits to authenticated;

create or replace function public.fn_site_edits_touch()
 returns trigger language plpgsql set search_path to 'public' as $$
begin
  new.updated_at := now();
  new.updated_by := auth.uid();
  new.created_at := old.created_at;
  new.created_by := old.created_by;
  return new;
end $$;
drop trigger if exists trg_site_edits_touch on public.site_edits;
create trigger trg_site_edits_touch before update on public.site_edits
  for each row execute function public.fn_site_edits_touch();
