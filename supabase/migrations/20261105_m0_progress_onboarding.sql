-- 2026-11-05 · M0 progressi serverda, hisobga bogʻlangan holat, birinchi kirish savoli
-- 1) kompas_m0_events  — dars ochildi / qism ochildi / dars yakunlandi / faol vaqt (javob matni yozilmaydi)
-- 2) kompas_user_state — modul progressi (xp, done, seen, open) qurilmalar orasida; javoblar (notes) yozilmaydi
-- 3) profiles.stage*    — "Hozir qaysi bosqichdasiz?" javobi, faqat RPC orqali
-- 4) kompas_admin_m0_overview() — admin uchun voronka va talabalar roʻyxati

-- ── 1. Voqealar ─────────────────────────────────────────────
create table if not exists public.kompas_m0_events (
  id          bigint generated always as identity primary key,
  user_id     uuid not null default auth.uid() references auth.users(id) on delete cascade,
  lab         text not null check (lab ~ '^[a-z][a-z-]{1,39}$'),
  module      text not null check (module ~ '^m[0-9a-z-]{1,8}$'),
  lesson      text check (lesson is null or lesson ~ '^(l[0-9]{1,2}|hub|yakun)$'),
  section     smallint check (section is null or section between 0 and 3),
  event       text not null check (event in ('view','section','done','active','finish')),
  active_sec  integer not null default 0 check (active_sec between 0 and 900),
  created_at  timestamptz not null default now()
);
comment on table public.kompas_m0_events is 'M0 oʻqish voqealari. Javob matni, email yoki token yozilmaydi. Talaba faqat oʻziniki uchun yozadi, oʻqish faqat admin.';
create index if not exists kompas_m0_events_user_idx on public.kompas_m0_events (user_id, created_at desc);
create index if not exists kompas_m0_events_lab_idx  on public.kompas_m0_events (lab, created_at desc);

alter table public.kompas_m0_events enable row level security;
revoke all on public.kompas_m0_events from anon, authenticated;
grant insert (lab, module, lesson, section, event, active_sec) on public.kompas_m0_events to authenticated;
grant select on public.kompas_m0_events to authenticated;

drop policy if exists m0_events_insert_own on public.kompas_m0_events;
create policy m0_events_insert_own on public.kompas_m0_events
  for insert to authenticated with check (user_id = auth.uid());
drop policy if exists m0_events_admin_read on public.kompas_m0_events;
create policy m0_events_admin_read on public.kompas_m0_events
  for select to authenticated using (public.fn_is_admin());

-- Suiisteʼmoldan himoya: bir foydalanuvchi bir sutkada 3000 tadan ortiq voqea yozolmaydi
create or replace function public.kompas_m0_events_cap() returns trigger
language plpgsql security definer set search_path = public as $$
begin
  if (select count(*) from public.kompas_m0_events
      where user_id = new.user_id and created_at > now() - interval '1 day') >= 3000 then
    return null;
  end if;
  new.created_at := now();
  return new;
end $$;
revoke execute on function public.kompas_m0_events_cap() from public, anon, authenticated;
drop trigger if exists trg_m0_events_cap on public.kompas_m0_events;
create trigger trg_m0_events_cap before insert on public.kompas_m0_events
  for each row execute function public.kompas_m0_events_cap();

-- ── 2. Hisobga bogʻlangan holat ─────────────────────────────
create table if not exists public.kompas_user_state (
  user_id    uuid not null default auth.uid() references auth.users(id) on delete cascade,
  key        text not null check (key ~ '^kompas_[a-z]+_m[0-9a-z]{1,6}_v1$'),
  value      jsonb not null check (jsonb_typeof(value) = 'object' and pg_column_size(value) < 16384),
  updated_at timestamptz not null default now(),
  primary key (user_id, key)
);
comment on table public.kompas_user_state is 'Modul progressi (xp, done, seen, open, lv). Javob matni bu yerga yozilmaydi.';
alter table public.kompas_user_state enable row level security;
revoke all on public.kompas_user_state from anon, authenticated;
grant select, delete on public.kompas_user_state to authenticated;
grant insert (key, value, updated_at), update (key, value, updated_at) on public.kompas_user_state to authenticated;

drop policy if exists user_state_own_read on public.kompas_user_state;
create policy user_state_own_read on public.kompas_user_state
  for select to authenticated using (user_id = auth.uid() or public.fn_is_admin());
drop policy if exists user_state_own_insert on public.kompas_user_state;
create policy user_state_own_insert on public.kompas_user_state
  for insert to authenticated with check (user_id = auth.uid());
drop policy if exists user_state_own_update on public.kompas_user_state;
create policy user_state_own_update on public.kompas_user_state
  for update to authenticated using (user_id = auth.uid()) with check (user_id = auth.uid());
drop policy if exists user_state_own_delete on public.kompas_user_state;
create policy user_state_own_delete on public.kompas_user_state
  for delete to authenticated using (user_id = auth.uid());

