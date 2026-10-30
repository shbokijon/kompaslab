// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — suggest.js (2026-10-30)
//  Matn maydonlarida avtomatik taklif: universitet, dastur, davlat, stipendiya,
//  shahar, til, sertifikat, soha. Maydon turi yorligʻi (label) yoki placeholder
//  matnidan aniqlanadi; aniq belgilash: data-suggest="uni|prog|schol|prog-schol|
//  country|country-en-multi|city|city-country|lang|test|field|degree|off".
//  Maʼlumot: data/suggest/lists.json (kichik) va universities.json (birinchi
//  kerak boʻlganda yuklanadi). Manbalar: tools/suggest/build_suggest.py.
//  Talaba tanlagan qiymatlar shu qurilmada eslab qolinadi (kompas_suggest_v1).
//  Hech narsa majburiy emas: roʻyxatda yoʻq qiymatni oʻzi yozaveradi.
// ═══════════════════════════════════════════════════════════════
(function () {
  "use strict";
  if (window.KSuggest) return;
  var script = document.currentScript;
  var BASE = "data/suggest/";
  try { if (script && script.src) BASE = new URL("../data/suggest/", script.src).href; } catch (e) {}
  var HKEY = "kompas_suggest_v1";

  // ── Yordamchilar ──
  function norm(s) {
    return String(s || "").toLowerCase()
      .replace(/ş/g, "sh").replace(/ç/g, "ch")
      .normalize("NFD").replace(/[̀-ͯ]/g, "")
      .replace(/[ʻʼ'‘’`]/g, "").replace(/\s+/g, " ").trim();
  }
  function uz(t) { // oʻzbekcha matnni foydalanuvchi alifbosida koʻrsatish
    var A = window.KAlifbo;
    return A && A.mode !== "eski" && A.conv ? A.conv(t) : t;
  }
  function getJSON(name) {
    return fetch(BASE + name, { credentials: "same-origin" }).then(function (r) {
      if (!r.ok) throw new Error(r.status);
      return r.json();
    });
  }
  var lists = null, listsP = null, unis = null, unisP = null;
  function loadLists() {
    if (lists) return Promise.resolve(lists);
    if (!listsP) listsP = getJSON("lists.json").then(function (d) { lists = prep(d); return lists; });
    return listsP;
  }
  function loadUnis() {
    if (unis) return Promise.resolve(unis);
    if (!unisP) unisP = Promise.all([getJSON("universities.json"), loadLists()]).then(function (r) {
      unis = r[0].map(function (u) { return { v: u[0], cc: u[1], n: norm(u[0]) }; });
      return unis;
    });
    return unisP;
  }
  function prep(d) {
    var c = d.countries, C = [];
    Object.keys(c).forEach(function (k) { C.push({ cc: k, uz: c[k][0], en: c[k][1], n: norm(c[k][0] + " " + c[k][1]) }); });
    // qoʻshimcha nomlar (koʻp yoziladigan)
    var alias = { GB: "uk angliya britain england", US: "usa aqsh amerika", KR: "korea koreya", AE: "uae baa", NL: "gollandiya holland", DE: "olmoniya" };
    C.forEach(function (x) { if (alias[x.cc]) x.n += " " + alias[x.cc]; });
    d._countries = C;
    d._cByCode = c;
    var subj = [];
    var def = { S: "MSc", A: "MA", B: "MSc" };
    var special = { "Law": "LLM", "Public Administration": "MPA", "Social Work": "MA", "Education": "MA", "Architecture": "MArch" };
    Object.keys(d.subjects).forEach(function (g) {
      d.subjects[g].forEach(function (s) { subj.push({ s: s, d: special[s] || def[g], n: norm(s) }); });
    });
    d._subjects = subj;
    d._schol = d.scholarships.map(function (x) { return { v: x[0], cc: x[1], n: norm(x[0]) }; });
    function simple(a) { return a.map(function (v) { return { v: v, n: norm(v) }; }); }
    d._langs = simple(d.languages); d._tests = simple(d.tests); d._cities = simple(d.cities_uz); d._fields = simple(d.fields_uz);
    return d;
  }
  function cname(cc) { var c = lists && lists._cByCode[cc]; return c ? uz(c[0]) : ""; }

  // Moslik: soʻzlar boshi > ichida; hamma soʻzlar boʻlishi shart
  function score(n, q, qt) {
    if (n === q) return 0;
    for (var i = 0; i < qt.length; i++) if (n.indexOf(qt[i]) < 0) return -1;
    if ((" " + n).indexOf(" " + qt[0]) >= 0) return 1;   // soʻz boshidan
    return 2;                                             // soʻz ichidan
  }
  function rank(arr, q, key, limit) {
    var qt = q.split(" ").filter(Boolean), out = [];
    for (var i = 0; i < arr.length; i++) {
      var s = score(arr[i][key || "n"], q, qt);
      if (s >= 0) out.push([s, arr[i]]);
    }
    out.sort(function (a, b) { return a[0] - b[0] || a[1].n.length - b[1].n.length; });
    return out.slice(0, limit || 8).map(function (x) { return x[1]; });
  }

  // ── Tarix (shu qurilmada) ──
  function hist() { try { return JSON.parse(localStorage.getItem(HKEY) || "{}") || {}; } catch (e) { return {}; } }
  function remember(kind, v) {
    v = String(v || "").trim(); if (v.length < 2 || v.length > 160) return;
    var h = hist(), a = (h[kind] || []).filter(function (x) { return x !== v; });
    a.unshift(v); h[kind] = a.slice(0, 25);
    try { localStorage.setItem(HKEY, JSON.stringify(h)); } catch (e) {}
  }

  // ── Maydon turini aniqlash ──
  function labelOf(el) {
    var t = "";
    if (el.id) { var l = document.querySelector('label[for="' + el.id + '"]'); if (l) t = l.textContent; }
    if (!t) { var p = el.closest("label"); if (p) t = p.textContent; }
    if (!t) {
      var prev = el.previousElementSibling;
      for (var i = 0; i < 2 && prev && !t; i++, prev = prev.previousElementSibling) if (/^(LABEL|SPAN|B|STRONG|DIV)$/.test(prev.nodeName) && prev.textContent.length < 80) t = prev.textContent;
    }
    return norm(t);
  }
  function kindOf(el) {
    var ds = el.getAttribute("data-suggest");
    if (ds) return ds === "off" ? "" : ds;
    if (el.nodeName !== "INPUT" || !/^(text|search|)$/i.test(el.getAttribute("type") || "")) return "";
    var L = labelOf(el), P = norm(el.getAttribute("placeholder"));
    if (/https?:|doi|@/.test(P)) return "";
    if (/universitet va dastur|universitet|university/.test(L) || (!L && /^university/.test(P))) return "uni";
    if (/^dastur yoki stipendiya/.test(L)) return "prog-schol";
    if (/^dastur|programme/.test(L)) return "prog";
    if (/stipendiya|scholarship/.test(L)) return "schol";
    if (/mamlakatlar|target countries/.test(L)) return "country-en-multi";
    if (/shahar, mamlakat|city, country/.test(L)) return "city-country";
    if (/^davlat|^mamlakat|^country/.test(L)) return "country";
    if (/^shahar|^city/.test(L)) return "city";
    if (/^\d-til|^til\b|^language/.test(L)) return "lang";
    if (/sertifikat|certificate/.test(L)) return "test";
    if (/daraja va yonalish|degree/.test(L)) return "degree";
    if (/^soha/.test(P) || /^soha\b/.test(L)) return "field";
    return "";
  }

  // ── Takliflar ──
  function suggest(kind, raw) {
    var q = norm(raw);
    var h = (hist()[kind] || []).filter(function (v) { return !q || norm(v).indexOf(q) >= 0; }).slice(0, 3)
      .map(function (v) { return { v: v, sub: "avval yozgansiz", mine: 1 }; });
    function done(items, note) {
      var seen = {}; var out = [];
      h.concat(items).forEach(function (x) { var k = x.v + "|" + (x.mine ? "" : x.sub || ""); if (!seen[k] && !(x.mine === undefined && seen[x.v + "|"])) { seen[k] = 1; out.push(x); } });
      return { items: out.slice(0, 8), note: note };
    }
    if (!q && !h.length) return Promise.resolve({ items: [] });
    return loadLists().then(function (L) {
      switch (kind) {
        case "uni":
          if (q.length < 2) return done([]);
          return loadUnis().then(function (U) {
            return done(rank(U, q).map(function (u) { return { v: u.v, sub: cname(u.cc), cc: u.cc }; }),
              "Ochiq roʻyxat (Hipo, MIT). Topilmasa, nomini oʻzingiz yozing.");
          });
        case "prog": case "degree": {
          var m = /^(msc|ma|mres|meng|mphil|mba|llm|mph|ms|mpa|med|march|phd|bsc|ba|beng)\b\.?\s*(in\s+)?/.exec(q);
          var deg = m ? L.degrees.concat(["BSc", "BA", "BEng"]).filter(function (d) { return d.toLowerCase() === m[1]; })[0] : "";
          var qq = m ? q.slice(m[0].length) : q;
          if (qq.length < 2) return done([]);
          var r = rank(L._subjects, qq).map(function (s) {
            var d = deg || (kind === "degree" ? "BSc" : s.d);
            return { v: kind === "degree" ? d + " in " + s.s : d + " " + s.s, sub: "" };
          });
          return done(r, kind === "degree" ? "" : "Namuna nom. Aniq nomini universitet sahifasidan oling.");
        }
        case "prog-schol": {
          var s1 = rank(L._schol, q, "n", 5).map(function (x) { return { v: x.v, sub: x.cc ? cname(x.cc) : "stipendiya" }; });
          return done(s1);
        }
        case "schol":
          return done(rank(L._schol, q).map(function (x) { return { v: x.v, sub: x.cc ? cname(x.cc) : "" }; }));
        case "country":
          return done(rank(L._countries, q).map(function (c) { return { v: uz(c.uz), sub: c.en }; }));
        case "country-en-multi": {
          var parts = raw.split(","), last = norm(parts[parts.length - 1]);
          if (!last) return done([]);
          var head = parts.slice(0, -1).map(function (x) { return x.trim(); }).filter(Boolean);
          return done(rank(L._countries, last).map(function (c) { return { v: head.concat([c.en]).join(", ") + ", ", label: c.en, sub: uz(c.uz) }; }));
        }
        case "city":
          return done(rank(L._cities, q).map(function (c) { return { v: c.v, sub: "" }; }));
        case "city-country":
          return done(rank(L._cities, q).map(function (c) { return { v: c.v + ", Uzbekistan", sub: "" }; }));
        case "lang":
          return done(rank(L._langs, q).map(function (c) { return { v: c.v, sub: "" }; }));
        case "test":
          return done(rank(L._tests, q).map(function (c) { return { v: c.v, sub: "" }; }));
        case "field":
          return done(rank(L._fields, q).map(function (c) { return { v: uz(c.v), sub: "" }; }));
      }
      return done([]);
    });
  }

  // ── Koʻrinish ──
  var css = ".ks-box{position:absolute;z-index:400;background:var(--surface,#fffefb);color:var(--text,#1a2e26);border:1px solid var(--border,#e2ded3);border-radius:12px;box-shadow:0 12px 32px rgba(26,46,38,.16);max-height:320px;overflow:auto;padding:4px;font:inherit;font-size:15px}" +
    ".ks-box[hidden]{display:none}.ks-it{display:flex;justify-content:space-between;gap:10px;align-items:baseline;padding:9px 10px;border-radius:8px;cursor:pointer;line-height:1.3}" +
    ".ks-it small{color:var(--muted,#5f7169);font-size:12.5px;white-space:nowrap}.ks-it[aria-selected=true],.ks-it:hover{background:var(--accent-lit,#e8f0ec)}" +
    ".ks-it.mine small{color:var(--accent2,#c4622d)}.ks-note{padding:6px 10px 4px;color:var(--muted,#5f7169);font-size:12px;border-top:1px solid var(--border,#e2ded3);margin-top:4px}" +
    "@media (max-width:480px){.ks-box{font-size:16px}.ks-it{padding:11px 10px}}";
  var st = document.createElement("style"); st.textContent = css; (document.head || document.documentElement).appendChild(st);

  var box = document.createElement("div");
  box.className = "ks-box"; box.hidden = true;
  box.setAttribute("role", "listbox"); box.setAttribute("translate", "no"); box.id = "ks-list";
  var cur = null, items = [], active = -1, seq = 0;

  function place() {
    if (!cur) return;
    var r = cur.getBoundingClientRect(), h = Math.min(box.scrollHeight || 320, 320);
    var below = window.innerHeight - r.bottom, above = r.top;
    var up = below < h + 12 && above > below;   // pastda joy boʻlmasa, yuqoriga ochiladi
    box.style.left = (r.left + window.scrollX) + "px";
    box.style.top = (up ? r.top + window.scrollY - h - 4 : r.bottom + window.scrollY + 4) + "px";
    box.style.width = Math.max(r.width, 220) + "px";
  }
  function close() { box.hidden = true; active = -1; if (cur) cur.setAttribute("aria-expanded", "false"); }
  function render(res) {
    items = res.items || [];
    box.innerHTML = "";
    if (!items.length) { close(); return; }
    items.forEach(function (it, i) {
      var d = document.createElement("div");
      d.className = "ks-it" + (it.mine ? " mine" : "");
      d.setAttribute("role", "option"); d.id = "ks-o" + i;
      var b = document.createElement("span"); b.textContent = it.label || it.v; d.appendChild(b);
      if (it.sub) { var s = document.createElement("small"); s.textContent = it.mine ? uz(it.sub) : it.sub; d.appendChild(s); }
      d.addEventListener("mousedown", function (e) { e.preventDefault(); pick(i); });
      box.appendChild(d);
    });
    if (res.note) { var n = document.createElement("div"); n.className = "ks-note"; n.textContent = uz(res.note); box.appendChild(n); }
    if (!box.parentNode) document.body.appendChild(box);
    active = -1; box.hidden = false; place();
    cur.setAttribute("aria-expanded", "true");
  }
  function hl(i) {
    var opts = box.querySelectorAll(".ks-it");
    opts.forEach(function (o, k) { o.setAttribute("aria-selected", k === i ? "true" : "false"); });
    active = i;
    if (opts[i]) { opts[i].scrollIntoView({ block: "nearest" }); cur.setAttribute("aria-activedescendant", opts[i].id); }
  }
  function fire(el) {
    el.dispatchEvent(new Event("input", { bubbles: true }));
    el.dispatchEvent(new Event("change", { bubbles: true }));
  }
  function pick(i) {
    var it = items[i]; if (!it || !cur) return;
    var el = cur;
    el.value = it.v; fire(el);
    remember(el._ksKind, it.label ? it.label : it.v);
    if (el._ksKind === "uni" && it.cc) companion(el, it.cc);
    close();
    if (/,\s$/.test(it.v)) { el.focus(); update(el); }
  }
  // Universitet tanlansa: shu formadagi boʻsh "Davlat" maydonini toʻldirish
  function companion(el, cc) {
    var p = el.parentNode;
    for (var up = 0; up < 4 && p && p !== document.body; up++, p = p.parentNode) {
      var ins = p.querySelectorAll ? p.querySelectorAll("input") : [];
      for (var k = 0; k < ins.length; k++) {
        var f = ins[k];
        if (f === el || f.value) continue;
        if (kindOf(f) === "country") { f.value = cname(cc); fire(f); return; }
      }
    }
  }
  function update(el) {
    var my = ++seq;
    suggest(el._ksKind, el.value).then(function (res) { if (my === seq && cur === el && document.activeElement === el) render(res); })
      .catch(function () { close(); });
  }
  function attach(el, kind) {
    el._ksKind = kind;
    el.setAttribute("autocomplete", "off");
    el.setAttribute("role", "combobox");
    el.setAttribute("aria-autocomplete", "list");
    el.setAttribute("aria-controls", "ks-list");
    el.setAttribute("aria-expanded", "false");
    el.addEventListener("input", function (e) { if (e.isTrusted) { cur = el; update(el); } });
    el.addEventListener("focus", function () { cur = el; if (kind === "uni") loadUnis().catch(function () {}); update(el); });
    el.addEventListener("blur", function () { setTimeout(function () { if (cur === el) close(); }, 120); remember(kind, el.value); });
    el.addEventListener("keydown", function (e) {
      if (box.hidden || cur !== el) return;
      var n = items.length;
      if (e.key === "ArrowDown") { e.preventDefault(); hl((active + 1) % n); }
      else if (e.key === "ArrowUp") { e.preventDefault(); hl((active - 1 + n) % n); }
      else if (e.key === "Enter" && active >= 0) { e.preventDefault(); pick(active); }
      else if (e.key === "Escape") { close(); }
    });
  }
  // Fokus boʻlganda aniqlanadi: keyin qoʻshilgan qatorlar (jadval vositalari) ham ishlaydi
  document.addEventListener("focusin", function (e) {
    var el = e.target;
    if (!el || el._ksKind !== undefined || el.nodeName !== "INPUT") return;
    var k = kindOf(el);
    el._ksKind = k || "";
    if (k) { attach(el, k); cur = el; if (k === "uni") loadUnis().catch(function () {}); update(el); }
  }, true);
  window.addEventListener("resize", place);
  window.addEventListener("scroll", place, true);

  window.KSuggest = { kindOf: kindOf, suggest: suggest, norm: norm };
})();
