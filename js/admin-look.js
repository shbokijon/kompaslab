// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — admin-look.js (2026-11-17): Admin → Dizayn
//  Saytning koʻrinishi: mavzu (fasl/bayram, avtomatik yoki qoʻlda), shrift juftligi,
//  matn/sarlavha oʻlchami, bloklar orasidagi masofa, burchaklar, kontent kengligi, "Aa" tugmasi.
//  Jadval: site_settings (key='ui'), tarix: site_settings_log. Saytda qoʻllash: js/kompas-ui.js (KLook).
//  Mavzu, shrift va chegaralar roʻyxati bitta joyda — kompas-ui.js da; bu fayl ularni
//  koʻrinish oynasidagi (iframe) sahifadan oladi: window.KLook.
// ═══════════════════════════════════════════════════════════════
const LK = (() => {
  const PK = 'kompas_ui_prev', CK = 'kompas_ui_v1'
  const PAGES = [
    ['index.html', 'Bosh sahifa'], ['master-lab.html', 'Dastur sahifasi'], ['master-lab-dastur.html', 'Modullar roʻyxati'],
    ['master-lab-m0-1.html', 'Dars sahifasi (kirish kerak)'], ['narxlar.html', 'Narxlar'], ['mamlakatlar.html', 'Mamlakatlar'], ['savollar.html', 'Savollar']
  ]
  const PRESETS = {
    sp: [['Zich', 0.85], ['Oddiy', 1], ['Keng', 1.15]],
    r: [['Toʻgʻri', 0.3], ['Yumshoq', 1], ['Yumaloq', 1.5]],
    w: [['Tor', 0.92], ['Oddiy', 1], ['Keng', 1.1]]
  }
  let K = null, s = null, saved = null, savedAt = null, built = false, page = 'index.html', device = 'desk', dark = false

  const $ = (id) => document.getElementById(id)
  const esc = (x) => String(x == null ? '' : x).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;')
  const pct = (v) => Math.round(v * 100) + '%'
  const same = (a, b) => JSON.stringify(strip(a)) === JSON.stringify(strip(b))
  function strip(x) { const o = JSON.parse(JSON.stringify(x || {})); delete o._date; return o }

  function css() {
    if ($('lk-css')) return
    const st = document.createElement('style'); st.id = 'lk-css'
    st.textContent = `
.lk-grid{display:grid;grid-template-columns:minmax(0,430px) minmax(0,1fr);gap:14px;align-items:start}
.lk-side{display:flex;flex-direction:column;gap:14px}
.lk-prev{position:sticky;top:70px}
.lk-b{padding:14px 18px}
.lk-b h3{font-size:13px;font-weight:800;margin:0 0 10px}
.lk-note{font-size:12px;color:var(--muted);line-height:1.55;margin-top:8px}
.lk-seg{display:inline-flex;border:1px solid var(--border);border-radius:10px;overflow:hidden}
.lk-seg button{border:0;background:var(--surface);padding:7px 12px;font:700 12.5px 'Outfit','IBM Plex Sans',sans-serif;color:var(--muted);cursor:pointer}
.lk-seg button.on{background:var(--accent);color:#fff}
.lk-th{display:grid;grid-template-columns:repeat(auto-fill,minmax(92px,1fr));gap:8px}
.lk-t{border:2px solid var(--border);border-radius:12px;padding:8px;cursor:pointer;background:var(--surface);text-align:left;font-family:'Outfit','IBM Plex Sans',sans-serif}
.lk-t.on{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-lit)}
.lk-t.now{outline:2px dashed var(--accent2);outline-offset:2px}
.lk-sw{display:flex;height:22px;border-radius:7px;overflow:hidden;margin-bottom:6px;border:1px solid rgba(0,0,0,.06)}
.lk-sw i{flex:1}
.lk-t b{display:block;font-size:12px}
.lk-t small{font-size:10.5px;color:var(--muted)}
.lk-hol{width:100%;border-collapse:collapse;font-size:12.5px}
.lk-hol td{padding:5px 4px;border-top:1px solid var(--border);vertical-align:middle}
.lk-hol input[type=text],.lk-hol input[type=date]{width:100%;min-width:0;padding:5px 6px;border:1px solid var(--border);border-radius:7px;font:12px 'JetBrains Mono','IBM Plex Sans',monospace;background:var(--bg);color:var(--text)}
.lk-hol input.bad{border-color:var(--red);background:var(--red-lit)}
.lk-f{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.lk-fc{border:2px solid var(--border);border-radius:12px;padding:10px;cursor:pointer;background:var(--surface);text-align:left}
.lk-fc.on{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-lit)}
.lk-fc .h{font-size:19px;line-height:1.15;color:var(--text);margin-bottom:4px}
.lk-fc .p{font-size:12.5px;line-height:1.4;color:var(--text)}
.lk-fc small{display:block;margin-top:6px;font:600 10.5px 'Outfit','IBM Plex Sans',sans-serif;color:var(--muted)}
.lk-row{display:grid;grid-template-columns:130px 1fr 46px;gap:10px;align-items:center;font-size:12.5px;margin:8px 0}
.lk-row input[type=range]{width:100%;accent-color:var(--accent)}
.lk-row output{font:700 12px 'JetBrains Mono','IBM Plex Sans',monospace;text-align:right}
.lk-pre{display:flex;gap:4px;margin:-2px 0 8px 140px;flex-wrap:wrap}
.lk-pre button{border:1px solid var(--border);background:var(--surface);border-radius:7px;padding:3px 9px;font:600 11.5px 'Outfit','IBM Plex Sans',sans-serif;color:var(--muted);cursor:pointer}
.lk-pre button.on{border-color:var(--accent);color:var(--accent);background:var(--accent-lit)}
.lk-bar{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.lk-dirty{font-size:12px;color:var(--accent2);font-weight:700}
.lk-fw{background:repeating-conic-gradient(#eef1ef 0 25%,#f7f8f7 0 50%) 0 0/18px 18px;border-top:1px solid var(--border);display:flex;justify-content:center;height:calc(100vh - 190px);min-height:520px}
.lk-fw iframe{border:0;width:100%;height:100%;background:#fff}
.lk-fw.mob iframe{width:390px;box-shadow:0 0 0 1px var(--border),0 10px 30px rgba(0,0,0,.08)}
.lk-now{font-size:12.5px;padding:8px 10px;border-radius:9px;background:var(--accent-lit);color:var(--accent);margin-bottom:10px;line-height:1.5}
.lk-log{font-size:12px}
.lk-log div{display:flex;justify-content:space-between;gap:8px;padding:5px 0;border-top:1px solid var(--border)}
@media(max-width:1100px){.lk-grid{grid-template-columns:1fr}.lk-prev{position:static}.lk-fw{height:70vh}}
`
    document.head.appendChild(st)
  }

  function build() {
    css()
    const sec = $('sec-look')
    sec.innerHTML = `
<div class="lk-grid">
  <div class="lk-side">
    <div class="card">
      <div class="ch"><h2>🎨 Dizayn</h2><div class="lk-bar"><span class="lk-dirty" id="lkDirty"></span></div></div>
      <div class="lk-b">
        <div class="lk-bar">
          <button class="btn bp bsm" id="lkSave" onclick="LK.save()">Saytga saqlash</button>
          <button class="btn bs bsm" onclick="LK.revert()">Saqlanganiga qaytarish</button>
          <button class="btn bs bsm" onclick="LK.reset()">Standart</button>
        </div>
        <div class="lk-note" id="lkInfo">Oʻzgarishlar oʻngdagi oynada darhol koʻrinadi. Saytga “Saytga saqlash” bosilgandan keyin chiqadi: tashrifchilarda 5 daqiqagacha (keyingi ochilishda). Deploy kerak emas.</div>
      </div>
    </div>
    <div class="card"><div class="lk-b" id="lkTheme"></div></div>
    <div class="card"><div class="lk-b" id="lkFont"></div></div>
    <div class="card"><div class="lk-b" id="lkSize"></div></div>
    <div class="card"><div class="lk-b"><h3>Oʻzgarishlar tarixi</h3><div class="lk-log" id="lkLog">—</div></div></div>
  </div>
  <div class="card lk-prev">
    <div class="ch" style="gap:8px;flex-wrap:wrap">
      <select class="flt" id="lkPage" onchange="LK.page(this.value)">${PAGES.map(p => `<option value="${p[0]}">${esc(p[1])}</option>`).join('')}</select>
      <div class="lk-seg" id="lkDev"><button class="on" data-v="desk" onclick="LK.device('desk')">🖥️ Kompyuter</button><button data-v="mob" onclick="LK.device('mob')">📱 Telefon</button></div>
      <div class="lk-seg" id="lkDark"><button class="on" data-v="0" onclick="LK.dark(false)">☀ Yorugʻ</button><button data-v="1" onclick="LK.dark(true)">☾ Tungi</button></div>
      <label style="font-size:12px;color:var(--muted);display:flex;align-items:center;gap:6px">Sana: <input type="date" class="flt" id="lkDate" onchange="LK.date(this.value)" title="Avtomatik rejimda shu sanada qaysi mavzu chiqishini koʻrish (saqlanmaydi)"></label>
    </div>
    <div class="lk-fw" id="lkFw"><iframe id="lkFrame" title="Sayt koʻrinishi"></iframe></div>
  </div>
</div>`
    $('lkFrame').addEventListener('load', onFrame)
    // Admin sahifasidagi namunalar uchun hamma shriftlar (faqat shu boʻlim ochilganda)
    built = true
  }

  function fontsLink() {
    if ($('lk-fonts') || !K) return
    const q = Object.values(K.FONTS).map(f => f.q).filter(Boolean).join('&')
    const l = document.createElement('link'); l.id = 'lk-fonts'; l.rel = 'stylesheet'
    l.href = 'https://fonts.googleapis.com/css2?' + q + '&family=Caladea:wght@400;700&display=swap'
    document.head.appendChild(l)
  }

  async function load() {
    const { data, error } = await supabase.from('site_settings').select('value,updated_at').eq('key', 'ui').maybeSingle()
    if (error) {
      $('lkInfo').innerHTML = '<span style="color:var(--red)">' + esc(/site_settings/.test(error.message) ? 'site_settings jadvali bazada yoʻq (migratsiya 20261117_site_settings.sql qoʻllanmagan). Koʻrinish oynasi ishlaydi, saqlash ishlamaydi.' : error.message) + '</span>'
    }
    saved = data ? data.value : null
    savedAt = data ? data.updated_at : null
    loadLog()
  }
  async function loadLog() {
    const { data } = await supabase.from('site_settings_log').select('id,value,changed_at').eq('key', 'ui').order('id', { ascending: false }).limit(10)
    LK._log = data || []
    $('lkLog').innerHTML = (savedAt ? `<div><span>Hozirgi: ${esc(String(savedAt).slice(0, 16).replace('T', ' '))}</span><span></span></div>` : '') +
      (LK._log.length ? LK._log.map((r, i) => `<div><span>${esc(String(r.changed_at).slice(0, 16).replace('T', ' '))} · ${esc(describe(r.value))}</span><button class="btn bs bsm" onclick="LK.fromLog(${i})">Tahrirga olish</button></div>`).join('') : '<div style="color:var(--muted)">Oldingi holat yoʻq</div>')
  }
  function describe(v) {
    if (!K) return ''
    const m = K.merge(v)
    return (m.mode === 'auto' ? 'Avtomatik' : (K.THEMES[m.theme] || {}).n) + ', ' + ((K.FONTS[m.font] || {}).n || '').replace(/ \(.*\)$/, '') + ', matn ' + pct(m.fs)
  }

  function pushPreview() {
    try { sessionStorage.setItem(PK, JSON.stringify(s)) } catch (e) {}
    const w = $('lkFrame').contentWindow
    try { if (w && w.KLook) w.KLook.apply(s) } catch (e) {}
    dirty()
    renderNow()
  }
  function dirty() {
    const d = !same(s, K.merge(saved))
    $('lkDirty').textContent = d ? '● Saqlanmagan oʻzgarish bor' : ''
  }
  function onFrame() {
    const w = $('lkFrame').contentWindow
    let k = null
    try { k = w.KLook } catch (e) {}
    if (!k) return
    try { w.document.documentElement.setAttribute('data-theme', dark ? 'dark' : 'light') } catch (e) {}
    if (!K) {
      K = k
      s = K.merge(saved)
      fontsLink()
      render()
      pushPreview()
    }
  }

  function render() { renderTheme(); renderFont(); renderSize(); dirty(); if (LK._log) loadLog() }
  function swatch(t) {
    const c = t.c || { a2: '#c4622d', bg: '#f4f3ef', g: '#8a6a10', al: '#e8f0ec' }
    return `<span class="lk-sw"><i style="background:#2d4a3e"></i><i style="background:${c.a2}"></i><i style="background:${c.g}"></i><i style="background:${c.bg}"></i></span>`
  }
  function renderNow() {
    const el = $('lkNow'); if (!el || !K) return
    const d = K.today(s), r = K.resolve(s), t = K.THEMES[r.id] || {}
    el.innerHTML = s.mode === 'auto'
      ? `Avtomatik: <b>${esc(d)}</b> (Toshkent) sanasida <b>${esc(t.e + ' ' + t.n)}</b> chiqadi (${esc(r.why)}).`
      : `Qoʻlda: saytda doim <b>${esc(t.e + ' ' + t.n)}</b>.`
    document.querySelectorAll('.lk-t').forEach(b => b.classList.toggle('now', b.dataset.t === r.id && s.mode === 'auto'))
  }
  function renderTheme() {
    const T = K.THEMES
    const tiles = (kind) => Object.keys(T).filter(id => T[id].k === kind).map(id =>
      `<button type="button" class="lk-t${s.mode === 'manual' && s.theme === id ? ' on' : ''}" data-t="${id}" onclick="LK.theme('${id}')">${swatch(T[id])}<b>${esc(T[id].e + ' ' + T[id].n)}</b></button>`).join('')
    const rows = K.HOLS.map(h => {
      const x = s.hol[h.id], yearly = /^\d{2}-\d{2}$/.test(K.DEF.hol[h.id].from)
      const inp = (k) => yearly
        ? `<input type="text" value="${esc(x[k])}" placeholder="OO-KK" maxlength="10" onchange="LK.hol('${h.id}','${k}',this)">`
        : `<input type="date" value="${esc(x[k])}" onchange="LK.hol('${h.id}','${k}',this)">`
      return `<tr><td style="width:24px"><input type="checkbox" ${x.on ? 'checked' : ''} onchange="LK.hol('${h.id}','on',this)"></td><td>${esc(h.n)}<br><small style="color:var(--muted)">${yearly ? 'har yil' : 'bu yilgi sana'}</small></td><td>${inp('from')}</td><td>${inp('to')}</td></tr>`
    }).join('')
    $('lkTheme').innerHTML = `
<h3>Mavzu</h3>
<div class="lk-bar" style="margin-bottom:10px"><div class="lk-seg"><button class="${s.mode === 'auto' ? 'on' : ''}" onclick="LK.mode('auto')">Avtomatik</button><button class="${s.mode === 'manual' ? 'on' : ''}" onclick="LK.mode('manual')">Qoʻlda</button></div></div>
<div class="lk-now" id="lkNow"></div>
<div class="lk-th">${tiles('asosiy')}${tiles('fasl')}</div>
<div class="lk-th" style="margin-top:8px">${tiles('bayram')}</div>
<div class="lk-note">Faqat urgʻu va fon tusi oʻzgaradi. Asosiy yashil rang va logotip hamma mavzuda bir xil. Tungi rejim oʻz ranglarida qoladi. Mavzuni bossangiz, rejim “Qoʻlda” ga oʻtadi.</div>
${s.mode === 'auto' ? `
<h3 style="margin-top:14px">Avtomatik qoida</h3>
<label style="font-size:12.5px;display:flex;gap:8px;align-items:center;margin-bottom:8px"><input type="checkbox" ${s.seasons ? 'checked' : ''} onchange="LK.set('seasons',this.checked)"> Fasllar: Qish (dek–fev), Bahor (mar–may), Yoz (iyun–avg), Kuz (sen–noy)</label>
<table class="lk-hol"><tbody>${rows}</tbody></table>
<div class="lk-note">Bayram fasldan ustun. Bir necha bayram toʻqnashsa, roʻyxatdagi yuqoridagisi chiqadi. Ramazon va Hayitlar sanasi har yili oʻzgaradi: Oʻzbekiston musulmonlari idorasi eʼlonidan kiriting (<a href="https://muslim.uz" target="_blank" rel="noopener">muslim.uz</a>). Bitta kunlik bayram uchun “dan” ni toʻldirish yetarli. Sana boʻsh boʻlsa, bayram ishlamaydi.</div>` : ''}`
    renderNow()
  }
  function renderFont() {
    const F = K.FONTS
    const fam = (stack, def) => esc(stack || def)
    $('lkFont').innerHTML = `<h3>Shrift</h3><div class="lk-f">${Object.keys(F).map(id => {
      const f = F[id]
      return `<button type="button" class="lk-fc${s.font === id ? ' on' : ''}" onclick="LK.set('font','${id}')">
<div class="h" style="font-family:${fam(f.h, '"Cambria","Caladea","Playfair Display",serif')}">Kuzatuvdan kashfiyotga</div>
<div class="p" style="font-family:${fam(f.b, '"Outfit","IBM Plex Sans",sans-serif')}" data-alifbo="off">Öqituvçi, ğalaba, şahar, çiroq. Oʻzbek tili — 2026</div>
<small>${esc(f.n)} · ${esc(f.d)}</small></button>`
    }).join('')}</div>
<div class="lk-note">Sarlavha va matn shriftlari juftlikda tanlanadi. Hamma juftlikda Ö, Ğ, Ş, Ç, ʻ, ʼ uchun zaxira shrift ulangan: tanlangan shriftda belgi boʻlmasa ham harf toʻgʻri chiqadi. Kod (JetBrains Mono) oʻzgarmaydi. Standartdan boshqa shrift sahifaga qoʻshimcha yuklanadi (taxminan 60–150 KB).</div>`
  }
  function slider(k, label, min, max) {
    const v = s[k]
    const pre = PRESETS[k] ? `<div class="lk-pre">${PRESETS[k].map(p => `<button type="button" class="${Math.abs(v - p[1]) < 0.001 ? 'on' : ''}" onclick="LK.set('${k}',${p[1]})">${esc(p[0])}</button>`).join('')}</div>` : ''
    return `<div class="lk-row"><span>${esc(label)}</span><input type="range" min="${min}" max="${max}" step="1" value="${Math.round(v * 100)}" oninput="LK.slide('${k}',this)"><output id="lkO_${k}">${pct(v)}</output></div>${pre}`
  }
  function renderSize() {
    const L = K.LIM
    $('lkSize').innerHTML = `<h3>Oʻlchamlar</h3>
${slider('fs', 'Matn oʻlchami', L.fs[0] * 100, L.fs[1] * 100)}
${slider('hs', 'Sarlavha oʻlchami', L.hs[0] * 100, L.hs[1] * 100)}
${slider('sp', 'Bloklar orasi', L.sp[0] * 100, L.sp[1] * 100)}
${slider('r', 'Burchaklar', L.r[0] * 100, L.r[1] * 100)}
${slider('w', 'Kontent kengligi', L.w[0] * 100, L.w[1] * 100)}
<label style="font-size:12.5px;display:flex;gap:8px;align-items:center;margin-top:10px"><input type="checkbox" ${s.reader ? 'checked' : ''} onchange="LK.set('reader',this.checked)"> Talabaga “Aa” tugmasi (A− / A+): har kim oʻzi uchun matnni ${pct(K.FS_STEPS[0])}–${pct(K.FS_STEPS[K.FS_STEPS.length - 1])} oraligʻida oʻzgartiradi</label>
<div class="lk-note">Bu sozlamalar butun saytga taalluqli (bosh sahifa, dastur, modul va dars sahifalari). Kabinet, kirish, admin va pullik modul oynasi hozircha oʻzgarmaydi. “Bloklar orasi” ichki boʻshliqlarni (padding, gap) oʻzgartiradi; juda katta qiymat telefonda joyni toraytiradi: “📱 Telefon” koʻrinishida tekshiring.</div>`
  }

  // ── Amallar ──
  function set(k, v) { s[k] = v; if (k === 'font' || k === 'reader') renderFont(), renderSize(); if (k === 'seasons') renderTheme(); if (PRESETS[k] || ['fs', 'hs'].includes(k)) renderSize(); pushPreview() }
  function slide(k, el) { s[k] = +el.value / 100; $('lkO_' + k).textContent = pct(s[k]); pushPreview() }
  function theme(id) { s.mode = 'manual'; s.theme = id; renderTheme(); pushPreview() }
  function mode(m) { s.mode = m; renderTheme(); pushPreview() }
  function hol(id, k, el) {
    const x = s.hol[id]
    if (k === 'on') x.on = el.checked
    else {
      const v = el.value.trim(), yearly = el.type === 'text'
      const ok = !v || (yearly ? /^(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$/.test(v) : /^\d{4}-\d{2}-\d{2}$/.test(v))
      el.classList.toggle('bad', !ok)
      if (!ok) return
      x[k] = v
    }
    pushPreview()
  }
  async function save() {
    const v = strip(K.merge(s))
    const b = $('lkSave'); b.disabled = true
    let r = await supabase.from('site_settings').update({ value: v }).eq('key', 'ui').select('updated_at')
    if (!r.error && (!r.data || !r.data.length)) r = await supabase.from('site_settings').insert({ key: 'ui', value: v }).select('updated_at')
    b.disabled = false
    if (r.error) { toast('❌ ' + r.error.message); return }
    saved = v; savedAt = r.data && r.data[0] ? r.data[0].updated_at : new Date().toISOString()
    // Shu brauzerda sayt darhol yangi koʻrinishda ochilsin
    try { localStorage.setItem(CK, JSON.stringify({ t: Date.now(), d: v })) } catch (e) {}
    toast('✅ Saqlandi. Tashrifchilarda 5 daqiqagacha yangilanadi')
    dirty(); loadLog()
  }
  function revert() { s = K.merge(saved); if ($('lkDate').value) s._date = $('lkDate').value; render(); pushPreview() }
  function reset() { const d = s._date; s = K.merge(null); if (d) s._date = d; render(); pushPreview() }
  function fromLog(i) { const r = (LK._log || [])[i]; if (!r) return; s = K.merge(r.value); render(); pushPreview(); toast('Tahrirga olindi. Saytga chiqarish uchun “Saytga saqlash”') }
  function date(v) { if (v) s._date = v; else delete s._date; pushPreview() }
  function setPage(p) { page = p; $('lkFrame').src = '/' + p }
  function setDevice(d) {
    device = d
    $('lkFw').classList.toggle('mob', d === 'mob')
    document.querySelectorAll('#lkDev button').forEach(b => b.classList.toggle('on', b.dataset.v === d))
  }
  function setDark(on) {
    dark = on
    document.querySelectorAll('#lkDark button').forEach(b => b.classList.toggle('on', b.dataset.v === (on ? '1' : '0')))
    try { $('lkFrame').contentWindow.document.documentElement.setAttribute('data-theme', on ? 'dark' : 'light') } catch (e) {}
  }

  async function open() {
    if (!built) build()
    await load()
    if (K) { s = K.merge(saved); render(); pushPreview(); return }
    // Koʻrinish oynasi sozlamani sessionStorage dan oʻqiydi (faqat iframe ichida)
    try { sessionStorage.setItem(PK, JSON.stringify(saved || {})) } catch (e) {}
    $('lkFrame').src = '/' + page
  }

  return { open, save, revert, reset, set, slide, theme, mode, hol, fromLog, date, page: setPage, device: setDevice, dark: setDark }
})()
