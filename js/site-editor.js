// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — site-editor.js (2026-11-13)
//  Jonli sayt muharriri: haqiqiy sahifa ustida istalgan qismni tanlash,
//  matnini tahrirlash, yashirish va qayta koʻrsatish. Faqat admin.
//  Yoqish: sahifa?kedit=1 (yoki admin → Vebsayt → "Jonli tahrirlash"); oʻchirish: ?kedit=0.
//  Bu fayl js/kompas-ui.js tomonidan faqat tahrir rejimida yuklanadi; KSiteEdits oʻsha yerda.
//  Yozuvlar: site_edits jadvali (RLS: faqat admin yozadi). Saytda qoʻllash: kompas-ui.js.
// ═══════════════════════════════════════════════════════════════
(function () {
  "use strict";
  var K = window.KSiteEdits;
  if (!K || window.__kseLoaded) return;
  window.__kseLoaded = true;
  var FILE = K.file;
  var SB_URL = "https://usxpkmbjrdllnitlzdpq.supabase.co";
  var SB_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVzeHBrbWJqcmRsbG5pdGx6ZHBxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI1MzUxNzcsImV4cCI6MjA4ODExMTE3N30.wecMraU0qbnT89IKaoyu0-gDBfo0kUBF1t6ajMJNvT8";
  var UMD = "https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/dist/umd/supabase.min.js";
  var COLS = "id,page,sel,kind,guard,label,value,status";
  var OKTAG = { B: 1, STRONG: 1, I: 1, EM: 1, U: 1, BR: 1, SMALL: 1, MARK: 1, SUB: 1, SUP: 1, A: 1, SPAN: 1 };
  var OKATTR = /^(class|href|target|rel|lang|translate|data-alifbo)$/;
  var sb = null, rows = [], lost = [], mode = "pick", cur = null, editing = null, client = false;

  // ── yordamchilar ─────────────────────────────────────────────
  function ready(cb) { if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", cb); else cb(); }
  function load(src) {
    return new Promise(function (res, rej) {
      var s = document.createElement("script"); s.src = src; s.onload = res;
      s.onerror = function () { rej(new Error("Yuklanmadi: " + src)); };
      document.head.appendChild(s);
    });
  }
  function getClient() {
    // Sahifaning oʻz mijozi boʻlsa, oʻshani ishlatamiz; window.supabase ni hech qachon almashtirmaymiz
    var w = window.supabase;
    if (w && typeof w.from === "function") return Promise.resolve(w);
    var make = function (lib) { return lib.createClient(SB_URL, SB_KEY, { auth: { persistSession: true, autoRefreshToken: true, detectSessionInUrl: false } }); };
    if (w && typeof w.createClient === "function") return Promise.resolve(make(w));
    return load(UMD).then(function () { return make(window.supabase); });
  }
  function short(s, n) { s = String(s || "").replace(/\s+/g, " ").trim(); return s.length > n ? s.slice(0, n - 1) + "…" : s; }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function tagName(el) { return el.tagName.toLowerCase(); }
  function words(el) {
    var tw = document.createTreeWalker(el, 4, null), out = [], n;
    while ((n = tw.nextNode())) if (!/^(SCRIPT|STYLE|NOSCRIPT|TEMPLATE)$/.test(n.parentNode.nodeName)) out.push(n.nodeValue);
    return out.join(" ");
  }
  function labelOf(el) {
    var h = el.querySelector && el.querySelector("h1,h2,h3,h4");
    var t = short(words(h || el), 70);
    return "<" + tagName(el) + (el.id ? "#" + el.id : "") + "> " + (t || "(matnsiz)");
  }
  // Yangi alifbo (Ö Ğ Ş Ç) → manbadagi amaldagi alifbo (oʻ gʻ sh ch, U+02BB / U+02BC)
  function toOld(t) {
    return t.replace(/Ş(?=[A-ZÖĞŞÇ])/g, "SH").replace(/Ç(?=[A-ZÖĞŞÇ])/g, "CH")
      .replace(/Ş/g, "Sh").replace(/ş/g, "sh").replace(/Ç/g, "Ch").replace(/ç/g, "ch")
      .replace(/Ö/g, "Oʻ").replace(/ö/g, "oʻ").replace(/Ğ/g, "Gʻ").replace(/ğ/g, "gʻ")
      .replace(/([oOgG])['\u2018\u2019`](?=[A-Za-z])/g, "$1\u02bb")
      .replace(/([A-Za-z])['\u2018\u2019`](?=[A-Za-z])/g, "$1\u02bc");
  }
  function oldHtml(html) {
    var t = document.createElement("template"); t.innerHTML = html;
    var tw = document.createTreeWalker(t.content, 4, null), n;
    while ((n = tw.nextNode())) {
      var p = n.parentNode, foreign = false;
      while (p && p.nodeType === 1) {
        var lg = p.getAttribute("lang");
        if ((lg && !/^uz/i.test(lg)) || p.getAttribute("translate") === "no" || p.getAttribute("data-alifbo") === "off") { foreign = true; break; }
        p = p.parentNode;
      }
      if (!foreign) n.nodeValue = toOld(n.nodeValue);
    }
    return t.innerHTML;
  }
  function dropCache() { try { localStorage.removeItem("kompas_edits_v1:" + FILE); } catch (e) {} }
  function inHost(t) { return t === host || (host && host.contains(t)); }
  function rowsOf(el) { return el && el.__kse ? el.__kse : {}; }
  function setRow(el, r) { el.__kse = el.__kse || {}; el.__kse[r.kind] = r; }

  // ── koʻrinish (Shadow DOM: sayt CSS iga taʼsir qilmaydi) ──────────
  var host = document.createElement("div");
  host.id = "kse-host";
  host.setAttribute("data-alifbo", "off");
  host.setAttribute("translate", "no");
  var root = host.attachShadow({ mode: "open" });
  root.innerHTML = '<style>' +
    ':host{all:initial}' +
    '*{box-sizing:border-box;font-family:Outfit,"IBM Plex Sans",system-ui,sans-serif}' +
    '.box{position:fixed;pointer-events:none;z-index:2147483645;border-radius:4px;display:none}' +
    '.hov{outline:2px dashed #c4622d;background:rgba(196,98,45,.06)}' +
    '.sel{outline:3px solid #2d4a3e;background:rgba(45,74,62,.07)}' +
    '.tip{position:fixed;z-index:2147483646;pointer-events:none;background:#1a2e26;color:#fff;font-size:11px;padding:3px 7px;border-radius:5px;display:none;max-width:60vw;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}' +
    '.pn{position:fixed;right:16px;bottom:16px;z-index:2147483647;width:340px;max-width:calc(100vw - 24px);background:#fff;color:#1a2e26;border:1px solid #dce8e2;border-radius:14px;box-shadow:0 12px 40px rgba(0,0,0,.18);font-size:13px;overflow:hidden}' +
    '.hd{display:flex;align-items:center;gap:8px;padding:10px 12px;background:#2d4a3e;color:#fff}' +
    '.hd b{font-size:13px}.hd .pg{opacity:.7;font-size:11px;flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}' +
    '.hd button{background:rgba(255,255,255,.14);color:#fff;border:0;border-radius:6px;width:26px;height:24px;cursor:pointer;font-size:13px}' +
    '.bd{padding:10px 12px;display:grid;gap:9px;max-height:60vh;overflow:auto}' +
    '.pn.min .bd{display:none}' +
    '.seg{display:flex;background:#f0f4f2;border-radius:9px;padding:3px}' +
    '.seg button{flex:1;border:0;background:none;padding:6px;border-radius:7px;font-weight:700;font-size:12px;color:#6b7f76;cursor:pointer}' +
    '.seg button.on{background:#fff;color:#2d4a3e;box-shadow:0 1px 3px rgba(0,0,0,.08)}' +
    '.row{display:flex;flex-wrap:wrap;gap:6px}' +
    '.b{border:1px solid #dce8e2;background:#fff;color:#1a2e26;border-radius:8px;padding:6px 10px;font-size:12px;font-weight:700;cursor:pointer}' +
    '.b:hover{border-color:#2d4a3e}.b:disabled{opacity:.45;cursor:not-allowed}' +
    '.b.p{background:#2d4a3e;border-color:#2d4a3e;color:#fff}.b.w{color:#c4622d}' +
    '.lbl{font-size:12px;line-height:1.45;background:#f4f3ef;border-radius:8px;padding:7px 9px;word-break:break-word}' +
    '.lbl code{font-family:"JetBrains Mono",monospace;font-size:10.5px;color:#6b7f76}' +
    '.note{font-size:11.5px;color:#6b7f76;line-height:1.45}' +
    '.msg{font-size:12px;min-height:0}.msg.ok{color:#1a7a4a}.msg.er{color:#c0392b}' +
    '.ft{display:flex;justify-content:space-between;align-items:center;font-size:11.5px;color:#6b7f76;border-top:1px solid #dce8e2;padding-top:8px}' +
    '.ft a{color:#2d4a3e;font-weight:700}' +
    'label.chk{display:flex;gap:6px;align-items:center;font-size:12px;color:#1a2e26;cursor:pointer}' +
    '.lost{font-size:11.5px;background:#fdecea;color:#c0392b;border-radius:8px;padding:7px 9px;line-height:1.5}' +
    '.lost button{margin-left:4px}' +
    '@media(max-width:560px){.pn{right:8px;left:8px;bottom:8px;width:auto}}' +
    '</style>' +
    '<div class="box hov"></div><div class="box sel"></div><div class="tip"></div>' +
    '<div class="pn" role="dialog" aria-label="Sayt muharriri">' +
    '<div class="hd"><b>✏️ Sayt muharriri</b><span class="pg"></span>' +
    '<button data-a="min" title="Yigʻish">–</button><button data-a="exit" title="Muharrirdan chiqish">✕</button></div>' +
    '<div class="bd">' +
    '<div class="seg"><button data-a="pick" class="on">🎯 Tanlash</button><button data-a="browse">👆 Saytni bosish</button></div>' +
    '<label class="chk"><input type="checkbox" data-a="client"> Mijoz koʻrinishi (yashirinlar koʻrinmaydi)</label>' +
    '<div class="cur"></div><div class="lostbox"></div><div class="msg"></div>' +
    '<div class="ft"><span class="cnt"></span><a href="admin.html#vebsayt" target="_blank" rel="noopener">Admin → Vebsayt ↗</a></div>' +
    '</div></div>';
  var $ = function (s) { return root.querySelector(s); };
  var hov = $(".hov"), selb = $(".sel"), tip = $(".tip"), pn = $(".pn");
  $(".pg").textContent = FILE;

  var pageCss = document.createElement("style");
  pageCss.id = "kse-page-css";
  pageCss.textContent =
    "[data-kse-hidden]{opacity:.35!important;outline:2px dashed #c4622d!important;outline-offset:-3px}" +
    "html.kse-client [data-kse-hidden]{display:none!important}" +
    "html.kse-pick body *{cursor:crosshair!important}" +
    "[data-kse-editing]{outline:2px solid #c9a84c!important;outline-offset:3px;cursor:text!important;background:rgba(201,168,76,.08)}" +
    "html.kse-pick [data-kse-editing], html.kse-pick [data-kse-editing] *{cursor:text!important}";

  // Panel matni ham saytdagi kabi yangi alifboda (alifbo.js Shadow DOM ichiga kirmaydi)
  function cv(node) {
    var c = window.KAlifbo && window.KAlifbo.conv; if (!c || !node) return;
    var tw = document.createTreeWalker(node, 4, null), n;
    while ((n = tw.nextNode())) {
      if (n.parentNode && /^(CODE|STYLE)$/.test(n.parentNode.nodeName)) continue;
      var v = c(n.nodeValue); if (v !== n.nodeValue) n.nodeValue = v;
    }
  }
  function msg(t, kind) { var m = $(".msg"); m.className = "msg" + (kind ? " " + kind : ""); m.textContent = t || ""; cv(m); }
  function place(box, el) {
    if (!el || !el.isConnected) { box.style.display = "none"; return; }
    var r = el.getBoundingClientRect();
    if (!r.width && !r.height) { box.style.display = "none"; return; }
    box.style.display = "block";
    box.style.left = r.left + "px"; box.style.top = r.top + "px";
    box.style.width = r.width + "px"; box.style.height = r.height + "px";
  }
  var hovEl = null;
  function track() {
    place(hov, mode === "pick" && !editing && hovEl !== cur ? hovEl : null);
    place(selb, cur);
    if (mode === "pick" && hovEl && !editing && hovEl !== cur) {
      var r = hovEl.getBoundingClientRect();
      tip.style.display = "block"; tip.textContent = labelOf(hovEl);
      tip.style.left = Math.max(4, r.left) + "px"; tip.style.top = Math.max(4, r.top - 22) + "px";
    } else tip.style.display = "none";
  }
  var raf = 0;
  function sched() { if (!raf) raf = requestAnimationFrame(function () { raf = 0; track(); }); }

  // ── element holati ──────────────────────────────────────────
  function why(el) {
    if (!el || el === document.body || el === document.documentElement) return "Bu butun sahifa";
    if (/^(SCRIPT|STYLE|INPUT|TEXTAREA|SELECT|IMG|CANVAS|VIDEO|IFRAME|svg|SVG)$/.test(el.nodeName)) return "Bu element matn emas";
    if (!K.norm(K.txt(el))) return "Bu elementda matn yoʻq";
    for (var p = el.parentElement; p && p !== document.body; p = p.parentElement)
      if (p.hasAttribute("data-kse-id")) return "Yuqoridagi blok allaqachon tahrirlangan: oʻsha blokni tahrirlang (⬆ Ota blok)";
    var all = el.querySelectorAll("*");
    for (var i = 0; i < all.length; i++) {
      var c = all[i];
      if (!OKTAG[c.nodeName]) return "Ichida <" + tagName(c) + "> bor: ichkiroq (kichikroq) qismni tanlang";
      for (var j = 0; j < c.attributes.length; j++) {
        var a = c.attributes[j].name;
        if (!OKATTR.test(a) && !/^data-kse/.test(a)) return "Ichida sayt kodi boshqaradigan qism bor (" + a + "): ichkiroq qismni tanlang";
      }
    }
    if (K.txt(el).length > 4000) return "Matn juda uzun: kichikroq qismni tanlang";
    return "";
  }
  function render() {
    var box = $(".cur");
    var n = rows.length;
    $(".cnt").textContent = n ? "Bu sahifada " + n + " ta oʻzgarish" : "Bu sahifada oʻzgarish yoʻq";
    if (!cur) {
      box.innerHTML = '<div class="note">' + (mode === "pick"
        ? "Sahifadagi istalgan qismni bosing: matnini tahrirlash yoki yashirish mumkin."
        : "Sayt odatdagidek ishlaydi (havolalar ochiladi). Tahrirlash uchun “Tanlash”ni bosing.") + "</div>";
      cv(box); cv($(".cnt"));
      return;
    }
    var rs = rowsOf(cur), hidden = !!rs.hide, w = why(cur);
    var h = '<div class="lbl">' + esc(labelOf(cur)) + '<br><code>' + esc(short(K.path(cur), 90)) + '</code>' +
      (hidden ? '<br><b style="color:#c4622d">Saytda yashirin</b>' : "") +
      (rs.html ? '<br><b style="color:#b08a00">Matni tahrirlangan</b>' : "") + '</div>';
    if (editing) {
      h += '<div class="row"><button class="b p" data-a="save">💾 Saqlash</button><button class="b" data-a="cancel">Bekor</button></div>' +
        '<div class="note">Matnni toʻgʻridan-toʻgʻri sahifada yozing. Ctrl+Enter saqlaydi, Esc bekor qiladi. Qalin/kursiv: Ctrl+B / Ctrl+I.</div>';
    } else {
      h += '<div class="row">' +
        '<button class="b" data-a="up"' + (cur.parentElement && cur.parentElement !== document.body && cur.parentElement !== document.documentElement ? "" : " disabled") + '>⬆ Ota blok</button>' +
        '<button class="b" data-a="edit"' + (w ? " disabled" : "") + '>✏️ Matnni tahrirlash</button>' +
        (hidden ? '<button class="b" data-a="show">👁 Koʻrsatish</button>' : '<button class="b w" data-a="hide">🙈 Yashirish</button>') +
        (rs.html ? '<button class="b" data-a="revert">↩ Asl matn</button>' : "") +
        '<button class="b" data-a="desel">✕</button></div>' +
        (w ? '<div class="note">' + esc(w) + '</div>' : "");
    }
    box.innerHTML = h; cv(box); cv($(".cnt"));
  }
  function renderLost() {
    var b = $(".lostbox");
    if (!lost.length) { b.innerHTML = ""; return; }
    b.innerHTML = '<div class="lost">⚠️ ' + lost.length + ' ta oʻzgarish bu sahifada topilmadi (sahifa manbasi oʻzgargan boʻlishi mumkin), saytda qoʻllanmayapti:' +
      lost.map(function (r) {
        return '<div>' + (r.kind === "hide" ? "Yashirish" : "Matn") + ": " + esc(short(r.label || r.sel, 60)) +
          ' <button class="b" data-a="off" data-id="' + r.id + '">Bekor qilish</button></div>';
      }).join("") + '</div>';
    cv(b);
  }
  function select(el) {
    if (!el || inHost(el)) return;
    if (el === document.documentElement) el = document.body;
    cur = el === document.body ? null : el;
    render(); sched();
  }

  // ── bazaga yozish ───────────────────────────────────────────
  function fail(e) { msg("❌ " + (e && (e.message || e.details) || e), "er"); }
  async function write(kind, el, fields) {
    var r = rowsOf(el)[kind];
    var res;
    if (r) res = await sb.from("site_edits").update(fields).eq("id", r.id).select(COLS).single();
    else {
      var base = { page: FILE, sel: K.path(el), kind: kind, guard: el.__kseGuard != null ? el.__kseGuard : K.guard(el), label: short(labelOf(el), 160) };
      res = await sb.from("site_edits").insert(Object.assign(base, fields)).select(COLS).single();
      if (res.error && res.error.code === "23505") {
        // Shu yoʻlda topilmagan eski faol yozuv bor: uni shu element bilan yangilaymiz
        var old = await sb.from("site_edits").select("id").eq("page", FILE).eq("sel", base.sel).eq("kind", kind).eq("status", "active").maybeSingle();
        if (old.data) res = await sb.from("site_edits").update(Object.assign({ guard: base.guard, label: base.label }, fields)).eq("id", old.data.id).select(COLS).single();
      }
    }
    if (res.error) throw res.error;
    dropCache();
    return res.data;
  }
  function forget(row) {
    rows = rows.filter(function (x) { return x.id !== row.id; });
    lost = lost.filter(function (x) { return x.id !== row.id; });
  }
  async function hide(on) {
    var el = cur; if (!el) return;
    try {
      if (on) {
        var r = await write("hide", el, { status: "active" });
        setRow(el, r); rows.push(r); el.setAttribute("data-kse-hidden", "");
        msg("✅ Yashirildi. Saytda bir necha daqiqada (yangi tashrifda) koʻrinmaydi.", "ok");
      } else {
        var o = rowsOf(el).hide;
        var u = await sb.from("site_edits").update({ status: "off" }).eq("id", o.id);
        if (u.error) throw u.error;
        dropCache(); forget(o); delete el.__kse.hide; el.removeAttribute("data-kse-hidden");
        msg("✅ Yana koʻrinadi.", "ok");
      }
    } catch (e) { fail(e); }
    render(); sched();
  }
  function startEdit() {
    var el = cur; if (!el || why(el)) return;
    if (el.__kseGuard == null && !rowsOf(el).html) el.__kseGuard = K.guard(el);
    editing = { el: el, html: el.innerHTML };
    el.setAttribute("contenteditable", "true");
    el.setAttribute("data-kse-editing", "");
    el.focus();
    try { var rg = document.createRange(); rg.selectNodeContents(el); rg.collapse(false); var s = getSelection(); s.removeAllRanges(); s.addRange(rg); } catch (e) {}
    msg(""); render(); sched();
  }
  function endEdit() {
    if (!editing) return;
    var el = editing.el;
    el.removeAttribute("contenteditable"); el.removeAttribute("data-kse-editing");
    editing = null;
  }
  function cancelEdit() {
    if (!editing) return;
    editing.el.innerHTML = editing.html;
    endEdit(); msg(""); render(); sched();
  }
  async function saveEdit() {
    if (!editing) return;
    var el = editing.el;
    var html = oldHtml(K.clean(el.innerHTML)).replace(/^(\s|&nbsp;|<br>)+|(\s|&nbsp;|<br>)+$/g, "");
    if (!K.norm(html.replace(/<[^>]+>/g, ""))) { msg("⚠️ Matn boʻsh boʻlib qoldi. Qismni olib tashlash uchun “Yashirish”dan foydalaning.", "er"); return; }
    if (html.length > 20000) { msg("⚠️ Matn juda uzun", "er"); return; }
    try {
      var r = await write("html", el, { value: html, status: "active" });
      // Ichidagi oldingi matn tahrirlari endi shu blok ichida: ularni bekor qilamiz
      var inner = [].slice.call(el.querySelectorAll("[data-kse-id]"));
      for (var i = 0; i < inner.length; i++) {
        var id = +inner[i].getAttribute("data-kse-id");
        await sb.from("site_edits").update({ status: "off" }).eq("id", id);
        rows = rows.filter(function (x) { return x.id !== id; });
      }
      endEdit();
      setRow(el, r);
      if (!rows.some(function (x) { return x.id === r.id; })) rows.push(r); else rows = rows.map(function (x) { return x.id === r.id ? r : x; });
      el.innerHTML = K.clean(r.value);
      el.setAttribute("data-kse", "t"); el.setAttribute("data-kse-id", r.id);
      msg("✅ Saqlandi. Saytda bir necha daqiqada (yangi tashrifda) koʻrinadi.", "ok");
    } catch (e) { fail(e); }
    render(); sched();
  }
  async function revert() {
    var el = cur, o = el && rowsOf(el).html;
    if (!o || !confirm("Bu qism manbadagi asl matnga qaytarilsinmi?")) return;
    var u = await sb.from("site_edits").update({ status: "off" }).eq("id", o.id);
    if (u.error) { fail(u.error); return; }
    dropCache();
    location.reload();
  }
  async function off(id) {
    var u = await sb.from("site_edits").update({ status: "off" }).eq("id", id);
    if (u.error) { fail(u.error); return; }
    dropCache();
    var r = lost.filter(function (x) { return x.id === id; })[0];
    if (r) forget(r);
    renderLost(); render(); msg("✅ Bekor qilindi", "ok");
  }

  // ── hodisalar ───────────────────────────────────────────────
  function setMode(m) {
    mode = m;
    document.documentElement.classList.toggle("kse-pick", m === "pick");
    [].forEach.call(root.querySelectorAll(".seg button"), function (b) { b.classList.toggle("on", b.getAttribute("data-a") === m); });
    hovEl = null; render(); sched();
  }
  root.addEventListener("click", function (e) {
    var b = e.target.closest("[data-a]"); if (!b) return;
    var a = b.getAttribute("data-a");
    if (a === "pick" || a === "browse") { if (editing) cancelEdit(); setMode(a); }
    else if (a === "min") pn.classList.toggle("min");
    else if (a === "exit") {
      if (editing && !confirm("Saqlanmagan matn bor. Chiqilsinmi?")) return;
      try { sessionStorage.removeItem("kompas_kedit"); } catch (er) {}
      location.href = location.pathname + "?kedit=0";
    }
    else if (a === "client") { client = b.checked; document.documentElement.classList.toggle("kse-client", client); sched(); }
    else if (a === "up") { if (cur && cur.parentElement) select(cur.parentElement); }
    else if (a === "edit") startEdit();
    else if (a === "save") saveEdit();
    else if (a === "cancel") cancelEdit();
    else if (a === "hide") hide(true);
    else if (a === "show") hide(false);
    else if (a === "revert") revert();
    else if (a === "desel") { cur = null; render(); sched(); }
    else if (a === "off") off(+b.getAttribute("data-id"));
  });
  function guardEv(e) {
    if (inHost(e.target)) return;
    if (editing) {
      if (editing.el.contains(e.target)) { if (e.target.closest && e.target.closest("a")) e.preventDefault(); return; }
      e.preventDefault(); e.stopPropagation(); e.stopImmediatePropagation();
      return;
    }
    if (mode !== "pick") return;
    e.preventDefault(); e.stopPropagation(); e.stopImmediatePropagation();
    if (e.type === "click") select(e.target);
  }
  ["click", "auxclick", "dblclick", "submit"].forEach(function (t) { window.addEventListener(t, guardEv, true); });
  window.addEventListener("mouseover", function (e) {
    if (editing || mode !== "pick") return;
    hovEl = inHost(e.target) ? null : e.target;
    sched();
  }, true);
  window.addEventListener("scroll", sched, true);
  window.addEventListener("resize", sched);
  window.addEventListener("keydown", function (e) {
    if (editing) {
      if (e.key === "Escape") { e.preventDefault(); cancelEdit(); }
      else if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) { e.preventDefault(); saveEdit(); }
      return;
    }
    if (e.key === "Escape" && cur) { cur = null; render(); sched(); }
  }, true);
  window.addEventListener("beforeunload", function (e) { if (editing) { e.preventDefault(); e.returnValue = ""; } });

  // ── ishga tushirish ─────────────────────────────────────────
  function applyAll() {
    lost = [];
    rows.forEach(function (r) {
      var el = (r.kind === "html" && document.querySelector('[data-kse-id="' + r.id + '"]')) || K.locate(r);
      if (!el) { lost.push(r); return; }
      setRow(el, r);
      if (r.kind === "hide") el.setAttribute("data-kse-hidden", "");
      else if (r.kind === "html" && el.getAttribute("data-kse-id") !== String(r.id)) {
        el.__kseGuard = r.guard;
        el.innerHTML = K.clean(r.value);
        el.setAttribute("data-kse", "t"); el.setAttribute("data-kse-id", r.id);
      }
    });
  }
  function deepLink() {
    var m = /[?&]ksel=([^&#]+)/.exec(location.search); if (!m) return;
    var g = /[?&]kg=([^&#]*)/.exec(location.search);
    var el = K.locate({ sel: decodeURIComponent(m[1]), guard: g ? decodeURIComponent(g[1]) : "" });
    if (!el) { msg("⚠️ Admin paneldan tanlangan qism bu sahifada topilmadi", "er"); return; }
    select(el);
    el.scrollIntoView({ block: "center" });
    setTimeout(sched, 400);
  }
  ready(function () {
    document.head.appendChild(pageCss);
    document.documentElement.appendChild(host);
    cv(pn);
    setMode("pick");
    msg("Kirish tekshirilmoqda…");
    getClient().then(function (c) {
      sb = c;
      return sb.auth.getSession();
    }).then(function (s) {
      if (!s.data || !s.data.session) throw new Error("NOAUTH");
      return sb.rpc("fn_is_admin");
    }).then(function (a) {
      if (a.error || a.data !== true) throw new Error("NOADMIN");
      return sb.from("site_edits").select(COLS).eq("page", FILE).eq("status", "active").order("id");
    }).then(function (r) {
      if (r.error) throw r.error;
      rows = r.data || [];
      // JS chizadigan qismlar ulgursin
      return new Promise(function (res) { if (document.readyState === "complete") setTimeout(res, 300); else window.addEventListener("load", function () { setTimeout(res, 300); }); });
    }).then(function () {
      applyAll(); renderLost(); render(); msg(""); deepLink();
    }).catch(function (e) {
      var m = e && e.message;
      setMode("browse");
      root.querySelector(".seg").style.display = "none";
      if (m === "NOAUTH") $(".cur").innerHTML = '<div class="note">Tahrirlash uchun admin hisobi bilan kiring: <a href="login.html" style="color:#2d4a3e;font-weight:700">Kirish</a></div>';
      else if (m === "NOADMIN") $(".cur").innerHTML = '<div class="note">Bu rejim faqat adminlar uchun. Chiqish uchun ✕ ni bosing.</div>';
      else fail(e);
      if (m === "NOAUTH" || m === "NOADMIN") msg("");
      cv($(".cur"));
    });
  });
})();
