// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — auth.js
//  Barcha autentifikatsiya va sessiya logikasi
//  config.js dan KEYIN yuklaning:
//    <script src="js/config.js"></script>
//    <script src="js/auth.js"></script>
// ═══════════════════════════════════════════════════════════════


// ════════════════════════════════════════════
//  1. SESSION VA FOYDALANUVCHI
// ════════════════════════════════════════════

/**
 * Joriy sessiyani olish
 * @returns {Promise<Session|null>}
 */
async function getSession() {
  try {
    const { data: { session }, error } = await supabase.auth.getSession()
    if (error) throw error
    return session
  } catch (e) {
    console.error('getSession xatosi:', e.message)
    return null
  }
}

/**
 * Joriy foydalanuvchini olish (Supabase Auth)
 * @returns {Promise<User|null>}
 */
async function getCurrentUser() {
  const session = await getSession()
  return session?.user ?? null
}

/**
 * Profiles jadvalidan foydalanuvchi profilini olish
 * @param {string} userId
 * @returns {Promise<Object|null>}
 */
async function getUserProfile(userId) {
  try {
    const { data, error } = await supabase
      .from(DB.profiles)
      .select('*')
      .eq('id', userId)
      .single()
    if (error) throw error
    return data
  } catch (e) {
    console.error('getUserProfile xatosi:', e.message)
    return null
  }
}


// ════════════════════════════════════════════
//  2. SAHIFA HIMOYA FUNKSIYALARI (Guards)
// ════════════════════════════════════════════

/**
 * requireAuth()
 * — Sahifa ochilganda sessiyani tekshiradi
 * — Sessiya yo'q bo'lsa login.html ga yo'naltiradi
 * — Barcha himoyalangan sahifalar boshida chaqirng
 *
 * @returns {Promise<{user, profile}|null>}
 *
 * ISHLATISH:
 *   <script>
 *   document.addEventListener('DOMContentLoaded', async () => {
 *     const auth = await requireAuth()
 *     if (!auth) return  // redirect allaqachon bo'ladi
 *     // auth.user  — Supabase user
 *     // auth.profile — profiles jadvali
 *   })
 *   </script>
 */
async function requireAuth() {
  const session = await getSession()

  if (!session) {
    // Qaytish uchun URL saqlash
    const returnTo = window.location.pathname + window.location.search
    sessionStorage.setItem('returnTo', returnTo)
    window.location.href = APP_CONFIG.routes.login
    return null
  }

  const profile = await getUserProfile(session.user.id)
  return { user: session.user, profile }
}

/**
 * requireEnrollment()
 * — requireAuth() dan KEYIN chaqiring
 * — Foydalanuvchi kursga yozilganini tekshiradi
 * — Yozilmagan bo'lsa payment.html ga yo'naltiradi
 *
 * @param {string} userId
 * @param {string} courseSlug  — masalan 'eyuf-lab'
 * @returns {Promise<Object|null>}  — enrollment yozuvi
 */
async function requireEnrollment(userId, courseSlug) {
  try {
    // Kurs ID sini olish
    const { data: course, error: cErr } = await supabase
      .from(DB.courses)
      .select('id')
      .eq('slug', courseSlug)
      .single()

    if (cErr || !course) {
      window.location.href = APP_CONFIG.routes.payment
      return null
    }

    // Enrollment tekshirish
    const { data: enrollment, error: eErr } = await supabase
      .from(DB.enrollments)
      .select('*')
      .eq('user_id', userId)
      .eq('course_id', course.id)
      .eq('payment_status', 'paid')
      .single()

    if (eErr || !enrollment) {
      window.location.href = `${APP_CONFIG.routes.payment}?course=${courseSlug}`
      return null
    }

    return enrollment
  } catch (e) {
    console.error('requireEnrollment xatosi:', e.message)
    window.location.href = APP_CONFIG.routes.payment
    return null
  }
}

/**
 * requireAdmin()
 * — Admin sahifalarini himoya qilish uchun
 * — Admin emas bo'lsa dashboard ga yo'naltiradi
 *
 * @returns {Promise<{user, profile}|null>}
 *
 * ISHLATISH (admin.html boshida):
 *   const auth = await requireAdmin()
 *   if (!auth) return
 */
