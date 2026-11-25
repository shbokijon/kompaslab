// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — kompas-ui.js (2026-10-18)
//  Har sahifada <head> ichida (defer emas) yuklanadi:
//  · Sahifalar orasidagi oʻtish yoʻnalishi (View Transitions: next / prev)
//  · Ichki havolalarga "nav" tovushi (sfx.js), ←/→ bilan oldingi/keyingi sahifa
//  · dastur tablari (mobil panel) va "yoʻl"dagi kompas strelkasi
// ═══════════════════════════════════════════════════════════════
// ── Tungi rejim (2026-10-30): tanlov localStorage "kompas_theme" (light|dark), boʻlmasa tizim sozlamasi.
//    <head> da sinxron ishlaydi, shuning uchun sahifa yorugʻ holda "miltillamaydi". Ranglar: css/kompas-ui.css oxiridagi blok.
(function () {
  var KEY = "kompas_theme", root = document.documentElement;
  var mq = window.matchMedia ? window.matchMedia("(prefers-color-scheme: dark)") : null;
  function saved() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function apply() { var t = saved() || (mq && mq.matches ? "dark" : "light"); root.setAttribute("data-theme", t); return t; }
  apply();
  if (mq && mq.addEventListener) mq.addEventListener("change", function () { if (!saved()) { apply(); sync(); } });
  var SUN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.5"/><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22M4.9 4.9l1.8 1.8M17.3 17.3l1.8 1.8M4.9 19.1l1.8-1.8M17.3 6.7l1.8-1.8"/></svg>';
  var MOON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5z"/></svg>';
  var btns = [];
  function sync() {
    var dark = root.getAttribute("data-theme") === "dark";
    btns.forEach(function (b) { b.innerHTML = dark ? SUN : MOON; b.setAttribute("aria-label", dark ? "Yorugʻ rejim" : "Tungi rejim"); b.setAttribute("title", dark ? "Yorugʻ rejim" : "Tungi rejim"); b.setAttribute("aria-pressed", dark ? "true" : "false"); });
  }
  function make() {
    var b = document.createElement("button");
    b.type = "button"; b.className = "kl-theme"; b.setAttribute("data-snd", "tab");
    b.addEventListener("click", function () {
      var t = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      try { localStorage.setItem(KEY, t); } catch (e) {}
      root.setAttribute("data-theme", t); sync();
    });
    btns.push(b); return b;
  }
  function mount() {
    var slot = document.querySelector("[data-sfx-slot]");
    if (slot && slot.parentNode) { slot.parentNode.insertBefore(make(), slot); }
    else {
      var xp = document.querySelector("header.top .xp");
      var nav = document.querySelector(".at-nav .wrap, .atop .wrap");
      if (xp) xp.parentNode.insertBefore(make(), xp);
      else if (nav) nav.appendChild(make());
      else { var b = make(); b.classList.add("kl-theme-float"); document.body.appendChild(b); }
    }
    sync();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", mount); else mount();
})();

// ── Koʻrinish sozlamalari (2026-11-17): admin → Dizayn. Mavzu (fasl/bayram, avtomatik yoki qoʻlda),
//    shrift juftligi, matn/sarlavha oʻlchami, bloklar orasidagi masofa, burchaklar, kontent kengligi,
//    talaba uchun A− A A+ tugmasi. Sozlama: Supabase site_settings (key='ui'), kesh localStorage "kompas_ui_v1" (5 daqiqa).
//    Ishlash usuli: sozlama standart boʻlmasa, sahifadagi CSS qoidalari bir marta oʻzgaruvchiga oʻtkaziladi
//    (font-size → calc(…*var(--kt-fs)), "Cambria…" → var(--kt-head,…) va h.k.), keyin oʻzgarish faqat :root qiymati.
//    Standart holatda hech narsa qayta yozilmaydi. Mavzu ranglari faqat yorugʻ rejimda (tungi rejim oʻzgarmaydi).
//    Oʻchirish: ?look=0. Admin koʻrinishi (iframe): sessionStorage "kompas_ui_prev".
(function () {
  var root = document.documentElement;
  var URL_ = "https://usxpkmbjrdllnitlzdpq.supabase.co/rest/v1/site_settings?select=value,updated_at&key=eq.ui";
  var AK = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVzeHBrbWJqcmRsbG5pdGx6ZHBxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI1MzUxNzcsImV4cCI6MjA4ODExMTE3N30.wecMraU0qbnT89IKaoyu0-gDBfo0kUBF1t6ajMJNvT8";
  var CK = "kompas_ui_v1", FSK = "kompas_fs", PK = "kompas_ui_prev", TTL = 5 * 60 * 1000;
  var OFF = /[?&]look=0/.test(location.search);
  var FRAMED = false; try { FRAMED = window.top !== window; } catch (e) { FRAMED = true; }

  // Shrift juftliklari. Har roʻyxatda ikkinchi oʻrinda zaxira (ʻ ʼ Ö Ğ Ş Ç uchun, CLAUDE.md shrift qoidasi).
  var SERIF2 = '"Playfair Display",serif', SANS2 = '"IBM Plex Sans",sans-serif';
  var FONTS = {
    kompas:   { n: "Kompas (standart)", d: "Cambria / Caladea + Outfit", h: null, b: null, q: "" },
    dmserif:  { n: "DM Serif + Outfit", d: "Yirik, nafis sarlavha", h: '"DM Serif Display",' + SERIF2, b: null, q: "family=DM+Serif+Display:ital@0;1" },
    fraunces: { n: "Fraunces + Inter", d: "Zamonaviy kitob uslubi", h: '"Fraunces",' + SERIF2, b: '"Inter",' + SANS2, q: "family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Inter:wght@400;500;600;700;800" },
    lora:     { n: "Lora + Source Sans 3", d: "Yumshoq, oʻqishga qulay", h: '"Lora",' + SERIF2, b: '"Source Sans 3",' + SANS2, q: "family=Lora:wght@400;600;700&family=Source+Sans+3:wght@400;500;600;700;800" },
    noto:     { n: "Noto Serif + Noto Sans", d: "Belgilar qamrovi eng keng", h: '"Noto Serif",' + SERIF2, b: '"Noto Sans",' + SANS2, q: "family=Noto+Serif:wght@400;600;700&family=Noto+Sans:wght@400;500;600;700;800" },
    literata: { n: "Literata + Nunito Sans", d: "Uzun matn uchun", h: '"Literata",' + SERIF2, b: '"Nunito Sans",' + SANS2, q: "family=Literata:opsz,wght@7..72,400;7..72,600;7..72,700&family=Nunito+Sans:wght@400;600;700;800" },
    pt:       { n: "PT Serif + PT Sans", d: "Klassik, sodda", h: '"PT Serif",' + SERIF2, b: '"PT Sans",' + SANS2, q: "family=PT+Serif:wght@400;700&family=PT+Sans:wght@400;700" },
    manrope:  { n: "Manrope (faqat sans)", d: "Toza, interfeys uslubi", h: '"Manrope",' + SANS2, b: '"Manrope",' + SANS2, q: "family=Manrope:wght@400;500;600;700;800" }
  };
  // Mavzular: faqat urgʻu va fon tuslari. Asosiy yashil (--accent) va logotip oʻzgarmaydi.
  // Kontrast: oq matn urgʻu rangida ≥ 4.5:1 (tools/site/test_look.cjs tekshiradi).
  function P(a2, a2h, a2l, bg, sf, bd, g, gl, al) { return { a2: a2, a2h: a2h, a2l: a2l, bg: bg, sf: sf, bd: bd, g: g, gl: gl, al: al }; }
  var THEMES = {
    standart:    { n: "Standart", e: "🧭", k: "asosiy", c: null },
    qish:        { n: "Qish", e: "❄️", k: "fasl", c: P("#3f6889", "#31536e", "#e6eef4", "#f1f4f6", "#ffffff", "#dbe3e9", "#7f6a2c", "#f1ecdc", "#e5eef0") },
    bahor:       { n: "Bahor", e: "🌸", k: "fasl", c: P("#b24f6b", "#933f57", "#f8e9ee", "#f3f7f1", "#ffffff", "#dce8dc", "#7d6812", "#f5f0d6", "#e3f0e4") },
    yoz:         { n: "Yoz", e: "☀️", k: "fasl", c: P("#a35f17", "#864e13", "#f9eedc", "#f7f5ed", "#fffefa", "#e7e1cd", "#8c690b", "#f8efd2", "#e6efe6") },
    kuz:         { n: "Kuz", e: "🍂", k: "fasl", c: P("#ad5426", "#90451f", "#f8ebe2", "#f6f2ea", "#fffdf8", "#e6dccb", "#8a6310", "#f7edd5", "#e9efe8") },
    navruz:      { n: "Navroʻz", e: "🌷", k: "bayram", c: P("#5c7b28", "#4a6420", "#edf3e0", "#f3f6ec", "#fffffb", "#dfe6cf", "#8f7111", "#f6efd0", "#e4efe2") },
    ramazon:     { n: "Ramazon", e: "🌙", k: "bayram", c: P("#2f6b6b", "#255656", "#e2efee", "#f2f4f2", "#ffffff", "#dce3df", "#8a6e26", "#f3ecd8", "#e4eeeb") },
    hayit:       { n: "Hayit", e: "✨", k: "bayram", c: P("#86611a", "#6d4f15", "#f6eed9", "#f6f4ee", "#fffefa", "#e5dfcd", "#86611a", "#f6eed9", "#e7efe9") },
    mustaqillik: { n: "Mustaqillik kuni", e: "🇺🇿", k: "bayram", c: P("#1f6f9e", "#185a81", "#e3eff6", "#f2f6f7", "#ffffff", "#dae4e8", "#8a6a10", "#f5eed6", "#e4f0ec") },
    yangiyil:    { n: "Yangi yil", e: "🎄", k: "bayram", c: P("#a8443a", "#8a372f", "#f7e6e3", "#f4f4f0", "#ffffff", "#e0e2da", "#8c6a0e", "#f7efd4", "#e4eee8") }
  };
  // Bayramlar: from/to "OO-KK" (har yil) yoki "YYYY-OO-KK" (bir martalik; Ramazon va Hayitlar sanasi har yil oʻzgaradi).
  var HOLS = [
    { id: "ramazon", t: "ramazon", n: "Ramazon oyi" },
    { id: "ramazonhayit", t: "hayit", n: "Ramazon hayiti" },
    { id: "qurbonhayit", t: "hayit", n: "Qurbon hayiti" },
    { id: "navruz", t: "navruz", n: "Navroʻz" },
    { id: "mustaqillik", t: "mustaqillik", n: "Mustaqillik kuni" },
    { id: "yangiyil", t: "yangiyil", n: "Yangi yil" }
  ];
  var DEF = {
    v: 1, mode: "manual", theme: "standart", seasons: true,
    hol: {
      ramazon: { on: true, from: "", to: "" }, ramazonhayit: { on: true, from: "", to: "" }, qurbonhayit: { on: true, from: "", to: "" },
      navruz: { on: true, from: "03-15", to: "03-25" }, mustaqillik: { on: true, from: "08-28", to: "09-03" }, yangiyil: { on: true, from: "12-25", to: "01-03" }
    },
    font: "kompas", fs: 1, hs: 1, sp: 1, r: 1, w: 1, reader: true
  };
  var FS_STEPS = [0.9, 1, 1.12, 1.25];
  var LIM = { fs: [0.85, 1.2], hs: [0.85, 1.25], sp: [0.75, 1.3], r: [0, 1.8], w: [0.85, 1.2] };

  function clone(o) { return JSON.parse(JSON.stringify(o)); }
  function merge(s) {
    var o = clone(DEF);
    if (!s || typeof s !== "object") return o;
    ["mode", "theme", "font"].forEach(function (k) { if (typeof s[k] === "string") o[k] = s[k]; });
    ["seasons", "reader"].forEach(function (k) { if (typeof s[k] === "boolean") o[k] = s[k]; });
    Object.keys(LIM).forEach(function (k) { var v = +s[k]; if (isFinite(v) && v > 0 || (k === "r" && v === 0)) o[k] = Math.min(LIM[k][1], Math.max(LIM[k][0], v)); });
    if (s.hol && typeof s.hol === "object") HOLS.forEach(function (h) {
      var x = s.hol[h.id]; if (!x) return;
      o.hol[h.id] = { on: x.on !== false, from: String(x.from || ""), to: String(x.to || "") };
    });
    if (!THEMES[o.theme]) o.theme = "standart";
    if (!FONTS[o.font]) o.font = "kompas";
    if (typeof s._date === "string") o._date = s._date;
    return o;
  }
  // Toshkent vaqti (UTC+5) boʻyicha bugun
  function today(s) {
    if (s && /^\d{4}-\d{2}-\d{2}$/.test(s._date || "")) return s._date;
    return new Date(Date.now() + 5 * 3600e3).toISOString().slice(0, 10);
  }
  function inRange(d, from, to) {
    var md = /^\d{2}-\d{2}$/, full = /^\d{4}-\d{2}-\d{2}$/;
    if (md.test(from) && md.test(to)) { var x = d.slice(5); return from <= to ? (x >= from && x <= to) : (x >= from || x <= to); }
    if (full.test(from) && full.test(to)) return d >= from && d <= to;
    if (full.test(from) && !to) return d === from;
    return false;
  }
  function season(d) { var m = +d.slice(5, 7); return m === 12 || m <= 2 ? "qish" : m <= 5 ? "bahor" : m <= 8 ? "yoz" : "kuz"; }
  function resolve(s) {
    s = merge(s);
    if (s.mode !== "auto") return { id: s.theme, why: "qoʻlda" };
    var d = today(s);
    for (var i = 0; i < HOLS.length; i++) {
      var h = HOLS[i], x = s.hol[h.id];
      if (x && x.on && inRange(d, x.from, x.to)) return { id: h.t, why: h.n };
    }
    if (s.seasons) { var f = season(d); return { id: f, why: "fasl" }; }
    return { id: "standart", why: "avtomatik" };
  }

  // ── CSS qoidalarini oʻzgaruvchiga oʻtkazish (bir marta) ──
  var PX = /^-?\d*\.?\d+px$/;
  var HSEL = /(^|[\s,>+~(])h[1-3](?![\w-])/i;
  function tok(v, prop, max) {
    if (!v || /var\(|calc\(|env\(/.test(v)) return null;
    var ch = false;
    var out = v.split(/\s+/).map(function (t) {
      if (PX.test(t) && parseFloat(t) !== 0 && (!max || Math.abs(parseFloat(t)) <= max)) { ch = true; return "calc(" + t + " * var(" + prop + ",1))"; }
      return t;
    }).join(" ");
    return ch ? out : null;
  }
  var SP = ["padding-top", "padding-right", "padding-bottom", "padding-left", "row-gap", "column-gap"];
  var MG = ["margin-left", "margin-right"];
  var RD = ["border-top-left-radius", "border-top-right-radius", "border-bottom-right-radius", "border-bottom-left-radius"];
  function fixStyle(st, sel) {
    var pr = function (p) { return st.getPropertyPriority(p); };
    var ff = st.getPropertyValue("font-family"), head = HSEL.test(sel || "");
    if (ff) {
      if (ff.indexOf("--kt-head") >= 0) head = true;
      else if (ff.indexOf("var(") < 0) {
        if (/cambria|caladea/i.test(ff)) { st.setProperty("font-family", "var(--kt-head," + ff + ")", pr("font-family")); head = true; }
        else if (/outfit/i.test(ff)) st.setProperty("font-family", "var(--kt-body," + ff + ")", pr("font-family"));
      }
    }
    var fz = st.getPropertyValue("font-size");
    if (fz && fz.indexOf("var(") < 0 && /px|rem|vw|vh|vmin|vmax|clamp|min\(|max\(/.test(fz) && !/(^|[^r])em\b|%/.test(fz)) {
      st.setProperty("font-size", "calc(" + fz + " * var(--kt-fs,1)" + (head ? " * var(--kt-hs,1)" : "") + ")", pr("font-size"));
      if (!head && sel) FZ.push({ st: st, sel: sel }); // keyin: sahifadagi h1–h3 ga tegishli boʻlsa sarlavha deb belgilanadi
    }
    SP.forEach(function (p) { var n = tok(st.getPropertyValue(p), "--kt-sp"); if (n) st.setProperty(p, n, pr(p)); });
    // Manfiy chekka (margin) koʻpincha ota blok padding'ini "yeydi" (toʻliq enli lenta): u ham birga oʻzgaradi
    MG.forEach(function (p) { var v = st.getPropertyValue(p); if (/^-\d*\.?\d+px$/.test(v || "")) st.setProperty(p, "calc(" + v + " * var(--kt-sp,1))", pr(p)); });
    RD.forEach(function (p) { var n = tok(st.getPropertyValue(p), "--kt-r", 40); if (n) st.setProperty(p, n, pr(p)); });
    var mw = st.getPropertyValue("max-width");
    if (PX.test(mw || "") && parseFloat(mw) >= 900) st.setProperty("max-width", "calc(" + mw + " * var(--kt-w,1))", pr("max-width"));
  }
  var FZ = [];
  function headPass() {
    if (!document.body || !FZ.length) return;
    var hs = document.querySelectorAll("h1,h2,h3"); if (!hs.length) return;
    var rest = [];
    FZ.forEach(function (x) {
      var hit = false;
      try { for (var i = 0; i < hs.length && !hit; i++) hit = hs[i].matches(x.sel); } catch (e) {}
      if (hit) { var v = x.st.getPropertyValue("font-size"); if (v.indexOf("--kt-hs") < 0) x.st.setProperty("font-size", v.replace(/\)\s*$/, " * var(--kt-hs,1))"), x.st.getPropertyPriority("font-size")); }
      else rest.push(x);
    });
    FZ = rest;
  }
  function walk(rules) {
    for (var i = 0; i < rules.length; i++) {
      var r = rules[i];
      if (r.style && r.selectorText) { if (!/^\s*:root\s*$/.test(r.selectorText)) fixStyle(r.style, r.selectorText); }
      else if (r.cssRules) walk(r.cssRules); // @media, @supports, @layer (@keyframes ichida selectorText yoʻq)
    }
  }
  var REW = false, seen = typeof WeakSet === "function" ? new WeakSet() : null;
  function rewriteAll() {
    if (!seen) return;
    var ss = document.styleSheets;
    for (var i = 0; i < ss.length; i++) {
      var sh = ss[i]; if (seen.has(sh)) continue;
      var node = sh.ownerNode; if (node && node.id === "klook-css") { seen.add(sh); continue; }
      var rules = null; try { rules = sh.cssRules; } catch (e) { seen.add(sh); continue; } // boshqa domen (Google Fonts)
      if (!rules) continue;
      seen.add(sh); walk(rules);
    }
    if (document.body) {
      var els = document.querySelectorAll("[style]");
      for (var j = 0; j < els.length; j++) if (!els[j].__kt) { els[j].__kt = 1; fixStyle(els[j].style, els[j].tagName); }
      headPass();
    }
  }
  var mo = null;
  function startRewrite() {
    if (REW) { rewriteAll(); return; }
    REW = true; root.setAttribute("data-klook", "1");
    rewriteAll();
    var t = 0, again = function () { clearTimeout(t); t = setTimeout(rewriteAll, 30); };
    document.addEventListener("DOMContentLoaded", rewriteAll);
    window.addEventListener("load", rewriteAll);
    document.addEventListener("load", function (e) { if (e.target && e.target.tagName === "LINK") again(); }, true);
    if (window.MutationObserver) { mo = new MutationObserver(function (ms) {
      for (var i = 0; i < ms.length; i++) for (var k = 0; k < ms[i].addedNodes.length; k++) {
        var n = ms[i].addedNodes[k]; if (n.nodeName === "STYLE" || n.nodeName === "LINK") { again(); return; }
      }
    }); mo.observe(root, { childList: true, subtree: true }); }
  }

  // ── Qoʻllash ──
  var cur = null, userFs = 1, fsBtns = [];
  try { var u = parseFloat(localStorage.getItem(FSK)); if (FS_STEPS.indexOf(u) >= 0) userFs = u; } catch (e) {}
  function styleEl(id) {
    var el = document.getElementById(id);
    if (!el) { el = document.createElement("style"); el.id = id; (document.head || root).appendChild(el); }
    return el;
  }
  function paletteCss(id) {
    var t = THEMES[id]; if (!t || !t.c) return "";
    var c = t.c;
    return "html:not([data-theme=\"dark\"]){--accent2:" + c.a2 + ";--accent2-h:" + c.a2h + ";--accent2-lit:" + c.a2l +
      ";--bg:" + c.bg + ";--surface:" + c.sf + ";--border:" + c.bd + ";--gold:" + c.g + ";--gold-lit:" + c.gl + ";--accent-lit:" + c.al +
      ";--cream:" + c.bg + ";--kl-clay:" + c.a2 + ";--kl-cream:" + c.bg + ";--kl-line:" + c.bd + "}";
  }
  function apply(s) {
    s = merge(s); cur = s;
    var th = resolve(s), f = FONTS[s.font];
    root.setAttribute("data-ktheme", th.id);
    styleEl("klook-vars").textContent = paletteCss(th.id);
    var link = document.getElementById("klook-font");
    if (f.q) {
      var href = "https://fonts.googleapis.com/css2?" + f.q + "&display=swap";
      if (!link) { link = document.createElement("link"); link.rel = "stylesheet"; link.id = "klook-font"; (document.head || root).appendChild(link); }
      if (link.getAttribute("href") !== href) link.setAttribute("href", href);
    } else if (link) link.parentNode.removeChild(link);
    var fs = s.fs * (s.reader ? userFs : 1);
    var st = root.style;
    if (f.h) st.setProperty("--kt-head", f.h); else st.removeProperty("--kt-head");
    if (f.b) st.setProperty("--kt-body", f.b); else st.removeProperty("--kt-body");
    st.setProperty("--kt-fs", String(+fs.toFixed(3)));
    st.setProperty("--kt-fs0", String(+fs.toFixed(3))); // blok shrifti (site_edits style) shunga koʻpaytiriladi
    st.setProperty("--kt-hs", String(s.hs)); st.setProperty("--kt-sp", String(s.sp));
    st.setProperty("--kt-r", String(s.r)); st.setProperty("--kt-w", String(s.w));
    if (f.q || fs !== 1 || s.hs !== 1 || s.sp !== 1 || s.r !== 1 || s.w !== 1) startRewrite();
    syncFs();
    return th;
  }

  var stored = null;
  try { var c0 = JSON.parse(localStorage.getItem(CK) || "null"); if (c0 && c0.d) stored = c0; } catch (e) {}
  var prev = null;
  if (FRAMED) { try { prev = JSON.parse(sessionStorage.getItem(PK) || "null"); } catch (e) {} }
  if (!OFF) apply(prev || (stored && stored.d) || null);

  function fresh() {
    if (OFF || prev || !window.fetch) return;
    if (stored && Date.now() - stored.t < TTL) return;
    fetch(URL_, { headers: { apikey: AK, Authorization: "Bearer " + AK } })
      .then(function (r) { return r.ok ? r.json() : (r.status >= 400 && r.status < 500 ? [] : null); }) // 4xx (masalan, jadval yoʻq) = standart, keshlanadi
      .then(function (d) {
        if (!Array.isArray(d)) return;
        var v = d[0] ? d[0].value : null;
        try { localStorage.setItem(CK, JSON.stringify({ t: Date.now(), d: v })); } catch (e) {}
        if (JSON.stringify(merge(v)) !== JSON.stringify(cur)) apply(v);
      }).catch(function () {});
  }
  fresh();

  // ── Talaba uchun "Aa" (A− A A+) tugmasi: faqat matn oʻlchami, tanlov qurilmada ──
  function label() { return Math.round(userFs * 100) + "%"; }
  function syncFs() {
    fsBtns.forEach(function (w) {
      w.style.display = cur && cur.reader ? "" : "none";
      var v = w.querySelector(".kl-fs-v"); if (v) v.textContent = label();
      var i = FS_STEPS.indexOf(userFs);
      var m = w.querySelector("[data-fs=\"-1\"]"), p = w.querySelector("[data-fs=\"1\"]");
      if (m) m.disabled = i <= 0; if (p) p.disabled = i >= FS_STEPS.length - 1;
    });
  }
  function setFs(v) {
    userFs = v;
    try { if (v === 1) localStorage.removeItem(FSK); else localStorage.setItem(FSK, String(v)); } catch (e) {}
    apply(cur);
  }
  var CSS = ".kl-fs{position:relative;display:inline-flex;flex:none}" +
    ".kl-fs>button.kl-fs-b{display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:10px;border:1px solid var(--border,#e0e8e2);background:var(--surface,#fff);color:var(--text,#1a2e26);cursor:pointer;font:700 14px/1 \"Outfit\",\"IBM Plex Sans\",sans-serif;padding:0;letter-spacing:-.02em}" +
    ".kl-fs>button.kl-fs-b:hover{border-color:var(--accent,#2d4a3e)}" +
    ".kl-fs-p{position:absolute;right:0;top:calc(100% + 8px);z-index:400;display:none;align-items:center;gap:4px;padding:6px;border-radius:12px;background:var(--surface,#fff);border:1px solid var(--border,#e0e8e2);box-shadow:0 10px 28px rgba(26,46,38,.16);white-space:nowrap}" +
    ".kl-fs.open .kl-fs-p{display:flex}" +
    ".kl-fs-p button{min-width:38px;height:34px;border-radius:9px;border:1px solid var(--border,#e0e8e2);background:transparent;color:var(--text,#1a2e26);cursor:pointer;font:700 15px/1 \"Outfit\",\"IBM Plex Sans\",sans-serif}" +
    ".kl-fs-p button:hover:not(:disabled){border-color:var(--accent,#2d4a3e);background:var(--accent-lit,#e8f0ec)}" +
    ".kl-fs-p button:disabled{opacity:.35;cursor:default}" +
    ".kl-fs-v{min-width:48px;text-align:center;font:600 13px/1 \"Outfit\",\"IBM Plex Sans\",sans-serif;color:var(--muted,#5f7169)}" +
    ".kl-fs-float{position:fixed;left:58px;bottom:14px;z-index:300}" +
    ".kl-fs-float.kl-fs-solo{left:14px}.kl-fs-float>button.kl-fs-b{box-shadow:0 4px 14px rgba(0,0,0,.18)}" +
    ".kl-fs-float .kl-fs-p{top:auto;bottom:calc(100% + 8px);left:0;right:auto}" +
    "header.top .kl-fs{margin-right:8px}" +
    "html[data-theme=\"dark\"] .kl-fs-p{box-shadow:0 10px 28px rgba(0,0,0,.45)}" +
    "html[data-klook] body{overflow-wrap:break-word}" + // kattalashgan matn tor kartochkadan chiqib ketmasin
    "@media print{.kl-fs{display:none!important}}";
  function makeFs() {
    var w = document.createElement("div"); w.className = "kl-fs";
    w.innerHTML = '<button type="button" class="kl-fs-b" aria-haspopup="true" aria-expanded="false" title="Matn oʻlchami" aria-label="Matn oʻlchami" data-snd="tab">Aa</button>' +
      '<div class="kl-fs-p" role="group" aria-label="Matn oʻlchami"><button type="button" data-fs="-1" aria-label="Kichikroq">A−</button>' +
      '<button type="button" data-fs="0" class="kl-fs-v" title="Asl oʻlcham" aria-label="Asl oʻlcham"></button>' +
      '<button type="button" data-fs="1" aria-label="Kattaroq">A+</button></div>';
    var b = w.firstChild;
    b.addEventListener("click", function (e) { e.stopPropagation(); var o = !w.classList.contains("open"); w.classList.toggle("open", o); b.setAttribute("aria-expanded", o ? "true" : "false"); });
    w.querySelector(".kl-fs-p").addEventListener("click", function (e) {
      e.stopPropagation();
      var t = e.target.closest ? e.target.closest("[data-fs]") : null; if (!t) return;
      var d = +t.getAttribute("data-fs"), i = FS_STEPS.indexOf(userFs);
      setFs(d === 0 ? 1 : FS_STEPS[Math.min(FS_STEPS.length - 1, Math.max(0, i + d))]);
    });
    document.addEventListener("click", function () { w.classList.remove("open"); b.setAttribute("aria-expanded", "false"); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") { w.classList.remove("open"); b.setAttribute("aria-expanded", "false"); } });
    fsBtns.push(w); return w;
  }
  function mountFs() {
    styleEl("klook-css").textContent = CSS;
    var th = document.querySelector(".kl-theme");
    var w = makeFs();
    if (th && th.parentNode) {
      if (th.classList.contains("kl-theme-float")) { w.classList.add("kl-fs-float"); document.body.appendChild(w); }
      else th.parentNode.insertBefore(w, th.nextSibling);
    } else { w.classList.add("kl-fs-float"); document.body.appendChild(w); }
    syncFs();
    // Tor ekranda sarlavha qatori sigʻmasa (menyu yoki modul sarlavhasi), tugma pastki chap burchakka oʻtadi
    function fit() {
      if (w.classList.contains("kl-fs-float") || w.style.display === "none") return;
      var row = w.parentNode, vw = window.innerWidth, over = root.scrollWidth > vw + 1;
      if (!over && row) for (var i = 0; i < row.children.length; i++) { var rc = row.children[i].getBoundingClientRect(); if (rc.width && rc.right > vw + 1) { over = true; break; } }
      if (over) {
        w.classList.add("kl-fs-float");
        if (!document.querySelector(".kl-theme-float")) w.classList.add("kl-fs-solo");
        document.body.appendChild(w);
      }
    }
    fit(); window.addEventListener("load", fit); setTimeout(fit, 300);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", mountFs); else mountFs();

  // Admin koʻrinishi va testlar uchun
  window.KLook = {
    THEMES: THEMES, FONTS: FONTS, HOLS: HOLS, DEF: DEF, LIM: LIM, FS_STEPS: FS_STEPS,
    merge: merge, resolve: resolve, today: today, season: season, inRange: inRange,
    apply: function (s) { return apply(s); }, current: function () { return cur; },
    need: function () { startRewrite(); } // blok shrifti uchun CSS oʻlchamlarini var(--kt-fs) ga oʻtkazish
  };
})();

(function () {
  var DIR = "kl_dir";
  // Yangi sahifa ochilganda: oldingi sahifada bosilgan havola yoʻnalishini oʻtishga qoʻshamiz
  window.addEventListener("pagereveal", function (e) {
    var d = null;
    try { d = sessionStorage.getItem(DIR); sessionStorage.removeItem(DIR); } catch (x) {}
    if (e.viewTransition && d && e.viewTransition.types) { try { e.viewTransition.types.add(d); } catch (x) {} }
  });
  function setDir(d) { try { if (d) sessionStorage.setItem(DIR, d); else sessionStorage.removeItem(DIR); } catch (x) {} }

  function internal(a) {
    if (!a || !a.getAttribute) return false;
    var h = a.getAttribute("href");
    if (!h || h.charAt(0) === "#" || a.target === "_blank" || a.hasAttribute("download")) return false;
    if (/^(mailto|tel|javascript):/i.test(h)) return false;
    try { var u = new URL(h, location.href); return u.origin === location.origin && u.pathname !== location.pathname; } catch (x) { return false; }
  }

  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[href]");
    if (!a || e.defaultPrevented || e.button || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    if (internal(a)) setDir(a.getAttribute("data-dir") || a.getAttribute("rel") === "next" && "next" || a.getAttribute("rel") === "prev" && "prev" || "");
  }, true);

  function ready(fn) { if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", fn); else fn(); }

  ready(function () {
    // Ichki havolalar: tovush (sfx.js [data-snd] ni oʻzi chaladi)
    document.querySelectorAll("a[href]").forEach(function (a) { if (!a.hasAttribute("data-snd") && internal(a)) a.setAttribute("data-snd", "nav"); });

    // Mobil tab paneli
    var bar = document.querySelector(".kl-tabbar");
    if (bar) {
      document.body.classList.add("kl-has-tabs");
      var cur = bar.querySelector('[aria-current="page"]');
      if (cur && bar.firstElementChild) { var t = bar.firstElementChild; t.scrollLeft = cur.offsetLeft - (t.clientWidth - cur.clientWidth) / 2; }
    }

    // ←/→: oldingi va keyingi sahifa (dars va modul sahifalarida)
    document.addEventListener("keydown", function (e) {
      if (e.metaKey || e.ctrlKey || e.altKey || e.shiftKey) return;
      var t = e.target; if (t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName))) return;
      var rel = e.key === "ArrowRight" ? "next" : e.key === "ArrowLeft" ? "prev" : "";
      if (!rel) return;
      var a = document.querySelector('a[rel="' + rel + '"][data-kkey]');
      if (a) { setDir(rel); if (window.KSfx) KSfx.play("nav"); location.href = a.href; }
    });

    needles();
    window.addEventListener("resize", function () { clearTimeout(needles.t); needles.t = setTimeout(needles, 150); });
    phaseTabs();
  });

  // Dastur sahifasi (2026-10-30): faza tugmasi bosilganda faqat shu faza modullari koʻrinadi.
  // Manzil: #faza-N (havolani ulashish mumkin). Belgilash: tools/landing/split.py → phase_tabs().
  function phaseTabs() {
    var box = document.querySelector(".kl-ph"); if (!box) return;
    var body = document.getElementById("kl-ph-mods"); if (!body) return;
    var btns = box.querySelectorAll("button[data-ph]");
    document.documentElement.classList.add("kl-ph-on");
    function show(k, scroll) {
      btns.forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-ph") === k ? "true" : "false"); });
      body.querySelectorAll("[data-ph]").forEach(function (el) {
        var on = el.getAttribute("data-ph") === k;
        el.hidden = !on;
        if (on && el.tagName === "DETAILS") { el.classList.remove("kl-ph-in"); void el.offsetWidth; el.classList.add("kl-ph-in"); }
      });
      if (scroll) body.scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth", block: "start" });
    }
    btns.forEach(function (b) {
      b.addEventListener("click", function () {
        var k = b.getAttribute("data-ph");
        show(k, false);
        if (box.scrollWidth > box.clientWidth) box.scrollTo({ left: b.offsetLeft - (box.clientWidth - b.offsetWidth) / 2, behavior: "smooth" });
        if (window.KSfx) KSfx.play("pick");
        try { history.replaceState(null, "", "#faza-" + k); } catch (e) {}
      });
    });
    var m = /^#faza-(\d+)$/.exec(location.hash);
    show(m && box.querySelector('button[data-ph="' + m[1] + '"]') ? m[1] : "0", false);
  }

  // Kompas strelkasi joriy bekatda turadi
  var SVG = '<svg viewBox="0 0 44 44" aria-hidden="true"><circle cx="22" cy="22" r="20" fill="#fffefb" stroke="#c4622d" stroke-width="2.5"/><circle cx="22" cy="22" r="15.5" fill="none" stroke="#e2ded3" stroke-dasharray="1.5 3.2"/><g class="kn"><path d="M22 18.6 L37 22 L22 25.4 Z" fill="#c4622d"/><path d="M22 18.6 L7 22 L22 25.4 Z" fill="#2d4a3e"/><circle cx="22" cy="22" r="2.6" fill="#fffefb" stroke="#2d4a3e" stroke-width="1.4"/></g></svg>';
  function needles() {
    document.querySelectorAll(".kl-route[data-needle]").forEach(function (r) {
      var st = r.querySelector(".kl-st.is-here, .kl-st.is-current");
      var n = r.querySelector(".kl-route-needle");
      if (!st) { if (n) n.remove(); r.classList.remove("has-needle"); return; }
      var dot = st.querySelector(".kl-st-n"); if (!dot) return;
      if (!n) { n = document.createElement("span"); n.className = "kl-route-needle"; n.innerHTML = SVG; r.appendChild(n); }
      var rr = r.getBoundingClientRect(), dr = dot.getBoundingClientRect();
      n.style.top = (dr.top - rr.top + (dr.height - n.offsetHeight) / 2) + "px";
      n.style.left = (dr.left - rr.left + (dr.width - n.offsetWidth) / 2) + "px";
      r.classList.add("has-needle");
    });
  }
  window.KUI = { needles: needles, setDir: setDir };
})();

// ── Profil belgisi (2026-10-30): kirgan foydalanuvchiga nav'da "Kirish" oʻrniga profil.
//    Sessiya Supabase'ning localStorage kalitidan oʻqiladi (config.js boʻlmagan sahifada ham ishlaydi).
//    Obuna holati faqat koʻrinish uchun: kontentga kirishni server (fn_paid_page, RLS) tekshiradi.
//    Kesh: localStorage "kompas_me_v1" (uid, ism, rol, faol obunalar), 5 daqiqada yangilanadi.
(function () {
  var TOK = "sb-usxpkmbjrdllnitlzdpq-auth-token", ME = "kompas_me_v1", TTL = 300000;
  var LABS = { "bachelor-lab": "Bakalavr dasturi", "master-lab": "Magistratura dasturi", "phd-lab": "PhD dasturi", "gks-lab": "GKS dasturi", "usa-lab": "USA dasturi", "daad-lab": "DAAD dasturi", "tadbirkor-talaba": "Tadbirkor Talaba", "miggo": "Musofir dasturi" };
  function rd(k) { try { return JSON.parse(localStorage.getItem(k) || "null"); } catch (e) { return null; } }
  function user() { var s = rd(TOK); return s && s.user && s.user.id ? s.user : null; }
  function esc(t) { return String(t == null ? "" : t).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function names(u, me) {
    var md = u.user_metadata || {};
    var full = (me && me.name) || md.full_name || [md.first_name, md.last_name].filter(Boolean).join(" ") || "";
    var first = (me && me.first) || md.first_name || full.split(" ")[0] || (u.email || "").split("@")[0];
    var ini = (full || first || u.email || "?").split(/\s+/).filter(Boolean).slice(0, 2).map(function (w) { return w.charAt(0); }).join("").toUpperCase();
    return { full: full || first, first: first, ini: ini || "?" };
  }
  function dt(s) { var d = new Date(s); return isNaN(d) ? "" : ("0" + d.getDate()).slice(-2) + "." + ("0" + (d.getMonth() + 1)).slice(-2) + "." + d.getFullYear(); }

  var chip = null;
  function render(u, me) {
    var n = names(u, me), subs = (me && me.uid === u.id && me.subs) || [];
    var paid = subs.length > 0;
    var st = paid
      ? subs.map(function (s) { return "<li><b>" + esc(LABS[s.slug] || s.title || s.slug) + "</b>" + (s.exp ? " · " + dt(s.exp) + " gacha" : "") + "</li>"; }).join("")
      : "<li>Bepul hisob: M0 darslari ochiq</li>";
    if (!chip) {
      chip = document.createElement("div");
      chip.className = "kl-me";
      chip.innerHTML = '<button type="button" class="kl-me-b" aria-haspopup="true" aria-expanded="false" data-snd="tab"></button><div class="kl-me-m" role="menu" hidden></div>';
      var b = chip.firstChild, m = chip.lastChild;
      b.addEventListener("click", function (e) { e.stopPropagation(); var o = m.hidden; m.hidden = !o; b.setAttribute("aria-expanded", o ? "true" : "false"); });
      document.addEventListener("click", function (e) { if (!chip.contains(e.target)) { m.hidden = true; b.setAttribute("aria-expanded", "false"); } });
      document.addEventListener("keydown", function (e) { if (e.key === "Escape" && !m.hidden) { m.hidden = true; b.setAttribute("aria-expanded", "false"); b.focus(); } });
    }
    chip.classList.toggle("is-paid", paid);
    chip.firstChild.setAttribute("aria-label", "Profil: " + n.full);
    chip.firstChild.innerHTML = '<span class="kl-me-a" aria-hidden="true">' + esc(n.ini) + '</span><span class="kl-me-n">' + esc(n.first) + "</span>";
    chip.lastChild.innerHTML =
      '<div class="kl-me-h"><span class="kl-me-a" aria-hidden="true">' + esc(n.ini) + '</span><div><b>' + esc(n.full) + '</b><small translate="no">' + esc(u.email || "") + "</small></div></div>" +
      '<div class="kl-me-s"><span class="kl-me-tag">' + (paid ? "Obunachi" : "Roʻyxatdan oʻtgan") + "</span><ul>" + st + "</ul></div>" +
      '<a role="menuitem" href="profil.html">👤 Profil</a><a role="menuitem" href="dashboard.html">🏠 Kabinet</a>' +
      (me && me.uid === u.id && me.admin ? '<a role="menuitem" href="admin.html">🛠 Admin panel</a>' : "") +
      '<a role="menuitem" href="profil.html?chiqish=1" class="kl-me-out">🚪 Chiqish</a>';
    return chip;
  }
  function mount(c) {
    // Kirgan foydalanuvchiga "Bepul boshlash" (register.html) kerak emas: kabinetga yoʻnaltiramiz
    var st = document.querySelectorAll("[data-kl-start]");
    for (var i = 0; i < st.length; i++) { st[i].href = "dashboard.html"; st[i].textContent = "Kabinet"; }
    if (c.parentNode) return;
    var nav = document.querySelector("nav.nav .wrap");
    var login = nav && nav.querySelector('a[href="login.html"]');
    if (login) { login.parentNode.replaceChild(c, login); return; }
    var slot = nav && nav.querySelector("[data-sfx-slot]");
    if (slot) { slot.parentNode.insertBefore(c, slot.nextSibling); return; }
    if (nav) { nav.appendChild(c); return; }
    var xp = document.querySelector("header.top .xp");
    if (xp) { c.classList.add("kl-me-sm"); xp.appendChild(c); }
  }
  function footer() {
    document.querySelectorAll('footer a[href="login.html"]').forEach(function (a) { a.href = "profil.html"; a.textContent = "Profil"; });
  }
  function refresh(u) {
    var sb = window.supabase;
    if (!sb || typeof sb.from !== "function") return;
    var me = rd(ME);
    if (me && me.uid === u.id && Date.now() - (me.at || 0) < TTL) return;
    Promise.all([
      sb.from("profiles").select("first_name,full_name,role").eq("id", u.id).maybeSingle(),
      sb.from("enrollments").select("payment_status,expires_at,frozen_at,courses(slug,title)").eq("user_id", u.id)
    ]).then(function (r) {
      if (r[0].error || r[1].error) return;
      var p = r[0].data || {}, now = Date.now();
      var subs = (r[1].data || []).filter(function (e) {
        return (e.payment_status === "paid" || e.payment_status === "partial") && !e.frozen_at && (!e.expires_at || new Date(e.expires_at).getTime() > now);
      }).map(function (e) { return { slug: e.courses && e.courses.slug, title: e.courses && e.courses.title, exp: e.expires_at }; });
      var next = { uid: u.id, at: now, first: p.first_name || "", name: p.full_name || "", admin: p.role === "admin", subs: subs };
      try { localStorage.setItem(ME, JSON.stringify(next)); } catch (e) {}
      render(u, next);
    }).catch(function () {});
  }
  // Eski sessiyani serverda tekshirish (2026-11-06): admin hisobni oʻchirgach, brauzerdagi JWT
  // ~1 soat amal qiladi va nav'da oʻchirilgan hisob koʻrinib qolardi. Auth serveri tokenni rad etsa,
  // mahalliy sessiya, kesh va M0 cookie tozalanadi. Tarmoq xatosida hech narsa oʻzgarmaydi.
  var VK = "kompas_vfy_v1", VTTL = 120000;
  function dead() {
    try { localStorage.removeItem(TOK); localStorage.removeItem(ME); sessionStorage.removeItem("kompas_fixes_v1"); } catch (e) {}
    try { fetch("/api/m0-session", { method: "DELETE", credentials: "same-origin" }).catch(function () {}); } catch (e) {}
    if (chip && chip.parentNode) { var a = document.createElement("a"); a.href = "login.html"; a.className = "btn"; a.textContent = "Kirish"; chip.parentNode.replaceChild(a, chip); }
  }
  function verify(u) {
    var s = rd(TOK), t = s && s.access_token;
    if (!t || !window.fetch) return;
    try { var v = JSON.parse(sessionStorage.getItem(VK) || "null"); if (v && v.u === u.id && Date.now() - v.at < VTTL) return; } catch (e) {}
    fetch("https://usxpkmbjrdllnitlzdpq.supabase.co/auth/v1/user", { headers: { apikey: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVzeHBrbWJqcmRsbG5pdGx6ZHBxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI1MzUxNzcsImV4cCI6MjA4ODExMTE3N30.wecMraU0qbnT89IKaoyu0-gDBfo0kUBF1t6ajMJNvT8", Authorization: "Bearer " + t }, cache: "no-store" })
      .then(function (r) {
        if (r.ok) { try { sessionStorage.setItem(VK, JSON.stringify({ u: u.id, at: Date.now() })); } catch (e) {} return; }
        // Faqat hisob bazada yoʻqligi aniq boʻlsa chiqariladi; muddati oʻtgan token (yangilanadi) tegilmaydi
        if (r.status === 401 || r.status === 403 || r.status === 404) {
          r.json().then(function (j) {
            var m = ((j && (j.error_code || j.code)) || "") + " " + ((j && (j.msg || j.message)) || "");
            if (/user_not_found|does not exist/i.test(m)) dead();
          }).catch(function () {});
        }
      }).catch(function () {});
  }
  function run() {
    var u = user();
    if (!u) { try { localStorage.removeItem(ME); } catch (e) {} return; }
    mount(render(u, rd(ME)));
    footer();
    refresh(u);
    verify(u);
  }
  window.KUI_ME = { reset: function () { try { localStorage.removeItem(ME); } catch (e) {} } };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run); else run();
})();

// ── Matn tuzatishlari (2026-10-31): admin paneldagi "Darslar → Matn tuzatishlari" (text_fixes, status=active).
//    Mayda xato saytda darhol tuzaladi; keyin tools/site/apply_fixes.py bilan manba faylga yoziladi (status=baked).
//    Pullik modullar (page "paid:…") bu yerda emas, serverda fn_paid_page() ichida qoʻllanadi.
//    Sahifa kaliti: fayl nomi ("master-lab-m0-2.html"), prefiks ("master-lab-m0*") yoki "*". Oʻchirish: ?fixes=0
(function () {
  if (/[?&]fixes=0/.test(location.search)) return;
  var file = location.pathname.split("/").pop() || "index.html";
  if (!/\.html?$/.test(file)) file += ".html";
  if (/^admin/.test(file)) return;
  var URL_ = "https://usxpkmbjrdllnitlzdpq.supabase.co/rest/v1/text_fixes?select=id,page,old_text,new_text&status=eq.active&page=not.like.paid:*&order=id";
  var KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVzeHBrbWJqcmRsbG5pdGx6ZHBxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI1MzUxNzcsImV4cCI6MjA4ODExMTE3N30.wecMraU0qbnT89IKaoyu0-gDBfo0kUBF1t6ajMJNvT8";
  var CK = "kompas_fixes_v1", TTL = 10 * 60 * 1000;
  function mine(list) {
    return list.filter(function (f) {
      var p = f.page;
      return p === "*" || p === file || (p.slice(-1) === "*" && file.indexOf(p.slice(0, -1)) === 0);
    });
  }
  function load() {
    try { var c = JSON.parse(sessionStorage.getItem(CK) || "null"); if (c && Date.now() - c.t < TTL) return Promise.resolve(c.d); } catch (e) {}
    if (!window.fetch) return Promise.resolve([]);
    return fetch(URL_, { headers: { apikey: KEY, Authorization: "Bearer " + KEY } })
      .then(function (r) { return r.ok ? r.json() : []; })
      .then(function (d) { d = Array.isArray(d) ? d : []; try { sessionStorage.setItem(CK, JSON.stringify({ t: Date.now(), d: d })); } catch (e) {} return d; })
      .catch(function () { return []; });
  }
  var SKIP = { SCRIPT: 1, STYLE: 1, TEXTAREA: 1, INPUT: 1, NOSCRIPT: 1, TEMPLATE: 1, CODE: 1, PRE: 1 };
  function variants(fx) {
    var conv = window.KAlifbo && window.KAlifbo.conv;
    return fx.map(function (f) {
      var v = [f.old_text];
      if (conv) { var c = conv(f.old_text); if (c !== f.old_text) v.push(c); }
      return { v: v, n: f.new_text };
    });
  }
  function fixNode(n, fx) {
    var t = n.nodeValue, o = t;
    for (var i = 0; i < fx.length; i++) for (var j = 0; j < fx[i].v.length; j++) {
      var a = fx[i].v[j];
      if (a && t.indexOf(a) !== -1) t = t.split(a).join(fx[i].n);
    }
    if (t !== o) n.nodeValue = t;
  }
  function walk(root, fx) {
    if (!root) return;
    if (root.nodeType === 3) { if (root.parentNode && !SKIP[root.parentNode.nodeName]) fixNode(root, fx); return; }
    if (root.nodeType !== 1 || SKIP[root.nodeName]) return;
    var tw = document.createTreeWalker(root, 4, null), n;
    while ((n = tw.nextNode())) if (!SKIP[n.parentNode.nodeName]) fixNode(n, fx);
  }
  function ready(cb) { if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", cb); else cb(); }
  load().then(function (all) {
    var fx = mine(all || []);
    if (!fx.length) return;
    ready(function () {
      var vx = variants(fx);
      walk(document.body, vx);
      new MutationObserver(function (ms) {
        for (var i = 0; i < ms.length; i++) for (var j = 0; j < ms[i].addedNodes.length; j++) walk(ms[i].addedNodes[j], vx);
      }).observe(document.body, { childList: true, subtree: true });
    });
  });
})();

// ── Sayt tahrirlari (2026-11-13): admin → Vebsayt (site_edits, status=active).
//    hide: element koʻrinmaydi · html: elementning ichki matni almashadi (faqat matn va oddiy teglar).
//    Element CSS yoʻli (sel) bilan topiladi; asl matn boshi (guard) mos kelmasa, shu teg ichidan guard boʻyicha izlanadi,
//    topilmasa oʻzgarish qoʻllanmaydi. Yashirish oldindan CSS bilan (kesh), sahifa yuklangach tekshiriladi.
//    Muharrir: ?kedit=1 (faqat admin; js/site-editor.js), chiqish ?kedit=0. Oʻchirish: ?edits=0
//    text (2026-11-25): murakkab blok (tugma, ikonka, ⓘ, forma ichida) tuzilmasi tegilmaydi, faqat matn tugunlari almashadi.
//    Bu blok js/site-edits.js ga ham koʻchiriladi (kompas-ui.js yuklamaydigan sahifalar uchun):
//    python3 tools/site/site_edits_js.py. Belgilar orasini oʻzgartirsangiz, skriptni qayta ishga tushiring.
// <site-edits>
(function () {
  if (window.KSiteEdits) return; // sahifada ikkala fayl boʻlsa, bir marta
  var file = location.pathname.split("/").pop() || "index.html";
  if (!/\.html?$/.test(file)) file += ".html";
  if (/^admin/.test(file)) return;
  var G = 60;
  var SKIPT = { SCRIPT: 1, STYLE: 1, NOSCRIPT: 1, TEMPLATE: 1 };
  function txt(el) {
    if (!el) return "";
    if (el.nodeType === 3) return el.nodeValue;
    var out = "", tw = (el.ownerDocument || document).createTreeWalker(el, 4, null), n;
    while ((n = tw.nextNode())) {
      var p = n.parentNode, bad = false;
      while (p && p !== el) { if (SKIPT[p.nodeName]) { bad = true; break; } p = p.parentNode; }
      if (!bad) out += n.nodeValue;
    }
    return out;
  }
  // Alifbodan qatʼi nazar bir xil: oʻ/ö → o, gʻ/ğ → g, ş → sh, ç → ch; faqat harflar qoladi
  function norm(s) {
    return String(s || "").toLowerCase()
      .replace(/([og])[\u02bb\u02bc'\u2018\u2019`]/g, "$1")
      .replace(/ö/g, "o").replace(/ğ/g, "g").replace(/ş/g, "sh").replace(/ç/g, "ch")
      .replace(/[^a-z\u00c0-\u024f\u0400-\u04ff]/g, "");
  }
  function guard(el) { return norm(txt(el)).slice(0, G); }
  function okId(id, doc) {
    if (!id || !/^[A-Za-z][\w-]*$/.test(id)) return false;
    try { return doc.querySelectorAll("#" + id).length === 1; } catch (e) { return false; }
  }
  function path(el) {
    var doc = el.ownerDocument || document, parts = [];
    while (el && el.nodeType === 1 && el !== doc.body && el !== doc.documentElement) {
      var id = el.getAttribute("id");
      if (okId(id, doc)) { parts.unshift("#" + id); return parts.join(" > "); }
      var i = 1, s = el;
      while ((s = s.previousElementSibling)) if (s.tagName === el.tagName) i++;
      parts.unshift(el.tagName.toLowerCase() + ":nth-of-type(" + i + ")");
      el = el.parentElement;
    }
    parts.unshift("body");
    return parts.join(" > ");
  }
  function q(doc, sel) { try { return doc.querySelector(sel); } catch (e) { return null; } }
  function same(el, g) { return !g || guard(el) === g; }
  function locate(r, doc) {
    doc = doc || document;
    var el = q(doc, r.sel);
    if (el && same(el, r.guard)) return el;
    if (!r.guard) return null;
    var head = /^#[A-Za-z][\w-]*/.exec(r.sel), root = head ? q(doc, head[0]) : doc.body;
    var tag = (/([a-z][a-z0-9]*)(?::nth-of-type\(\d+\))?$/.exec(r.sel) || [])[1];
    if (!root || !tag) return null;
    var c = [].filter.call(root.querySelectorAll(tag), function (x) { return guard(x) === r.guard; });
    return c.length === 1 ? c[0] : null;
  }
  var OKTAG = { B: 1, STRONG: 1, I: 1, EM: 1, U: 1, BR: 1, SMALL: 1, MARK: 1, SUB: 1, SUP: 1, A: 1, SPAN: 1 };
  function clean(html) {
    var t = document.createElement("template");
    t.innerHTML = String(html || "");
    (function walk(node) {
      [].slice.call(node.childNodes).forEach(function (c) {
        if (c.nodeType === 3) return;
        if (c.nodeType !== 1 || !OKTAG[c.nodeName]) {
          if (c.nodeType === 1 && !SKIPT[c.nodeName]) {
            walk(c);
            if (/^(DIV|P|LI|H\d)$/.test(c.nodeName) && c.previousSibling) node.insertBefore(document.createElement("br"), c);
            while (c.firstChild) node.insertBefore(c.firstChild, c);
          }
          node.removeChild(c); return;
        }
        [].slice.call(c.attributes).forEach(function (a) {
          var n = a.name.toLowerCase(), v = a.value, keep = false;
          if (n === "class") keep = /^[\w\- ]{1,80}$/.test(v);
          else if (c.nodeName === "A" && n === "href") keep = /^(https?:\/\/|mailto:|tel:|\/|#|[\w.-]+\.html)/i.test(v.trim()) && !/^\s*javascript:/i.test(v);
          else if (c.nodeName === "A" && n === "target") keep = v === "_blank";
          else if (n === "lang") keep = /^[a-z]{2,3}(-[A-Za-z]{2,4})?$/.test(v);
          else if (n === "translate") keep = v === "no";
          else if (n === "data-alifbo") keep = v === "off";
          else if (n === "aria-hidden") keep = v === "true";
          else if (n === "data-snd") keep = /^[a-z0-9]{1,16}$/.test(v);
          if (!keep) c.removeAttribute(a.name);
        });
        if (c.nodeName === "A" && c.getAttribute("target")) c.setAttribute("rel", "noopener");
        walk(c);
      });
    })(t.content);
    return t.innerHTML;
  }
  // ── Blok uslubi (kind 'style', 2026-11-19): {"fs":1.15,"w":560,"sym":true} ──
  // fs: shu blok va ichidagi matn (var(--kt-fs) orqali, KLook CSS ni bir marta oʻtkazadi);
  // w: kenglik px, blok avtomatik markazda, telefonda ota blokdan oshmaydi;
  // sym: bir qatordagi bir xil (teg + class) qoʻshni bloklarga ham shu kenglik.
  var FS_LIM = [0.7, 1.6], W_MIN = 80;
  function parseStyle(v) {
    var o = {}; try { o = typeof v === "string" ? JSON.parse(v) : (v || {}); } catch (e) { o = {}; }
    var r = {};
    var f = +o.fs; if (isFinite(f) && f > 0 && Math.abs(f - 1) > 0.001) r.fs = Math.min(FS_LIM[1], Math.max(FS_LIM[0], Math.round(f * 100) / 100));
    var w = +o.w; if (isFinite(w) && w >= W_MIN && w <= 4000) r.w = Math.round(w);
    if (typeof o.sym === "boolean") r.sym = o.sym; // false: faqat shu blok
    return r;
  }
  function peers(el) {
    var p = el.parentElement; if (!p) return [];
    var cls = (el.getAttribute("class") || "").split(/\s+/).filter(Boolean).sort().join(" ");
    return [].filter.call(p.children, function (c) {
      return c !== el && c.tagName === el.tagName && (c.getAttribute("class") || "").split(/\s+/).filter(Boolean).sort().join(" ") === cls;
    });
  }
  function clearStyle(el) {
    if (!el || !el.__kstyle) return;
    var o = el.__kstyle; el.__kstyle = null;
    ["--kt-fs", "font-size", "width", "max-width", "margin-left", "margin-right", "justify-self", "flex", "box-sizing"].forEach(function (p) { el.style.removeProperty(p); });
    if (o.prev) for (var k in o.prev) if (o.prev[k]) el.style.setProperty(k, o.prev[k][0], o.prev[k][1]);
    el.removeAttribute("data-kse-style");
    (o.peers || []).forEach(clearStyle);
  }
  function setW(el, w) {
    el.__kt = 1; // KLook inline uslubni qayta yozmasin
    var prev = {};
    ["width", "max-width", "margin-left", "margin-right"].forEach(function (p) { var v = el.style.getPropertyValue(p); if (v) prev[p] = [v, el.style.getPropertyPriority(p)]; });
    el.style.setProperty("box-sizing", "border-box");
    el.style.setProperty("width", w + "px", "important");
    el.style.setProperty("max-width", "100%", "important");
    el.style.setProperty("margin-left", "auto", "important");
    el.style.setProperty("margin-right", "auto", "important");
    var pd = el.parentElement ? getComputedStyle(el.parentElement).display : "";
    if (/grid/.test(pd)) el.style.setProperty("justify-self", "center");
    if (/flex/.test(pd)) el.style.setProperty("flex", "0 1 auto");
    return prev;
  }
  function style(el, v) {
    clearStyle(el);
    var o = parseStyle(v); if (!o.fs && !o.w) return o;
    var st = { prev: {}, peers: [] };
    if (o.fs) {
      var fz0 = el.style.getPropertyValue("font-size"); if (fz0) st.prev["font-size"] = [fz0, el.style.getPropertyPriority("font-size")];
      // Asl oʻlcham (global sozlamasiz): hozirgi hisoblangan px / --kt-fs0
      var r0 = parseFloat(getComputedStyle(document.documentElement).getPropertyValue("--kt-fs0")) || 1;
      var base = (parseFloat(getComputedStyle(el).fontSize) || 16) / r0;
      el.__kt = 1;
      el.style.setProperty("--kt-fs", "calc(var(--kt-fs0,1) * " + o.fs + ")");
      el.style.setProperty("font-size", "calc(" + (Math.round(base * 100) / 100) + "px * var(--kt-fs0,1) * " + o.fs + ")");
      if (window.KLook && window.KLook.need) window.KLook.need();
    }
    if (o.w) {
      var pw = setW(el, o.w); for (var k in pw) st.prev[k] = pw[k];
      if (o.sym) peers(el).forEach(function (c) {
        if (c.__kstyle) return;
        var pv = setW(c, o.w); c.__kstyle = { prev: pv, peers: [], by: el }; c.setAttribute("data-kse-style", "p"); st.peers.push(c);
      });
    }
    el.__kstyle = st; el.setAttribute("data-kse-style", "1");
    return o;
  }

  // ── Matn tugunlari (kind 'text', 2026-11-25): {"n":12,"c":{"3":"yangi matn"}} ──
  // n: blokdagi boʻsh boʻlmagan matn tugunlari soni (sahifa oʻzgarsa mos kelmaydi va qoʻllanmaydi);
  // c: oʻzgargan tugunlar (tartib raqami → matn, amaldagi alifboda). Tuzilma, atribut va JS tegilmaydi.
  function tnodes(el) {
    var out = [], tw = (el.ownerDocument || document).createTreeWalker(el, 4, null), n;
    while ((n = tw.nextNode())) {
      if (!/\S/.test(n.nodeValue)) continue;
      var p = n.parentNode, bad = false;
      while (p && p !== el) { if (SKIPT[p.nodeName]) { bad = true; break; } p = p.parentNode; }
      if (!bad) out.push(n);
    }
    return out;
  }
  function parseText(v) {
    var o = null; try { o = typeof v === "string" ? JSON.parse(v) : v; } catch (e) {}
    if (!o || typeof o.n !== "number" || !o.c || typeof o.c !== "object") return null;
    return o;
  }
  function textApply(el, v) {
    var o = parseText(v); if (!o) return false;
    var ns = tnodes(el); if (ns.length !== o.n) return false;
    for (var k in o.c) { var i = +k; if (ns[i] && typeof o.c[k] === "string" && ns[i].nodeValue !== o.c[k]) ns[i].nodeValue = o.c[k]; }
    return true;
  }

  window.KSiteEdits = { file: file, norm: norm, txt: txt, guard: guard, path: path, locate: locate, clean: clean, G: G,
    style: style, clearStyle: clearStyle, parseStyle: parseStyle, peers: peers, FS_LIM: FS_LIM, W_MIN: W_MIN,
    tnodes: tnodes, parseText: parseText, textApply: textApply };

  var S = sessionStorage, KE = "kompas_kedit";
  try {
    if (/[?&]kedit=0/.test(location.search)) {
      S.removeItem(KE);
      history.replaceState(null, "", location.pathname + location.search.replace(/([?&])kedit=0&?/, "$1").replace(/[?&]$/, "") + location.hash);
    }
    else if (/[?&]kedit=1/.test(location.search)) S.setItem(KE, "1");
  } catch (e) {}
  var EDIT = false; try { EDIT = S.getItem(KE) === "1"; } catch (e) {}
  if (EDIT) {
    var sc = document.createElement("script"); sc.src = "js/site-editor.js"; sc.defer = true;
    (document.head || document.documentElement).appendChild(sc);
    return;
  }
  if (/[?&]edits=0/.test(location.search)) return;

  var URL_ = "https://usxpkmbjrdllnitlzdpq.supabase.co/rest/v1/site_edits?select=id,sel,kind,guard,value&status=eq.active&page=eq." + encodeURIComponent(file) + "&order=id";
  var KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVzeHBrbWJqcmRsbG5pdGx6ZHBxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI1MzUxNzcsImV4cCI6MjA4ODExMTE3N30.wecMraU0qbnT89IKaoyu0-gDBfo0kUBF1t6ajMJNvT8";
  var CK = "kompas_edits_v1:" + file, TTL = 5 * 60 * 1000;
  var cache = null; try { cache = JSON.parse(localStorage.getItem(CK) || "null"); } catch (e) {}
  var st = null;
  function css(rows) {
    var s = rows.filter(function (r) { return r.kind === "hide"; }).map(function (r) { return r.sel + "{display:none!important}"; }).join("\n");
    if (!st) { st = document.createElement("style"); st.id = "kse-hide"; (document.head || document.documentElement).appendChild(st); }
    // Notoʻgʻri selektor butun qoidani buzmasligi uchun har birini alohida tekshiramiz
    st.textContent = s.split("\n").filter(function (l) { try { return l && document.querySelector(l.replace(/\{.*$/, "")) !== undefined; } catch (e) { return false; } }).join("\n");
  }
  var done = {};
  function apply(rows, final) {
    var keep = [];
    rows.forEach(function (r) {
      if (done[r.id]) { if (r.kind === "hide" && done[r.id] === "css") keep.push(r); return; }
      var el = (r.kind === "html" && document.querySelector('[data-kse-id="' + r.id + '"]')) || (r.kind === "text" && document.querySelector('[data-kse-tid="' + r.id + '"]')) || locate(r);
      if (!el) { if (!final && r.kind === "hide" && cache) keep.push(r); return; }
      if (r.kind === "hide") {
        if (q(document, r.sel) === el) { keep.push(r); done[r.id] = "css"; }
        else { el.style.setProperty("display", "none", "important"); el.setAttribute("data-kse", "h"); done[r.id] = 1; }
      } else if (r.kind === "html") {
        el.innerHTML = clean(r.value); el.setAttribute("data-kse", "t"); el.setAttribute("data-kse-id", r.id); done[r.id] = 1;
      } else if (r.kind === "style") {
        style(el, r.value); done[r.id] = 1;
      } else if (r.kind === "text") {
        // JS kech chizadigan blokda tugunlar soni hali mos kelmasa, keyingi urinishda qayta tekshiriladi
        if (textApply(el, r.value)) { el.setAttribute("data-kse-tid", r.id); done[r.id] = 1; }
      }
    });
    css(keep);
  }
  var rows = cache && Array.isArray(cache.d) ? cache.d : [];
  if (rows.length) css(rows);
  function ready(cb) { if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", cb); else cb(); }
  function fresh() {
    if (cache && Date.now() - cache.t < TTL) return Promise.resolve(rows);
    if (!window.fetch) return Promise.resolve(rows);
    return fetch(URL_, { headers: { apikey: KEY, Authorization: "Bearer " + KEY } })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (d) {
        if (!Array.isArray(d)) return rows;
        try { localStorage.setItem(CK, JSON.stringify({ t: Date.now(), d: d })); } catch (e) {}
        return d;
      })
      .catch(function () { return rows; });
  }
  ready(function () {
    if (rows.length) apply(rows, false);
    fresh().then(function (d) {
      if (d !== rows) { done = {}; rows = d; ready(function () { apply(rows, false); }); }
      // Kech yuklanadigan (JS chizadigan) qismlar uchun bir marta qayta urinish
      window.addEventListener("load", function () { setTimeout(function () { apply(rows, true); }, 400); });
      if (document.readyState === "complete") setTimeout(function () { apply(rows, true); }, 400);
    });
  });
})();
// </site-edits>
