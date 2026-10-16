// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — protect.js
//  Kurs materiallarini nusxalashni qiyinlashtiradi (toʻliq toʻsib boʻlmaydi):
//   · matnni belgilash, nusxa olish, oʻng tugma, sudrash, chop etish oʻchiriladi
//     (input/textarea ichida yozish va nusxalash ishlaydi)
//   · ekranga juda xira suv belgisi: "kompaslab.uz"
// ═══════════════════════════════════════════════════════════════
(function () {
  if (window.__kompasProtect) return;
  window.__kompasProtect = true;

  var css =
    "body{-webkit-user-select:none;user-select:none;-webkit-touch-callout:none}" +
    "input,textarea,select,[contenteditable],[contenteditable] *{-webkit-user-select:text;user-select:text}" +
    "img{-webkit-user-drag:none}" +
    ".kp-wm{position:fixed;inset:0;z-index:350;pointer-events:none;background-repeat:repeat;opacity:.045}" +
    ".kp-msg{position:fixed;left:50%;bottom:24px;transform:translateX(-50%);z-index:9999;background:#1e3329;color:#fff;font:700 13px Outfit,system-ui,sans-serif;padding:9px 14px;border-radius:10px;box-shadow:0 8px 24px rgba(0,0,0,.25);opacity:0;transition:opacity .2s;pointer-events:none}" +
    ".kp-msg.on{opacity:1}" +
    "@media print{body>*{display:none!important}body:after{content:'Kompas Lab materiallarini chop etib boʻlmaydi.';display:block;padding:40px;font:700 18px sans-serif}}";
  var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);

  function editable(t) {
    return t && t.closest && t.closest("input,textarea,select,[contenteditable]");
  }
  var msg, timer;
  function note() {
    if (!msg) { msg = document.createElement("div"); msg.className = "kp-msg"; msg.setAttribute("role", "status"); document.body.appendChild(msg); }
    msg.textContent = "Kurs materiallari himoyalangan";
    msg.classList.add("on"); clearTimeout(timer); timer = setTimeout(function () { msg.classList.remove("on"); }, 1800);
  }
  ["copy", "cut", "contextmenu", "dragstart", "selectstart"].forEach(function (ev) {
    document.addEventListener(ev, function (e) {
      if (editable(e.target)) return;
      e.preventDefault(); if (ev !== "selectstart" && ev !== "dragstart") note();
    });
  });
  document.addEventListener("keydown", function (e) {
    var k = (e.key || "").toLowerCase(), mod = e.ctrlKey || e.metaKey;
    if (mod && (k === "s" || k === "p" || k === "u")) { e.preventDefault(); note(); return; }
    if (mod && (k === "c" || k === "x" || k === "a") && !editable(e.target)) { e.preventDefault(); note(); }
  });

  // Suv belgisi: diagonal, butun ekran boʻylab
  function watermark(text) {
    var c = document.createElement("canvas"), w = 280, h = 170, g = c.getContext("2d");
    if (!g) return;
    c.width = w; c.height = h;
    g.translate(w / 2, h / 2); g.rotate(-0.4);
    g.fillStyle = "#000"; g.font = "500 13px Outfit,system-ui,sans-serif"; g.textAlign = "center";
    g.fillText(text, 0, 0);
    var d = document.querySelector(".kp-wm") || document.createElement("div");
    d.className = "kp-wm"; d.setAttribute("aria-hidden", "true");
    d.style.backgroundImage = "url(" + c.toDataURL() + ")";
    if (!d.parentNode) document.body.appendChild(d);
  }
  // Faqat tizimga kirganlarga (M0 va darslar shu holatda ochiladi)
  function start() {
    var sb = window.supabase;
    if (!sb || !sb.auth || typeof sb.auth.getSession !== "function") return;
    sb.auth.getSession().then(function (r) {
      if (r && r.data && r.data.session) watermark("kompaslab.uz");
    }).catch(function () {});
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start);
  else start();
})();
