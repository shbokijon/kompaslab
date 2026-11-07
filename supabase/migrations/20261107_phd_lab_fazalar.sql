-- PhD Lab oylik fazalari (asoschi tasdigʻi 2026-11-07).
-- I M1–M3, II M4–M5, III M6–M7, IV M8–M9. module_indexes = modules.order_index = paid_pages.module_index.
-- on_sale bu faylda yoqilmaydi: PhD M1–M9 paid_pages ga yuklangach alohida yoqiladi.
begin;
insert into public.course_phases(course_slug, phase, track, module_indexes) values
 ('phd-lab',1,'','{1,2,3}'),('phd-lab',2,'','{4,5}'),('phd-lab',3,'','{6,7}'),('phd-lab',4,'','{8,9}')
on conflict (course_slug, phase, track) do update set module_indexes = excluded.module_indexes;
commit;
