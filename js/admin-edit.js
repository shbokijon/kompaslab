// KOMPAS LAB — koʻrinma tahrir rejimi (2026-11-06).
// Ochish: admin.html → "Sahifani tahrirlash" (sahifa manzili oxiriga ?edit=1; kompas-ui.js shu faylni yuklaydi).
// Sinov: &dry=1 — bazaga yozmaydi. Faqat fn_is_admin() true qaytarsa ishlaydi.
// Tahrir text_fixes qatoriga (eski → yangi) aylanadi: kompas-ui.js, fn_paid_page va tools/site/apply_fixes.py oʻzgarmaydi.
// Cheklov: bitta matn tugunini tahrirlaydi; qalin/havola/blok qoʻshish va oʻchirish yoʻq; pullik modul (-o.html) hozircha yoʻq.
(function () {
  if (!/[?&]edit=1/.test(location.search)) return;
  var sb = window.supabase;
  var DRY = /[?&]dry=1/.test(location.search);
  var file = location.pathname.split("/").pop() || "index.html";
  if (!/\.html?$/.test(file)) file += ".html";
  var BLOCK = "p,li,h1,h2,h3,h4,td,th,blockquote,figcaption";
  var NOEDIT = "nav,footer,header.top,script,style,noscript,template,textarea,input,select,button,a,label,summary,.kl-ed-bar,[data-noedit]";
  var edits = new Map(); // element -> { snap: [matn tugunlari qiymati], skel: string }

  // Saytdagi matn yangi alifboda boʻlishi mumkin; text_fixes manba alifbosida yoziladi (admin.html fxNorm bilan bir xil)
  function norm(s) {
    return (s || "").replace(/\r/g, "").trim()
      .replace(/Ö/g, "Oʻ").replace(/ö/g, "oʻ").replace(/Ğ/g, "Gʻ").replace(/ğ/g, "gʻ")
      .replace(/Ş/g, "Sh").replace(/ş/g, "sh").replace(/Ç/g, "Ch").replace(/ç/g, "ch")
      .replace(/([oOgG])['‘’`ʼ](?=[A-Za-z])/g, "$1ʻ")
      .replace(/([A-Za-z])['‘’`](?=[A-Za-z])/g, "$1ʼ");
  }
  function nodes(el) {
    var w = document.createTreeWalker(el, 4, null), a = [], n;
    while ((n = w.nextNode())) a.push(n);
    return a;
  }
  function skel(el) {
    return Array.prototype.map.call(el.querySelectorAll("*"), function (e) { return e.nodeName; }).join(",");
  }
  function count(hay, needle) { var n = 0, i = 0; while ((i = hay.indexOf(needle, i)) !== -1) { n++; i += needle.length; } return n; }

  function editable(el) {
    if (el.closest(NOEDIT)) return false;
    if (el.querySelector(BLOCK)) return false;          // ichida boshqa blok bor — ichkarisi tahrirlanadi
    return el.textContent.trim().length >= 3;
  }
  function ok(el) { var e = edits.get(el); return e && e.skel === skel(el) && e.snap.length === nodes(el).length; }

  // Oʻzgargan matn tugunlari -> [{old,new}]; tuzilmasi buzilgan elementlar -> broken
  function collect() {
    var rows = [], broken = 0;
    edits.forEach(function (e, el) {
      var ns = nodes(el);
      if (e.skel !== skel(el) || e.snap.length !== ns.length) { broken++; return; }
      ns.forEach(function (n, i) { if (n.nodeValue !== e.snap[i]) rows.push({ old: e.snap[i], neu: n.nodeValue, el: el }); });
    });
    return { rows: rows, broken: broken };
  }

  var bar = document.createElement("div");
  bar.className = "kl-ed-bar";
  bar.setAttribute("style", "position:fixed;left:0;right:0;bottom:0;z-index:99999;background:#2d4a3e;color:#f4f3ef;font:600 13px Outfit,system-ui,sans-serif;padding:10px 14px;display:flex;gap:10px;align-items:center;flex-wrap:wrap");
  bar.innerHTML = '<span>✏️ Tahrir rejimi' + (DRY ? " (sinov)" : "") + '</span><span id="kl-ed-n" style="opacity:.85">Matnga bosib yozing (tablarni oching)</span>' +
    '<button type="button" id="kl-ed-save" style="margin-left:auto;background:#c4622d;color:#fff;border:0;border-radius:8px;padding:8px 14px;font:inherit">Saqlash</button>' +
    '<button type="button" id="kl-ed-off" style="background:transparent;color:#f4f3ef;border:1px solid #f4f3ef;border-radius:8px;padding:8px 12px;font:inherit">Chiqish</button>';
  var msg = bar.querySelector("#kl-ed-n");

  function refresh() {
    var c = collect();
    msg.textContent = c.rows.length + " ta oʻzgarish" + (c.broken ? " · " + c.broken + " ta blokning tuzilmasi buzilgan (saqlanmaydi)" : "");
  }
  function arm(el) {
    el.setAttribute("contenteditable", "plaintext-only");
    if (el.contentEditable !== "plaintext-only") el.setAttribute("contenteditable", "true");
    el.style.outline = "1px dashed rgba(196,98,45,.45)";
    el.style.outlineOffset = "2px";
    el.addEventListener("focus", function () { if (!edits.has(el)) edits.set(el, { snap: nodes(el).map(function (n) { return n.nodeValue; }), skel: skel(el) }); });
    el.addEventListener("keydown", function (ev) { if (ev.key === "Enter") ev.preventDefault(); });       // yangi paragraf qoʻshilmaydi
    el.addEventListener("paste", function (ev) { ev.preventDefault(); document.execCommand("insertText", false, ((ev.clipboardData || window.clipboardData).getData("text") || "").replace(/\s+/g, " ")); });
    el.addEventListener("input", function () { el.style.outline = ok(el) ? "1px solid #c9a84c" : "2px solid #b3261e"; refresh(); });
  }
  function save() {
    var c = collect(), body = [], skipped = [], dup = 0;
    var all = nodes(document.body).filter(function (n) { return !(n.parentNode && n.parentNode.closest && n.parentNode.closest("script,style,.kl-ed-bar")); });
    c.rows.forEach(function (r) {
      var o = norm(r.old), n = norm(r.neu);
      if (o.length < 2) { skipped.push("juda qisqa: " + r.old); return; }
      if (o === n) return;
      var same = all.reduce(function (s, t) { return s + count(t.nodeValue, r.old); }, 0) + 1;
      if (same > 1) dup++;
      body.push({ page: file, old_text: o, new_text: n, note: "koʻrinma tahrir" + (same > 1 ? " (sahifada " + same + " joyda)" : "") });
    });
    if (!body.length) { msg.textContent = "Saqlanadigan oʻzgarish yoʻq" + (skipped.length ? " · " + skipped.join("; ") : ""); return; }
    window.__KFX = body;
    if (DRY) { msg.textContent = "Sinov: " + body.length + " ta qator tayyor (bazaga yozilmadi)"; return; }
    sb.from("text_fixes").insert(body).then(function (r) {
      msg.textContent = r && r.error ? "Xatolik: " + r.error.message : "Saqlandi: " + body.length + " ta" + (dup ? " (" + dup + " tasi sahifada takrorlanadi, hammasi tuzaladi)" : "") + ". Saytda ≤10 daqiqada koʻrinadi. Admin panelda “Yangilash” ni bosing";
    });
  }

  function start() {
    document.body.appendChild(bar);
    document.querySelectorAll(BLOCK).forEach(function (el) { if (editable(el)) arm(el); });
    bar.querySelector("#kl-ed-save").addEventListener("click", save);
    bar.querySelector("#kl-ed-off").addEventListener("click", function () { location.search = location.search.replace(/[?&]edit=1/, "").replace(/^&/, "?"); });
    window.__KED = { armed: document.querySelectorAll("[contenteditable]").length, collect: collect };
  }
  function boot(n) {
    sb = window.supabase;
    if (!sb || typeof sb.rpc !== "function") { if (n < 25) setTimeout(function () { boot(n + 1); }, 160); return; }
    sb.rpc("fn_is_admin").then(function (r) {
      if (!r || r.error || r.data !== true) return;
      if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start); else start();
    });
  }
  boot(0);
})();
