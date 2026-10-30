/* Kompas Atlas: rasmiy registr nusxasidan qidiruv (NL, CA va keyingilari).
   Sozlama sahifadagi <script type="application/json" id="atlas-cfg"> da.
   Maʼlumot faqat oʻqiladi; hech narsa serverga yuborilmaydi. */
(function () {
  "use strict";
  var cfgEl = document.getElementById("atlas-cfg");
  if (!cfgEl) return;
  var cfg = JSON.parse(cfgEl.textContent);
  var PAGE = 30;
  var $ = function (id) { return document.getElementById(id); };
  var q = $("arQ"), f = $("arF"), list = $("arList"), stat = $("arStat"), more = $("arMore"), count = $("arCount");
  var rows = [], hits = [], shown = 0, data = null;

  function norm(s) { return String(s || "").toLowerCase().normalize("NFKD").replace(/[̀-ͯ]/g, ""); }
  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }

  function card(r) {
    var c = el("article", "ar-card");
    var h = el("h3", null, r[0]);
    h.setAttribute("lang", cfg.lang || "en");
    c.appendChild(h);
    var meta = el("p", "ar-meta");
    meta.setAttribute("lang", cfg.lang || "en");
    if (cfg.kind === "nl") {
      meta.textContent = "KvK: " + r[1];
    } else if (cfg.kind === "ca") {
      meta.textContent = [r[2], r[1]].filter(Boolean).join(" · ");
      var occ = el("p", "ar-occ", r[3] || "");
      occ.setAttribute("lang", "en");
      c.appendChild(meta);
      c.appendChild(occ);
      var tags = el("div", "ar-tags");
      if (r[4]) { var t = el("span", null, r[4]); t.setAttribute("lang", "en"); tags.appendChild(t); }
      if (r[5]) tags.appendChild(el("span", null, "Tasdiqlangan oʻrinlar: " + r[5]));
      c.appendChild(tags);
      return c;
    }
    c.appendChild(meta);
    return c;
  }

  function render(reset) {
    if (reset) { list.textContent = ""; shown = 0; }
    var end = Math.min(hits.length, shown + PAGE);
    for (var i = shown; i < end; i++) list.appendChild(card(hits[i]));
    shown = end;
    more.hidden = shown >= hits.length;
    count.textContent = hits.length ? (hits.length.toLocaleString("en-US").replace(/,/g, " ") + " ta yozuv") : "";
    if (!hits.length) {
      var e = el("div", "ar-empty");
      e.appendChild(el("b", null, "Mos yozuv topilmadi"));
      e.appendChild(el("p", null, "Nomni boshqacha yozib koʻring (masalan, B.V., Inc. yoki Ltd qismisiz). Roʻyxatda yoʻqligi ham yakuniy xulosa emas: rasmiy registrning oʻzida tekshiring."));
      list.appendChild(e);
    }
  }

  function search() {
    var term = norm(q.value.trim());
    var fv = f ? f.value : "";
    hits = rows.filter(function (r) {
      if (fv && r[1] !== fv) return false;
      return !term || r._n.indexOf(term) !== -1;
    });
    render(true);
  }

  var timer;
  q.addEventListener("input", function () { clearTimeout(timer); timer = setTimeout(search, 160); });
  if (f) f.addEventListener("change", search);
  more.addEventListener("click", function () { render(false); });

  fetch(cfg.data, { cache: "no-cache" }).then(function (r) {
    if (!r.ok) throw new Error(r.status);
    return r.json();
  }).then(function (d) {
    data = d;
    rows = d.rows || [];
    rows.forEach(function (r) { r._n = norm(r[0] + " " + (cfg.kind === "ca" ? (r[2] + " " + r[3]) : r[1])); });
    if (f && d.provinces) {
      d.provinces.forEach(function (p) { var o = el("option", null, p); o.value = p; o.setAttribute("lang", "en"); f.appendChild(o); });
    }
    var parts = [d.count.toLocaleString("en-US").replace(/,/g, " ") + " ta yozuv"];
    if (d.period) parts.push("davr: " + d.period);
    if (d.last_updated) parts.push("registr sanasi: " + d.last_updated);
    parts.push("Kompas yuklab olgan: " + d.retrieved_at);
    stat.textContent = parts.join(" · ");
    stat.className = "ar-stat ok";
    q.disabled = false; if (f) f.disabled = false;
    search();
  }).catch(function () {
    stat.textContent = "Kompas nusxasi hali tayyor emas yoki yuklanmadi. Rasmiy registrdan bevosita foydalaning (havola yuqorida).";
    stat.className = "ar-stat warn";
    more.hidden = true;
  });
})();
