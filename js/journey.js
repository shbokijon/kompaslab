// ═══════════════════════════════════════════════════════════════
//  Kompas Lab — "Mening yoʻlim" paneli (dashboard.html)
//  1) Kompas: strelka keyingi qadamga buriladi
//  2) Shaxsiy vaqt chizigʻi: maqsad sanasigacha haftalar va Lab hajmi
//  3) Hujjatlar javoni: modul yakunida tayyor boʻlgan hujjatlar
//  4) Haftalik ritm: oxirgi 8 haftada kabinetga kirilgan haftalar
//  Faqat shu qurilmadagi haqiqiy progressdan (localStorage) quriladi; soxta raqam yoʻq.
//  Ishlatish: <div id="journey"></div> + <script src="js/journey.js" defer></script>
// ═══════════════════════════════════════════════════════════════
(function () {
  var KEY = "kompas_journey_v1";
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  // Darslar soni: tools/landing/mods.json va CLAUDE.md dagi holat jadvali (17.10.2026)
  var LABS = [
    { id: "master", n: "Master Lab", lessons: 59, m0: "master-lab-m0.html", key: "kompas_master_m0_v1" },
    { id: "bachelor", n: "Bachelor Lab", lessons: 86, m0: "bachelor-lab-m0.html", key: "kompas_bachelor_m0_v1" },
    { id: "gks", n: "GKS Lab", lessons: 54, m0: "gks-lab-m0.html", key: "kompas_gks_m0_v1" },
    { id: "usa", n: "USA Lab", lessons: 46, m0: "usa-lab-m0.html", key: "kompas_usa_m0_v1" },
    { id: "daad", n: "DAAD Lab", lessons: 51, m0: "daad-lab.html", key: null },
    { id: "tt", n: "Tadbirkor Talaba", lessons: 54, m0: "tadbirkor-talaba-m0.html", key: "kompas_tt_m0_v1" },
    { id: "musofir", n: "Musofir Lab", lessons: 44, m0: "musofir-lab-m0.html", key: "kompas_musofir_m0_v1" }
  ];
  var PHD = { n: "PhD Lab M0", m0: "phd-lab-m0.html", key: "kompas_phd_m0_v1" };
  // Hujjatlar: qaysi modul yakunida qaysi hujjat tayyor boʻladi
  var DOCS = [
    { k: "kompas_master_m0_v1", m0: true, n: "Qaror bayonoti", s: "Master M0", ic: "seedling" },
    { k: "kompas_master_m1_v1", n: "Saralangan roʻyxat", s: "Master M1", ic: "telescope" },
    { k: "kompas_master_m2_v1", n: "Strategik hujjat", s: "Master M2", ic: "calendar" },
    { k: "kompas_master_m3_v1", n: "Akademik CV", s: "Master M3", ic: "scroll" },
    { k: "kompas_master_m4_v1", n: "Aloqa paketi", s: "Master M4", ic: "bell" },
    { k: "kompas_master_m5_v1", n: "Maqsad bayonnomasi", s: "Master M5", ic: "memo" },
    { k: "kompas_master_m6_v1", n: "Loyiha taklifi", s: "Master M6", ic: "books" },
    { k: "kompas_master_m7_v1", n: "Stipendiya portfeli", s: "Master M7", ic: "money" },
    { k: "kompas_master_m8_v1", n: "Joʻnash paketi", s: "Master M8", ic: "lock" },
    { k: "kompas_gks_m1_v1", n: "Hujjatlar nazorat jadvali", s: "GKS M1", ic: "scroll" },
    { k: "kompas_gks_m2_v1", n: "Universitet tanlovi", s: "GKS M2", ic: "telescope" },
    { k: "kompas_gks_m3u_v1", n: "Nomzod profili", s: "GKS M3-U", ic: "bulb" },
    { k: "kompas_gks_m4u_v1", n: "Shaxsiy bayonot", s: "GKS M4-U", ic: "memo" },
    { k: "kompas_gks_m5u_v1", n: "Reja, paket va intervyu", s: "GKS M5-U", ic: "calendar" },
    { k: "kompas_gks_m3m_v1", n: "STAR inventari va akademik CV", s: "GKS M3-M", ic: "scroll" },
    { k: "kompas_gks_m4m_v1", n: "Oʻquv rejasi", s: "GKS M4-M", ic: "calendar" },
    { k: "kompas_gks_m5m_v1", n: "Professor, bayonot va intervyu", s: "GKS M5-M", ic: "bell" },
    { k: "kompas_gks_m3d_v1", n: "Ilmiy pozitsiya", s: "GKS M3-D", ic: "telescope" },
    { k: "kompas_gks_m4d_v1", n: "Ilmiy reja", s: "GKS M4-D", ic: "books" },
    { k: "kompas_gks_m5d_v1", n: "Professor bilan muloqot va yakuniy paket", s: "GKS M5-D", ic: "bell" }
  ];
  var PACE = [[2, "Sekin: 2 dars/hafta (~2 soat)"], [4, "Oʻrtacha: 4 dars/hafta (~4 soat)"], [6, "Tez: 6 dars/hafta (~6 soat)"]];
  var DAY = 86400000, MON = ["yan", "fev", "mar", "apr", "may", "iyn", "iyl", "avg", "sen", "okt", "noy", "dek"];

  function load(k) { try { return JSON.parse(localStorage.getItem(k) || "null"); } catch (e) { return null; } }
  var S = load(KEY) || {};
  function save() { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {} }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function fmt(d) { return d.getDate() + "-" + MON[d.getMonth()] + " " + d.getFullYear(); }
  function today() { var d = new Date(); d.setHours(0, 0, 0, 0); return d; }
  function m0pct(key) { var o = key && load(key); return o && o.xp ? Math.min(100, Math.round(o.xp / 250 * 100)) : 0; }
  function done(doc) { var o = load(doc.k); if (!o) return false; return doc.m0 ? o.xp >= 250 : !!(o.done && o.done.fin); }
  // ISO hafta raqami (yil*100 + hafta)
  function week(d) { var t = new Date(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate())), n = t.getUTCDay() || 7; t.setUTCDate(t.getUTCDate() + 4 - n); var y = t.getUTCFullYear(), w = Math.ceil(((t - Date.UTC(y, 0, 1)) / DAY + 1) / 7); return y * 100 + w; }

  // ── Haftalik ritm: kabinet ochilgan haftani qayd qilish ──
  S.weeks = S.weeks || []; var wk = week(new Date());
  if (S.weeks.indexOf(wk) < 0) { S.weeks.push(wk); S.weeks = S.weeks.slice(-60); save(); }

  // ── Keyingi qadam ──
  function nextStep() {
    var all = LABS.filter(function (l) { return l.key; }).map(function (l) { return { n: l.n + " M0", href: l.m0, pct: m0pct(l.key) }; }).concat([{ n: PHD.n, href: PHD.m0, pct: m0pct(PHD.key) }]);
    var go = all.filter(function (m) { return m.pct > 0 && m.pct < 100; }).sort(function (a, b) { return b.pct - a.pct; })[0];
    if (go) return { t: "Davom eting: " + go.n, s: go.pct + "% bajarildi. Bir dars ~20–40 daqiqa.", href: go.href, b: "Davom etish →" };
    var fin = all.filter(function (m) { return m.pct >= 100; })[0];
    if (fin) {
      var lab = S.lab ? LABS.filter(function (l) { return l.id === S.lab; })[0] : null;
      return { t: fin.n + " yakunlangan", s: lab && !S.date ? "Pastda maqsad sanangizni kiriting: vaqt yetadimi, koʻrasiz." : "Keyingi qadam: Lab sahifasida dastur va tariflar.", href: fin.href.replace("-m0.html", ".html"), b: "Lab sahifasi →" };
    }
    return { t: "Bepul M0 dan boshlang", s: "Har Labning M0 qismi bepul: toʻlovdan oldin dastur sizga mosligini tekshirasiz.", href: "#modulesList", b: "M0 tanlash →" };
  }

  var CSS = '.jy{display:grid;gap:14px;margin:0 0 22px;}' +
    '.jy-c{background:#fff;border:1px solid var(--border,#e0e8e4);border-radius:16px;padding:16px 18px;}' +
    '.jy-h{display:flex;justify-content:space-between;align-items:baseline;gap:10px;margin-bottom:10px;}' +
    '.jy-h b{font-size:16.5px;color:var(--accent,#2d4a3e);}.jy-h span{font-size:13.5px;color:var(--muted,#6b7f76);}' +
    '.jy-next{display:grid;grid-template-columns:84px minmax(0,1fr);gap:16px;align-items:center;}' +
    '.jy-cmp{width:84px;height:84px;position:relative;}' +
    '.jy-cmp svg{width:100%;height:100%;display:block;}' +
    '.jy-ndl{transform-origin:42px 42px;transition:transform 1.6s cubic-bezier(.2,1.4,.4,1);}' +
    '.jy-next h3{font-size:16px;line-height:1.3;margin:0 0 4px;color:var(--text,#1a2e26);}.jy-next p{font-size:15px;color:var(--muted,#6b7f76);margin:0 0 10px;}' +
    '.jy-btn{display:inline-block;background:var(--accent2,#c4622d);color:#fff;text-decoration:none;font-weight:700;font-size:15px;padding:8px 16px;border-radius:10px;}' +
    '.jy-row{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:12px;}' +
    '.jy-row label{display:flex;flex-direction:column;gap:4px;font-size:13.5px;font-weight:700;color:var(--muted,#6b7f76);flex:1 1 150px;}' +
    '.jy-row select,.jy-row input{min-height:40px;border:1.5px solid var(--border,#e0e8e4);border-radius:10px;padding:6px 10px;font:inherit;font-size:16.5px;color:var(--text,#1a2e26);background:#fff;}' +
    '.jy-tl{position:relative;height:44px;margin:6px 0 4px;}' +
    '.jy-track{position:absolute;left:0;right:0;top:16px;height:12px;border-radius:99px;background:var(--accent-light,#e8f0ec);overflow:hidden;}' +
    '.jy-need{position:absolute;left:0;top:0;bottom:0;width:0;border-radius:99px;background:linear-gradient(90deg,var(--accent,#2d4a3e),#4e7a68);transition:width 1.4s cubic-bezier(.3,.9,.3,1);}' +
    '.jy-need.over{background:linear-gradient(90deg,var(--accent2,#c4622d),#e0896a);}' +
    '.jy-flag{position:absolute;top:0;transform:translateX(-50%);font-size:12.5px;font-weight:800;color:var(--muted,#6b7f76);white-space:nowrap;}' +
    '.jy-flag i{display:block;width:2px;height:14px;background:currentColor;margin:2px auto 0;}' +
    '.jy-tl .jy-now{left:0;transform:none;}.jy-tl .jy-dl{right:0;left:auto;transform:none;text-align:right;color:var(--accent2,#c4622d);}' +
    '.jy-tl .jy-dl i{margin-right:0;}.jy-tl .jy-now i{margin-left:0;}' +
    '.jy-v{font-size:15px;margin-top:8px;}.jy-v b{color:var(--accent,#2d4a3e);}.jy-v.over b{color:var(--accent2,#c4622d);}' +
    '.jy-shelf{display:grid;grid-template-columns:repeat(auto-fill,minmax(96px,1fr));gap:10px;}' +
    '.jy-doc{position:relative;text-align:center;font-size:13px;font-weight:700;line-height:1.25;color:var(--muted2,#9aada6);padding:10px 6px 8px;border-radius:12px;border:1.5px dashed var(--border,#e0e8e4);}' +
    '.jy-doc img{width:40px;height:40px;display:block;margin:0 auto 6px;filter:grayscale(1);opacity:.35;}' +
    '.jy-doc small{display:block;font-weight:600;font-size:12px;margin-top:2px;}' +
    '.jy-doc.on{border-style:solid;border-color:var(--accent,#2d4a3e);color:var(--accent,#2d4a3e);background:var(--accent-light,#e8f0ec);}' +
    '.jy-doc.on img{filter:none;opacity:1;}' +
    '.jy-doc.drop{animation:jyDrop .7s cubic-bezier(.3,1.6,.5,1) both;}' +
    '@keyframes jyDrop{0%{transform:translateY(-26px) rotate(-8deg);opacity:0}100%{transform:none;opacity:1}}' +
    '.jy-wk{display:flex;gap:6px;align-items:flex-end;}' +
    '.jy-wk span{flex:1;display:flex;flex-direction:column;align-items:center;gap:4px;font-size:12px;color:var(--muted2,#9aada6);}' +
    '.jy-wk i{width:100%;max-width:34px;height:34px;border-radius:9px;background:var(--accent-light,#e8f0ec);transform:scale(.6);opacity:.5;transition:transform .5s,opacity .5s,background .5s;}' +
    '.jy-wk i.on{background:var(--accent,#2d4a3e);}.jy-wk i.show{transform:none;opacity:1;}' +
    '.jy-wk span.cur i{outline:2px solid var(--accent2,#c4622d);outline-offset:2px;}' +
    '.jy-cal{margin-top:14px;}' +
    '.jy-ch{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:8px;margin-bottom:8px;}' +
    '.jy-ch b{font-size:15px;color:var(--accent,#2d4a3e);}' +
    '.jy-ca{display:flex;gap:6px;flex-wrap:wrap;}' +
    '.jy-mini{border:1.5px solid var(--border,#e0e8e4);background:#fff;color:var(--accent,#2d4a3e);font:inherit;font-weight:700;font-size:13.5px;padding:6px 11px;border-radius:9px;cursor:pointer;min-height:34px;}' +
    '.jy-mini:hover{background:var(--accent-light,#e8f0ec);}' +
    '.jy-g{display:grid;grid-template-columns:84px repeat(7,minmax(0,1fr));gap:5px;align-items:center;}' +
    '.jy-gh{font-size:12px;font-weight:800;color:var(--muted2,#9aada6);text-align:center;}' +
    '.jy-wl2{font-size:12px;color:var(--muted,#6b7f76);font-weight:700;white-space:nowrap;}' +
    '.jy-d{position:relative;height:38px;border-radius:9px;border:1.5px solid transparent;background:#f1f4f2;color:#8a9c94;font:inherit;font-size:12.5px;font-weight:700;cursor:pointer;padding:0;transition:transform .12s,background .2s;}' +
    '.jy-d:hover{transform:scale(1.07);}' +
    '.jy-d.p{background:#fbe9a8;border-color:#e6c94f;color:#6e5600;}' +
    '.jy-d.ok{background:#bfe5c9;border-color:#5fb176;color:#175c2d;}' +
    '.jy-d.miss{background:#f6c3bd;border-color:#dc6a60;color:#8a241b;}' +
    '.jy-d.past:not(.p):not(.ok):not(.miss){opacity:.55;}' +
    '.jy-d.td{outline:2px solid var(--accent,#2d4a3e);outline-offset:1px;}' +
    '.jy-d.dl::after{content:"\\1F6A9";position:absolute;right:1px;top:-7px;font-size:13px;}' +
    '.jy-lg{display:flex;flex-wrap:wrap;gap:12px;margin-top:10px;font-size:13px;color:var(--muted,#6b7f76);}' +
    '.jy-lg i{display:inline-block;width:12px;height:12px;border-radius:4px;margin-right:5px;vertical-align:-1px;border:1.5px solid transparent;}' +
    '.jy-sum{font-size:14.5px;margin-top:10px;}.jy-sum b{color:var(--accent,#2d4a3e);}' +
    '@media(max-width:600px){.jy-g{grid-template-columns:66px repeat(7,minmax(0,1fr));gap:4px;}.jy-d{height:34px;font-size:12px;}.jy-wl2{font-size:10.5px;}}' +
    '@media(max-width:600px){.jy-next{grid-template-columns:64px minmax(0,1fr);}.jy-cmp{width:64px;height:64px;}}' +
    '@media(prefers-reduced-motion:reduce){.jy-ndl,.jy-need,.jy-wk i{transition:none!important;}.jy-doc.drop{animation:none;}}';

  function render(root) {
    var st = document.createElement("style"); st.textContent = CSS; document.head.appendChild(st);
    var n = nextStep();
    root.className = "jy";
    root.innerHTML =
      // 1. Kompas
      '<div class="jy-c"><div class="jy-next"><div class="jy-cmp" aria-hidden="true"><svg viewBox="0 0 84 84"><circle cx="42" cy="42" r="39" fill="#fff" stroke="#e0e8e4" stroke-width="3"/><circle cx="42" cy="42" r="31" fill="none" stroke="#e8f0ec" stroke-width="2" stroke-dasharray="2 6"/>' +
      '<text x="42" y="15" text-anchor="middle" font-size="9" font-weight="800" fill="#6b7f76">N</text>' +
      '<g class="jy-ndl"><path d="M42 12 L48 42 L42 46 L36 42 Z" fill="#c4622d"/><path d="M42 72 L48 42 L42 38 L36 42 Z" fill="#2d4a3e"/></g><circle cx="42" cy="42" r="4" fill="#fff" stroke="#2d4a3e" stroke-width="2"/></svg></div>' +
      '<div><h3>' + esc(n.t) + "</h3><p>" + esc(n.s) + '</p><a class="jy-btn" href="' + esc(n.href) + '">' + esc(n.b) + "</a></div></div></div>" +
      // 2. Vaqt chizigʻi
      '<div class="jy-c"><div class="jy-h"><b>Mening vaqt chizigʻim</b><span>Maqsad sanasigacha</span></div>' +
      '<div class="jy-row"><label>Lab<select data-j="lab"><option value="">— tanlang —</option>' + LABS.map(function (l) { return '<option value="' + l.id + '"' + (S.lab === l.id ? " selected" : "") + ">" + l.n + " (" + l.lessons + " dars)</option>"; }).join("") + "</select></label>" +
      '<label>Ariza muddati<input type="date" data-j="date" value="' + esc(S.date || "") + '"></label>' +
      '<label>Surʼat<select data-j="pace">' + PACE.map(function (p) { return '<option value="' + p[0] + '"' + (+S.pace === p[0] || (!S.pace && p[0] === 4) ? " selected" : "") + ">" + p[1] + "</option>"; }).join("") + "</select></label></div>" +
      '<div class="jy-tl"><div class="jy-track"><div class="jy-need"></div></div><div class="jy-flag jy-now">Bugun<i></i></div><div class="jy-flag jy-dl"><i></i></div></div><div class="jy-v"></div><div class="jy-cal"></div></div>' +
      // 3. Hujjatlar javoni
      '<div class="jy-c"><div class="jy-h"><b>Hujjatlar javoni</b><span class="jy-cnt"></span></div><div class="jy-shelf"></div></div>' +
      // 4. Haftalik ritm
      '<div class="jy-c"><div class="jy-h"><b>Haftalik ritm</b><span class="jy-wl"></span></div><div class="jy-wk"></div></div>';

    // Kompas strelkasi: avval tebranadi, keyin keyingi qadam tomonga (oʻngga, 62°) toʻxtaydi
    var ndl = root.querySelector(".jy-ndl");
    if (reduce) ndl.style.transform = "rotate(62deg)";
    else { ndl.style.transform = "rotate(-140deg)"; requestAnimationFrame(function () { requestAnimationFrame(function () { ndl.style.transform = "rotate(62deg)"; }); }); }

    root.querySelectorAll("[data-j]").forEach(function (el) {
      el.addEventListener("change", function () { S[el.getAttribute("data-j")] = el.value; save(); timeline(root, true); calendar(root); });
    });
    timeline(root, false); calendar(root); shelf(root); rhythm(root);
  }

  function timeline(root, again) {
    var lab = LABS.filter(function (l) { return l.id === S.lab; })[0], dl = S.date ? new Date(S.date + "T00:00:00") : null, v = root.querySelector(".jy-v"), need = root.querySelector(".jy-need"), flag = root.querySelector(".jy-dl");
    if (!lab || !dl) { need.style.width = "0"; flag.innerHTML = "Muddat<i></i>"; v.className = "jy-v"; v.innerHTML = "Lab va ariza muddatini tanlang: kompas sizga necha hafta kerakligini va vaqt yetishini koʻrsatadi."; return; }
    var pace = +(S.pace || 4), weeksNeed = Math.ceil(lab.lessons / pace), weeksLeft = Math.floor((dl - today()) / DAY / 7);
    flag.innerHTML = fmt(dl) + "<i></i>";
    if (weeksLeft <= 0) { need.style.width = "100%"; need.classList.add("over"); v.className = "jy-v over"; v.innerHTML = "<b>Bu sana oʻtgan yoki juda yaqin.</b> Keyingi ariza siklini tanlang."; return; }
    var pct = Math.min(100, weeksNeed / weeksLeft * 100), over = weeksNeed > weeksLeft;
    need.classList.toggle("over", over);
    if (again && !reduce) { need.style.transition = "none"; need.style.width = "0"; void need.offsetWidth; need.style.transition = ""; }
    requestAnimationFrame(function () { need.style.width = pct + "%"; });
    var end = new Date(today().getTime() + weeksNeed * 7 * DAY);
    v.className = "jy-v" + (over ? " over" : "");
    v.innerHTML = over
      ? "<b>" + lab.n + " uchun ~" + weeksNeed + " hafta kerak, sizda " + weeksLeft + " hafta bor.</b> Surʼatni oshiring yoki keyingi siklni koʻzlang."
      : "<b>" + lab.n + ": ~" + weeksNeed + " hafta (taxminan " + fmt(end) + " gacha).</b> Muddatgacha " + weeksLeft + " hafta, zaxira " + (weeksLeft - weeksNeed) + " hafta.";
  }


  // ── Interaktiv kalendar: hafta × kun katakchalari ──
  // Katak holati (S.cal[YYYY-MM-DD]): 1 = reja (sariq), 2 = bajarildi (yashil).
  // Oʻtib ketgan rejali kun bajarilmagan boʻlsa qizil. Bosish: boʻsh → reja → bajarildi → boʻsh.
  // Faqat foydalanuvchi oʻzi belgilagan kunlar; avtomatik hisob-kitob yoʻq.
  var DN = ["Du", "Se", "Cho", "Pa", "Ju", "Sha", "Ya"];
  function ymd(d) { return d.getFullYear() + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2); }
  function monday(d) { var x = new Date(d.getFullYear(), d.getMonth(), d.getDate()); x.setDate(x.getDate() - ((x.getDay() + 6) % 7)); return x; }
  function calendar(root) {
    var box = root.querySelector(".jy-cal"); if (!box) return;
    S.cal = S.cal || {};
    var t = today(), tk = ymd(t), dl = S.date ? new Date(S.date + "T00:00:00") : null, dk = dl ? ymd(dl) : "";
    var start = new Date(monday(t).getTime() - 7 * DAY);
    var weeks = 8;
    if (dl && dl >= t) weeks = Math.min(60, Math.max(4, Math.ceil((monday(dl).getTime() - start.getTime()) / DAY / 7) + 1));
    var pace = +(S.pace || 4);
    var rows = "", nOk = 0, nPlan = 0, nMiss = 0;
    for (var w = 0; w < weeks; w++) {
      var ws = new Date(start.getTime() + w * 7 * DAY), we = new Date(ws.getTime() + 6 * DAY);
      rows += '<div class="jy-wl2">' + ws.getDate() + (ws.getMonth() !== we.getMonth() ? "-" + MON[ws.getMonth()] : "") + "–" + we.getDate() + " " + MON[we.getMonth()] + "</div>";
      for (var i = 0; i < 7; i++) {
        var d = new Date(ws.getTime() + i * DAY), k = ymd(d), v = S.cal[k] || 0, past = k < tk, cls = "jy-d";
        if (v === 2) { cls += " ok"; nOk++; } else if (v === 1 && past) { cls += " miss"; nMiss++; } else if (v === 1) { cls += " p"; nPlan++; }
        if (past) cls += " past"; if (k === tk) cls += " td"; if (k === dk) cls += " dl";
        var st = v === 2 ? "bajarildi" : v === 1 ? (past ? "oʻtkazib yuborilgan" : "rejalashtirilgan") : "boʻsh";
        rows += '<button type="button" class="' + cls + '" data-k="' + k + '" title="' + fmt(d) + ": " + st + (k === dk ? " (ariza muddati)" : "") + '" aria-label="' + fmt(d) + ", " + st + '">' + d.getDate() + "</button>";
      }
    }
    box.innerHTML =
      '<div class="jy-ch"><b>Haftalik reja</b><div class="jy-ca"><button type="button" class="jy-mini" data-a="auto">Surʼat boʻyicha toʻldirish</button><button type="button" class="jy-mini" data-a="clear">Tozalash</button></div></div>' +
      '<div class="jy-g"><span></span>' + DN.map(function (n) { return '<span class="jy-gh">' + n + "</span>"; }).join("") + rows + "</div>" +
      '<div class="jy-lg"><span><i style="background:#fbe9a8;border-color:#e6c94f"></i>Reja</span><span><i style="background:#bfe5c9;border-color:#5fb176"></i>Bajarildi</span><span><i style="background:#f6c3bd;border-color:#dc6a60"></i>Oʻtkazib yuborilgan</span><span><i style="background:#f1f4f2"></i>Boʻsh</span>' + (dl ? "<span>🚩 Ariza muddati</span>" : "") + "</div>" +
      '<div class="jy-sum">Bajarildi: <b>' + nOk + "</b> · Oldinda: <b>" + nPlan + "</b> · Oʻtkazib yuborilgan: <b>" + nMiss + "</b>. Katakni bosing: reja → bajarildi → boʻsh.</div>";
    box.querySelectorAll(".jy-d").forEach(function (b) {
      b.addEventListener("click", function () {
        var k = b.getAttribute("data-k"), v = ((S.cal[k] || 0) + 1) % 3;
        if (v) S.cal[k] = v; else delete S.cal[k];
        save(); calendar(root);
        var nb = root.querySelector('.jy-d[data-k="' + k + '"]'); if (nb) nb.focus();
      });
    });
    box.querySelector('[data-a="clear"]').addEventListener("click", function () {
      if (Object.keys(S.cal).length && !confirm("Hamma belgilar oʻchirilsinmi?")) return;
      S.cal = {}; save(); calendar(root);
    });
    box.querySelector('[data-a="auto"]').addEventListener("click", function () {
      // Haftasiga `pace` ta kun: dushanbadan boshlab teng taqsimlangan (bugundan keyingi kunlar)
      var PAT = { 1: [3], 2: [1, 4], 3: [0, 2, 4], 4: [0, 1, 3, 4], 5: [0, 1, 2, 3, 4], 6: [0, 1, 2, 3, 4, 5] };
      var pat = PAT[Math.min(6, Math.max(1, pace))] || PAT[4], last = dl && dl >= t ? dl : new Date(start.getTime() + weeks * 7 * DAY - DAY);
      for (var w2 = 0; w2 < weeks; w2++) pat.forEach(function (di) {
        var d2 = new Date(start.getTime() + (w2 * 7 + di) * DAY), k2 = ymd(d2);
        if (k2 >= tk && d2 <= last && !S.cal[k2]) S.cal[k2] = 1;
      });
      save(); calendar(root);
    });
  }

  function shelf(root) {
    var seen = S.shelf || [], got = 0;
    root.querySelector(".jy-shelf").innerHTML = DOCS.map(function (d, i) {
      var on = done(d); if (on) got++;
      var fresh = on && seen.indexOf(d.k) < 0;
      return '<div class="jy-doc' + (on ? " on" : "") + (fresh && !reduce ? " drop" : "") + '" style="animation-delay:' + (i * 0.12) + 's"><img src="img/3d/' + d.ic + '.webp" width="160" height="160" alt="" loading="lazy">' + esc(d.n) + "<small>" + (on ? "✓ " : "🔒 ") + esc(d.s) + "</small></div>";
    }).join("");
    root.querySelector(".jy-cnt").textContent = got + " / " + DOCS.length + " tayyor";
    S.shelf = DOCS.filter(done).map(function (d) { return d.k; }); save();
  }

  function rhythm(root) {
    var now = new Date(), cells = [], streak = 0, counting = true;
    for (var i = 7; i >= 0; i--) { var d = new Date(now.getTime() - i * 7 * DAY); cells.push({ w: week(d), d: d }); }
    for (var j = cells.length - 1; j >= 0; j--) { if (S.weeks.indexOf(cells[j].w) >= 0 && counting) streak++; else counting = false; }
    var box = root.querySelector(".jy-wk");
    box.innerHTML = cells.map(function (c, i) { return '<span class="' + (i === cells.length - 1 ? "cur" : "") + '"><i class="' + (S.weeks.indexOf(c.w) >= 0 ? "on" : "") + '"></i>' + c.d.getDate() + "-" + MON[c.d.getMonth()] + "</span>"; }).join("");
    box.querySelectorAll("i").forEach(function (el, i) { if (reduce) el.classList.add("show"); else setTimeout(function () { el.classList.add("show"); }, 80 * i); });
    root.querySelector(".jy-wl").textContent = streak >= 2 ? streak + " hafta ketma-ket" : "Har hafta kamida bir marta qayting";
  }

  function boot() { var r = document.getElementById("journey"); if (r) render(r); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
