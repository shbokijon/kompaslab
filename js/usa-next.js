// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — usa-next.js (2026-11-20)
//  USA dasturi M1–M8 oxiridagi "Keyingi qadam" bloki ([data-mnext]) ichidagi [data-mn] qatorlarini
//  foydalanuvchining oʻz javoblaridan toʻldiradi. Faqat localStorage (kompas_usa_mN_v1) oʻqiladi,
//  hech narsa yozilmaydi va serverga yuborilmaydi. Maʼlumot boʻlmasa, sahifadagi umumiy matn qoladi.
//  Matn amaldagi alifboda (oʻ, gʻ); yangi alifboni js/alifbo.js koʻrsatadi.
// ═══════════════════════════════════════════════════════════════
(function () {
  var box = document.querySelector("[data-mnext]"); if (!box) return;
  function load(n) { try { return JSON.parse(localStorage.getItem("kompas_usa_m" + n + "_v1") || "null") || {}; } catch (e) { return {}; } }
  function notes(n) { return load(n).notes || {}; }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function set(key, html) { var el = box.querySelector('[data-mn="' + key + '"]'); if (el && html) el.innerHTML = html; }
  function day(d) { return ("0" + d.getDate()).slice(-2) + "." + ("0" + (d.getMonth() + 1)).slice(-2) + "." + d.getFullYear(); }
  function parse(s) { var m = /^(\d{4})-(\d{2})-(\d{2})/.exec(s || ""); return m ? new Date(+m[1], +m[2] - 1, +m[3]) : null; }
  function today() { var t = new Date(); t.setHours(0, 0, 0, 0); return t; }
  function nf(n) { return String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, " "); }
  function short(s, n) { s = String(s || "").replace(/\s+/g, " ").trim(); return s.length > n ? s.slice(0, n) + "…" : s; }
  var DAY = 864e5;
  var n = +box.getAttribute("data-mnext");

  if (n === 1) {
    var u = notes(1).uni;
    if (u) set("m1", "<b>Kartangizdagi universitet: " + esc(short(u, 80)) + ".</b> Endi savol boshqa: bir yili qanchaga tushadi va <b>budjetingiz</b> bunga yetadimi? M2 da shuni raqam bilan hisoblaymiz.");
  }

  if (n === 2) {
    var p = String(notes(2).p_in || "").split("|").map(Number);
    var C = p[0], F = p[1], Y = Math.max(1, Math.min(6, Math.round(p[2]) || 4)), G = (p[3] || 0) / 100;
    if (C > 0) {
      var tot = 0, need = 0;
      for (var y = 0; y < Y; y++) { var c = C * Math.pow(1 + G, y); tot += c; need += Math.max(0, c - (F || 0)); }
      var sh = tot ? Math.round(need / tot * 100) : 0;
      var way = sh <= 0 ? "natija granti boʻlsa yaxshi, boʻlmasa ham oʻzingiz toʻlay olasiz" : sh <= 50 ? "natija grantlari va arzon yoʻllar (ikki yillik kollej, arzon hududlar)" : "faqat toʻliq ehtiyojni qoplaydigan universitetlar (A va B guruhi) yoki parallel boshqa mamlakat";
      set("m2", "<b>Sizning hisobingiz:</b><ul><li>" + Y + " yillik narx: <b>" + nf(tot) + " USD</b>;</li><li>kerakli yordam: <b>" + nf(need) + " USD (" + sh + "%)</b>;</li><li>sizga mos yoʻl: " + way + ".</li></ul> M3 da aynan shu ulushni qoplaydigan universitetlarni rasmiy sahifa va CDS H6 bilan topamiz.");
    }
  }

  if (n === 3) {
    var a = notes(3).a_guruh;
    if (a) set("m3", "<b>A va B guruhidagi universitetlaringiz yordamni turli formada soʻraydi:</b><br><i>" + esc(short(a, 200)) + "</i><br>M4 da har biriga forma, hujjat va muddat qatorini yozamiz.");
  }

  if (n === 4) {
    var d = parse(notes(4).muddat);
    if (d) {
      var left = Math.round((d - today()) / DAY);
      set("m4", "<b>Eng yaqin moliyaviy yordam muddatingiz: " + day(d) + "</b> " + (left >= 0 ? "(" + left + " kun qoldi)." : "(bu sana oʻtgan: keyingi muddatni yozing).") +
        " III bosqichda (M5–M6) davlat dasturlari: Oʻzbekistonda bakalavriatda oʻqiyotganlar uchun Global UGRAD, 2+ yillik tajribalilar uchun Fulbright magistraturasi.");
    }
  }

  if (n === 5) {
    var q = notes(5).qaror;
    if (q) set("m5", "<b>UGRAD boʻyicha qaroringiz: " + esc(q) + ".</b> Bakalavrni tugatib, 2 yillik ish tajribasi yigʻilgach, keyingi davlat dasturi Fulbright magistraturasi. M6 da uning shartlarini va J-1 majburiyatini rejangiz bilan solishtirasiz.");
  }

  if (n === 6) {
    var q6 = notes(6).qaror;
    if (q6) set("m6", "<b>Fulbright boʻyicha qaroringiz: " + esc(q6) + ".</b> Qaysi yoʻlni tanlasangiz ham, AQSh magistraturasi va PhD ga kafedra moliyasi orqali ham borish mumkin. IV bosqichda (M7–M8) moliya paketini solishtirasiz va viza tartibini oʻrganasiz.");
  }

  if (n === 7) {
    var q7 = notes(7).qaror;
    if (q7) set("m7", "<b>Tanlovingiz: " + esc(q7) + ".</b> Taklifni qabul qilgach, universitet I-20 yoki DS-2019 beradi. M8 da Toshkentdagi viza tartibini, maqomni saqlashni va ishlash qoidalarini oʻrganasiz.");
  }

  if (n === 8) {
    var b = parse(notes(8).boshlanish);
    if (b) {
      var v = new Date(b.getTime() - 365 * DAY), e = new Date(b.getTime() - 30 * DAY);
      set("m8", box.querySelector('[data-mn="m8"]').innerHTML + "<br><b>Sizning sanalaringiz:</b> viza " + day(v) + " dan berilishi mumkin, AQShga kirish " + day(e) + " dan erta emas.");
    }
  }
})();
