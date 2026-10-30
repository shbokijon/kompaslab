// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — k4.js (2026-10-30): bosh sahifadagi "4K yoʻli" animatsiyasi
//  · Kompas strelkasi bekatlar boʻylab yuradi: Kirish → Ketish → Kampus → Karyera.
//    Tutash chiziq tayyor qism (1–2), uzuq chiziq rejadagi qism (2–4).
//  · Boʻlim ekranga kirganda bir marta oʻynaydi; bekat yoki kartani bosish strelkani oʻsha joyga olib boradi.
//  · Tovush: sfx.js (KSfx.play k1–k4, k4end). Brauzer qoidasi boʻyicha sahifada biror marta
//    bosilmaguncha tovush chiqmaydi; foydalanuvchi 🔇 qilgan boʻlsa — jim.
//  · prefers-reduced-motion: harakatsiz, hamma bekat darhol ochiq.
// ═══════════════════════════════════════════════════════════════
(function () {
  var sec = document.getElementById("yol-4k");
  if (!sec) return;
  var stage = sec.querySelector(".k4x-stage"), svg = sec.querySelector(".k4x-svg");
  var base = svg.querySelector(".k4x-base"), done = svg.querySelector(".k4x-done"), plan = svg.querySelector(".k4x-plan"), mask = svg.querySelector(".k4x-mask");
  var grad = svg.querySelector("#k4xGrad");
  var trav = sec.querySelector(".k4x-trav"), needle = trav.querySelector(".k4x-needle");
  var items = [].slice.call(sec.querySelectorAll(".k4x-s"));
  var READY = 2;                       // 1–2 bekat tayyor, keyingilari rejada
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var pts = [], lens = [], total = 0, cur = 0, raf = 0, at = -1, played = false;

  function snd(n) { if (window.KSfx) window.KSfx.play(n); }

  function measure() {
    var r = stage.getBoundingClientRect();
    svg.setAttribute("viewBox", "0 0 " + r.width + " " + r.height);
    pts = items.map(function (li) {
      var d = li.querySelector(".k4x-dot").getBoundingClientRect();
      return { x: d.left - r.left + d.width / 2, y: d.top - r.top + d.height / 2 };
    });
    var d = "M" + pts.map(function (p) { return p.x.toFixed(1) + " " + p.y.toFixed(1); }).join(" L");
    [base, mask].forEach(function (p) { p.setAttribute("d", d); });
    plan.setAttribute("d", "M" + pts.slice(READY - 1).map(function (p) { return p.x.toFixed(1) + " " + p.y.toFixed(1); }).join(" L"));
    lens = [0];
    for (var i = 1; i < pts.length; i++) lens.push(lens[i - 1] + Math.hypot(pts[i].x - pts[i - 1].x, pts[i].y - pts[i - 1].y));
    total = lens[lens.length - 1];
    done.setAttribute("d", "M" + pts.slice(0, READY).map(function (p) { return p.x.toFixed(1) + " " + p.y.toFixed(1); }).join(" L"));
    grad.setAttribute("x1", pts[0].x); grad.setAttribute("y1", pts[0].y);
    grad.setAttribute("x2", pts[READY - 1].x); grad.setAttribute("y2", pts[READY - 1].y);
    draw(cur);
  }

  function pointAt(t) {
    for (var i = 1; i < pts.length; i++) {
      if (t <= lens[i] || i === pts.length - 1) {
        var seg = lens[i] - lens[i - 1] || 1, k = Math.max(0, Math.min(1, (t - lens[i - 1]) / seg));
        return { x: pts[i - 1].x + (pts[i].x - pts[i - 1].x) * k, y: pts[i - 1].y + (pts[i].y - pts[i - 1].y) * k,
                 a: Math.atan2(pts[i].y - pts[i - 1].y, pts[i].x - pts[i - 1].x) };
      }
    }
    return { x: 0, y: 0, a: 0 };
  }

  function draw(t) {
    cur = t;
    var l1 = lens[READY - 1] || 0;
    done.style.strokeDasharray = l1 + " " + l1;
    done.style.strokeDashoffset = String(Math.max(0, l1 - Math.min(t, l1)));
    mask.style.strokeDasharray = total + " " + total;
    mask.style.strokeDashoffset = String(total - t);
    var p = pointAt(t);
    trav.style.transform = "translate(" + p.x.toFixed(1) + "px," + p.y.toFixed(1) + "px)";
    return p;
  }

  function arrive(i, quiet) {
    at = i;
    items.forEach(function (li, j) { li.classList.toggle("on", j <= i || li.classList.contains("seen")); li.classList.toggle("here", j === i); });
    items[i].classList.add("seen");
    needle.style.transform = "rotate(" + (i % 2 ? -8 : 8) + "deg)";
    setTimeout(function () { needle.style.transform = "rotate(0deg)"; }, 260);
    if (!quiet) { snd("k" + (i + 1)); sparks(pts[i], i < READY ? "#2d4a3e" : "#c9a84c"); }
  }

  function sparks(p, color) {
    if (reduce) return;
    for (var k = 0; k < 10; k++) {
      var s = document.createElement("i"), ang = Math.PI * 2 * k / 10 + Math.random() * 0.4, dist = 22 + Math.random() * 18;
      s.className = "k4x-spark";
      s.style.left = p.x + "px"; s.style.top = p.y + "px";
      s.style.background = k % 3 ? color : "#c4622d";
      s.style.setProperty("--dx", (Math.cos(ang) * dist).toFixed(1) + "px");
      s.style.setProperty("--dy", (Math.sin(ang) * dist).toFixed(1) + "px");
      stage.appendChild(s);
      setTimeout(function (n) { return function () { n.remove(); }; }(s), 950);
    }
  }

  function ease(x) { return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; }

  // Strelkani bitta bekatdan keyingisiga olib boradi (oraliq bekatlarda ham toʻxtab oʻtadi)
  function travel(to, cb) {
    cancelAnimationFrame(raf);
    trav.classList.add("go");
    if (reduce) { draw(lens[to]); arrive(to, true); if (cb) cb(); return; }
    var from = at < 0 ? 0 : at;
    if (at < 0) { draw(0); arrive(0); if (to === 0) { if (cb) cb(); return; } }
    var step = to > from ? 1 : -1, next = from + step;
    if (from === to) { arrive(to); if (cb) cb(); return; }
    var t0 = lens[from], t1 = lens[next], dur = 700, start = null;
    trav.classList.add("moving");
    function frame(ts) {
      if (start === null) start = ts;
      var k = Math.min(1, (ts - start) / dur), p = draw(t0 + (t1 - t0) * ease(k));
      needle.style.transform = "rotate(" + (p.a * 180 / Math.PI + 90).toFixed(1) + "deg)";
      if (k < 1) { raf = requestAnimationFrame(frame); return; }
      trav.classList.remove("moving");
      arrive(next);
      if (next !== to) setTimeout(function () { travel(to, cb); }, 260);
      else if (cb) cb();
    }
    raf = requestAnimationFrame(frame);
  }

  function playAll() {
    played = true;
    items.forEach(function (li) { li.classList.remove("on", "here", "seen"); });
    at = -1; draw(0);
    travel(items.length - 1, function () { setTimeout(function () { snd("k4end"); }, 220); });
  }

  items.forEach(function (li, i) {
    function go(e) {
      if (e && e.target.closest("a")) return;   // kartadagi havola oʻz ishini qiladi
      if (!played) played = true;
      travel(i);
    }
    li.querySelector(".k4x-dot").addEventListener("click", go);
    li.querySelector(".k4x-card").addEventListener("click", go);
  });
  sec.querySelector(".k4x-replay").addEventListener("click", playAll);

  var rt = 0;
  window.addEventListener("resize", function () { clearTimeout(rt); rt = setTimeout(function () { measure(); if (at >= 0) draw(lens[at]); }, 120); });

  function init() {
    measure();
    if (reduce) { trav.classList.add("go"); draw(total); items.forEach(function (li) { li.classList.add("on", "seen"); }); items[items.length - 1].classList.add("here"); at = items.length - 1; return; }
    if (!("IntersectionObserver" in window)) { playAll(); return; }
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting && !played) { io.disconnect(); setTimeout(playAll, 250); } });
    }, { threshold: 0.35 });
    io.observe(stage);
  }
  if (document.readyState === "complete") init(); else window.addEventListener("load", init);
})();
