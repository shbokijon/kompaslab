// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — kompas-ui.js (2026-10-18)
//  Har sahifada <head> ichida (defer emas) yuklanadi:
//  · Sahifalar orasidagi oʻtish yoʻnalishi (View Transitions: next / prev)
//  · Ichki havolalarga "nav" tovushi (sfx.js), ←/→ bilan oldingi/keyingi sahifa
//  · Lab tablari (mobil panel) va "yoʻl"dagi kompas strelkasi
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
  var LABS = { "bachelor-lab": "Bachelor Lab", "master-lab": "Master Lab", "phd-lab": "PhD Lab", "gks-lab": "GKS Lab", "usa-lab": "USA Lab", "daad-lab": "DAAD Lab", "tadbirkor-talaba": "Tadbirkor Talaba", "miggo": "Musofir Lab" };
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
  function run() {
    var u = user();
    if (!u) { try { localStorage.removeItem(ME); } catch (e) {} return; }
    mount(render(u, rd(ME)));
    footer();
    refresh(u);
  }
  window.KUI_ME = { reset: function () { try { localStorage.removeItem(ME); } catch (e) {} } };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run); else run();
})();
