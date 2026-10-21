// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — kompas-ui.js (2026-10-18)
//  Har sahifada <head> ichida (defer emas) yuklanadi:
//  · Sahifalar orasidagi oʻtish yoʻnalishi (View Transitions: next / prev)
//  · Ichki havolalarga "nav" tovushi (sfx.js), ←/→ bilan oldingi/keyingi sahifa
//  · Lab tablari (mobil panel) va "yoʻl"dagi kompas strelkasi
// ═══════════════════════════════════════════════════════════════
(function () {
  var DIR = "kl_dir";
  // Yangi sahifa ochilganda: oldingi sahifada bosilgan havola yoʻnalishini oʻtishga qoʻshamiz
  window.addEventListener("pagereveal", function (e) {
    var d = null;
    try { d = sessionStorage.getItem(DIR); sessionStorage.removeItem(DIR); } catch (x) {}
    if (e.viewTransition && d && e.viewTransition.types) { try { e.viewTransition.types.add(d); } catch (x) {} }
  });
  function setDir(d) { try { if (d) sessionStorage.setItem(DIR, d); else sessionStorage.removeItem(DIR); } catch (x) {} }

  function internal(a) {
    if (!a || !a.getAttribute) return false;
    var h = a.getAttribute("href");
    if (!h || h.charAt(0) === "#" || a.target === "_blank" || a.hasAttribute("download")) return false;
    if (/^(mailto|tel|javascript):/i.test(h)) return false;
    try { var u = new URL(h, location.href); return u.origin === location.origin && u.pathname !== location.pathname; } catch (x) { return false; }
  }

  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[href]");
    if (!a || e.defaultPrevented || e.button || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    if (internal(a)) setDir(a.getAttribute("data-dir") || a.getAttribute("rel") === "next" && "next" || a.getAttribute("rel") === "prev" && "prev" || "");
  }, true);

  function ready(fn) { if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", fn); else fn(); }

  ready(function () {
    // Ichki havolalar: tovush (sfx.js [data-snd] ni oʻzi chaladi)
    document.querySelectorAll("a[href]").forEach(function (a) { if (!a.hasAttribute("data-snd") && internal(a)) a.setAttribute("data-snd", "nav"); });

    // Mobil tab paneli
    var bar = document.querySelector(".kl-tabbar");
    if (bar) {
      document.body.classList.add("kl-has-tabs");
      var cur = bar.querySelector('[aria-current="page"]');
      if (cur && bar.firstElementChild) { var t = bar.firstElementChild; t.scrollLeft = cur.offsetLeft - (t.clientWidth - cur.clientWidth) / 2; }
    }

    // ←/→: oldingi va keyingi sahifa (dars va modul sahifalarida)
    document.addEventListener("keydown", function (e) {
      if (e.metaKey || e.ctrlKey || e.altKey || e.shiftKey) return;
      var t = e.target; if (t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName))) return;
      var rel = e.key === "ArrowRight" ? "next" : e.key === "ArrowLeft" ? "prev" : "";
      if (!rel) return;
      var a = document.querySelector('a[rel="' + rel + '"][data-kkey]');
      if (a) { setDir(rel); if (window.KSfx) KSfx.play("nav"); location.href = a.href; }
    });

    needles();
    window.addEventListener("resize", function () { clearTimeout(needles.t); needles.t = setTimeout(needles, 150); });
  });

  // Kompas strelkasi joriy bekatda turadi
  var SVG = '<svg viewBox="0 0 44 44" aria-hidden="true"><circle cx="22" cy="22" r="20" fill="#fffefb" stroke="#c4622d" stroke-width="2.5"/><circle cx="22" cy="22" r="15.5" fill="none" stroke="#e2ded3" stroke-dasharray="1.5 3.2"/><g class="kn"><path d="M22 18.6 L37 22 L22 25.4 Z" fill="#c4622d"/><path d="M22 18.6 L7 22 L22 25.4 Z" fill="#2d4a3e"/><circle cx="22" cy="22" r="2.6" fill="#fffefb" stroke="#2d4a3e" stroke-width="1.4"/></g></svg>';
  function needles() {
    document.querySelectorAll(".kl-route[data-needle]").forEach(function (r) {
      var st = r.querySelector(".kl-st.is-here, .kl-st.is-current");
      var n = r.querySelector(".kl-route-needle");
      if (!st) { if (n) n.remove(); r.classList.remove("has-needle"); return; }
      var dot = st.querySelector(".kl-st-n"); if (!dot) return;
      if (!n) { n = document.createElement("span"); n.className = "kl-route-needle"; n.innerHTML = SVG; r.appendChild(n); }
      var rr = r.getBoundingClientRect(), dr = dot.getBoundingClientRect();
      n.style.top = (dr.top - rr.top + (dr.height - n.offsetHeight) / 2) + "px";
      n.style.left = (dr.left - rr.left + (dr.width - n.offsetWidth) / 2) + "px";
      r.classList.add("has-needle");
    });
  }
  window.KUI = { needles: needles, setDir: setDir };
})();
