// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — config.js
//  Supabase ulanish va global konstantalar
//
//  ⚠️  Bu faylni hech qachon GitHub ga push qilmang!
//      .gitignore: js/config.js
//
//  TO'LDIRISH TARTIBI:
//    1. SUPABASE_URL      → Supabase → Settings → API → Project URL
//    2. SUPABASE_ANON_KEY → Supabase → Settings → API → anon (public) key
//    3. adminEmails       → Sizning email manzilingiz
//    4. baseUrl           → kompaslab.uz (deploy bo'lgandan keyin)
// ═══════════════════════════════════════════════════════════════

// ─── 1. SUPABASE KALITLAR ────────────────────────────────────
//  Supabase → Settings → API sahifasidan oling
const SUPABASE_URL      = 'https://XXXXXXXXXXXX.supabase.co'
const SUPABASE_ANON_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.XXXX'

// ─── 2. SUPABASE CLIENT ──────────────────────────────────────
const supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY, {
  auth: {
    autoRefreshToken:   true,
    persistSession:     true,
    detectSessionInUrl: true,
  }
})

// ─── 3. LOYIHA SOZLAMALARI ───────────────────────────────────
const APP_CONFIG = {
  name:    'Kompas Lab',
  version: '2.0.0',
  baseUrl: 'https://kompaslab.uz',

  // Sahifa yo'llari
  routes: {
    login:     'login.html',
    register:  'register.html',
    dashboard: 'dashboard.html',
    payment:   'payment.html',
    lesson:    'lesson.html',
    admin:     'admin.html',
    reset:     'reset-password.html',
  },

  // Kurslar (slug Supabase courses.slug bilan mos bo'lishi kerak)
  courses: {
    eyuf:     { slug: 'eyuf-lab',     name: 'EYUF Lab',     emoji: '🎯', modules: 6,  lessons: 20,  price: 499000 },
    bachelor: { slug: 'bachelor-lab', name: 'Bachelor Lab', emoji: '🎓', modules: 8,  lessons: 42,  price: 499000 },
    master:   { slug: 'master-lab',   name: 'Master Lab',   emoji: '🔬', modules: 8,  lessons: 28,  price: 499000 },
    phd:      { slug: 'phd-lab',      name: 'PhD Lab',      emoji: '⚗️', modules: 9,  lessons: 32,  price: 699000 },
  },

  // Admin email ro'yxati
  adminEmails: [
    'shokhrukh@kompaslab.uz',
    // qo'shimcha admin kerak bo'lsa shu yerga qo'shing
  ],
}

// ─── 4. JADVAL NOMLARI ───────────────────────────────────────
const DB = {
  profiles:    'profiles',
  courses:     'courses',
  modules:     'modules',
  lessons:     'lessons',
  enrollments: 'enrollments',
  progress:    'progress',
  notes:       'notes',
  materials:   'materials',
  payments:    'payments',
  waitlist:    'waitlist',
  coming_soon: 'coming_soon',
}

// ─── 5. YORDAMCHI FUNKSIYALAR ────────────────────────────────

/** 499000 → "499,000" */
function formatMoney(n) {
  return (n || 0).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')
}

/** 2900000 → "2 900 000 so'm" */
function formatPrice(amount) {
  if (!amount && amount !== 0) return '—'
  return Number(amount).toLocaleString('ru-RU') + " so'm"
}

/** ISO → "12 Yanvar 2025" */
function formatDate(iso) {
  if (!iso) return '—'
  return new Date(iso).toLocaleDateString('uz-Latn', {
    year: 'numeric', month: 'long', day: 'numeric'
  })
}

/** ISO → "12.01.2025" */
function formatDateShort(iso) {
  if (!iso) return '—'
  return new Date(iso).toLocaleDateString('ru-RU')
}

/** ISO → "2 soat oldin" */
function timeAgo(iso) {
  if (!iso) return '—'
  const sec = Math.floor((Date.now() - new Date(iso)) / 1000)
  if (sec < 60)    return 'Hozirgina'
  if (sec < 3600)  return `${Math.floor(sec/60)} daqiqa oldin`
  if (sec < 86400) return `${Math.floor(sec/3600)} soat oldin`
  if (sec < 604800)return `${Math.floor(sec/86400)} kun oldin`
  return formatDateShort(iso)
}

/** "Sardor Karimov" → "SK" */
function getInitials(name) {
  if (!name) return '?'
  return name.trim().split(' ')
    .map(n => n[0]?.toUpperCase())
    .filter(Boolean).slice(0, 2).join('')
}

/** ?course=eyuf-lab → "eyuf-lab" */
function getParam(name) {
  return new URLSearchParams(window.location.search).get(name)
}

/** Toast xabarnoma */
function showToast(msg, type = 'success', ms = 3500) {
  let el = document.getElementById('toast')
  if (!el) {
    el = document.createElement('div')
    el.id = 'toast'
    el.style.cssText = [
      'position:fixed;bottom:22px;right:22px',
      'padding:11px 18px;border-radius:10px',
      "font-family:'Outfit',sans-serif;font-size:13px;font-weight:600",
      'z-index:9999;transform:translateY(80px);opacity:0',
      'transition:all 0.3s;box-shadow:0 8px 24px rgba(0,0,0,.15)',
    ].join(';')
    document.body.appendChild(el)
  }
  const bg = { success:'#2d4a3e', error:'#c0392b', warning:'#b08a00', info:'#1a56a0' }
  el.style.background = bg[type] || bg.success
  el.style.color = '#fff'
  el.textContent = msg
  el.style.transform = 'translateY(0)'
  el.style.opacity = '1'
  clearTimeout(el._t)
  el._t = setTimeout(() => {
    el.style.transform = 'translateY(80px)'
    el.style.opacity = '0'
  }, ms)
}

// ─── 6. ULANISHNI TEKSHIRISH ─────────────────────────────────
// Brauzer Console da: checkSupabaseConnection()
async function checkSupabaseConnection() {
  try {
    const { data, error } = await supabase.from(DB.courses).select('id').limit(1)
    if (error) {
      console.warn('⚠️ Supabase xato:', error.message)
      return false
    }
    const count = data?.length ?? 0
    console.log(`✅ Supabase ulandi — courses jadvali: ${count} ta yozuv`)
    return true
  } catch (e) {
    console.error('❌ URL yoki Key noto\'g\'ri:', e.message)
    return false
  }
}
