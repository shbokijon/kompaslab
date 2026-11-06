-- 2026-11-06: courses.total_lessons ni qayta hisoblash (trigger qoidasi bilan bir xil: faqat published darslar).
-- Sabab: Master 59 (haqiqiy 58), DAAD 51 (0), PhD 60 (5) eskirgan edi.
update courses c set total_lessons = coalesce((
  select count(l.id) from lessons l join modules m on m.id = l.module_id
  where m.course_id = c.id and l.status = 'published'), 0), updated_at = now()
where c.total_lessons is distinct from coalesce((
  select count(l.id) from lessons l join modules m on m.id = l.module_id
  where m.course_id = c.id and l.status = 'published'), 0);
