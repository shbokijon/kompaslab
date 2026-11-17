-- 2026-11-17 · Admin → Dizayn: saytning koʻrinish sozlamalari (mavzu, shrift, oʻlchamlar)
-- site_settings: bitta qator = bitta sozlama toʻplami. Hozircha faqat key = 'ui'.
--   value (jsonb): { v, mode: auto|manual, theme, seasons, hol{…}, font, fs, hs, sp, r, w, reader }
--   Tuzilma va chegaralar: js/kompas-ui.js (KLook.merge) — mijoz notoʻgʻri qiymatni baribir chegaraga keltiradi.
-- Saytda: js/kompas-ui.js anon kalit bilan oʻqiydi (5 daqiqa kesh). Yozish: faqat admin (fn_is_admin).
-- Oʻchirish yoʻq; standartga qaytarish = qiymatni almashtirish. Oldingi qiymat site_settings_log da qoladi.

create table if not exists public.site_settings (
  key        text primary key check (key ~ '^[a-z][a-z0-9_]{0,30}$'),
  value      jsonb not null default '{}'::jsonb check (jsonb_typeof(value) = 'object' and pg_column_size(value) <= 16000),
  updated_at timestamptz not null default now(),
  updated_by uuid default auth.uid()
);

create table if not exists public.site_settings_log (
  id         bigint generated always as identity primary key,
  key        text not null,
  value      jsonb not null,
  changed_at timestamptz not null default now(),
  changed_by uuid
);

alter table public.site_settings enable row level security;
alter table public.site_settings_log enable row level security;

drop policy if exists "site_settings: ui ochiq" on public.site_settings;
create policy "site_settings: ui ochiq" on public.site_settings
  for select using (key = 'ui' or public.fn_is_admin());

drop policy if exists "site_settings: faqat admin yozadi" on public.site_settings;
create policy "site_settings: faqat admin yozadi" on public.site_settings
  for insert with check (public.fn_is_admin());

drop policy if exists "site_settings: faqat admin yangilaydi" on public.site_settings;
create policy "site_settings: faqat admin yangilaydi" on public.site_settings
  for update using (public.fn_is_admin()) with check (public.fn_is_admin());

drop policy if exists "site_settings_log: faqat admin oʻqiydi" on public.site_settings_log;
create policy "site_settings_log: faqat admin oʻqiydi" on public.site_settings_log
  for select using (public.fn_is_admin());

revoke all on public.site_settings from anon, authenticated;
revoke all on public.site_settings_log from anon, authenticated;
grant select (key, value, updated_at) on public.site_settings to anon, authenticated;
grant insert (key, value) on public.site_settings to authenticated;
grant update (value) on public.site_settings to authenticated;
grant select on public.site_settings_log to authenticated;

-- Har oʻzgarishda: vaqt va muallif serverda qoʻyiladi, eski qiymat jurnalga yoziladi
create or replace function public.fn_site_settings_touch()
 returns trigger language plpgsql security definer set search_path to 'public' as $$
begin
  if tg_op = 'UPDATE' then
    insert into public.site_settings_log (key, value, changed_at, changed_by)
      values (old.key, old.value, old.updated_at, old.updated_by);
  end if;
  new.updated_at := now();
  new.updated_by := auth.uid();
  return new;
end $$;
revoke all on function public.fn_site_settings_touch() from public, anon, authenticated;

drop trigger if exists trg_site_settings_touch on public.site_settings;
create trigger trg_site_settings_touch before insert or update on public.site_settings
  for each row execute function public.fn_site_settings_touch();
