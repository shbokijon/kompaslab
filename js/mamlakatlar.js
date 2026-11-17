// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — mamlakatlar.js (2026-11-17)
//  mamlakatlar.html dagi dunyo xaritasi (SVG, kutubxonasiz).
//  Chegaralar: data/globe.json (tools/globe/build_globe.py, Natural Earth 1:110m).
//  Raqamlar sahifaning oʻzida (details.mx-c), sozlama #mx-cfg (build_site.py yozadi).
//  Qatlamlar: "atlas" — maʼlumot bor mamlakatlar; "flow" — 2025-yilda Oʻzbekistondan
//  oʻqishga ketganlar (top-10). Tanlov localStorage da saqlanmaydi.
// ═══════════════════════════════════════════════════════════════
(function () {
  var root = document.getElementById("mxMap");
  var cfgEl = document.getElementById("mx-cfg");
  if (!root || !cfgEl) return;
  var CFG = JSON.parse(cfgEl.textContent);
  var W = 1000, LAT0 = 84, LAT1 = -58, H = Math.round((LAT0 - LAT1) / 360 * W);
  var NS = "http://www.w3.org/2000/svg";
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var tip = document.getElementById("mxTip"), legend = document.getElementById("mxLegend");
  var layer = "atlas", sel = null, shapes = {}, centers = {}, svg, arc, gMap;

  function px(lon, lat) { return [(lon + 180) / 360 * W, (LAT0 - Math.max(LAT1, Math.min(LAT0, lat))) / 360 * W]; }
  function el(n, a) { var e = document.createElementNS(NS, n); for (var k in a) e.setAttribute(k, a[k]); return e; }
  function fmt(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, " "); }
  function conv(t) { return window.KAlifbo && window.KAlifbo.conv ? window.KAlifbo.conv(t) : t; }

  function build(j) {
    var paths = {}, box = {};
    j.r.forEach(function (f) {
      var iso = j.c[f[0]], x = 0, y = 0, d = "", prev = null, bb = [1e9, 1e9, -1e9, -1e9], n = 0;
      for (var k = 1; k < f.length; k += 2) {
        x += f[k]; y += f[k + 1];
        var lon = x / 10, lat = y / 10, p = px(lon, lat);
        d += (prev === null || Math.abs(lon - prev) > 180 ? "M" : "L") + p[0].toFixed(1) + " " + p[1].toFixed(1);
        prev = lon; n++;
        bb[0] = Math.min(bb[0], p[0]); bb[1] = Math.min(bb[1], p[1]); bb[2] = Math.max(bb[2], p[0]); bb[3] = Math.max(bb[3], p[1]);
      }
      paths[iso] = (paths[iso] || "") + d + "Z";
      var area = (bb[2] - bb[0]) * (bb[3] - bb[1]);
      if (bb[2] - bb[0] < 500 && (!box[iso] || area > box[iso].a)) box[iso] = { a: area, c: [(bb[0] + bb[2]) / 2, (bb[1] + bb[3]) / 2] };
    });
    svg = el("svg", { viewBox: "0 0 " + W + " " + H, role: "img", "aria-label": conv("Dunyo xaritasi: maʼlumot bor mamlakatlar") });
    gMap = el("g", {});
    Object.keys(paths).forEach(function (iso) {
      var p = el("path", { d: paths[iso], "data-iso": iso, class: "mx-land" });
      gMap.appendChild(p); shapes[iso] = p;
      if (box[iso]) centers[iso] = box[iso].c;
    });
    Object.keys(CFG.points || {}).forEach(function (iso) {
      var ll = CFG.points[iso], c = px(ll[1], ll[0]);
      var p = el("circle", { cx: c[0].toFixed(1), cy: c[1].toFixed(1), r: 6, "data-iso": iso, class: "mx-land mx-pt" });
      gMap.appendChild(p); shapes[iso] = p; centers[iso] = c;
    });
    svg.appendChild(gMap);
    arc = el("path", { class: "mx-arc", d: "" });
    svg.appendChild(arc);
    var h = px(CFG.home_ll[1], CFG.home_ll[0]);
    svg.appendChild(el("circle", { cx: h[0].toFixed(1), cy: h[1].toFixed(1), r: 4.5, class: "mx-home" }));
    root.querySelector(".mx-load") && root.querySelector(".mx-load").remove();
    root.insertBefore(svg, tip);
    svg.addEventListener("mousemove", hover);
    svg.addEventListener("mouseleave", function () { tip.hidden = true; });
    svg.addEventListener("click", function (e) {
      var iso = e.target.getAttribute && e.target.getAttribute("data-iso");
      if (iso && CFG.covered.indexOf(iso) >= 0) pick(iso, true);
    });
    paint();
  }

  function info(iso) {
    var nm = (CFG.names[iso]) || (CFG.flows[iso] && CFG.flows[iso][0]);
    if (!nm) return null;
    if (layer === "flow") return CFG.flows[iso] ? nm + ": " + fmt(CFG.flows[iso][1]) + " kishi (2025)" : nm + ": top-10 da yoʻq";
    return CFG.covered.indexOf(iso) >= 0 ? nm : null;
  }
  function hover(e) {
    var iso = e.target.getAttribute && e.target.getAttribute("data-iso"), t = iso && info(iso);
    if (!t) { tip.hidden = true; return; }
    var r = root.getBoundingClientRect();
    tip.textContent = conv(t); tip.hidden = false;
    var x = e.clientX - r.left + 12, y = e.clientY - r.top + 12;
    if (x + tip.offsetWidth > r.width) x = e.clientX - r.left - tip.offsetWidth - 12;
    tip.style.left = x + "px"; tip.style.top = y + "px";
  }

  function paint() {
    var max = 0; Object.keys(CFG.flows).forEach(function (k) { max = Math.max(max, CFG.flows[k][1]); });
    Object.keys(shapes).forEach(function (iso) {
      var s = shapes[iso], cls = "mx-land" + (s.tagName === "circle" ? " mx-pt" : "");
      s.style.fillOpacity = "";
      if (iso === CFG.home) cls += " is-home";
      else if (layer === "atlas" && CFG.covered.indexOf(iso) >= 0) cls += " is-on";
      else if (layer === "flow" && CFG.flows[iso]) { cls += " is-flow"; s.style.fillOpacity = (0.25 + 0.75 * Math.sqrt(CFG.flows[iso][1] / max)).toFixed(2); }
      if (iso === sel) cls += " is-sel";
      s.setAttribute("class", cls);
    });
    svg.setAttribute("class", "lay-" + layer);
    legend.innerHTML = layer === "atlas"
      ? '<span><i class="lg-on"></i>' + conv("Maʼlumot bor") + '</span><span><i class="lg-home"></i>' + conv("Oʻzbekiston: siz shu yerdan boshlaysiz") + "</span>"
      : '<span><i class="lg-flow"></i>' + conv("Rang qancha toʻq, shuncha koʻp ketgan") + '</span><span><i class="lg-you"></i>' + conv("Oʻzbekiston") + "</span><span>" + conv("Manba: Milliy statistika qoʻmitasi, 2025") + "</span>";
    drawArc();
  }

  function drawArc() {
    if (!arc) return;
    var a = px(CFG.home_ll[1], CFG.home_ll[0]), b = sel && sel !== CFG.home && centers[sel];
    if (!b) { arc.setAttribute("d", ""); return; }
    var mx = (a[0] + b[0]) / 2, my = Math.min(a[1], b[1]) - Math.abs(a[0] - b[0]) * 0.22 - 10;
    arc.setAttribute("d", "M" + a[0].toFixed(1) + " " + a[1].toFixed(1) + "Q" + mx.toFixed(1) + " " + my.toFixed(1) + " " + b[0].toFixed(1) + " " + b[1].toFixed(1));
    if (!reduce) { arc.classList.remove("go"); void arc.getBoundingClientRect(); arc.classList.add("go"); }
  }

  function pick(iso, scroll) {
    sel = iso;
    document.querySelectorAll(".mx-c").forEach(function (d) { d.open = d.getAttribute("data-iso") === iso; });
    document.querySelectorAll(".mx-chip").forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-iso") === iso ? "true" : "false"); });
    var card = document.getElementById("mx-" + iso);
    if (scroll && card) {
      var list = document.getElementById("mxList");
      if (getComputedStyle(list).overflowY === "auto") list.scrollTo({ top: card.offsetTop - list.offsetTop, behavior: reduce ? "auto" : "smooth" });
      else card.scrollIntoView({ block: "start", behavior: reduce ? "auto" : "smooth" });
    }
    if (window.KSfx && KSfx.play) try { KSfx.play("pick"); } catch (e) {}
    paint();
  }

  document.querySelectorAll(".mx-chip").forEach(function (b) {
    b.addEventListener("click", function () { pick(b.getAttribute("data-iso"), true); });
  });
  document.querySelectorAll(".mx-c").forEach(function (d) {
    d.addEventListener("toggle", function () { if (d.open && sel !== d.getAttribute("data-iso")) pick(d.getAttribute("data-iso"), false); });
  });
  document.querySelectorAll(".mx-layer").forEach(function (b) {
    b.addEventListener("click", function () {
      layer = b.getAttribute("data-layer");
      document.querySelectorAll(".mx-layer").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      paint();
    });
  });

  var src = root.getAttribute("data-globe-src") || "data/globe.json";
  fetch(src).then(function (r) { if (!r.ok) throw r.status; return r.json(); }).then(build).catch(function () {
    var l = root.querySelector(".mx-load"); if (l) l.textContent = conv("Xarita yuklanmadi. Mamlakatlar roʻyxati pastda.");
  });
})();
