-- 2026-11-06, asoschi qarori: yillik tarif hamma Labda olib tashlanadi. Tariflar: oylik (bitta faza) va 6 oylik.
-- Sabab: 3 yoki 4 oylik "hammasi birdaniga" tarifi oylik narx bilan birga ikkala shartni bajara olmaydi
-- (oyiga oylikdan arzon VA 4 faza × oylikdan qimmat emas); 6 oylik bajaradi, yillik keraksiz.
-- Mavjud yillik obunalar yoʻq (faqat test-lab sinov yozuvi). enrollment_plan enumidagi 'yearly' tarix uchun qoladi.

-- 1) Narxlar: yillik narx yoʻq; eski `price` ustuni 6 oylikka teng (zaxira sifatida ishlatilgan joylar uchun)
update public.courses
   set price_yearly = null,
       price = coalesce(price_6m, price),
       updated_at = now()
 where slug <> 'test-lab';

-- Admin sinovi (S) endi 6 oylik tarif bilan, 1 000 soʻm
update public.courses set price_6m = 1000, updated_at = now() where slug = 'test-lab';

-- 2) Buyurtma: 'yearly' qabul qilinmaydi (RPC toʻgʻridan-toʻgʻri chaqirilsa ham)
do $mig$
declare d text;
begin
  d := pg_get_functiondef('public.fn_create_pending_payment'::regproc);
  d := replace(d, $q$p_plan not in ('monthly','6m','yearly')$q$, $q$p_plan not in ('monthly','6m')$q$);
  d := regexp_replace(d, $q$when '6m' then v_c\.price_6m\s+else coalesce\(v_c\.price_yearly, v_c\.price\) end;$q$, $q$when '6m' then v_c.price_6m end;$q$);
  if position('coalesce(v_c.price_yearly' in d) > 0 or position($q$('monthly','6m','yearly')$q$ in d) > 0 then
    raise exception 'fn_create_pending_payment: kutilgan matn topilmadi, qoʻlda tekshiring';
  end if;
  execute d;

  d := pg_get_functiondef('public.kompas_public_stats'::regproc);
  d := replace(d, $q$'y', coalesce(c.price_yearly, c.price)$q$, $q$'y', c.price_yearly$q$);
  if position('coalesce(c.price_yearly, c.price)' in d) > 0 then
    raise exception 'kompas_public_stats: kutilgan matn topilmadi';
  end if;
  execute d;
end $mig$;
