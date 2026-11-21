// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — bachelor-next.js (2026-11-21)
//  Bakalavr dasturi M1–M8 oxiridagi "Keyingi qadam" bloki ([data-mnext]) ichidagi [data-mn] qatorlarini
//  foydalanuvchining oʻz javoblaridan toʻldiradi. Faqat localStorage (kompas_bachelor_mN_v1) oʻqiladi,
//  hech narsa yozilmaydi. Maʼlumot boʻlmasa, sahifadagi umumiy matn qoladi.
//  Matn amaldagi alifboda (oʻ, gʻ); yangi alifboni js/alifbo.js koʻrsatadi.
// ═══════════════════════════════════════════════════════════════
(function () {
  var box = document.querySelector("[data-mnext]"); if (!box) return;
  function load(n) { try { return JSON.parse(localStorage.getItem("kompas_bachelor_m" + n + "_v1") || "null") || {}; } catch (e) { return {}; } }
  function notes(n) { return load(n).notes || {}; }
  function set(key, html) { var el = box.querySelector('[data-mn="' + key + '"]'); if (el && html) el.innerHTML = html; }
  function day(d) { return ("0" + d.getDate()).slice(-2) + "." + ("0" + (d.getMonth() + 1)).slice(-2) + "." + d.getFullYear(); }
  function parse(s) { var m = /^(\d{4})-(\d{2})-(\d{2})/.exec(s || ""); return m ? new Date(+m[1], +m[2] - 1, +m[3]) : null; }
  function today() { var t = new Date(); t.setHours(0, 0, 0, 0); return t; }
  function lines(s) { return String(s || "").split(/\n+/).map(function (x) { return x.trim(); }).filter(function (x) { return x.length > 2; }).length; }
  var DAY = 864e5;
  var n = +box.getAttribute("data-mnext");
  var r1 = notes(1), uni = lines(r1.orzu) + lines(r1.moljal) + lines(r1.ishonchli);
  var erta = parse(notes(2).erta);

  if (n === 1 && uni) {
    set("m1", "<b>Roʻyxatingizda " + uni + " ta universitet bor.</b> Endi har birining muddati va test talabini bitta jadvalga qoʻyish qoladi. " +
      "M2 da eng erta muddatingizdan orqaga hisoblab, qaysi ishni qachon boshlashni aniqlaysiz.");
  }

  if (n === 2 && erta) {
    var ask = new Date(erta.getTime() - 56 * DAY), left = Math.round((ask - today()) / DAY);
    set("m2", "<b>Eng erta muddatingiz: " + day(erta) + ".</b> Tavsiya soʻrash kuni: <b>" + day(ask) + "</b> " +
      (left >= 0 ? "(" + left + " kun qoldi)." : "(bu sana oʻtdi: soʻrovni shu hafta yuboring).") +
      " II bosqichda faoliyatlar roʻyxati, CV va yutuqlar varaqasini shu sanagacha tayyorlaysiz.");
  }

  if (n === 3) {
    var f = notes(3), k = lines(f.f13) + lines(f.f46) + lines(f.f710);
    if (k) set("m3", "<b>Roʻyxatingizda " + k + " ta faoliyat yozuvi bor.</b> Ulardan eng kuchli 3–5 tasi M4 da yutuqlar varaqasiga oʻtadi va oʻqituvchingiz ularni oʻz xatida tasdiqlaydi.");
  }

  if (n === 4 && erta) {
    var ess = new Date(erta.getTime() - 84 * DAY), l2 = Math.round((ess - today()) / DAY);
    set("m4", "<b>Inshoning birinchi qoralamasi: " + day(ess) + " gacha</b> " + (l2 >= 0 ? "(" + l2 + " kun qoldi)." : "(bu sana oʻtdi: qoralamani shu hafta boshlang).") +
      " III bosqichda (M5–M6) inshoni yozasiz va 4 yillik moliyaviy rejani tuzasiz.");
  }

  if (n === 5 && uni) {
    set("m5", "<b>Inshongiz tayyor.</b> Roʻyxatingizdagi " + uni + " ta universitetdan eng ehtimolli birini olib, M6 da uning xarajatini 4 yilga hisoblaysiz va stipendiyalarni saralaysiz.");
  }

  if (n === 6) {
    var p = String(notes(6).plan4 || ""), m = /jami boʻshliq:\s*([\d\s ]+)/.exec(p);
    if (m) {
      var gap = +m[1].replace(/\D/g, "");
      set("m6", gap > 0
        ? "<b>4 yilda qoplanmagan qism: " + m[1].trim() + ".</b> Topshirishdan oldin bu boʻshliqni yopadigan stipendiya yoki arzonroq universitetni roʻyxatda qoldiring. IV bosqichda (M7–M8) ariza topshiriladi."
        : "<b>4 yillik rejangiz qoplangan.</b> Endi hujjatlar, insho va reja bir joyga kelib, ariza topshiriladi. IV bosqichda (M7–M8) arizani topshirasiz va joʻnashni rejalashtirasiz.");
    }
  }

  if (n === 7) {
    var t = lines(notes(7).topsh);
    if (t) set("m7", "<b>Topshirilgan arizalaringiz: " + t + " ta.</b> Endi javob kutiladi, baʼzi universitetlar intervyuga chaqiradi. M8 da intervyuga tayyorlanasiz va natijalar uchun qaror jadvalini tuzasiz.");
  }

  if (n === 8) {
    var j = parse(notes(8).jonash);
    if (j) {
      var l3 = Math.round((j - today()) / DAY), el = box.querySelector('[data-mn="m8"]');
      if (el && l3 >= 0) el.innerHTML += "<br><b>Joʻnashingizgacha " + l3 + " kun qoldi</b> (" + day(j) + "). 30 kunlik roʻyxatni " + day(new Date(j.getTime() - 30 * DAY)) + " dan boshlang.";
    }
  }
})();
