/* Kompas Lab — obuna sotuvi (Click SHOP-API), 2026-11-06.
 *
 * MODE:
 *   "off"   — hamma joyda kutish roʻyxati (oldingi holat);
 *   "admin" — "Toʻlash" tugmasi faqat adminlarga koʻrinadi (sinov);
 *   "on"    — hamma uchun ochiq. OFERTA_URL boʻsh boʻlsa, "on" ishlamaydi va "admin" kabi qoladi:
 *             "toʻlov qaytarilmaydi" qoidasi qabul qilingan ommaviy ofertasiz amal qilmaydi.
 * Qaysi Lab sotuvda: bazadan (admin → Lablar va narxlar, courses.on_sale), kompas_public_stats().prices[slug]:
 *   pp   — pullik modul yuklangan (aks holda hech kimga sotilmaydi);
 *   sale — hamma uchun sotuvda (on_sale va status=active). sale=false boʻlsa, faqat admin sinovi.
 * Narx, faza va trek faqat serverda (fn_create_pending_payment) hisoblanadi va shu shartlar serverda ham tekshiriladi;
 * bu fayl faqat tugmani koʻrsatadi, kirish huquqini bermaydi.
 */
(function () {
  "use strict";

  var CFG = window.KOMPAS_SALE = window.KOMPAS_SALE || {
    MODE: "on",
    OFERTA_URL: "oferta.html",
    SERVICE_ID: "114929",
    MERCHANT_ID: "66329"
  };

  var adminP = null, statsP = null;
  function open() { return CFG.MODE === "on" && !!CFG.OFERTA_URL; }
  CFG.isAdmin = function () {
    if (adminP) return adminP;
    if (!window.supabase || !window.supabase.auth) return (adminP = Promise.resolve(false));
    adminP = window.supabase.auth.getSession().then(function (r) {
      if (!r || !r.data || !r.data.session) return false;
      return window.supabase.rpc("fn_is_admin").then(function (x) { return x && x.data === true; }, function () { return false; });
    }, function () { return false; });
    return adminP;
  };
  CFG.stats = function () {
    if (statsP) return statsP;
    if (!window.supabase || typeof window.supabase.rpc !== "function") return (statsP = Promise.resolve({}));
    statsP = window.supabase.rpc("kompas_public_stats").then(function (r) {
      return (r && !r.error && r.data && r.data.prices) || {};
    }, function () { return {}; });
    return statsP;
  };
  // Umumiy ruxsat (tugma kimga chiqishi mumkin): admin yoki ochiq sotuv
  CFG.canBuy = function () {
    if (CFG.MODE === "off") return Promise.resolve(false);
    if (open()) return Promise.resolve(true);
    return CFG.isAdmin();
  };
  // Shu Lab uchun: pullik modul bor va (admin yoki ochiq sotuv + bazada sotuvda)
  CFG.canBuyLab = function (slug) {
    if (CFG.MODE === "off") return Promise.resolve(false);
    return Promise.all([CFG.isAdmin(), CFG.stats()]).then(function (v) {
      var p = v[1][slug];
      if (!p || !p.pp) return false;
      if (v[0]) return true;
      return open() && p.sale === true;
    });
  };
  // Sinov: ochiq sotuv yoʻq yoki shu Lab bazada sotuvda emas (tugmani faqat admin koʻradi)
  CFG.isTestLab = function (slug) {
    return CFG.stats().then(function (st) { return !open() || !(st[slug] && st[slug].sale === true); });
  };
  CFG.isTest = function () { return !open(); };

  var LABEL = { monthly: "Oylik obunani toʻlash", "6m": "6 oylik obunani toʻlash", yearly: "Yillik obunani toʻlash" };

  function enhance() {
    var btns = document.querySelectorAll("[data-buy]");
    if (!btns.length) return;
    var bySlug = {};
    Array.prototype.forEach.call(btns, function (b) {
      var v = (b.getAttribute("data-buy") || "").split("|"), slug = v[0], plan = v[1];
      if (!LABEL[plan]) return;
      (bySlug[slug] = bySlug[slug] || []).push([b, plan]);
    });
    Object.keys(bySlug).forEach(function (slug) {
      Promise.all([CFG.canBuyLab(slug), CFG.isTestLab(slug)]).then(function (r) {
        if (!r[0]) return;
        bySlug[slug].forEach(function (x) {
          var b = x[0], plan = x[1], a = document.createElement("a");
          a.className = b.className.replace("btn-g", "btn-p");
          a.href = "tolov.html?lab=" + encodeURIComponent(slug) + "&plan=" + encodeURIComponent(plan);
          a.textContent = LABEL[plan];
          a.setAttribute("data-snd", "nav");
          b.parentNode.replaceChild(a, b);
        });
        var st = document.querySelector("[data-paystatus=\"" + slug + "\"]");
        if (!st) return;
        st.innerHTML = "<b>Toʻlov Click orqali.</b> Toʻlov sahifasida tarif, aniq summa va ochiladigan modullar koʻrsatiladi; kirish toʻlov tasdiqlangan zahoti ochiladi." +
          (r[1] ? " <b>Sinov rejimi: tugmani faqat adminlar koʻradi.</b>" : "");
        var ico = st.previousElementSibling;
        if (ico) ico.textContent = "💳";
        var sec = st.closest("section"), rf = sec && sec.querySelector(".refund");
        if (rf) rf.innerHTML = "<b>Toʻlov qaytarilmaydi.</b> Shuning uchun har Labning M0 qismi bepul: toʻlashdan oldin dastur sizga mosligini tekshirasiz. " +
          "Istisno faqat texnik xato: pul ikki marta yechilgan, 24 soatda kirish ochilmagan yoki summa notoʻgʻri. Avtomatik yechish yoʻq: keyingi oy uchun toʻlamasangiz, obuna oʻzi toʻxtaydi.";
      });
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", enhance);
  else enhance();
})();