async function requireAdmin() {
  const auth = await requireAuth()
  if (!auth) return null

  const isAdmin =
    auth.profile?.role === 'admin' ||
    APP_CONFIG.adminEmails.includes(auth.user.email)

  if (!isAdmin) {
    showToast('⛔ Bu sahifaga kirish uchun admin huquqi kerak', 'error')
    setTimeout(() => {
      window.location.href = APP_CONFIG.routes.dashboard
    }, 1500)
    return null
  }

  return auth
}

/**
 * redirectIfLoggedIn()
 * — Login va Register sahifalari uchun
 * — Kirgan foydalanuvchi login sahifasiga kirishini oldini oladi
 */
async function redirectIfLoggedIn() {
  const session = await getSession()
  if (session) {
    // Avvalgi sahifaga yoki dashboardga yo'naltirish
    const returnTo = sessionStorage.getItem('returnTo')
    sessionStorage.removeItem('returnTo')
    window.location.href = returnTo || APP_CONFIG.routes.dashboard
  }
}


// ════════════════════════════════════════════
//  3. LOGIN / LOGOUT / REGISTER
// ════════════════════════════════════════════

/**
 * login(email, password)
 * @returns {Promise<{success, user, error}>}
 */
async function login(email, password) {
  try {
    const { data, error } = await supabase.auth.signInWithPassword({
      email:    email.trim().toLowerCase(),
      password: password
    })

    if (error) {
      const msgs = {
        'Invalid login credentials':       'Email yoki parol noto\'g\'ri.',
        'Email not confirmed':             'Emailni tasdiqlang. Xat spam papkasida bo\'lishi mumkin.',
        'Too many requests':               'Ko\'p urinish. Bir oz kuting.',
      }
      return {
        success: false,
        error: msgs[error.message] || 'Kirish muvaffaqiyatsiz. Qayta urinib ko\'ring.'
      }
    }

    return { success: true, user: data.user }

  } catch (e) {
    return { success: false, error: 'Tarmoq xatosi. Internet ulanishini tekshiring.' }
  }
}

/**
 * logout()
 * — Supabase sessiyasini yakunlaydi
 * — login.html ga yo'naltiradi
 */
async function logout() {
  await supabase.auth.signOut()
  window.location.href = APP_CONFIG.routes.login
}

/**
 * register(data)
 * @param {Object} data — { email, password, firstName, lastName, phone, education, goal }
 * @returns {Promise<{success, user, error}>}
 */
async function register({ email, password, firstName, lastName, phone, education, goal }) {
  try {
    // Supabase Auth da foydalanuvchi yaratish
    const { data: authData, error: authError } = await supabase.auth.signUp({
      email:    email.trim().toLowerCase(),
      password: password,
      options: {
        data: {
          full_name: `${firstName.trim()} ${lastName.trim()}`,
          phone:     phone,
        },
        emailRedirectTo: `${APP_CONFIG.baseUrl}/${APP_CONFIG.routes.dashboard}`
      }
    })

    if (authError) {
      const msgs = {
        'User already registered':      'Bu email allaqachon ro\'yxatdan o\'tgan. Kirishga urinib ko\'ring.',
        'Password should be at least 6 characters': 'Parol kamida 6 ta belgidan iborat bo\'lishi kerak.',
      }
      return {
        success: false,
        error: msgs[authError.message] || authError.message
      }
    }

    // Profiles jadvaliga ma'lumot yozish
    // (Supabase trigger ham buni qiladi, lekin qo'shimcha ma'lumotlar uchun)
    if (authData.user) {
      const { error: profileError } = await supabase
        .from(DB.profiles)
        .upsert({
          id:         authData.user.id,
          email:      email.trim().toLowerCase(),
          first_name: firstName.trim(),
          last_name:  lastName.trim(),
          full_name:  `${firstName.trim()} ${lastName.trim()}`,
          phone:      phone?.trim() || null,
          education:  education || null,
          goal:       goal || null,
          role:       'student',
          created_at: new Date().toISOString(),
        }, { onConflict: 'id' })

      if (profileError) {
        // Kritik xato emas — auth muvaffaqiyatli bo'ldi
        console.warn('Profile yozishda xato:', profileError.message)
      }
    }

    return { success: true, user: authData.user }

  } catch (e) {
    return { success: false, error: 'Ro\'yxatdan o\'tishda xato. Qayta urinib ko\'ring.' }
  }
}

