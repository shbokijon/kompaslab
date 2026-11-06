/* Kompas Lab — Qoʻllab-quvvatlash (donat) bloki, qollab-quvvatlash.html
 *
 * 2026-11-06: Click SHOP-API orqali. Oqim: summa → fn_create_donation (baza "D<raqam>" beradi)
 * → my.click.uz toʻlov sahifasi → Click Prepare/Complete → Edge Function click-shop → donations jadvali.
 * Kirish shart emas. ENABLED = false qilinsa, blok "Tayyorlanmoqda" holatiga qaytadi.
 *
 * Ataylab qoʻllab-quvvatlanmaydi: karta raqami, P2P oʻtkazma, shaxsiy hisob rekvizitlari.
 * Sabab: biznes tushumi shaxsiy kartaga kelsa, soliq xavfi (P2P monitoringi) va
 * firibgarlar "Kompas Lab nomidan" karta raqami tarqatishi oson boʻladi.
 */
(function () {
  "use strict";

  var DONAT = {
    ENABLED: true,
    SERVICE_ID: "114929",
    MERCHANT_ID: "66329",
    MIN: 1000,
    MAX: 10000000
  };

  var amt = 25000;
  function fmt(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, " "); }
  function $(id) { return document.getElementById(id); }

  function setAmt(n) {
    amt = n;
    var go = $("donatGo");
    if (go) go.textContent = n ? "Click orqali " + fmt(n) + " soʻm" : "Summani kiriting";
    if (go) go.disabled = !n;
  }

  function payUrl(ref, sum) {
    var ret = location.origin + "/donat?d=" + encodeURIComponent(ref) + "#donat";
    return "https://my.click.uz/services/pay?service_id=" + DONAT.SERVICE_ID +
      "&merchant_id=" + DONAT.MERCHANT_ID +
      "&amount=" + sum.toFixed(2) +
      "&transaction_param=" + encodeURIComponent(ref) +
      "&return_url=" + encodeURIComponent(ret);
  }

  // Click sahifasidan qaytganda: holatni serverdan soʻraymiz, "paid" boʻlsagina tabriklaymiz
  function checkReturn() {
    var m = /[?&]d=(D\d{1,18})/.exec(location.search);
    var note = $("donatThanks");
    if (!m || !note) return;
    var ref = m[1], tries = 0;
    note.hidden = false;
    note.textContent = "Toʻlov holati tekshirilmoqda…";
    function ask() {
      tries++;
      window.supabase.rpc("fn_donation_status", { p_ref: ref }).then(function (r) {
        var row = r && r.data && r.data[0], st = row && row.status;
        if (st === "paid") {
          note.textContent = "Rahmat! " + fmt(row.amount) + " soʻm qabul qilindi.";
          if (window.KCelebrate) window.KCelebrate.show({
            kind: "donat", title: "Rahmat!", amount: row.amount,
            text: "Donatingiz Kompas Labga tushdi. U yangi darslar, manbalarni tekshirish va saytni yuritishga sarflanadi."
          });
          try { history.replaceState(null, "", "/donat#donat"); } catch (e) {}
          return;
        }
        if (st === "failed" || st === "rejected") { note.textContent = "Toʻlov amalga oshmadi. Pul yechilgan boʻlsa, Click chekidagi raqam bilan bizga yozing."; return; }
        if (tries < 8) { setTimeout(ask, 2000); return; }
        note.textContent = "Click hali tasdiqlamadi. Bir necha daqiqadan keyin sahifani yangilang yoki Click ilovasidagi chekni koʻring.";
      }, function () { if (tries < 8) setTimeout(ask, 2000); });
    }
    ask();
  }

  function initDonat() {
    var box = $("donatBox");
    if (!box) return;
    var live = DONAT.ENABLED && window.supabase && typeof window.supabase.rpc === "function";
    box.setAttribute("data-state", live ? "on" : "off");
    if ($("donatOff")) $("donatOff").hidden = live;
    if ($("donatOn")) $("donatOn").hidden = !live;
    if (!live) return;

    checkReturn();

    var btns = box.querySelectorAll(".dn-amt"), own = $("donatSum"), msg = $("donatMsg"), go = $("donatGo");
    function say(t) { if (msg) msg.textContent = t || ""; }
    Array.prototype.forEach.call(btns, function (b) {
      b.addEventListener("click", function () {
        Array.prototype.forEach.call(btns, function (x) { x.classList.remove("is-on"); });
        b.classList.add("is-on");
        if (own) own.value = "";
        say(""); setAmt(parseInt(b.getAttribute("data-amt"), 10));
      });
    });
    if (own) own.addEventListener("input", function () {
      Array.prototype.forEach.call(btns, function (x) { x.classList.remove("is-on"); });
      var n = Math.round(Number(own.value));
      if (!own.value) { setAmt(0); say(""); return; }
      if (!(n >= DONAT.MIN && n <= DONAT.MAX)) { setAmt(0); say("Summa 1 000 dan 10 000 000 soʻmgacha boʻlishi kerak."); return; }
      say(""); setAmt(n);
    });
    setAmt(amt);

    go.addEventListener("click", function () {
      if (!amt) return;
      go.disabled = true; say("");
      var sum = amt;
      window.supabase.rpc("fn_create_donation", { p_amount: sum }).then(function (r) {
        var row = r && r.data && r.data[0];
        if (r.error || !row || !row.order_ref) {
          go.disabled = false;
          say("Hozir buyurtma yaratib boʻlmadi. Birozdan keyin qayta urinib koʻring.");
          return;
        }
        location.href = payUrl(row.order_ref, Number(row.amount));
      }, function () {
        go.disabled = false;
        say("Internet aloqasini tekshirib, qayta urinib koʻring.");
      });
    });
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

  function init() { initDonat(); initShare(); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
