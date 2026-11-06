/* Kompas Lab — obuna sotuvi (Click SHOP-API), 2026-11-06.
 *
 * MODE:
 *   "off"   — hamma joyda kutish roʻyxati (oldingi holat);
 *   "admin" — "Toʻlash" tugmasi faqat adminlarga koʻrinadi (sinov);
 *   "on"    — hamma uchun ochiq. OFERTA_URL boʻsh boʻlsa, "on" ishlamaydi va "admin" kabi qoladi:
 *             "toʻlov qaytarilmaydi" qoidasi qabul qilingan ommaviy ofertasiz amal qilmaydi.
 * LABS: sotuvdagi Lablar. Narx, faza va trek faqat serverda (fn_create_pending_payment) hisoblanadi;
 * bu fayl faqat tugmani koʻrsatadi, kirish huquqini bermaydi.
 */
(function () {
  "use strict";

  var CFG = window.KOMPAS_SALE = window.KOMPAS_SALE || {
    MODE: "admin",
    OFERTA_URL: "",
    LABS: ["bachelor-lab", "master-lab", "usa-lab", "gks-lab"],
    SERVICE_ID: "114929",
    MERCHANT_ID: "66329"
  };

  var cache = null;
  CFG.canBuy = function () {
    if (cache) return cache;
    var open = CFG.MODE === "on" && !!CFG.OFERTA_URL;
    if (open) return (cache = Promise.resolve(true));
    if (CFG.MODE === "off" || !window.supabase || !window.supabase.auth) return (cache = Promise.resolve(false));
    cache = window.supabase.auth.getSession().then(function (r) {
      if (!r || !r.data || !r.data.session) return false;
      return window.supabase.rpc("fn_is_admin").then(function (x) { return x && x.data === true; }, function () { return false; });
    }, function () { return false; });
    return cache;
  };
  CFG.isTest = function () { return !(CFG.MODE === "on" && CFG.OFERTA_URL); };

  var LABEL = { monthly: "Oylik obunani toʻlash", "6m": "6 oylik obunani toʻlash", yearly: "Yillik obunani toʻlash" };

  function enhance() {
    var btns = document.querySelectorAll("[data-buy]");
    if (!btns.length) return;
    CFG.canBuy().then(function (ok) {
      if (!ok) return;
      var seen = {};
      Array.prototype.forEach.call(btns, function (b) {
        var v = (b.getAttribute("data-buy") || "").split("|"), slug = v[0], plan = v[1];
        if (CFG.LABS.indexOf(slug) < 0 || !LABEL[plan]) return;
        seen[slug] = 1;
        var a = document.createElement("a");
        a.className = b.className.replace("btn-g", "btn-p");
        a.href = "tolov.html?lab=" + encodeURIComponent(slug) + "&plan=" + encodeURIComponent(plan);
        a.textContent = LABEL[plan];
        a.setAttribute("data-snd", "nav");
        b.parentNode.replaceChild(a, b);
      });
      Object.keys(seen).forEach(function (slug) {
        var st = document.querySelector("[data-paystatus=\"" + slug + "\"]");
        if (!st) return;
        st.innerHTML = "<b>Toʻlov Click orqali.</b> Toʻlov sahifasida tarif, aniq summa va ochiladigan modullar koʻrsatiladi; kirish toʻlov tasdiqlangan zahoti ochiladi." +
          (CFG.isTest() ? " <b>Sinov rejimi: tugmani faqat adminlar koʻradi.</b>" : "");
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
