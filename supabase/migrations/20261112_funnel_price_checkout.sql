-- 2026-11-12: Voronkaning oʻrta qadamlari: narxni koʻrish va toʻlov sahifasini ochish.
-- Mijoz yozadi (anon ham), lekin faqat shu RPC orqali: 2 ta voqea, uzunlik cheklovi,
-- odam + Lab + kun boʻyicha bitta yozuv (dedup), umumiy tezlik chegarasi.
-- Toʻlov urinishi alohida yozilmaydi: u payments jadvalida (fn_create_pending_payment).

alter table public.conversion_events drop constraint if exists conversion_events_event_name_check;
alter table public.conversion_events add constraint conversion_events_event_name_check
  check (event_name = any (array['cta_clicked','m0_started','m0_completed','price_viewed','checkout_started',
                                 'payment_completed','first_task_completed','refund_requested']));

create or replace function public.kompas_track_event(
  p_event text,
  p_vid   text,
  p_slug  text  default null,
  p_path  text  default null,
  p_props jsonb default null
) returns boolean
language plpgsql
security definer
set search_path to 'public', 'pg_temp'
as $$
declare
  v_uid  uuid := auth.uid();
  v_vid  text := case when p_vid ~ '^[a-z0-9]{10,40}$' then p_vid end;
  v_slug text := case when p_slug ~ '^[a-z0-9-]{2,40}$' then p_slug end;
  v_path text := case when p_path ~ '^/[A-Za-z0-9._/-]{0,120}$' then p_path end;
  v_day  date := (now() at time zone 'Asia/Tashkent')::date;
  v_props jsonb := '{}'::jsonb;
  n int;
begin
  if p_event not in ('price_viewed', 'checkout_started') then return false; end if;
  if v_uid is null and v_vid is null then return false; end if;
  if v_slug is not null and not exists (select 1 from courses where slug = v_slug) then v_slug := null; end if;

  if p_props is not null and jsonb_typeof(p_props) = 'object' then
    select coalesce(jsonb_object_agg(k, left(p_props->>k, 20)), '{}'::jsonb) into v_props
    from unnest(array['plan', 'track']) k
    where p_props ? k and jsonb_typeof(p_props->k) = 'string';
  end if;

  select count(*) into n from conversion_events
  where source = 'server' and created_at > now() - interval '1 minute';
  if n >= 200 then return false; end if;

  insert into conversion_events(event_name, user_id, visitor_id, course_slug, page_path,
                                source, trust_level, properties, dedup_key)
  values (p_event, v_uid, v_vid, v_slug, v_path, 'server', 'self_reported', v_props,
          p_event || ':' || coalesce(v_uid::text, v_vid) || ':' || coalesce(v_slug, '-') || ':' || v_day)
  on conflict (dedup_key) do nothing;
  return true;
end $$;

revoke all on function public.kompas_track_event(text, text, text, text, jsonb) from public;
grant execute on function public.kompas_track_event(text, text, text, text, jsonb) to anon, authenticated;