/**
 * resetPassword(email)
 * — Parol tiklash emailini yuboradi
 */
async function resetPassword(email) {
  try {
    const { error } = await supabase.auth.resetPasswordForEmail(
      email.trim().toLowerCase(),
      { redirectTo: `${APP_CONFIG.baseUrl}/${APP_CONFIG.routes.reset}` }
    )
    if (error) throw error
    return { success: true }
  } catch (e) {
    return { success: false, error: e.message }
  }
}

/**
 * updatePassword(newPassword)
 * — reset-password.html da ishlatiladigan yangi parol o'rnatish
 */
async function updatePassword(newPassword) {
  try {
    const { error } = await supabase.auth.updateUser({ password: newPassword })
    if (error) throw error
    return { success: true }
  } catch (e) {
    return { success: false, error: e.message }
  }
}


// ════════════════════════════════════════════
//  4. ENROLLMENT TEKSHIRISH
// ════════════════════════════════════════════

/**
 * getUserEnrollments(userId)
 * — Foydalanuvchining barcha yozilgan kurslarini olish
 * @returns {Promise<Array>}
 */
async function getUserEnrollments(userId) {
  try {
    const { data, error } = await supabase
      .from(DB.enrollments)
      .select(`
        *,
        course:courses(id, title, slug, description)
      `)
      .eq('user_id', userId)
      .eq('payment_status', 'paid')
      .order('enrolled_at', { ascending: false })

    if (error) throw error
    return data || []
  } catch (e) {
    console.error('getUserEnrollments xatosi:', e.message)
    return []
  }
}

/**
 * isEnrolled(userId, courseSlug)
 * — Foydalanuvchi kursga yozilganmi?
 * @returns {Promise<boolean>}
 */
async function isEnrolled(userId, courseSlug) {
  const enrollments = await getUserEnrollments(userId)
  return enrollments.some(e => e.course?.slug === courseSlug)
}


// ════════════════════════════════════════════
//  5. AUTH HOLAT O'ZGARISHINI KUZATISH
// ════════════════════════════════════════════

/**
 * onAuthChange(callback)
 * — Sessiya o'zgarganda (login/logout) avtomatik ishga tushadi
 * — Dashboard da foydalanuvchi chiqsa darhol login ga yuboriladi
 *
 * ISHLATISH:
 *   onAuthChange((event, session) => {
 *     if (event === 'SIGNED_OUT') window.location.href = 'login.html'
 *   })
 */
function onAuthChange(callback) {
  supabase.auth.onAuthStateChange((event, session) => {
    callback(event, session)
  })
}


// ════════════════════════════════════════════
//  6. PROFIL YANGILASH
// ════════════════════════════════════════════

/**
 * updateProfile(userId, updates)
 * @param {string} userId
 * @param {Object} updates — { first_name, last_name, phone, ... }
 */
async function updateProfile(userId, updates) {
  try {
    const { data, error } = await supabase
      .from(DB.profiles)
      .update({ ...updates, updated_at: new Date().toISOString() })
      .eq('id', userId)
      .select()
      .single()

    if (error) throw error
    return { success: true, data }
  } catch (e) {
    return { success: false, error: e.message }
  }
}


// ════════════════════════════════════════════
//  7. WAITLIST
// ════════════════════════════════════════════

/**
 * addToWaitlist(email, courseSlug, source)
 * — Landing page dagi "Tez orada" emaillarni saqlash
 * @param {string} email
 * @param {string} courseSlug  — 'gks-lab', 'ikki-miya', 'notion-shablonlar'
 * @param {string} source      — 'landing', 'popup', ...
 * @returns {Promise<{success, error}>}
 */
async function addToWaitlist(email, courseSlug, source = 'landing') {
  try {
    const { error } = await supabase
      .from(DB.waitlist)
      .upsert({
        email:      email.trim().toLowerCase(),
        course_slug: courseSlug,
        source:     source,
        added_at:   new Date().toISOString(),
      }, { onConflict: 'email,course_slug' })  // bir email bir kurs uchun bir marta

    if (error) throw error
    return { success: true }
  } catch (e) {
    // "duplicate key" xatosi — allaqachon ro'yxatda
    if (e.message?.includes('duplicate') || e.code === '23505') {
      return { success: true }  // foydalanuvchiga xato ko'rsatmang
    }
    return { success: false, error: e.message }
  }
}


