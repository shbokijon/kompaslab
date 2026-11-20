/* Admin → talaba oynasi → "Javoblar" (2026-11-19, asoschi).
 * Profil maydonlari va kompas_user_state dagi har bir modul holati: jarayon va javoblar.
 * Javoblar 2026-11-19 dan yoziladi (js/kompas-sync.js); undan oldingi yozuvlarda faqat jarayon bor.
 * Oʻqish RLS bilan: user_state_own_read → fn_is_admin(). */
(function () {
  "use strict";
  var LAB = { master: "Magistratura", bachelor: "Bakalavr", phd: "PhD", gks: "GKS", usa: "USA", daad: "DAAD", tt: "Tadbirkor Talaba", musofir: "Musofir", maktab: "Maktab", research: "Tadqiqot" };
  var SKIP = { xp: 1, done: 1, seen: 1, open: 1, lv: 1, v: 1 };
  // M0 v2 (Magistratura, Bakalavr, USA) savollari
  var LABELS = {
    ans: "Javoblar", start: "Boshlash vaqti", stage: "Hozir qayerda", early: "Erta muddat rejada", date: "Ariza muddati (oʻzi kiritgan)",
    deg: "Daraja", field: "Soha", fieldX: "Soha: hali bilmayman", ftype: "Magistratura turi", where: "Mamlakat", grades: "Baholar",
    docs: "Hujjatlar", cv: "CV", sop: "Maqsad bayonnomasi", ref: "Tavsiya xati", tr: "Baholar qaydnomasi", lang: "Ingliz tili sertifikati",
    ach: "Yutuqlar", ess: "Insho", route: "Yoʻl (USA)", test: "SAT yoki GRE", fund: "Pul", game: "Kuchli/zaif jumla oʻyini", task: "Bepul vazifa bajarildi", res: "Natija",
    avg: "Ball", low: "Eng zaif yoʻnalishlar (tartib raqami)", at: "Hisoblangan sana", notes: "Yozuvlar"
  };
  var VALS = {
    start: { "2027k": "2027 kuzi", "2028b": "2028 boshi", "2028k": "2028 kuzi", "2029k": "2029 kuzi", x: "Hali bilmayman" },
    stage: { sch: "Maktab, litsey yoki kollej", u12: "Universitet, 1–2 kurs", u34: "Universitet, 3–4 kurs", g0: "Bitirgan, tajriba 2 yildan kam", g2: "Bitirgan, 2+ yil tajriba", s9: "9-sinf", s10: "10-sinf", s11: "11-sinf", lic: "Litsey yoki kollej", grad: "Maktabni bitirgan", uni: "Universitetda" },
    early: { y: "Ha", n: "Yoʻq", b: "Bilmayman" },
    route: { bak: "Bakalavr", ugrad: "Global UGRAD", mag: "Magistratura", phd: "PhD", x: "Hali aniq emas" },
    deg: { bak: "Bakalavr", mag: "Magistratura", phd: "PhD", x: "Hali aniq emas" },
    ftype: { taught: "Oʻquv", research: "Tadqiqot", x: "Bilmayman" },
    grades: { a: "Aʼlo", y: "Yaxshi", o: "Oʻrta", x: "Aytishi qiyin" },
    fund: { full: "Oila toʻliq toʻlaydi", part: "Oila qisman + stipendiya", sch: "Faqat toʻliq stipendiya", x: "Ota-onasi bilan gaplashmagan", oila: "Oila yoki oʻz puli", uni: "Universitet stipendiyasi", davlat: "Davlat yoki xalqaro stipendiya", a40: "Yiliga 40 000 $ dan koʻp", a15: "Yiliga 15–40 ming $", a5: "Yiliga 5–15 ming $", a0: "Yiliga 5 000 $ dan kam" },
    doc: { 2: "Bor", 1: "Jarayonda", 0: "Yoʻq" },
    game: { k: "Kuchli", z: "Zaif", i: "Ishonchli", x: "Xavfli" }
  };
  var PROFILE = [["first_name", "Ism"], ["last_name", "Familiya"], ["email", "Email"], ["phone", "Telefon"], ["education", "Taʼlim"], ["goal", "Maqsad"],
    ["stage", "Bosqich (kabinet savoli)"], ["stage_detail", "Bosqich tafsiloti"], ["works", "Ishlaydimi"], ["onboarded_at", "Kabinet savoliga javob bergan"], ["created_at", "Roʻyxatdan oʻtgan"]];

  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", "\"": "&quot;" }[c]; }); }
  function day(iso) { return iso ? String(iso).slice(0, 10).split("-").reverse().join(".") : ""; }
  function title(key) {
    var m = /^kompas_([a-z]+)_m([0-9a-z]+)_v1$/.exec(key);
    if (!m) return key;
    return (LAB[m[1]] || m[1]) + " · M" + m[2].toUpperCase();
  }
  function val(path, k, v) {
    var parent = path[path.length - 1];
    if (parent === "docs" && VALS.doc[v] != null) return VALS.doc[v];
    if (parent === "game" && VALS.game[v]) return VALS.game[v];
    if (VALS[k] && VALS[k][v] != null) return VALS[k][v];
    if (v === true) return "ha";
    if (v === false) return "yoʻq";
    return v;
  }
  function rows(obj, path, out) {
    Object.keys(obj || {}).forEach(function (k) {
      if (!path.length && SKIP[k]) return;
      var v = obj[k], label = path[path.length - 1] === "game" ? (+k + 1) + "-jumla" : (LABELS[k] || k), p = path.concat(k);
      if (v == null || v === "" || (Array.isArray(v) && !v.length)) return;
      if (Array.isArray(v) && v.every(function (x) { return typeof x !== "object"; })) {
        out.push([p, label, v.map(function (x) { return val(path, k, x); }).join(", ")]);
      } else if (typeof v === "object") {
        if (p.length > 4) { out.push([p, label, JSON.stringify(v)]); return; }
        var sub = []; rows(v, p, sub);
        if (sub.length) { out.push([p, label, null]); sub.forEach(function (r) { out.push(r); }); }
      } else {
        out.push([p, label, val(path, k, v)]);
      }
    });
    return out;
  }
  function table(list) {
    return '<div style="display:grid;grid-template-columns:minmax(120px,38%) 1fr;gap:4px 12px;font-size:13px">' + list.map(function (r) {
      var pad = "padding-left:" + Math.max(0, r[0].length - 1) * 12 + "px";
      if (r[2] === null) return '<div style="grid-column:1/-1;font-weight:700;margin-top:6px;' + pad + '">' + esc(r[1]) + "</div>";
      return '<div style="color:var(--muted);' + pad + '">' + esc(r[1]) + '</div><div style="white-space:pre-wrap;word-break:break-word">' + esc(r[2]) + "</div>";
    }).join("") + "</div>";
  }

  async function render(userId, profile, el) {
    if (!el || !userId) return;
    el.innerHTML = '<div class="sd-empty">Yuklanmoqda…</div>';
    var p = profile || {};
    var h = '<div class="sd-h">Profil</div>' + table(PROFILE.filter(function (f) { return p[f[0]] != null && p[f[0]] !== ""; }).map(function (f) {
      var v = p[f[0]]; if (/_at$/.test(f[0])) v = day(v); if (v === true) v = "ha"; if (v === false) v = "yoʻq";
      return [[f[0]], f[1], v];
    }));
    var res = await supabase.from("kompas_user_state").select("key, value, updated_at").eq("user_id", userId).order("updated_at", { ascending: false });
    if (res.error) { el.innerHTML = h + '<div class="sd-empty">Xatolik: ' + esc(res.error.message) + "</div>"; return; }
    var data = (res.data || []).filter(function (r) { return !/^kompas_sync_/.test(r.key); });
    h += '<div class="sd-h">Modullar</div>';
    if (!data.length) h += '<div class="sd-empty">Hali hech qaysi modul ochilmagan.</div>';
    data.forEach(function (r) {
      var v = r.value || {}, done = Object.keys(v.done || {}).filter(function (k) { return v.done[k]; }).length;
      var list = rows(v, [], []);
      h += '<details style="border:1px solid var(--border);border-radius:10px;padding:8px 12px" ' + (list.length ? "open" : "") + '><summary style="cursor:pointer;font-weight:700">' + esc(title(r.key)) +
        ' <span style="font-weight:400;color:var(--muted);font-size:12px">· jarayon ' + (+v.xp || 0) + " XP, " + done + " ta qadam yoki dars · " + esc(day(r.updated_at)) + "</span></summary>" +
        (list.length ? table(list) : '<div class="sd-empty">Javoblar yoʻq: bu yozuv 19.11.2026 dan oldin saqlangan, talaba modulga qayta kirganda yoziladi.</div>') + "</details>";
    });
    el.innerHTML = h;
  }
  window.KAnswers = { render: render };
})();
