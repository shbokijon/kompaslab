-- 2026-11-06 · Lablar va narxlar: saytda koʻrinish (status) va sotuv (on_sale)
-- status: active = saytda koʻrinadi; draft = yashirin; archived = eski.
-- on_sale: true = hamma uchun sotuvda; false = faqat admin sinovi (paid_pages boʻlsa).
-- Sotuv sharti serverda: paid_pages bor + (on_sale va active, yoki admin).

begin;

-- 1. Sotuv bayrogʻi (standart: sotuvda emas)
alter table public.courses add column if not exists on_sale boolean not null default false;
comment on column public.courses.on_sale is 'Hamma uchun sotuvda. false: faqat admin sinov toʻlovi. Admin paneldan.';
comment on column public.courses.status is 'active: saytda koʻrinadi; draft: yashirin; archived: eski. Admin paneldan.';

-- 2. Saytda sahifasi bor 8 Lab koʻrinadi; Maktab, Research, AI Amaliyot va test-lab yashirin qoladi
update public.courses set status = 'active'
 where slug in ('bachelor-lab','master-lab','phd-lab','gks-lab','usa-lab','daad-lab','tadbirkor-talaba','miggo');

-- 3. Holat matni manbada amaldagi alifboda (saytda alifbo.js yangisiga oʻgiradi)
update public.courses set holat = 'Kutish roʻyxati' where holat = 'Kutish röyxati';

-- 4. Talaba obuna boʻlgan Labni har doim koʻradi (Lab yashirilsa ham profil va kabinetda nomi chiqadi)
drop policy if exists "courses: obunachi koʻradi" on public.courses;
create policy "courses: obunachi koʻradi" on public.courses for select to authenticated
  using (exists (select 1 from public.enrollments e where e.course_id = courses.id and e.user_id = auth.uid()));

-- 5. Ommaviy statistika: st (holat), sale (sotuvda), pp (pullik modul bor), ph (oylik fazalar soni)
create or replace function public.kompas_public_stats()
 returns json
 language sql
 stable security definer
 set search_path to 'public'
as $function$
  select json_build_object(
    'registered', (select count(*) from profiles where role is distinct from 'admin'),
    'last_signup', (select max(created_at) from profiles where role is distinct from 'admin'),
    'waitlist', (select count(distinct email) from waitlist),
    'waitlist_by_lab', coalesce((select json_object_agg(course_slug, n) from (select course_slug, count(*) as n from waitlist group by course_slug) t), '{}'::json),
    'prices', coalesce((select json_object_agg(c.slug, json_build_object(
        'y', coalesce(c.price_yearly, c.price), 'm', c.price_monthly, 's6', c.price_6m, 'h', c.holat,
        'st', c.status, 'sale', (c.on_sale and c.status = 'active'),
        'pp', exists (select 1 from paid_pages p where p.course_slug = c.slug),
        'ph', (select max(cp.phase) from course_phases cp where cp.course_slug = c.slug)))
      from courses c where c.slug <> 'test-lab'), '{}'::json),
    'at', now()
  );
$function$;

-- 6. Buyurtma: on_sale sharti qoʻshildi (qolgan mantiq oʻzgarmagan)
create or replace function public.fn_create_pending_payment(p_course_slug text, p_plan text, p_track text default null::text)
 returns table(order_ref text, order_no bigint, amount bigint, course_title text, plan text, phase integer, track text, phase_modules integer[])
 language plpgsql
 security definer
 set search_path to 'public', 'pg_temp'
as $function$
#variable_conflict use_column
declare
 v_user uuid := auth.uid(); v_c public.courses%rowtype; v_e public.enrollments%rowtype;
 v_has boolean; v_active boolean; v_amount bigint; v_phase int; v_track text; v_max int; v_no bigint; v_mods int[];
 v_kind char(1); v_ref bigint;
