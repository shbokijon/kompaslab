-- 2026-11-20: Telegram bot ikkinchi admin (@kompaslab_admin). Admin xabarlari tg_admins dagi har faol chatga.
insert into public.tg_admins (chat_id, label) values (8756998537, 'kompaslab_admin') on conflict (chat_id) do update set active = true;

-- Yordam soʻrovi har admin chatiga alohida uzatiladi; xabar raqami faqat chat ichida noyob.
alter table public.tg_support add column if not exists admin_chat_id bigint not null default 255077744;
alter table public.tg_support drop constraint if exists tg_support_pkey;
alter table public.tg_support add primary key (admin_chat_id, admin_message_id);

-- Toʻlov xabari: asoschi uchun dedup kaliti oʻzgarmaydi, boshqa adminlarga ":<chat>" qoʻshiladi.
create or replace function public.fn_tg_on_payment()
 returns trigger language plpgsql security definer set search_path to 'public', 'pg_temp' as $function$
declare
  v_title text; v_slug text; v_ref text; v_exp timestamptz; v_phase int; v_track text;
  v_tarif text; v_lbl text; v_chat bigint; v_msg text; v_name text; v_adm text;
begin
  if not (NEW.status in ('confirmed','paid') and (TG_OP = 'INSERT' or OLD.status not in ('confirmed','paid'))) then
    return NEW;
  end if;

  begin
    select title, slug into v_title, v_slug from public.courses where id = NEW.course_id;
    v_ref := coalesce(NEW.kind, '') || coalesce(NEW.ref_no, NEW.order_no)::text;
    select e.expires_at, e.phase, e.track into v_exp, v_phase, v_track
      from public.enrollments e where e.user_id = NEW.user_id and e.course_id = NEW.course_id;

    v_tarif := public.fn_tg_plan(NEW.plan::text);
    if NEW.plan::text = 'monthly' and v_phase is not null then
      v_lbl := public.fn_tg_phase_label(v_slug, v_phase, v_track);
      v_tarif := v_tarif || ', ' || v_phase || '-bosqich' || coalesce(' (' || v_lbl || ')', '');
    end if;

    v_msg := '✅ Toʻlov qabul qilindi' || E'\n\n'
          || 'Lab: ' || coalesce(v_title, '—') || E'\n'
          || 'Tarif: ' || v_tarif || E'\n'
          || coalesce('Muddat: ' || to_char(v_exp at time zone 'Asia/Tashkent', 'DD.MM.YYYY') || ' gacha' || E'\n', '')
          || 'Summa: ' || public.fn_tg_som(NEW.amount) || E'\n'
          || 'Raqam: ' || v_ref || E'\n\n'
          || 'Darslar kabinetda ochildi: https://kompaslab.uz/';

    select chat_id into v_chat from public.tg_links
     where user_id = NEW.user_id and blocked_at is null;
    if v_chat is not null then
      insert into public.tg_outbox(bot, chat_id, kind, dedup_key, text_src)
      values ('user', v_chat, 'payment_user', 'pay:' || NEW.id, v_msg)
      on conflict (dedup_key) do nothing;
    end if;

    select coalesce(full_name, email, NEW.user_id::text) into v_name from public.profiles where id = NEW.user_id;
    v_adm := 'Toʻlov ' || v_ref || E'\n'
          || 'Talaba: ' || coalesce(v_name, '—') || E'\n'
          || 'Lab: ' || coalesce(v_title, '—') || ' · ' || v_tarif || E'\n'
          || 'Summa: ' || public.fn_tg_som(NEW.amount) || ' · ' || coalesce(NEW.method::text, '') || E'\n'
          || 'Telegram: ' || case when v_chat is null then 'bogʻlanmagan' else 'bogʻlangan' end;
    insert into public.tg_outbox(bot, chat_id, kind, dedup_key, text_src)
    select 'admin', a.chat_id, 'payment_admin',
           'payadm:' || NEW.id || case when a.chat_id = public.fn_tg_admin_chat() then '' else ':' || a.chat_id end,
           v_adm
      from public.tg_admins a where a.active
    on conflict (dedup_key) do nothing;

    perform public.fn_tg_kick_flush();
  exception when others then
    raise warning 'fn_tg_on_payment: %', sqlerrm;
  end;
  return NEW;
end $function$;

create or replace function public.fn_admin_digest_enqueue()
 returns void language plpgsql security definer set search_path to 'public', 'pg_temp' as $function$
declare v_day text := to_char((now() at time zone 'Asia/Tashkent')::date, 'YYYY-MM-DD'); v_txt text;
begin
  v_txt := public.fn_admin_digest_text();
  insert into public.tg_outbox(bot, chat_id, kind, dedup_key, text_src)
  select 'admin', a.chat_id, 'digest',
         'digest:' || v_day || case when a.chat_id = public.fn_tg_admin_chat() then '' else ':' || a.chat_id end,
         v_txt
    from public.tg_admins a where a.active
  on conflict (dedup_key) do nothing;
exception when others then
  raise warning 'fn_admin_digest_enqueue: %', sqlerrm;
end $function$;
