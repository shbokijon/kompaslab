-- 2026-11-19: Modul videolari (asoschi): admin → Videolar boʻlimidan havola qoʻyiladi.
-- Bitta qator = bitta joy: dastur (course_slug) + modul (module_index, M0 = 0) + joy (slot: l1…l9, res).
-- Oʻqish faqat kompas_module_videos() orqali: M0 hammaga, pullik modul faqat shu modulga kirish
-- huquqi borlarga (kompas_my_module_access) va adminga. Jadvalning oʻzi faqat admin uchun.
create table if not exists public.module_videos (
  id bigserial primary key,
  course_slug text not null,
  module_index int not null check (module_index between 0 and 40),
  slot text not null check (slot ~ '^(l[0-9]{1,2}|res)$'),
  provider text not null default 'youtube' check (provider in ('youtube', 'vimeo')),
  video text not null default '' check (length(video) <= 300),
  title text check (length(title) <= 160),
  sec int check (sec between 1 and 7200),
  status text not null default 'active' check (status in ('active', 'off')),
  updated_at timestamptz not null default now(),
  updated_by uuid default auth.uid(),
  unique (course_slug, module_index, slot)
);

alter table public.module_videos enable row level security;
revoke all on public.module_videos from anon;
grant select, insert, update, delete on public.module_videos to authenticated;
grant usage, select on sequence public.module_videos_id_seq to authenticated;

drop policy if exists module_videos_admin on public.module_videos;
create policy module_videos_admin on public.module_videos for all to authenticated
  using (public.fn_is_admin()) with check (public.fn_is_admin());

create or replace function public.fn_module_videos_touch() returns trigger
language plpgsql set search_path = public, pg_temp as $$
begin new.updated_at := now(); new.updated_by := auth.uid(); return new; end $$;
drop trigger if exists trg_module_videos_touch on public.module_videos;
create trigger trg_module_videos_touch before update on public.module_videos
  for each row execute function public.fn_module_videos_touch();

create or replace function public.kompas_module_videos(p_course_slug text, p_module_index int)
returns jsonb language plpgsql stable security definer set search_path = public, pg_temp as $$
declare v jsonb;
begin
  if p_module_index <> 0 and not public.fn_is_admin() then
    if auth.uid() is null or not public.kompas_my_module_access(p_course_slug, p_module_index) then
      return '{}'::jsonb;
    end if;
  end if;
  select coalesce(jsonb_object_agg(slot, jsonb_strip_nulls(jsonb_build_object(
           'p', provider, 'v', video, 'title', title, 'sec', sec))), '{}'::jsonb)
    into v
    from public.module_videos
   where course_slug = p_course_slug and module_index = p_module_index
     and status = 'active' and video <> '';
  return v;
end $$;
revoke all on function public.kompas_module_videos(text, int) from public;
grant execute on function public.kompas_module_videos(text, int) to anon, authenticated;
