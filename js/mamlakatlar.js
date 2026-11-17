// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — mamlakatlar.js (2026-11-17, v2)
//  mamlakatlar.html: SVG dunyo xaritasi (kutubxonasiz) + mamlakat kartasi.
//  Chegaralar: data/globe.json (Natural Earth 1:110m). Raqamlar: #mx-cfg
//  (tools/atlas/build_site.py, manba tools/atlas/mamlakatlar_data.py).
//  Xarita qatlamlari (doira + raqam): talabalar | flow (2025 Oʻzbekistondan) | qs.
//  Hudud: Dunyo / Yevropa / Osiyo (viewBox animatsiyasi).
//  Karta: 3 ta asosiy raqam (sanab chiqadi) + boʻlim tablari, izoh ⓘ ostida.
//  prefers-reduced-motion: animatsiyasiz. Tanlov saqlanmaydi.
// ═══════════════════════════════════════════════════════════════
(function () {
  var root = document.getElementById("mxMap"), cfgEl = document.getElementById("mx-cfg"), card = document.getElementById("mxCard");
  if (!root || !cfgEl || !card) return;
  var C = JSON.parse(cfgEl.textContent);
  var W = 1000, LAT0 = 84, LAT1 = -58, H = Math.round((LAT0 - LAT1) / 360 * W);
  var NS = "http://www.w3.org/2000/svg";
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var tip = document.getElementById("mxTip"), legend = document.getElementById("mxLegend");
  var mobile = window.matchMedia && window.matchMedia("(max-width: 640px)").matches;
  // Telefonda boshlangʻich kesim: Amerika sharqi → Yaponiya, Shimoliy qutb va Janubiy okeansiz (balandroq xarita)
  var ZOOM = { world: [0, 0, W, H], eu: box(-13, 34, 33, 62), as: box(52, -12, 150, 56), start: mobile ? box(-62, -44, 150, 74) : [0, 0, W, H] };
  var homeDot, layer = "talabalar", sel = null, tab = null, shapes = {}, svg, gMap, gBub, arc, plane, vb = ZOOM.start.slice(), anim = 0, planeRaf = 0;

  function px(lon, lat) { return [(lon + 180) / 360 * W, (LAT0 - Math.max(LAT1, Math.min(LAT0, lat))) / 360 * W]; }
  function box(lo0, la0, lo1, la1) { var a = px(lo0, la1), b = px(lo1, la0); return [a[0], a[1], b[0] - a[0], b[1] - a[1]]; }
  function el(n, a) { var e = document.createElementNS(NS, n); for (var k in a) e.setAttribute(k, a[k]); return e; }
  function fmt(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, " "); }
  function short(n) {
    if (n >= 1e6) return (Math.round(n / 1e4) / 100).toString().replace(".", ",") + " mln";
    if (n >= 1e4) return Math.round(n / 1000) + " ming";
    return fmt(n);
  }
  function conv(t) { return window.KAlifbo && window.KAlifbo.conv ? window.KAlifbo.conv(t) : t; }
  function esc(t) { return String(t).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function snd(n) { if (window.KSfx && KSfx.play) try { KSfx.play(n); } catch (e) {} }
  function isoOf(t) {
    for (var i = 0; i < 3 && t && t.getAttribute; i++, t = t.parentNode) { var v = t.getAttribute("data-iso"); if (v) return v; }
    return null;
  }

  // ---------------------------------------------------------- xarita
  function build(j) {
    var paths = {};
    j.r.forEach(function (f) {
      var iso = j.c[f[0]], x = 0, y = 0, d = "", prev = null;
      for (var k = 1; k < f.length; k += 2) {
        x += f[k]; y += f[k + 1];
        var lon = x / 10, p = px(lon, y / 10);
        d += (prev === null || Math.abs(lon - prev) > 180 ? "M" : "L") + p[0].toFixed(1) + " " + p[1].toFixed(1);
        prev = lon;
      }
      paths[iso] = (paths[iso] || "") + d + "Z";
    });
    svg = el("svg", { viewBox: vb.join(" "), role: "img", "aria-label": conv("Dunyo xaritasi") });
    gMap = el("g", {});
    Object.keys(paths).forEach(function (iso) { var p = el("path", { d: paths[iso], "data-iso": iso }); gMap.appendChild(p); shapes[iso] = p; });
    Object.keys(C.points || {}).forEach(function (iso) {
      var ll = C.points[iso], c = px(ll[1], ll[0]), p = el("circle", { cx: c[0], cy: c[1], r: 3, "data-iso": iso });
      gMap.appendChild(p); shapes[iso] = p;
    });
    svg.appendChild(gMap);
    arc = el("path", { class: "mx-arc", d: "" }); svg.appendChild(arc);
    gBub = el("g", { class: "mx-bubs" }); svg.appendChild(gBub);
    var h = px(C.home_ll[1], C.home_ll[0]);
    homeDot = el("circle", { cx: h[0], cy: h[1], r: 4, class: "mx-home" }); svg.appendChild(homeDot);
    plane = el("image", { href: "img/3d/plane.webp", width: 22, height: 22, class: "mx-plane", visibility: "hidden" }); svg.appendChild(plane);
    var l = root.querySelector(".mx-load"); if (l) l.remove();
    root.insertBefore(svg, tip);
    svg.addEventListener("mousemove", hover);
    svg.addEventListener("mouseleave", function () { tip.hidden = true; });
    svg.addEventListener("click", function (e) { if (dragged) return; var iso = isoOf(e.target); if (iso && C.c[iso]) pick(iso); });
    // Barmoq yoki sichqoncha bilan surish (gorizontal); vertikal aylantirish sahifaga qoladi (touch-action: pan-y)
    var drag = null, dragged = false;
    svg.addEventListener("pointerdown", function (e) { drag = { x: e.clientX, y: e.clientY, vb: vb.slice() }; dragged = false; });
    window.addEventListener("pointermove", function (e) {
      if (!drag) return;
      var k = vb[2] / svg.getBoundingClientRect().width, dx = (e.clientX - drag.x) * k, dy = (e.clientY - drag.y) * k;
      if (!dragged && Math.abs(e.clientX - drag.x) < 6 && Math.abs(e.clientY - drag.y) < 6) return;
      dragged = true; tip.hidden = true;
      vb[0] = clamp(drag.vb[0] - dx, 0, W - vb[2]); vb[1] = clamp(drag.vb[1] - dy, 0, H - vb[3]);
      svg.setAttribute("viewBox", vb.join(" "));
    });
    window.addEventListener("pointerup", function () { if (drag && dragged) setTimeout(function () { dragged = false; }, 0); drag = null; });
    window.addEventListener("pointercancel", function () { drag = null; dragged = false; });
    paint(true);
  }

  // 1 ekran pikseli = necha xarita birligi (doira va yozuv ekranda bir xil oʻlchamda qoladi)
  function clamp(v, a, b) { return Math.max(a, Math.min(b, v)); }
  function scale() { var w = svg && svg.getBoundingClientRect().width; return w ? vb[2] / w : vb[2] / W; }
  function mval(iso) { var m = C.m[layer][iso]; return layer === "flow" ? m[1] : m[0]; }

  function paint(grow) {
    var m = C.m[layer], s = scale();
    Object.keys(shapes).forEach(function (iso) {
      var cls = "mx-land";
      if (iso === C.home) cls += " is-home";
      else if (layer === "flow" ? m[iso] : C.c[iso]) cls += " is-on";
      if (iso === sel) cls += " is-sel";
      shapes[iso].setAttribute("class", cls);
    });
    homeDot.setAttribute("r", (5 * s).toFixed(2)); homeDot.style.strokeWidth = (2 * s).toFixed(2);
    gMap.style.strokeWidth = (0.6 * s).toFixed(3);
    while (gBub.firstChild) gBub.removeChild(gBub.firstChild);
    var max = Math.max.apply(null, Object.keys(m).map(mval)), boxes = [];
    Object.keys(m).sort(function (a, b) { return mval(b) - mval(a); }).forEach(function (iso, i) {
      var a = C.anchors[iso]; if (!a) return;
      var p = px(a[1], a[0]), v = mval(iso), r, txt;
      if (layer === "qs") { r = (6 + 12 * Math.sqrt((100 - v) / 99)) * s; txt = "#" + v; }
      else { r = (5 + 19 * Math.sqrt(v / max)) * s; txt = short(v); }
      // yozuvlar ustma-ust tushsa, kichigining yozuvi yashiriladi (doira qoladi, raqam kartada va tooltipda)
      var fs = 12 * s, tw = txt.length * fs * 0.58, ty = p[1] + r + fs, bx = [p[0] - tw / 2, ty - fs, p[0] + tw / 2, ty + fs * 0.3];
      var clash = boxes.some(function (o) { return bx[0] < o[2] && bx[2] > o[0] && bx[1] < o[3] && bx[3] > o[1]; });
      var g = el("g", { class: "mx-bub" + (iso === sel ? " is-sel" : ""), "data-iso": iso, transform: "translate(" + p[0].toFixed(1) + " " + p[1].toFixed(1) + ")" });
      var c = el("circle", { r: r.toFixed(2) });
      g.appendChild(c);
      if (!clash) {
        var t = el("text", { y: (r + fs).toFixed(2), "font-size": fs.toFixed(2), "stroke-width": (3 * s).toFixed(2) });
        t.textContent = txt; g.appendChild(t); boxes.push(bx);
      }
      if (grow && !reduce) { c.style.animationDelay = (i * 45) + "ms"; g.classList.add("grow"); }
      gBub.appendChild(g);
    });
    legend.textContent = conv({
      talabalar: "Doira qancha katta, xalqaro talaba shuncha koʻp. Yillar har xil: aniq davr kartada.",
      flow: "2025-yilda Oʻzbekistondan oʻqish uchun ketganlar, top-10 (Milliy statistika qoʻmitasi).",
      qs: "Mamlakatdagi eng yuqori oʻrindagi universitet, QS 2027. Doira qancha katta, oʻrin shuncha yuqori."
    }[layer]);
    drawArc(false);
  }

  function info(iso) {
    var m = C.m[layer][iso], n = (C.c[iso] && C.c[iso].n) || (C.m.flow[iso] && C.m.flow[iso][0]);
    if (!n) return null;
    if (!m) return C.c[iso] ? n : null;
    if (layer === "flow") return n + ": " + fmt(m[1]) + " kishi (2025)";
    if (layer === "qs") return n + ": " + m[1] + ", " + m[0] + "-oʻrin";
    return n + ": " + fmt(m[0]) + " (" + m[1] + ")";
  }
  function hover(e) {
    var iso = isoOf(e.target), s = iso && info(iso);
    if (!s) { tip.hidden = true; return; }
    var r = root.getBoundingClientRect();
    tip.textContent = conv(s); tip.hidden = false;
    var x = e.clientX - r.left + 12, y = e.clientY - r.top + 12;
    if (x + tip.offsetWidth > r.width) x = e.clientX - r.left - tip.offsetWidth - 12;
    tip.style.left = x + "px"; tip.style.top = y + "px";
  }

  function zoomTo(key, target) {
    var from = vb.slice(), to = target || ZOOM[key], t0 = performance.now(), dur = reduce ? 0 : 650;
    cancelAnimationFrame(anim);
    (function step(now) {
      var k = dur ? Math.min(1, (now - t0) / dur) : 1, e = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2;
      for (var i = 0; i < 4; i++) vb[i] = from[i] + (to[i] - from[i]) * e;
      svg.setAttribute("viewBox", vb.join(" "));
      if (k < 1) anim = requestAnimationFrame(step); else paint(false);
    })(t0);
  }

  function drawArc(fly) {
    if (!arc) return;
    var a = px(C.home_ll[1], C.home_ll[0]), an = sel && sel !== C.home && C.anchors[sel], b = an && px(an[1], an[0]);
    cancelAnimationFrame(planeRaf);
    if (!b) { arc.setAttribute("d", ""); plane.setAttribute("visibility", "hidden"); return; }
    var mx = (a[0] + b[0]) / 2, my = Math.min(a[1], b[1]) - Math.abs(a[0] - b[0]) * 0.22 - 10;
    arc.setAttribute("d", "M" + a[0].toFixed(1) + " " + a[1].toFixed(1) + "Q" + mx.toFixed(1) + " " + my.toFixed(1) + " " + b[0].toFixed(1) + " " + b[1].toFixed(1));
    arc.style.strokeWidth = (2 * scale()).toFixed(2);
    var sz = 22 * scale();
    plane.setAttribute("width", sz); plane.setAttribute("height", sz);
    function at(t) {
      var u = 1 - t, x = u * u * a[0] + 2 * u * t * mx + t * t * b[0], y = u * u * a[1] + 2 * u * t * my + t * t * b[1];
      var dx = 2 * u * (mx - a[0]) + 2 * t * (b[0] - mx), dy = 2 * u * (my - a[1]) + 2 * t * (b[1] - my);
      var back = dx < 0, ang = Math.atan2(dy, dx) * 180 / Math.PI + (back ? 180 : 0);
      plane.setAttribute("transform", "translate(" + x.toFixed(1) + " " + y.toFixed(1) + ") rotate(" + ang.toFixed(1) + ")" + (back ? " scale(-1 1)" : "") + " translate(" + (-sz / 2) + " " + (-sz / 2) + ")");
    }
    plane.setAttribute("visibility", "visible");
    if (!fly || reduce) { at(1); return; }
    var t0 = performance.now();
    (function step(now) { var k = Math.min(1, (now - t0) / 1300); at(1 - Math.pow(1 - k, 3)); if (k < 1) planeRaf = requestAnimationFrame(step); })(t0);
  }

  // ---------------------------------------------------------- karta
  function countUp(node) {
    var to = +node.getAttribute("data-to"), t0 = performance.now(), dur = 900;
    if (reduce || !to) { node.textContent = fmt(to); return; }
    (function step(now) { var k = Math.min(1, (now - t0) / dur), e = 1 - Math.pow(1 - k, 3); node.textContent = fmt(Math.round(to * e)); if (k < 1) requestAnimationFrame(step); })(t0);
  }
  function vhtml(v, unit) {
    var u = unit ? " <small>" + esc(unit) + "</small>" : "";
    return typeof v === "number" ? '<b class="mx-num" data-to="' + v + '">' + fmt(v) + "</b>" + u : "<b>" + esc(v) + "</b>" + u;
  }
  function render(fresh) {
    var c = C.c[sel], rows = c.rows, groups = C.groups.filter(function (g) { return rows.some(function (r) { return r[0] === g; }); });
    if (!tab || groups.indexOf(tab) < 0) tab = groups[0];
    var kpi = c.kpi.map(function (i) {
      var r = rows[i];
      return '<div class="mx-kpi"><img src="img/3d/' + C.icons[r[0]] + '.webp" alt="" width="40" height="40">' + vhtml(r[2], r[3]) + '<span title="' + esc(r[1]) + '">' + esc(r[1]) + "</span><em>" + esc(r[4]) + "</em></div>";
    }).join("");
    var tabs = groups.map(function (g) {
      return '<button type="button" role="tab" class="mx-tab" data-g="' + esc(g) + '" aria-selected="' + (g === tab) + '"><img src="img/3d/' + C.icons[g] + '.webp" alt="" width="24" height="24">' + esc(g) + "</button>";
    }).join("");
    var items = rows.map(function (r, i) {
      if (r[0] !== tab) return "";
      var id = "mxn" + i;
      return '<li class="mx-item"><div class="mx-it-h"><span>' + esc(r[1]) + '</span><button type="button" class="mx-i" aria-expanded="false" aria-controls="' + id + '" aria-label="Izoh va manba">i</button></div>' +
        '<div class="mx-it-v">' + vhtml(r[2], r[3]) + "<em>" + esc(r[4]) + "</em></div>" +
        '<div class="mx-more" id="' + id + '" hidden>' + (r[7] ? "<p>" + esc(r[7]) + "</p>" : "") +
        '<a href="' + esc(r[6]) + '" target="_blank" rel="noopener">' + esc(r[5]) + " ↗</a></div></li>";
    }).join("");
    var head = sel === C.home ? "Siz shu yerdan boshlaysiz. Xaritadan mamlakat tanlang." : "Rasmiy koʻrsatkichlar: " + rows.length;
    var lab = c.lab ? '<a class="mx-lab" href="' + c.lab + '" data-snd="nav">' + esc(c.lab_n) + ": shu yoʻnalish boʻyicha tayyorlov →</a>" : "";
    var ctl = mobile && sel !== C.home ? '<div class="mx-sh-ctl"><button type="button" class="mx-sh-grip" data-sheet="toggle" aria-expanded="false" aria-label="Kartani kattalashtirish"></button><button type="button" class="mx-sh-x" data-sheet="close" aria-label="Yopish">×</button></div>' : "";
    card.innerHTML = ctl + '<div class="mx-card-in"><header class="mx-ch"><span class="mx-f" aria-hidden="true">' + c.f + "</span><div><h2>" + esc(c.n) + "</h2><p>" + esc(head) + "</p></div></header>" +
      '<div class="mx-kpis">' + kpi + "</div>" +
      (groups.length > 1 ? '<div class="mx-tabs" role="tablist">' + tabs + "</div>" : "") +
      '<ul class="mx-items" role="tabpanel">' + items + "</ul>" + lab + "</div>";
    if (fresh) card.querySelectorAll(".mx-kpi .mx-num").forEach(countUp);
    if (fresh && !reduce) { card.classList.remove("in"); void card.offsetWidth; card.classList.add("in"); }
  }
  card.addEventListener("click", function (e) {
    var t = e.target.closest("button"); if (!t) return;
    if (t.classList.contains("mx-tab")) {
      tab = t.getAttribute("data-g"); snd("pick"); render();
      var f = card.querySelector('.mx-tab[aria-selected="true"]'); if (f) f.focus();
    } else if (t.classList.contains("mx-i")) {
      var m = document.getElementById(t.getAttribute("aria-controls")), open = m.hidden;
      m.hidden = !open; t.setAttribute("aria-expanded", open ? "true" : "false");
    }
  });
  card.addEventListener("keydown", function (e) {
    if (!e.target.classList.contains("mx-tab") || (e.key !== "ArrowRight" && e.key !== "ArrowLeft")) return;
    var ts = [].slice.call(card.querySelectorAll(".mx-tab")), i = ts.indexOf(e.target) + (e.key === "ArrowRight" ? 1 : -1);
    ts[(i + ts.length) % ts.length].click();
  });

  function pick(iso, quiet) {
    if (!C.c[iso]) return;
    sel = iso; tab = null;
    document.querySelectorAll(".mx-chip").forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-iso") === iso ? "true" : "false"); });
    render(true);
    if (!quiet) { snd("pick"); sheet(true); if (!mobile && window.innerWidth < 860) card.scrollIntoView({ block: "start", behavior: reduce ? "auto" : "smooth" }); }
    if (svg) {
      paint(false); drawArc(!quiet);
      // tanlangan mamlakat koʻrinishdan tashqarida boʻlsa, xarita unga suriladi
      var an = C.anchors[iso], q = an && px(an[1], an[0]);
      if (q && (q[0] < vb[0] + vb[2] * .08 || q[0] > vb[0] + vb[2] * .92 || q[1] < vb[1] || q[1] > vb[1] + vb[3])) {
        var to = [clamp(q[0] - vb[2] / 2, 0, W - vb[2]), clamp(q[1] - vb[3] / 2, 0, H - vb[3]), vb[2], vb[3]];
        zoomTo(null, to);
      }
    }
  }

  document.querySelectorAll(".mx-chip").forEach(function (b) { b.addEventListener("click", function () { pick(b.getAttribute("data-iso")); }); });
  document.querySelectorAll(".mx-layer").forEach(function (b) {
    b.addEventListener("click", function () {
      layer = b.getAttribute("data-layer");
      document.querySelectorAll(".mx-layer").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      snd("pick"); if (svg) paint(true);
    });
  });
  document.querySelectorAll("[data-zoom]").forEach(function (b) {
    b.addEventListener("click", function () {
      document.querySelectorAll("[data-zoom]").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      if (svg) zoomTo(b.getAttribute("data-zoom"));
    });
  });

  // ---------------------------------------------------------- telefon: pastki panel
  var sheetOn = false, mapSeen = true;
  function sheet(open) {
    if (!mobile) return;
    if (open !== undefined) sheetOn = open && sel !== C.home;
    var on = sheetOn && mapSeen;
    card.classList.toggle("is-sheet", on);
    document.body.classList.toggle("mx-sheet-on", on);
    if (!on) card.classList.remove("is-full");
  }
  if (mobile) {
    if ("IntersectionObserver" in window) new IntersectionObserver(function (es) { mapSeen = es[0].isIntersecting; sheet(); }, { threshold: 0.25 }).observe(root);
    card.addEventListener("click", function (e) {
      var t = e.target.closest("[data-sheet]"); if (!t) return;
      if (t.getAttribute("data-sheet") === "close") sheet(false);
      else { card.classList.toggle("is-full"); t.setAttribute("aria-expanded", card.classList.contains("is-full") ? "true" : "false"); }
    });
  }

  // ---------------------------------------------------------- diagrammalar
  var ch = document.querySelector(".mx-charts");
  if (ch) {
    var tabs = ch.querySelectorAll("[data-chart][role=tab]"), pans = ch.querySelectorAll(".mx-cpanel");
    var still = matchMedia("(prefers-reduced-motion: reduce)").matches;
    ch.classList.add("mx-js");
    function showChart(k) {
      tabs.forEach(function (t) { t.setAttribute("aria-selected", t.getAttribute("data-chart") === k ? "true" : "false"); });
      pans.forEach(function (p) {
        var on = p.getAttribute("data-chart") === k;
        p.hidden = !on;
        if (on && !still) { p.classList.add("mx-anim"); void p.offsetWidth; requestAnimationFrame(function () { p.classList.remove("mx-anim"); }); }
      });
    }
    tabs.forEach(function (t) { t.addEventListener("click", function () { showChart(t.getAttribute("data-chart")); snd("tab"); }); });
    pans.forEach(function (p, i) { p.hidden = i > 0; if (!still) p.classList.add("mx-anim"); });
    if (!still && "IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (es) {
        if (!es[0].isIntersecting) return; io.disconnect();
        pans.forEach(function (p) { if (!p.hidden) p.classList.remove("mx-anim"); });
      }, { threshold: 0.3 });
      io.observe(ch);
    } else pans.forEach(function (p) { p.classList.remove("mx-anim"); });
    ch.addEventListener("click", function (e) {
      var b = e.target.closest("button.mx-row"); if (!b) return;
      pick(b.getAttribute("data-iso"));
      document.querySelector(".mx-grid").scrollIntoView({ behavior: still ? "auto" : "smooth", block: "start" });
    });
  }

  var rz = 0;
  window.addEventListener("resize", function () { clearTimeout(rz); rz = setTimeout(function () { if (svg) paint(false); }, 150); });

  if (mobile) document.querySelectorAll("[data-zoom]").forEach(function (b) { b.setAttribute("aria-pressed", "false"); });
  pick(C.home, true);
  fetch(root.getAttribute("data-globe-src") || "data/globe.json").then(function (r) { if (!r.ok) throw r.status; return r.json(); }).then(build).catch(function () {
    var l = root.querySelector(".mx-load"); if (l) l.textContent = conv("Xarita yuklanmadi. Mamlakatni pastdagi tugmalardan tanlang.");
  });
})();