// ════════════════════════════════════════════
//  8. ADMIN FUNKSIYALARI
// ════════════════════════════════════════════

/**
 * adminEnrollStudent(data)
 * — Admin paneldan qo'lda talabani kursga yozish
 * @param {Object} data — { email, courseSlug, plan, amount, method, note }
 * @returns {Promise<{success, error}>}
 */
async function adminEnrollStudent({ email, courseSlug, plan, amount, method, note }) {
  try {
    // 1. Foydalanuvchini email orqali qidirish
    const { data: profile, error: profileErr } = await supabase
      .from(DB.profiles)
      .select('id, full_name')
      .eq('email', email.trim().toLowerCase())
      .single()

    if (profileErr || !profile) {
      return {
        success: false,
        error: `"${email}" emailli foydalanuvchi topilmadi. Avval ro'yxatdan o'tishi kerak.`
      }
    }

    // 2. Kursni olish
    const { data: course, error: courseErr } = await supabase
      .from(DB.courses)
      .select('id, title')
      .eq('slug', courseSlug)
      .single()

    if (courseErr || !course) {
      return { success: false, error: 'Kurs topilmadi' }
    }

    // 3. To'lov yozuvi yaratish
    const { data: payment, error: payErr } = await supabase
      .from(DB.payments)
      .insert({
        user_id:    profile.id,
        course_id:  course.id,
        amount:     amount,
        method:     method,
        status:     'confirmed',
        note:       note || null,
        confirmed_at: new Date().toISOString(),
        confirmed_by: 'admin_manual',
      })
      .select()
      .single()

    if (payErr) throw payErr

    // 4. Enrollment yaratish
    const { error: enrollErr } = await supabase
      .from(DB.enrollments)
      .upsert({
        user_id:         profile.id,
        course_id:       course.id,
        plan:            plan,
        payment_status:  'paid',
        payment_id:      payment.id,
        enrolled_at:     new Date().toISOString(),
      }, { onConflict: 'user_id,course_id' })

    if (enrollErr) throw enrollErr

    return {
      success: true,
      message: `✓ ${profile.full_name} — ${course.title} (${plan}) ga muvaffaqiyatli yozildi!`
    }

  } catch (e) {
    console.error('adminEnrollStudent xatosi:', e)
    return { success: false, error: e.message }
  }
}

/**
 * adminConfirmPayment(paymentId, userId, courseId, plan)
 * — Kutilayotgan to'lovni tasdiqlash
 */
async function adminConfirmPayment(paymentId, userId, courseId, plan) {
  try {
    // To'lov statusini yangilash
    await supabase
      .from(DB.payments)
      .update({ status: 'confirmed', confirmed_at: new Date().toISOString() })
      .eq('id', paymentId)

    // Enrollment yaratish yoki yangilash
    const { error } = await supabase
      .from(DB.enrollments)
      .upsert({
        user_id:        userId,
        course_id:      courseId,
        plan:           plan,
        payment_status: 'paid',
        payment_id:     paymentId,
        enrolled_at:    new Date().toISOString(),
      }, { onConflict: 'user_id,course_id' })

    if (error) throw error
    return { success: true }
  } catch (e) {
    return { success: false, error: e.message }
  }
}


// ════════════════════════════════════════════
//  9. DARS BOSHQARUVI (Admin)
// ════════════════════════════════════════════

/**
 * adminSaveLesson(lessonData)
 * — Yangi dars yaratish yoki mavjudini yangilash
 * @param {Object} d — { id?, course_slug, module_order, title, vimeo_url,
 *                       order_index, duration, is_free, status, description }
 */
