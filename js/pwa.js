// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — pwa.js
//  · service worker ni roʻyxatdan oʻtkazadi (oflayn ishlash)
//  · telefonda "Ilovani oʻrnatish" taklifi: Android'da bitta tugma,
//    iPhone'da qoʻlda qoʻshish yoʻriqnomasi. Yopilsa 14 kun koʻrsatilmaydi.
//  · oʻrnatish va ilova rejimida ochilishni sanaydi (kompas_pwa_event)
// ═══════════════════════════════════════════════════════════════
(function () {
  if (window.__kompasPwa) return;
  window.__kompasPwa = true;

  var URL = "https://usxpkmbjrdllnitlzdpq.supabase.co";
  var KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVzeHBrbWJqcmRsbG5pdGx6ZHBxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzI1MzUxNzcsImV4cCI6MjA4ODExMTE3N30.wecMraU0qbnT89IKaoyu0-gDBfo0kUBF1t6ajMJNvT8";
  var HIDE_DAYS = 14;
  var ua = navigator.userAgent || "";
  var isIOS = /iphone|ipad|ipod/i.test(ua) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);
  var isAndroid = /android/i.test(ua);
  var platform = isIOS ? "ios" : isAndroid ? "android" : "desktop";
  var standalone = (window.matchMedia && window.matchMedia("(display-mode: standalone)").matches) || navigator.standalone === true;
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if ("serviceWorker" in navigator && (location.protocol === "https:" || location.hostname === "localhost")) {
    window.addEventListener("load", function () { navigator.serviceWorker.register("/sw.js").catch(function () {}); });
  }

  function ls(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
  function vid() {
    var id = ls("kompas_vid");
    if (!id || !/^[a-z0-9]{8,40}$/.test(id)) { id = Date.now().toString(36) + Math.random().toString(36).slice(2, 10); ls("kompas_vid", id); }
    return id;
  }
  function track(ev) {
    try {
      fetch(URL + "/rest/v1/rpc/kompas_pwa_event", { method: "POST", keepalive: true, headers: { "Content-Type": "application/json", apikey: KEY, Authorization: "Bearer " + KEY },
        body: JSON.stringify({ p_vid: vid(), p_event: ev, p_platform: platform }) }).catch(function () {});
    } catch (e) {}
  }

  if (standalone) { track("standalone"); return; }       // ilova ichida taklif kerak emas
  window.addEventListener("appinstalled", function () { track("installed"); hide(true); });

  var mobile = isIOS || isAndroid;
  var path = location.pathname;
  if (!mobile || /admin|login|register|reset|payment/.test(path)) return;
  var until = +ls("kompas_pwa_hide") || 0;
  if (Date.now() < until) return;
  var views = (+ls("kompas_pwa_views") || 0) + 1; ls("kompas_pwa_views", String(views));

  var css =
    ".kpw{position:fixed;left:12px;right:12px;bottom:12px;z-index:390;display:flex;gap:12px;align-items:center;background:#fffefb;border:1px solid #e2ded3;border-radius:18px;padding:12px 12px 12px 14px;box-shadow:0 18px 50px rgba(26,46,38,.22);font-family:Outfit,system-ui,sans-serif;color:#1a2e26;max-width:520px;margin:0 auto;transform:translateY(140%);transition:transform .45s cubic-bezier(.2,.9,.3,1.1)}" +
    ".kpw.on{transform:none}" +
    ".kpw .klogo{width:46px;height:46px;border-radius:13px}" +
    ".kpw-t{flex:1;min-width:0;font-size:13.5px;line-height:1.35}.kpw-t b{display:block;font-size:15px}" +
    ".kpw-i{min-height:42px;padding:0 16px;border:0;border-radius:12px;background:#c4622d;color:#fff;font:800 14px Outfit,system-ui,sans-serif;cursor:pointer;flex:none}" +
    ".kpw-x{position:absolute;top:-10px;right:-6px;width:30px;height:30px;border-radius:50%;border:1px solid #e2ded3;background:#fff;color:#5f7169;font-size:16px;line-height:1;cursor:pointer}" +
    ".kpw-sh{display:inline-block;padding:0 4px;border:1px solid #c9c4b6;border-radius:5px;font-weight:800}" +
    (reduce ? ".kpw{transition:none}" : "");

  var box, deferred = null;
  function build(html, withBtn) {
    if (box) return;
    var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
    box = document.createElement("div"); box.className = "kpw"; box.setAttribute("role", "dialog"); box.setAttribute("aria-label", "Ilovani oʻrnatish");
    box.innerHTML = '<span class="klogo"><img class="klogo-b" src="/img/brand/logo-base.webp" alt="" width="128" height="128"><img class="klogo-a" src="/img/brand/logo-arrow.webp" alt="" width="128" height="128"></span>' +
      '<div class="kpw-t">' + html + "</div>" + (withBtn ? '<button type="button" class="kpw-i">Oʻrnatish</button>' : "") + '<button type="button" class="kpw-x" aria-label="Yopish">×</button>';
    document.body.appendChild(box);
    box.querySelector(".kpw-x").addEventListener("click", function () { hide(false); });
    var b = box.querySelector(".kpw-i");
    if (b) b.addEventListener("click", function () {
      if (!deferred) return;
      deferred.prompt();
      deferred.userChoice.then(function (c) { if (c && c.outcome === "accepted") hide(true); }).catch(function () {});
      deferred = null;
    });
    requestAnimationFrame(function () { requestAnimationFrame(function () { box.classList.add("on"); }); });
    track("prompt");
  }
  function hide(forever) {
    ls("kompas_pwa_hide", String(Date.now() + (forever ? 3650 : HIDE_DAYS) * 864e5));
    if (box) { box.classList.remove("on"); setTimeout(function () { if (box) box.remove(); box = null; }, 500); }
  }
  // Birinchi sahifada emas: ikkinchi koʻrishdan yoki 25 soniyadan keyin
  function ready(fn) { if (views >= 2) setTimeout(fn, 1500); else setTimeout(fn, 25000); }

  if (isAndroid) {
    window.addEventListener("beforeinstallprompt", function (e) {
      e.preventDefault(); deferred = e;
      ready(function () { if (deferred) build("<b>Kompas Lab ilovasi</b>Bosh ekranga qoʻshing: bir bosishda ochiladi, darslar internetsiz ham ochiladi.", true); });
    });
  } else if (isIOS && /safari/i.test(ua) && !/crios|fxios|edgios/i.test(ua)) {
    ready(function () { build("<b>Kompas Lab'ni ekranga qoʻshing</b>Pastdagi <span class=\"kpw-sh\">⬆︎</span> Ulashish tugmasi → <b style=\"display:inline;font-size:inherit\">“Add to Home Screen”</b> (“На экран «Домой»”).", false); });
  }
})();
