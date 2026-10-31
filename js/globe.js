// ═══════════════════════════════════════════════════════════════
//  Kompas Lab — yoʻnalishlar globusi (Canvas 2D, tashqi kutubxonasiz)
//  Ishlatish: <link rel="stylesheet" href="css/globe.css"> + <div class="kglobe" data-globe></div>
//             + <script src="js/globe.js" defer></script>  (ixtiyoriy: js/sfx.js — tovushlar)
//  Maʼlumot: data/globe.json (tools/globe/build_globe.py; Natural Earth 1:110m, jamoat mulki)
//  Qatlamlar: Xarita · Ob-havo (hozirgi, Open-Meteo Forecast API) · Iqlim (oxirgi 12 toʻliq oy,
//  Open-Meteo Historical API, ERA5). Ob-havo maʼlumoti faqat qatlam yoki mamlakat tanlanganda yuklanadi.
//  Boshqaruv: toʻliq ekran, aylanish tezligi va yoʻnalishi; tanlov localStorage "kompas_globe_v1" da.
//  Faqat koʻrinish maydoniga kirganda ishga tushadi; prefers-reduced-motion da sukut boʻyicha aylanmaydi
// ═══════════════════════════════════════════════════════════════
(function () {
  var ORIGIN = { iso: "UZB", id: "UZB", n: "Oʻzbekiston", c: "Toshkent", lat: 41.31, lon: 69.28 };
  // Lablar va mamlakatlar: index.html dagi Lab tavsiflari va Master Lab M7 asosida; c — ob-havo olinadigan poytaxt
  var DEST = [
    { id: "GBR", n: "Buyuk Britaniya", c: "London", lat: 51.51, lon: -0.13, labs: [["master-lab", "Master Lab", "Chevening, magistratura"], ["phd-lab", "PhD Lab", "Doktorantura"], ["musofir-lab", "Musofir Lab", "Rasmiy mavsumiy ish"]] },
    { id: "USA", n: "AQSh", c: "Vashington", lat: 38.9, lon: -77.04, labs: [["usa-lab", "USA Lab", "Bakalavr yordami, UGRAD, Fulbright, PhD"]] },
    { id: "DEU", n: "Germaniya", c: "Berlin", lat: 52.52, lon: 13.4, labs: [["daad-lab", "DAAD Lab", "Magistratura va doktorantura"], ["musofir-lab", "Musofir Lab", "Rasmiy ish"]] },
    { id: "KOR", n: "Koreya", c: "Seul", lat: 37.57, lon: 126.98, labs: [["gks-lab", "GKS Lab", "Global Korea Scholarship"], ["musofir-lab", "Musofir Lab", "EPS: rasmiy ish"]] },
    { id: "POL", n: "Polsha", c: "Varshava", lat: 52.23, lon: 21.01, labs: [["musofir-lab", "Musofir Lab", "Rasmiy ish va firibgarlikdan himoya"]] },
    { id: "HUN", n: "Vengriya", c: "Budapesht", lat: 47.5, lon: 19.04, labs: [["master-lab", "Master Lab", "Stipendium Hungaricum (M7)"]] },
    { id: "TUR", n: "Turkiya", c: "Anqara", lat: 39.93, lon: 32.86, labs: [["master-lab", "Master Lab", "Türkiye Bursları (M7)"]] },
    { id: "CHN", n: "Xitoy", c: "Pekin", lat: 39.9, lon: 116.4, labs: [["master-lab", "Master Lab", "Xitoy hukumati stipendiyasi, CSC (M7)"]] },
    { id: "JPN", n: "Yaponiya", c: "Tokio", lat: 35.68, lon: 139.69, labs: [["master-lab", "Master Lab", "MEXT (M7)"]] }
  ];
  var PTS = [ORIGIN].concat(DEST);          // ob-havo soʻrovidagi tartib
  var R = Math.PI / 180;
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var SPD = [0, 0.5, 1, 2, 4], SKEY = "kompas_globe_v1";
  var MON = ["yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avgust", "sentabr", "oktabr", "noyabr", "dekabr"];
  var DATA = null, WAIT = [];
  function snd(n) { if (window.KSfx) window.KSfx.play(n); }
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

  // ── Ob-havo va iqlim: Open-Meteo (CC BY 4.0, kalitsiz). Bitta soʻrovda 10 ta shahar ──
  var WX = { cur: null, cl: null, curErr: false, clErr: false, curAt: 0, period: "" }, wxWait = { cur: [], cl: [] };
  var LAT = PTS.map(function (p) { return p.lat; }).join(","), LON = PTS.map(function (p) { return p.lon; }).join(",");
  function arr(j) { return Array.isArray(j) ? j : [j]; }
  function ymd(d) { return d.getFullYear() + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2); }
  function load(kind, cb) {
    var have = kind === "cur" ? WX.cur && Date.now() - WX.curAt < 15 * 60000 : WX.cl;
    if (have) return cb();
    wxWait[kind].push(cb); if (wxWait[kind].length > 1) return;
    var url;
    if (kind === "cur") {
      url = "https://api.open-meteo.com/v1/forecast?latitude=" + LAT + "&longitude=" + LON +
        "&current=temperature_2m,apparent_temperature,relative_humidity_2m,precipitation,weather_code,wind_speed_10m,is_day&wind_speed_unit=kmh&timezone=auto";
    } else {
      // Oxirgi 12 toʻliq oy (joriy oy kirmaydi: arxiv bir necha kun kechikadi)
      var now = new Date(), a = new Date(now.getFullYear() - 1, now.getMonth(), 1), b = new Date(now.getFullYear(), now.getMonth(), 0);
      WX.period = MON[a.getMonth()] + " " + a.getFullYear() + " – " + MON[b.getMonth()] + " " + b.getFullYear();
      url = "https://archive-api.open-meteo.com/v1/archive?latitude=" + LAT + "&longitude=" + LON +
        "&start_date=" + ymd(a) + "&end_date=" + ymd(b) + "&daily=temperature_2m_mean,precipitation_sum&timezone=auto";
    }
    fetch(url).then(function (r) { if (!r.ok) throw r.status; return r.json(); }).then(function (j) {
      j = arr(j); if (j.length !== PTS.length) throw "len";
      if (kind === "cur") {
        WX.cur = j.map(function (o) { var c = o.current || {}; return { t: c.temperature_2m, f: c.apparent_temperature, h: c.relative_humidity_2m, p: c.precipitation, code: c.weather_code, w: c.wind_speed_10m, day: c.is_day === 1, time: c.time }; });
        WX.curAt = Date.now(); WX.curErr = false;
      } else {
        WX.cl = j.map(function (o) {
          var d = o.daily || {}, T = d.temperature_2m_mean || [], P = d.precipitation_sum || [], tm = d.time || [], M = {}, st = 0, n = 0, ps = 0, wet = 0;
          tm.forEach(function (day, i) {
            var k = day.slice(0, 7), m = M[k] || (M[k] = { k: k, ts: 0, tn: 0, p: 0 });
            if (T[i] != null) { m.ts += T[i]; m.tn++; st += T[i]; n++; }
            if (P[i] != null) { m.p += P[i]; ps += P[i]; if (P[i] >= 1) wet++; }
          });
          var mons = Object.keys(M).sort().map(function (k) { var m = M[k]; return { k: k, t: m.tn ? m.ts / m.tn : null, p: m.p }; }).filter(function (m) { return m.t != null; });
          if (!n || mons.length < 12) return null;
          var hot = mons.reduce(function (a, b) { return b.t > a.t ? b : a; }), cold = mons.reduce(function (a, b) { return b.t < a.t ? b : a; });
          return { t: st / n, hot: hot, cold: cold, p: ps, wet: wet, mons: mons };
        });
        WX.clErr = false;
      }
    }).catch(function () { if (kind === "cur") WX.curErr = true; else WX.clErr = true; })
      .then(function () { var q = wxWait[kind]; wxWait[kind] = []; q.forEach(function (f) { f(); }); });
  }
  // WMO ob-havo kodi → turkum va nom (https://open-meteo.com/en/docs, "WMO Weather interpretation codes")
  function cat(c) {
    if (c === 0 || c === 1) return "clear"; if (c === 2 || c === 3) return "cloud"; if (c === 45 || c === 48) return "fog";
    if ((c >= 51 && c <= 67) || (c >= 80 && c <= 82)) return "rain"; if ((c >= 71 && c <= 77) || c === 85 || c === 86) return "snow";
    if (c >= 95) return "storm"; return "cloud";
  }
  var WNAME = { 0: "ochiq osmon", 1: "asosan ochiq", 2: "qisman bulutli", 3: "bulutli", 45: "tuman", 48: "qirovli tuman", 51: "mayda yomgʻir", 53: "mayda yomgʻir", 55: "kuchli mayda yomgʻir", 56: "muzlovchi mayda yomgʻir", 57: "muzlovchi mayda yomgʻir", 61: "yengil yomgʻir", 63: "yomgʻir", 65: "kuchli yomgʻir", 66: "muzlovchi yomgʻir", 67: "muzlovchi yomgʻir", 71: "yengil qor", 73: "qor", 75: "kuchli qor", 77: "qor donalari", 80: "yengil jala", 81: "jala", 82: "kuchli jala", 85: "qor yogʻishi", 86: "kuchli qor yogʻishi", 95: "momaqaldiroq", 96: "doʻl bilan momaqaldiroq", 99: "doʻl bilan momaqaldiroq" };
  function emo(w) { var k = cat(w.code); return k === "clear" ? (w.day ? (w.code === 1 ? "🌤️" : "☀️") : "🌙") : k === "cloud" ? (w.code === 2 && w.day ? "⛅" : "☁️") : k === "fog" ? "🌫️" : k === "rain" ? "🌧️" : k === "snow" ? "❄️" : "⛈️"; }
  // Harorat rangi: sovuq koʻk → issiq qizil
  var TST = [[-15, [59, 91, 219]], [0, [77, 171, 247]], [10, [56, 178, 172]], [18, [242, 201, 76]], [26, [240, 140, 58]], [35, [214, 51, 108]]];
  function trgb(t) {
    if (t <= TST[0][0]) return TST[0][1]; if (t >= TST[TST.length - 1][0]) return TST[TST.length - 1][1];
    for (var i = 1; i < TST.length; i++) if (t <= TST[i][0]) { var a = TST[i - 1], b = TST[i], k = (t - a[0]) / (b[0] - a[0]); return [0, 1, 2].map(function (j) { return Math.round(a[1][j] + (b[1][j] - a[1][j]) * k); }); }
  }
  function tcol(t) { var c = trgb(t); return "rgb(" + c.join(",") + ")"; }
  function tink(t) { var c = trgb(t); return (0.299 * c[0] + 0.587 * c[1] + 0.114 * c[2]) > 165 ? "#1a2e26" : "#fff"; }
  function f1(x) { return (Math.round(x * 10) / 10).toFixed(1).replace(".", ",").replace("-", "−"); }
  function f0(x) { return String(Math.round(x)).replace("-", "−"); }
  // Iqlim saralash: taʼriflar legendada yoziladi
  var FILT = {
    hot: { n: "Issiq yoz", d: "eng issiq oy oʻrtachasi ≥ 25°C", f: function (c) { return c.hot.t >= 25; } },
    cold: { n: "Sovuq qish", d: "eng sovuq oy oʻrtachasi ≤ 0°C", f: function (c) { return c.cold.t <= 0; } },
    wet: { n: "Yomgʻirli", d: "yillik yogʻin ≥ 1000 mm", f: function (c) { return c.p >= 1000; } }
  };
  // Quyosh tik tushadigan nuqta (taxminiy, ±1°): kun/tun chegarasi uchun
  function sunPos() {
    var d = new Date(), N = (Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), d.getUTCDate()) - Date.UTC(d.getUTCFullYear(), 0, 0)) / 864e5;
    var dec = -23.44 * Math.cos(2 * Math.PI / 365 * (N + 10)), h = d.getUTCHours() + d.getUTCMinutes() / 60;
    return [dec * R, (-15 * (h - 12)) * R];
  }
  function hh(n) { var x = Math.sin(n * 127.1 + 311.7) * 43758.5453; return x - Math.floor(x); }

  function init(root) {
    var saved = {}; try { saved = JSON.parse(localStorage.getItem(SKEY) || "{}") || {}; } catch (e) {}
    var spd = saved.spd != null && SPD[saved.spd] != null ? saved.spd : (reduce ? 0 : 2), lastSpd = spd || 2, dir = saved.dir === -1 ? -1 : 1, layer = /^(map|wx|cl)$/.test(saved.layer) ? saved.layer : "map", filt = "";
    root.setAttribute("data-sfx", "");
    root.innerHTML =
      '<div class="kg-main"><div class="kg-stage"><canvas aria-hidden="true"></canvas>' +
        '<div class="kg-zoom"><button type="button" data-z="1" aria-label="Kattalashtirish" title="Kattalashtirish">+</button><button type="button" data-z="-1" aria-label="Kichraytirish" title="Kichraytirish">−</button>' +
        '<button type="button" data-a="home" aria-label="Toshkentga qaytish" title="Toshkentga qaytish">⌂</button><button type="button" data-a="full" class="kg-fs" aria-label="Toʻliq ekran" title="Toʻliq ekran"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></button></div>' +
        '</div>' +
        '<div class="kg-bar">' +
          '<div class="kg-seg" role="group" aria-label="Globus qatlami"><button type="button" data-l="map" data-snd="swap">🗺️ Xarita</button><button type="button" data-l="wx" data-snd="swap">🌦️ Ob-havo</button><button type="button" data-l="cl" data-snd="swap">🌡️ Iqlim</button></div>' +
          '<div class="kg-ctl"><button type="button" data-a="play" class="kg-ib"></button><button type="button" data-a="dir" class="kg-ib"></button>' +
            '<label class="kg-spd"><span>Tezlik</span><input type="range" min="0" max="4" step="1" aria-label="Aylanish tezligi"><b></b></label><span data-sfx-slot></span></div>' +
        '</div>' +
        '<div class="kg-leg" hidden></div>' +
      '</div>' +
      '<div class="kg-side"><div class="kg-list" role="list">' + DEST.map(function (d) { return '<button type="button" role="listitem" data-c="' + d.id + '" data-snd="none"><span>' + d.n + '</span><small class="kg-t"></small></button>'; }).join("") + '</div><div class="kg-card" hidden aria-live="polite"></div></div>';
    var cv = root.querySelector("canvas"), ctx = cv.getContext("2d"), card = root.querySelector(".kg-card"), stage = root.querySelector(".kg-stage"), leg = root.querySelector(".kg-leg");
    var rng = root.querySelector(".kg-spd input"), rngB = root.querySelector(".kg-spd b"), bPlay = root.querySelector('[data-a="play"]'), bDir = root.querySelector('[data-a="dir"]');
    var css = getComputedStyle(root);
    function tok(n, d) { return css.getPropertyValue(n).trim() || d; }
    var C = { land: tok("--kg-land", "#2d4a3e"), sea: tok("--kg-sea", "#e8f0ec"), arc: tok("--kg-arc", "#c4622d"), dim: tok("--kg-dim", "#9fb3aa"), night: tok("--kg-night", "#6f7f99") };
    var W = 0, H = 0, r0 = 0, r = 0, dpr = 1, lon0 = 40, lat0 = 30, zoom = 1, zt = 1, sel = null, t0 = performance.now(), running = false, raf = 0, drag = null, pinch = null, idleAt = 0, target = null, D = null;
    var destIdx = {}, pointers = {};
    var sp0 = 0, cp0 = 0, sun = sunPos(), sunAt = 0;
    if (window.KSfx && window.KSfx.mount) window.KSfx.mount();

    function persist() { try { localStorage.setItem(SKEY, JSON.stringify({ spd: spd, dir: dir, layer: layer })); } catch (e) {} }
    function size() {
      var w = stage.clientWidth; if (!w) return; dpr = Math.min(w < 500 ? 1.5 : 2, window.devicePixelRatio || 1);
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
    // Joriy qatlamdagi qiymat (°C) va iqlim saralashiga mosligi; i — PTS indeksi
    function val(i) {
      if (layer === "wx") return WX.cur && WX.cur[i] && WX.cur[i].t != null ? WX.cur[i].t : null;
      if (layer === "cl") return WX.cl && WX.cl[i] ? WX.cl[i].t : null;
      return null;
    }
    function match(i) { return !(layer === "cl" && filt && WX.cl && WX.cl[i]) || FILT[filt].f(WX.cl[i]); }
    function draw() {
      sp0 = Math.sin(lat0 * R); cp0 = Math.cos(lat0 * R); r = r0 * zoom;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0); ctx.clearRect(0, 0, W, H);
      var now = performance.now();
      if (now - sunAt > 30000) { sun = sunPos(); sunAt = now; }
      var showNight = layer === "wx", ss = Math.sin(sun[0]), cs = Math.cos(sun[0]);
      // Dengiz; Ob-havo qatlamida tungi tomoni toʻqroq (quyosh nuqtasidan qarama-qarshi yorugʻlik)
      ctx.beginPath(); ctx.arc(W / 2, H / 2, r, 0, 2 * Math.PI); ctx.fillStyle = C.sea; ctx.fill();
      // Tun: quyosh nuqtasidan 90° uzoqdagi katta aylana (terminator) ekranda ellips boʻladi
      if (showNight) {
        var sp = proj(sun[0], sun[1]), a = Math.atan2(sp[1] - H / 2, sp[0] - W / 2), sz = sp[2];
        ctx.save(); ctx.translate(W / 2, H / 2); ctx.rotate(a); ctx.scale(r, r);
        ctx.beginPath(); ctx.arc(0, 0, 1, Math.PI / 2, Math.PI * 1.5, false); ctx.ellipse(0, 0, Math.max(0.001, Math.abs(sz)), 1, 0, Math.PI * 1.5, Math.PI / 2, sz > 0);
        ctx.fillStyle = "rgba(38,56,96,.12)"; ctx.fill(); ctx.restore();
      }
      if (!D) return;
      var selI = sel ? D.idx[sel] : -2, orI = D.idx[ORIGIN.iso];
      var cval = {}; PTS.forEach(function (p, i) { var v = val(i); if (v != null) cval[D.idx[p.id]] = { v: v, ok: match(i) }; });
      // Quruqlik nuqtalari rang boʻyicha guruhlanadi: Lab mamlakatlari quyuqroq, tanlangani toʻq sariq,
      // Ob-havo/Iqlim qatlamida — harorat rangida; tungi tomondagi oddiy quruqlik koʻkimtir
      var ds = Math.max(1.2, r / 170), bk = {}, cols = [];
      for (var i = 0; i < D.dots.length; i++) {
        var q = D.dots[i], p = proj(q[0], q[1]); if (p[2] <= 0 || p[0] < -4 || p[0] > W + 4 || p[1] < -4 || p[1] > H + 4) continue;
        var c = q[2], cv2 = cval[c], col;
        if (cv2) col = cv2.ok ? tcol(cv2.v) : C.dim;
        else if (c === selI) col = C.arc;
        else if (destIdx[c] || c === orI) col = C.land;
        else col = showNight && Math.sin(q[0]) * ss + Math.cos(q[0]) * cs * Math.cos(q[1] - sun[1]) < 0 ? C.night : C.dim;
        if (!bk[col]) { bk[col] = []; cols.push(col); }
        bk[col].push(p[0] - ds / 2, p[1] - ds / 2, p[2]);
      }
      cols.forEach(function (col) {
        var a = bk[col]; ctx.fillStyle = col;
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
      DEST.forEach(function (d, di) {
        var on = sel === d.id, cur = !sel && flight().d === d, tt = on ? flight().t : 1;
        // Tanlangan yoʻnalish: uchilgan qism toʻq, hali uchilmagani xira
        [[1, on && tt < 1 ? 0.25 : 1], [tt, on && tt < 1 ? 1 : 0]].forEach(function (seg) {
          if (!seg[1]) return; ctx.beginPath(); var pen = false;
          for (var k = 0; k <= 48 && k / 48 <= seg[0] + 1e-6; k++) {
            var q = slerp(ORIGIN, d, k / 48), p = proj(q[0], q[1]), x = W / 2 + (p[0] - W / 2) * q[2], y = H / 2 + (p[1] - H / 2) * q[2];
            if (p[2] > -0.1) { if (pen) ctx.lineTo(x, y); else ctx.moveTo(x, y); pen = true; } else pen = false;
          }
          ctx.strokeStyle = C.arc; ctx.globalAlpha = seg[1] * (on || cur ? 0.95 : sel ? 0.18 : 0.45) * (match(di + 1) ? 1 : 0.3); ctx.lineWidth = on ? 2.4 : 1.2; ctx.stroke();
        });
        ctx.globalAlpha = 1;
      });
      // Shaharlar: avval tanlangan mamlakat, keyin Toshkent, keyin boshqa poytaxtlar; yozuvlar bir-birini bosmaydi
      var boxes = [], order = Object.keys(D.city).sort(function (x, y) { return (y === sel) - (x === sel) || (y === ORIGIN.iso) - (x === ORIGIN.iso); });
      function free(x, y, w, h) { for (var i = 0; i < boxes.length; i++) { var q = boxes[i]; if (x < q[0] + q[2] && x + w > q[0] && y < q[1] + q[3] && y + h > q[1]) return false; } boxes.push([x, y, w, h]); return true; }
      // Ob-havo/Iqlim: harorat yorliqlari birinchi joy oladi
      var tags = [];
      if (layer !== "map") {
        var ord = PTS.map(function (p, i) { return i; }).sort(function (a, b) { return (PTS[b].id === sel) - (PTS[a].id === sel) || (b === 0) - (a === 0); });
        ord.forEach(function (i) {
          var v = val(i); if (v == null) return;
          var pt = PTS[i], p = proj(pt.lat * R, pt.lon * R); if (p[2] <= 0.08 || p[0] < 0 || p[0] > W || p[1] < 0 || p[1] > H) return;
          var txt = f0(v) + "°" + (layer === "cl" && WX.cl[i] ? " · " + f0(WX.cl[i].p) + " mm" : "");
          ctx.font = "800 12px Outfit, sans-serif";
          var w = ctx.measureText(txt).width + (layer === "wx" ? 30 : 14), h = 22, x = p[0] - w / 2, y = p[1] - h - 9;
          if (free(x, y, w, h)) tags.push({ i: i, p: p, x: x, y: y, w: w, h: h, txt: txt, v: v, ok: match(i) });
        });
      }
      var pts2 = [];
      order.forEach(function (iso) {
        var isSel = iso === sel, isOr = iso === ORIGIN.iso;
        D.city[iso].forEach(function (c) {
          var cap = c[3] === 1;
          if (!cap && !isSel && !(isOr && zoom >= 1.5)) return;
          var p = proj(c[1] * R, c[2] * R); if (p[2] <= 0.05 || p[0] < 0 || p[0] > W || p[1] < 0 || p[1] > H) return;
          pts2.push([p, cap, isOr, isSel]);
          var want = isSel || isOr || (cap && zoom >= 1.9);
          if (!want) return;
          var txt = c[0] + (cap ? " ★" : ""), fs = cap ? 12.5 : 11;
          ctx.font = (cap ? 800 : 600) + " " + fs + "px Outfit, sans-serif";
          var w = ctx.measureText(txt).width;
          if (free(p[0] + 7, p[1] - fs + 3, w + 2, fs + 2)) pts2[pts2.length - 1].push(txt, fs);
        });
      });
      if (layer === "wx") effects(now);
      pts2.forEach(function (o) {
        var p = o[0], cap = o[1], isOr = o[2], isSel = o[3];
        ctx.beginPath(); ctx.arc(p[0], p[1], cap ? (isSel ? 6 : 4.5) : 2.6, 0, 2 * Math.PI);
        ctx.fillStyle = cap ? (isOr ? C.land : C.arc) : "#fff"; ctx.fill(); ctx.lineWidth = cap ? 2 : 1.4; ctx.strokeStyle = cap ? "#fff" : (isOr ? C.land : C.arc); ctx.stroke();
        if (o[4]) label(o[4], p[0] + 8, p[1] + 4, o[5], cap ? 800 : 600, C.land);
      });
      tags.forEach(tag);
      DEST.forEach(function (d) { d._p = proj(d.lat * R, d.lon * R); });
      if (showNight) { var sp2 = proj(sun[0], sun[1]); if (sp2[2] > 0.05) { ctx.save(); ctx.globalAlpha = 0.9; glyph("sun", sp2[0], sp2[1], 16); ctx.restore(); } }
      plane();
    }
    // Harorat yorligʻi: rangli tabletka, Ob-havo qatlamida ichida ob-havo belgisi
    function tag(o) {
      ctx.save(); ctx.globalAlpha = o.ok ? 1 : 0.35;
      ctx.beginPath(); rrect(o.x, o.y, o.w, o.h, 11); ctx.fillStyle = tcol(o.v); ctx.shadowColor = "rgba(0,0,0,.18)"; ctx.shadowBlur = 6; ctx.shadowOffsetY = 2; ctx.fill(); ctx.shadowColor = "transparent";
      ctx.beginPath(); ctx.moveTo(o.p[0] - 5, o.y + o.h - 0.5); ctx.lineTo(o.p[0], o.y + o.h + 6); ctx.lineTo(o.p[0] + 5, o.y + o.h - 0.5); ctx.fill();
      var tx = o.x + 7;
      if (layer === "wx") {
        var w = WX.cur[o.i]; ctx.beginPath(); ctx.arc(o.x + 11, o.y + o.h / 2, 9, 0, 2 * Math.PI); ctx.fillStyle = "rgba(255,255,255,.92)"; ctx.fill();
        glyph(wkind(w), o.x + 11, o.y + o.h / 2, 13); tx = o.x + 24;
      }
      ctx.font = "800 12px Outfit, sans-serif"; ctx.textBaseline = "middle"; ctx.fillStyle = tink(o.v); ctx.fillText(o.txt, tx, o.y + o.h / 2 + 0.5); ctx.textBaseline = "alphabetic";
      ctx.restore();
    }
    function wkind(w) { var k = cat(w.code); return k === "clear" ? (w.day ? "sun" : "moon") : k; }
    function rrect(x, y, w, h, rr) { ctx.moveTo(x + rr, y); ctx.arcTo(x + w, y, x + w, y + h, rr); ctx.arcTo(x + w, y + h, x, y + h, rr); ctx.arcTo(x, y + h, x, y, rr); ctx.arcTo(x, y, x + w, y, rr); ctx.closePath(); }
    // Ob-havo belgilari (vektor): sun, moon, cloud, fog, rain, snow, storm; s — oʻlcham (px)
    function cloudP(x, y, s) { ctx.beginPath(); ctx.arc(x - s * 0.22, y + s * 0.06, s * 0.2, 0, 7); ctx.arc(x + s * 0.02, y - s * 0.08, s * 0.26, 0, 7); ctx.arc(x + s * 0.25, y + s * 0.08, s * 0.18, 0, 7); ctx.rect(x - s * 0.22, y + s * 0.06, s * 0.47, s * 0.2); }
    function glyph(k, x, y, s) {
      ctx.save(); ctx.lineCap = "round";
      if (k === "sun") {
        ctx.strokeStyle = "#f0a500"; ctx.lineWidth = Math.max(1, s * 0.09);
        for (var i = 0; i < 8; i++) { var a = i * Math.PI / 4; ctx.beginPath(); ctx.moveTo(x + Math.cos(a) * s * 0.33, y + Math.sin(a) * s * 0.33); ctx.lineTo(x + Math.cos(a) * s * 0.48, y + Math.sin(a) * s * 0.48); ctx.stroke(); }
        ctx.beginPath(); ctx.arc(x, y, s * 0.24, 0, 7); ctx.fillStyle = "#ffc21a"; ctx.fill();
      } else if (k === "moon") {
        ctx.beginPath(); ctx.arc(x, y, s * 0.34, Math.PI * 0.5, Math.PI * 1.5, false); ctx.ellipse(x, y, s * 0.16, s * 0.34, 0, Math.PI * 1.5, Math.PI * 0.5, true); ctx.fillStyle = "#7b8db3"; ctx.fill();
      } else if (k === "fog") {
        ctx.strokeStyle = "#8a979f"; ctx.lineWidth = Math.max(1, s * 0.1);
        [-0.2, 0, 0.2].forEach(function (d, i) { ctx.beginPath(); ctx.moveTo(x - s * (0.32 - i * 0.05), y + d * s); ctx.lineTo(x + s * (0.32 - (2 - i) * 0.05), y + d * s); ctx.stroke(); });
      } else {
        var dark = k === "storm", yy = k === "cloud" ? y : y - s * 0.12;
        cloudP(x, yy, s); ctx.fillStyle = dark ? "#7d8796" : k === "cloud" ? "#b9c3cc" : "#9fb0c0"; ctx.fill();
        if (k === "rain") { ctx.strokeStyle = "#2f6fd6"; ctx.lineWidth = Math.max(1, s * 0.08); [-0.16, 0.02, 0.2].forEach(function (d) { ctx.beginPath(); ctx.moveTo(x + d * s, y + s * 0.2); ctx.lineTo(x + d * s - s * 0.06, y + s * 0.38); ctx.stroke(); }); }
        if (k === "snow") { ctx.fillStyle = "#4dabf7"; [-0.16, 0.02, 0.2].forEach(function (d, i) { ctx.beginPath(); ctx.arc(x + d * s, y + s * (0.28 + (i % 2) * 0.08), s * 0.06, 0, 7); ctx.fill(); }); }
        if (k === "storm") { ctx.beginPath(); ctx.moveTo(x + s * 0.04, y + s * 0.12); ctx.lineTo(x - s * 0.1, y + s * 0.3); ctx.lineTo(x + s * 0.02, y + s * 0.3); ctx.lineTo(x - s * 0.08, y + s * 0.48); ctx.strokeStyle = "#f0a500"; ctx.lineWidth = Math.max(1, s * 0.09); ctx.stroke(); }
      }
      ctx.restore();
    }
    // Shahar atrofidagi jonli effektlar: yomgʻir tomchilari, qor, chaqmoq, tuman, quyosh nuri
    function effects(now) {
      if (!WX.cur) return;
      var t = reduce ? 0 : now / 1000, Rr = 22 * Math.min(1.8, Math.sqrt(zoom));
      PTS.forEach(function (pt, i) {
        var w = WX.cur[i]; if (!w || w.code == null) return;
        var p = proj(pt.lat * R, pt.lon * R); if (p[2] <= 0.15) return;
        var k = cat(w.code), x = p[0], y = p[1] + 4, n, j;
        ctx.save(); ctx.lineCap = "round";
        if (k === "rain" || k === "storm") {
          n = w.code >= 63 && w.code !== 80 ? 16 : 10; ctx.strokeStyle = "#2f6fd6"; ctx.lineWidth = 1.3;
          for (j = 0; j < n; j++) {
            var px = x + (hh(i * 31 + j) - 0.5) * 2 * Rr, ph = (hh(i * 17 + j * 3) + t * (0.9 + hh(j) * 0.5)) % 1, py = y - Rr + ph * 2 * Rr;
            ctx.globalAlpha = 0.65 * Math.sin(ph * Math.PI); ctx.beginPath(); ctx.moveTo(px, py); ctx.lineTo(px - 1.6, py + 5.5); ctx.stroke();
          }
          if (k === "storm" && !reduce && (t % 3.2) < 0.12) { ctx.globalAlpha = 0.9; ctx.beginPath(); ctx.moveTo(x + 4, y - Rr * 0.8); ctx.lineTo(x - 4, y - 2); ctx.lineTo(x + 2, y - 2); ctx.lineTo(x - 5, y + Rr * 0.7); ctx.strokeStyle = "#f5c400"; ctx.lineWidth = 2.2; ctx.stroke(); }
        } else if (k === "snow") {
          ctx.fillStyle = "#fff"; ctx.strokeStyle = "#6aa8e8"; ctx.lineWidth = 0.8;
          for (j = 0; j < 14; j++) {
            var ph2 = (hh(i * 13 + j * 7) + t * (0.22 + hh(j + 9) * 0.15)) % 1, sx = x + (hh(i * 29 + j) - 0.5) * 2 * Rr + Math.sin(t * 2 + j) * 3, sy = y - Rr + ph2 * 2 * Rr;
            ctx.globalAlpha = 0.9 * Math.sin(ph2 * Math.PI); ctx.beginPath(); ctx.arc(sx, sy, 1.9, 0, 7); ctx.fill(); ctx.stroke();
          }
        } else if (k === "fog" || k === "cloud") {
          ctx.fillStyle = k === "fog" ? "#9aa5ad" : "#c3ccd4";
          for (j = 0; j < 3; j++) { ctx.globalAlpha = k === "fog" ? 0.28 : 0.22; ctx.beginPath(); ctx.ellipse(x + Math.sin(t * 0.4 + j * 2) * Rr * 0.5, y - Rr * 0.3 + j * Rr * 0.3, Rr * 0.7, Rr * 0.22, 0, 0, 7); ctx.fill(); }
        } else if (k === "clear" && w.day) {
          var g = ctx.createRadialGradient(x, y - 4, 0, x, y - 4, Rr * (1 + 0.08 * Math.sin(t * 2)));
          g.addColorStop(0, "rgba(255,200,40,.45)"); g.addColorStop(1, "rgba(255,200,40,0)"); ctx.fillStyle = g; ctx.beginPath(); ctx.arc(x, y - 4, Rr * 1.1, 0, 7); ctx.fill();
        }
        ctx.restore();
      });
    }
    // ── Samolyot: tanlangan yoʻnalishda, aks holda yoʻnalishlar boʻylab navbat bilan uchadi ──
    var FLY = 3600, FLYS = 4200, fly = null;
    function ease(t) { return t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2; }
    function flight() {
      var el = performance.now() - t0, d, t;
      if (sel) {
        d = DEST.filter(function (x) { return x.id === sel; })[0];
        if (!fly || fly.done) return { d: d, t: 1, done: true };
        return { d: d, t: ease(Math.min(1, (performance.now() - fly.at) / FLYS)) };
      }
      var n = reduce ? 0 : Math.floor(el / FLY); d = DEST[n % DEST.length]; t = (el % FLY) / FLY;
      if (reduce) t = 0.55;
      return { d: d, t: ease(t) };
    }
    function gdist(a, b) {
      var la1 = a.lat * R, la2 = b.lat * R, dl = (b.lon - a.lon) * R;
      return Math.acos(Math.max(-1, Math.min(1, Math.sin(la1) * Math.sin(la2) + Math.cos(la1) * Math.cos(la2) * Math.cos(dl))));
    }
    // Uchish: kamera butun yoʻnalishni koʻrsatadi (oʻrtasiga qaraydi), samolyot Toshkentdan uchadi
    function takeoff(d) {
      fly = { d: d, at: performance.now(), done: false };
      if (reduce || !running) return land();
      var m = slerp(ORIGIN, d, 0.5), half = gdist(ORIGIN, d) / 2;
      target = [m[1] / R, Math.max(-30, Math.min(55, m[0] / R))];
      setZoom(Math.max(1, Math.min(2.4, 0.8 / Math.sin(half)))); idleAt = performance.now() + FLYS + 8000;
    }
    // Qoʻnish: kamera mamlakatga yaqinlashadi
    function land() {
      var d = fly.d; fly.done = true; fly.landAt = performance.now();
      target = [d.lon, Math.max(-30, Math.min(55, d.lat))]; idleAt = performance.now() + 8000;
      setZoom(d.id === "USA" || d.id === "CHN" ? 2 : d.id === "GBR" || d.id === "KOR" || d.id === "HUN" || d.id === "POL" ? 3.2 : 2.6);
      if (!running) { lon0 = target[0]; lat0 = target[1]; target = null; draw(); }
    }
    function scr(q) { var p = proj(q[0], q[1]); return [W / 2 + (p[0] - W / 2) * q[2], H / 2 + (p[1] - H / 2) * q[2], p[2], p]; }
    function plane() {
      var f = flight(); if (!f.d) return;
      if (f.done) {
        // Qoʻnish toʻlqini (1,6 s)
        var e = fly && fly.landAt ? (performance.now() - fly.landAt) / 1600 : 1, pd = f.d._p;
        if (!reduce && e < 1 && pd && pd[2] > 0.05) {
          ctx.save(); ctx.globalAlpha = 0.7 * (1 - e); ctx.strokeStyle = C.arc; ctx.lineWidth = 2;
          ctx.beginPath(); ctx.arc(pd[0], pd[1], 6 + 22 * e, 0, 2 * Math.PI); ctx.stroke(); ctx.restore();
        }
        return;
      }
      var t = Math.min(0.985, Math.max(0.015, f.t)), q = slerp(ORIGIN, f.d, t), a = scr(q), b = scr(slerp(ORIGIN, f.d, t + 0.01));
      if (a[2] <= 0.02) return;
      var lift = (q[2] - 1) / 0.16, s = (7 + 6 * lift) * Math.min(1.8, Math.sqrt(zoom)) * (W < 500 ? 0.9 : 1), ang = Math.atan2(b[1] - a[1], b[0] - a[0]);
      var fade = Math.min(1, Math.min(t, 1 - t) * 12);
      // Yerdagi soya: balandlik qancha katta boʻlsa, shuncha uzoq va xira
      ctx.save(); ctx.globalAlpha = 0.18 * fade * (1 - 0.4 * lift);
      ctx.translate(a[3][0] + 3 * lift, a[3][1] + 4 * lift); ctx.rotate(ang); ctx.scale(s * 0.9, s * 0.9);
      shape(); ctx.fillStyle = "#0d1f18"; ctx.fill(); ctx.restore();
      // Samolyot: hajm va soya bilan; qanotlar biroz qiyshayadi (bank)
      ctx.save(); ctx.globalAlpha = fade; ctx.translate(a[0], a[1]); ctx.rotate(ang);
      var bank = Math.sin(t * Math.PI * 2) * 0.12; ctx.scale(s, s * (1 - Math.abs(bank)));
      var g = ctx.createLinearGradient(0, -1, 0, 1); g.addColorStop(0, "#ffffff"); g.addColorStop(0.5 + bank, "#eef2ef"); g.addColorStop(1, "#b9c7c0");
      shape(); ctx.fillStyle = g; ctx.fill(); ctx.lineWidth = 0.09; ctx.strokeStyle = C.land; ctx.stroke();
      ctx.beginPath(); ctx.moveTo(0.55, 0); ctx.lineTo(-0.7, 0); ctx.lineWidth = 0.1; ctx.strokeStyle = C.arc; ctx.stroke();
      ctx.beginPath(); ctx.ellipse(0.78, 0, 0.12, 0.07, 0, 0, 2 * Math.PI); ctx.fillStyle = C.land; ctx.fill();
      ctx.restore();
    }
    // Samolyot shakli (tepadan), burni +x tomonda, oʻlchami ~2 birlik
    function shape() {
      ctx.beginPath();
      ctx.moveTo(1, 0); ctx.quadraticCurveTo(0.95, -0.11, 0.7, -0.12);
      ctx.lineTo(0.18, -0.12); ctx.lineTo(-0.28, -0.95); ctx.lineTo(-0.46, -0.95); ctx.lineTo(-0.24, -0.12);
      ctx.lineTo(-0.72, -0.1); ctx.lineTo(-0.94, -0.42); ctx.lineTo(-1.06, -0.42); ctx.lineTo(-0.96, -0.06);
      ctx.lineTo(-0.96, 0.06); ctx.lineTo(-1.06, 0.42); ctx.lineTo(-0.94, 0.42); ctx.lineTo(-0.72, 0.1);
      ctx.lineTo(-0.24, 0.12); ctx.lineTo(-0.46, 0.95); ctx.lineTo(-0.28, 0.95); ctx.lineTo(0.18, 0.12);
      ctx.lineTo(0.7, 0.12); ctx.quadraticCurveTo(0.95, 0.11, 1, 0); ctx.closePath();
    }
    var slowDev = false, ft = [], lastT = 0, odd = false;
    function loop(now) {
      if (!running) return;
      if (fly && !fly.done && now - fly.at > FLYS) land();
      if (lastT) { ft.push(now - lastT); if (ft.length > 30) { ft.shift(); slowDev = ft.reduce(function (a, b) { return a + b; }, 0) / ft.length > 26; } } lastT = now;
      var idle = !target && !drag && !pinch && Math.abs(zt - zoom) < 0.01;
      if (idle && slowDev && (odd = !odd)) { raf = requestAnimationFrame(loop); return; }
      if (target) { var dl = ((target[0] - lon0 + 540) % 360) - 180, dt = target[1] - lat0; lon0 += dl * 0.09; lat0 += dt * 0.09; if (Math.abs(dl) < 0.15 && Math.abs(dt) < 0.15) target = null; }
      else if (!drag && !pinch && SPD[spd] && performance.now() > idleAt) lon0 += dir * (slowDev ? 0.1 : 0.05) * SPD[spd] / zoom;
      zoom += (zt - zoom) * 0.15;
      draw(); raf = requestAnimationFrame(loop);
    }
    function start() { if (!running) { running = true; raf = requestAnimationFrame(loop); } }
    function stop() { running = false; cancelAnimationFrame(raf); }
    function setZoom(z) { zt = Math.max(1, Math.min(4, z)); idleAt = performance.now() + 5000; if (!running) { zoom = zt; draw(); } }

    // ── Boshqaruv paneli ──
    function paintCtl() {
      rng.value = spd; rngB.textContent = SPD[spd] ? String(SPD[spd]).replace(".", ",") + "×" : "toʻxtagan";
      bPlay.textContent = SPD[spd] ? "⏸" : "▶"; bPlay.title = SPD[spd] ? "Aylanishni toʻxtatish" : "Aylantirish"; bPlay.setAttribute("aria-label", bPlay.title);
      bDir.textContent = dir > 0 ? "↻" : "↺"; bDir.title = "Aylanish yoʻnalishi: " + (dir > 0 ? "gʻarbdan sharqqa" : "sharqdan gʻarbga"); bDir.setAttribute("aria-label", bDir.title);
      root.querySelectorAll(".kg-seg button").forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-l") === layer ? "true" : "false"); });
    }
    function setLayer(l) {
      layer = l; filt = ""; persist(); paintCtl();
      if (l === "wx" || (l === "cl" && sel)) load("cur", refresh); if (l === "cl" || (l === "wx" && sel)) load("cl", refresh);
      refresh();
    }
    // Legend, roʻyxatdagi haroratlar, kartochka va globusni yangilash
    function refresh() {
      var have = layer === "wx" ? WX.cur : layer === "cl" ? WX.cl : null, err = layer === "wx" ? WX.curErr : WX.clErr;
      leg.hidden = layer === "map";
      if (layer !== "map") {
        var stops = TST.map(function (s) { return "rgb(" + s[1].join(",") + ") " + Math.round((s[0] + 15) / 50 * 100) + "%"; }).join(",");
        var h = '<div class="kg-scale"><span>−15°</span><i style="background:linear-gradient(90deg,' + stops + ')"></i><span>35°+</span></div>';
        if (!have && !err) h += '<p class="kg-src">Maʼlumot yuklanmoqda…</p>';
        else if (err && !have) h += '<p class="kg-src kg-err">Ob-havo maʼlumotini olib boʻlmadi. Internetni tekshirib, qayta urinib koʻring. <button type="button" data-a="retry">Qayta</button></p>';
        if (layer === "wx" && have) {
          h += '<p class="kg-src">Hozirgi harorat (°C) va ob-havo, poytaxtlarda. Koʻkimtir quruqlik — hozir tun. Manba: <a href="https://open-meteo.com/" target="_blank" rel="noopener">Open-Meteo.com</a> (CC BY 4.0), har 15 daqiqada yangilanadi.</p>';
        }
        if (layer === "cl" && have) {
          h += '<div class="kg-filt" role="group" aria-label="Iqlim boʻyicha saralash">' + [["", "Hammasi"]].concat(Object.keys(FILT).map(function (k) { return [k, FILT[k].n]; })).map(function (f) { return '<button type="button" data-f="' + f[0] + '" aria-pressed="' + (filt === f[0]) + '" data-snd="pick">' + f[1] + "</button>"; }).join("") + "</div>";
          h += '<p class="kg-src">Oʻrtacha harorat va yogʻin, ' + WX.period + " (oxirgi 12 toʻliq oy), poytaxtlarda." + (filt ? " <b>" + FILT[filt].n + "</b>: " + FILT[filt].d + "." : "") + ' Manba: <a href="https://open-meteo.com/en/docs/historical-weather-api" target="_blank" rel="noopener">Open-Meteo Historical API</a>, ERA5 qayta tahlili (CC BY 4.0).</p>';
        }
        leg.innerHTML = h;
      }
      root.querySelectorAll(".kg-list button").forEach(function (b) {
        var i = PTS.map(function (p) { return p.id; }).indexOf(b.getAttribute("data-c")), v = val(i), t = b.querySelector(".kg-t");
        t.textContent = v == null ? "" : (layer === "wx" && WX.cur[i] ? emo(WX.cur[i]) + " " : "") + f0(v) + "°";
        t.style.background = v == null ? "" : tcol(v); t.style.color = v == null ? "" : tink(v);
        b.classList.toggle("kg-dim", !match(i));
      });
      if (sel) cardWx();
      if (!running) draw();
    }
    leg.addEventListener("click", function (e) {
      var f = e.target.closest("[data-f]"); if (f) { filt = f.getAttribute("data-f"); refresh(); return; }
      if (e.target.closest('[data-a="retry"]')) { WX.curErr = WX.clErr = false; setLayer(layer); }
    });
    root.querySelector(".kg-seg").addEventListener("click", function (e) { var b = e.target.closest("[data-l]"); if (b) setLayer(b.getAttribute("data-l")); });
    rng.addEventListener("input", function () { spd = +rng.value; if (spd) lastSpd = spd; idleAt = 0; persist(); paintCtl(); });
    bPlay.addEventListener("click", function () { spd = SPD[spd] ? 0 : (lastSpd || 2); idleAt = 0; persist(); paintCtl(); });
    bDir.addEventListener("click", function () { dir = -dir; if (!SPD[spd]) spd = lastSpd || 2; idleAt = 0; persist(); paintCtl(); });

    // ── Toʻliq ekran: Fullscreen API, boʻlmasa (iPhone) — sahifa ustidagi qatlam ──
    var fsApi = root.requestFullscreen ? "requestFullscreen" : root.webkitRequestFullscreen ? "webkitRequestFullscreen" : null;
    function fsEl() { return document.fullscreenElement || document.webkitFullscreenElement; }
    function setFull(on) {
      root.classList.toggle("kg-full", on); document.documentElement.classList.toggle("kg-lock", on);
      var b = root.querySelector('[data-a="full"]'); b.title = on ? "Toʻliq ekrandan chiqish" : "Toʻliq ekran"; b.setAttribute("aria-label", b.title);
      requestAnimationFrame(size);
    }
    function toggleFull() {
      var on = !root.classList.contains("kg-full");
      if (fsApi) {
        if (on) { var pr = root[fsApi](); if (pr && pr.catch) pr.catch(function () { setFull(true); }); }
        else if (fsEl()) (document.exitFullscreen || document.webkitExitFullscreen).call(document); else setFull(false);
      } else setFull(on);
    }
    ["fullscreenchange", "webkitfullscreenchange"].forEach(function (ev) { document.addEventListener(ev, function () { setFull(fsEl() === root); }); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && root.classList.contains("kg-full") && !fsEl()) setFull(false); });

    // ── Mamlakat kartochkasi ──
    function show(id, user) {
      sel = id; var d = DEST.filter(function (x) { return x.id === id; })[0];
      root.querySelectorAll(".kg-list button").forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-c") === id ? "true" : "false"); });
      if (!d) { card.hidden = true; fly = null; setZoom(1); return; }
      if (user) snd("whoosh");
      var cities = D && D.city[id] ? D.city[id].map(function (c) { return c[0] + (c[3] ? " (poytaxt)" : ""); }).join(", ") : "";
      card.innerHTML = '<button type="button" class="kg-x" aria-label="Yopish">×</button><b>' + d.n + "</b>" + (cities ? '<small class="kg-c">' + cities + "</small>" : "") +
        '<button type="button" class="kg-fly" data-a="fly" data-snd="none">✈ Toshkentdan qayta uchish</button><div class="kg-wx" data-wx></div>' +
        d.labs.map(function (l) { return '<a href="' + l[0] + '.html"><span>' + l[1] + "</span><small>" + l[2] + "</small></a>"; }).join("") + '<small class="kg-n">Har Lab bepul M0 bilan boshlanadi.</small>';
      card.hidden = false; cardWx();
      if (layer !== "map") { load("cur", refresh); load("cl", refresh); }
      takeoff(d);
    }
    // Kartochkadagi ob-havo va iqlim: hozir + oxirgi 12 oy, Toshkent bilan solishtirish, oylik grafik
    function cardWx() {
      var box = card.querySelector("[data-wx]"); if (!box) return;
      if (layer === "map") { box.innerHTML = ""; return; }  // Xarita qatlamida ob-havo va iqlim koʻrsatilmaydi
      var i = PTS.map(function (p) { return p.id; }).indexOf(sel), pt = PTS[i], h = "";
      var w = WX.cur && WX.cur[i], c = WX.cl && WX.cl[i], o = WX.cl && WX.cl[0];
      if (w && w.t != null) {
        h += '<div class="kg-now"><span class="kg-e">' + emo(w) + '</span><div><b style="color:' + tcol(w.t) + '">' + f0(w.t) + "°C</b> " + pt.c + "da hozir: " + (WNAME[w.code] || "") +
          "<small>His qilinishi " + f0(w.f) + "° · shamol " + f0(w.w) + " km/soat · namlik " + f0(w.h) + "%" + (w.time ? " · " + w.time.slice(11, 16) + " (mahalliy vaqt)" : "") + "</small></div></div>";
      } else if (WX.curErr) h += '<small class="kg-c">Hozirgi ob-havoni olib boʻlmadi.</small>';
      else h += '<small class="kg-c">Ob-havo yuklanmoqda…</small>';
      if (c) {
        var diff = o ? c.t - o.t : 0;
        h += '<div class="kg-cl"><small class="kg-h">Iqlim: ' + WX.period + "</small>" + spark(c) +
          "<ul><li>Oʻrtacha harorat <b>" + f1(c.t) + "°C</b>" + (o && sel !== "UZB" ? " (Toshkentdan " + f1(Math.abs(diff)) + "° " + (diff < 0 ? "sovuqroq" : "issiqroq") + ")" : "") + "</li>" +
          "<li>Eng issiq oy: " + MON[+c.hot.k.slice(5) - 1] + " <b>" + f1(c.hot.t) + "°</b> · eng sovuq: " + MON[+c.cold.k.slice(5) - 1] + " <b>" + f1(c.cold.t) + "°</b></li>" +
          "<li>Yogʻin <b>" + f0(c.p) + " mm</b>, yogʻinli kunlar (≥1 mm) <b>" + c.wet + "</b>" + (o && sel !== "UZB" ? " (Toshkentda " + f0(o.p) + " mm, " + o.wet + " kun)" : "") + "</li></ul></div>";
      }
      if (w || c) h += '<small class="kg-n">Manba: <a href="https://open-meteo.com/" target="_blank" rel="noopener">Open-Meteo.com</a> (CC BY 4.0)' + (c ? ", ERA5" : "") + ".</small>";
      box.innerHTML = h;
    }
    // 12 oy: ustunlar — yogʻin (mm), chiziq — oʻrtacha harorat (°C)
    function spark(c) {
      var m = c.mons.slice(-12), W2 = 240, H2 = 64, pad = 4, bw = (W2 - pad * 2) / 12;
      var pmax = Math.max.apply(null, m.map(function (x) { return x.p; }).concat([1])), tmin = Math.min.apply(null, m.map(function (x) { return x.t; })), tmax = Math.max.apply(null, m.map(function (x) { return x.t; }));
      var span = Math.max(1, tmax - tmin), bars = "", pts = [], lab = "";
      m.forEach(function (x, j) {
        var bh = x.p / pmax * (H2 - 22), X = pad + j * bw;
        bars += '<rect x="' + (X + bw * 0.18).toFixed(1) + '" y="' + (H2 - 12 - bh).toFixed(1) + '" width="' + (bw * 0.64).toFixed(1) + '" height="' + bh.toFixed(1) + '" rx="1.5" fill="#9ec5f5"><title>' + MON[+x.k.slice(5) - 1] + ": " + f0(x.p) + " mm, " + f1(x.t) + "°C</title></rect>";
        pts.push([(X + bw / 2).toFixed(1), (6 + (1 - (x.t - tmin) / span) * (H2 - 26)).toFixed(1), x.t]);
        lab += '<text x="' + (X + bw / 2).toFixed(1) + '" y="' + (H2 - 2) + '" text-anchor="middle">' + MON[+x.k.slice(5) - 1].charAt(0).toUpperCase() + "</text>";
      });
      var dots = pts.map(function (p) { return '<circle cx="' + p[0] + '" cy="' + p[1] + '" r="2.6" fill="' + tcol(p[2]) + '" stroke="#fff" stroke-width="1"/>'; }).join("");
      return '<svg class="kg-sp" viewBox="0 0 ' + W2 + " " + H2 + '" role="img" aria-label="Oylik oʻrtacha harorat va yogʻin">' + bars + '<polyline points="' + pts.map(function (p) { return p[0] + "," + p[1]; }).join(" ") + '" fill="none" stroke="#c4622d" stroke-width="1.6" stroke-linejoin="round"/>' + dots + lab + "</svg>" +
        '<small class="kg-lg"><i class="kg-lt"></i>harorat <i class="kg-lp"></i>yogʻin</small>';
    }
    card.addEventListener("click", function (e) {
      if (e.target.classList.contains("kg-x")) show(null);
      else if (e.target.closest('[data-a="fly"]') && sel) { snd("whoosh"); takeoff(DEST.filter(function (x) { return x.id === sel; })[0]); }
    });
    root.querySelector(".kg-list").addEventListener("click", function (e) { var b = e.target.closest("[data-c]"); if (b) { var c = b.getAttribute("data-c"); show(sel === c ? null : c, sel !== c); } });
    root.querySelector(".kg-zoom").addEventListener("click", function (e) {
      var b = e.target.closest("button"); if (!b) return;
      var z = +b.getAttribute("data-z"), a = b.getAttribute("data-a");
      if (z) setZoom(zt * (z > 0 ? 1.5 : 1 / 1.5));
      else if (a === "home") { show(null); target = [ORIGIN.lon - 30, 30]; idleAt = performance.now() + 4000; if (!running) { lon0 = target[0]; lat0 = target[1]; target = null; draw(); } }
      else if (a === "full") toggleFull();
    });
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
      if (best) show(best, best !== sel);
    }
    window.addEventListener("pointerup", up); window.addEventListener("pointercancel", up);
    // Gʻildirak: sahifani aylantirmasdan faqat toʻliq ekranda yaqinlashtiradi
    cv.addEventListener("wheel", function (e) { if (!root.classList.contains("kg-full")) return; e.preventDefault(); setZoom(zt * (e.deltaY < 0 ? 1.15 : 1 / 1.15)); }, { passive: false });
    cv.style.touchAction = "pan-y";
    paintCtl(); size();
    if (window.ResizeObserver) new ResizeObserver(function () { if (stage.clientWidth !== W) size(); }).observe(stage); else window.addEventListener("resize", size);
    var asked = false;
    function boot() { if (asked) return; asked = true; getData(function (d) { D = d; DEST.forEach(function (x) { destIdx[d.idx[x.id]] = 1; }); draw(); }); if (layer !== "map") setLayer(layer); }
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (es) { if (es[0].isIntersecting) boot(); }, { rootMargin: "600px" }).observe(root);
      new IntersectionObserver(function (es) { es[0].isIntersecting && !document.hidden ? start() : stop(); }, { rootMargin: "100px" }).observe(root);
    } else { boot(); start(); }
    document.addEventListener("visibilitychange", function () { if (document.hidden) stop(); else if (root.getBoundingClientRect().top < innerHeight) start(); });
    root.kglobe = { show: show, layer: setLayer };
  }
  function boot() { document.querySelectorAll("[data-globe]").forEach(init); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