async function adminSaveLesson(d) {
  try {
    // Modul ID sini olish
    const { data: course } = await supabase
      .from(DB.courses)
      .select('id')
      .eq('slug', d.course_slug)
      .single()

    if (!course) return { success: false, error: 'Kurs topilmadi' }

    const { data: module } = await supabase
      .from(DB.modules)
      .select('id')
      .eq('course_id', course.id)
      .eq('order_index', d.module_order)
      .single()

    if (!module) return { success: false, error: `Modul ${d.module_order} topilmadi` }

    const payload = {
      module_id:   module.id,
      title:       d.title,
      vimeo_url:   d.vimeo_url,
      order_index: d.order_index || 1,
      duration:    d.duration || null,
      is_free:     d.is_free || false,
      status:      d.status || 'draft',
      description: d.description || null,
      updated_at:  new Date().toISOString(),
    }

    let result
    if (d.id) {
      // Mavjud darsni yangilash
      const { data, error } = await supabase
        .from(DB.lessons)
        .update(payload)
        .eq('id', d.id)
        .select()
        .single()
      if (error) throw error
      result = data
    } else {
      // Yangi dars yaratish
      const { data, error } = await supabase
        .from(DB.lessons)
        .insert({ ...payload, created_at: new Date().toISOString() })
        .select()
        .single()
      if (error) throw error
      result = data
    }

    return { success: true, data: result }
  } catch (e) {
    console.error('adminSaveLesson xatosi:', e)
    return { success: false, error: e.message }
  }
}

/**
 * adminToggleLessonStatus(lessonId, currentStatus)
 * — draft ↔ published almashtirish
 */
async function adminToggleLessonStatus(lessonId, currentStatus) {
  const newStatus = currentStatus === 'published' ? 'draft' : 'published'
  try {
    const { error } = await supabase
      .from(DB.lessons)
      .update({ status: newStatus, updated_at: new Date().toISOString() })
      .eq('id', lessonId)
    if (error) throw error
    return { success: true, newStatus }
  } catch (e) {
    return { success: false, error: e.message }
  }
}

/**
 * adminDeleteLesson(lessonId)
 */
async function adminDeleteLesson(lessonId) {
  try {
    const { error } = await supabase
      .from(DB.lessons)
      .delete()
      .eq('id', lessonId)
    if (error) throw error
    return { success: true }
  } catch (e) {
    return { success: false, error: e.message }
  }
}


// ════════════════════════════════════════════
//  10. DASHBOARD STATISTIKA (Admin)
// ════════════════════════════════════════════

/**
 * adminGetStats()
 * — Admin dashboard uchun umumiy raqamlar
 * @returns {Promise<Object>}
 */
async function adminGetStats() {
  try {
    const [students, lessons, payments, waitlist] = await Promise.all([
      supabase.from(DB.profiles).select('id', { count: 'exact', head: true }).eq('role', 'student'),
      supabase.from(DB.lessons).select('id', { count: 'exact', head: true }).eq('status', 'published'),
      supabase.from(DB.payments).select('amount').eq('status', 'confirmed'),
      supabase.from(DB.waitlist).select('id', { count: 'exact', head: true }),
    ])

    const totalRevenue = (payments.data || []).reduce((sum, p) => sum + (p.amount || 0), 0)

    return {
      students: students.count || 0,
      lessons:  lessons.count  || 0,
      revenue:  totalRevenue,
      waitlist: waitlist.count || 0,
    }
  } catch (e) {
    console.error('adminGetStats xatosi:', e.message)
    return { students: 0, lessons: 0, revenue: 0, waitlist: 0 }
  }
}

/**
 * adminGetCourseStats(courseSlug)
 * — Kurs bo'yicha statistika: darslar soni, talabalar soni
 */
async function adminGetCourseStats(courseSlug) {
  try {
    const { data: course } = await supabase
      .from(DB.courses)
      .select('id')
      .eq('slug', courseSlug)
      .single()

    if (!course) return { lessons: 0, students: 0 }

    const [lessons, students] = await Promise.all([
      supabase.from(DB.lessons)
        .select('id', { count: 'exact', head: true })
        .eq('module_id', course.id),  // module.course_id orqali
      supabase.from(DB.enrollments)
        .select('id', { count: 'exact', head: true })
        .eq('course_id', course.id)
        .eq('payment_status', 'paid'),
    ])

    return {
      lessons:  lessons.count  || 0,
      students: students.count || 0,
    }
  } catch (e) {
    return { lessons: 0, students: 0 }
  }
}
