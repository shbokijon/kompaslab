// AVTOMATIK: js/kompas-ui.js dagi <site-edits> bloki nusxasi. Qoʻlda tahrirlamang:
// python3 tools/site/site_edits_js.py
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
