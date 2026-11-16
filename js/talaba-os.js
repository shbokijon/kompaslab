// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — Talaba OS (os.html), 2026-11-16, MVP v1
//  Talabaning ish joyi: Bugun · Arizalarim · 4K yoʻlim · Ish stoli · Tekshiruv.
//  Maʼlumot: localStorage "kompas_os_v1" (Kabinet zaxirasi ham shu kalitni oladi).
//  Server: kompas_os_state jadvali boʻlsa, hisobga bogʻlanadi (migratsiya
//  supabase/migrations/20261116_talaba_os.sql). Jadval boʻlmasa, jim ishlaydi.
//  Tekshiruv boʻlimi qoidalar asosida ishlaydi (sunʼiy intellekt emas).
//  Soxta raqam yoʻq: hamma koʻrsatkich talabaning oʻz kiritganidan.
// ═══════════════════════════════════════════════════════════════
(function () {
  "use strict";
  var KEY = "kompas_os_v1";
  var DAY = 86400000;
  var MON = ["yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avgust", "sentabr", "oktabr", "noyabr", "dekabr"];
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  function esc(v) { return String(v == null ? "" : v).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function uid() { return Date.now().toString(36) + Math.random().toString(36).slice(2, 6); }
  function today() { var d = new Date(); d.setHours(0, 0, 0, 0); return d; }
  function parseD(s) { if (!s) return null; var p = s.split("-"); var d = new Date(+p[0], +p[1] - 1, +p[2] || 1); return isNaN(d) ? null : d; }
  function fmtD(s) { var d = parseD(s); return d ? d.getDate() + "-" + MON[d.getMonth()] + " " + d.getFullYear() : "—"; }
  function daysLeft(s) { var d = parseD(s); return d ? Math.round((d - today()) / DAY) : null; }
  function snd(n) { try { if (window.KSfx) KSfx.play(n); } catch (e) {} }

  // ── Maʼlumotlar tuzilmasi ─────────────────────────────────
  function blank() { return { v: 1, updated: 0, profile: {}, apps: [], road: {}, drafts: [], checks: {} }; }
  function load() { try { var o = JSON.parse(localStorage.getItem(KEY) || "null"); if (o && o.v === 1) return Object.assign(blank(), o); } catch (e) {} return blank(); }
  var S = load();
  var saveT = null;
  function save(silent) {
    S.updated = Date.now();
    try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) { toast("Saqlab boʻlmadi: brauzer xotirasi toʻlgan boʻlishi mumkin."); }
    clearTimeout(saveT); saveT = setTimeout(Sync.push, 3000);
    if (!silent) flash();
  }
  function flash() { var b = $("#osSaved"); if (!b) return; b.classList.add("on"); clearTimeout(b._t); b._t = setTimeout(function () { b.classList.remove("on"); }, 1200); }

  // ── Server bilan bogʻlash (jadval boʻlsa) ─────────────────
  var Sync = {
    user: null, off: false,
    start: function (user) {
      Sync.user = user; var sb = window.supabase;
      if (!sb || typeof sb.from !== "function") return;
      sb.from("kompas_os_state").select("state,updated_at").maybeSingle().then(function (r) {
        if (r.error) { Sync.off = true; return; }
        var remote = r.data && r.data.state;
        if (remote && remote.v === 1 && (+remote.updated || 0) > (+S.updated || 0)) {
          S = Object.assign(blank(), remote); try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {}
          renderAll(); toast("Boshqa qurilmadagi oʻzgarishlar olindi.");
        } else if (S.updated) Sync.push();
        setBadge();
      }, function () { Sync.off = true; });
    },
    push: function () {
      var sb = window.supabase;
      if (!Sync.user || Sync.off || !sb) return;
      sb.from("kompas_os_state").upsert({ state: S, updated_at: new Date(S.updated || Date.now()).toISOString() }, { onConflict: "user_id" }).then(function (r) { if (r && r.error) Sync.off = true; setBadge(); }, function () {});
    }
  };
  function setBadge() {
    var b = $("#osSync"); if (!b) return;
    var on = Sync.user && !Sync.off;
    b.textContent = on ? "☁ Hisobingizga saqlanadi" : "💾 Shu qurilmada saqlanadi";
    b.title = on ? "Boshqa qurilmada kirsangiz ham shu maʼlumot chiqadi." : "Maʼlumot shu brauzerda. Zaxira: Kabinet → Zaxirani yuklab olish.";
  }

  // ── Lugʻatlar ─────────────────────────────────────────────
  var STAGES = [
    { id: "kirish", n: "Kirish", s: "Universitetga kirish: tanlov, hujjatlar, ariza", ic: "🧭" },
    { id: "ketish", n: "Ketish", s: "Qabul xatidan keyin: moliya, viza, sugʻurta, yoʻl", ic: "🧳" },
    { id: "kampus", n: "Kampus", s: "Oʻqish davri: oʻqish, amaliyot, ilmiy ish", ic: "🏛" },
    { id: "karyera", n: "Karyera", s: "Bitirgandan keyin: ish, keyingi daraja yoki qaytish", ic: "🎯" }
  ];
  var LEVELS = [["bachelor", "Bakalavr"], ["master", "Magistratura"], ["phd", "PhD"], ["exchange", "Almashinuv / qisqa dastur"]];
  var STATUS = [
    ["idea", "Koʻrib chiqyapman", "#6b7f76"],
    ["prep", "Tayyorlanyapman", "#b08a00"],
    ["sent", "Topshirildi", "#1a56a0"],
    ["interview", "Intervyu / qoʻshimcha", "#7a4fb0"],
    ["accepted", "Qabul qilindi", "#1a7a4a"],
    ["rejected", "Rad etildi", "#c0392b"],
    ["dropped", "Voz kechdim", "#9aada6"]
  ];
  function stInfo(id) { return STATUS.filter(function (s) { return s[0] === id; })[0] || STATUS[0]; }
  var DOCS = [
    ["cv", "CV (rezyume)"], ["sop", "Motivatsion xat / SoP"], ["rec1", "Tavsiya xati 1"], ["rec2", "Tavsiya xati 2"],
    ["transcript", "Diplom va baholar varaqasi"], ["lang", "Til sertifikati"], ["passport", "Pasport nusxasi"]
  ];
  var DOCS_EXTRA = [["proposal", "Ilmiy loyiha taklifi (research proposal)"], ["portfolio", "Portfolio"], ["test", "SAT / GRE / GMAT natijasi"], ["finance", "Moliyaviy hujjat"], ["essay", "Qoʻshimcha insho"]];

  // 4K yoʻli: umumiy qadamlar (sanalar va kvotalar yoʻq — ular dastur sahifasida)
  var ROAD = {
    kirish: [
      ["k1", "Darajam, soham va boshlanish yilim aniq", "master-lab-m0.html", "Master M0"],
      ["k2", "5–8 ta universitet yoki stipendiya roʻyxatim bor", "#arizalar", "Arizalarim"],
      ["k3", "Har birining rasmiy talablari va muddatini oʻz sahifasidan tekshirdim", "#arizalar", "Arizalarim"],
      ["k4", "Til sertifikati: qaysi test, qaysi ball, qachon", "atlas-ingliz-tili-testi.html", "Atlas"],
      ["k5", "CV ning birinchi nusxasi tayyor", "#ish-stoli", "Ish stoli"],
      ["k6", "Tavsiya beradigan 2–3 kishi bilan gaplashdim", "#ish-stoli", "Ish stoli"],
      ["k7", "Motivatsion xat (SoP) yozildi va boshqa odam oʻqib chiqdi", "#tekshiruv", "Tekshiruv"],
      ["k8", "Kamida bitta ariza topshirildi", "#arizalar", "Arizalarim"]
    ],
    ketish: [
      ["t1", "Qabul xati (offer) shartlarini oʻqib, javob muddatini yozdim", "#arizalar", "Arizalarim"],
      ["t2", "Birinchi yil xarajatlari hisoblandi: oʻqish, yashash, sugʻurta, yoʻl", null, null],
      ["t3", "Viza talablari elchixona yoki rasmiy sahifadan olindi", null, null],
      ["t4", "Viza hujjatlari yigʻildi va ariza topshirildi", null, null],
      ["t5", "Tibbiy sugʻurta tanlandi", null, null],
      ["t6", "Yotoqxona yoki ijara uy topildi", null, null],
      ["t7", "Chipta olindi, kelish kuni universitetga xabar qilindi", null, null]
    ],
    kampus: [
      ["c1", "Universitetda roʻyxatdan oʻtdim, talaba guvohnomasi olindi", null, null],
      ["c2", "Bank hisobi va telefon raqami ochildi", null, null],
      ["c3", "Birinchi semestr fanlari va baholash qoidalarini oʻqidim", null, null],
      ["c4", "Har fan oʻqituvchisi bilan kamida bir marta gaplashdim", null, null],
      ["c5", "Akademik yozish va manba keltirish qoidalarini oʻrgandim", null, null],
      ["c6", "Amaliyot (internship) yoki ilmiy loyihaga ariza berdim", null, null]
    ],
    karyera: [
      ["r1", "Yoʻlim tanlandi: ish, keyingi daraja yoki Oʻzbekistonga qaytish", null, null],
      ["r2", "Bitiruvdan keyingi viza yoki yashash qoidasini rasmiy sahifadan tekshirdim", null, null],
      ["r3", "CV yangilandi: loyihalar, natijalar, koʻnikmalar", "#ish-stoli", "Ish stoli"],
      ["r4", "Sohamdagi 10 ta odam bilan aloqa (LinkedIn, konferensiya)", null, null],
      ["r5", "Ish yoki PhD arizalari topshirildi", "#arizalar", "Arizalarim"]
    ]
  };

  var DTYPES = [
    ["sop", "Motivatsion xat / SoP", 1000],
    ["cv", "CV (rezyume)", 0],
    ["rec", "Tavsiya soʻrovi (oʻqituvchiga xat)", 250],
    ["prof", "Professorga xat (cold email)", 250],
    ["essay", "Insho", 650],
    ["proposal", "Ilmiy loyiha taklifi", 1500],
    ["other", "Boshqa", 0]
  ];
  function dType(id) { return DTYPES.filter(function (t) { return t[0] === id; })[0] || DTYPES[6]; }
  // Tuzilma andozalari: faqat qism nomlari, tayyor gap yoʻq — matnni talaba oʻzi yozadi
  var SKEL = {
    sop: "[1. Boshlanish: qaysi dasturga va nega aynan shu soha? Bitta aniq voqea yoki savoldan boshlang.]\n\n[2. Tayyorgarligim: oʻqish, loyiha, ish. Har biri uchun nima qildim va natija nima boʻldi.]\n\n[3. Nega aynan shu universitet: aniq fan, laboratoriya yoki professor nomi.]\n\n[4. Keyingi reja: bitirgandan keyin 3–5 yilda nima qilaman.]\n",
    cv: "ISM FAMILIYA\nEmail · Telefon · Shahar · LinkedIn\n\nTAʼLIM\n[Universitet, yoʻnalish, yillar, GPA]\n\nTAJRIBA\n[Lavozim, tashkilot, yillar — 2–3 ta natija, feʼl bilan boshlang]\n\nLOYIHALAR / ILMIY ISH\n[]\n\nKOʻNIKMALAR VA TILLAR\n[]\n",
    rec: "[Salom va kimligingiz: qaysi fanda, qaysi yili oʻqigansiz.]\n\n[Soʻrov: qaysi dasturga, qaysi muddatgacha tavsiya kerak.]\n\n[Yordam uchun: CV, dastur havolasi, siz haqingizda eslatma — ilova qilinadi.]\n\n[Rahmat va javob kutish.]\n",
    prof: "[Mavzu qatori: aniq va qisqa, masalan dastur + soha.]\n\n[1-gap: kimsiz va nima uchun yozyapsiz.]\n\n[2–3 gap: professorning qaysi ishini oʻqidingiz va sizni nima qiziqtirdi.]\n\n[2 gap: sizning tegishli tajribangiz.]\n\n[Aniq savol: masalan, keyingi yilga talaba olasizmi?]\n",
    essay: "[Savolni shu yerga koʻchiring.]\n\n[Javobingiz.]\n",
    proposal: "[Sarlavha]\n\n[Muammo va savol]\n\n[Hozirgi bilim: kim nima qilgan]\n\n[Usul va maʼlumot]\n\n[Kutilayotgan natija va ahamiyati]\n\n[Reja (oylar boʻyicha)]\n\n[Manbalar]\n",
    other: ""
  };

  // ── Tekshiruv qoidalari (rubrika) ─────────────────────────
  var RUBRIC = {
    sop: [
      ["Birinchi paragraf aniq voqea yoki savol bilan boshlanadi, umumiy gap bilan emas", 2],
      ["Nega aynan shu dastur: kamida bitta aniq fan, laboratoriya yoki professor nomi bor", 3],
      ["Har bir daʼvo dalil bilan: loyiha, natija, raqam yoki ish", 3],
      ["Keyingi reja aniq: lavozim, soha yoki loyiha", 2],
      ["Har paragraf bitta fikr haqida", 1],
      ["Matnni boshqa odam oʻqib, fikr bildirdi", 2],
      ["Imlo va grammatika tekshirildi", 1]
    ],
    cv: [
      ["1–2 sahifa, tartib: eng yangisi tepada", 2],
      ["Har tajribada natija bor (nima oʻzgardi), vazifalar roʻyxati emas", 3],
      ["Sana, tashkilot va shahar har qatorda bir xil formatda", 1],
      ["Rasm, tugʻilgan sana, oilaviy holat yoʻq (agar dastur talab qilmasa)", 1],
      ["Email jiddiy koʻrinishda (ism.familiya@…)", 1],
      ["PDF qilib saqlandi, fayl nomida ism bor", 1]
    ],
    rec: [
      ["Kimligingiz va qaysi fanda oʻqiganingiz eslatildi", 2],
      ["Muddat aniq yozildi va kamida 3–4 hafta vaqt bor", 3],
      ["CV va dastur havolasi ilova qilindi", 2],
      ["Xat qisqa: 200 soʻzdan oshmaydi", 1]
    ],
    prof: [
      ["Mavzu qatori aniq", 2],
      ["Professorning aniq ishi (maqola, loyiha) tilga olindi", 3],
      ["Oʻzingiz haqingizda 2–3 gapdan oshmaydi", 1],
      ["Oxirida bitta aniq savol bor", 2],
      ["CV ilova qilindi", 1]
    ],
    essay: [
      ["Savolga toʻgʻridan-toʻgʻri javob beradi", 3],
      ["Kamida bitta shaxsiy, aniq misol bor", 2],
      ["Soʻz cheklovi ichida", 2],
      ["Boshqa odam oʻqib chiqdi", 1]
    ],
    proposal: [
      ["Ilmiy savol bitta jumlada aytilgan", 3],
      ["Mavjud ishlar manba bilan keltirilgan", 2],
      ["Usul savolga mos va bajarsa boʻladigan", 2],
      ["Vaqt rejasi bor", 1],
      ["Manbalar roʻyxati bir xil formatda", 1]
    ],
    other: [["Matn maqsadi aniq", 1], ["Boshqa odam oʻqib chiqdi", 1]]
  };
  // Shablon va boʻsh iboralar: komissiya koʻp koʻradigan, maʼno bermaydigan gaplar
  var CLICHE_EN = ["passionate", "passion for", "since i was a child", "since childhood", "ever since i was", "i have always been", "i have always wanted", "from a young age", "dream come true", "in today's world", "in today’s world", "in this day and age", "ever-changing", "ever-evolving", "fast-paced world", "delve", "tapestry", "embark on a journey", "journey of", "unwavering", "testament to", "pivotal role", "plays a crucial role", "a myriad of", "it is worth noting", "furthermore", "moreover", "in conclusion", "to sum up", "make a difference", "give back to society", "hard-working", "team player", "think outside the box", "eager to learn", "broaden my horizons"];
  var CLICHE_UZ = ["shunchaki", "aslida esa", "bugungi globallashuv", "globallashuv davrida", "taʼkidlash joizki", "shuni aytish kerakki", "bolaligimdan", "orzuim edi", "katta ahamiyatga ega", "muhim rol oʻynaydi", "yangi ufqlar", "xulosa qilib aytganda"];
  var STOP = "the a an and or of to in on for with at by from as is are was were be been i my me we our you your it its this that these those which who have has had do did not but so if than then there their they he she his her them also can will would should could into about more most very such".split(" ");

  function words(t) { return (t.toLowerCase().match(/[a-zа-яёʻʼ'’ğşçöüñ0-9-]+/gi) || []); }
  function autoCheck(text, limit) {
    var w = words(text), n = w.length, out = [];
    var sents = text.split(/[.!?]+\s/).map(function (s) { return s.trim(); }).filter(function (s) { return s.split(/\s+/).length > 2; });
    var avg = sents.length ? Math.round(n / sents.length) : 0;
    var paras = text.split(/\n\s*\n/).filter(function (p) { return p.trim().length > 40; }).length;
    var low = " " + text.toLowerCase().replace(/\s+/g, " ") + " ";
    var hits = CLICHE_EN.concat(CLICHE_UZ).filter(function (c) { return low.indexOf(c) >= 0; });
    var cnt = {}; w.forEach(function (x) { if (x.length > 3 && STOP.indexOf(x) < 0) cnt[x] = (cnt[x] || 0) + 1; });
    var rep = Object.keys(cnt).filter(function (k) { return cnt[k] >= Math.max(5, n / 80); }).sort(function (a, b) { return cnt[b] - cnt[a]; }).slice(0, 5);
    var iCount = w.filter(function (x) { return x === "i"; }).length;
    var iStart = sents.filter(function (s) { return /^i\s/i.test(s); }).length;
    var bracket = (text.match(/\[[^\]]{3,}\]/g) || []).length;
    if (!n) return { n: 0, items: [{ ok: false, t: "Matn hali yozilmagan." }] };
    if (limit) out.push({ ok: n <= limit && n >= limit * 0.6, t: "Soʻzlar: " + n + " / " + limit + (n > limit ? " — cheklovdan " + (n - limit) + " ta oshgan." : n < limit * 0.6 ? " — cheklovning 60% idan kam: imkoniyatdan toʻliq foydalanmayapsiz." : " — meʼyorda.") });
    else out.push({ ok: true, t: "Soʻzlar: " + n + "." });
    out.push({ ok: !bracket, t: bracket ? bracket + " ta [ ] andoza qismi hali toʻldirilmagan." : "Andoza qismlari toʻldirilgan." });
    out.push({ ok: !hits.length, t: hits.length ? "Shablon iboralar (" + hits.length + "): " + hits.slice(0, 8).map(function (h) { return "«" + h + "»"; }).join(", ") + ". Ularni oʻz misolingiz bilan almashtiring." : "Koʻp uchraydigan shablon iboralar topilmadi." });
    out.push({ ok: avg <= 25, t: "Oʻrtacha gap uzunligi: " + avg + " soʻz" + (avg > 25 ? " — uzun. 15–22 soʻz oʻqishga qulay." : ".") });
    if (rep.length) out.push({ ok: false, t: "Koʻp takrorlangan soʻzlar: " + rep.map(function (k) { return k + " (" + cnt[k] + ")"; }).join(", ") + "." });
    if (sents.length >= 6) out.push({ ok: iStart / sents.length < 0.35, t: "«I» bilan boshlangan gaplar: " + iStart + " / " + sents.length + (iStart / sents.length >= 0.35 ? " — juda koʻp. Gap boshini almashtiring." : ".") });
    if (n > 250) out.push({ ok: paras >= 3, t: "Paragraflar: " + paras + (paras < 3 ? " — matnni maʼno boʻyicha boʻling (boʻsh qator bilan)." : ".") });
    if ((text.match(/!/g) || []).length > 1) out.push({ ok: false, t: "Undov belgisi koʻp: rasmiy matnda odatda ishlatilmaydi." });
    return { n: n, items: out, iCount: iCount };
  }

  // ── Toast ─────────────────────────────────────────────────
  function toast(t) {
    var el = $("#osToast"); if (!el) return;
    el.textContent = t; el.classList.add("on"); clearTimeout(el._t); el._t = setTimeout(function () { el.classList.remove("on"); }, 2600);
  }

  // ── Hisob-kitob ───────────────────────────────────────────
  function appDocs(a) { var keys = Object.keys(a.docs || {}); return { total: keys.length, done: keys.filter(function (k) { return a.docs[k]; }).length }; }
  function activeApps() { return S.apps.filter(function (a) { return ["rejected", "dropped", "accepted"].indexOf(a.status) < 0; }); }
  function stage() { return S.profile.stage || "kirish"; }
  function roadPct(st) { var l = ROAD[st], d = l.filter(function (x) { return S.road[x[0]]; }).length; return { d: d, t: l.length, p: Math.round(d / l.length * 100) }; }
  function nextRoad() { var st = stage(); return ROAD[st].filter(function (x) { return !S.road[x[0]]; })[0]; }
  function name() { return S.profile.name || ""; }

  function nextAction() {
    // 1) muddati yaqin, hujjati toʻliq boʻlmagan ariza
    var apps = activeApps().filter(function (a) { return a.deadline && a.status !== "sent" && a.status !== "interview"; })
      .map(function (a) { return { a: a, d: daysLeft(a.deadline), k: appDocs(a) }; })
      .filter(function (x) { return x.d !== null && x.d >= 0; }).sort(function (x, y) { return x.d - y.d; });
    var u = apps[0];
    if (u && u.k.done < u.k.total) {
      var miss = Object.keys(u.a.docs).filter(function (k) { return !u.a.docs[k]; }).map(docName);
      return { ic: "⏳", t: u.a.name + ": " + u.d + " kun qoldi", s: "Sizning ariza paketingizda yana " + (u.k.total - u.k.done) + " ta hujjat yetishmaydi: " + miss.slice(0, 3).join(", ") + (miss.length > 3 ? "…" : "") + ".", go: "arizalar", id: u.a.id, b: "Paketni ochish" };
    }
    if (u) return { ic: "📮", t: u.a.name + " paketi tayyor", s: "Hujjatlar toʻliq. Topshirgach, holatini «Topshirildi» qiling — " + u.d + " kun qoldi.", go: "arizalar", id: u.a.id, b: "Arizani ochish" };
    if (!S.apps.length) return { ic: "🎯", t: "Birinchi arizangizni qoʻshing", s: "Universitet yoki stipendiya nomi va muddati yetarli. Hujjatlar roʻyxatini OS oʻzi tuzadi.", go: "arizalar", add: true, b: "Ariza qoʻshish" };
    var r = nextRoad();
    if (r) return { ic: "🧭", t: r[1], s: "Bu 4K yoʻlingizning " + STAGES.filter(function (x) { return x.id === stage(); })[0].n + " bosqichidagi keyingi qadam.", go: "yol", b: "Yoʻlni ochish" };
    return { ic: "✅", t: "Bu bosqich qadamlari bajarilgan", s: "Keyingi bosqichga oʻting yoki arizalaringiz holatini yangilang.", go: "yol", b: "4K yoʻlim" };
  }
  function docName(k) { var d = DOCS.concat(DOCS_EXTRA).filter(function (x) { return x[0] === k; })[0]; return d ? d[1] : k.replace(/^c_/, ""); }

  // ═══ RENDER ═══════════════════════════════════════════════
  var TAB = "bugun", openApp = null, openDraft = null, checkDraft = null;
  var TABS = [["bugun", "Bugun", "☀"], ["arizalar", "Arizalarim", "📮"], ["yol", "4K yoʻlim", "🧭"], ["ish-stoli", "Ish stoli", "✍"], ["tekshiruv", "Tekshiruv", "🔍"]];
  var ALIAS = { "arizalar": "arizalar", "yol": "yol", "4k": "yol", "ish-stoli": "ish-stoli", "tekshiruv": "tekshiruv", "bugun": "bugun" };

  function go(t, opt) {
    TAB = ALIAS[t] || "bugun"; opt = opt || {};
    if (opt.app !== undefined) openApp = opt.app;
    if (opt.draft !== undefined) openDraft = opt.draft;
    if (history.replaceState) history.replaceState(null, "", "#" + TAB);
    renderAll();
    if (opt.add) setTimeout(function () { appForm(); }, 30);
    window.scrollTo(0, 0);
  }

  function renderAll() {
    $$(".os-tab").forEach(function (b) { var on = b.getAttribute("data-tab") === TAB; b.classList.toggle("on", on); b.setAttribute("aria-current", on ? "page" : "false"); });
    var v = $("#osView");
    if (!S.profile.stage && TAB === "bugun") { v.innerHTML = vOnboard(); bindOnboard(); return; }
    v.innerHTML = TAB === "bugun" ? vToday() : TAB === "arizalar" ? vApps() : TAB === "yol" ? vRoad() : TAB === "ish-stoli" ? vDesk() : vCheck();
    bindView();
  }

  // ── Birinchi kirish ───────────────────────────────────────
  var ob = {};
  function vOnboard() {
    var y = new Date().getFullYear();
    return '<section class="os-card os-onb">' +
      '<div class="os-kicker">Talaba OS · 1 daqiqa</div>' +
      '<h2>Sizning ish joyingizni sozlaymiz</h2>' +
      '<p class="os-muted">Uchta savol. Javoblarga qarab bosh sahifa sizga keyingi qadamni koʻrsatadi. Keyin «Sozlash» dan oʻzgartirasiz.</p>' +
      '<div class="os-q"><b>1. Hozir 4K yoʻlining qaysi bosqichidasiz?</b><div class="os-opts">' +
      STAGES.map(function (s) { return '<button type="button" class="os-opt" data-ob="stage" data-v="' + s.id + '"><span>' + s.ic + '</span><b>' + s.n + '</b><small>' + s.s + '</small></button>'; }).join("") + '</div></div>' +
      '<div class="os-q"><b>2. Qaysi darajaga intilyapsiz?</b><div class="os-chips">' +
      LEVELS.map(function (l) { return '<button type="button" class="os-chip" data-ob="level" data-v="' + l[0] + '">' + l[1] + '</button>'; }).join("") + '</div></div>' +
      '<div class="os-q"><b>3. Qachon oʻqishni boshlamoqchisiz?</b><div class="os-chips">' +
      [y, y + 1, y + 2].map(function (n) { return '<button type="button" class="os-chip" data-ob="year" data-v="' + n + '">' + n + '</button>'; }).join("") +
      '<button type="button" class="os-chip" data-ob="year" data-v="">Hali bilmayman</button></div></div>' +
      '<label class="os-field"><span>Soha (ixtiyoriy)</span><input id="obField" placeholder="masalan: geofizika, IT, biznes" maxlength="60" data-suggest="off"></label>' +
      '<button type="button" class="os-btn" id="obGo" disabled>Ish joyimni ochish →</button></section>';
  }
  function bindOnboard() {
    $$("[data-ob]").forEach(function (b) {
      b.addEventListener("click", function () {
        var k = b.getAttribute("data-ob"); ob[k] = b.getAttribute("data-v");
        $$('[data-ob="' + k + '"]').forEach(function (x) { x.classList.toggle("on", x === b); });
        snd("pick"); $("#obGo").disabled = !ob.stage;
      });
    });
    $("#obGo").addEventListener("click", function () {
      S.profile.stage = ob.stage; S.profile.level = ob.level || ""; S.profile.year = ob.year || ""; S.profile.field = ($("#obField").value || "").trim();
      if (!S.apps.length) S.profile.fresh = 1;
      save(); snd("win"); renderAll();
    });
  }

  // ── Bugun ─────────────────────────────────────────────────
  function vToday() {
    var na = nextAction(), st = stage(), rp = roadPct(st);
    var up = S.apps.filter(function (a) { var d = daysLeft(a.deadline); return d !== null && d >= 0 && ["rejected", "dropped", "accepted", "sent"].indexOf(a.status) < 0; })
      .sort(function (a, b) { return daysLeft(a.deadline) - daysLeft(b.deadline); }).slice(0, 4);
    var docT = 0, docD = 0; activeApps().forEach(function (a) { var k = appDocs(a); docT += k.total; docD += k.done; });
    var lvl = (LEVELS.filter(function (l) { return l[0] === S.profile.level; })[0] || [0, ""])[1];
    var goal = [lvl, S.profile.field, S.profile.year ? S.profile.year + "-yil" : ""].filter(Boolean).join(" · ");
    var drafts = S.drafts.slice().sort(function (a, b) { return b.updated - a.updated; }).slice(0, 3);
    return '<div class="os-hello"><h1>' + esc(greet()) + (name() ? ", " + esc(name()) : "") + '</h1><p>' + (goal ? "Sizning maqsadingiz: <b>" + esc(goal) + "</b>" : "Maqsadingizni «Sozlash» da kiriting.") + ' · <button type="button" class="os-link" id="osSetup">Sozlash</button></p></div>' +
      '<section class="os-card os-next"><div class="os-next-ic">' + na.ic + '</div><div><div class="os-kicker">Keyingi qadamingiz</div><h2>' + esc(na.t) + '</h2><p>' + esc(na.s) + '</p>' +
      '<button type="button" class="os-btn" data-go="' + na.go + '"' + (na.id ? ' data-app="' + na.id + '"' : "") + (na.add ? ' data-add="1"' : "") + '>' + esc(na.b) + ' →</button></div></section>' +
      '<div class="os-grid3">' +
      '<button type="button" class="os-stat" data-go="yol"><span>4K bosqichingiz</span><b>' + esc(STAGES.filter(function (x) { return x.id === st; })[0].n) + '</b><i class="os-bar"><i style="width:' + rp.p + '%"></i></i><small>' + rp.d + " / " + rp.t + ' qadam</small></button>' +
      '<button type="button" class="os-stat" data-go="arizalar"><span>Arizalaringiz</span><b>' + activeApps().length + ' faol</b><small>' + S.apps.filter(function (a) { return a.status === "sent" || a.status === "interview"; }).length + " ta topshirilgan · " + S.apps.filter(function (a) { return a.status === "accepted"; }).length + ' ta qabul</small></button>' +
      '<button type="button" class="os-stat" data-go="arizalar"><span>Ariza paketingiz</span><b>' + (docT ? Math.round(docD / docT * 100) + "%" : "—") + '</b><i class="os-bar"><i style="width:' + (docT ? Math.round(docD / docT * 100) : 0) + '%"></i></i><small>' + docD + " / " + docT + ' hujjat tayyor</small></button></div>' +
      '<section class="os-card"><div class="os-h"><h3>Yaqin muddatlaringiz</h3><button type="button" class="os-link" data-go="arizalar">Hammasi</button></div>' +
      (up.length ? '<ul class="os-dl">' + up.map(function (a) { var d = daysLeft(a.deadline); return '<li><button type="button" data-go="arizalar" data-app="' + a.id + '"><span class="os-days ' + (d <= 14 ? "hot" : d <= 45 ? "warm" : "") + '">' + d + '<small>kun</small></span><span><b>' + esc(a.name) + '</b><small>' + esc([a.program, a.country].filter(Boolean).join(" · ")) + " · " + fmtD(a.deadline) + '</small></span></button></li>'; }).join("") + "</ul>"
        : '<p class="os-muted">Muddat kiritilgan faol ariza yoʻq. Muddatni har dasturning rasmiy sahifasidan oling.</p>') + '</section>' +
      '<section class="os-card"><div class="os-h"><h3>Ish stolingizdagi hujjatlar</h3><button type="button" class="os-link" data-go="ish-stoli">Ish stoli</button></div>' +
      (drafts.length ? '<ul class="os-mini">' + drafts.map(function (d) { var w = words(d.text).length; return '<li><button type="button" data-go="ish-stoli" data-draft="' + d.id + '"><b>' + esc(d.title) + '</b><small>' + esc(dType(d.type)[1]) + " · " + w + ' soʻz · ' + ago(d.updated) + '</small></button></li>'; }).join("") + "</ul>"
        : '<p class="os-muted">Hali hujjat yoʻq. CV yoki motivatsion xatdan boshlang: andoza qismlarini koʻrsatadi, matnni oʻzingiz yozasiz.</p>') + '</section>' +
      '<p class="os-foot">Darslar va M0 progressingiz — <a href="dashboard.html">Kabinetda</a>.</p>';
  }
  function greet() { var h = new Date().getHours(); return h < 5 ? "Xayrli tun" : h < 12 ? "Xayrli tong" : h < 17 ? "Xayrli kun" : "Xayrli kech"; }
  function ago(t) { if (!t) return ""; var m = Math.round((Date.now() - t) / 60000); return m < 1 ? "hozirgina" : m < 60 ? m + " daqiqa oldin" : m < 1440 ? Math.round(m / 60) + " soat oldin" : Math.round(m / 1440) + " kun oldin"; }

  // ── Arizalarim ────────────────────────────────────────────
  function vApps() {
    if (openApp) { var a = S.apps.filter(function (x) { return x.id === openApp; })[0]; if (a) return vAppOne(a); openApp = null; }
    var list = S.apps.slice().sort(function (a, b) {
      var oa = STATUS.findIndex(function (s) { return s[0] === a.status; }), ob2 = STATUS.findIndex(function (s) { return s[0] === b.status; });
      var fa = ["rejected", "dropped"].indexOf(a.status) >= 0, fb = ["rejected", "dropped"].indexOf(b.status) >= 0;
      if (fa !== fb) return fa ? 1 : -1;
      var da = daysLeft(a.deadline), db = daysLeft(b.deadline);
      if (da === null && db !== null) return 1; if (db === null && da !== null) return -1;
      return (da || 0) - (db || 0) || oa - ob2;
    });
    return '<div class="os-h os-ph"><div><h1>Arizalarim</h1><p class="os-muted">Har ariza — alohida paket: muddat, holat, hujjatlar roʻyxati.</p></div><button type="button" class="os-btn" id="appAdd">+ Ariza</button></div>' +
      '<div id="appForm"></div>' +
      (list.length ? '<div class="os-apps">' + list.map(function (a) {
        var k = appDocs(a), d = daysLeft(a.deadline), si = stInfo(a.status);
        return '<button type="button" class="os-app" data-app="' + a.id + '"><span class="os-st" style="--c:' + si[2] + '">' + si[1] + '</span>' +
          '<b>' + esc(a.name) + '</b><small>' + esc([a.kind === "grant" ? "Stipendiya" : "Universitet", a.program, a.country].filter(Boolean).join(" · ")) + '</small>' +
          '<span class="os-app-row"><span>' + (a.deadline ? (d >= 0 ? "⏳ " + d + " kun · " : "⌛ oʻtgan · ") + fmtD(a.deadline) : "Muddat kiritilmagan") + '</span><span>📎 ' + k.done + "/" + k.total + '</span></span>' +
          '<i class="os-bar"><i style="width:' + (k.total ? Math.round(k.done / k.total * 100) : 0) + '%"></i></i></button>';
      }).join("") + "</div>"
        : '<div class="os-empty"><div>📮</div><p>Bu yerda arizalaringiz turadi. Universitet yoki stipendiya qoʻshing: OS muddatni sanaydi va hujjatlar roʻyxatini tuzadi.</p><p class="os-muted">Muddat va talablarni faqat dasturning rasmiy sahifasidan oling.</p></div>');
  }
  function appForm(a) {
    var box = $("#appForm"); if (!box) return; a = a || {};
    box.innerHTML = '<form class="os-card os-form" id="appF"><h3>' + (a.id ? "Arizani tahrirlash" : "Yangi ariza") + '</h3>' +
      '<div class="os-seg">' + [["uni", "Universitet"], ["grant", "Stipendiya"]].map(function (k) { return '<label><input type="radio" name="kind" value="' + k[0] + '"' + ((a.kind || "uni") === k[0] ? " checked" : "") + '><span>' + k[1] + '</span></label>'; }).join("") + '</div>' +
      '<label class="os-field"><span>Nomi *</span><input name="name" required maxlength="90" value="' + esc(a.name || "") + '" data-suggest="uni" placeholder="masalan: University of Leeds yoki GKS"></label>' +
      '<div class="os-row2"><label class="os-field"><span>Dastur</span><input name="program" maxlength="90" value="' + esc(a.program || "") + '" data-suggest="prog" placeholder="MSc Data Science"></label>' +
      '<label class="os-field"><span>Davlat</span><input name="country" maxlength="40" value="' + esc(a.country || "") + '" data-suggest="country"></label></div>' +
      '<div class="os-row2"><label class="os-field"><span>Topshirish muddati</span><input type="date" name="deadline" value="' + esc(a.deadline || "") + '"></label>' +
      '<label class="os-field"><span>Holat</span><select name="status">' + STATUS.map(function (s) { return '<option value="' + s[0] + '"' + ((a.status || "idea") === s[0] ? " selected" : "") + ">" + s[1] + "</option>"; }).join("") + '</select></label></div>' +
      '<label class="os-field"><span>Rasmiy sahifa havolasi</span><input type="url" name="url" maxlength="300" value="' + esc(a.url || "") + '" placeholder="https://…"></label>' +
      '<div class="os-actions"><button class="os-btn" type="submit">Saqlash</button><button class="os-btn ghost" type="button" id="appCancel">Bekor qilish</button></div></form>';
    $("#appCancel").addEventListener("click", function () { box.innerHTML = ""; });
    $("#appF").addEventListener("submit", function (e) {
      e.preventDefault(); var f = e.target, nm = f.name.value.trim(); if (!nm) return;
      var o = a.id ? a : { id: uid(), created: Date.now(), docs: {}, note: "" };
      o.kind = f.kind.value; o.name = nm; o.program = f.program.value.trim(); o.country = f.country.value.trim();
      o.deadline = f.deadline.value; o.status = f.status.value; o.url = f.url.value.trim();
      if (!a.id) { DOCS.forEach(function (d) { o.docs[d[0]] = false; }); if (S.profile.level === "phd") o.docs.proposal = false; S.apps.push(o); }
      save(); snd("win"); toast(a.id ? "Saqlandi." : nm + " qoʻshildi. Hujjatlar roʻyxati tuzildi."); openApp = o.id; renderAll();
    });
    var first = box.querySelector("input[name=name]"); if (first) first.focus();
  }
  function vAppOne(a) {
    var k = appDocs(a), d = daysLeft(a.deadline), si = stInfo(a.status);
    var extra = DOCS_EXTRA.filter(function (x) { return !(x[0] in a.docs); });
    var linked = S.drafts.filter(function (dr) { return dr.app === a.id; });
    return '<button type="button" class="os-back" id="appBack">← Arizalarim</button>' +
      '<section class="os-card"><div class="os-h"><div><span class="os-st" style="--c:' + si[2] + '">' + si[1] + '</span><h1 class="os-t1">' + esc(a.name) + '</h1>' +
      '<p class="os-muted">' + esc([a.kind === "grant" ? "Stipendiya" : "Universitet", a.program, a.country].filter(Boolean).join(" · ")) + (a.url ? ' · <a href="' + esc(a.url) + '" target="_blank" rel="noopener">Rasmiy sahifa ↗</a>' : "") + '</p></div>' +
      '<button type="button" class="os-link" id="appEdit">Tahrirlash</button></div>' +
      '<div class="os-row2 os-kv"><div><span>Muddat</span><b>' + (a.deadline ? fmtD(a.deadline) : "—") + '</b><small>' + (d === null ? "Rasmiy sahifadan kiriting" : d >= 0 ? d + " kun qoldi" : "Muddat oʻtgan") + '</small></div>' +
      '<div><span>Holat</span><select id="appSt">' + STATUS.map(function (s) { return '<option value="' + s[0] + '"' + (a.status === s[0] ? " selected" : "") + ">" + s[1] + "</option>"; }).join("") + '</select></div></div></section>' +
      '<div id="appForm"></div>' +
      '<section class="os-card"><div class="os-h"><h3>Sizning ariza paketingiz</h3><span class="os-muted">' + k.done + " / " + k.total + ' tayyor</span></div><i class="os-bar big"><i style="width:' + (k.total ? Math.round(k.done / k.total * 100) : 0) + '%"></i></i>' +
      '<ul class="os-check">' + Object.keys(a.docs).map(function (key) {
        return '<li><label><input type="checkbox" data-doc="' + esc(key) + '"' + (a.docs[key] ? " checked" : "") + '><span>' + esc(docName(key)) + '</span></label><button type="button" class="os-x" data-deldoc="' + esc(key) + '" aria-label="Olib tashlash">×</button></li>';
      }).join("") + '</ul>' +
      '<div class="os-add"><select id="docAdd"><option value="">+ Hujjat qoʻshish…</option>' + extra.map(function (x) { return '<option value="' + x[0] + '">' + x[1] + "</option>"; }).join("") + '<option value="__c">Boshqa (oʻzim yozaman)</option></select></div>' +
      '<p class="os-muted os-sm">Roʻyxat umumiy. Aniq talablar dasturdan dasturga farq qiladi — rasmiy sahifadagi roʻyxat bilan solishtiring.</p></section>' +
      '<section class="os-card"><div class="os-h"><h3>Shu arizaga bogʻlangan hujjatlar</h3><button type="button" class="os-link" id="appNewDraft">+ Yangi hujjat</button></div>' +
      (linked.length ? '<ul class="os-mini">' + linked.map(function (dr) { return '<li><button type="button" data-go="ish-stoli" data-draft="' + dr.id + '"><b>' + esc(dr.title) + '</b><small>' + esc(dType(dr.type)[1]) + " · " + words(dr.text).length + ' soʻz</small></button></li>'; }).join("") + "</ul>" : '<p class="os-muted">Hali yoʻq. Motivatsion xat har dasturga alohida yoziladi.</p>') + '</section>' +
      '<section class="os-card"><h3>Eslatmalaringiz</h3><textarea id="appNote" class="os-note" rows="4" maxlength="3000" placeholder="Masalan: professor bilan yozishma, toʻlov, intervyu sanasi…">' + esc(a.note || "") + '</textarea></section>' +
      '<button type="button" class="os-del" id="appDel">Arizani oʻchirish</button>';
  }

  // ── 4K yoʻlim ─────────────────────────────────────────────
  function vRoad() {
    var st = stage();
    return '<div class="os-ph"><h1>4K yoʻlim</h1><p class="os-muted">Kirish → Ketish → Kampus → Karyera. Bosqichingizni tanlang va qadamlarni belgilang.</p></div>' +
      '<div class="os-4k">' + STAGES.map(function (s, i) {
        var p = roadPct(s.id), cur = s.id === st, past = STAGES.findIndex(function (x) { return x.id === st; }) > i;
        return '<button type="button" class="os-4k-s' + (cur ? " on" : "") + (past ? " past" : "") + '" data-stage="' + s.id + '"><span class="os-4k-ic">' + s.ic + '</span><b>' + s.n + '</b><small>' + p.d + "/" + p.t + '</small><i class="os-bar"><i style="width:' + p.p + '%"></i></i></button>';
      }).join("") + '</div>' +
      STAGES.map(function (s) {
        var open = s.id === st;
        return '<details class="os-card os-stg"' + (open ? " open" : "") + '><summary><span>' + s.ic + " " + s.n + '</span><small>' + s.s + '</small></summary><ul class="os-check">' +
          ROAD[s.id].map(function (x) {
            var link = x[2] ? (x[2].charAt(0) === "#" ? '<button type="button" class="os-tag" data-go="' + x[2].slice(1) + '">' + x[3] + " →</button>" : '<a class="os-tag" href="' + x[2] + '">' + x[3] + " ↗</a>") : "";
            return '<li><label><input type="checkbox" data-road="' + x[0] + '"' + (S.road[x[0]] ? " checked" : "") + '><span>' + esc(x[1]) + '</span></label>' + link + '</li>';
          }).join("") + '</ul>' + (open ? "" : '<button type="button" class="os-link" data-stage="' + s.id + '">Shu bosqichdaman</button>') + '</details>';
      }).join("") +
      '<p class="os-muted os-sm">Viza, sugʻurta va bitiruvdan keyingi qoidalar har mamlakatda boshqacha va tez oʻzgaradi. Faqat elchixona va universitetning rasmiy sahifasiga tayaning.</p>';
  }

  // ── Ish stoli ─────────────────────────────────────────────
  function vDesk() {
    if (openDraft) { var d = S.drafts.filter(function (x) { return x.id === openDraft; })[0]; if (d) return vEditor(d); openDraft = null; }
    var list = S.drafts.slice().sort(function (a, b) { return b.updated - a.updated; });
    return '<div class="os-h os-ph"><div><h1>Ish stoli</h1><p class="os-muted">Sizning hujjatlaringiz: yozing, versiyasini saqlang, tekshiring.</p></div></div>' +
      '<div class="os-types">' + DTYPES.map(function (t) { return '<button type="button" class="os-type" data-newdraft="' + t[0] + '">+ ' + esc(t[1]) + '</button>'; }).join("") + '</div>' +
      (list.length ? '<ul class="os-mini os-desk">' + list.map(function (d) {
        var app = S.apps.filter(function (a) { return a.id === d.app; })[0];
        return '<li><button type="button" data-draft="' + d.id + '"><b>' + esc(d.title) + '</b><small>' + esc(dType(d.type)[1]) + (app ? " · " + esc(app.name) : "") + " · " + words(d.text).length + " soʻz · " + ago(d.updated) + '</small></button></li>';
      }).join("") + "</ul>" : '<div class="os-empty"><div>✍</div><p>Hujjat turini tanlang. Andoza faqat qism nomlarini beradi — matnni oʻzingiz yozasiz. Komissiya tayyor shablonni tez taniydi.</p></div>');
  }
  function vEditor(d) {
    var t = dType(d.type), w = words(d.text).length;
    return '<button type="button" class="os-back" id="drBack">← Ish stoli</button>' +
      '<section class="os-card os-ed"><input class="os-ed-t" id="drTitle" value="' + esc(d.title) + '" maxlength="90" aria-label="Hujjat nomi">' +
      '<div class="os-ed-meta"><span>' + esc(t[1]) + '</span>' +
      '<label>Ariza: <select id="drApp"><option value="">—</option>' + S.apps.map(function (a) { return '<option value="' + a.id + '"' + (d.app === a.id ? " selected" : "") + ">" + esc(a.name) + "</option>"; }).join("") + '</select></label>' +
      '<label>Soʻz cheklovi: <input type="number" id="drLim" min="0" max="10000" step="50" value="' + (d.limit || "") + '" placeholder="yoʻq"></label></div>' +
      '<textarea id="drText" class="os-ed-x" lang="en" data-alifbo="off" spellcheck="true" placeholder="Shu yerga yozing…">' + esc(d.text) + '</textarea>' +
      '<div class="os-ed-bar"><span id="drCount">' + w + (d.limit ? " / " + d.limit : "") + ' soʻz</span>' +
      '<button type="button" class="os-btn sm" id="drCheck">🔍 Tekshirish</button><button type="button" class="os-btn sm ghost" id="drVer">Versiyani saqlash</button>' +
      '<button type="button" class="os-btn sm ghost" id="drCopy">Nusxa</button><button type="button" class="os-btn sm ghost" id="drDl">.txt</button></div></section>' +
      ((d.versions || []).length ? '<section class="os-card"><h3>Versiyalar</h3><ul class="os-mini">' + d.versions.slice().reverse().map(function (v, i) {
        var idx = d.versions.length - 1 - i;
        return '<li class="os-ver"><span><b>' + new Date(v.t).toLocaleString("uz-UZ", { day: "numeric", month: "short", hour: "2-digit", minute: "2-digit" }) + '</b><small>' + words(v.text).length + ' soʻz</small></span><button type="button" class="os-link" data-restore="' + idx + '">Tiklash</button></li>';
      }).join("") + '</ul></section>' : "") +
      '<button type="button" class="os-del" id="drDel">Hujjatni oʻchirish</button>';
  }
  function newDraft(type, appId) {
    var t = dType(type), app = S.apps.filter(function (a) { return a.id === appId; })[0];
    var d = { id: uid(), type: type, title: t[1] + (app ? " — " + app.name : ""), text: SKEL[type] || "", limit: t[2] || 0, app: appId || "", created: Date.now(), updated: Date.now(), versions: [] };
    S.drafts.push(d); save(); snd("pick"); return d;
  }

  // ── Tekshiruv ─────────────────────────────────────────────
  function vCheck() {
    var list = S.drafts.slice().sort(function (a, b) { return b.updated - a.updated; });
    if (!list.length) return '<div class="os-ph"><h1>Tekshiruv</h1></div><div class="os-empty"><div>🔍</div><p>Avval Ish stolida hujjat yozing. Keyin shu yerda ikki bosqichda tekshirasiz: avtomatik qoidalar va rubrika.</p><button type="button" class="os-btn" data-go="ish-stoli">Ish stoliga →</button></div>';
    var d = list.filter(function (x) { return x.id === checkDraft; })[0] || list[0]; checkDraft = d.id;
    var r = autoCheck(d.text, d.limit), rub = RUBRIC[d.type] || RUBRIC.other, ck = S.checks[d.id] || {};
    var max = rub.reduce(function (s, x) { return s + x[1]; }, 0), got = rub.reduce(function (s, x, i) { return s + (ck[i] ? x[1] : 0); }, 0);
    var autoOk = r.items.filter(function (x) { return x.ok; }).length;
    return '<div class="os-ph"><h1>Tekshiruv</h1><p class="os-muted">Hujjatingizni topshirishdan oldin koʻrib chiqing.</p></div>' +
      '<label class="os-field"><span>Hujjat</span><select id="ckSel">' + list.map(function (x) { return '<option value="' + x.id + '"' + (x.id === d.id ? " selected" : "") + ">" + esc(x.title) + "</option>"; }).join("") + '</select></label>' +
      '<section class="os-card"><div class="os-h"><h3>1. Avtomatik tekshiruv</h3><span class="os-muted">' + autoOk + " / " + r.items.length + '</span></div><ul class="os-auto">' +
      r.items.map(function (x) { return '<li class="' + (x.ok ? "ok" : "no") + '"><span>' + (x.ok ? "✓" : "!") + '</span>' + esc(x.t) + '</li>'; }).join("") + '</ul>' +
      '<p class="os-muted os-sm">Bu qoidalar asosidagi tekshiruv: soʻz soni, gap uzunligi, takror, shablon iboralar. Mazmunni baholamaydi.</p></section>' +
      '<section class="os-card"><div class="os-h"><h3>2. Rubrika: oʻzingiz baholang</h3><span class="os-score">' + got + " / " + max + '</span></div><i class="os-bar big"><i style="width:' + Math.round(got / max * 100) + '%"></i></i><ul class="os-check">' +
      rub.map(function (x, i) { return '<li><label><input type="checkbox" data-rub="' + i + '"' + (ck[i] ? " checked" : "") + '><span>' + esc(x[0]) + ' <small class="os-w">' + x[1] + ' ball</small></span></label></li>'; }).join("") + '</ul>' +
      '<p class="os-muted os-sm">Har bandni rostdan bajargandagina belgilang. Rubrika — oʻzingizni tekshirish uchun, kafolat emas.</p></section>' +
      '<section class="os-card os-soon"><h3>3. Fikr beruvchi (rejada)</h3><p class="os-muted">Matningizni rubrika boʻyicha savollar bilan koʻrib chiqadigan yordamchi. Matnni sizning oʻrningizga yozmaydi. Hozir: hujjatni ishonchli odamga — oʻqituvchi yoki u yerda oʻqiyotgan talabaga — koʻrsating.</p></section>' +
      '<button type="button" class="os-btn ghost" data-go="ish-stoli" data-draft="' + d.id + '">Hujjatni tahrirlash →</button>';
  }

  // ── Hodisalar ─────────────────────────────────────────────
  function bindView() {
    $$("[data-go]").forEach(function (b) {
      b.addEventListener("click", function (e) {
        e.preventDefault(); snd("nav");
        go(b.getAttribute("data-go"), { app: b.getAttribute("data-app") || (b.getAttribute("data-go") === "arizalar" ? null : undefined), draft: b.getAttribute("data-draft") || (b.getAttribute("data-go") === "ish-stoli" ? null : undefined), add: !!b.getAttribute("data-add") });
      });
    });
    var x;
    if ((x = $("#osSetup"))) x.addEventListener("click", function () { S.profile.stage = ""; renderAll(); });
    // Arizalar
    if ((x = $("#appAdd"))) x.addEventListener("click", function () { appForm(); });
    $$(".os-app[data-app]").forEach(function (b) { b.addEventListener("click", function () { snd("nav"); openApp = b.getAttribute("data-app"); renderAll(); window.scrollTo(0, 0); }); });
    var a = openApp && S.apps.filter(function (q) { return q.id === openApp; })[0];
    if (a && TAB === "arizalar") {
      $("#appBack").addEventListener("click", function () { openApp = null; renderAll(); });
      $("#appEdit").addEventListener("click", function () { appForm(a); });
      $("#appSt").addEventListener("change", function (e) { a.status = e.target.value; save(); if (a.status === "accepted") { snd("win"); celebrate(); } renderAll(); });
      $$("[data-doc]").forEach(function (c) { c.addEventListener("change", function () { a.docs[c.getAttribute("data-doc")] = c.checked; save(); snd(c.checked ? "xp" : "tab"); var k = appDocs(a); if (c.checked && k.done === k.total) { toast("Ariza paketingiz toʻliq tayyor."); snd("win"); } renderAll(); }); });
      $$("[data-deldoc]").forEach(function (c) { c.addEventListener("click", function () { delete a.docs[c.getAttribute("data-deldoc")]; save(); renderAll(); }); });
      $("#docAdd").addEventListener("change", function (e) {
        var v = e.target.value; if (!v) return;
        if (v === "__c") { var n = (prompt("Hujjat nomi:") || "").trim().slice(0, 60); if (!n) { e.target.value = ""; return; } v = "c_" + n; }
        a.docs[v] = false; save(); renderAll();
      });
      $("#appNote").addEventListener("input", function (e) { a.note = e.target.value; save(true); });
      $("#appNewDraft").addEventListener("click", function () { var d = newDraft("sop", a.id); go("ish-stoli", { draft: d.id }); });
      $("#appDel").addEventListener("click", function () { if (!confirm("«" + a.name + "» arizasi va uning roʻyxati oʻchiriladi. Bogʻlangan hujjatlar Ish stolida qoladi. Davom etasizmi?")) return; S.apps = S.apps.filter(function (q) { return q !== a; }); S.drafts.forEach(function (d) { if (d.app === a.id) d.app = ""; }); openApp = null; save(); renderAll(); });
    }
    // 4K
    $$("[data-stage]").forEach(function (b) { b.addEventListener("click", function (e) { e.preventDefault(); S.profile.stage = b.getAttribute("data-stage"); save(); snd("pick"); renderAll(); }); });
    $$("[data-road]").forEach(function (c) { c.addEventListener("change", function () { S.road[c.getAttribute("data-road")] = c.checked; if (!c.checked) delete S.road[c.getAttribute("data-road")]; save(); snd(c.checked ? "xp" : "tab"); var st = stage(), p = roadPct(st); if (c.checked && p.d === p.t) { toast("Bu bosqichning hamma qadami bajarildi."); snd("win"); } renderAll(); }); });
    // Ish stoli
    $$("[data-newdraft]").forEach(function (b) { b.addEventListener("click", function () { var d = newDraft(b.getAttribute("data-newdraft")); openDraft = d.id; renderAll(); }); });
    $$(".os-desk [data-draft]").forEach(function (b) { b.addEventListener("click", function () { snd("nav"); openDraft = b.getAttribute("data-draft"); renderAll(); window.scrollTo(0, 0); }); });
    var d = openDraft && S.drafts.filter(function (q) { return q.id === openDraft; })[0];
    if (d && TAB === "ish-stoli") bindEditor(d);
    // Tekshiruv
    if ((x = $("#ckSel"))) x.addEventListener("change", function (e) { checkDraft = e.target.value; renderAll(); });
    $$("[data-rub]").forEach(function (c) { c.addEventListener("change", function () { var m = S.checks[checkDraft] = S.checks[checkDraft] || {}; m[c.getAttribute("data-rub")] = c.checked; if (!c.checked) delete m[c.getAttribute("data-rub")]; save(); snd(c.checked ? "xp" : "tab"); renderAll(); }); });
  }
  function bindEditor(d) {
    var ta = $("#drText"), cnt = $("#drCount");
    function upd() { var w = words(ta.value).length; cnt.textContent = w + (d.limit ? " / " + d.limit : "") + " soʻz"; cnt.classList.toggle("over", !!d.limit && w > d.limit); }
    upd(); autosize(ta);
    ta.addEventListener("input", function () { d.text = ta.value; d.updated = Date.now(); upd(); autosize(ta); save(true); flash(); });
    $("#drTitle").addEventListener("input", function (e) { d.title = e.target.value.slice(0, 90) || dType(d.type)[1]; d.updated = Date.now(); save(true); });
    $("#drApp").addEventListener("change", function (e) { d.app = e.target.value; save(); });
    $("#drLim").addEventListener("input", function (e) { d.limit = Math.max(0, parseInt(e.target.value, 10) || 0); save(true); upd(); });
    $("#drBack").addEventListener("click", function () { openDraft = null; renderAll(); });
    $("#drVer").addEventListener("click", function () {
      d.versions = d.versions || []; var last = d.versions[d.versions.length - 1];
      if (last && last.text === d.text) { toast("Bu versiya allaqachon saqlangan."); return; }
      d.versions.push({ t: Date.now(), text: d.text }); d.versions = d.versions.slice(-10); save(); snd("xp"); toast("Versiya saqlandi (oxirgi 10 tasi turadi)."); renderAll();
    });
    $$("[data-restore]").forEach(function (b) { b.addEventListener("click", function () { var v = d.versions[+b.getAttribute("data-restore")]; if (!v || !confirm("Hozirgi matn shu versiya bilan almashtiriladi. Avval hozirgisini versiya qilib saqlang. Davom etasizmi?")) return; d.text = v.text; d.updated = Date.now(); save(); renderAll(); }); });
    $("#drCopy").addEventListener("click", function () { var done = function () { toast("Nusxalandi."); }; if (navigator.clipboard) navigator.clipboard.writeText(d.text).then(done, function () { ta.select(); document.execCommand("copy"); done(); }); else { ta.select(); document.execCommand("copy"); done(); } });
    $("#drDl").addEventListener("click", function () {
      var a = document.createElement("a"); a.href = URL.createObjectURL(new Blob([d.text], { type: "text/plain;charset=utf-8" }));
      a.download = (d.title || "hujjat").replace(/[^\wʻʼ\- ]+/g, "").trim().replace(/\s+/g, "_").slice(0, 60) + ".txt";
      document.body.appendChild(a); a.click(); a.remove(); setTimeout(function () { URL.revokeObjectURL(a.href); }, 2000);
    });
    $("#drCheck").addEventListener("click", function () { checkDraft = d.id; go("tekshiruv"); });
    $("#drDel").addEventListener("click", function () { if (!confirm("«" + d.title + "» butunlay oʻchiriladi, versiyalari bilan. Davom etasizmi?")) return; S.drafts = S.drafts.filter(function (q) { return q !== d; }); delete S.checks[d.id]; openDraft = null; save(); renderAll(); });
  }
  function autosize(t) { t.style.height = "auto"; t.style.height = Math.max(320, t.scrollHeight + 4) + "px"; }
  function celebrate() {
    toast("Tabriklaymiz! Qabul xati — katta qadam. Endi «Ketish» bosqichi.");
  }

  // ── Ishga tushirish ───────────────────────────────────────
  function boot() {
    var nav = $("#osTabs");
    nav.innerHTML = TABS.map(function (t) { return '<button type="button" class="os-tab" data-tab="' + t[0] + '"><span>' + t[2] + '</span><b>' + t[1] + '</b></button>'; }).join("");
    $$(".os-tab").forEach(function (b) { b.addEventListener("click", function () { snd("tab"); openApp = null; openDraft = null; go(b.getAttribute("data-tab")); }); });
    var h = (location.hash || "").slice(1); if (ALIAS[h]) TAB = ALIAS[h];
    window.addEventListener("storage", function (e) { if (e.key === KEY) { S = load(); renderAll(); } });
    setBadge(); renderAll();
    auth();
  }
  function auth() {
    var sb = window.supabase;
    if (!sb || !sb.auth) return;
    sb.auth.getSession().then(function (r) {
      var s = r && r.data && r.data.session;
      if (!s) {
        var to = "os.html" + location.hash;
        try { sessionStorage.setItem("returnTo", to); localStorage.setItem("kompas_return", JSON.stringify({ to: to, at: Date.now() })); } catch (e) {}
        location.href = "login.html"; return;
      }
      var u = s.user, md = u.user_metadata || {};
      if (!S.profile.name && md.first_name) { S.profile.name = md.first_name; try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {} if (TAB === "bugun") renderAll(); }
      Sync.start(u);
    }, function () {});
  }
  window.KompasOS = { state: function () { return S; }, autoCheck: autoCheck };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
