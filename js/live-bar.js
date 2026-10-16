// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — live-bar.js
//  Saytning eng tepasida doim koʻrinadigan jonli panel:
//   · hozir saytda turganlar (Supabase Realtime Presence, bir brauzer = 1)
//   · roʻyxatdan oʻtganlar (kompas_public_stats().registered)
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
    ".klb{position:fixed;top:0;left:0;right:0;height:" + H + "px;z-index:400;background:#1e3329;display:flex;align-items:center;justify-content:center;gap:10px;font-family:Outfit,system-ui,sans-serif;box-shadow:0 1px 0 rgba(255,255,255,.06) inset}" +
    ".klb[hidden]{display:none}" +
    ".klb-c{position:relative;display:inline-flex;align-items:center;gap:6px;height:32px;padding:0 12px 0 4px;border-radius:99px;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.22);color:#fff;font-weight:800;font-size:15px;font-variant-numeric:tabular-nums;cursor:default;-webkit-tap-highlight-color:transparent}" +
    ".klb-c[hidden]{display:none}" +
    ".klb-c img{width:28px;height:28px;display:block;filter:drop-shadow(0 1px 2px rgba(0,0,0,.35))}" +
    ".klb-d{width:8px;height:8px;border-radius:50%;background:#3ddc84;box-shadow:0 0 0 0 rgba(61,220,132,.6)}" +
    ".klb-n.bump{animation:klbBump .6s ease}" +
    ".klb-tip{position:absolute;top:36px;left:50%;transform:translateX(-50%);white-space:nowrap;background:#fff;color:#1a2e26;font-size:12px;font-weight:700;padding:5px 9px;border-radius:8px;box-shadow:0 6px 20px rgba(0,0,0,.18);opacity:0;pointer-events:none;transition:opacity .15s}" +
    ".klb-c:hover .klb-tip,.klb-c.tip .klb-tip,.klb-c:focus-visible .klb-tip{opacity:1}" +
    ".klb-c:focus-visible{outline:2px solid #e9a27a;outline-offset:2px}" +
    "@keyframes klbBump{0%{transform:scale(1)}40%{transform:scale(1.3)}100%{transform:scale(1)}}" +
    "@keyframes klbPulse{0%{box-shadow:0 0 0 0 rgba(61,220,132,.55)}70%{box-shadow:0 0 0 7px rgba(61,220,132,0)}100%{box-shadow:0 0 0 0 rgba(61,220,132,0)}}" +
    "@keyframes klbFloat{0%,100%{transform:translateY(0)}50%{transform:translateY(-2px)}}" +
    (reduce ? "" : ".klb-d{animation:klbPulse 2s infinite}.klb-c img{animation:klbFloat 4s ease-in-out infinite}.klb-c+.klb-c img{animation-delay:-2s}") +
    // Panel koʻringanda sahifa menyusini pastga suramiz
    "body.klb-on{padding-top:" + H + "px}" +
    "body.klb-on .nav{top:" + H + "px!important}" +
    "body.klb-on .top{top:" + H + "px!important}" +
    "body.klb-on .gate{min-height:calc(100vh - " + (60 + H) + "px)}";

  function nf(n) { return String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, " "); }

  function chip(id, icon, label, dot) {
    return '<span class="klb-c" id="' + id + '" tabindex="0" role="img" aria-label="' + label + '" hidden>' +
      '<img src="img/3d/' + icon + '.webp" width="28" height="28" alt="">' + (dot ? '<i class="klb-d"></i>' : "") +
      '<b class="klb-n">0</b><span class="klb-tip">' + label + "</span></span>";
  }

  function mount() {
    var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
    var bar = document.createElement("div");
    bar.className = "klb"; bar.hidden = true; bar.setAttribute("aria-live", "polite");
    bar.innerHTML = chip("klbOn", "telescope", "Hozir saytda", true) + chip("klbReg", "bachelor", "Roʻyxatdan oʻtganlar", false);
    document.body.insertBefore(bar, document.body.firstChild);
    // Telefonda bosilganda izoh 2 soniya koʻrinadi
    bar.addEventListener("click", function (e) {
      var c = e.target.closest(".klb-c"); if (!c) return;
      c.classList.add("tip"); setTimeout(function () { c.classList.remove("tip"); }, 2000);
    });
    return bar;
  }

  function setVal(bar, id, n) {
    var c = document.getElementById(id), b = c.querySelector(".klb-n");
    var prev = c.hidden ? null : b.textContent;
    b.textContent = nf(n);
    c.setAttribute("aria-label", c.querySelector(".klb-tip").textContent + ": " + nf(n));
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
    if (!id) {
      id = (Date.now().toString(36) + Math.random().toString(36).slice(2, 10));
      try { localStorage.setItem("kompas_vid", id); } catch (e) {}
    }
    return id;
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
