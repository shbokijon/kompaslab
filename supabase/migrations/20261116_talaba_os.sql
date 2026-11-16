-- ═══════════════════════════════════════════════════════════════
--  Talaba OS (os.html) — holatni hisobga bogʻlash, 2026-11-16
--  Bir foydalanuvchi = bir qator. Ichida: profil (bosqich, daraja, soha),
--  arizalar, 4K qadamlari, Ish stoli hujjatlari (matn bilan), rubrika belgilari.
--  Hujjat matni shu yerda saqlanadi: shuning uchun faqat egasi oʻqiydi.
--  Admin ham oʻqimaydi (fn_is_admin siyosatda yoʻq) — talaba matni shaxsiy.
--  QOʻLLANMAGAN: asoschi tasdigʻini kutadi.
-- ═══════════════════════════════════════════════════════════════
create table if not exists public.kompas_os_state (
  user_id    uuid primary key default auth.uid() references auth.users(id) on delete cascade,
  state      jsonb not null check (jsonb_typeof(state) = 'object' and pg_column_size(state) < 524288),
  updated_at timestamptz not null default now()
);
comment on table public.kompas_os_state is 'Talaba OS holati (os.html). Faqat egasi oʻqiydi va yozadi.';

alter table public.kompas_os_state enable row level security;
revoke all on public.kompas_os_state from anon, authenticated;
grant select, delete on public.kompas_os_state to authenticated;
grant insert (state, updated_at), update (state, updated_at) on public.kompas_os_state to authenticated;

drop policy if exists os_state_own_read on public.kompas_os_state;
create policy os_state_own_read on public.kompas_os_state
  for select to authenticated using (user_id = auth.uid());
drop policy if exists os_state_own_insert on public.kompas_os_state;
create policy os_state_own_insert on public.kompas_os_state
  for insert to authenticated with check (user_id = auth.uid());
drop policy if exists os_state_own_update on public.kompas_os_state;
create policy os_state_own_update on public.kompas_os_state
  for update to authenticated using (user_id = auth.uid()) with check (user_id = auth.uid());
drop policy if exists os_state_own_delete on public.kompas_os_state;
create policy os_state_own_delete on public.kompas_os_state
  for delete to authenticated using (user_id = auth.uid());

-- Admin uchun faqat soni (matnsiz): nechta talaba OS dan foydalanyapti
create or replace function public.kompas_admin_os_usage() returns jsonb
language plpgsql stable security definer set search_path = public as $$
begin
  if not public.fn_is_admin() then raise exception 'forbidden'; end if;
  return jsonb_build_object(
    'users', (select count(*) from public.kompas_os_state),
    'active_7d', (select count(*) from public.kompas_os_state where updated_at > now() - interval '7 days'),
    'apps', (select coalesce(sum(jsonb_array_length(coalesce(state->'apps','[]'::jsonb))),0) from public.kompas_os_state),
    'drafts', (select coalesce(sum(jsonb_array_length(coalesce(state->'drafts','[]'::jsonb))),0) from public.kompas_os_state)
  );
end $$;
revoke execute on function public.kompas_admin_os_usage() from public, anon;
grant execute on function public.kompas_admin_os_usage() to authenticated;