-- ── 3. Birinchi kirish savoli ───────────────────────────────
alter table public.profiles add column if not exists stage        text;
alter table public.profiles add column if not exists stage_detail text;
alter table public.profiles add column if not exists works        boolean;
alter table public.profiles add column if not exists onboarded_at timestamptz;

create or replace function public.kompas_save_onboarding(
  p_stage text, p_detail text, p_works boolean, p_goal text default null
) returns void
language plpgsql security definer set search_path = public as $$
begin
  if auth.uid() is null then raise exception 'auth_required'; end if;
  if p_stage not in ('school','college','bachelor','bachelor_done','master','master_done','phd','work') then
    raise exception 'bad_stage';
  end if;
  if p_detail is not null and p_detail !~ '^[a-z0-9_+-]{1,16}$' then raise exception 'bad_detail'; end if;
  if p_goal is not null and p_goal not in ('bachelor','masters','phd','grant','research','work','business','multiple','unsure') then
    raise exception 'bad_goal';
  end if;
  update public.profiles
     set stage = p_stage, stage_detail = p_detail, works = p_works,
         goal = coalesce(p_goal, goal), onboarded_at = now(), updated_at = now()
   where id = auth.uid();
end $$;
revoke execute on function public.kompas_save_onboarding(text,text,boolean,text) from public, anon;
grant execute on function public.kompas_save_onboarding(text,text,boolean,text) to authenticated;

-- ── 4. Admin koʻrinishi ─────────────────────────────────────
create or replace function public.kompas_admin_m0_overview() returns jsonb
language plpgsql stable security definer set search_path = public, auth as $$
declare r jsonb;
begin
  if not public.fn_is_admin() then raise exception 'forbidden'; end if;
  with u as (
    select au.id, au.created_at, au.email_confirmed_at, au.last_sign_in_at,
           p.full_name, p.email, p.stage, p.stage_detail, p.works, p.goal, p.role
      from auth.users au left join public.profiles p on p.id = au.id
  ),
  ev as (select * from public.kompas_m0_events),
  per_user_lab as (
    select user_id, lab,
           count(distinct lesson) filter (where event = 'done')              as lessons_done,
           max(created_at)                                                   as last_seen,
           sum(active_sec)                                                   as active_sec,
           bool_or(event = 'finish')                                         as finished,
           (array_agg(lesson  order by created_at desc) filter (where lesson ~ '^l'))[1]  as last_lesson,
           (array_agg(section order by created_at desc) filter (where section is not null))[1] as last_section
      from ev group by user_id, lab
  ),
  lessons as (
    select lab, lesson,
           count(distinct user_id) filter (where event in ('view','section')) as reached,
           count(distinct user_id) filter (where event = 'done')              as done,
           round(avg(active_sec) filter (where event = 'active'))             as avg_chunk
      from ev where lesson ~ '^l' group by lab, lesson
  )
  select jsonb_build_object(
    'funnel', jsonb_build_object(
      'registered', (select count(*) from u where coalesce(role::text,'student') <> 'admin'),
      'confirmed',  (select count(*) from u where email_confirmed_at is not null and coalesce(role::text,'student') <> 'admin'),
      'onboarded',  (select count(*) from u where stage is not null),
      'started',    (select count(distinct user_id) from ev),
      'lesson1',    (select count(distinct user_id) from ev where event = 'done'),
      'finished',   (select count(distinct user_id) from ev where event = 'finish')
    ),
    'labs', coalesce((select jsonb_agg(jsonb_build_object(
        'lab', lab, 'users', users, 'finished', fin, 'minutes', mins) order by users desc)
      from (select lab, count(*) users, count(*) filter (where finished) fin,
                   round(sum(active_sec)/60.0) mins from per_user_lab group by lab) x), '[]'::jsonb),
    'lessons', coalesce((select jsonb_agg(to_jsonb(l) order by l.lab, l.lesson) from lessons l), '[]'::jsonb),
    'users', coalesce((select jsonb_agg(jsonb_build_object(
        'name', u.full_name, 'email', u.email, 'stage', u.stage, 'detail', u.stage_detail, 'works', u.works,
        'goal', u.goal, 'signed_up', u.created_at, 'confirmed', u.email_confirmed_at is not null,
        'lab', pl.lab, 'done', pl.lessons_done, 'last_lesson', pl.last_lesson, 'last_section', pl.last_section,
        'minutes', round(coalesce(pl.active_sec,0)/60.0), 'last_seen', pl.last_seen, 'finished', pl.finished)
        order by coalesce(pl.last_seen, u.created_at) desc)
      from u left join per_user_lab pl on pl.user_id = u.id
      where coalesce(u.role::text,'student') <> 'admin'), '[]'::jsonb)
  ) into r;
  return r;
end $$;
revoke execute on function public.kompas_admin_m0_overview() from public, anon;
grant execute on function public.kompas_admin_m0_overview() to authenticated;
