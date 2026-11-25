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
  // aria-hidden: sarlavhadagi ⓘ (span.kl-i); data-snd: havola tovushi (2026-11-21: ikkalasi tahrirni yopib qoʻyardi)
  var OKATTR = /^(class|href|target|rel|lang|translate|data-alifbo|aria-hidden|data-snd)$/;
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
    '.hdl{position:fixed;z-index:2147483647;width:12px;height:34px;margin:-17px 0 0 -6px;border-radius:6px;background:#fff;border:2px solid #2d4a3e;box-shadow:0 1px 4px rgba(0,0,0,.25);cursor:ew-resize;display:none;touch-action:none}' +
    '.hdl:hover,.hdl.on{background:#2d4a3e}' +
    '.gd{position:fixed;z-index:2147483645;pointer-events:none;border-left:1px dashed #c4622d;display:none}' +
    '.sz{display:grid;gap:6px;border-top:1px solid #dce8e2;padding-top:8px}' +
    '.szh{font-size:11px;font-weight:800;letter-spacing:.04em;text-transform:uppercase;color:#6b7f76}' +
    '.szr{display:grid;grid-template-columns:62px 34px 1fr 34px auto;gap:6px;align-items:center;font-size:12px}' +
    '.szr .b{padding:5px 0;text-align:center}.szr .v{text-align:center;font:700 12px "JetBrains Mono",monospace}' +
    '.szr .b.s{padding:5px 8px}' +
    '.tl{display:grid;gap:6px;max-height:42vh;overflow:auto;padding-right:2px}' +
    '.ti{display:grid;gap:2px}.ti span{font:600 10.5px "JetBrains Mono",monospace;color:#6b7f76}' +
    '.ti textarea{width:100%;resize:vertical;min-height:30px;border:1px solid #dce8e2;border-radius:7px;padding:5px 7px;font-size:13px;line-height:1.4;color:#1a2e26;background:#fff}' +
    '.ti textarea:focus{outline:2px solid #2d4a3e;border-color:#2d4a3e}' +
    '@media(max-width:560px){.pn{right:8px;left:8px;bottom:8px;width:auto}}' +
    '</style>' +
    '<div class="box hov"></div><div class="box sel"></div><div class="tip"></div>' +
    '<div class="gd" data-g="l"></div><div class="gd" data-g="r"></div>' +
    '<div class="pn" role="dialog" aria-label="Sayt muharriri">' +
    '<div class="hd"><b>✏️ Sayt muharriri</b><span class="pg"></span>' +
    '<button data-a="min" title="Yigʻish">–</button><button data-a="exit" title="Muharrirdan chiqish">✕</button></div>' +
    '<div class="bd">' +
    '<div class="seg"><button data-a="pick" class="on">🎯 Tanlash</button><button data-a="browse">👆 Saytni bosish</button></div>' +
    '<label class="chk"><input type="checkbox" data-a="client"> Mijoz koʻrinishi (yashirinlar koʻrinmaydi)</label>' +
    '<div class="cur"></div><div class="lostbox"></div><div class="msg"></div>' +
    '<div class="ft"><span class="cnt"></span><a href="admin.html#vebsayt" target="_blank" rel="noopener">Admin → Vebsayt ↗</a></div>' +
    '</div></div>' +
    '<div class="hdl" data-h="l" title="Kenglik: sudrang"></div><div class="hdl" data-h="r" title="Kenglik: sudrang"></div>';
  var $ = function (s) { return root.querySelector(s); };
  var hov = $(".hov"), selb = $(".sel"), tip = $(".tip"), pn = $(".pn");
  var hl = $('[data-h="l"]'), hr = $('[data-h="r"]'), gl = $('[data-g="l"]'), gr = $('[data-g="r"]');
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
    place(hov, editing && editing.text ? hovEl : mode === "pick" && !editing && hovEl !== cur ? hovEl : null);
    place(selb, cur);
    var showH = cur && cur.isConnected && mode === "pick" && !editing && sizable(cur);
    [hl, hr].forEach(function (h) { h.style.display = showH ? "block" : "none"; });
    if (showH) {
      var rc = cur.getBoundingClientRect(), y = rc.top + Math.min(rc.height, window.innerHeight) / 2;
      if (rc.top < 0 && rc.bottom > 0) y = Math.max(40, Math.min(window.innerHeight - 40, (Math.max(0, rc.top) + Math.min(window.innerHeight, rc.bottom)) / 2));
      hl.style.left = rc.left + "px"; hl.style.top = y + "px";
      hr.style.left = rc.right + "px"; hr.style.top = y + "px";
    }
    if (mode === "pick" && hovEl && !editing && hovEl !== cur) {
      var r = hovEl.getBoundingClientRect();
      tip.style.display = "block"; tip.textContent = labelOf(hovEl);
      tip.style.left = Math.max(4, r.left) + "px"; tip.style.top = Math.max(4, r.top - 22) + "px";
    } else if (!drag) tip.style.display = "none";
  }
  var raf = 0;
  function sched() { if (!raf) raf = requestAnimationFrame(function () { raf = 0; track(); }); }

  // ── element holati ──────────────────────────────────────────
  function why(el) {
    if (!el || el === document.body || el === document.documentElement) return "Bu butun sahifa";
    if (/^(SCRIPT|STYLE|INPUT|TEXTAREA|SELECT|IMG|CANVAS|VIDEO|IFRAME|svg|SVG)$/.test(el.nodeName)) return "Bu element matn emas";
    if (!K.tnodes(el).length) return "Bu elementda matn yoʻq";
    for (var p = el.parentElement; p && p !== document.body; p = p.parentElement)
      if (p.hasAttribute("data-kse-id") || p.hasAttribute("data-kse-tid")) return "Yuqoridagi blok allaqachon tahrirlangan: oʻsha blokni tahrirlang (⬆ Ota blok)";
    if (!simple(el) && !rowsOf(el).html) {
      if (el.querySelector("[data-kse-id],[data-kse-tid]")) return "Ichidagi qism alohida tahrirlangan: oʻsha qismni tahrirlang yoki uning tahririni bekor qiling (↩ Asl matn)";
      if (K.tnodes(el).length > TMAX) return "Blokda " + K.tnodes(el).length + " ta matn boʻlagi bor: kichikroq qismni tanlang (eng koʻpi " + TMAX + ")";
    }
    return "";
  }
  // Oddiy blok: faqat matn va b/i/a/span… Unda matn joyida (contenteditable) tahrirlanadi.
  // Boshqa bloklar (tugma, ikonka, forma, ⓘ, kod boshqaradigan qism) "matn boʻlaklari" rejimida: tuzilma tegilmaydi.
  var TMAX = 80;
  function simple(el) {
    if (rowsOf(el).text) return false;
    if (K.txt(el).length > 4000) return false;
    var all = el.querySelectorAll("*");
    for (var i = 0; i < all.length; i++) {
      var c = all[i];
      if (!OKTAG[c.nodeName]) return false;
      for (var j = 0; j < c.attributes.length; j++) {
        var a = c.attributes[j].name;
        if (!OKATTR.test(a) && !/^data-kse/.test(a)) return false;
      }
    }
    return true;
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
    var rs = rowsOf(cur), hidden = !!rs.hide, w = why(cur), tx = !w && !simple(cur) && !rs.html;
    var h = '<div class="lbl">' + esc(labelOf(cur)) + '<br><code>' + esc(short(K.path(cur), 90)) + '</code>' +
      (hidden ? '<br><b style="color:#c4622d">Saytda yashirin</b>' : "") +
      (rs.html || rs.text ? '<br><b style="color:#b08a00">Matni tahrirlangan</b>' : "") + '</div>';
    if (editing && editing.text) {
      h += '<div class="note">Bu blokda tugma, ikonka yoki kod boshqaradigan qism bor: uning tuzilmasi oʻzgarmaydi, faqat matn boʻlaklari. Sahifadagi matnni bossangiz, mos maydon tanlanadi.</div>' +
        '<div class="tl">' + editing.nodes.map(function (n, i) {
          var p = n.parentElement;
          return '<label class="ti"><span>' + (i + 1) + ' · &lt;' + esc(p ? tagName(p) : "?") + '&gt;</span>' +
            '<textarea data-ti="' + i + '" rows="1">' + esc(n.nodeValue.replace(/^\s+|\s+$/g, "")) + '</textarea></label>';
        }).join("") + '</div>' +
        '<div class="row"><button class="b p" data-a="save">💾 Saqlash</button><button class="b" data-a="cancel">Bekor</button></div>' +
        '<div class="note">Ctrl+Enter saqlaydi, Esc bekor qiladi.</div>';
    } else if (editing) {
      h += '<div class="row"><button class="b p" data-a="save">💾 Saqlash</button><button class="b" data-a="cancel">Bekor</button></div>' +
        '<div class="note">Matnni toʻgʻridan-toʻgʻri sahifada yozing. Ctrl+Enter saqlaydi, Esc bekor qiladi. Qalin/kursiv: Ctrl+B / Ctrl+I.</div>';
    } else {
      h += '<div class="row">' +
        '<button class="b" data-a="up"' + (cur.parentElement && cur.parentElement !== document.body && cur.parentElement !== document.documentElement ? "" : " disabled") + '>⬆ Ota blok</button>' +
        '<button class="b" data-a="edit"' + (w ? " disabled" : "") + '>✏️ Matnni tahrirlash</button>' +
        (hidden ? '<button class="b" data-a="show">👁 Koʻrsatish</button>' : '<button class="b w" data-a="hide">🙈 Yashirish</button>') +
        (rs.html || rs.text ? '<button class="b" data-a="revert">↩ Asl matn</button>' : "") +
        '<button class="b" data-a="desel">✕</button></div>' +
        (w ? '<div class="note">' + esc(w) + '</div>' : tx ? '<div class="note">Murakkab blok: matn boʻlaklari panelda alohida tahrirlanadi, tugma va ikonkalar joyida qoladi.</div>' : "") + sizePanel();
    }
    box.innerHTML = h; cv(box); cv($(".cnt"));
    if (editing && editing.text) {
      // Maydondagi matn alifbo.js oʻgirgan koʻrinishda boʻlmasin: yozilgan qiymat aynan saqlanadi
      [].forEach.call(box.querySelectorAll("textarea[data-ti]"), function (t) { t.value = editing.vals[+t.getAttribute("data-ti")]; grow(t); });
    }
  }
  function grow(t) { t.style.height = "auto"; t.style.height = Math.min(160, t.scrollHeight + 2) + "px"; }
  function renderLost() {
    var b = $(".lostbox");
    if (!lost.length) { b.innerHTML = ""; return; }
    b.innerHTML = '<div class="lost">⚠️ ' + lost.length + ' ta oʻzgarish bu sahifada topilmadi (sahifa manbasi oʻzgargan boʻlishi mumkin), saytda qoʻllanmayapti:' +
      lost.map(function (r) {
        return '<div>' + ({ hide: "Yashirish", style: "Oʻlcham" }[r.kind] || "Matn") + ": " + esc(short(r.label || r.sel, 60)) +
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
  function fail(e) {
    // 23514: bazada 'text' turi hali yoʻq (supabase/migrations/20261125_site_edits_text.sql qoʻllanmagan)
    if (e && e.code === "23514" && /kind_check/.test(e.message || "")) { msg("❌ Bazaga 20261125_site_edits_text.sql migratsiyasi hali qoʻllanmagan: murakkab blok matni saqlanmadi", "er"); return; }
    msg("❌ " + (e && (e.message || e.details) || e), "er");
  }
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
  // ── Matn boʻlaklari rejimi (kind 'text') ─────────────────────
  function foreign(n) {
    for (var p = n.parentNode; p && p.nodeType === 1; p = p.parentNode) {
      var lg = p.getAttribute("lang");
      if ((lg && !/^uz/i.test(lg)) || p.getAttribute("translate") === "no" || p.getAttribute("data-alifbo") === "off") return true;
    }
    return false;
  }
  function startText() {
    var el = cur;
    if (el.__kseGuard == null && !rowsOf(el).text) el.__kseGuard = K.guard(el);
    var nodes = K.tnodes(el);
    editing = { el: el, text: true, nodes: nodes, orig: [], ws: [], vals: [] };
    nodes.forEach(function (n, i) {
      var v = n.nodeValue, m = /^(\s*)([\s\S]*?)(\s*)$/.exec(v);
      editing.orig[i] = v; editing.ws[i] = [m[1], m[3]]; editing.vals[i] = m[2];
    });
    el.setAttribute("data-kse-editing", "");
    msg(""); render(); sched();
    var f = root.querySelector("textarea[data-ti]"); if (f) f.focus();
  }
  function focusNode(t) {
    if (!editing || !editing.text) return;
    for (var i = 0; i < editing.nodes.length; i++) if (t === editing.nodes[i].parentNode || (t.contains && t.contains(editing.nodes[i]))) {
      var f = root.querySelector('textarea[data-ti="' + i + '"]'); if (f) { f.focus(); f.scrollIntoView({ block: "nearest" }); } return;
    }
  }
  root.addEventListener("input", function (e) {
    var t = e.target; if (!editing || !editing.text || !t.hasAttribute || !t.hasAttribute("data-ti")) return;
    var i = +t.getAttribute("data-ti"), n = editing.nodes[i];
    editing.vals[i] = t.value; grow(t);
    n.nodeValue = editing.ws[i][0] + t.value + editing.ws[i][1];
    sched();
  });
  root.addEventListener("focusin", function (e) {
    var t = e.target; if (!editing || !editing.text || !t.hasAttribute || !t.hasAttribute("data-ti")) return;
    hovEl = editing.nodes[+t.getAttribute("data-ti")].parentElement; place(hov, hovEl);
  });
  function cancelText() {
    editing.nodes.forEach(function (n, i) { if (n.nodeValue !== editing.orig[i]) n.nodeValue = editing.orig[i]; });
    editing.el.removeAttribute("data-kse-editing"); editing = null; hovEl = null;
  }
  async function saveText() {
    var ed = editing, el = ed.el, old = rowsOf(el).text, prev = old ? (K.parseText(old.value) || { c: {} }).c : {};
    var c = {}, k;
    for (k in prev) c[k] = prev[k];
    for (var i = 0; i < ed.nodes.length; i++) {
      var v = ed.vals[i];
      if (!/\S/.test(v)) { msg("⚠️ " + (i + 1) + "-maydon boʻsh qoldi. Qismni olib tashlash uchun uni tanlab “Yashirish”dan foydalaning.", "er"); return; }
      var full = ed.ws[i][0] + v + ed.ws[i][1];
      if (full !== ed.orig[i]) c[i] = foreign(ed.nodes[i]) ? full : toOld(full);
    }
    if (!Object.keys(c).length) { msg("Oʻzgarish yoʻq"); return; }
    var value = JSON.stringify({ n: ed.nodes.length, c: c });
    if (value.length > 20000) { msg("⚠️ Matn juda uzun: kichikroq qismni tanlang", "er"); return; }
    try {
      var r = await write("text", el, { value: value, status: "active" });
      el.removeAttribute("data-kse-editing"); editing = null; hovEl = null;
      setRow(el, r);
      if (!rows.some(function (x) { return x.id === r.id; })) rows.push(r); else rows = rows.map(function (x) { return x.id === r.id ? r : x; });
      K.textApply(el, r.value);
      el.setAttribute("data-kse-tid", r.id);
      msg("✅ Saqlandi. Saytda bir necha daqiqada (yangi tashrifda) koʻrinadi.", "ok");
    } catch (e) { fail(e); }
    render(); sched();
  }
  function startEdit() {
    var el = cur; if (!el || why(el)) return;
    if (!simple(el) && !rowsOf(el).html) { startText(); return; }
    if (el.__kseGuard == null && !rowsOf(el).html) el.__kseGuard = K.guard(el);
    editing = { el: el, html: el.innerHTML };
    // ⓘ belgisi tasodifan oʻchmasin: u tahrirlanmaydi, saqlanganda joyida qoladi
    [].forEach.call(el.querySelectorAll(".kl-i"), function (x) { x.setAttribute("contenteditable", "false"); });
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
    [].forEach.call(el.querySelectorAll("[contenteditable]"), function (x) { x.removeAttribute("contenteditable"); });
    editing = null;
  }
  function cancelEdit() {
    if (!editing) return;
    if (editing.text) { cancelText(); msg(""); render(); sched(); return; }
    editing.el.innerHTML = editing.html;
    endEdit(); msg(""); render(); sched();
  }
  async function saveEdit() {
    if (!editing) return;
    if (editing.text) return saveText();
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
    var el = cur, o = el && (rowsOf(el).html || rowsOf(el).text);
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

  // ── Oʻlcham: shrift va kenglik (kind 'style') ─────────────────────
  var FS_STEP = 0.05, SNAP = 10, stTimer = 0;
  function sizable(el) { return el && el !== document.body && el !== document.documentElement && !inHost(el) && el.nodeType === 1 && !/^(SCRIPT|STYLE|BR|HR)$/.test(el.nodeName); }
  function curSt(el) { var r = rowsOf(el).style; return K.parseStyle(el.__kseDraft || (r ? r.value : {})); }
  function maxW(el) {
    var p = el.parentElement; if (!p) return window.innerWidth;
    var cs = getComputedStyle(p);
    return Math.max(K.W_MIN, p.clientWidth - (parseFloat(cs.paddingLeft) || 0) - (parseFloat(cs.paddingRight) || 0));
  }
  function sizePanel() {
    if (!cur || !sizable(cur)) return "";
    if (cur.__kstyle && cur.__kstyle.by) return '<div class="sz"><div class="szh">Oʻlcham</div><div class="note">Bu blok qoʻshnisi bilan simmetrik oʻlchanadi.</div><div class="row"><button class="b" data-a="main">Asosiy blokni tanlash</button></div></div>';
    var o = curSt(cur), np = K.peers(cur).length, mw = Math.round(maxW(cur));
    var wTxt = o.w ? o.w + " px" : "Avto", fTxt = Math.round((o.fs || 1) * 100) + "%";
    var has = !!rowsOf(cur).style;
    return '<div class="sz"><div class="szh">Oʻlcham</div>' +
      '<div class="szr"><span>Shrift</span><button class="b" data-a="fs-" title="Kichikroq">A−</button><span class="v">' + fTxt + '</span><button class="b" data-a="fs+" title="Kattaroq">A+</button><button class="b s" data-a="fs0" title="Asl oʻlcham">100%</button></div>' +
      '<div class="szr"><span>Kenglik</span><button class="b" data-a="w-">−</button><span class="v">' + wTxt + '</span><button class="b" data-a="w+">+</button><button class="b s" data-a="wauto" title="Asl kenglik">Avto</button></div>' +
      (np ? '<label class="chk"><input type="checkbox" data-a="sym"' + (o.sym !== false ? " checked" : "") + '> Qoʻshni ' + np + ' ta blok ham shu kenglikda (simmetriya)</label>' : "") +
      '<div class="note">Kenglikni blok chetidagi tutqichni sudrab ham berasiz. Blok markazda turadi; 25, 33, 50, 66, 75, 100% va qoʻshni bloklar kengligiga yopishadi. Eng koʻpi ' + mw + ' px.</div>' +
      (has ? '<div class="row"><button class="b" data-a="stoff">↩ Asl oʻlcham</button></div>' : "") + '</div>';
  }
  function draftOf(el) { var o = curSt(el); if (o.sym == null && K.peers(el).length) o.sym = true; return o; }
  function setSt(ch, now) {
    var el = cur; if (!el) return;
    var o = draftOf(el);
    for (var k in ch) o[k] = ch[k];
    if (!o.w) delete o.w; if (!o.fs || Math.abs(o.fs - 1) < 0.001) delete o.fs;
    el.__kseDraft = o;
    K.style(el, o);
    var row = rowsOf(el).style; if (row) row.value = JSON.stringify(K.parseStyle(o));
    render(); sched();
    clearTimeout(stTimer);
    stTimer = setTimeout(function () { saveSt(el, o); }, now ? 0 : 700);
  }
  async function saveSt(el, o) {
    var v = K.parseStyle(o), row = rowsOf(el).style;
    try {
      if (!v.fs && !v.w) {
        if (row) {
          var u = await sb.from("site_edits").update({ status: "off" }).eq("id", row.id);
          if (u.error) throw u.error;
          dropCache(); forget(row); delete el.__kse.style;
        }
        msg("✅ Asl oʻlcham", "ok");
      } else {
        if (el.__kseGuard == null) el.__kseGuard = K.guard(el);
        var r = await write("style", el, { value: JSON.stringify(v), status: "active" });
        setRow(el, r);
        if (!rows.some(function (x) { return x.id === r.id; })) rows.push(r); else rows = rows.map(function (x) { return x.id === r.id ? r : x; });
        msg("✅ Oʻlcham saqlandi. Saytda bir necha daqiqada (yangi tashrifda) koʻrinadi.", "ok");
      }
    } catch (e) { fail(e); }
    el.__kseDraft = null;
    render(); sched();
  }
  function stepFs(d) {
    var f = (draftOf(cur).fs || 1) + d * FS_STEP;
    f = Math.min(K.FS_LIM[1], Math.max(K.FS_LIM[0], Math.round(f * 100) / 100));
    setSt({ fs: f });
  }
  function stepW(d) {
    var mw = maxW(cur), w = draftOf(cur).w || Math.round(cur.getBoundingClientRect().width);
    var steps = [0.25, 1 / 3, 0.5, 2 / 3, 0.75, 1].map(function (x) { return Math.round(mw * x); });
    var nx = d > 0 ? steps.filter(function (x) { return x > w + 2; })[0] : steps.filter(function (x) { return x < w - 2; }).pop();
    if (nx == null) return;
    setSt({ w: nx >= mw ? 0 : nx });
  }
  function styleOff() { if (cur && confirm("Bu blok asl oʻlchamiga qaytarilsinmi?")) setSt({ fs: 1, w: 0 }, true); }

  // Tutqichni sudrash: kenglik = 2 × |sichqoncha − markaz| (blok markazda qoladi)
  var drag = null;
  function snapW(w, mw) {
    var c = [0.25, 1 / 3, 0.5, 2 / 3, 0.75, 1].map(function (x) { return { w: mw * x, t: Math.round(x * 100) + "%" }; });
    var p = cur && cur.parentElement;
    if (p) [].forEach.call(p.children, function (x) { if (x !== cur && !(cur.__kstyle && cur.__kstyle.peers.indexOf(x) >= 0)) { var r = x.getBoundingClientRect(); if (r.width > 40) c.push({ w: r.width, t: "qoʻshni" }); } });
    var best = null;
    c.forEach(function (x) { var dd = Math.abs(x.w - w); if (dd <= SNAP && (!best || dd < best.d)) best = { d: dd, w: x.w, t: x.t }; });
    return best ? { w: Math.round(best.w), t: best.t } : { w: Math.round(w), t: Math.round(w / mw * 100) + "%" };
  }
  function down(e) {
    if (!cur) return;
    e.preventDefault(); e.stopPropagation();
    var h = e.currentTarget; h.classList.add("on");
    try { h.setPointerCapture(e.pointerId); } catch (er) {}
    var rc = cur.getBoundingClientRect();
    drag = { h: h, cx: rc.left + rc.width / 2, mw: maxW(cur), o: draftOf(cur) };
  }
  function move(e) {
    if (!drag) return;
    var w = Math.min(drag.mw, Math.max(K.W_MIN, 2 * Math.abs(e.clientX - drag.cx)));
    var sn = snapW(w, drag.mw);
    var o = drag.o; o.w = sn.w >= drag.mw - 1 ? 0 : sn.w;
    K.style(cur, o); drag.w = o.w;
    var rc = cur.getBoundingClientRect();
    gl.style.display = gr.style.display = "block";
    [gl, gr].forEach(function (g, i) { g.style.left = (i ? rc.right : rc.left) + "px"; g.style.top = "0px"; g.style.height = window.innerHeight + "px"; });
    tip.style.display = "block"; tip.textContent = (o.w ? sn.w + " px · " + sn.t : "Avto (toʻliq)");
    tip.style.left = Math.max(4, drag.cx - 50) + "px"; tip.style.top = Math.max(4, rc.top - 24) + "px";
    sched();
  }
  function up() {
    if (!drag) return;
    var d = drag; drag = null; d.h.classList.remove("on");
    gl.style.display = gr.style.display = "none"; tip.style.display = "none";
    if (d.w != null) setSt({ w: d.w, sym: d.o.sym }, true);
  }
  [hl, hr].forEach(function (h) { h.addEventListener("pointerdown", down); h.addEventListener("pointermove", move); h.addEventListener("pointerup", up); h.addEventListener("pointercancel", up); });

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
    else if (a === "fs-" || a === "fs+") stepFs(a === "fs+" ? 1 : -1);
    else if (a === "fs0") setSt({ fs: 1 });
    else if (a === "w-" || a === "w+") stepW(a === "w+" ? 1 : -1);
    else if (a === "wauto") setSt({ w: 0 });
    else if (a === "sym") setSt({ sym: b.checked });
    else if (a === "main") { var m = cur && cur.__kstyle && cur.__kstyle.by; if (m) select(m); }
    else if (a === "stoff") styleOff();
  });
  function guardEv(e) {
    if (inHost(e.target)) return;
    if (editing) {
      // havola ochilmasin; <summary> ichidagi sarlavhada bosish ⓘ oynasini ochib-yopmasin
      if (editing.text) {
        // Matn boʻlaklari rejimi: sahifadagi matnni bosish mos maydonni tanlaydi, sayt kodi ishlamaydi
        e.preventDefault(); e.stopPropagation(); e.stopImmediatePropagation();
        if (e.type === "click" && editing.el.contains(e.target)) focusNode(e.target);
        return;
      }
      if (editing.el.contains(e.target)) { if (e.target.closest && e.target.closest("a, summary")) e.preventDefault(); return; }
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
    // Panel maydonlarida yozilgan tugmalar sahifaga (←/→ sahifa almashtirish va b.) yetib bormasin
    if (inHost(e.target)) e.stopPropagation();
    if (editing) {
      if (e.key === "Escape") { e.preventDefault(); cancelEdit(); }
      else if (e.key === "Enter" && (e.ctrlKey || e.metaKey)) { e.preventDefault(); saveEdit(); }
      // <summary> ichida boʻsh joy va Enter brauzerda ⓘ oynasini ochadi: oʻrniga matn yozamiz
      else if (!editing.text && (e.key === " " || e.key === "Enter") && editing.el.closest("summary") && editing.el.contains(e.target)) {
        e.preventDefault();
        if (e.key === " ") document.execCommand("insertText", false, " ");
        else document.execCommand("insertLineBreak");
      }
      return;
    }
    if (e.key === "Escape" && cur) { cur = null; render(); sched(); }
  }, true);
  window.addEventListener("beforeunload", function (e) { if (editing) { e.preventDefault(); e.returnValue = ""; } });

  // ── ishga tushirish ─────────────────────────────────────────
  function applyAll() {
    lost = [];
    rows.forEach(function (r) {
      var el = (r.kind === "html" && document.querySelector('[data-kse-id="' + r.id + '"]')) || (r.kind === "text" && document.querySelector('[data-kse-tid="' + r.id + '"]')) || K.locate(r);
      if (!el) { lost.push(r); return; }
      if (r.kind === "text") {
        if (el.getAttribute("data-kse-tid") !== String(r.id) && !K.textApply(el, r.value)) { lost.push(r); return; }
        el.__kseGuard = r.guard; el.setAttribute("data-kse-tid", r.id);
      }
      setRow(el, r);
      if (r.kind === "hide") el.setAttribute("data-kse-hidden", "");
      else if (r.kind === "style") K.style(el, r.value);
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
