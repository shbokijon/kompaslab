/* Kompas Lab — Qoʻllab-quvvatlash (donat) bloki, qollab-quvvatlash.html (2026-10-30)
 *
 * Toʻlov ulanmaguncha ENABLED = false: sahifada faqat "Tayyorlanmoqda" holati chiqadi.
 * Yoqish (asoschi qarori bilan): Click yoki Payme bergan rasmiy toʻlov havolasini URL ga
 * yozing, PROVIDER ni belgilang va ENABLED = true qiling.
 *
 * Ataylab qoʻllab-quvvatlanmaydi: karta raqami, P2P oʻtkazma, shaxsiy hisob rekvizitlari.
 * Sabab: biznes tushumi shaxsiy kartaga kelsa, soliq xavfi (P2P monitoringi) va
 * firibgarlar "Kompas Lab nomidan" karta raqami tarqatishi oson boʻladi.
 */
(function () {
  "use strict";

  var DONAT = {
    ENABLED: false,
    PROVIDER: "",   // "Click" yoki "Payme"
    URL: ""         // faqat rasmiy toʻlov sahifasi (https), pastdagi HOSTS roʻyxatidan
  };

  // Ruxsat etilgan toʻlov sahifalari. Merchant havolasi berilganda domenini tekshirib, kerak boʻlsa qoʻshing.
  var HOSTS = ["my.click.uz", "indoor.click.uz", "checkout.paycom.uz", "payme.uz"];

  function okUrl(u) {
    try {
      var x = new URL(u);
      return x.protocol === "https:" && HOSTS.indexOf(x.hostname) !== -1;
    } catch (e) { return false; }
  }

  function render() {
    var box = document.getElementById("donatBox");
    if (!box) return;
    var live = DONAT.ENABLED && okUrl(DONAT.URL) && (DONAT.PROVIDER === "Click" || DONAT.PROVIDER === "Payme");
    box.setAttribute("data-state", live ? "on" : "off");
    var off = document.getElementById("donatOff"), on = document.getElementById("donatOn"), a = document.getElementById("donatGo");
    if (off) off.hidden = live;
    if (on) on.hidden = !live;
    if (live && a) {
      a.href = DONAT.URL;
      a.textContent = DONAT.PROVIDER + " orqali qoʻllab-quvvatlash";
    }
  }

  // Ulashish: telefonda tizim oynasi, kompyuterda havolani nusxalash
  function initShare() {
    var b = document.getElementById("shareBtn"), msg = document.getElementById("shareMsg");
    if (!b) return;
    var url = "https://www.kompaslab.uz/";
    var text = "Xorijda oʻqish va stipendiyaga oʻzbek tilida tayyorgarlik. Har Labda M0 bepul.";
    function say(t) { if (msg) { msg.textContent = t; } }
    b.addEventListener("click", function () {
      if (navigator.share) {
        navigator.share({ title: "Kompas Lab", text: text, url: url }).catch(function () {});
        return;
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(function () { say("Havola nusxalandi."); }, function () { say(url); });
      } else {
        say(url);
      }
    });
  }

  function init() { render(); initShare(); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
