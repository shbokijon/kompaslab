// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — master-next.js (2026-11-19)
//  Magistratura M1–M8 oxiridagi "Keyingi qadam" bloki ([data-mnext]) ichidagi [data-mn] qatorlarini
//  foydalanuvchining oʻz javoblaridan toʻldiradi. Faqat localStorage (kompas_master_mN_v1) oʻqiladi,
//  hech narsa yozilmaydi va serverga yuborilmaydi. Maʼlumot boʻlmasa, sahifadagi umumiy matn qoladi.
//  Matn amaldagi alifboda (oʻ, gʻ); yangi alifboni js/alifbo.js koʻrsatadi.
// ═══════════════════════════════════════════════════════════════
(function () {
  var box = document.querySelector("[data-mnext]"); if (!box) return;
  function load(n) { try { return JSON.parse(localStorage.getItem("kompas_master_m" + n + "_v1") || "null") || {}; } catch (e) { return {}; } }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function set(key, html) { var el = box.querySelector('[data-mn="' + key + '"]'); if (el && html) el.innerHTML = html; }
  function day(d) { return ("0" + d.getDate()).slice(-2) + "." + ("0" + (d.getMonth() + 1)).slice(-2) + "." + d.getFullYear(); }
  function parse(s) { var m = /^(\d{4})-(\d{2})-(\d{2})/.exec(s || ""); return m ? new Date(+m[1], +m[2] - 1, +m[3]) : null; }
  function today() { var t = new Date(); t.setHours(0, 0, 0, 0); return t; }
  function rows() { var r = load(2).rows; return Array.isArray(r) ? r : []; }
  function future(list) {
    var t = today();
    return list.map(function (r) { return { r: r, d: parse(r.date) }; }).filter(function (x) { return x.d && x.d >= t; })
      .sort(function (a, b) { return a.d - b.d; });
  }
  var DAY = 864e5;

  var n = +box.getAttribute("data-mnext");

  if (n === 1) {
    var p = load(1).progs || [];
    if (p.length) set("m1", "<b>Roʻyxatingizdagi " + p.length + " ta dastur har xil kunda yopiladi.</b> Qaysi biri birinchi? M2 da roʻyxatingiz Arizalar jadvaliga bitta tugma bilan koʻchadi, Siz faqat sanalarni qoʻyasiz.");
  }

  if (n === 2) {
    var f = future(rows());
    if (f.length) {
      var first = f[0], ask = new Date(first.d.getTime() - 56 * DAY), left = Math.round((ask - today()) / DAY);
      set("m2rec", "<b>Tavsiya xatini soʻrash kuningiz: " + day(ask) + "</b> " +
        (left > 0 ? "(" + left + " kun qoldi). " : "(bu kun oʻtgan: hoziroq soʻrang). ") +
        "Hisob: eng erta sana " + esc(first.r.name || "") + ", " + day(first.d) + ", undan 8 hafta oldin. M4 da soʻrash xatini birga yozamiz.");
    }
    var a1 = (load(1).notes || {}).a1;
    if (a1) set("m2cv", "<b>CV ning Taʼlim boʻlimi uchun M1 dagi yozuvingiz tayyor:</b><br><i>" + esc(String(a1).split("\n").slice(0, 2).join(" · ").slice(0, 180)) + "</i><br>M3 da uni CV qatoriga aylantiramiz.");
  }

  if (n === 4) {
    var nt = load(1).notes || {};
    var parts = [["Oʻtmish", nt.nPast], ["Hozir", nt.nNow], ["Maqsad", nt.nGoal]].filter(function (x) { return x[1]; });
    if (parts.length) set("m4", "<b>Maqsad bayonnomangizning tayanch qismi allaqachon bor (M1 hikoyangiz):</b><br>" +
      parts.map(function (x) { return x[0] + ": <i>" + esc(String(x[1]).slice(0, 220)) + "</i>"; }).join("<br>") +
      "<br>M5 da bu 4 savolli tuzilmaga joylanadi va dalil bilan kengayadi.");
  }

  if (n === 6) {
    var sch = rows().filter(function (r) { return r.type === "s"; }), fs = future(sch);
    if (sch.length) set("m6", "<b>Jadvalingizda " + sch.length + " ta stipendiya bor.</b> " +
      (fs.length ? "Eng yaqini: " + esc(fs[0].r.name || "") + ", " + day(fs[0].d) + " (" + Math.round((fs[0].d - today()) / DAY) + " kun qoldi). " : "Sanalari hali kiritilmagan. ") +
      "M7 da ularni majburiy shartlar boʻyicha tekshiramiz va 3 tasini tanlaymiz.");
  }

  if (n === 7) {
    var pf = (load(7).port || []).filter(function (x) { return x && x.id; });
    if (pf.length) set("m7", "<b>Tanlagan " + pf.length + " ta stipendiyangiz boʻyicha suhbat savollari</b> M8 da. Komissiya savollarining koʻpi Siz yozgan jumlalardan tugʻiladi: javobni ovoz chiqarib mashq qilasiz.");
  }

  if (n === 8) {
    var f8 = future(rows());
    if (f8.length) set("m8", box.querySelector('[data-mn="m8"]').innerHTML + "<br><b>Eng yaqin sana:</b> " + esc(f8[0].r.name || "") + ", " + day(f8[0].d) + " (" + Math.round((f8[0].d - today()) / DAY) + " kun qoldi).");
  }
})();
