// Pullik modul sahifasi (masalan master-lab-m3.html): obunachiga "Modulni ochish" tugmasi.
// Bu fayl faqat koʻrinishni oʻzgartiradi. Haqiqiy tekshiruv serverda: fn_paid_page() obuna
// yoki admin boʻlmasa kontentni bermaydi. Shu sababli bu yerdagi xato hech kimga kontent ochmaydi.
(function () {
  "use strict";
  var box = document.querySelector(".kl-lock[data-paid]");
  if (!box) return;
  var slug = box.getAttribute("data-paid");
  var mod = parseInt(box.getAttribute("data-mod"), 10);
  var reader = box.getAttribute("data-reader");
  // In GKS, U/M/D tracks share the visible M3-M5 labels, but paid_pages uses
  // unique indices 3..11. Match the reader's actual backend module identifier.
  var accessIndex = mod;
  if (slug === "gks-lab" && reader) {
    var key = new URL(reader, location.href).searchParams.get("m");
    var trackIndex = {"m3-u":3,"m4-u":4,"m5-u":5,
      "m3-m":6,"m4-m":7,"m5-m":8,
      "m3-d":9,"m4-d":10,"m5-d":11};
    if (Object.prototype.hasOwnProperty.call(trackIndex,key)) accessIndex = trackIndex[key];
  }
  var sb = window.supabase;
  if (!sb || !sb.auth || !(mod >= 1)) return;

  function setText(sel, txt) { var el = box.querySelector(sel); if (el) el.textContent = txt; }
  function buttons(list) {
    var row = box.querySelector("[data-paid-row]");
    if (!row) return;
    row.innerHTML = "";
    list.forEach(function (b) {
      var a = document.createElement("a");
      a.className = "btn " + (b.primary ? "btn-p" : "btn-g");
      a.href = b.href;
      a.textContent = b.label;
      a.setAttribute("data-snd", "nav");
      row.appendChild(a);
    });
  }
  function open() {
    box.classList.add("is-open");
    var img = box.querySelector("img");
    if (img) img.src = "img/3d/compass.webp";
    setText("[data-paid-t]", "Modul siz uchun ochiq.");
    setText("[data-paid-d]", "Javoblaringiz shu qurilmada saqlanadi. Darslarni tartib bilan oʻting: har darsda 4 qism ochilgach, dars yakunlanadi.");
    buttons([{label: "Modulni ochish", href: reader, primary: true}, {label: "Mening kabinetim", href: "dashboard.html"}]);
    document.querySelectorAll(".kl-lessons .kl-st.is-locked").forEach(function (li) {
      li.classList.remove("is-locked");
      li.classList.add("is-free");
      var s = li.querySelector(".kl-st-s");
      if (s) s.textContent = "Ochiq";
    });
  }

  sb.auth.getSession().then(function (r) {
    if (!r || !r.data || !r.data.session) return;
    return Promise.all([
      sb.rpc("fn_is_admin"),
      sb.rpc("fn_my_access", {p_course_slug: slug}),
      sb.rpc("kompas_my_module_access", {p_course_slug: slug, p_module_index: accessIndex})
    ]).then(function (res) {
      // The module-level RPC is authoritative when available; payment/grant checks remain on server.
      if (res[2] && !res[2].error) {
        if (res[2].data === true) open();
        else setText("[data-paid-t]", "Bu modul hozircha yopiq.");
        return;
      }
      if (res[0] && res[0].data === true) { open(); return; }
      var a = res[1] && res[1].data;
      if (!a || !a.access) return;
      // unlocked_modules M0 ni ham sanaydi (M0 = 1-oʻrin), shuning uchun Mn uchun n+1 kerak
      if ((a.unlocked_modules || 0) >= accessIndex + 1) { open(); return; }
      setText("[data-paid-t]", "Bu modul keyinroq ochiladi.");
      setText("[data-paid-d]", "Tarifingiz boʻyicha hozir " + (a.unlocked_modules || 0) + " ta modul ochiq (M0 bilan). Oylik obunada keyingi faza navbatdagi toʻlov bilan, toʻlov qilingan zahoti ochiladi.");
      buttons([{label: "Mening kabinetim", href: "dashboard.html", primary: true}]);
    });
  }).catch(function () {});
})();
