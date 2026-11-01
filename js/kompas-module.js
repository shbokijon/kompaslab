// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — kompas-module.js (2026-10-18)
//  M0 modulining uch koʻrinishi (bitta manbadan tools/modules/build.py yigʻadi):
//    hub    <nom>.html          — modul: maqsad, darslar yoʻli, nishonlar
//    lesson <nom>-N.html        — bitta dars (toʻrt qism), oldingi/keyingi
//    yakun  <nom>-yakun.html    — vositalar, nishonlar, qaror va rozilik
//  Modulning oʻz JS kodi (XP, darslar, vositalar) oʻzgarmaydi: sahifa toʻliq DOM bilan
//  keladi, bu fayl faqat koʻrinishni tanlaydi va navigatsiyani quradi.
//  Progress: modulning localStorage kaliti (KMOD.key), hamma sahifalarga umumiy.
// ═══════════════════════════════════════════════════════════════
(function () {
  var M = window.KMOD; if (!M) return;
  // Free M0 reading is public. Registration is required only to sync/save a personal result.
  // Do not auto-open underage Maktab Lab: it requires its own parent-consent flow.
  if (!/^maktab-lab/.test(M.base || '')) document.body.classList.remove('locked');
  var body = document.body, view = body.getAttribute("data-kview"), curId = body.getAttribute("data-klesson");
  var L = M.lessons, N = L.length;
  function $(s, r) { return (r || document).querySelector(s); }
  function el(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function state() { try { return JSON.parse(localStorage.getItem(M.key) || "{}") || {}; } catch (e) { return {}; } }
  function page(i) { return M.base + "-" + (i + 1) + ".html"; }
  var YAKUN = M.base + "-yakun.html", HUB = M.base + ".html";
  function idx(id) { for (var i = 0; i < N; i++) if (L[i].id === id) return i; return -1; }

  // ── Sahifa ichidagi havolalarni alohida sahifalarga yoʻnaltirish ──
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    var h = a.getAttribute("href").slice(1); if (!h) return;
    var i = idx(h);
    if (i >= 0) { a.setAttribute("href", page(i)); return; }
    if (/^(tool-|qaror$|vositalar$|nishonlar$)/.test(h) && view !== "yakun") a.setAttribute("href", YAKUN + "#" + h);
  });

  function crumb(extra) {
    return '<nav class="kl-crumb" aria-label="Yoʻl"><a href="index.html">Kompas Lab</a><span aria-hidden="true">/</span><a href="' + M.lab + '">' + esc(M.labName) + '</a><span aria-hidden="true">/</span>' +
      (extra ? '<a href="' + HUB + '">' + esc(M.mod) + '</a><span aria-hidden="true">/</span><span>' + esc(extra) + "</span>" : "<span>" + esc(M.mod) + "</span>") + "</nav>";
  }
  function steps(S, cur) {
    var done = S.done || {}, h = "";
    L.forEach(function (l, i) {
      var c = l.id === cur ? "cur" : done[l.id] ? "done" : "";
      h += '<a class="' + c + '" href="' + page(i) + '"' + (c === "cur" ? ' aria-current="page"' : "") + ' title="' + esc("Dars " + l.num + ": " + l.title) + '"><i>' + (done[l.id] && c !== "cur" ? "✓" : esc(l.num.split(".").pop())) + "</i><span>" + esc(l.short || l.num) + "</span></a>";
    });
    var yc = cur === "yakun" ? "cur" : done.dec ? "done" : "";
    h += '<a class="' + yc + '" href="' + YAKUN + '"' + (yc === "cur" ? ' aria-current="page"' : "") + ' title="Yakun: vositalar va qaror"><i>' + (done.dec && yc !== "cur" ? "✓" : "★") + "</i><span>Yakun</span></a>";
    return '<div class="kl-steps" aria-label="Modul darslari">' + h + "</div>";
  }
  function firstOpen(S) { var d = S.done || {}; for (var i = 0; i < N; i++) if (!d[L[i].id]) return i; return -1; }
  var wrap = $("main .wrap");

  // ═══ HUB ═══
  if (view === "hub") {
    var S = state(), d = S.done || {}, nd = 0; L.forEach(function (l) { if (d[l.id]) nd++; });
    var fo = firstOpen(S);
    // Hero ostida asosiy tugma
    var facts = $(".hero .facts");
    if (facts) {
      var go = fo < 0 ? (d.dec ? HUB + "#nishonlar" : YAKUN) : page(fo);
      var label = fo < 0 ? (d.dec ? "Modul yakunlangan" : "Yakuniy bosqichga oʻtish") : nd ? "Davom etish: Dars " + L[fo].num : "Birinchi darsni boshlash";
      var act = el("div", "kl-hub-actions");
      act.innerHTML = '<a class="btn btn-p" href="' + go + '" data-dir="next">' + esc(label) + '</a><a class="btn btn-g" href="' + M.lab + '">' + esc(M.labName) + " sahifasi</a>";
      facts.parentNode.insertBefore(act, facts.nextSibling);
    }
    // Darslar yoʻli
    var sec = $("#darslar");
    if (sec) {
      var sub = $(".sub", sec);
      if (sub) sub.textContent = "Har dars alohida sahifada va toʻrt qismdan iborat: Diqqat 🔥, Asosiy qism, Xulosa va Topshiriq. Progress shu qurilmada saqlanadi: " + nd + " / " + N + " dars yakunlangan.";
      var ol = el("ol", "kl-route kl-hub-route"); ol.setAttribute("data-needle", "");
      L.forEach(function (l, i) {
        var done = !!d[l.id], cur = i === fo;
        var li = el("li", "kl-st" + (done ? " is-done" : cur ? " is-current" : ""));
        li.innerHTML = '<a href="' + page(i) + '"><span class="kl-st-n">' + (done ? "✓" : esc(l.num)) + '</span><span class="kl-st-b"><b>' + esc(l.title) + "</b><small>" + esc(l.meta || "") + '</small></span><span class="kl-st-s">' + (done ? "Yakunlangan" : cur ? (nd ? "Davom etish" : "Boshlash") : "Dars " + esc(l.num)) + "</span></a>";
        ol.appendChild(li);
      });
      var yk = el("li", "kl-st" + (d.dec ? " is-done" : fo < 0 ? " is-current" : ""));
      yk.innerHTML = '<a href="' + YAKUN + '"><span class="kl-st-n">' + (d.dec ? "✓" : "★") + '</span><span class="kl-st-b"><b>Yakun: vositalar va qaror</b><small>' + esc(M.yakunMeta) + '</small></span><span class="kl-st-s">' + (d.dec ? "Tasdiqlangan" : "Yakun") + "</span></a>";
      ol.appendChild(yk);
      (sub || $("h2", sec)).insertAdjacentElement("afterend", ol);
    }
  }

  // ═══ DARS ═══
  if (view === "lesson") {
    var i = idx(curId), art = document.getElementById(curId);
    if (i < 0 || !art) return;
    var S2 = state(), l = L[i];
    art.classList.add("kl-cur", "open");
    var hd = $(".l-head", art); if (hd) { hd.setAttribute("aria-expanded", "true"); hd.hidden = true; }
    // Birinchi qism ochilgan deb belgilanadi (modul kodi: tab bosilishi)
    var t0 = $(".tab", art); if (t0 && !((S2.seen || {})[curId] || []).length) t0.click();
    var tags = $(".l-m", art), ic = $(".l-ic img", art);
    var head = el("div", "kl-lhead");
    head.innerHTML = crumb("Dars " + l.num) + steps(S2, curId) + '<h1>' + esc(l.title) + '</h1><div class="kl-lmeta">' + (tags ? tags.innerHTML : "") + "</div>";
    wrap.insertBefore(head, wrap.firstChild);
    var prev = i > 0 ? [page(i - 1), "Oldingi dars", "Dars " + L[i - 1].num + ": " + L[i - 1].title] : [HUB, "Modul sahifasi", M.mod + ": barcha darslar"];
    var next = i < N - 1 ? [page(i + 1), "Keyingi dars", "Dars " + L[i + 1].num + ": " + L[i + 1].title] : [YAKUN, "Yakuniy bosqich", "Vositalar, nishonlar va qaror"];
    var foot = el("div", "kl-lfoot");
    foot.innerHTML = '<div class="kl-pager"><a class="pv" rel="prev" data-kkey data-dir="prev" href="' + prev[0] + '"><small>' + prev[1] + "</small><b>" + esc(prev[2]) + '</b></a><a class="nx" rel="next" data-kkey data-dir="next" href="' + next[0] + '"><small>' + next[1] + "</small><b>" + esc(next[2]) + '</b></a></div><p class="kl-keys"><kbd>←</kbd> <kbd>→</kbd> oldingi va keyingi sahifa</p>';
    $("#darslar").appendChild(foot);
    document.title = "Dars " + l.num + ": " + l.title + " · " + M.labName + " " + M.mod + " | Kompas Lab";

    // Oʻqish progressi
    var rb = el("div", "kl-read", "<i></i>"); rb.setAttribute("aria-hidden", "true"); body.appendChild(rb);
    var bar = rb.firstChild, tick = false;
    function read() {
      tick = false; var r = art.getBoundingClientRect(), h = r.height - window.innerHeight * 0.6;
      var p = h > 0 ? Math.min(1, Math.max(0, -r.top / h)) : 1; bar.style.width = (p * 100).toFixed(1) + "%";
    }
    window.addEventListener("scroll", function () { if (!tick) { tick = true; requestAnimationFrame(read); } }, { passive: true });
    art.addEventListener("click", function () { setTimeout(read, 50); });
    read();

    // Dars yakunlanganda: tabrik oynasi va keyingi qadam
    var was = !!(S2.done || {})[curId];
    var dlg = el("div", "kl-done");
    dlg.setAttribute("role", "dialog"); dlg.setAttribute("aria-modal", "true"); dlg.setAttribute("aria-labelledby", "klDoneT");
    dlg.innerHTML = '<div class="kl-done-c"><svg viewBox="0 0 84 84" aria-hidden="true"><circle cx="42" cy="42" r="38"/><path d="M26 43 L37 54 L59 31"/></svg><span class="kl-xp">+20 XP</span><h2 id="klDoneT">Dars ' + esc(l.num) + ' yakunlandi</h2><p>' + (i < N - 1 ? "Keyingisi: Dars " + esc(L[i + 1].num) + ". " + esc(L[i + 1].title) : "Hamma darslar oʻqildi. Endi vositalar va qaror.") + '</p><a class="btn btn-p" rel="next" data-dir="next" href="' + next[0] + '">' + (i < N - 1 ? "Keyingi darsga oʻtish" : "Yakuniy bosqichga oʻtish") + '</a><button type="button" class="btn btn-g" data-close>Shu darsda qolish</button></div>';
    body.appendChild(dlg);
    function close() { dlg.classList.remove("on"); }
    dlg.addEventListener("click", function (e) { if (e.target === dlg || e.target.hasAttribute("data-close")) close(); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") close(); });
    var cb = $("[data-complete]", art);
    if (cb) cb.addEventListener("click", function () {
      setTimeout(function () {
        var now = !!(state().done || {})[curId];
        if (now && !was) {
          was = true;
          var st = $(".kl-steps a.cur i", head); if (st) st.textContent = "✓";
          dlg.classList.add("on"); setTimeout(function () { var a = $("a", dlg); if (a) a.focus(); }, 60);
          if (window.KSfx) setTimeout(function () { KSfx.play("chime"); }, 520);
        }
      }, 80);
    });
  }

  // ═══ YAKUN ═══
  if (view === "yakun") {
    var S3 = state();
    var hd3 = el("div", "kl-lhead");
    hd3.innerHTML = crumb("Yakun") + steps(S3, "yakun") + "<h1>Yakun: vositalar, nishonlar va qaror</h1><div class=\"kl-lmeta\"><span>" + esc(M.yakunMeta) + "</span></div>";
    wrap.insertBefore(hd3, wrap.firstChild);
    var f3 = el("div", "kl-lfoot");
    f3.innerHTML = '<div class="kl-pager"><a class="pv" rel="prev" data-kkey data-dir="prev" href="' + page(N - 1) + '"><small>Oldingi dars</small><b>Dars ' + esc(L[N - 1].num) + ": " + esc(L[N - 1].title) + '</b></a><a class="nx primary" rel="next" data-kkey data-dir="next" href="' + HUB + '"><small>Modul sahifasi</small><b>' + esc(M.mod) + ": umumiy koʻrinish</b></a></div>";
    var q = $("#qaror"); (q || wrap).insertAdjacentElement("afterend", f3);
    document.title = "Yakun: vositalar va qaror · " + M.labName + " " + M.mod + " | Kompas Lab";
  }
})();
