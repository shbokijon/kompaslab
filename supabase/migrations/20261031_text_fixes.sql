-- 2026-10-31 · Dars matnidagi mayda xatolarni admin paneldan tuzatish
-- text_fixes: admin "eski matn → yangi matn" yozadi.
--   page: 'master-lab-m0-2.html' (bitta sahifa), 'master-lab-m0*' (prefiks: butun modul),
--         '*' (hamma sahifa) yoki 'paid:master-lab:3' (pullik modul, serverda qoʻllanadi).
--   status: active (saytda qoʻllanadi) · baked (manba faylga yozildi, endi kerak emas) · off (oʻchirilgan).
-- Ochiq sahifalar tuzatishni js/kompas-ui.js orqali oʻqiydi (anon: faqat active, paid: dan tashqari).
-- Pullik modullar: fn_paid_page() HTML ni qaytarishdan oldin active tuzatishlarni qoʻllaydi.

create table if not exists public.text_fixes (
  id         bigint generated always as identity primary key,
  page       text not null check (char_length(page) between 1 and 200),
  old_text   text not null check (char_length(old_text) between 2 and 600),
  new_text   text not null check (char_length(new_text) <= 600),
  status     text not null default 'active' check (status in ('active', 'baked', 'off')),
  note       text check (note is null or char_length(note) <= 300),
  created_at timestamptz not null default now(),
  created_by uuid default auth.uid(),
  baked_at   timestamptz
);
create index if not exists text_fixes_active_idx on public.text_fixes (status, page);

alter table public.text_fixes enable row level security;

drop policy if exists "text_fixes: ochiq sahifa tuzatishlari" on public.text_fixes;
create policy "text_fixes: ochiq sahifa tuzatishlari"
  on public.text_fixes for select
  using ((status = 'active' and page not like 'paid:%') or public.fn_is_admin());

drop policy if exists "text_fixes: faqat admin yozadi" on public.text_fixes;
create policy "text_fixes: faqat admin yozadi"
  on public.text_fixes for insert with check (public.fn_is_admin());

drop policy if exists "text_fixes: faqat admin yangilaydi" on public.text_fixes;
create policy "text_fixes: faqat admin yangilaydi"
  on public.text_fixes for update using (public.fn_is_admin()) with check (public.fn_is_admin());

drop policy if exists "text_fixes: faqat admin oʻchiradi" on public.text_fixes;
create policy "text_fixes: faqat admin oʻchiradi"
  on public.text_fixes for delete using (public.fn_is_admin());

grant select on public.text_fixes to anon, authenticated;
grant insert, update, delete on public.text_fixes to authenticated;

-- Pullik modul: tuzatishlar serverda qoʻllanadi (matn ochiq roʻyxatga chiqmaydi)
create or replace function public.fn_paid_page(p_course_slug text, p_module_index integer)
 returns jsonb
 language plpgsql
 stable security definer
 set search_path to 'public'
as $function$
declare
  v_uid uuid := auth.uid();
  v_course uuid;
  v_mod uuid;
  v_pos int;
  e enrollments%rowtype;
  v_html text;
  v_ver text;
  f record;
begin
  if v_uid is null then return jsonb_build_object('ok', false, 'reason', 'auth'); end if;
  select id into v_course from courses where slug = p_course_slug;
  if v_course is null then return jsonb_build_object('ok', false, 'reason', 'no_course'); end if;
  select id into v_mod from modules where course_id = v_course and order_index = p_module_index;
  if v_mod is null then return jsonb_build_object('ok', false, 'reason', 'missing'); end if;
  if not public.fn_is_admin() then
    select * into e from enrollments where user_id = v_uid and course_id = v_course;
    if not found or e.payment_status not in ('paid', 'partial') then
      return jsonb_build_object('ok', false, 'reason', 'no_access');
    end if;
    if e.frozen_at is not null then return jsonb_build_object('ok', false, 'reason', 'frozen'); end if;
    if e.expires_at is not null and e.expires_at <= now() then return jsonb_build_object('ok', false, 'reason', 'expired'); end if;
    v_pos := public.fn_module_position(v_mod);
    if e.unlocked_modules is not null and v_pos > e.unlocked_modules then
      return jsonb_build_object('ok', false, 'reason', 'locked', 'unlocked_modules', e.unlocked_modules);
    end if;
  end if;
  select html, version into v_html, v_ver from paid_pages where course_slug = p_course_slug and module_index = p_module_index;
  if v_html is null then return jsonb_build_object('ok', false, 'reason', 'missing'); end if;
  for f in select old_text, new_text from text_fixes
            where status = 'active' and page = 'paid:' || p_course_slug || ':' || p_module_index
            order by id loop
    v_html := replace(v_html, f.old_text, f.new_text);
  end loop;
  return jsonb_build_object('ok', true, 'html', v_html, 'version', v_ver);
end $function$;