begin
 if v_user is null then raise exception 'AUTH_REQUIRED' using errcode='28000'; end if;
 if not public.kompas_account_active() then raise exception 'ACCOUNT_SUSPENDED'; end if;
 if p_plan is null or p_plan not in ('monthly','6m','yearly') then raise exception 'BAD_PLAN'; end if;

 select * into v_c from public.courses where slug=p_course_slug;
 if not found then raise exception 'COURSE_NOT_FOUND'; end if;
 if v_c.slug='test-lab' then
   if not public.fn_is_admin() then raise exception 'COURSE_NOT_FOR_SALE'; end if;
 elsif not exists (select 1 from public.paid_pages where course_slug=v_c.slug) then
   raise exception 'COURSE_NOT_FOR_SALE';
 elsif not (v_c.on_sale and v_c.status='active') and not public.fn_is_admin() then
   raise exception 'COURSE_NOT_FOR_SALE';
 end if;

 v_amount := case p_plan when 'monthly' then v_c.price_monthly when '6m' then v_c.price_6m
                         else coalesce(v_c.price_yearly, v_c.price) end;
 if v_amount is null or v_amount < 1000 then raise exception 'PLAN_NOT_AVAILABLE'; end if;

 select * into v_e from public.enrollments where user_id=v_user and course_id=v_c.id;
 v_has := found;
 v_active := v_has and v_e.payment_status in ('paid','partial') and v_e.frozen_at is null
             and (v_e.expires_at is null or v_e.expires_at>now());
 if v_active and v_e.installment_id is not null and v_e.payment_status<>'paid' then
   raise exception 'INSTALLMENT_ACTIVE';
 end if;
 if v_active and v_e.expires_at is null then raise exception 'ALREADY_ENROLLED'; end if;

 if p_plan='monthly' then
   if v_active and v_e.plan::text in ('6m','yearly') then raise exception 'HAS_FULL_PLAN'; end if;
   select max(cp.phase) into v_max from public.course_phases cp where cp.course_slug=v_c.slug;
   if v_max is null then raise exception 'MONTHLY_NOT_AVAILABLE'; end if;
   v_phase := case when v_has and v_e.plan::text='monthly' then coalesce(v_e.phase,0)+1 else 1 end;
   if v_phase > v_max then raise exception 'ALL_PHASES_PAID'; end if;
   v_track := case when v_has then v_e.track end;
   if exists (select 1 from public.course_phases cp where cp.course_slug=v_c.slug and cp.phase=v_phase and cp.track<>'') then
     v_track := coalesce(v_track, lower(nullif(trim(p_track),'')));
     if v_track is null or not exists (select 1 from public.course_phases cp
          where cp.course_slug=v_c.slug and cp.phase=v_phase and cp.track=v_track) then
       raise exception 'TRACK_REQUIRED';
     end if;
   end if;
   select coalesce(array_agg(x order by x), '{}') into v_mods
     from public.course_phases cp, unnest(cp.module_indexes) x
    where cp.course_slug=v_c.slug and cp.phase=v_phase and (cp.track='' or cp.track=coalesce(v_track,''));
 end if;

 update public.payments p set status='rejected', note=concat_ws('; ', p.note, 'yangi buyurtma bilan almashtirildi')
  where p.user_id=v_user and p.course_id=v_c.id and p.status='pending'
    and p.installment_item_id is null and p.provider_trans_id is null;

 v_kind := case when v_c.slug='test-lab' then 'S' else 'T' end;
 v_ref := public.fn_next_ref(v_kind, 'order');
 insert into public.payments(user_id, course_id, plan, amount, method, status, phase, track, kind, ref_no)
 values (v_user, v_c.id, p_plan::public.enrollment_plan, v_amount, 'click', 'pending', v_phase, v_track, v_kind, v_ref)
 returning payments.order_no into v_no;

 return query select v_kind||v_ref, v_no, v_amount, v_c.title, p_plan, v_phase, v_track, v_mods;
end; $function$;

commit;
