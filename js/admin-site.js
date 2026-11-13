// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — admin-site.js (2026-11-13): Admin → Vebsayt
//  Sahifa boʻlimlari va qismlari roʻyxati, koʻrinadi/yashirin, oʻzgarishlar tarixi,
//  "Jonli tahrirlash" (haqiqiy sahifa ?kedit=1, js/site-editor.js).
//  Jadval: site_edits. Saytda qoʻllash: js/kompas-ui.js (KSiteEdits).
//  norm/txt/path/guard pastda kompas-ui.js dagi bilan AYNAN bir xil boʻlishi shart
//  (tekshiruv: node tools/site/test_site_edits.cjs).
// ═══════════════════════════════════════════════════════════════
const WS = (() => {
  const G = 60
  const SKIPT = { SCRIPT: 1, STYLE: 1, NOSCRIPT: 1, TEMPLATE: 1 }
  function txt(el) {
    if (!el) return ''
    if (el.nodeType === 3) return el.nodeValue
    let out = ''
    const tw = (el.ownerDocument || document).createTreeWalker(el, 4, null)
    let n
    while ((n = tw.nextNode())) {
      let p = n.parentNode, bad = false
      while (p && p !== el) { if (SKIPT[p.nodeName]) { bad = true; break } p = p.parentNode }
      if (!bad) out += n.nodeValue
    }
    return out
  }
  function norm(s) {
    return String(s || '').toLowerCase()
      .replace(/([og])[\u02bb\u02bc'\u2018\u2019`]/g, '$1')
      .replace(/ö/g, 'o').replace(/ğ/g, 'g').replace(/ş/g, 'sh').replace(/ç/g, 'ch')
      .replace(/[^a-z\u00c0-\u024f\u0400-\u04ff]/g, '')
  }
  function guard(el) { return norm(txt(el)).slice(0, G) }
  function okId(id, doc) {
    if (!id || !/^[A-Za-z][\w-]*$/.test(id)) return false
    try { return doc.querySelectorAll('#' + id).length === 1 } catch (e) { return false }
  }
  function path(el) {
    const doc = el.ownerDocument || document, parts = []
    while (el && el.nodeType === 1 && el !== doc.body && el !== doc.documentElement) {
      const id = el.getAttribute('id')
      if (okId(id, doc)) { parts.unshift('#' + id); return parts.join(' > ') }
      let i = 1, s = el
      while ((s = s.previousElementSibling)) if (s.tagName === el.tagName) i++
      parts.unshift(el.tagName.toLowerCase() + ':nth-of-type(' + i + ')')
      el = el.parentElement
    }
    parts.unshift('body')
    return parts.join(' > ')
  }

  const COLS = 'id,page,sel,kind,guard,label,value,status,note,created_at,updated_at'
  const SKIP = /^(SCRIPT|STYLE|NOSCRIPT|TEMPLATE|LINK|META|BR|HR)$/
  // kompas-ui.js yuklamaydigan sahifalar: ularda tahrir qoʻllanmaydi
  const NO_UI = ['master-lab-manbalar.html', 'sources.html']
  let pages = [], file = 'index.html', doc = null, edits = [], hideRows = []

  const short = (s, n) => { s = String(s || '').replace(/\s+/g, ' ').trim(); return s.length > n ? s.slice(0, n - 1) + '…' : s }
  const urlOf = (f) => '/' + (f === 'index.html' ? '' : f.replace(/\.html$/, ''))
  // Yorliq uchun: matn boʻlaklari orasiga boʻsh joy (guard emas, faqat koʻrsatish)
  function words(el) {
    const tw = (el.ownerDocument || document).createTreeWalker(el, 4, null), out = []
    let n
    while ((n = tw.nextNode())) { let p = n.parentNode, bad = false; while (p && p !== el) { if (SKIPT[p.nodeName]) { bad = true; break } p = p.parentNode } if (!bad) out.push(n.nodeValue) }
    return out.join(' ')
  }
  function label(el) {
    const h = el.querySelector('h1,h2,h3,h4')
    const t = short(words(h || el), 70)
    return '<' + el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + '> ' + (t || '(matnsiz)')
  }
  function groupOf(f) {
    const m = /^(bachelor-lab|master-lab|phd-lab|gks-lab|usa-lab|daad-lab|musofir-lab|tadbirkor-talaba|atlas)/.exec(f)
    if (!m) return 'Sayt'
    return { atlas: 'Atlas' }[m[1]] || m[1].replace('-lab', '').replace(/^\w/, c => c.toUpperCase()).replace('Tadbirkor-talaba', 'Tadbirkor Talaba') + ' Lab'
  }

  async function loadPages() {
    if (pages.length) return
    try {
      const x = await (await fetch('/sitemap.xml', { cache: 'no-store' })).text()
      pages = [...x.matchAll(/<loc>https?:\/\/[^/]+\/?([^<]*)<\/loc>/g)].map(m => (m[1] || 'index').replace(/\.html$/, '') + '.html')
    } catch (e) { pages = ['index.html', 'qanday-ishlaydi.html', 'narxlar.html', 'savollar.html'] }
    pages = [...new Set(pages)].filter(f => !NO_UI.includes(f))
    const groups = {}
    pages.forEach(f => { (groups[groupOf(f)] = groups[groupOf(f)] || []).push(f) })
    const order = ['Sayt', ...Object.keys(groups).filter(g => g !== 'Sayt' && g !== 'Atlas').sort(), 'Atlas'].filter(g => groups[g])
    const sel = document.getElementById('wsPage')
    sel.innerHTML = order.map(g => '<optgroup label="' + escHtml(g) + '">' +
      groups[g].map(f => '<option value="' + escHtml(f) + '">' + escHtml(f.replace(/\.html$/, '')) + '</option>').join('') + '</optgroup>').join('') +
      '<option value="__other">Boshqa sahifa…</option>'
    sel.value = file
  }

  function blocks(d) {
    const out = []
    const kids = (el) => [...el.children].filter(c => !SKIP.test(c.nodeName))
    kids(d.body).forEach(el => {
      if (el.nodeName === 'MAIN') kids(el).forEach(c => out.push(c))
      else out.push(el)
    })
    return out
  }
  function partsOf(el) {
    let c = el
    for (let i = 0; i < 4; i++) {
      const k = [...c.children].filter(x => !SKIP.test(x.nodeName))
      if (k.length === 1 && !/^H\d$/.test(k[0].nodeName)) c = k[0]; else break
    }
    const k = [...c.children].filter(x => !SKIP.test(x.nodeName) && norm(txt(x)))
    return k.length >= 2 ? k : []
  }
  function hideRowFor(el) {
    const p = path(el), g = guard(el), tag = el.tagName.toLowerCase()
    return hideRows.find(r => r.sel === p) ||
      (g ? hideRows.find(r => r.guard === g && new RegExp('(^|> )' + tag + '(:nth-of-type\\(\\d+\\))?$').test(r.sel)) : null)
  }

  async function open() {
    await loadPages()
    const box = document.getElementById('wsBlocks')
    box.innerHTML = '<tr><td colspan="3" style="color:var(--muted)">Yuklanmoqda…</td></tr>'
    document.getElementById('wsTitle').textContent = 'Sahifa boʻlimlari: ' + file
    document.getElementById('wsOpen').href = urlOf(file)
    try {
      const r = await fetch('/' + file, { cache: 'no-store', credentials: 'same-origin' })
      if (!r.ok) throw new Error('HTTP ' + r.status)
      doc = new DOMParser().parseFromString(await r.text(), 'text/html')
      if (!/kompas-ui\.js/.test(doc.documentElement.innerHTML)) {
        box.innerHTML = '<tr><td colspan="3" style="color:var(--red)">Bu sahifa js/kompas-ui.js ni yuklamaydi: oʻzgarishlar saytda qoʻllanmaydi.</td></tr>'
        await loadEdits(); return
      }
    } catch (e) {
      box.innerHTML = '<tr><td colspan="3" style="color:var(--red)">Sahifa ochilmadi: ' + escHtml(e.message) + '</td></tr>'
      return
    }
    await loadEdits()
    render()
  }

  function render() {
    const box = document.getElementById('wsBlocks')
    if (!doc) return
    const list = blocks(doc)
    let h = '', n = 0
    const row = (el, sub) => {
      const r = hideRowFor(el), p = path(el), g = guard(el), id = 'ws' + (n++)
      const parentHidden = sub && sub.hidden
      return '<tr' + (sub ? ' class="ws-sub" data-par="' + sub.id + '" style="display:none"' : '') + '>' +
        '<td style="' + (sub ? 'padding-left:34px;' : '') + 'max-width:520px">' +
          (!sub && partsOf(el).length ? '<button class="btn bs bsm ws-tg" data-id="' + id + '" title="Qismlar" style="padding:2px 7px;margin-right:6px">▸</button>' : '') +
          '<span style="font-weight:' + (sub ? 500 : 700) + '">' + escHtml(label(el)) + '</span>' +
          '<div style="font-family:JetBrains Mono,monospace;font-size:10.5px;color:var(--muted2);margin-top:2px">' + escHtml(short(p, 80)) + '</div></td>' +
        '<td><label class="ws-sw" title="' + (parentHidden ? 'Yuqori boʻlim yashirin' : '') + '"><input type="checkbox" ' + (r ? '' : 'checked') +
          ' data-sel="' + escHtml(p) + '" data-g="' + escHtml(g) + '" data-l="' + escHtml(short(label(el), 160)) + '"' + (r ? ' data-row="' + r.id + '"' : '') +
          ' onchange="WS.toggle(this)"> <span>' + (r ? 'Yashirin' : 'Koʻrinadi') + '</span></label></td>' +
        '<td><a class="btn bs bsm" style="text-decoration:none" target="_blank" rel="noopener" href="' + escHtml(liveUrl(p, g)) + '">✏️ Jonli</a></td></tr>' +
        (!sub ? partsOf(el).map(c => row(c, { id, hidden: !!r })).join('') : '')
    }
    list.forEach(el => { h += row(el, null) })
    box.innerHTML = h || '<tr><td colspan="3" style="color:var(--muted)">Boʻlim topilmadi</td></tr>'
    box.querySelectorAll('.ws-tg').forEach(b => b.onclick = () => {
      const on = b.textContent === '▸'
      b.textContent = on ? '▾' : '▸'
      box.querySelectorAll('tr[data-par="' + b.dataset.id + '"]').forEach(t => { t.style.display = on ? '' : 'none' })
    })
    document.getElementById('wsInfo').textContent = list.length + ' ta boʻlim · ' + hideRows.length + ' ta yashirin'
  }
  const liveUrl = (sel, g) => urlOf(file) + '?kedit=1' + (sel ? '&ksel=' + encodeURIComponent(sel) + '&kg=' + encodeURIComponent(g || '') : '')

  async function toggle(cb) {
    const show = cb.checked
    cb.disabled = true
    try {
      if (!show) {
        const ins = { page: file, sel: cb.dataset.sel, kind: 'hide', guard: cb.dataset.g || '', label: cb.dataset.l, status: 'active' }
        let res = await supabase.from('site_edits').insert(ins).select(COLS).single()
        if (res.error && res.error.code === '23505') {
          const o = await supabase.from('site_edits').select('id').eq('page', file).eq('sel', ins.sel).eq('kind', 'hide').eq('status', 'active').maybeSingle()
          if (o.data) res = await supabase.from('site_edits').update({ guard: ins.guard, label: ins.label }).eq('id', o.data.id).select(COLS).single()
        }
        if (res.error) throw res.error
        toast('🙈 Yashirildi. Saytda bir necha daqiqada (yangi tashrifda) koʻrinmaydi')
      } else {
        const { error } = await supabase.from('site_edits').update({ status: 'off' }).eq('id', +cb.dataset.row)
        if (error) throw error
        toast('👁 Yana koʻrinadi')
      }
    } catch (e) { toast('❌ ' + (e.message || e)); cb.checked = !show }
    cb.disabled = false
    await loadEdits(); render()
  }

  async function loadEdits() {
    const scope = document.getElementById('wsScope').value, st = document.getElementById('wsStatus').value
    let q = supabase.from('site_edits').select(COLS).order('updated_at', { ascending: false }).limit(500)
    if (scope === 'page') q = q.eq('page', file)
    if (st) q = q.eq('status', st)
    const { data, error } = await q
    const tb = document.getElementById('wsEdits')
    if (error) {
      tb.innerHTML = '<tr><td colspan="6" style="color:var(--red)">' + escHtml(/site_edits/.test(error.message) ? 'site_edits jadvali bazada yoʻq (migratsiya 20261113_site_edits.sql qoʻllanmagan)' : error.message) + '</td></tr>'
      edits = []; hideRows = []; return
    }
    edits = data || []
    if (scope === 'page' && st === 'active') hideRows = edits.filter(r => r.kind === 'hide')
    else {
      const a = await supabase.from('site_edits').select(COLS).eq('page', file).eq('status', 'active').eq('kind', 'hide')
      hideRows = a.data || []
    }
    tb.innerHTML = edits.length ? edits.map(r => {
      const val = r.kind === 'html' ? short((r.value || '').replace(/<br\s*\/?>/gi, ' ').replace(/<[^>]+>/g, ''), 90) : '—'
      const on = r.status === 'active'
      return '<tr><td><a href="' + escHtml(urlOf(r.page)) + '" target="_blank" rel="noopener">' + escHtml(r.page.replace(/\.html$/, '')) + '</a></td>' +
        '<td>' + (r.kind === 'hide' ? '🙈 Yashirish' : '✏️ Matn') + '</td>' +
        '<td style="max-width:280px;font-size:12px">' + escHtml(short(r.label || r.sel, 90)) + '</td>' +
        '<td style="max-width:320px;font-size:12px">' + escHtml(val) + '</td>' +
        '<td style="font-size:12px;white-space:nowrap">' + escHtml(String(r.updated_at || '').slice(0, 16).replace('T', ' ')) + '</td>' +
        '<td style="white-space:nowrap">' + (on
          ? '<span class="tag tgr">Faol</span> <button class="btn bs bsm" onclick="WS.setStatus(' + r.id + ',\'off\')">Bekor qilish</button>' +
            ' <a class="btn bs bsm" style="text-decoration:none" target="_blank" rel="noopener" href="' + escHtml(urlOf(r.page) + '?kedit=1&ksel=' + encodeURIComponent(r.sel) + '&kg=' + encodeURIComponent(r.guard || '')) + '">↗</a>'
          : '<span style="color:var(--muted);font-size:12px">Bekor qilingan</span> <button class="btn bs bsm" onclick="WS.setStatus(' + r.id + ',\'active\')">Qayta yoqish</button>') +
        '</td></tr>'
    }).join('') : '<tr><td colspan="6" style="color:var(--muted)">Oʻzgarish yoʻq</td></tr>'
  }
  async function setStatus(id, status) {
    if (status === 'off' && !confirm('Bu oʻzgarish bekor qilinsinmi? Sayt manbadagi asl holatiga qaytadi.')) return
    const { error } = await supabase.from('site_edits').update({ status }).eq('id', id)
    if (error) { toast('❌ ' + (error.code === '23505' ? 'Shu joyda boshqa faol oʻzgarish bor: avval uni bekor qiling' : error.message)); return }
    toast(status === 'off' ? '✅ Bekor qilindi' : '✅ Qayta yoqildi')
    await loadEdits(); render()
  }

  function pick(v) {
    if (v === '__other') {
      const f = prompt('Sahifa fayli (masalan: master-lab-m0.html yoki oferta):', '')
      v = (f || '').trim().replace(/^https?:\/\/[^/]+/i, '').replace(/[?#].*$/, '').replace(/^\/+/, '')
      if (!v) { document.getElementById('wsPage').value = file; return }
      if (!/\.html?$/.test(v)) v += '.html'
      if (!/^[a-z0-9][a-z0-9._-]*\.html$/.test(v)) { toast('⚠️ Fayl nomi notoʻgʻri'); document.getElementById('wsPage').value = file; return }
      const s = document.getElementById('wsPage')
      if (![...s.options].some(o => o.value === v)) s.insertAdjacentHTML('afterbegin', '<option value="' + escHtml(v) + '">' + escHtml(v.replace(/\.html$/, '')) + '</option>')
      s.value = v
    }
    file = v
    open()
  }
  return { open, pick, toggle, loadEdits: () => loadEdits().then(render), setStatus, live: () => window.open(liveUrl(), '_blank', 'noopener'), _t: { norm, txt, guard, path } }
})()

// admin.html#vebsayt (sayt muharriridan kelganda) — kirish tekshiruvidan keyin ochiladi
;(function () {
  if (location.hash !== '#vebsayt') return
  let n = 0
  const t = setInterval(() => {
    if (document.body.style.display !== 'none') { clearInterval(t); nav('website', document.getElementById('wsNav')) }
    else if (++n > 100) clearInterval(t)
  }, 150)
})()
