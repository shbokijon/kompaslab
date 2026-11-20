-- 2026-11-20: xabar yuborish poydevori (email + Telegram), marketing roziligi, saytdagi eʼlon paneli, bot adminlari.
-- Hamma jadvalda RLS yoqilgan. Admin qoidalari fn_is_admin() orqali; servis (Edge Function) service_role bilan yozadi.

-- 1. Bot adminlari (hozir ADMIN_CHAT bitta raqam; keyingi qadamda tg-bot shu jadvaldan oʻqiydi)
create table if not exists public.tg_admins (
  chat_id   bigint primary key,
  label     text,
  active    boolean not null default true,
  added_at  timestamptz not null default now()
);
alter table public.tg_admins enable row level security;
insert into public.tg_admins (chat_id, label) values (255077744, 'asoschi') on conflict do nothing;
drop policy if exists tg_admins_admin_all on public.tg_admins;
create policy tg_admins_admin_all on public.tg_admins for all to authenticated
  using ((select public.fn_is_admin())) with check ((select public.fn_is_admin()));

-- 2. Email sozlamalari: marketing roziligi va obunani bekor qilish tokeni
create table if not exists public.email_prefs (
  user_id        uuid primary key references auth.users(id) on delete cascade,
  marketing      boolean not null default false,
  consent_at     timestamptz,
  consent_source text,
  optout_at      timestamptz,
  token          uuid not null default gen_random_uuid()
);
alter table public.email_prefs enable row level security;
drop policy if exists email_prefs_admin_read on public.email_prefs;
create policy email_prefs_admin_read on public.email_prefs for select to authenticated
  using ((select public.fn_is_admin()));

create or replace function public.fn_set_marketing_consent(p_on boolean, p_source text default 'profil')
returns void language plpgsql security definer set search_path = public as $$
begin
  if auth.uid() is null then raise exception 'not authenticated' using errcode = '42501'; end if;
  insert into public.email_prefs (user_id, marketing, consent_at, consent_source, optout_at)
  values (auth.uid(), p_on, case when p_on then now() end, left(coalesce(p_source,'profil'), 40), case when p_on then null else now() end)
  on conflict (user_id) do update set
    marketing      = excluded.marketing,
    consent_at     = case when excluded.marketing then now() else public.email_prefs.consent_at end,
    consent_source = excluded.consent_source,
    optout_at      = case when excluded.marketing then null else now() end;
end $$;
revoke all on function public.fn_set_marketing_consent(boolean, text) from public, anon;
grant execute on function public.fn_set_marketing_consent(boolean, text) to authenticated;

create or replace function public.fn_email_unsubscribe(p_token uuid)
returns boolean language plpgsql security definer set search_path = public as $$
begin
  update public.email_prefs set marketing = false, optout_at = now() where token = p_token;
  return found;
end $$;
revoke all on function public.fn_email_unsubscribe(uuid) from public;
grant execute on function public.fn_email_unsubscribe(uuid) to anon, authenticated;

-- 3. Yuborishlar va qabul qiluvchilar
create table if not exists public.broadcasts (
  id          bigint generated always as identity primary key,
  kind        text not null check (kind in ('marketing','service')),
  segment     text not null,
  channel     text not null check (channel in ('email','telegram','both')),
  subject     text,
  body        text not null,
  status      text not null default 'draft' check (status in ('draft','approved','sending','sent','cancelled')),
  test_only   boolean not null default true,
  created_by  uuid default auth.uid(),
  created_at  timestamptz not null default now(),
  approved_at timestamptz,
  sent_at     timestamptz
);
alter table public.broadcasts enable row level security;
drop policy if exists broadcasts_admin_all on public.broadcasts;
create policy broadcasts_admin_all on public.broadcasts for all to authenticated
  using ((select public.fn_is_admin())) with check ((select public.fn_is_admin()));

create table if not exists public.broadcast_recipients (
  id           bigint generated always as identity primary key,
  broadcast_id bigint not null references public.broadcasts(id) on delete cascade,
  user_id      uuid   not null references auth.users(id) on delete cascade,
  channel      text   not null check (channel in ('email','telegram')),
  status       text   not null default 'queued' check (status in ('queued','sent','failed','skipped')),
  skip_reason  text,
  provider_id  text,
  error        text,
  sent_at      timestamptz,
  unique (broadcast_id, user_id, channel)
);
create index if not exists broadcast_recipients_user_sent_idx on public.broadcast_recipients (user_id, sent_at desc);
create index if not exists broadcast_recipients_broadcast_idx on public.broadcast_recipients (broadcast_id);
alter table public.broadcast_recipients enable row level security;
drop policy if exists broadcast_recipients_admin_all on public.broadcast_recipients;
create policy broadcast_recipients_admin_all on public.broadcast_recipients for all to authenticated
  using ((select public.fn_is_admin())) with check ((select public.fn_is_admin()));

-- 4. Saytdagi eʼlon paneli: hamma faol eʼlonni koʻradi, yozish faqat admin
create table if not exists public.site_announcements (
  id         bigint generated always as identity primary key,
  text       text not null check (char_length(text) <= 240),
  link       text,
  starts_at  timestamptz not null default now(),
  ends_at    timestamptz,
  active     boolean not null default true,
  created_at timestamptz not null default now()
);
alter table public.site_announcements enable row level security;
drop policy if exists site_announcements_public_read on public.site_announcements;
create policy site_announcements_public_read on public.site_announcements for select to anon, authenticated
  using (active and starts_at <= now() and (ends_at is null or ends_at > now()));
drop policy if exists site_announcements_admin_all on public.site_announcements;
create policy site_announcements_admin_all on public.site_announcements for all to authenticated
  using ((select public.fn_is_admin())) with check ((select public.fn_is_admin()));
