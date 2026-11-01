-- Kompas Lab: additive access grants, audit trail, read-only infrastructure statistics.
-- Safe for existing enrollments; no existing users or payments are modified.
create table if not exists public.access_grants (
 id uuid primary key default gen_random_uuid(),
 user_id uuid not null references public.profiles(id) on delete cascade,
 course_id uuid not null references public.courses(id) on delete cascade,
 module_id uuid references public.modules(id) on delete cascade,
 expires_at timestamptz,
 revoked_at timestamptz,
 note text not null default '',
 granted_by uuid not null references public.profiles(id),
 created_at timestamptz not null default now(),
 constraint grant_note_length check (char_length(note) <= 500),
 constraint grant_expires_future check (expires_at is null or expires_at > created_at)
);
create index if not exists access_grants_lookup on public.access_grants(user_id,course_id,module_id) where revoked_at is null;
alter table public.access_grants enable row level security;
revoke all on public.access_grants from anon, authenticated;
grant select on public.access_grants to authenticated;
drop policy if exists access_grants_read on public.access_grants;
create policy access_grants_read on public.access_grants for select to authenticated
using (user_id = (select auth.uid()) or public.fn_is_admin());

create table if not exists public.admin_audit_logs (
 id bigint generated always as identity primary key,
 actor_id uuid not null,
 target_user_id uuid,
 action text not null,
 details jsonb not null default '{}'::jsonb,
 created_at timestamptz not null default now()
);
create index if not exists admin_audit_created on public.admin_audit_logs(created_at desc);
alter table public.admin_audit_logs enable row level security;
revoke all on public.admin_audit_logs from anon,authenticated;
grant select on public.admin_audit_logs to authenticated;
drop policy if exists admin_audit_owner_read on public.admin_audit_logs;
create policy admin_audit_owner_read on public.admin_audit_logs for select to authenticated using (public.fn_is_admin());

-- Single transactional operation: grant or revoke. Only an existing full admin
-- can perform mutations. Never rely on client-side role flags.
create or replace function public.admin_set_access(
 p_user_id uuid, p_course_id uuid, p_module_id uuid default null,
 p_expires_at timestamptz default null, p_note text default '',
 p_revoke boolean default false
) returns uuid language plpgsql security definer
set search_path = '' as $$
declare v_id uuid; v_actor uuid;
begin
 v_actor := auth.uid();
 if v_actor is null or not public.fn_is_admin() then
   raise exception 'ADMIN_REQUIRED' using errcode='42501';
 end if;
 if not exists (select 1 from public.profiles where id=p_user_id) then
   raise exception 'USER_NOT_FOUND';
 end if;
 if not exists(select 1 from public.courses where id=p_course_id) then
   raise exception 'COURSE_NOT_FOUND';
 end if;
 if p_module_id is not null and not exists
   (select 1 from public.modules where id=p_module_id and course_id=p_course_id) then
   raise exception 'MODULE_NOT_IN_COURSE';
 end if;
 if char_length(coalesce(p_note,'')) > 500 then raise exception 'NOTE_TOO_LONG'; end if;
 if not p_revoke and p_expires_at is not null and p_expires_at <= now() then
   raise exception 'EXPIRY_MUST_BE_IN_FUTURE';
 end if;
 if p_revoke then
   update public.access_grants set revoked_at=now()
   where user_id=p_user_id and course_id=p_course_id
     and module_id is not distinct from p_module_id and revoked_at is null
   returning id into v_id;
 else
   update public.access_grants
     set expires_at=p_expires_at, note=coalesce(p_note,''), granted_by=v_actor,
         created_at=now(), revoked_at=null
   where id=(select id from public.access_grants
             where user_id=p_user_id and course_id=p_course_id
               and module_id is not distinct from p_module_id and revoked_at is null
             order by created_at desc limit 1)
   returning id into v_id;
   if v_id is null then
     insert into public.access_grants(user_id,course_id,module_id,expires_at,note,granted_by)
     values(p_user_id,p_course_id,p_module_id,p_expires_at,coalesce(p_note,''),v_actor)
     returning id into v_id;
   end if;
 end if;
 insert into public.admin_audit_logs(actor_id,target_user_id,action,details)
 values(v_actor,p_user_id,case when p_revoke then 'access.revoke' else 'access.grant' end,
        jsonb_build_object('course_id',p_course_id,'module_id',p_module_id,'expires_at',p_expires_at,'note',p_note));
 return v_id;
end $$;
revoke all on function public.admin_set_access(uuid,uuid,uuid,timestamptz,text,boolean) from public,anon;
grant execute on function public.admin_set_access(uuid,uuid,uuid,timestamptz,text,boolean) to authenticated;

-- Access grants complement (do not overwrite) existing paid enrollments.
-- Keep published state as prerequisite; free lessons remain independently public.
drop policy if exists access_grants_lessons_read on public.lessons;
create policy access_grants_lessons_read on public.lessons for select to authenticated
using (
 status = 'published'
 and exists (
   select 1 from public.modules m join public.access_grants g on g.course_id=m.course_id
   where m.id=lessons.module_id and g.user_id=(select auth.uid())
   and (g.module_id is null or g.module_id=m.id)
   and g.revoked_at is null and (g.expires_at is null or g.expires_at>now())
 )
);
drop policy if exists access_grants_contents_read on public.lesson_contents;
create policy access_grants_contents_read on public.lesson_contents for select to authenticated
using (
 exists (
   select 1 from public.lessons l
   join public.modules m on m.id=l.module_id
   join public.access_grants g on g.course_id=m.course_id
   where l.id=lesson_contents.lesson_id and l.status='published'
   and g.user_id=(select auth.uid()) and (g.module_id is null or g.module_id=m.id)
   and g.revoked_at is null and (g.expires_at is null or g.expires_at>now())
 )
);
-- Supabase SQL stats (not provider billing usage).
create or replace function public.admin_system_stats()
returns jsonb language plpgsql security definer set search_path='' as $$
begin
 if auth.uid() is null or not public.fn_is_admin() then
   raise exception 'ADMIN_REQUIRED' using errcode='42501';
 end if;
 return jsonb_build_object(
   'database_bytes',pg_database_size(current_database()),
   'database_connections', (select count(*) from pg_stat_activity where datname=current_database()),
   'course_count',(select count(*) from public.courses),
   'module_count',(select count(*) from public.modules),
   'lesson_count',(select count(*) from public.lessons),
   'registered_count',(select count(*) from public.profiles),
   'captured_at',now()
 );
end $$;
revoke all on function public.admin_system_stats() from public, anon;
grant execute on function public.admin_system_stats() to authenticated;
