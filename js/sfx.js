// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — sfx.js (modullardagi tovush effektlari)
//  · Tovushlar Web Audio API bilan sintez qilinadi: fayl yuklanmaydi, internetsiz ishlaydi.
//  · Faqat foydalanuvchi bosgandan keyin chalinadi (brauzer avtoijro qoidasi).
//  · Oʻchirish tugmasi modul sarlavhasida (.top .xp); tanlov localStorage "kompas_sfx" da,
//    hamma sahifalarga umumiy ("0" = oʻchiq).
//  API: KSfx.play(nom)  — tap | tab | xp | badge | level | win | warn
//       KSfx.gain(oldXp, newXp) — XP qoʻshilganda mos tovushni tanlaydi
// ═══════════════════════════════════════════════════════════════
(function () {
  var KEY = "kompas_sfx", LEVELS = [80, 170], ctx = null, master = null, last = {};
  function on() { try { return localStorage.getItem(KEY) !== "0"; } catch (e) { return true; } }
  function audio() {
    if (!ctx) {
      var AC = window.AudioContext || window.webkitAudioContext; if (!AC) return null;
      ctx = new AC(); master = ctx.createGain(); master.gain.value = 0.5; master.connect(ctx.destination);
    }
    if (ctx.state === "suspended") ctx.resume();
    return ctx;
  }
  // Bitta nota: chastota (Hz), boshlanish (s), davomiylik (s), toʻlqin, balandlik
  function note(f, t, d, type, vol) {
    var o = ctx.createOscillator(), g = ctx.createGain(), s = ctx.currentTime + t;
    o.type = type || "sine"; o.frequency.setValueAtTime(f, s);
    g.gain.setValueAtTime(0.0001, s); g.gain.exponentialRampToValueAtTime(vol || 0.2, s + 0.008); g.gain.exponentialRampToValueAtTime(0.0001, s + d);
    o.connect(g); g.connect(master); o.start(s); o.stop(s + d + 0.02);
  }
  var C5 = 523.25, E5 = 659.25, G5 = 783.99, C6 = 1046.5, E6 = 1318.5, G6 = 1568;
  var SOUNDS = {
    tap: function () { note(1200, 0, 0.04, "sine", 0.05); },
    tab: function () { note(740, 0, 0.06, "triangle", 0.09); note(990, 0.03, 0.06, "triangle", 0.06); },
    xp: function () { note(988, 0, 0.09, "square", 0.05); note(1319, 0.07, 0.22, "square", 0.05); },
    badge: function () { [C6, E6, G6].forEach(function (f, i) { note(f, i * 0.07, 0.25, "triangle", 0.13); }); },
    level: function () { [C5, E5, G5, C6].forEach(function (f, i) { note(f, i * 0.09, 0.3, "triangle", 0.15); }); [C6, E6, G6].forEach(function (f) { note(f, 0.36, 0.7, "sine", 0.06); }); },
    win: function () {
      [G5, C6, E6, G6].forEach(function (f, i) { note(f, i * 0.1, 0.22, "square", 0.04); note(f, i * 0.1, 0.3, "triangle", 0.1); });
      [C5, E5, G5, C6].forEach(function (f) { note(f, 0.45, 1.1, "sine", 0.07); });
    },
    warn: function () { note(330, 0, 0.12, "triangle", 0.14); note(247, 0.1, 0.18, "triangle", 0.14); }
  };
  function play(name) {
    if (!on() || !SOUNDS[name]) return;
    var now = Date.now(); if (last[name] && now - last[name] < 60) return; last[name] = now;   // ikki marta ketma-ket chalinmasin
    try { if (audio()) SOUNDS[name](); } catch (e) {}
  }
  function gain(x0, x1) {
    if (x1 <= x0) return play("badge");
    for (var i = 0; i < LEVELS.length; i++) if (x0 < LEVELS[i] && x1 >= LEVELS[i]) return play("level");
    play("xp");
  }
  window.KSfx = { play: play, gain: gain };

  // Dars boʻlimlari va tugmalar uchun yengil tovush; XP beradigan bosish oʻz tovushini qoʻshadi
  document.addEventListener("click", function (e) {
    var el = e.target.closest && e.target.closest(".tab, .l-head, button, .btn, input[type=checkbox], input[type=radio]");
    if (!el || el.disabled || el.id === "sfxBtn") return;
    play(el.matches(".tab, .l-head") ? "tab" : "tap");
  });

  function mount() {
    var box = document.querySelector(".top .xp"); if (!box || document.getElementById("sfxBtn")) return;
    var st = document.createElement("style");
    st.textContent = "#sfxBtn{flex:none;width:32px;height:32px;border-radius:50%;border:1px solid var(--border,#ddd);background:transparent;cursor:pointer;font-size:15px;line-height:1;padding:0;display:grid;place-items:center}#sfxBtn:hover{background:rgba(0,0,0,.05)}";
    document.head.appendChild(st);
    var b = document.createElement("button"); b.type = "button"; b.id = "sfxBtn";
    function paint() { var o = on(); b.textContent = o ? "🔊" : "🔇"; b.setAttribute("aria-pressed", o ? "true" : "false"); b.title = o ? "Tovushni oʻchirish" : "Tovushni yoqish"; b.setAttribute("aria-label", b.title); }
    b.addEventListener("click", function () { try { localStorage.setItem(KEY, on() ? "0" : "1"); } catch (e) {} paint(); play("tap"); });
    paint(); box.appendChild(b);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", mount); else mount();
})();
