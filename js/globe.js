// ═══════════════════════════════════════════════════════════════
//  Kompas Lab — yoʻnalishlar globusi (Canvas 2D, tashqi kutubxonasiz)
//  Ishlatish: <div class="kglobe" data-globe></div> + <script src="js/globe.js" defer></script>
//  Maʼlumot: data/globe.json (tools/globe/build_globe.py; Natural Earth 1:110m, jamoat mulki)
//  Faqat koʻrinish maydoniga kirganda ishga tushadi; prefers-reduced-motion da aylanmaydi
// ═══════════════════════════════════════════════════════════════
(function () {
  var ORIGIN = { iso: "UZB", n: "Toshkent", lat: 41.31, lon: 69.28 };
  // Lablar va mamlakatlar: index.html dagi Lab tavsiflari va Master Lab M7 asosida
  var DEST = [
    { id: "GBR", n: "Buyuk Britaniya", lat: 51.51, lon: -0.13, labs: [["master-lab", "Master Lab", "Chevening, magistratura"], ["phd-lab", "PhD Lab", "Doktorantura"], ["musofir-lab", "Musofir Lab", "Rasmiy mavsumiy ish"]] },
    { id: "USA", n: "AQSh", lat: 38.9, lon: -77.04, labs: [["usa-lab", "USA Lab", "Global UGRAD, Fulbright, doktorantura"]] },
    { id: "DEU", n: "Germaniya", lat: 52.52, lon: 13.4, labs: [["daad-lab", "DAAD Lab", "Magistratura va doktorantura"], ["musofir-lab", "Musofir Lab", "Rasmiy ish"]] },
    { id: "KOR", n: "Koreya", lat: 37.57, lon: 126.98, labs: [["gks-lab", "GKS Lab", "Global Korea Scholarship"], ["musofir-lab", "Musofir Lab", "EPS: rasmiy ish"]] },
    { id: "POL", n: "Polsha", lat: 52.23, lon: 21.01, labs: [["musofir-lab", "Musofir Lab", "Rasmiy ish va firibgarlikdan himoya"]] },
    { id: "HUN", n: "Vengriya", lat: 47.5, lon: 19.04, labs: [["master-lab", "Master Lab", "Stipendium Hungaricum (M7)"]] },
    { id: "TUR", n: "Turkiya", lat: 39.93, lon: 32.86, labs: [["master-lab", "Master Lab", "Türkiye Bursları (M7)"]] },
    { id: "CHN", n: "Xitoy", lat: 39.9, lon: 116.4, labs: [["master-lab", "Master Lab", "Xitoy hukumati stipendiyasi, CSC (M7)"]] },
    { id: "JPN", n: "Yaponiya", lat: 35.68, lon: 139.69, labs: [["master-lab", "Master Lab", "MEXT (M7)"]] }
  ];
  var R = Math.PI / 180;
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var DATA = null, WAIT = [];
  function getData(cb) {
    if (DATA) return cb(DATA);
    WAIT.push(cb); if (WAIT.length > 1) return;
    var src = (document.querySelector("[data-globe-src]") || {}).getAttribute ? document.querySelector("[data-globe-src]").getAttribute("data-globe-src") : "data/globe.json";
    fetch(src).then(function (r) { return r.json(); }).then(function (j) {
      var dots = [], rings = [], idx = {};
      j.c.forEach(function (c, i) { idx[c] = i; });
      for (var i = 0; i < j.d.length; i += 3) dots.push([j.d[i] / 10 * R, j.d[i + 1] / 10 * R, j.d[i + 2]]);
      j.r.forEach(function (f) { var x = 0, y = 0, pts = []; for (var k = 1; k < f.length; k += 2) { x += f[k]; y += f[k + 1]; pts.push([y / 10 * R, x / 10 * R]); } rings.push({ c: f[0], p: pts }); });
      DATA = { dots: dots, rings: rings, idx: idx, cap: j.cap.map(function (c) { return [c[0] * R, c[1] * R]; }), city: j.city };
      WAIT.forEach(function (f) { f(DATA); }); WAIT = [];
    }).catch(function () { WAIT = []; });
  }

  function init(root) {
    root.innerHTML = '<div class="kg-stage"><canvas aria-hidden="true"></canvas><div class="kg-zoom"><button type="button" data-z="1" aria-label="Kattalashtirish">+</button><button type="button" data-z="-1" aria-label="Kichraytirish">−</button></div></div>' +
      '<div class="kg-side"><div class="kg-list" role="list">' + DEST.map(function (d) { return '<button type="button" role="listitem" data-c="' + d.id + '">' + d.n + "</button>"; }).join("") + '</div><div class="kg-card" hidden aria-live="polite"></div></div>';
    var cv = root.querySelector("canvas"), ctx = cv.getContext("2d"), card = root.querySelector(".kg-card"), stage = root.querySelector(".kg-stage");
    var css = getComputedStyle(root);
    function tok(n, d) { return css.getPropertyValue(n).trim() || d; }
    var C = { land: tok("--kg-land", "#2d4a3e"), sea: tok("--kg-sea", "#e8f0ec"), arc: tok("--kg-arc", "#c4622d"), dim: tok("--kg-dim", "#9fb3aa") };
    var W = 0, H = 0, r0 = 0, r = 0, dpr = 1, lon0 = 40, lat0 = 30, zoom = 1, zt = 1, sel = null, t0 = performance.now(), running = false, raf = 0, drag = null, pinch = null, idleAt = 0, target = null, D = null;
    var destIdx = {}, pointers = {};
    var sp0 = 0, cp0 = 0;

    function size() {
      var w = stage.clientWidth; dpr = Math.min(w < 500 ? 1.5 : 2, window.devicePixelRatio || 1);
      W = w; H = w; cv.width = W * dpr; cv.height = H * dpr; cv.style.width = W + "px"; cv.style.height = H + "px";
      r0 = W * 0.44; draw();
    }
    // Ortografik proyeksiya: [x, y, z>0 — oldingi yarim shar]
    function proj(lat, lon) {
      var l = lon - lon0 * R, cl = Math.cos(lat), sl = Math.sin(lat);
      var x = cl * Math.sin(l), y = cp0 * sl - sp0 * cl * Math.cos(l), z = sp0 * sl + cp0 * cl * Math.cos(l);
      return [W / 2 + r * x, H / 2 - r * y, z];
    }
    function slerp(a, b, t) {
      var la1 = a.lat * R, lo1 = a.lon * R, la2 = b.lat * R, lo2 = b.lon * R;
      var x1 = Math.cos(la1) * Math.cos(lo1), y1 = Math.cos(la1) * Math.sin(lo1), z1 = Math.sin(la1), x2 = Math.cos(la2) * Math.cos(lo2), y2 = Math.cos(la2) * Math.sin(lo2), z2 = Math.sin(la2);
      var d = Math.acos(Math.max(-1, Math.min(1, x1 * x2 + y1 * y2 + z1 * z2))), s = Math.sin(d) || 1, A = Math.sin((1 - t) * d) / s, B = Math.sin(t * d) / s;
      var x = A * x1 + B * x2, y = A * y1 + B * y2, z = A * z1 + B * z2, h = 1 + 0.16 * Math.sin(Math.PI * t) / Math.sqrt(zoom);
      return [Math.atan2(z, Math.sqrt(x * x + y * y)), Math.atan2(y, x), h];
    }
    function label(txt, x, y, size, weight, color) {
      ctx.font = weight + " " + size + "px Outfit, sans-serif"; ctx.lineWidth = 3; ctx.strokeStyle = "rgba(255,255,255,.85)"; ctx.strokeText(txt, x, y); ctx.fillStyle = color; ctx.fillText(txt, x, y);
    }
    function draw() {
      sp0 = Math.sin(lat0 * R); cp0 = Math.cos(lat0 * R); r = r0 * zoom;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0); ctx.clearRect(0, 0, W, H);
      ctx.beginPath(); ctx.arc(W / 2, H / 2, r, 0, 2 * Math.PI); ctx.fillStyle = C.sea; ctx.fill();
      if (!D) return;
      var selI = sel ? D.idx[sel] : -2, orI = D.idx[ORIGIN.iso];
      // Quruqlik nuqtalari: Lab mamlakatlari quyuqroq, tanlangani toʻq sariq
      var ds = Math.max(1.2, r / 170), B = [[], [], []];
      for (var i = 0; i < D.dots.length; i++) {
        var q = D.dots[i], p = proj(q[0], q[1]); if (p[2] <= 0 || p[0] < -4 || p[0] > W + 4 || p[1] < -4 || p[1] > H + 4) continue;
        var k = q[2] === selI ? 2 : (destIdx[q[2]] || q[2] === orI) ? 1 : 0;
        B[k].push(p[0] - ds / 2, p[1] - ds / 2, p[2]);
      }
      // Nuqtalar rang va chuqurlik boʻyicha guruhlab chiziladi (har kadrda 9 ta fill)
      [C.dim, C.land, C.arc].forEach(function (col, k) {
        var a = B[k]; if (!a.length) return; ctx.fillStyle = col;
        for (var band = 0; band < 3; band++) {
          ctx.beginPath(); ctx.globalAlpha = 0.4 + 0.3 * band;
          for (var j = 0; j < a.length; j += 3) { var z = a[j + 2]; if ((z < 0.35 ? 0 : z < 0.7 ? 1 : 2) === band) ctx.rect(a[j], a[j + 1], ds, ds); }
          ctx.fill();
        }
      });
      // Davlat chegaralari
      ctx.globalAlpha = 1; ctx.lineJoin = "round";
      [false, true].forEach(function (hi) {
        ctx.beginPath();
        D.rings.forEach(function (g) {
          if ((g.c === selI) !== hi) return;
          var pen = false;
          for (var k = 0; k < g.p.length; k++) { var p = proj(g.p[k][0], g.p[k][1]); if (p[2] > 0.02) { if (pen) ctx.lineTo(p[0], p[1]); else ctx.moveTo(p[0], p[1]); pen = true; } else pen = false; }
        });
        ctx.strokeStyle = hi ? C.arc : C.land; ctx.globalAlpha = hi ? 0.95 : 0.32; ctx.lineWidth = hi ? 1.8 : 0.7; ctx.stroke();
      });
      ctx.globalAlpha = 1;
      // Boshqa poytaxtlar: mayda nuqta
      if (zoom > 1.3) { ctx.fillStyle = C.land; ctx.globalAlpha = 0.5; D.cap.forEach(function (c) { var p = proj(c[0], c[1]); if (p[2] > 0.1) ctx.fillRect(p[0] - 1.2, p[1] - 1.2, 2.4, 2.4); }); ctx.globalAlpha = 1; }
      // Yoylar
      var ph = ((performance.now() - t0) / 2600) % 1;
      DEST.forEach(function (d) {
        var on = sel === d.id; ctx.beginPath(); var pen = false;
        for (var k = 0; k <= 48; k++) {
          var q = slerp(ORIGIN, d, k / 48), p = proj(q[0], q[1]), x = W / 2 + (p[0] - W / 2) * q[2], y = H / 2 + (p[1] - H / 2) * q[2];
          if (p[2] > -0.1) { if (pen) ctx.lineTo(x, y); else ctx.moveTo(x, y); pen = true; } else pen = false;
        }
        ctx.strokeStyle = C.arc; ctx.globalAlpha = on ? 0.95 : sel ? 0.18 : 0.5; ctx.lineWidth = on ? 2.4 : 1.2; ctx.stroke(); ctx.globalAlpha = 1;
        if (!reduce && (!sel || on)) { var q2 = slerp(ORIGIN, d, ph), p2 = proj(q2[0], q2[1]); if (p2[2] > 0) { ctx.beginPath(); ctx.arc(W / 2 + (p2[0] - W / 2) * q2[2], H / 2 + (p2[1] - H / 2) * q2[2], 2.6, 0, 2 * Math.PI); ctx.fillStyle = C.arc; ctx.fill(); } }
      });
      // Shaharlar: poytaxt (halqa) va asosiy shaharlar
      var showAll = zoom >= 1.9;
      Object.keys(D.city).forEach(function (iso) {
        var isSel = iso === sel, isOr = iso === ORIGIN.iso;
        D.city[iso].forEach(function (c) {
          var p = proj(c[1] * R, c[2] * R); if (p[2] <= 0.05) return;
          var cap = c[3] === 1, big = cap && (isSel || isOr || showAll);
          if (!cap && !(isSel || (isOr && zoom >= 1.5) || showAll)) return;
          ctx.beginPath(); ctx.arc(p[0], p[1], cap ? (isSel ? 6 : 4.5) : 2.6, 0, 2 * Math.PI);
          ctx.fillStyle = cap ? (isOr ? C.land : C.arc) : "#fff"; ctx.fill(); ctx.lineWidth = cap ? 2 : 1.4; ctx.strokeStyle = cap ? "#fff" : (isOr ? C.land : C.arc); ctx.stroke();
          if (big || isSel || (isOr && zoom >= 1.5) || (showAll && !cap && zoom >= 2.4)) label(c[0] + (cap ? " ★" : ""), p[0] + 8, p[1] + 4, cap ? 12.5 : 11, cap ? 800 : 600, C.land);
        });
      });
      DEST.forEach(function (d) { d._p = proj(d.lat * R, d.lon * R); });
    }
    var slowDev = false, ft = [], lastT = 0, odd = false;
    function loop(now) {
      if (!running) return;
      if (lastT) { ft.push(now - lastT); if (ft.length > 30) { ft.shift(); slowDev = ft.reduce(function (a, b) { return a + b; }, 0) / ft.length > 26; } } lastT = now;
      var idle = !target && !drag && !pinch && Math.abs(zt - zoom) < 0.01;
      if (idle && slowDev && (odd = !odd)) { raf = requestAnimationFrame(loop); return; }
      if (target) { var dl = ((target[0] - lon0 + 540) % 360) - 180, dt = target[1] - lat0; lon0 += dl * 0.09; lat0 += dt * 0.09; if (Math.abs(dl) < 0.15 && Math.abs(dt) < 0.15) target = null; }
      else if (!drag && !pinch && !reduce && performance.now() > idleAt) lon0 += (slowDev ? 0.1 : 0.05) / zoom;
      zoom += (zt - zoom) * 0.15;
      draw(); raf = requestAnimationFrame(loop);
    }
    function start() { if (!running) { running = true; raf = requestAnimationFrame(loop); } }
    function stop() { running = false; cancelAnimationFrame(raf); }
    function setZoom(z) { zt = Math.max(1, Math.min(4, z)); idleAt = performance.now() + 5000; if (!running) { zoom = zt; draw(); } }
    function show(id) {
      sel = id; var d = DEST.filter(function (x) { return x.id === id; })[0];
      root.querySelectorAll(".kg-list button").forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-c") === id ? "true" : "false"); });
      if (!d) { card.hidden = true; setZoom(1); return; }
      var cities = D && D.city[id] ? D.city[id].map(function (c) { return c[0] + (c[3] ? " (poytaxt)" : ""); }).join(", ") : "";
      card.innerHTML = '<button type="button" class="kg-x" aria-label="Yopish">×</button><b>' + d.n + "</b>" + (cities ? '<small class="kg-c">' + cities + "</small>" : "") + d.labs.map(function (l) { return '<a href="' + l[0] + '.html"><span>' + l[1] + "</span><small>" + l[2] + "</small></a>"; }).join("") + '<small class="kg-n">Har Lab bepul M0 bilan boshlanadi.</small>';
      card.hidden = false;
      target = [d.lon, Math.max(-30, Math.min(55, d.lat))]; idleAt = performance.now() + 8000;
      setZoom(id === "USA" || id === "CHN" ? 2 : id === "GBR" || id === "KOR" || id === "HUN" || id === "POL" ? 3.2 : 2.6);
      if (!running) { lon0 = target[0]; lat0 = target[1]; target = null; draw(); }
    }
    card.addEventListener("click", function (e) { if (e.target.classList.contains("kg-x")) show(null); });
    root.querySelector(".kg-list").addEventListener("click", function (e) { var c = e.target.getAttribute("data-c"); if (c) show(sel === c ? null : c); });
    root.querySelector(".kg-zoom").addEventListener("click", function (e) { var z = +e.target.getAttribute("data-z"); if (z) setZoom(zt * (z > 0 ? 1.5 : 1 / 1.5)); });
    cv.addEventListener("pointerdown", function (e) {
      pointers[e.pointerId] = [e.clientX, e.clientY]; var ids = Object.keys(pointers);
      if (ids.length === 2) { var a = pointers[ids[0]], b = pointers[ids[1]]; pinch = { d: Math.hypot(a[0] - b[0], a[1] - b[1]), z: zt }; drag = null; }
      else drag = { x: e.clientX, y: e.clientY, lon: lon0, lat: lat0, moved: false };
      target = null;
    });
    window.addEventListener("pointermove", function (e) {
      if (!pointers[e.pointerId]) return; pointers[e.pointerId] = [e.clientX, e.clientY];
      if (pinch) { var ids = Object.keys(pointers); if (ids.length === 2) { var a = pointers[ids[0]], b = pointers[ids[1]]; setZoom(pinch.z * Math.hypot(a[0] - b[0], a[1] - b[1]) / pinch.d); } return; }
      if (!drag) return; var dx = e.clientX - drag.x, dy = e.clientY - drag.y; if (Math.abs(dx) + Math.abs(dy) > 4) drag.moved = true;
      lon0 = drag.lon - dx / r * 57; lat0 = Math.max(-70, Math.min(75, drag.lat + dy / r * 57)); if (!running) draw();
    });
    function up(e) {
      delete pointers[e.pointerId]; if (pinch) { if (!Object.keys(pointers).length) pinch = null; return; }
      if (!drag) return; var moved = drag.moved; drag = null; idleAt = performance.now() + 5000; if (moved || e.type === "pointercancel") return;
      var bx = cv.getBoundingClientRect(), x = e.clientX - bx.left, y = e.clientY - bx.top, best = null, bd = 24 * 24;
      DEST.forEach(function (d) { if (d._p && d._p[2] > 0) { var q = (d._p[0] - x) * (d._p[0] - x) + (d._p[1] - y) * (d._p[1] - y); if (q < bd) { bd = q; best = d.id; } } });
      if (best) show(best);
    }
    window.addEventListener("pointerup", up); window.addEventListener("pointercancel", up);
    cv.style.touchAction = "pan-y";
    size(); window.addEventListener("resize", size);
    getData(function (d) { D = d; DEST.forEach(function (x) { destIdx[d.idx[x.id]] = 1; }); draw(); });
    if ("IntersectionObserver" in window) new IntersectionObserver(function (es) { es[0].isIntersecting && !document.hidden ? start() : stop(); }, { rootMargin: "100px" }).observe(root);
    else start();
    document.addEventListener("visibilitychange", function () { if (document.hidden) stop(); });
    root.kglobe = { show: show };
  }
  function boot() { document.querySelectorAll("[data-globe]").forEach(init); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
