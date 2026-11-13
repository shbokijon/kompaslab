// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — live-bar.js
//  Saytning eng tepasida doim koʻrinadigan jonli panel:
//   · hozir saytda turganlar (Supabase Realtime Presence, bir brauzer = 1)
//   · roʻyxatdan oʻtganlar (kompas_public_stats().registered)
//   · tashriflar: bugun / shu hafta / shu oy / shu yil (kompas_track_visit)
//     1 tashrif = 1 brauzer × 1 kun (Toshkent vaqti), hafta dushanbadan
//  Raqam olinmasa, oʻsha belgi koʻrsatilmaydi: soxta raqam yoʻq.
// ═══════════════════════════════════════════════════════════════
(function () {
  if (window.__kompasLiveBar) return;
  window.__kompasLiveBar = true;

  var URL = "https://usxpkmbjrdllnitlzdpq.supabase.co";
  var KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVzeHBrbWJqcmRsbG5pdGx6ZHBxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI1MzUxNzcsImV4cCI6MjA4ODExMTE3N30.wecMraU0qbnT89IKaoyu0-gDBfo0kUBF1t6ajMJNvT8";
  var H = 40;            // panel balandligi (px)
  var REG_MIN = 10;      // bosh sahifadagi qoida bilan bir xil: 10 dan kam boʻlsa koʻrsatilmaydi
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  var css =
    ".klb{position:fixed;top:0;left:0;right:0;height:" + H + "px;z-index:400;background:#1e3329;display:flex;align-items:center;justify-content:safe center;gap:8px;padding:0 10px;overflow-x:auto;scrollbar-width:none;font-family:Outfit,IBM Plex Sans,system-ui,sans-serif;box-shadow:0 1px 0 rgba(255,255,255,.06) inset}" +
    ".klb::-webkit-scrollbar{display:none}.klb[hidden]{display:none}" +
    ".klb-s{flex:none;width:1px;height:22px;background:rgba(255,255,255,.25)}.klb-s[hidden]{display:none}" +
    ".klb-c{position:relative;display:inline-flex;align-items:center;gap:6px;height:32px;padding:0 12px 0 4px;flex:none;border-radius:99px;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.22);color:#fff;font-weight:800;font-size:15px;font-variant-numeric:tabular-nums;cursor:default;-webkit-tap-highlight-color:transparent}" +
    ".klb-c[hidden]{display:none}" +
    ".klb-c img{width:28px;height:28px;display:block;filter:drop-shadow(0 1px 2px rgba(0,0,0,.35))}" +
    ".klb-d{width:8px;height:8px;border-radius:50%;background:#3ddc84;box-shadow:0 0 0 0 rgba(61,220,132,.6)}" +
    ".klb-n.bump{animation:klbBump .6s ease}" +
    ".klb-tip{position:fixed;top:" + (H - 2) + "px;left:0;z-index:401;transform:translateX(-50%);white-space:nowrap;background:#fff;color:#1a2e26;font-size:12px;font-weight:700;padding:5px 9px;border-radius:8px;box-shadow:0 6px 20px rgba(0,0,0,.18);opacity:0;pointer-events:none;transition:opacity .15s}" +
    ".klb-tip.on{opacity:1}" +
    "@media(max-width:560px){.klb{gap:5px;padding:0 6px}.klb-c{height:28px;gap:3px;padding:0 8px 0 2px;font-size:13px}.klb-c img{width:22px;height:22px}.klb-d{width:6px;height:6px}}" +
    "@media(max-width:420px){.klb{gap:4px;padding:0 4px}.klb-c{padding:0 6px 0 1px;gap:2px;font-size:12px}.klb-c img{width:20px;height:20px}.klb-s{height:18px}}" +
    ".klb-c:focus-visible{outline:2px solid #e9a27a;outline-offset:2px}" +
    // Aloqa (2026-11-13): email, Telegram, Instagram — panelning oʻng tomoni
    ".klb-st{display:flex;align-items:center;gap:inherit;margin:0 auto;flex:none}" +
    ".klb-k{display:flex;align-items:center;gap:6px;flex:none;margin-left:auto;padding-left:6px}" +
    ".klb-kl{color:rgba(255,255,255,.75);font-size:13px;font-weight:700;margin-right:2px}" +
    ".klb-a{display:inline-flex;align-items:center;gap:6px;height:30px;min-width:30px;justify-content:center;padding:0 8px;border-radius:99px;color:#fff;text-decoration:none;font-size:13px;font-weight:700;background:rgba(255,255,255,.10);border:1px solid rgba(255,255,255,.2);transition:background .15s}" +
    ".klb-a:hover{background:rgba(255,255,255,.22)}.klb-a:focus-visible{outline:2px solid #e9a27a;outline-offset:2px}" +
    ".klb-a svg{width:16px;height:16px;flex:none;fill:currentColor}" +
    "@media(max-width:760px){.klb-kl,.klb-em{display:none}.klb-a{padding:0;width:30px}}" +
    "@media(max-width:420px){.klb-a{width:26px;height:26px;min-width:26px}.klb-a svg{width:14px;height:14px}.klb-k{gap:4px}}" +
    "@keyframes klbBump{0%{transform:scale(1)}40%{transform:scale(1.3)}100%{transform:scale(1)}}" +
    "@keyframes klbPulse{0%{box-shadow:0 0 0 0 rgba(61,220,132,.55)}70%{box-shadow:0 0 0 7px rgba(61,220,132,0)}100%{box-shadow:0 0 0 0 rgba(61,220,132,0)}}" +
    "@keyframes klbFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-2px)}}" +
    (reduce ? "" : ".klb-d{animation:klbPulse 2s infinite}.klb-c img{animation:klbFloat 4s ease-in-out infinite}.klb-c:nth-child(even) img{animation-delay:-2s}") +
    // Panel koʻringanda sahifa menyusini pastga suramiz
    "body.klb-on{padding-top:" + H + "px}" +
    "body.klb-on .nav{top:" + H + "px!important}" +
    "body.klb-on .top{top:" + H + "px!important}" +
    "body.klb-on .gate{min-height:calc(100vh - " + (60 + H) + "px)}";

  function nf(n) { return String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, " "); }

  function chip(id, icon, label, dot) {
    return '<span class="klb-c" id="' + id + '" data-tip="' + label + '" tabindex="0" role="img" aria-label="' + label + '" hidden>' +
      '<img src="img/3d/' + icon + '.webp" width="28" height="28" alt="">' + (dot ? '<i class="klb-d"></i>' : "") +
      '<b class="klb-n">0</b></span>';
  }

  var MAIL = "kompaslab.uz@gmail.com";
  var ICO = {
    mail: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5h18a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zm9 7.2L4 7.3V17h16V7.3l-8 4.9zM5.2 7l6.8 4.2L18.8 7H5.2z"/></svg>',
    tg: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M21.9 4.6 18.7 19.7c-.2 1-.9 1.3-1.7.8l-4.8-3.5-2.3 2.2c-.3.3-.5.5-1 .5l.3-4.9 8.9-8c.4-.3-.1-.5-.6-.2L6.5 13.5 1.8 12c-1-.3-1-1 .2-1.5L20.6 3.4c.9-.3 1.6.2 1.3 1.2z"/></svg>',
    ig: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.2c3.2 0 3.6 0 4.8.1 3.3.1 4.8 1.7 4.9 4.9.1 1.3.1 1.6.1 4.8s0 3.6-.1 4.8c-.1 3.2-1.7 4.8-4.9 4.9-1.3.1-1.6.1-4.8.1s-3.6 0-4.8-.1c-3.3-.1-4.8-1.7-4.9-4.9C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.8C2.4 4 3.9 2.4 7.2 2.3 8.4 2.2 8.8 2.2 12 2.2zm0 2c-3.1 0-3.5 0-4.7.1-2.3.1-3.4 1.2-3.5 3.5-.1 1.2-.1 1.6-.1 4.7s0 3.5.1 4.7c.1 2.3 1.2 3.4 3.5 3.5 1.2.1 1.6.1 4.7.1s3.5 0 4.7-.1c2.3-.1 3.4-1.2 3.5-3.5.1-1.2.1-1.6.1-4.7s0-3.5-.1-4.7c-.1-2.3-1.2-3.4-3.5-3.5-1.2-.1-1.6-.1-4.7-.1zm0 3.3a4.5 4.5 0 1 1 0 9 4.5 4.5 0 0 1 0-9zm0 7.4a2.9 2.9 0 1 0 0-5.8 2.9 2.9 0 0 0 0 5.8zm4.7-8.6a1.1 1.1 0 1 1 0 2.1 1.1 1.1 0 0 1 0-2.1z"/></svg>'
  };
  function contacts() {
    return '<div class="klb-k" translate="no" data-alifbo="off"><span class="klb-kl">Aloqa:</span>' +
      '<a class="klb-a" href="mailto:' + MAIL + '" title="' + MAIL + '" aria-label="Email: ' + MAIL + '">' + ICO.mail + '<span class="klb-em">' + MAIL + '</span></a>' +
      '<a class="klb-a" href="https://t.me/kompaslab" target="_blank" rel="noopener" title="Telegram: @kompaslab" aria-label="Telegram kanal">' + ICO.tg + '</a>' +
      '<a class="klb-a" href="https://www.instagram.com/kompaslab" target="_blank" rel="noopener" title="Instagram: @kompaslab" aria-label="Instagram sahifa">' + ICO.ig + '</a></div>';
  }

  function mount() {
    var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
    var bar = document.createElement("div");
    bar.className = "klb"; bar.hidden = true; bar.setAttribute("aria-live", "polite");
    bar.innerHTML = '<div class="klb-st">' + chip("klbOn", "telescope", "Hozir saytda", true) + chip("klbReg", "bachelor", "Roʻyxatdan oʻtganlar", false) +
      '<i class="klb-s" id="klbSep" hidden></i>' +
      chip("klbD", "bell", "Bugungi tashriflar", false) + chip("klbW", "calendar", "Shu haftadagi tashriflar", false) +
      chip("klbM", "chart", "Shu oydagi tashriflar", false) + chip("klbY", "seedling", "Shu yildagi tashriflar", false) + '</div>' + contacts();
    document.body.insertBefore(bar, document.body.firstChild);
    bar.hidden = false; document.body.classList.add("klb-on");
    // Bitta umumiy izoh: panel gorizontal aylansa ham kesilmaydi
    var tip = document.createElement("div"); tip.className = "klb-tip"; tip.setAttribute("aria-hidden", "true");
    document.body.appendChild(tip);
    var timer;
    function show(c, ms) {
      var r = c.getBoundingClientRect(), half;
      tip.textContent = c.getAttribute("data-tip"); tip.classList.add("on");
      half = tip.offsetWidth / 2 + 6;
      tip.style.left = Math.min(Math.max(r.left + r.width / 2, half), window.innerWidth - half) + "px";
      clearTimeout(timer); if (ms) timer = setTimeout(hide, ms);
    }
    function hide() { tip.classList.remove("on"); }
    bar.addEventListener("mouseover", function (e) { var c = e.target.closest(".klb-c"); if (c) show(c); });
    bar.addEventListener("mouseleave", hide);
    bar.addEventListener("focusin", function (e) { var c = e.target.closest(".klb-c"); if (c) show(c); });
    bar.addEventListener("focusout", hide);
    bar.addEventListener("scroll", hide, { passive: true });
    // Telefonda bosilganda izoh 2 soniya koʻrinadi
    bar.addEventListener("click", function (e) { var c = e.target.closest(".klb-c"); if (c) show(c, 2000); });
    return bar;
  }

  function setVal(bar, id, n) {
    var c = document.getElementById(id), b = c.querySelector(".klb-n");
    var prev = c.hidden ? null : b.textContent;
    b.textContent = nf(n);
    c.setAttribute("aria-label", c.getAttribute("data-tip") + ": " + nf(n));
    if (c.hidden) { c.hidden = false; }
    else if (prev !== b.textContent && !reduce) { b.classList.remove("bump"); void b.offsetWidth; b.classList.add("bump"); }
    if (bar.hidden) { bar.hidden = false; document.body.classList.add("klb-on"); }
  }

  function client() {
    var s = window.supabase;
    if (s && typeof s.channel === "function") return s;                 // config.js yaratgan mijoz
    if (s && typeof s.createClient === "function") {
      return (window.__kompasClient = window.__kompasClient || s.createClient(URL, KEY, { auth: { persistSession: true, autoRefreshToken: true } }));
    }
    return null;
  }

  function visitorId() {
    var id = null;
    try { id = localStorage.getItem("kompas_vid"); } catch (e) {}
    if (!id || !/^[a-z0-9]{8,40}$/.test(id)) {
      id = (Date.now().toString(36) + Math.random().toString(36).slice(2, 10));
      try { localStorage.setItem("kompas_vid", id); } catch (e) {}
    }
    return id;
  }

  // Kanal oʻlchovi: utm.js sahifada boʻlmasa, shu yerdan yuklanadi (tashrifdan oldin)
  function withUtm(cb) {
    if (window.KompasUTM) return cb();
    var s = document.createElement("script"), done = false;
    s.src = "js/utm.js";
    s.onload = s.onerror = function () { if (!done) { done = true; cb(); } };
    setTimeout(function () { if (!done) { done = true; cb(); } }, 1500);
    document.head.appendChild(s);
  }

  function start() {
    var bar = mount(), sb = client();
    if (!sb) return;

    // Roʻyxatdan oʻtganlar: sahifa ochilganda va har 60 soniyada
    function loadReg() {
      if (document.hidden || typeof sb.rpc !== "function") return;
      sb.rpc("kompas_public_stats").then(function (r) {
        var n = r && !r.error && r.data ? r.data.registered : null;
        if (typeof n === "number" && n >= REG_MIN) setVal(bar, "klbReg", n);
      });
    }
    loadReg(); setInterval(loadReg, 60000);
    document.addEventListener("visibilitychange", loadReg);

    // Tashriflar: sahifa ochilganda 1 marta yoziladi (bir kunda takror sanalmaydi), har 5 daqiqada yangilanadi
    // UTM (js/utm.js): birinchi soʻrovda kanal ham yuboriladi; baza p_utm ni bilmasa, usiz qayta soʻraladi
    var utmSent = false, utmOff = false;
    function loadVisits() {
      if (document.hidden || typeof sb.rpc !== "function") return;
      var u = !utmSent && !utmOff && window.KompasUTM ? window.KompasUTM.get() : null;
      var args = u ? { p_vid: visitorId(), p_utm: u } : { p_vid: visitorId() };
      sb.rpc("kompas_track_visit", args).then(function (r) {
        if (u && r && r.error) { utmOff = true; loadVisits(); return; }
        if (u) utmSent = true;
        var d = r && !r.error && r.data;
        if (!d || typeof d.day !== "number") return;
        setVal(bar, "klbD", d.day); setVal(bar, "klbW", d.week); setVal(bar, "klbM", d.month); setVal(bar, "klbY", d.year);
        document.getElementById("klbSep").hidden = false;
      });
    }
    withUtm(loadVisits); setInterval(loadVisits, 300000);

    // Voronka (2026-11-12): narx sahifasi koʻrildi (narxlar.html yoki <lab>-narxlar.html).
    // kompas_track_event odam + Lab + kun boʻyicha bir marta yozadi; xato boʻlsa jim.
    var pm = location.pathname.match(/^\/(?:([a-z-]+?)-)?narxlar(?:\.html)?$/);
    if (pm && typeof sb.rpc === "function") {
      try {
        sb.rpc("kompas_track_event", { p_event: "price_viewed", p_vid: visitorId(), p_slug: pm[1] || null, p_path: location.pathname })
          .then(function () {}, function () {});
      } catch (e) {}
    }

    // Hozir saytda: Realtime Presence (bitta brauzer bir nechta tabda ham 1 marta sanaladi)
    if (typeof sb.channel !== "function") return;
    var ch = sb.channel("kompas-online", { config: { presence: { key: visitorId() } } });
    function count() { setVal(bar, "klbOn", Object.keys(ch.presenceState()).length); }
    ch.on("presence", { event: "sync" }, count)
      .subscribe(function (status) {
        if (status === "SUBSCRIBED") ch.track({ at: Date.now(), page: location.pathname });
      });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start);
  else start();
})();
