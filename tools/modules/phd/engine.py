# ═══════════════════════════════════════════════════════════════
#  PhD Lab pullik modullari (M1–M8) manbasini yaratish (2026-11-07)
#  Qobiq va JS: Amerika Lab engine nusxasi (GKS/Bachelor andozasi).
#  Fazalar (oylik obunada 1 toʻlov = 1 faza = 2 modul): I M1–M2, II M3–M4, III M5–M6, IV M7–M8.
#
#  python3 tools/modules/phd/engine.py          # hammasi
#  python3 tools/modules/phd/engine.py 3 7      # tanlanganlar
#
#  Kontent: tools/modules/phd/mods/m<N>.py (MOD lugʻati). Matnda oddiy apostrof (')
#  yoziladi: o'/g' → U+02BB, qolgani → U+02BC (fix()). [[...]] → <span lang="en">.
#  Manbalar faqat universitet va masʼul tashkilotlar sahifalari (phd/common.py).
#  Asl kontent: "PhD Lab v0.9 content prototype" (2026-10-31), sayt andozasiga oʻtkazilgan.
# ═══════════════════════════════════════════════════════════════
import importlib.util, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE.parent / "src"

SLUGS = [str(i) for i in range(1, 9)]
PHASE = {}
for _n in range(1, 9):
    PHASE[_n] = ["Faza I · Yoʻnalish va tanlov", "Faza II · Rahbar va taklif", "Faza III · Hujjatlar va moliya", "Faza IV · Ariza va oʻtish"][(_n - 1) // 2]


def code_of(slug):
    return str(slug)


def strip_tracks(html, keep):
    """Trek modulida boshqa treklarga tegishli <h4> boʻlimlari va <li> bandlarini olib tashlaydi."""
    pill = re.compile(r'(?:<span class="trk">([UMD])</span>\s*)+')
    def tracks(m):
        return set(re.findall(r'<span class="trk">([UMD])</span>', m.group(0)))
    # 1) <li> bandlari
    def li(m):
        body = m.group(1)
        pm = pill.match(body)
        if pm and keep not in tracks(pm):
            return ""
        return "<li>" + (body[pm.end():] if pm else body) + "</li>"
    html = re.sub(r"<li>(.*?)</li>", li, html, flags=re.S)
    # 2) <h4> boʻlimlari: keyingi <h4>, box yoki srcs gacha
    parts = re.split(r"(?=<h4>)", html)
    out = []
    for part in parts:
        hm = re.match(r"<h4>\s*((?:<span class=\"trk\">[UMD]</span>\s*)+)", part)
        if hm:
            ts = set(re.findall(r"[UMD]", re.sub(r"<[^>]+>", "", hm.group(1))))
            if keep not in ts:
                cut = re.search(r'<div class="(box|srcs)', part)
                part = part[cut.start():] if cut else ""
            else:
                part = part.replace(hm.group(1), "", 1)
        out.append(part)
    html = "".join(out)
    # 3) qolgan pill: oʻz treki boʻlsa olib tashlanadi, boshqa trek boʻlsa ham (matn umumiy qoladi)
    return re.sub(r'<span class="trk">[UMD]</span>\s*', "", html)


def fix(s):
    """Oʻzbek apostrofi: o'/g' → ʻ, qolgan ' → ʼ; [[x]] → inglizcha span."""
    s = re.sub(r"\[\[(.+?)\]\]", r'<span lang="en">\1</span>', s)
    s = re.sub(r"([oOgG])'", lambda m: m.group(1) + "ʻ", s)
    return s.replace("'", "ʼ")


def img(n, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<img{c} src="img/3d/{n}.webp" width="160" height="160" alt="" loading="lazy">'


TABS = '<div class="tabs" role="tablist"><button class="tab" role="tab">Diqqat 🔥<i class="seen"></i></button><button class="tab" role="tab">Asosiy qism<i class="seen"></i></button><button class="tab" role="tab">Xulosa<i class="seen"></i></button><button class="tab" role="tab">Topshiriq<i class="seen"></i></button></div>'


def quiz_html(q):
    items = "".join(
        f'<div class="qz" data-a="{a}"><p>“{fix(t)}”</p><div class="row"><button type="button" data-v="t">✓ Toʻgʻri</button><button type="button" data-v="n">✗ Notoʻgʻri</button></div><div class="why">{fix(w)}</div></div>'
        for t, a, w in q)
    return f'<b>Mini-test: toʻgʻri yoki notoʻgʻri?</b><div class="quiz" id="quiz">{items}</div><div class="verdict" id="quizRes"></div>'


def lesson_html(n, k, L, lxp):
    lid = f"l{k}"
    num = f"{n}.{k}"
    tags = f'<span class="tag">⏱ {L["min"]} daqiqa</span><span class="tag">{fix(L["kind"])}</span><span class="tag xp">+{lxp} XP{" · test +30 XP" if L.get("quiz") else ""}</span>'
    task = fix(L["task"])
    if L.get("quiz"):
        task = quiz_html(L["quiz"]) + '<div style="margin-top:14px">' + task + "</div>"
    else:
        task = "<b>Topshiriq</b>" + task
    ta = f'<textarea data-save="a{k}" placeholder="{fix(L["ph"])}"></textarea>' if L.get("ph") else ""
    return f'''      <!-- {num} -->
      <article class="lesson" id="{lid}">
        <button class="l-head" type="button" aria-expanded="false">
          <span class="l-ic">{img(L["ic"])}<span class="ok">✓</span></span>
          <span><span class="l-n">Dars {num}</span><span class="l-t" style="display:block">{fix(L["t"])}</span>
            <span class="l-m">{tags}</span></span>
          <span class="chev">▾</span>
        </button>
        <div class="l-body">
          {TABS}
          <div class="panel"><div class="hook">{fix(L["hook"])}</div></div>
          <div class="panel">
{fix(L["body"])}
          </div>
          <div class="panel"><div class="take">{img(L["ic"])}<p>{fix(L["take"])}</p></div></div>
          <div class="panel"><div class="assign">{task}
            {ta}</div></div>
          <div class="l-foot"><span class="hint" data-hint></span><button class="btn btn-p" type="button" data-complete="{lid}">Darsni yakunlash · +{lxp} XP</button></div>
        </div>
      </article>'''


def field_html(f):
    key, label = f["k"], fix(f["label"])
    small = f' <small>{fix(f["hint"])}</small>' if f.get("hint") else ""
    ph = fix(f.get("ph", ""))
    if f.get("type") == "area":
        wc = f' data-wc="{f["wc"]}"' if f.get("wc") else ""
        meter = '<div class="meterw" data-meter="' + key + '"></div>' if f.get("wc") else ""
        return f'<div class="fld"><label for="f_{key}">{label}{small}</label><textarea id="f_{key}" data-save="{key}"{wc} placeholder="{ph}"></textarea>{meter}</div>'
    if f.get("type") == "select":
        opts = "".join(f'<option value="{fix(o)}">{fix(o)}</option>' for o in f["opts"])
        return f'<div class="fld"><label for="f_{key}">{label}{small}</label><select id="f_{key}" data-save="{key}"><option value="">— tanlang —</option>{opts}</select></div>'
    typ = f.get("type", "text")
    return f'<div class="fld"><label for="f_{key}">{label}{small}</label><input id="f_{key}" type="{typ}" data-save="{key}" placeholder="{ph}"></div>'


def tool_html(T):
    return f'''  <section id="{T["id"]}">
    <h2>{fix(T["h2"])}</h2>
    <p class="sub">{fix(T["sub"])}</p>
    <div class="tool">
      <div class="tool-h">{img(T["ic"])}<div><h3>{fix(T["h3"])}</h3><span>{fix(T["tag"])} · +30 XP</span></div></div>
      {fix(T.get("pre", ""))}
      {"".join(field_html(f) for f in T["fields"])}
      <div id="toolOut" class="out" hidden></div>
      <button class="btn btn-p" type="button" id="toolBtn" data-min="{T["min"]}" style="margin-top:14px">{fix(T["btn"])} · +30 XP</button>
    </div>
  </section>'''


def check_html(C):
    items = "".join(f'<label class="ck" data-ck="c{i + 1}"><input type="checkbox"><span>{fix(t)}</span></label>' for i, t in enumerate(C["items"]))
    return f'''  <section id="check">
    <h2>{fix(C["h2"])}</h2>
    <p class="sub">{fix(C["sub"])}</p>
    <div class="tool">
      <div class="tool-h">{img("shield")}<div><h3>{fix(C["h3"])}</h3><span>{len(C["items"])} band · +30 XP</span></div></div>
      <div class="cklist">{items}</div>
      <button class="btn btn-p" type="button" id="ckBtn" style="margin-top:14px">Roʻyxat yakunlandi · +30 XP</button>
    </div>
  </section>'''


EXTRA_CSS = """/* PhD M1–M8 qoʻshimchalari */
.path.pn{grid-template-columns:repeat(var(--pn),minmax(0,1fr));}
@media(max-width:760px){.path.pn{grid-template-columns:repeat(4,minmax(0,1fr));}.path.pn .node::after{display:none;}}
.fld{margin-bottom:12px;}
.fld label{display:block;font-size:14px;font-weight:700;margin-bottom:6px;}
.fld label small{font-weight:500;color:var(--muted);}
.fld input,.fld select{width:100%;min-height:46px;padding:10px 12px;border:2px solid var(--border);border-radius:12px;font-family:inherit;font-size:16px;background:var(--bg);color:var(--text);}
.fld textarea{margin-top:0;}
.fld input:focus,.fld select:focus,textarea:focus{outline:none;border-color:var(--accent);background:#fff;}
.srcs{font-size:12.5px;color:var(--muted);margin-top:10px;}
.srcs a{color:#1f5fa8;}
.pill{font-size:12px;font-weight:800;padding:2px 9px;border-radius:99px;display:inline-block;}
.pill.ok{background:var(--green-lit);color:var(--green);} .pill.no{background:var(--red-lit);color:var(--red);} .pill.chk{background:var(--gold-lit);color:var(--gold);}
.meterw{margin-top:6px;}
.meterw .mt{display:flex;justify-content:space-between;font-size:13px;font-weight:700;color:var(--muted);}
.meterw .mb{height:8px;border-radius:99px;background:var(--border);overflow:hidden;margin-top:4px;}
.meterw .mb i{display:block;height:100%;background:var(--accent);transition:width .3s;}
.meterw.ok .mb i{background:var(--green);} .meterw.over .mb i{background:var(--red);}
.out{background:var(--bg);border:1px solid var(--border);border-radius:14px;padding:14px 16px;margin-top:12px;font-size:14.5px;white-space:pre-wrap;word-break:break-word;}
.cklist{display:grid;gap:8px;margin-top:12px;}
.trk{display:inline-block;font-size:11.5px;font-weight:900;padding:1px 8px;border-radius:99px;background:var(--accent-lit);color:var(--accent);margin-right:4px;}
.artifact{background:var(--surface);border:2px solid var(--accent);border-radius:20px;padding:22px;}
.artifact .row{display:flex;gap:10px;flex-wrap:wrap;margin-top:16px;}
.paper{background:#fff;color:#111;font-family:Georgia,"Times New Roman",serif;font-size:14.5px;line-height:1.5;padding:28px 30px;border:1px solid var(--border);border-radius:8px;}
.paper h1{font-family:Georgia,serif;font-size:22px;color:#111;margin:0 0 4px;}
.paper .ct{font-size:13px;color:#555;margin-bottom:12px;}
.paper h4{font-family:Georgia,serif;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:#111;border-bottom:1px solid #111;margin:16px 0 6px;padding-bottom:2px;}
.paper p{margin:0 0 6px;white-space:pre-wrap;}
.paper .ph{color:#999;font-style:italic;}
@media(max-width:760px){.paper{padding:18px 16px;font-size:13.5px;}.artifact{padding:16px;}.artifact .row .btn{flex:1 1 100%;}}
@media print{
  .top,.hero,.map,section:not(#artefakt),footer,.toast,.artifact .row,.noprint{display:none!important;}
  body{background:#fff;} .artifact{border:none;padding:0;} .paper{border:none;padding:0;font-size:11pt;}
}"""


JS = r"""<script>
(function () {
  var KEY = "%KEY%", MOD = %N%, LXP = %LXP%, NL = %NL%, FINXP = %FINXP%;
  var ART = %ART%;
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var S = { xp: 0, done: {}, seen: {}, notes: {}, quiz: {}, ck: {}, open: "l1" };
  try { var raw = localStorage.getItem(KEY); if (raw) { var o = JSON.parse(raw); for (var k in o) S[k] = o[k]; } } catch (e) {}
  function save() { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {} }
  function $(id) { return document.getElementById(id); }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  var ICON = {}; document.querySelectorAll("[data-icon]").forEach(function (i) { ICON[i.getAttribute("data-icon")] = i.src; });
  function icon(n) { return ICON[n] || ("img/3d/" + n + ".webp"); }
  function nv(k) { return String(S.notes[k] || "").trim(); }
  function wc(s) { s = String(s || "").trim(); return s ? s.split(/\s+/).length : 0; }
  function copyText(txt) { if (navigator.clipboard) navigator.clipboard.writeText(txt).then(function () { toast("Nusxalandi", "memo"); }, function () { prompt("Nusxalang:", txt); }); else prompt("Nusxalang:", txt); }
  function download(name, type, data) { var blob = new Blob([data], { type: type }); var a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = name; document.body.appendChild(a); a.click(); setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500); }
  window.KG = { S: S, save: save, nv: nv, esc: esc, toast: function (m, i) { toast(m, i); } };

  var MAX = 250, LEVELS = [[0, "1-daraja: Kuzatuvchi"], [80, "2-daraja: Izlanuvchi"], [170, "3-daraja: Kashfiyotchi"], [250, "Modul yakunlandi"]];
  function renderXp(bump) {
    $("xpN").textContent = S.xp; $("xpBar").style.width = Math.min(100, S.xp / MAX * 100) + "%";
    var l = LEVELS[0][1]; LEVELS.forEach(function (x) { if (S.xp >= x[0]) l = x[1]; }); $("lvl").textContent = l;
    if (bump) { var p = $("xpPill"); p.classList.remove("pop"); void p.offsetWidth; p.classList.add("pop"); }
  }
  var tt;
  function toast(msg, img) { if (window.KSfx && img === "lock") KSfx.play("warn"); $("toastT").textContent = msg; $("toastImg").src = icon(img || "bulb"); var t = $("toast"); t.classList.add("show"); clearTimeout(tt); tt = setTimeout(function () { t.classList.remove("show"); }, 2600); }
  function confetti() {
    if (window.KSfx) KSfx.play("win");
    if (reduce) return;
    var colors = ["#c4622d", "#2d4a3e", "#d9a441", "#1a7a4a", "#7a3cc4"];
    for (var i = 0; i < 46; i++) { var c = document.createElement("i"); c.className = "cf"; c.style.left = Math.random() * 100 + "vw"; c.style.background = colors[i % colors.length]; c.style.animationDuration = (1.6 + Math.random() * 1.6) + "s"; document.body.appendChild(c); setTimeout(function (el) { el.remove(); }.bind(null, c), 3600); }
  }
  function award(id, xp, msg, img) {
    if (S.done[id]) return false;
    S.done[id] = true; var x0 = S.xp; S.xp = Math.min(MAX, S.xp + xp); if (window.KSfx) KSfx.gain(x0, S.xp);
    var nd = 0; for (var i = 1; i <= NL; i++) if (S.done["l" + i]) nd++;
    if (nd >= Math.ceil(NL / 2)) S.done.half = true;
    if (nd >= NL) S.done.all = true;
    save(); renderXp(true); renderAll();
    toast((xp ? "+" + xp + " XP · " : "") + msg, img);
    if (S.xp >= MAX) setTimeout(function () { confetti(); toast("Tabriklaymiz! M" + MOD + " yakunlandi", "seedling"); }, 900);
    return true;
  }

  var lessons = document.querySelectorAll(".lesson");
  function openLesson(id, scroll) {
    lessons.forEach(function (l) { var on = l.id === id && !l.classList.contains("open"); l.classList.toggle("open", on); l.querySelector(".l-head").setAttribute("aria-expanded", on ? "true" : "false"); });
    S.open = id; save();
    var el = $(id); if (scroll && el && el.classList.contains("open")) el.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
  }
  function renderLesson(l) {
    var id = l.id, seen = S.seen[id] || [];
    l.querySelectorAll(".tab").forEach(function (t, i) { t.classList.toggle("v", seen.indexOf(i) >= 0); });
    l.classList.toggle("done", !!S.done[id]);
    var b = l.querySelector("[data-complete]"), h = l.querySelector("[data-hint]");
    if (S.done[id]) { b.disabled = true; b.textContent = "✓ Yakunlangan"; h.textContent = "Keyingi darsga oʻting."; }
    else h.textContent = seen.length < 4 ? "Oʻqilgan qismlar: " + seen.length + " / 4" : "Hammasi oʻqildi. Darsni yakunlang.";
  }
  lessons.forEach(function (l) {
    var id = l.id, tabs = l.querySelectorAll(".tab"), panels = l.querySelectorAll(".panel");
    S.seen[id] = S.seen[id] || [];
    function show(i, mark) {
      tabs.forEach(function (t, j) { t.setAttribute("aria-selected", j === i ? "true" : "false"); });
      panels.forEach(function (p, j) { p.classList.toggle("on", j === i); });
      if (mark && S.seen[id].indexOf(i) < 0) { S.seen[id].push(i); save(); }
      renderLesson(l);
    }
    tabs.forEach(function (t, i) { t.addEventListener("click", function () { show(i, true); }); });
    l.querySelector(".l-head").addEventListener("click", function () { openLesson(id, true); if (l.classList.contains("open") && S.seen[id].indexOf(0) < 0) { S.seen[id].push(0); save(); renderLesson(l); } });
    show(0, false);
  });
  document.querySelectorAll("[data-complete]").forEach(function (b) {
    b.addEventListener("click", function () {
      var id = b.getAttribute("data-complete");
      if ((S.seen[id] || []).length < 4) { toast("Avval toʻrt qismni ham oching", "lock"); return; }
      var n = +id.slice(1);
      award(id, LXP, "Dars " + parseInt(MOD, 10) + "." + n + " yakunlandi", "seedling");
      var next = $("l" + (n + 1));
      setTimeout(function () { if (next) openLesson(next.id, true); else { var t = document.querySelector("section[id]:not(#darslar)"); if (t) t.scrollIntoView({ behavior: reduce ? "auto" : "smooth" }); } }, 700);
    });
  });
  if (S.open && $(S.open)) openLesson(S.open, false);
  if (S.seen[S.open] && S.seen[S.open].indexOf(0) < 0) { S.seen[S.open].push(0); save(); }

  function meterFor(t) {
    var r = t.getAttribute("data-wc"); if (!r) return;
    var el = document.querySelector('[data-meter="' + t.getAttribute("data-save") + '"]'); if (!el) return;
    var lo = +r.split("-")[0], hi = +r.split("-")[1], n = wc(t.value), pct = Math.min(100, n / hi * 100);
    el.className = "meterw" + (n > hi ? " over" : n >= lo ? " ok" : "");
    el.innerHTML = '<div class="mt"><span>' + n + " soʻz</span><span>moʻljal: " + lo + "–" + hi + '</span></div><div class="mb"><i style="width:' + pct + '%"></i></div>';
  }
  document.querySelectorAll("[data-save]").forEach(function (t) {
    var k = t.getAttribute("data-save"); if (S.notes[k] != null) t.value = S.notes[k];
    meterFor(t);
    var tm; t.addEventListener("input", function () { meterFor(t); clearTimeout(tm); tm = setTimeout(function () { S.notes[k] = t.value; save(); renderArt(); }, 350); });
    t.addEventListener("change", function () { S.notes[k] = t.value; save(); renderArt(); });
  });
  document.querySelectorAll("[data-ck]").forEach(function (c) {
    var k = c.getAttribute("data-ck"), inp = c.querySelector("input");
    inp.checked = !!S.ck[k]; c.classList.toggle("on", inp.checked);
    inp.addEventListener("change", function () { S.ck[k] = inp.checked; c.classList.toggle("on", inp.checked); save(); renderArt(); });
  });

  var qz = document.querySelectorAll("#quiz .qz");
  function renderQuiz() {
    var answered = 0, right = 0;
    qz.forEach(function (q, i) {
      var a = S.quiz[i]; if (a == null) return; answered++; if (a === q.getAttribute("data-a")) right++;
      q.classList.add("ans");
      q.querySelectorAll("button").forEach(function (b) { var v = b.getAttribute("data-v"); b.classList.toggle("right", v === q.getAttribute("data-a")); b.classList.toggle("wrong", v === a && v !== q.getAttribute("data-a")); });
    });
    var r = $("quizRes");
    if (r && qz.length && answered === qz.length) { r.className = "verdict show box " + (right >= 3 ? "info" : "warn"); r.textContent = "Natija: " + right + " / " + qz.length + ". " + (right >= 3 ? "Asosiy qoidalarni bilasiz." : "Asosiy qismni yana bir koʻrib chiqing."); }
    return { answered: answered, right: right };
  }
  qz.forEach(function (q, i) {
    q.querySelectorAll("button").forEach(function (b) {
      b.addEventListener("click", function () {
        if (S.quiz[i] != null) return; S.quiz[i] = b.getAttribute("data-v"); save();
        var r = renderQuiz();
        if (r.answered === qz.length) { if (r.right >= 3) S.done.quizOk = true; award("quiz", 30, "Mini-test: " + r.right + "/" + qz.length, "books"); }
      });
    });
  });

  var tb = $("toolBtn");
  if (tb) tb.addEventListener("click", function () {
    var need = +tb.getAttribute("data-min"), keys = [], filled = 0;
    tb.parentNode.querySelectorAll("[data-save]").forEach(function (t) { keys.push(t.getAttribute("data-save")); if (nv(t.getAttribute("data-save"))) filled++; });
    if (filled < need) { toast("Kamida " + need + " ta maydonni toʻldiring (" + filled + " / " + keys.length + ")", "lock"); return; }
    if (window.KGTool && window.KGTool.check) { var msg = window.KGTool.check(); if (msg) { toast(msg, "lock"); return; } }
    award("tool", 30, "Vosita natijasi saqlandi", "memo");
  });
  var cb = $("ckBtn");
  if (cb) cb.addEventListener("click", function () {
    var all = document.querySelectorAll("#check [data-ck]"), on = 0;
    all.forEach(function (c) { if (S.ck[c.getAttribute("data-ck")]) on++; });
    if (on < all.length) { toast("Hali " + (all.length - on) + " ta band belgilanmagan", "lock"); return; }
    award("ck", 30, "Nazorat roʻyxati yakunlandi", "shield");
  });

  function artText() {
    var out = [];
    ART.forEach(function (sec) {
      var parts = sec.k.map(function (k) { return nv(k); }).filter(Boolean);
      out.push({ h: sec.h, t: parts.join("\n\n") });
    });
    return out;
  }
  function renderArt() {
    var p = $("artPaper"); if (!p) return;
    var secs = artText(), filled = 0;
    var h = "<h1>" + esc($("artTitle").textContent) + '</h1><div class="ct">PhD Lab · M' + MOD + " · " + new Date().toLocaleDateString("uz-UZ") + "</div>";
    secs.forEach(function (s) { if (s.t) filled++; h += "<h4>" + esc(s.h) + "</h4>" + (s.t ? "<p>" + esc(s.t) + "</p>" : '<p class="ph">Hali yozilmagan</p>'); });
    p.innerHTML = h;
    $("artMeta").textContent = filled + " / " + secs.length + " boʻlim toʻldirilgan.";
    var fb = $("finBtn"); fb.disabled = !!S.done.fin; if (S.done.fin) fb.textContent = "✓ Yakunlangan";
  }
  $("finBtn").addEventListener("click", function () {
    var nd = 0; for (var i = 1; i <= NL; i++) if (S.done["l" + i]) nd++;
    if (nd < NL) { toast("Avval barcha darslarni yakunlang (" + nd + " / " + NL + ")", "lock"); return; }
    if ($("toolBtn") && !S.done.tool) { toast("Avval vosita natijasini saqlang", "lock"); return; }
    if (!S.ck.hon) { toast("Halollik bayonotini belgilang", "lock"); return; }
    var secs = artText(), empty = secs.filter(function (s) { return !s.t; }).length;
    if (empty > Math.floor(secs.length / 3)) { toast("Hujjatda " + empty + " ta boʻsh boʻlim bor", "lock"); return; }
    award("fin", FINXP, "Modul hujjati tayyor", "seedling"); confetti(); renderArt();
  });
  $("docBtn").addEventListener("click", function () {
    var p = $("artPaper");
    download("PhD_M" + MOD + "_" + $("artTitle").textContent.replace(/[^A-Za-z0-9\u02bb\u02bc]+/g, "_") + ".doc", "application/msword", '<html><head><meta charset="utf-8"></head><body style="font-family:Georgia,serif">' + p.innerHTML + "</body></html>");
  });
  $("copyBtn").addEventListener("click", function () {
    copyText(artText().map(function (s) { return s.h.toUpperCase() + "\n" + (s.t || "—"); }).join("\n\n"));
  });

  function renderAll() {
    var nodes = document.querySelectorAll("[data-node]"), n = 0;
    nodes.forEach(function (el) { var d = !!S.done[el.getAttribute("data-node")]; el.classList.toggle("done", d); if (d) n++; });
    $("mapN").textContent = n + " / " + nodes.length + " bosqich";
    document.querySelectorAll("[data-badge]").forEach(function (el) { el.classList.toggle("on", !!S.done[el.getAttribute("data-badge")]); });
  }
  if (window.KGTool && window.KGTool.init) window.KGTool.init();
  renderQuiz(); renderArt(); renderAll(); renderXp(false);
})();
</script>"""


def page(slug, M):
    code = code_of(slug)
    n = int(code.split("-")[0])
    trk = code.split("-")[1] if "-" in code else ""
    les = M["lessons"]
    if trk:
        les = [dict(L, body=strip_tracks(L["body"], trk), task=strip_tracks(L["task"], trk)) for L in les]
    nl = len(les)
    lxp = 120 // nl
    finxp = 250 - nl * lxp - 90
    assert finxp > 0
    key = "kompas_phd_m" + slug + "_v1"
    nodes = "".join(f'<a class="node" href="#l{k}" data-node="l{k}"><span class="dot">{n}.{k}</span>{fix(L["short"])}</a>' for k, L in enumerate(les, 1))
    T, C = M["tool"], M["check"]
    nodes += f'<a class="node" href="#{T["id"]}" data-node="tool"><span class="dot">🛠</span>{fix(T["short"])}</a>'
    nodes += '<a class="node" href="#check" data-node="ck"><span class="dot">✅</span>Nazorat</a>'
    nodes += f'<a class="node" href="#artefakt" data-node="fin"><span class="dot">✓</span>{fix(M["art_short"])}</a>'
    pn = nl + 3
    goals = "".join(f'<li>{img(i)}<span><b>{fix(a)}:</b> {fix(b)}</span></li>' for i, a, b in M["goals"])
    badges = [("quizOk", "books", "Bilimdon", "Test 3+/4"), ("half", "compass", "Yarim yoʻl", f"{(nl + 1) // 2} dars"),
              ("all", "telescope", "Darslar", f"{nl} dars"), ("tool", "memo", fix(M["tool"]["badge"]), "Vosita"),
              ("ck", "shield", "Nazoratchi", "Roʻyxat"), ("fin", "seedling", fix(M["art_short"]), "Yakun")]
    bhtml = "".join(f'<div class="bdg" data-badge="{b}">{img(i)}{t}<small>{s}</small></div>' for b, i, t, s in badges)
    import json
    art = [{"h": fix(h), "k": ks} for h, ks in M["art"]]
    js = (JS.replace("%KEY%", key).replace("%N%", '"' + code + '"').replace("%LXP%", str(lxp)).replace("%NL%", str(nl))
          .replace("%FINXP%", str(finxp)).replace("%ART%", json.dumps(art, ensure_ascii=False)))
    extra_js = ("<script>\n" + M["js"].strip() + "\n</script>\n") if M.get("js") else ""
    nxt = (f'<a class="btn btn-p" href="{M["next_href"]}">Keyingi: {fix(M["next"])} →</a>' if M.get("next_href")
           else '<a class="btn btn-p" href="dashboard.html">Mening kabinetim →</a>')
    weeks = M["weeks"]
    html = f'''<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#2d4a3e">
<title>M{code} {fix(M["title"])} · PhD Lab · Kompas Lab</title>
<meta name="description" content="{fix(M["desc"])}">
<link rel="icon" href="img/3d/compass.webp" type="image/webp">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Caladea:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600;700&family=Playfair+Display:wght@400;700&text=%CA%BB%CA%BC%C3%96%C3%B6%C4%9E%C4%9F%C5%9E%C5%9F%C3%87%C3%A7&display=swap" rel="stylesheet"><script src="js/alifbo.js"></script>
<style>
{{{{CSS}}}}
{EXTRA_CSS}
.path.pn{{--pn:{pn};}}
</style>
</head>
<body>

<header class="top">
  <div class="wrap">
    <a class="logo" href="phd-lab.html"><img src="img/3d/compass.webp" width="160" height="160" alt="">Kompas Lab <small>· PhD Lab M{code}</small></a>
    <div class="xp" aria-live="polite">
      <span class="lvl" id="lvl">1-daraja: Kuzatuvchi</span>
      <span class="xp-pill" id="xpPill"><img src="img/3d/bulb.webp" width="160" height="160" alt=""><span id="xpN">0</span>&nbsp;XP</span>
    </div>
  </div>
  <div class="xp-bar"><i id="xpBar"></i></div>
</header>

<main>
<div class="wrap">

  <div class="hero">
    <div class="hero-g">
      <div>
        <div class="crumb"><a href="index.html">Kompas Lab</a> · <a href="phd-lab.html">PhD Lab</a> · Modul {code}</div>
        <span class="badge" style="background:var(--accent-lit);color:var(--accent)">{PHASE[n]}</span>
        <h1>{fix(M["title"])}</h1>
        <p class="lead">{fix(M["lead"])}</p>
        <div class="facts"><span class="fact"><b>{nl}</b> dars</span><span class="fact">~<b>{weeks}</b> hafta</span><span class="fact">{PHASE[n].split(" · ")[0]}</span><span class="fact"><b>250</b> XP</span></div>
      </div>
      {img(M["hero"], "hero-art float")}
    </div>
  </div>

  <nav class="map" aria-label="Modul xaritasi">
    <div class="map-h"><b>Sizning yoʻlingiz</b><span id="mapN">0 / {pn} bosqich</span></div>
    <div class="path pn">
      {nodes}
    </div>
  </nav>

  <section>
    <h2>Modul yakunida sizda</h2>
    <ul class="goal">
      {goals}
    </ul>
    <div class="box warn" style="margin-top:14px">{fix(M["warn"])}</div>
  </section>

  <section id="darslar">
    <h2>Darslar</h2>
    <p class="sub">Har dars toʻrt qismdan iborat: Diqqat 🔥, Asosiy qism, Xulosa va Topshiriq. Javoblaringiz faqat shu qurilmada saqlanadi.</p>
    <div class="lessons">

{chr(10).join(lesson_html(n, k, L, lxp) for k, L in enumerate(les, 1))}

    </div>
  </section>

{tool_html(T)}

{check_html(C)}

  <section id="nishonlar">
    <h2>Nishonlar</h2>
    <div class="badges">
      {bhtml}
    </div>
  </section>

  <section id="artefakt">
    <h2 id="artTitle">{fix(M["art_title"])}</h2>
    <p class="sub">Darslardagi javoblar va vositadan avtomatik yigʻiladi. PDF uchun “Chop etish” → “PDF sifatida saqlash”.</p>
    <div class="artifact">
      <div class="paper" id="artPaper"></div>
      <div class="noprint" id="artMeta" style="font-size:13.5px;color:var(--muted);margin-top:12px"></div>
      <label class="ck noprint" data-ck="hon" style="margin-top:12px"><input type="checkbox"><span><b>Halollik bayonoti:</b> bu hujjatdagi matn va faktlar meniki, tekshiriladigan va hujjat bilan tasdiqlanadi. Kompas namunalari faqat oʻrganish uchun.</span></label>
      <div class="row">
        <button class="btn btn-p" type="button" id="finBtn">Yakunlash · +{finxp} XP</button>
        <button class="btn btn-g" type="button" id="docBtn">📄 Word (.doc)</button>
        <button class="btn btn-g" type="button" id="copyBtn">📋 Matnni nusxalash</button>
        <button class="btn btn-g" type="button" onclick="window.print()">🖨 Chop etish / PDF</button>
      </div>
    </div>
  </section>

  <section>
    <div class="mentor">
      <div class="av">KL</div>
      <div>
        <q>{fix(M["tip"])}</q>
        <small>Kompas Lab maslahati</small>
      </div>
    </div>
  </section>

  <section>
    <h2>Modul pasporti</h2>
    <div class="pass">
      <div><b>Darslar</b>{nl} ta</div>
      <div><b>Vaqt</b>~{weeks} hafta (haftasiga 3–5 soat)</div>
      <div><b>Natija</b>{fix(M["art_title"])}</div>
    </div>
    <p class="srcs">Faktlar: {fix(M["sources"])}</p>
  </section>
</div>
</main>

<footer>
  <div class="wrap">
    <a class="btn btn-g" href="phd-lab.html">← PhD Lab</a>
    {nxt}
  </div>
</footer>

<div class="toast" id="toast" role="status"><img id="toastImg" src="img/3d/bulb.webp" width="160" height="160" alt=""><span id="toastT"></span></div>
<script src="js/sfx.js"></script>
{extra_js}{js}
</body>
</html>
'''
    return html


def load(slug):
    for d in (HERE, HERE / "mods"):
        if str(d) not in sys.path:
            sys.path.insert(0, str(d))
    spec = importlib.util.spec_from_file_location("phd_m" + slug, HERE / "mods" / ("m" + slug + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.MOD


if __name__ == "__main__":
    for slug in (sys.argv[1:] or SLUGS):
        out = SRC / f"phd-lab-m{slug}.src.html"
        out.write_text(page(slug, load(slug)), encoding="utf-8")
        print("yozildi:", out.relative_to(HERE.parent.parent.parent))
