// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — admin-videos.js (2026-11-19): Admin → Videolar
//  Har dastur, modul va dars uchun YouTube yoki Vimeo havolasi. Jadval: module_videos
//  (migratsiya supabase/migrations/20261119_module_videos.sql). Saytda koʻrsatish: js/module-video.js
//  (M0 hammaga, pullik modul faqat kirish huquqi borlarga: RPC kompas_module_videos).
//  Oʻchirish yoʻq: "Oʻchirish" holatni 'off' qiladi, qayta yoqsa boʻladi.
//  Joylar: l0 = M0 bosh sahifasi, l1…l12 = darslar, res = modul natijasi / yakun.
// ═══════════════════════════════════════════════════════════════
const VD = (() => {
  // Magistratura dars nomlari (master_v2/content.py bilan bir xil). Boshqa dasturlarda "N-dars".
  const NAMES = {
    'master-lab': {
      0: ['Muddat', 'Yoʻnalish', 'Hujjatlar', 'Pul'],
      1: ['Sizda nima bor?', 'Qiziqishingizni bitta jumlaga sigʻdiring', 'Reyting nimani koʻrsatadi', 'Dastur sizga mosmi', 'Roʻyxatni uch guruhga boʻlamiz', 'Pul qayerdan keladi', 'Sizning hikoyangiz'],
      2: ['Bitta arizada bir nechta sana', 'Sanadan orqaga hisoblaymiz', 'Hamma ariza bitta jadvalda', 'Bir nechta arizani birga yuritish', 'I bosqich yakuni: bir sahifalik reja'],
      3: ['CV kerakmi va qanday?', 'Taʼlim boʻlimi va baholar', 'Tajribani STAR bilan yozish', 'Nashr, chiqish va loyihalar', 'Koʻnikma, til va sertifikat', 'Yuborishdan oldingi tekshiruv'],
      4: ['Kuchli tavsiya xati nimadan iborat', 'Kimdan va qachon soʻrash', 'Ustozga Yutuqlar varaqasi', 'Professorga xat: qachon va qanday', 'Javob kelsa ham, kelmasa ham', 'Xatlar daftari'],
      5: ['Maqsad bayonnomasi nima', 'Tuzilma: toʻrtta savolga javob', '«Nega aynan shu dastur?»', 'Dalil bilan yozish', 'Birinchi qoralama', 'Tahrir', 'Namunalarni solishtirish'],
      6: ['Taklif qachon soʻraladi', 'Muammo bayoni', 'Adabiyotlar sharhi', 'Metodologiya', 'Ish rejasi va vaqt jadvali', 'Kutilayotgan natija', 'Format va iqtibos'],
      7: ['Stipendiya turlari va majburiy shartlar', 'Buyuk Britaniya', 'AQSh', 'Yevropa Ittifoqi', 'Osiyo', 'Turkiya va boshqa yoʻnalishlar', 'Oʻzbekiston dasturlari va universitet grantlari', 'Stipendiyalar roʻyxati'],
      8: ['Suhbat turlari', 'Suhbatdagi 10 ta savol', 'Stipendiya suhbatlari', '5 daqiqalik ilmiy taqdimot', 'Javobni yozib olish va baholash', 'Qabul xati kelgach: birinchi ikki hafta', 'Viza, sugʻurta, uy-joy, bank', 'Birinchi 90 kun va oʻqishdan keyin']
    }
  }
  let built = false, rows = [], labs = []
  const $ = (id) => document.getElementById(id)
  const esc = (x) => String(x == null ? '' : x).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;')

  function ytId(v) {
    v = String(v || '').trim()
    if (/^[\w-]{11}$/.test(v)) return v
    const m = /(?:youtu\.be\/|[?&]v=|\/embed\/|\/shorts\/|\/live\/)([\w-]{11})/.exec(v)
    return m ? m[1] : null
  }
  function vimeo(v) {
    v = String(v || '').trim()
    const m = /^(\d{6,12})(?:[\/?#:](?:h=)?([0-9a-f]{6,20}))?$/i.exec(v) || /vimeo\.com\/(?:video\/|.*\/)?(\d{6,12})(?:\/([0-9a-f]{6,20}))?/i.exec(v)
    if (!m) return null
    return { id: m[1], h: m[2] || ((/[?&]h=([0-9a-f]{6,20})/i.exec(v) || [])[1]) || '' }
  }
  // Havoladan provayder va saqlanadigan qiymat
  function detect(v) {
    if (/vimeo/i.test(v) || /^\d{6,12}(\D|$)/.test(String(v).trim())) {
      const x = vimeo(v); return x ? { p: 'vimeo', v: x.h ? x.id + '/' + x.h : x.id } : null
    }
    const id = ytId(v); return id ? { p: 'youtube', v: id } : null
  }
  function slotName(lab, mod, slot) {
    if (slot === 'res') return mod === 0 ? 'Yakun sahifasi' : 'Modul natijasi'
    if (slot === 'l0') return 'M0 bosh sahifasi'
    const i = +slot.slice(1), n = (NAMES[lab] && NAMES[lab][mod]) || []
    return (mod === 0 ? i + '-qadam' : 'M' + mod + '.' + i) + (n[i - 1] ? ': ' + n[i - 1] : '')
  }

  function css() {
    if ($('vd-css')) return
    const st = document.createElement('style'); st.id = 'vd-css'
    st.textContent = `
.vd-f{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;align-items:end}
.vd-f label{display:block;font-size:12px;font-weight:700;color:var(--muted);margin-bottom:4px}
.vd-f input,.vd-f select{width:100%;padding:8px 10px;border:1px solid var(--border);border-radius:9px;font:13px 'Outfit','IBM Plex Sans',sans-serif;background:var(--surface);color:var(--text)}
.vd-f .w2{grid-column:span 2}
.vd-ok{font-size:12.5px;margin-top:6px;color:var(--muted)}
.vd-ok b{color:var(--accent)}
.vd-bad{color:var(--red)!important}
.vd-note{font-size:12.5px;color:var(--muted);line-height:1.55}
.vd-note summary{cursor:pointer;font-weight:700}
.vd-off td{opacity:.5}
@media(max-width:760px){.vd-f{grid-template-columns:1fr 1fr}.vd-f .w2{grid-column:span 2}}`
    document.head.appendChild(st)
  }

  function build() {
    css()
    $('sec-videos').innerHTML = `
      <div class="card" style="margin-bottom:14px">
        <div class="ch"><h2>🎬 Video qoʻshish</h2></div>
        <div class="mb">
          <div class="vd-f">
            <div><label for="vdLab">Dastur</label><select id="vdLab" onchange="VD.mods()"></select></div>
            <div><label for="vdMod">Modul</label><select id="vdMod" onchange="VD.slots()"></select></div>
            <div class="w2"><label for="vdSlot">Joy</label><select id="vdSlot" onchange="VD.fill()"></select></div>
            <div class="w2"><label for="vdUrl">YouTube yoki Vimeo havolasi</label><input id="vdUrl" placeholder="https://youtu.be/… yoki https://vimeo.com/123456789/abcdef1234" oninput="VD.check()"></div>
            <div><label for="vdTitle">Sarlavha</label><input id="vdTitle" maxlength="160" placeholder="masalan, Roʻyxatni qanday tuzish"></div>
            <div><label for="vdSec">Uzunligi, soniya</label><input id="vdSec" type="number" min="1" max="7200" placeholder="60"></div>
          </div>
          <div class="vd-ok" id="vdOk">Havolani kiriting.</div>
          <div style="display:flex;gap:8px;margin-top:12px;flex-wrap:wrap">
            <button class="btn bp" onclick="VD.save()">Saqlash</button>
            <button class="btn bs" onclick="VD.clear()">Tozalash</button>
          </div>
          <details class="vd-note" style="margin-top:12px"><summary>ⓘ Qanday ishlaydi</summary>
            <p>Saqlangan video saytda darhol chiqadi (sahifani yangilaganda). M0 videosini hamma koʻradi; pullik modul videosini faqat shu modulga kirish huquqi bor talaba koʻradi: havolani server beradi.</p>
            <p>YouTube'da videoni <b>Roʻyxatsiz</b> (Unlisted) qilib yuklang. Vimeo'da yopiq video havolasi oxiridagi kodi bilan (vimeo.com/123456789/<b>abcdef1234</b>) kiritiladi. Vimeo bepul rejasida joylanadigan va yopiq videolar uchun jami 3 GB joy bor (Vimeo Help Center, 2026-11-19). Havolasi bor odam videoni tashqarida ham ochishi mumkin, shuning uchun videoda faqat "qanday bajarish" koʻrsatilsin.</p>
            <p>Oʻchirish yozuvni yoʻq qilmaydi: holat "oʻchiq" boʻladi, saytda koʻrinmaydi, qayta yoqsa boʻladi.</p>
          </details>
        </div>
      </div>
      <div class="card">
        <div class="ch"><h2>Videolar roʻyxati</h2>
          <span style="display:flex;gap:8px"><select class="flt" id="vdFLab" onchange="VD.render()"><option value="">Hamma dasturlar</option></select>
          <button class="btn bs bsm" onclick="VD.load()">🔄 Yangilash</button></span></div>
        <div class="tbl-scroll"><table class="tbl"><thead><tr><th>Dastur</th><th>Modul</th><th>Joy</th><th>Video</th><th>Sarlavha</th><th>Holat</th><th></th></tr></thead><tbody id="vdRows"><tr><td colspan="7">Yuklanmoqda…</td></tr></tbody></table></div>
      </div>`
    built = true
  }

  async function loadLabs() {
    const { data } = await supabase.from('courses').select('slug,title,status').order('slug')
    labs = (data || []).filter(c => c.slug && c.slug !== 'test-lab')
    if (!labs.length) labs = [{ slug: 'master-lab', title: 'Magistratura dasturi' }]
    const opts = labs.map(c => `<option value="${esc(c.slug)}">${esc(c.title || c.slug)}</option>`).join('')
    $('vdLab').innerHTML = opts
    $('vdFLab').innerHTML = '<option value="">Hamma dasturlar</option>' + opts
    if (labs.some(c => c.slug === 'master-lab')) $('vdLab').value = 'master-lab'
    mods()
  }
  function mods() {
    const lab = $('vdLab').value, n = NAMES[lab] ? Object.keys(NAMES[lab]).length - 1 : 16
    let h = ''; for (let i = 0; i <= n; i++) h += `<option value="${i}">M${i}${i === 0 ? ' (bepul)' : ''}</option>`
    $('vdMod').innerHTML = h; slots()
  }
  function slots() {
    const lab = $('vdLab').value, mod = +$('vdMod').value
    const nm = (NAMES[lab] && NAMES[lab][mod]) || null, cnt = nm ? nm.length : 12
    const list = (mod === 0 ? ['l0'] : []).concat(Array.from({ length: cnt }, (_, i) => 'l' + (i + 1)), ['res'])
    $('vdSlot').innerHTML = list.map(s => {
      const has = rows.find(r => r.course_slug === lab && r.module_index === mod && r.slot === s && r.status === 'active' && r.video)
      return `<option value="${s}">${esc(slotName(lab, mod, s))}${has ? ' · video bor' : ''}</option>`
    }).join('')
    fill()
  }
  function fill() {
    const lab = $('vdLab').value, mod = +$('vdMod').value, slot = $('vdSlot').value
    const r = rows.find(x => x.course_slug === lab && x.module_index === mod && x.slot === slot)
    $('vdUrl').value = r ? (r.provider === 'vimeo' ? 'https://vimeo.com/' + r.video : 'https://youtu.be/' + r.video) : ''
    $('vdTitle').value = r ? (r.title || '') : ''
    $('vdSec').value = r && r.sec ? r.sec : ''
    check()
  }
  function check() {
    const v = $('vdUrl').value.trim(), ok = $('vdOk')
    if (!v) { ok.textContent = 'Havolani kiriting.'; ok.classList.remove('vd-bad'); return null }
    const d = detect(v)
    if (!d) { ok.textContent = 'Havola tanilmadi: YouTube (youtu.be/… , youtube.com/watch?v=…) yoki Vimeo (vimeo.com/123456789) boʻlsin.'; ok.classList.add('vd-bad'); return null }
    ok.classList.remove('vd-bad')
    ok.innerHTML = (d.p === 'vimeo' ? 'Vimeo' : 'YouTube') + ' · ID: <b>' + esc(d.v) + '</b>'
    return d
  }
  function clear() { $('vdUrl').value = ''; $('vdTitle').value = ''; $('vdSec').value = ''; check() }

  async function save() {
    const d = check(); if (!d) { toast('⚠️ Havolani tekshiring'); return }
    const sec = +$('vdSec').value || null
    const row = { course_slug: $('vdLab').value, module_index: +$('vdMod').value, slot: $('vdSlot').value,
      provider: d.p, video: d.v, title: $('vdTitle').value.trim() || null, sec: sec && sec > 0 && sec <= 7200 ? Math.round(sec) : null, status: 'active' }
    const { error } = await supabase.from('module_videos').upsert(row, { onConflict: 'course_slug,module_index,slot' })
    if (error) { toast('❌ ' + (/module_videos/.test(error.message) ? 'Videolar jadvali bazada yoʻq: migratsiya qoʻllanmagan' : error.message)); return }
    toast('✅ Saqlandi. Saytda sahifa yangilanganda chiqadi')
    await load()
  }
  async function toggle(id, on) {
    const { error } = await supabase.from('module_videos').update({ status: on ? 'active' : 'off' }).eq('id', id)
    if (error) { toast('❌ ' + error.message); return }
    toast(on ? '✅ Yoqildi' : 'Oʻchirildi (yozuv saqlanadi)'); await load()
  }
  function edit(id) {
    const r = rows.find(x => x.id === id); if (!r) return
    $('vdLab').value = r.course_slug; mods(); $('vdMod').value = String(r.module_index); slots(); $('vdSlot').value = r.slot; fill()
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }

  function render() {
    const f = $('vdFLab').value, list = rows.filter(r => !f || r.course_slug === f)
    const title = (s) => (labs.find(c => c.slug === s) || {}).title || s
    $('vdRows').innerHTML = list.length ? list.map(r => {
      const url = r.provider === 'vimeo' ? 'https://vimeo.com/' + r.video : 'https://youtu.be/' + r.video
      const on = r.status === 'active'
      return `<tr class="${on ? '' : 'vd-off'}"><td>${esc(title(r.course_slug))}</td><td>M${r.module_index}</td><td>${esc(slotName(r.course_slug, r.module_index, r.slot))}</td>
        <td><a href="${esc(url)}" target="_blank" rel="noopener">${r.provider === 'vimeo' ? 'Vimeo' : 'YouTube'}</a>${r.sec ? ' · ' + r.sec + ' s' : ''}</td>
        <td>${esc(r.title || '—')}</td><td>${on ? 'Faol' : 'Oʻchiq'}</td>
        <td style="white-space:nowrap"><button class="btn bs bsm" onclick="VD.edit(${r.id})">Tahrir</button> <button class="btn bs bsm" onclick="VD.toggle(${r.id},${on ? 'false' : 'true'})">${on ? 'Oʻchirish' : 'Yoqish'}</button></td></tr>`
    }).join('') : '<tr><td colspan="7">Hali video yoʻq. Yuqoridagi formadan qoʻshing.</td></tr>'
  }
  async function load() {
    const { data, error } = await supabase.from('module_videos').select('id,course_slug,module_index,slot,provider,video,title,sec,status,updated_at').order('course_slug').order('module_index').order('slot')
    if (error) {
      rows = []
      $('vdRows').innerHTML = `<tr><td colspan="7">${/module_videos/.test(error.message) ? 'Videolar jadvali bazada hali yoʻq: migratsiya <code>20261119_module_videos.sql</code> qoʻllanishi kerak.' : esc(error.message)}</td></tr>`
      return
    }
    rows = (data || []).sort((a, b) => a.course_slug.localeCompare(b.course_slug) || a.module_index - b.module_index || order(a.slot) - order(b.slot))
    render(); if ($('vdSlot').options.length) { const s = $('vdSlot').value; slots(); $('vdSlot').value = s }
  }
  const order = (s) => s === 'l0' ? 0 : s === 'res' ? 99 : +s.slice(1)

  async function open() {
    if (!built) build()
    if (!labs.length) await loadLabs()
    await load()
  }
  return { open, load, render, mods, slots, fill, check, clear, save, toggle, edit }
})()
