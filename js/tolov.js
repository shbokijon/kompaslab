/* Kompas Lab — obuna toʻlovi sahifasi (tolov.html), 2026-11-06.
 * Oqim: Lab + tarif → rozilik → fn_create_pending_payment (baza "T<raqam>", summa va fazani beradi)
 * → my.click.uz → Click Prepare/Complete → click-shop → payments → trigger enrollments ni ochadi
 * → dashboard.html?tolov=T<raqam> holatni serverdan tekshiradi.
 * Summa mijozdan olinmaydi: Click'ga faqat server qaytargan summa yuboriladi, Complete da yana solishtiriladi.
 */
(function () {
  "use strict";

  var LABS = {
    "bachelor-lab": { name: "Bachelor Lab", page: "bachelor-lab-narxlar.html", phase: "4 modul" },
    "master-lab": { name: "Master Lab", page: "master-lab-narxlar.html", phase: "2 modul" },
    "usa-lab": { name: "USA Lab", page: "usa-lab-narxlar.html", phase: "2 modul" },
    "gks-lab": { name: "GKS Lab", page: "gks-lab-narxlar.html", phase: "I fazada M1–M2, keyin bittadan" }
  };
  var TRACKS = { u: "U · Bakalavriat (GKS-U)", m: "M · Magistratura (GKS-G)", d: "D · Doktorantura (GKS-G)" };
  var PLANS = {
    monthly: {
      name: "Oylik",
      rule: function (lab) {
        return "Har toʻlov bitta fazani ochadi (" + lab.phase + "). Muddat toʻlov kunidan 30 kun. " +
          "Oldingi oyning ishlatilmagan kunlari keyingisiga qoʻshilmaydi. Keyingi faza yangi toʻlov bilan ochiladi, " +
          "fazani muddatidan oldin tugatsangiz ham. Obuna tugasa, ochilgan modullar yopiladi.";
      }
    },
    "6m": {
      name: "6 oylik",
      rule: function () {
        return "Hamma modullar birdaniga ochiladi, muddat 6 oy. Amaldagi 6 oylik obunangiz boʻlsa, yangi muddat uning oxiriga qoʻshiladi.";
      }
    }
  };
  var ERR = {
    AUTH_REQUIRED: "Avval hisobingizga kiring.",
    ACCOUNT_SUSPENDED: "Hisobingiz vaqtincha toʻxtatilgan. Bizga yozing: kompaslab.uz@gmail.com",
    COURSE_NOT_FOR_SALE: "Bu Lab hozircha sotuvda emas.",
    PLAN_NOT_AVAILABLE: "Bu tarif hozircha mavjud emas. Boshqa tarifni tanlang.",
    MONTHLY_NOT_AVAILABLE: "Bu Labda oylik tarif yoʻq.",
    INSTALLMENT_ACTIVE: "Sizda boʻlib toʻlash davom etmoqda. Yangi obuna uchun bizga yozing.",
    ALREADY_ENROLLED: "Bu Lab sizga muddatsiz ochiq. Toʻlash shart emas.",
    HAS_FULL_PLAN: "Sizda 6 oylik obuna bor, unda hamma modullar ochiq. Oylik toʻlov shart emas.",
    ALL_PHASES_PAID: "Barcha fazalar toʻlangan. Muddatni uzaytirish uchun 6 oylik tarifni tanlang.",
    TRACK_REQUIRED: "Keyingi faza trekka bogʻliq. Trekni tanlang."
  };

  var $ = function (id) { return document.getElementById(id); };
  var fmt = function (n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, " "); };
  var q = new URLSearchParams(location.search);
  var slug = q.get("lab"), plan = q.get("plan"), order = null;

  function show(id) {
    ["tvGate", "tvLogin", "tvForm", "tvReady"].forEach(function (x) { if ($(x)) $(x).hidden = x !== id; });
  }
  function say(t) { var m = $("tvMsg"); if (m) m.textContent = t || ""; }

  function clickUrl(ref, sum) {
    var S = window.KOMPAS_SALE;
    return "https://my.click.uz/services/pay?service_id=" + S.SERVICE_ID +
      "&merchant_id=" + S.MERCHANT_ID +
      "&amount=" + Number(sum).toFixed(2) +
      "&transaction_param=" + encodeURIComponent(ref) +
      "&return_url=" + encodeURIComponent(location.origin + "/dashboard.html?tolov=" + encodeURIComponent(ref));
  }

  function renderPlans(prices) {
    var box = $("tvPlans"), lab = LABS[slug];
    box.innerHTML = "";
    var vals = { monthly: prices && prices.m, "6m": prices && prices.s6 };
    Object.keys(PLANS).forEach(function (k) {
      if (!(vals[k] > 0)) return;
      var l = document.createElement("label");
      l.className = "tv-plan";
      l.innerHTML = "<input type=\"radio\" name=\"tvPlan\" value=\"" + k + "\"><span><b>" + PLANS[k].name +
        "</b><em>" + fmt(vals[k]) + " soʻm</em></span>";
      box.appendChild(l);
    });
    var pick = box.querySelector("input[value=\"" + plan + "\"]") || box.querySelector("input");
    if (!pick) { say("Narxlar yuklanmadi. Sahifani yangilang."); return; }
    pick.checked = true; plan = pick.value;
    box.addEventListener("change", function (e) {
      if (e.target.name !== "tvPlan") return;
      plan = e.target.value; $("tvTrack").hidden = true; say(""); rule();
    });
    rule();
    function rule() { $("tvRule").textContent = PLANS[plan].rule(lab); }
  }

  function create() {
    var go = $("tvGo");
    if (!$("tvAgree").checked) { say("Davom etish uchun shartlarga rozilikni belgilang."); return; }
    var track = $("tvTrack").hidden ? null : ($("tvTrackSel").value || null);
    if (!$("tvTrack").hidden && !track) { say(ERR.TRACK_REQUIRED); return; }
    go.disabled = true; say("Buyurtma yaratilmoqda…");
    window.supabase.rpc("fn_create_pending_payment", { p_course_slug: slug, p_plan: plan, p_track: track }).then(function (r) {
      go.disabled = false;
      var row = r && r.data && r.data[0];
      if (r.error || !row || !row.order_ref) {
        var code = r.error && /([A-Z_]{6,})/.exec(r.error.message || "");
        code = code && code[1];
        if (code === "TRACK_REQUIRED") { $("tvTrack").hidden = false; }
        say((code && ERR[code]) || "Hozir buyurtma yaratib boʻlmadi. Birozdan keyin qayta urinib koʻring.");
        return;
      }
      order = row; say("");
      var mods = (row.phase_modules || []).map(function (n) { return "M" + n; }).join(", ");
      var lines = [
        ["Buyurtma", row.order_ref],
        ["Lab", row.course_title],
        ["Tarif", PLANS[row.plan] ? PLANS[row.plan].name : row.plan],
        row.phase ? ["Ochiladi", row.phase + "-faza" + (mods ? ": " + mods : "") + (row.track ? " (trek " + row.track.toUpperCase() + ")" : "")] : ["Ochiladi", "hamma modullar"],
        ["Summa", fmt(row.amount) + " soʻm"]
      ];
      $("tvSum").innerHTML = lines.map(function (x) { return "<div><span>" + x[0] + "</span><b></b></div>"; }).join("");
      Array.prototype.forEach.call($("tvSum").querySelectorAll("b"), function (b, i) { b.textContent = lines[i][1]; });
      $("tvPay").href = clickUrl(row.order_ref, row.amount);
      show("tvReady");
    }, function () { go.disabled = false; say("Internet aloqasini tekshirib, qayta urinib koʻring."); });
  }

  function init() {
    var S = window.KOMPAS_SALE;
    if (!LABS[slug] || !S || !window.supabase) { show("tvGate"); return; }
    $("tvLab").textContent = LABS[slug].name;
    $("tvBack").href = LABS[slug].page;
    Array.prototype.forEach.call(document.querySelectorAll("[data-tv-back]"), function (a) { a.href = LABS[slug].page; });
    if (S.OFERTA_URL) {
      $("tvOferta").innerHTML = "<a href=\"" + S.OFERTA_URL + "\" target=\"_blank\" rel=\"noopener\">Ommaviy oferta</a>";
    }
    S.isTestLab(slug).then(function (t) { if (t) $("tvTest").hidden = false; });

    window.supabase.auth.getSession().then(function (r) {
      if (!r || !r.data || !r.data.session) {
        try { sessionStorage.setItem("returnTo", "tolov.html" + location.search); } catch (e) {}
        try { localStorage.setItem("kompas_return", JSON.stringify({ to: "tolov.html" + location.search, at: Date.now() })); } catch (e) {}
        show("tvLogin"); return;
      }
      S.canBuyLab(slug).then(function (ok) {
        if (!ok) { show("tvGate"); return; }
        show("tvForm");
        window.supabase.rpc("kompas_public_stats").then(function (x) {
          var p = x && x.data && x.data.prices && x.data.prices[slug];
          renderPlans(p);
        }, function () { say("Narxlar yuklanmadi. Sahifani yangilang."); });
        $("tvGo").addEventListener("click", create);
        $("tvEdit").addEventListener("click", function () { show("tvForm"); });
      });
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
