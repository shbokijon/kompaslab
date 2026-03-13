-- ═══════════════════════════════════════════════════════════════════════
--  KOMPAS LAB — Supabase SQL Sxemasi
--  Versiya: 2.0  |  Jadvallar: 11 ta
--
--  ISHLATISH:
--    Supabase → SQL Editor → New query → Bu faylni yapıştır → Run
--
--  TARTIB (muhim — o'zgartirmang):
--    1. Extensions
--    2. ENUM turlari
--    3. Jadvallar (foreign key tartibida)
--    4. Indekslar
--    5. Triggerlar va funksiyalar
--    6. Row Level Security (RLS)
--    7. Seed ma'lumotlar (4 kurs + modullar)
-- ═══════════════════════════════════════════════════════════════════════


-- ═══════════════════════════════════════════════════════════════════════
--  0. TOZALASH (qayta ishga tushirishdan oldin)
--     Agar birinchi marta ishlatsangiz — bu blokni o'tkazib yuboring
-- ═══════════════════════════════════════════════════════════════════════
/*
DROP TABLE IF EXISTS coming_soon   CASCADE;
DROP TABLE IF EXISTS waitlist      CASCADE;
DROP TABLE IF EXISTS payments      CASCADE;
DROP TABLE IF EXISTS notes         CASCADE;
DROP TABLE IF EXISTS progress      CASCADE;
DROP TABLE IF EXISTS enrollments   CASCADE;
DROP TABLE IF EXISTS materials     CASCADE;
DROP TABLE IF EXISTS lessons       CASCADE;
DROP TABLE IF EXISTS modules       CASCADE;
DROP TABLE IF EXISTS courses       CASCADE;
DROP TABLE IF EXISTS profiles      CASCADE;

DROP TYPE IF EXISTS user_role;
DROP TYPE IF EXISTS course_status;
DROP TYPE IF EXISTS lesson_status;
DROP TYPE IF EXISTS payment_status;
DROP TYPE IF EXISTS payment_method;
DROP TYPE IF EXISTS enrollment_plan;
*/


-- ═══════════════════════════════════════════════════════════════════════
--  1. EXTENSIONS
-- ═══════════════════════════════════════════════════════════════════════

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";    -- UUID generatsiya
CREATE EXTENSION IF NOT EXISTS "pg_trgm";      -- Matn qidirish (ILIKE tezligi)


-- ═══════════════════════════════════════════════════════════════════════
--  2. ENUM TURLARI
-- ═══════════════════════════════════════════════════════════════════════

CREATE TYPE user_role AS ENUM (
  'student',    -- Oddiy talaba
  'admin'       -- Admin/Mentor (Shokhrukh)
);

CREATE TYPE course_status AS ENUM (
  'active',     -- Faol — sotilmoqda
  'draft',      -- Draft — ko'rinmaydi
  'archived'    -- Arxiv — eski kurs
);

CREATE TYPE lesson_status AS ENUM (
  'draft',      -- Ko'rinmaydi
  'published'   -- Ko'rinadi (yozilgan talabalar uchun)
);

CREATE TYPE payment_status AS ENUM (
  'pending',    -- To'lov kutilmoqda (admin tasdiqlashi kerak)
  'confirmed',  -- Admin tasdiqladi → enrollment faollashadi
  'paid',       -- To'langan (Click/Payme orqali avtomatik)
  'rejected',   -- Admin rad etdi
  'failed',     -- Texnik xatolik
  'refunded'    -- Qaytarilgan
);

CREATE TYPE payment_method AS ENUM (
  'click',      -- Click.uz
  'payme',      -- Payme
  'bank',       -- Bank o'tkazma
  'cash',       -- Naqd (admin qo'lda)
  'admin'       -- Admin tomonidan bepul berilgan
);

CREATE TYPE enrollment_plan AS ENUM (
  'starter'     -- Yagona tarif (barcha kurslarda bir xil)
);


-- ═══════════════════════════════════════════════════════════════════════
--  3. JADVALLAR
-- ═══════════════════════════════════════════════════════════════════════


-- ─────────────────────────────────────────────
--  3.1  PROFILES — Foydalanuvchi profili
--       auth.users bilan 1:1 bog'liq
-- ─────────────────────────────────────────────
CREATE TABLE profiles (
  id           UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  email        TEXT NOT NULL UNIQUE,
  first_name   TEXT NOT NULL DEFAULT '',
  last_name    TEXT NOT NULL DEFAULT '',
  full_name    TEXT GENERATED ALWAYS AS (first_name || ' ' || last_name) STORED,
  phone        TEXT,
  education    TEXT,                    -- 'bachelor', 'master', 'phd', ...
  goal         TEXT,                    -- 'masters', 'phd', 'grant', ...
  role         user_role NOT NULL DEFAULT 'student',
  avatar_url   TEXT,
  notes        TEXT,                    -- Admin izohi (faqat admin ko'radi)
  created_at   TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at   TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

COMMENT ON TABLE profiles IS 'Foydalanuvchi profili — auth.users bilan 1:1';


-- ─────────────────────────────────────────────
--  3.2  COURSES — Kurslar
-- ─────────────────────────────────────────────
CREATE TABLE courses (
  id           UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  slug         TEXT NOT NULL UNIQUE,   -- 'eyuf-lab', 'phd-lab', ...
  title        TEXT NOT NULL,
  description  TEXT,
  emoji        TEXT DEFAULT '📚',
  status       course_status NOT NULL DEFAULT 'draft',

  -- Narx (yagona tarif — so'mda)
  price          BIGINT NOT NULL DEFAULT 499000,
  -- Sxema muvofiqligini saqlash uchun (auth.js ishlatadi)
  price_starter  BIGINT GENERATED ALWAYS AS (price) STORED,
  price_scholar  BIGINT GENERATED ALWAYS AS (price) STORED,
  price_elite    BIGINT GENERATED ALWAYS AS (price) STORED,

  -- Meta
  total_modules   INT NOT NULL DEFAULT 0,   -- avtomatik yangilanadi
  total_lessons   INT NOT NULL DEFAULT 0,   -- avtomatik yangilanadi
  created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

COMMENT ON TABLE courses IS '4 ta asosiy kurs. price — yagona narx. price_starter/scholar/elite — muvofiqlik uchun computed.';


-- ─────────────────────────────────────────────
--  3.3  MODULES — Kurs modullari
-- ─────────────────────────────────────────────
CREATE TABLE modules (
  id           UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  course_id    UUID NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
  title        TEXT NOT NULL,
  description  TEXT,
  order_index  INT NOT NULL DEFAULT 0,    -- 0, 1, 2, ... (Modul 0 bepul)
  is_free      BOOLEAN NOT NULL DEFAULT FALSE,  -- Modul 0 uchun TRUE
  is_locked    BOOLEAN NOT NULL DEFAULT FALSE,  -- Qulflangan (hali yo'q)
  created_at   TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at   TIMESTAMPTZ NOT NULL DEFAULT NOW(),

  UNIQUE (course_id, order_index)   -- Bir kursda bir xil tartib bo'lmaydi
);

COMMENT ON TABLE modules IS 'Har kursning modullari. Modul 0 — bepul preview';


-- ─────────────────────────────────────────────
--  3.4  LESSONS — Darslar
-- ─────────────────────────────────────────────
CREATE TABLE lessons (
  id           UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  module_id    UUID NOT NULL REFERENCES modules(id) ON DELETE CASCADE,
  title        TEXT NOT NULL,
  description  TEXT,
  vimeo_url    TEXT,                    -- https://player.vimeo.com/video/XXXXXX
  order_index  INT NOT NULL DEFAULT 1,
  duration     TEXT,                    -- '20 daqiqa', '1 soat 10 daqiqa'
  duration_sec INT,                     -- sekundlarda (progress tracking uchun)
  is_free      BOOLEAN NOT NULL DEFAULT FALSE,
  status       lesson_status NOT NULL DEFAULT 'draft',
  created_at   TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at   TIMESTAMPTZ NOT NULL DEFAULT NOW(),

  UNIQUE (module_id, order_index)
);

COMMENT ON TABLE lessons IS 'Har modulning darslari. Vimeo URL — domain-locked embed';


-- ─────────────────────────────────────────────
--  3.5  MATERIALS — Dars materiallari
--       Har dars uchun 0..N ta material (PDF, docx)
-- ─────────────────────────────────────────────
CREATE TABLE materials (
  id           UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  lesson_id    UUID NOT NULL REFERENCES lessons(id) ON DELETE CASCADE,
  title        TEXT NOT NULL,             -- 'SoP Framework PDF'
  file_url     TEXT NOT NULL,             -- Google Drive yoki Supabase Storage URL
  file_type    TEXT NOT NULL DEFAULT 'pdf',   -- 'pdf', 'docx', 'xlsx', 'zip'
  file_size    TEXT,                      -- '2.4 MB'
  order_index  INT NOT NULL DEFAULT 1,
  created_at   TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

COMMENT ON TABLE materials IS 'Dars materiallari: PDF, docx va boshqalar';


-- ─────────────────────────────────────────────
--  3.6  ENROLLMENTS — Kursga yozilish
-- ─────────────────────────────────────────────
CREATE TABLE enrollments (
  id               UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id          UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  course_id        UUID NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
  plan             enrollment_plan NOT NULL DEFAULT 'starter',
  payment_status   payment_status NOT NULL DEFAULT 'pending',
  payment_id       UUID REFERENCES payments(id),   -- to'lov yozuvi
  enrolled_at      TIMESTAMPTZ,                     -- to'lov tasdiqlanganda
  expires_at       TIMESTAMPTZ,                     -- umrbod = NULL
  created_at       TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at       TIMESTAMPTZ NOT NULL DEFAULT NOW(),

  UNIQUE (user_id, course_id)   -- Bir kursga faqat bir marta yozilish
);

COMMENT ON TABLE enrollments IS 'Kim qaysi kursga yozilgan. payment_status=paid bo\'lsagina dashboard ochiladi';


-- ─────────────────────────────────────────────
--  3.7  PAYMENTS — To'lovlar
-- ─────────────────────────────────────────────
CREATE TABLE payments (
  id             UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id        UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  course_id      UUID NOT NULL REFERENCES courses(id),
  plan           enrollment_plan NOT NULL,
  amount         BIGINT NOT NULL,            -- so'mda
  method         payment_method NOT NULL DEFAULT 'click',
  status         payment_status NOT NULL DEFAULT 'pending',
  click_order_id TEXT,                       -- Click.uz order ID
  note           TEXT,                       -- Admin izohi
  confirmed_at   TIMESTAMPTZ,
  confirmed_by   TEXT,                       -- 'admin_manual', 'click_webhook'
  created_at     TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at     TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

COMMENT ON TABLE payments IS 'Barcha to\'lovlar tarixi. Click.uz webhook va admin qo\'lda tasdiqlash';


-- ─────────────────────────────────────────────
--  3.8  PROGRESS — Dars ko'rish tarixi
-- ─────────────────────────────────────────────
CREATE TABLE progress (
  id              UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id         UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  lesson_id       UUID NOT NULL REFERENCES lessons(id) ON DELETE CASCADE,
  completed       BOOLEAN NOT NULL DEFAULT FALSE,
  watched_percent INT NOT NULL DEFAULT 0 CHECK (watched_percent BETWEEN 0 AND 100),
  completed_at    TIMESTAMPTZ,
  last_watched_at TIMESTAMPTZ DEFAULT NOW(),
  created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),

  UNIQUE (user_id, lesson_id)
);

COMMENT ON TABLE progress IS 'Talabaning har dars ko\'rish holati. 95% watched = completed';


-- ─────────────────────────────────────────────
--  3.9  NOTES — Talaba konspektlari
-- ─────────────────────────────────────────────
CREATE TABLE notes (
  id          UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id     UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  lesson_id   UUID NOT NULL REFERENCES lessons(id) ON DELETE CASCADE,
  content     TEXT NOT NULL DEFAULT '',      -- Markdown formatda
  updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),

  UNIQUE (user_id, lesson_id)
);

COMMENT ON TABLE notes IS 'Talabaning dars konspektlari — auto-save 3 soniyada';


-- ─────────────────────────────────────────────
--  3.10  WAITLIST — "Tez orada" email ro'yxati
-- ─────────────────────────────────────────────
CREATE TABLE waitlist (
  id           UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  email        TEXT NOT NULL,
  course_slug  TEXT NOT NULL,              -- 'gks-lab', 'ikki-miya', 'notion-shablonlar'
  source       TEXT DEFAULT 'landing',    -- 'landing', 'popup', 'social'
  notified     BOOLEAN NOT NULL DEFAULT FALSE,
  added_at     TIMESTAMPTZ NOT NULL DEFAULT NOW(),

  UNIQUE (email, course_slug)
);

COMMENT ON TABLE waitlist IS 'Coming soon kurslarga email ro\'yxati. Launch paytida email yuborish uchun';


-- ─────────────────────────────────────────────
--  3.11  COMING_SOON — "Tez orada" mahsulotlar
--        Admin panel orqali boshqariladi
-- ─────────────────────────────────────────────
CREATE TABLE coming_soon (
  id           UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  slug         TEXT NOT NULL UNIQUE,       -- 'gks-lab', 'ikki-miya', ...
  title        TEXT NOT NULL,
  description  TEXT,
  emoji        TEXT DEFAULT '🔜',
  is_visible   BOOLEAN NOT NULL DEFAULT TRUE,
  launch_date  TEXT,                       -- '2025 Q3', 'Tez orada', ...
  waitlist_count INT NOT NULL DEFAULT 0,  -- denormalized — tezroq o'qish uchun
  order_index  INT NOT NULL DEFAULT 0,
  created_at   TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at   TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

COMMENT ON TABLE coming_soon IS 'Landing page da ko\'rinadigan "Tez orada" mahsulotlar';


-- ═══════════════════════════════════════════════════════════════════════
--  4. INDEKSLAR — Tez qidirish uchun
-- ═══════════════════════════════════════════════════════════════════════

-- Profiles
CREATE INDEX idx_profiles_email     ON profiles(email);
CREATE INDEX idx_profiles_role      ON profiles(role);

-- Courses
CREATE INDEX idx_courses_slug       ON courses(slug);
CREATE INDEX idx_courses_status     ON courses(status);

-- Modules
CREATE INDEX idx_modules_course     ON modules(course_id, order_index);

-- Lessons
CREATE INDEX idx_lessons_module     ON lessons(module_id, order_index);
CREATE INDEX idx_lessons_status     ON lessons(status);
CREATE INDEX idx_lessons_free       ON lessons(is_free) WHERE is_free = TRUE;

-- Enrollments
CREATE INDEX idx_enroll_user        ON enrollments(user_id);
CREATE INDEX idx_enroll_course      ON enrollments(course_id);
CREATE INDEX idx_enroll_status      ON enrollments(payment_status);
CREATE INDEX idx_enroll_user_course ON enrollments(user_id, course_id);

-- Payments
CREATE INDEX idx_payments_user      ON payments(user_id);
CREATE INDEX idx_payments_status    ON payments(status);
CREATE INDEX idx_payments_created   ON payments(created_at DESC);

-- Progress
CREATE INDEX idx_progress_user      ON progress(user_id);
CREATE INDEX idx_progress_lesson    ON progress(lesson_id);
CREATE INDEX idx_progress_user_les  ON progress(user_id, lesson_id);

-- Notes
CREATE INDEX idx_notes_user_lesson  ON notes(user_id, lesson_id);

-- Waitlist
CREATE INDEX idx_waitlist_course    ON waitlist(course_slug);
CREATE INDEX idx_waitlist_email     ON waitlist(email);


-- ═══════════════════════════════════════════════════════════════════════
--  5. TRIGGERLAR VA FUNKSIYALAR
-- ═══════════════════════════════════════════════════════════════════════


-- ─────────────────────────────────────────────
--  5.1  updated_at — Avtomatik yangilash
-- ─────────────────────────────────────────────
CREATE OR REPLACE FUNCTION fn_updated_at()
RETURNS TRIGGER LANGUAGE plpgsql AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$;

-- Barcha updated_at ustunli jadvallar uchun
CREATE TRIGGER trg_profiles_updated    BEFORE UPDATE ON profiles    FOR EACH ROW EXECUTE FUNCTION fn_updated_at();
CREATE TRIGGER trg_courses_updated     BEFORE UPDATE ON courses     FOR EACH ROW EXECUTE FUNCTION fn_updated_at();
CREATE TRIGGER trg_modules_updated     BEFORE UPDATE ON modules     FOR EACH ROW EXECUTE FUNCTION fn_updated_at();
CREATE TRIGGER trg_lessons_updated     BEFORE UPDATE ON lessons     FOR EACH ROW EXECUTE FUNCTION fn_updated_at();
CREATE TRIGGER trg_enrollments_updated BEFORE UPDATE ON enrollments FOR EACH ROW EXECUTE FUNCTION fn_updated_at();
CREATE TRIGGER trg_payments_updated    BEFORE UPDATE ON payments    FOR EACH ROW EXECUTE FUNCTION fn_updated_at();
CREATE TRIGGER trg_coming_soon_updated BEFORE UPDATE ON coming_soon FOR EACH ROW EXECUTE FUNCTION fn_updated_at();


-- ─────────────────────────────────────────────
--  5.2  Yangi foydalanuvchi → Profil avtomatik yaratish
--       auth.users ga yozilganda trigger ishlaydi
-- ─────────────────────────────────────────────
CREATE OR REPLACE FUNCTION fn_create_profile()
RETURNS TRIGGER LANGUAGE plpgsql SECURITY DEFINER AS $$
DECLARE
  fname TEXT;
  lname TEXT;
BEGIN
  -- full_name dan ism ajratish (agar metadata da bo'lsa)
  fname := COALESCE(
    NEW.raw_user_meta_data->>'first_name',
    SPLIT_PART(COALESCE(NEW.raw_user_meta_data->>'full_name', ''), ' ', 1),
    ''
  );
  lname := COALESCE(
    NEW.raw_user_meta_data->>'last_name',
    NULLIF(SPLIT_PART(COALESCE(NEW.raw_user_meta_data->>'full_name', ''), ' ', 2), ''),
    ''
  );

  INSERT INTO profiles (
    id,
    email,
    first_name,
    last_name,
    phone,
    role,
    created_at,
    updated_at
  ) VALUES (
    NEW.id,
    NEW.email,
    fname,
    lname,
    NEW.raw_user_meta_data->>'phone',
    'student',
    NOW(),
    NOW()
  )
  ON CONFLICT (id) DO NOTHING;  -- Agar allaqachon yaratilgan bo'lsa o'tkazib yuborish

  RETURN NEW;
END;
$$;

CREATE TRIGGER trg_create_profile
  AFTER INSERT ON auth.users
  FOR EACH ROW
  EXECUTE FUNCTION fn_create_profile();


-- ─────────────────────────────────────────────
--  5.3  Progress 95% → Avtomatik completed = true
-- ─────────────────────────────────────────────
CREATE OR REPLACE FUNCTION fn_auto_complete_lesson()
RETURNS TRIGGER LANGUAGE plpgsql AS $$
BEGIN
  IF NEW.watched_percent >= 95 AND NOT NEW.completed THEN
    NEW.completed    = TRUE;
    NEW.completed_at = NOW();
  END IF;
  RETURN NEW;
END;
$$;

CREATE TRIGGER trg_auto_complete
  BEFORE INSERT OR UPDATE ON progress
  FOR EACH ROW
  EXECUTE FUNCTION fn_auto_complete_lesson();


-- ─────────────────────────────────────────────
--  5.4  Payment confirmed → Enrollment avtomatik aktivlash
-- ─────────────────────────────────────────────
CREATE OR REPLACE FUNCTION fn_activate_enrollment()
RETURNS TRIGGER LANGUAGE plpgsql SECURITY DEFINER AS $$
BEGIN
  -- 'confirmed' (admin qo'lda) yoki 'paid' (Click/Payme avtomatik) bo'lganda ishlaydi
  IF NEW.status IN ('confirmed', 'paid')
     AND (OLD.status IS NULL OR OLD.status NOT IN ('confirmed', 'paid'))
  THEN
    INSERT INTO enrollments (
      user_id, course_id, plan, payment_status, payment_id, enrolled_at
    )
    VALUES (
      NEW.user_id, NEW.course_id, NEW.plan, 'paid', NEW.id, NOW()
    )
    ON CONFLICT (user_id, course_id) DO UPDATE SET
      payment_status = 'paid',
      payment_id     = NEW.id,
      enrolled_at    = NOW(),
      plan           = NEW.plan,
      updated_at     = NOW();
  END IF;
  RETURN NEW;
END;
$$;

CREATE TRIGGER trg_activate_enrollment
  AFTER INSERT OR UPDATE ON payments
  FOR EACH ROW
  EXECUTE FUNCTION fn_activate_enrollment();


-- ─────────────────────────────────────────────
--  5.5  Kurs statistikasini yangilash
--       Modul/Dars qo'shilganda total_modules, total_lessons yangilanadi
-- ─────────────────────────────────────────────
CREATE OR REPLACE FUNCTION fn_update_course_stats()
RETURNS TRIGGER LANGUAGE plpgsql AS $$
DECLARE
  cid UUID;
BEGIN
  -- Trigger qaysi jadvaldan kelganini aniqlash
  IF TG_TABLE_NAME = 'modules' THEN
    cid := COALESCE(NEW.course_id, OLD.course_id);
    UPDATE courses SET
      total_modules = (SELECT COUNT(*) FROM modules WHERE course_id = cid),
      updated_at    = NOW()
    WHERE id = cid;

  ELSIF TG_TABLE_NAME = 'lessons' THEN
    SELECT m.course_id INTO cid
    FROM modules m
    WHERE m.id = COALESCE(NEW.module_id, OLD.module_id);

    UPDATE courses SET
      total_lessons = (
        SELECT COUNT(l.id)
        FROM lessons l
        JOIN modules m ON l.module_id = m.id
        WHERE m.course_id = cid AND l.status = 'published'
      ),
      updated_at = NOW()
    WHERE id = cid;
  END IF;

  RETURN COALESCE(NEW, OLD);
END;
$$;

CREATE TRIGGER trg_modules_stats
  AFTER INSERT OR UPDATE OR DELETE ON modules
  FOR EACH ROW EXECUTE FUNCTION fn_update_course_stats();

CREATE TRIGGER trg_lessons_stats
  AFTER INSERT OR UPDATE OR DELETE ON lessons
  FOR EACH ROW EXECUTE FUNCTION fn_update_course_stats();


-- ─────────────────────────────────────────────
--  5.6  Waitlist hisoblagichi yangilash
-- ─────────────────────────────────────────────
CREATE OR REPLACE FUNCTION fn_update_waitlist_count()
RETURNS TRIGGER LANGUAGE plpgsql AS $$
BEGIN
  UPDATE coming_soon SET
    waitlist_count = (
      SELECT COUNT(*) FROM waitlist
      WHERE course_slug = COALESCE(NEW.course_slug, OLD.course_slug)
    )
  WHERE slug = COALESCE(NEW.course_slug, OLD.course_slug);
  RETURN COALESCE(NEW, OLD);
END;
$$;

CREATE TRIGGER trg_waitlist_count
  AFTER INSERT OR DELETE ON waitlist
  FOR EACH ROW EXECUTE FUNCTION fn_update_waitlist_count();


-- ─────────────────────────────────────────────
--  5.7  Foydalanuvchi progress foizini hisoblash
--       FUNCTION — dashboard da chaqiriladi
-- ─────────────────────────────────────────────
CREATE OR REPLACE FUNCTION fn_get_course_progress(
  p_user_id   UUID,
  p_course_id UUID
)
RETURNS TABLE (
  total_lessons     INT,
  completed_lessons INT,
  progress_pct      INT,
  last_active_at    TIMESTAMPTZ
)
LANGUAGE plpgsql AS $$
BEGIN
  RETURN QUERY
  WITH lesson_ids AS (
    SELECT l.id
    FROM lessons l
    JOIN modules m ON l.module_id = m.id
    WHERE m.course_id = p_course_id
      AND l.status = 'published'
  ),
  user_progress AS (
    SELECT pr.lesson_id, pr.completed, pr.last_watched_at
    FROM progress pr
    WHERE pr.user_id = p_user_id
      AND pr.lesson_id IN (SELECT id FROM lesson_ids)
  )
  SELECT
    (SELECT COUNT(*)::INT FROM lesson_ids)            AS total_lessons,
    (SELECT COUNT(*)::INT FROM user_progress WHERE completed = TRUE) AS completed_lessons,
    CASE
      WHEN (SELECT COUNT(*) FROM lesson_ids) = 0 THEN 0
      ELSE (
        (SELECT COUNT(*)::FLOAT FROM user_progress WHERE completed = TRUE) /
        (SELECT COUNT(*)::FLOAT FROM lesson_ids) * 100
      )::INT
    END                                                AS progress_pct,
    (SELECT MAX(last_watched_at) FROM user_progress)  AS last_active_at;
END;
$$;


-- ═══════════════════════════════════════════════════════════════════════
--  6. ROW LEVEL SECURITY (RLS)
--     Qoida: Har bir foydalanuvchi FAQAT O'Z ma'lumotini ko'radi
--     Admin — barcha ma'lumotlarni ko'radi va tahrirlaydi
-- ═══════════════════════════════════════════════════════════════════════


-- ─────────────────────────────────────────────
--  Yordamchi funksiya: foydalanuvchi admin ekanini tekshirish
-- ─────────────────────────────────────────────
CREATE OR REPLACE FUNCTION fn_is_admin()
RETURNS BOOLEAN LANGUAGE plpgsql SECURITY DEFINER AS $$
BEGIN
  RETURN EXISTS (
    SELECT 1 FROM profiles
    WHERE id = auth.uid() AND role = 'admin'
  );
END;
$$;


-- ─────────────────────────────────────────────
--  6.1  PROFILES
-- ─────────────────────────────────────────────
ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;

CREATE POLICY "profiles: o'z profilini ko'rish"
  ON profiles FOR SELECT
  USING (auth.uid() = id OR fn_is_admin());

CREATE POLICY "profiles: o'z profilini yangilash"
  ON profiles FOR UPDATE
  USING (auth.uid() = id OR fn_is_admin())
  WITH CHECK (auth.uid() = id OR fn_is_admin());

CREATE POLICY "profiles: trigger orqali yaratish"
  ON profiles FOR INSERT
  WITH CHECK (auth.uid() = id OR fn_is_admin());

CREATE POLICY "profiles: admin o'chirishi"
  ON profiles FOR DELETE
  USING (fn_is_admin());


-- ─────────────────────────────────────────────
--  6.2  COURSES — Hammaga ochiq (o'qish)
--       Faqat admin tahrirlaydi
-- ─────────────────────────────────────────────
ALTER TABLE courses ENABLE ROW LEVEL SECURITY;

CREATE POLICY "courses: barchaga ko'rinadi"
  ON courses FOR SELECT
  USING (status = 'active' OR fn_is_admin());

CREATE POLICY "courses: faqat admin yozadi"
  ON courses FOR INSERT
  WITH CHECK (fn_is_admin());

CREATE POLICY "courses: faqat admin yangilaydi"
  ON courses FOR UPDATE
  USING (fn_is_admin());

CREATE POLICY "courses: faqat admin o'chiradi"
  ON courses FOR DELETE
  USING (fn_is_admin());


-- ─────────────────────────────────────────────
--  6.3  MODULES — Hammaga ochiq (o'qish)
-- ─────────────────────────────────────────────
ALTER TABLE modules ENABLE ROW LEVEL SECURITY;

CREATE POLICY "modules: barchaga ko'rinadi"
  ON modules FOR SELECT
  USING (TRUE);

CREATE POLICY "modules: faqat admin boshqaradi"
  ON modules FOR ALL
  USING (fn_is_admin())
  WITH CHECK (fn_is_admin());


-- ─────────────────────────────────────────────
--  6.4  LESSONS
--       Published + is_free → hamma ko'radi
--       Published + to'liq → faqat yozilganlar
--       Draft → faqat admin
-- ─────────────────────────────────────────────
ALTER TABLE lessons ENABLE ROW LEVEL SECURITY;

CREATE POLICY "lessons: bepul darslarni hamma ko'radi"
  ON lessons FOR SELECT
  USING (
    (status = 'published' AND is_free = TRUE)  -- Bepul preview
    OR fn_is_admin()                            -- Admin hammasini ko'radi
    OR EXISTS (                                 -- Yozilgan talaba to'liq kursni ko'radi
      SELECT 1
      FROM enrollments e
      JOIN modules m ON m.id = lessons.module_id
      WHERE e.user_id      = auth.uid()
        AND e.course_id    = m.course_id
        AND e.payment_status = 'paid'
        AND lessons.status = 'published'
    )
  );

CREATE POLICY "lessons: faqat admin boshqaradi"
  ON lessons FOR ALL
  USING (fn_is_admin())
  WITH CHECK (fn_is_admin());


-- ─────────────────────────────────────────────
--  6.5  MATERIALS — Lessons bilan bir xil qoida
-- ─────────────────────────────────────────────
ALTER TABLE materials ENABLE ROW LEVEL SECURITY;

CREATE POLICY "materials: yozilgan talabalar ko'radi"
  ON materials FOR SELECT
  USING (
    fn_is_admin()
    OR EXISTS (
      SELECT 1
      FROM enrollments e
      JOIN lessons     l ON l.id = materials.lesson_id
      JOIN modules     m ON m.id = l.module_id
      WHERE e.user_id      = auth.uid()
        AND e.course_id    = m.course_id
        AND e.payment_status = 'paid'
    )
    OR EXISTS (  -- Bepul dars materiallari
      SELECT 1
      FROM lessons l
      WHERE l.id = materials.lesson_id AND l.is_free = TRUE
    )
  );

CREATE POLICY "materials: faqat admin boshqaradi"
  ON materials FOR ALL
  USING (fn_is_admin())
  WITH CHECK (fn_is_admin());


-- ─────────────────────────────────────────────
--  6.6  ENROLLMENTS
-- ─────────────────────────────────────────────
ALTER TABLE enrollments ENABLE ROW LEVEL SECURITY;

CREATE POLICY "enrollments: o'z yozuvlarini ko'radi"
  ON enrollments FOR SELECT
  USING (auth.uid() = user_id OR fn_is_admin());

CREATE POLICY "enrollments: faqat admin yaratadi"
  ON enrollments FOR INSERT
  WITH CHECK (fn_is_admin());

CREATE POLICY "enrollments: faqat admin yangilaydi"
  ON enrollments FOR UPDATE
  USING (fn_is_admin());


-- ─────────────────────────────────────────────
--  6.7  PAYMENTS
-- ─────────────────────────────────────────────
ALTER TABLE payments ENABLE ROW LEVEL SECURITY;

CREATE POLICY "payments: o'z to'lovlarini ko'radi"
  ON payments FOR SELECT
  USING (auth.uid() = user_id OR fn_is_admin());

CREATE POLICY "payments: talaba payment yaratadi (Click.uz callback)"
  ON payments FOR INSERT
  WITH CHECK (auth.uid() = user_id OR fn_is_admin());

CREATE POLICY "payments: faqat admin yangilaydi"
  ON payments FOR UPDATE
  USING (fn_is_admin());


-- ─────────────────────────────────────────────
--  6.8  PROGRESS
-- ─────────────────────────────────────────────
ALTER TABLE progress ENABLE ROW LEVEL SECURITY;

CREATE POLICY "progress: o'z progressini ko'radi va yangilaydi"
  ON progress FOR ALL
  USING (auth.uid() = user_id OR fn_is_admin())
  WITH CHECK (auth.uid() = user_id OR fn_is_admin());


-- ─────────────────────────────────────────────
--  6.9  NOTES
-- ─────────────────────────────────────────────
ALTER TABLE notes ENABLE ROW LEVEL SECURITY;

CREATE POLICY "notes: o'z konspektlari"
  ON notes FOR ALL
  USING (auth.uid() = user_id OR fn_is_admin())
  WITH CHECK (auth.uid() = user_id OR fn_is_admin());


-- ─────────────────────────────────────────────
--  6.10  WAITLIST — Hamma yoziladi, faqat admin ko'radi
-- ─────────────────────────────────────────────
ALTER TABLE waitlist ENABLE ROW LEVEL SECURITY;

CREATE POLICY "waitlist: hamma email yozishi mumkin"
  ON waitlist FOR INSERT
  WITH CHECK (TRUE);

CREATE POLICY "waitlist: faqat admin ko'radi"
  ON waitlist FOR SELECT
  USING (fn_is_admin());

CREATE POLICY "waitlist: faqat admin yangilaydi"
  ON waitlist FOR UPDATE
  USING (fn_is_admin());


-- ─────────────────────────────────────────────
--  6.11  COMING_SOON — Hamma ko'radi, admin boshqaradi
-- ─────────────────────────────────────────────
ALTER TABLE coming_soon ENABLE ROW LEVEL SECURITY;

CREATE POLICY "coming_soon: ko'rinadigan mahsulotlar hammaga"
  ON coming_soon FOR SELECT
  USING (is_visible = TRUE OR fn_is_admin());

CREATE POLICY "coming_soon: faqat admin boshqaradi"
  ON coming_soon FOR ALL
  USING (fn_is_admin())
  WITH CHECK (fn_is_admin());


-- ═══════════════════════════════════════════════════════════════════════
--  7. SEED MA'LUMOTLAR
--     4 ta kurs + barcha modullar
--     ⚠️  ID lar sabit — config.js da ham ishlatilishi mumkin
-- ═══════════════════════════════════════════════════════════════════════


-- ─────────────────────────────────────────────
--  7.1  Kurslar
-- ─────────────────────────────────────────────
INSERT INTO courses (id, slug, title, description, emoji, status, price)
VALUES
  (
    'aaaaaaaa-0001-0000-0000-000000000001',
    'eyuf-lab',
    'EYUF Lab',
    'El-yurt umidi stipendiyasi uchun to''liq yo''llanma. 6 modul, 20 ta video dars.',
    '🎯',
    'active',
    499000
  ),
  (
    'aaaaaaaa-0002-0000-0000-000000000002',
    'bachelor-lab',
    'Bachelor Lab',
    'Top-100 universitetlarda bakalavr ta''limi uchun ariza strategiyasi. 8 modul, 42 ta video dars.',
    '🎓',
    'draft',
    499000
  ),
  (
    'aaaaaaaa-0003-0000-0000-000000000003',
    'master-lab',
    'Master Lab',
    'Xorijda magistratura va DAAD, GKS, Erasmus+ grantlari uchun kompleks tayyorgarlik. 8 modul, 28 dars.',
    '🔬',
    'draft',
    499000
  ),
  (
    'aaaaaaaa-0004-0000-0000-000000000004',
    'phd-lab',
    'PhD Lab',
    'PhD dasturiga kirish: supervisor qidirish, Research Proposal, SoP, grant muhandisligi. 9 modul, 32 dars.',
    '⚗️',
    'draft',
    699000
  )
ON CONFLICT (slug) DO UPDATE SET
  title       = EXCLUDED.title,
  description = EXCLUDED.description,
  price       = EXCLUDED.price,
  status      = EXCLUDED.status;


-- ─────────────────────────────────────────────
--  7.2  EYUF Lab — Modullar (6 ta: 0–5)
--       20 ta dars | 499,000 so'm
-- ─────────────────────────────────────────────
INSERT INTO modules (course_id, title, description, order_index, is_free)
VALUES
  ('aaaaaaaa-0001-0000-0000-000000000001', 'Modul 0 — "El-yurt umidi" jamg''armasi haqida',   'EYUF nima, tarixi, tizim va asosiy tamoyillar',            0, TRUE),
  ('aaaaaaaa-0001-0000-0000-000000000001', 'Modul 1 — EYUF uchun talablar va hujjatlar',       'Kim ariza topshira oladi, hujjatlar ro''yxati, motivatsion esse', 1, FALSE),
  ('aaaaaaaa-0001-0000-0000-000000000001', 'Modul 2 — Test. 1-bo''lim: Tahliliy fikrlash',    '20 ta savol, mantiq, tuzilma va tayyorlanish strategiyasi', 2, FALSE),
  ('aaaaaaaa-0001-0000-0000-000000000001', 'Modul 3 — Test. 2-bo''lim',                        'IQ testi (bakalavriat) va Ilmiy tadqiqot kompetensiyasi',   3, FALSE),
  ('aaaaaaaa-0001-0000-0000-000000000001', 'Modul 4 — Suhbat. Eng muhim bosqich',              '100 ballik tizim, savol turlari, real misollar, tayyorgarlik', 4, FALSE),
  ('aaaaaaaa-0001-0000-0000-000000000001', 'Modul 5 — G''olib bo''ldingiz. Keyin-chi?',        'Visa, shartnoma, O''zbekistonga qaytish majburiyati',       5, FALSE)
ON CONFLICT (course_id, order_index) DO UPDATE SET title = EXCLUDED.title, description = EXCLUDED.description;


-- ─────────────────────────────────────────────
--  7.3  Bachelor Lab — Modullar (8 ta: 0–7)
--       42 ta dars | 499,000 so'm
-- ─────────────────────────────────────────────
INSERT INTO modules (course_id, title, order_index, is_free)
VALUES
  ('aaaaaaaa-0002-0000-0000-000000000002', 'Modul 0 — Kirish: Bachelor Lab tizimi',           0, TRUE),
  ('aaaaaaaa-0002-0000-0000-000000000002', 'Modul 1 — Maqsad belgilash va universitetlar',    1, FALSE),
  ('aaaaaaaa-0002-0000-0000-000000000002', 'Modul 2 — IELTS/SAT strategiyasi',                2, FALSE),
  ('aaaaaaaa-0002-0000-0000-000000000002', 'Modul 3 — Akademik CV (STAR format)',             3, FALSE),
  ('aaaaaaaa-0002-0000-0000-000000000002', 'Modul 4 — Motivatsion xat (SoP)',                 4, FALSE),
  ('aaaaaaaa-0002-0000-0000-000000000002', 'Modul 5 — Tavsiya xatlari (LoR)',                 5, FALSE),
  ('aaaaaaaa-0002-0000-0000-000000000002', 'Modul 6 — Ariza va suhbat tayyorgarlik',          6, FALSE),
  ('aaaaaaaa-0002-0000-0000-000000000002', 'Modul 7 — Grant va stipendiyalar',                7, FALSE)
ON CONFLICT (course_id, order_index) DO UPDATE SET title = EXCLUDED.title;


-- ─────────────────────────────────────────────
--  7.4  Master Lab — Modullar (8 ta: 0–7)
--       28 ta dars | 499,000 so'm
-- ─────────────────────────────────────────────
INSERT INTO modules (course_id, title, order_index, is_free)
VALUES
  ('aaaaaaaa-0003-0000-0000-000000000003', 'Modul 0 — Kirish: Master Lab tizimi',             0, TRUE),
  ('aaaaaaaa-0003-0000-0000-000000000003', 'Modul 1 — Dunyo universitetlarini xaritalash',    1, FALSE),
  ('aaaaaaaa-0003-0000-0000-000000000003', 'Modul 2 — Research fit: Supervisor qidirish',     2, FALSE),
  ('aaaaaaaa-0003-0000-0000-000000000003', 'Modul 3 — Cold Email va professor muloqoti',      3, FALSE),
  ('aaaaaaaa-0003-0000-0000-000000000003', 'Modul 4 — Akademik CV va motivatsion xat',        4, FALSE),
  ('aaaaaaaa-0003-0000-0000-000000000003', 'Modul 5 — Research Proposal yozish',              5, FALSE),
  ('aaaaaaaa-0003-0000-0000-000000000003', 'Modul 6 — DAAD, GKS, Erasmus+ ariza strategiyasi', 6, FALSE),
  ('aaaaaaaa-0003-0000-0000-000000000003', 'Modul 7 — Suhbat va final tayyorgarlik',          7, FALSE)
ON CONFLICT (course_id, order_index) DO UPDATE SET title = EXCLUDED.title;


-- ─────────────────────────────────────────────
--  7.5  PhD Lab — Modullar (9 ta: 0–8)
-- ─────────────────────────────────────────────
INSERT INTO modules (course_id, title, order_index, is_free)
VALUES
  ('aaaaaaaa-0004-0000-0000-000000000004', 'Modul 0 — Kirish: PhD Lab tizimi',                           0, TRUE),
  ('aaaaaaaa-0004-0000-0000-000000000004', 'Modul 1 — Research Identity & Scholar OS Setup',             1, FALSE),
  ('aaaaaaaa-0004-0000-0000-000000000004', 'Modul 2 — University & Supervisor Mapping System',           2, FALSE),
  ('aaaaaaaa-0004-0000-0000-000000000004', 'Modul 3 — Cold Email & Professor Outreach Engineering',      3, FALSE),
  ('aaaaaaaa-0004-0000-0000-000000000004', 'Modul 4 — Research Proposal Engineering',                    4, FALSE),
  ('aaaaaaaa-0004-0000-0000-000000000004', 'Modul 5 — Academic CV & Application Portfolio',              5, FALSE),
  ('aaaaaaaa-0004-0000-0000-000000000004', 'Modul 6 — Statement of Purpose (SoP) Mastery',              6, FALSE),
  ('aaaaaaaa-0004-0000-0000-000000000004', 'Modul 7 — Grant & Scholarship Engineering',                  7, FALSE),
  ('aaaaaaaa-0004-0000-0000-000000000004', 'Modul 8 — PhD Life & Remote Research Readiness',             8, FALSE)
ON CONFLICT (course_id, order_index) DO UPDATE SET title = EXCLUDED.title;


-- ─────────────────────────────────────────────
--  7.6  Coming Soon mahsulotlar
-- ─────────────────────────────────────────────
INSERT INTO coming_soon (slug, title, description, emoji, is_visible, order_index)
VALUES
  ('gks-lab',            'GKS Lab',              'Koreya hukumati stipendiyasi (GKS/KGSP) uchun to''liq yo''llanma', '🇰🇷', TRUE, 1),
  ('ikki-miya',          '2-miya',               'O''zbek va ingliz tilida paralel akademik fikrlash tizimi',        '🧠',  TRUE, 2),
  ('notion-shablonlar',  'Notion Shablonlar',    'Tadqiqotchilar uchun tayyor Notion workspace to''plami',           '📐',  TRUE, 3)
ON CONFLICT (slug) DO UPDATE SET
  title      = EXCLUDED.title,
  is_visible = EXCLUDED.is_visible;


-- ═══════════════════════════════════════════════════════════════════════
--  8. ADMIN FOYDALANUVCHI ROLI BERISH
--     Supabase da hisob yaratgandan keyin bu so'rovni ishga tushiring:
--
--     UPDATE profiles SET role = 'admin'
--     WHERE email = 'shokhrukh@kompaslab.uz';
--
--  Yoki auth.users ID ni to'g'ridan-to'g'ri:
--
--     UPDATE profiles SET role = 'admin'
--     WHERE id = 'SIZNING_USER_ID';
-- ═══════════════════════════════════════════════════════════════════════


-- ═══════════════════════════════════════════════════════════════════════
--  9. TEKSHIRISH — Hammasi to'g'ri yaratilganini confirm qiling
-- ═══════════════════════════════════════════════════════════════════════
SELECT
  'courses'     AS jadval, COUNT(*) AS soni FROM courses
UNION ALL SELECT 'modules',     COUNT(*) FROM modules
UNION ALL SELECT 'coming_soon', COUNT(*) FROM coming_soon;

-- Kutilgan natija:
-- courses     | 4
-- modules     | 31  (6+8+8+9)
-- coming_soon | 3
