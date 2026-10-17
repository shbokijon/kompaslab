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

  if (standalone) { track("standalone"); window.kompasInstall = function () { alert("Kompas Lab allaqachon ilova sifatida ochilgan."); }; return; }
  window.addEventListener("appinstalled", function () { track("installed"); hide(true); });

  var inApp = /; wv\)|Telegram|Instagram|FBAN|FBAV|Line\//i.test(ua) || (isIOS && !/safari/i.test(ua));
  var iosChrome = /crios/i.test(ua), iosOther = /fxios|edgios|yabrowser/i.test(ua);
  var samsung = /SamsungBrowser/i.test(ua), yandex = /YaBrowser/i.test(ua);
  var mobile = isIOS || isAndroid;
  var force = /[?&]pwa=1/.test(location.search);
  var deferred = null, box = null, css =
    ".kpw{position:fixed;left:12px;right:12px;bottom:12px;z-index:390;display:flex;gap:12px;align-items:center;background:#fffefb;border:1px solid #e2ded3;border-radius:18px;padding:12px 12px 12px 14px;box-shadow:0 18px 50px rgba(26,46,38,.22);font-family:Outfit,IBM Plex Sans,system-ui,sans-serif;color:#1a2e26;max-width:520px;margin:0 auto;transform:translateY(140%);transition:transform .45s cubic-bezier(.2,.9,.3,1.1)}" +
    ".kpw.on{transform:none}" +
    ".kpw .klogo{width:46px;height:46px;border-radius:13px}" +
    ".kpw-t{flex:1;min-width:0;font-size:13.5px;line-height:1.4}.kpw-t>b{display:block;font-size:15px}" +
    ".kpw-i{min-height:42px;padding:0 16px;border:0;border-radius:12px;background:#c4622d;color:#fff;font:800 14px Outfit,system-ui,sans-serif;cursor:pointer;flex:none}" +
    ".kpw-x{position:absolute;top:-10px;right:-6px;width:30px;height:30px;border-radius:50%;border:1px solid #e2ded3;background:#fff;color:#5f7169;font-size:16px;line-height:1;cursor:pointer}" +
    ".kpw-k{display:inline-block;min-width:20px;padding:0 5px;border:1px solid #c9c4b6;border-radius:6px;font-weight:800;text-align:center}" +
    (reduce ? ".kpw{transition:none}" : "");

  window.addEventListener("beforeinstallprompt", function (e) { e.preventDefault(); deferred = e; });

  // Brauzerga mos qoʻlda oʻrnatish yoʻriqnomasi
  function manual() {
    if (inApp) return "<b>Brauzerda oching</b>Telegram yoki Instagram ichidagi oynadan ilova oʻrnatib boʻlmaydi. Yuqoridagi <span class=\"kpw-k\">⋮</span> yoki <span class=\"kpw-k\">⋯</span> → <b style=\"display:inline\">“Brauzerda ochish”</b> (Open in browser), keyin shu yerdan oʻrnating.";
    if (isIOS && iosChrome) return "<b>Kompas Lab'ni ekranga qoʻshing</b>Manzil qatoridagi <span class=\"kpw-k\">⬆︎</span> Ulashish → <b style=\"display:inline\">“Add to Home Screen”</b> (“На экран «Домой»”).";
    if (isIOS) return "<b>Kompas Lab'ni ekranga qoʻshing</b>" + (iosOther ? "Safari'da oching, keyin: " : "") + "pastdagi <span class=\"kpw-k\">⬆︎</span> Ulashish → <b style=\"display:inline\">“Add to Home Screen”</b> (“На экран «Домой»”).";
    if (samsung) return "<b>Kompas Lab'ni ekranga qoʻshing</b>Pastdagi <span class=\"kpw-k\">≡</span> menyu → <b style=\"display:inline\">“Add page to” → “Home screen”</b> (“Добавить на” → “Главный экран”).";
    if (yandex) return "<b>Kompas Lab'ni ekranga qoʻshing</b><span class=\"kpw-k\">⋮</span> menyu → <b style=\"display:inline\">“Add to home screen”</b> (“Добавить ярлык”).";
    return "<b>Kompas Lab'ni ekranga qoʻshing</b>Yuqoridagi <span class=\"kpw-k\">⋮</span> menyu → <b style=\"display:inline\">“Install app”</b> yoki <b style=\"display:inline\">“Add to Home screen”</b> (“Установить приложение” / “Добавить на главный экран”).";
  }

  function show(html, withBtn) {
    if (box) box.remove();
    if (!document.getElementById("kpwCss")) { var st = document.createElement("style"); st.id = "kpwCss"; st.textContent = css; document.head.appendChild(st); }
    box = document.createElement("div"); box.className = "kpw"; box.setAttribute("role", "dialog"); box.setAttribute("aria-label", "Ilovani oʻrnatish");
    box.innerHTML = '<span class="klogo"><img class="klogo-b" src="/img/brand/logo-base.webp" alt="" width="128" height="128"><img class="klogo-a" src="/img/brand/logo-arrow.webp" alt="" width="128" height="128"></span>' +
      '<div class="kpw-t">' + html + "</div>" + (withBtn ? '<button type="button" class="kpw-i">Oʻrnatish</button>' : "") + '<button type="button" class="kpw-x" aria-label="Yopish">×</button>';
    document.body.appendChild(box);
    box.querySelector(".kpw-x").addEventListener("click", function () { hide(false); });
    var b = box.querySelector(".kpw-i");
    if (b) b.addEventListener("click", function () {
      if (!deferred) { show(manual(), false); return; }
      deferred.prompt();
      deferred.userChoice.then(function (c) { if (c && c.outcome === "accepted") hide(true); }).catch(function () {});
      deferred = null;
    });
    requestAnimationFrame(function () { requestAnimationFrame(function () { box && box.classList.add("on"); }); });
    track("prompt");
  }
  function hide(forever) {
    ls("kompas_pwa_hide", String(Date.now() + (forever ? 3650 : HIDE_DAYS) * 864e5));
    var b = box; box = null;
    if (b) { b.classList.remove("on"); setTimeout(function () { b.remove(); }, 500); }
  }
  function offer() {
    if (deferred) show("<b>Kompas Lab ilovasi</b>Bosh ekranga qoʻshing: bir bosishda ochiladi, darslar internetsiz ham ochiladi.", true);
    else show(manual(), false);
  }

  // Doimiy tugma uchun (masalan, sahifa pastida "📱 Ilovani oʻrnatish"): taklif yopilgan boʻlsa ham ishlaydi
  window.kompasInstall = offer;
  document.addEventListener("click", function (e) { var t = e.target.closest && e.target.closest("[data-install]"); if (t) { e.preventDefault(); offer(); } });

  var path = location.pathname;
  if (!force && (!mobile || /admin|login|register|reset|payment/.test(path))) return;
  if (!force && Date.now() < (+ls("kompas_pwa_hide") || 0)) return;
  var views = (+ls("kompas_pwa_views") || 0) + 1; ls("kompas_pwa_views", String(views));
  // Birinchi sahifada 12 soniyadan, keyingi sahifalarda 3 soniyadan keyin.
  // Chrome oʻz tugmasini bermasa ham (shartlar bajarilmagan yoki boshqa brauzer), qoʻlda yoʻriqnoma chiqadi.
  setTimeout(offer, force ? 300 : views >= 2 ? 3000 : 12000);
})();
