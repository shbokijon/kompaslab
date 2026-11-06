/* Kompas Lab: telefon maydoni.
 * +998 prefiksi maydon yonida qotirilgan, foydalanuvchi faqat 9 xonali raqamni yozadi.
 * Yozish paytida raqam 91-123-4567 koʻrinishiga keladi.
 * Ulash: <input type="tel" data-phone> (sahifa yuklanganda oʻzi ulanadi).
 * Bazaga saqlanadigan qiymat: "+998 91-123-4567" (KompasPhone.value).
 */
(function () {
  "use strict";

  // Faqat mahalliy 9 xonani qaytaradi. Yopishtirilgan "+998 91 123 45 67", "998911234567",
  // "0911234567", "8 91 123 45 67" kabi yozuvlar ham toʻgʻri qirqiladi.
  function digits(v) {
    var d = String(v == null ? "" : v).replace(/\D/g, "");
    if (d.length > 9) {
      if (d.indexOf("998") === 0) d = d.slice(3);
      else if (d.charAt(0) === "0" || d.charAt(0) === "8") d = d.slice(1);
    }
    d = d.replace(/^0+/, "");
    return d.slice(0, 9);
  }

  function format(v) {
    var d = digits(v);
    var out = d.slice(0, 2);
    if (d.length > 2) out += "-" + d.slice(2, 5);
    if (d.length > 5) out += "-" + d.slice(5, 9);
    return out;
  }

  function valid(v) { return digits(v).length === 9; }

  function value(v) { return valid(v) ? "+998 " + format(v) : ""; }

  function caretAfterDigits(str, n) {
    if (n <= 0) return 0;
    var seen = 0;
    for (var i = 0; i < str.length; i++) {
      if (/\d/.test(str.charAt(i))) { seen++; if (seen === n) return i + 1; }
    }
    return str.length;
  }

  function attach(input) {
    if (!input || input.getAttribute("data-phone-on")) return;
    input.setAttribute("data-phone-on", "1");
    input.setAttribute("autocomplete", "tel-national");
    input.setAttribute("inputmode", "numeric");
    if (!input.getAttribute("placeholder")) input.setAttribute("placeholder", "91-123-4567");
    input.addEventListener("input", function (e) {
      var raw = input.value;
      var pasted = (e && e.inputType === "insertFromPaste") || raw.replace(/\D/g, "").length > 9;
      var pos = input.selectionStart;
      var before = (raw.slice(0, pos == null ? raw.length : pos).match(/\d/g) || []).length;
      var next = format(raw);
      if (next !== raw) input.value = next;
      try {
        var to = pasted || pos == null ? next.length : caretAfterDigits(next, before);
        input.setSelectionRange(to, to);
      } catch (err) {}
    });
  }

  // Saqlangan qiymatni maydonga qoʻyish ("+998 90 123 45 67" kabi eski yozuvlar ham 90-123-4567 boʻladi)
  function set(input, stored) { input.value = format(stored); }

  window.KompasPhone = { digits: digits, format: format, valid: valid, value: value, attach: attach, set: set };

  function auto() {
    var list = document.querySelectorAll("input[data-phone]");
    for (var i = 0; i < list.length; i++) attach(list[i]);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", auto);
  else auto();
})();
