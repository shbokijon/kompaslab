"""Magistratura M1–M8 v2 (2026-11-19, asoschi): qisqa dars standarti.

Ishga tushirish (bir marta, src/*.src.html ni joyida yangilaydi):
    python3 tools/modules/master_v2/apply.py && python3 tools/modules/build.py master-lab-m1 … master-lab-m8

Kontent tools/modules/master_v2/content.py da YANGI alifboda yozilgan (Ö, Ğ, Ş, Ç);
manbaga yozishda amaldagi alifboga (oʻ, gʻ, sh, ch; U+02BB) oʻgiriladi, chunki saytda js/alifbo.js
yangi alifboni oʻzi koʻrsatadi. Qayta ishga tushirilsa, allaqachon yangilangan modul oʻtkaziladi
(<!-- mv2 --> belgisi).

Har darsda: Diqqat (panel 1) va Xulosa (panel 3) toʻliq almashadi; Asosiy qism (panel 2) kontentda
berilgan boʻlsa almashadi, eski "Rasmiy manbalar" va faktlar bloklari (facts2) saqlanib ⓘ ostiga oʻtadi;
Topshiriq (panel 4) da faqat sarlavha va koʻrsatma roʻyxati almashadi, vositalar (id, data-save) tegilmaydi.
"""
import re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from lib import lesson_span, panels, find_div_end
import content as C

SRC = pathlib.Path(__file__).resolve().parents[1] / "src"
MARK = "<!-- mv2 -->"

OLD = {"ö": "oʻ", "Ö": "Oʻ", "ğ": "gʻ", "Ğ": "Gʻ", "ş": "sh", "Ş": "Sh", "ç": "ch", "Ç": "Ch"}
def old(t):
    t = t.replace("'", "ʼ")
    return "".join(OLD.get(c, c) for c in t)

CSS = """
/* Master v2 (2026-11-19): qisqa dars, ⓘ, video joyi, keyingi qadam */
.mv-i{margin-top:12px;border:1px solid var(--border);border-radius:12px;background:var(--bg);font-size:14px}
.mv-i>summary{cursor:pointer;list-style:none;padding:9px 12px;font-weight:700;color:var(--muted)}
.mv-i>summary::-webkit-details-marker{display:none}
.mv-i>summary::before{content:"\\24D8";display:inline-block;margin-right:7px;color:var(--accent);font-weight:800}
.mv-i[open]>summary{border-bottom:1px solid var(--border)}
.mv-i>div{padding:10px 12px}
.mv-i .box,.mv-i .facts2{margin:8px 0}
.mv-fun{display:block;margin-top:10px;font-size:13.5px;color:var(--muted)}
.mv-take{font-size:16.5px;line-height:1.5}
.mv-note{background:var(--bg);border:1px solid var(--border);border-radius:16px;padding:14px 16px;font-size:14.5px;margin:0 0 6px}
.mv-next{background:var(--surface);border:2px solid var(--accent);border-radius:20px;padding:20px 22px}
.mv-next h2{margin-top:0}
.mv-next .mv-row{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px;align-items:center}
.mv-next .mv-k{background:var(--accent-lit);border-radius:14px;padding:12px 14px;margin:10px 0;font-size:15.5px}
.mv-next ul.mv-lock{list-style:none;padding:0;margin:10px 0;display:grid;gap:6px}
.mv-next ul.mv-lock li{display:flex;gap:8px;align-items:center;font-size:14.5px;color:var(--muted)}
.mv-next ul.mv-lock img{width:22px;height:22px}
.mv-bar{height:8px;border-radius:99px;background:var(--bg);overflow:hidden;margin:8px 0 2px}
.mv-bar i{display:block;height:100%;background:var(--accent)}
.mv-small{font-size:12.5px;color:var(--muted)}
[data-kvideo]:empty{display:none}
"""

def strip_emoji(t):
    return re.sub(r"[\U0001F300-\U0001FAFF☀-➿️]\s?", "", t)

def text_only(s, fn):
    """fn ni faqat <script>/<style> dan tashqaridagi teg orasidagi matnga qoʻllaydi."""
    out, pos = [], 0
    for m in re.finditer(r"<(script|style)\b.*?</\1>", s, re.S):
        out.append(_tx(s[pos:m.start()], fn)); out.append(m.group(0)); pos = m.end()
    out.append(_tx(s[pos:], fn))
    return "".join(out)

def _tx(s, fn):
    return re.sub(r">([^<]+)<", lambda m: ">" + fn(m.group(1)) + "<", s)

def words(t):
    t = t.replace("tarjimayi hol", "tarjimai hol").replace("Tarjimayi hol", "Tarjimai hol")
    t = t.replace("Brag Sheet quruvchi", "Yutuqlar varaqasi quruvchi").replace("Brag Sheet", "Yutuqlar varaqasi")
    t = t.replace("Outreach Log", "Xatlar daftari")
    t = re.sub(r"\s—\s", ": ", t)
    return t

def keep_blocks(p2):
    """Eski Asosiy qismdan saqlanadigan bloklar: manbalar (box … Rasmiy manbalar / Manbalar, .srcs) va facts2."""
    keep_src, keep_facts = [], []
    for cls in ("facts2",):
        pos = 0
        while True:
            i = p2.find('<div class="%s"' % cls, pos)
            if i < 0: break
            j = find_div_end(p2, i); keep_facts.append(p2[i:j]); pos = j
    for m in re.finditer(r'<div class="(?:box info|srcs)"[^>]*>', p2):
        j = find_div_end(p2, m.start()); blk = p2[m.start():j]
        if re.search(r"(Rasmiy manbalar|Manbalar)\s*:", blk): keep_src.append(blk)
    for m in re.finditer(r'<p class="hint">', p2):
        j = p2.index("</p>", m.start()) + 4; blk = p2[m.start():j]
        if "http" in blk: keep_src.append(blk)
    return keep_facts, keep_src

def info(summary, inner):
    return '<details class="mv-i"><summary>%s</summary><div>%s</div></details>' % (summary, inner)

def rebuild_lesson(art, n, lid, L):
    ps = panels(art)
    (a1, b1), (a2, b2), (a3, b3), (a4, b4) = ps[:4]
    p2_old = art[a2:b2]
    facts, srcs = keep_blocks(p2_old)

    # 1. Diqqat
    if L.get("hook"):
        hook = '<div class="hook">%s%s</div>' % (old(L["hook"]), ('<small class="mv-fun">%s</small>' % old(L["fun"])) if L.get("fun") else "")
        p1 = '<div class="panel">%s</div>' % hook
    else:
        p1 = art[a1:b1]
    # 2. Asosiy qism
    vid = '<div data-kvideo="%s"></div>' % lid
    if L.get("main"):
        body = old(L["main"])
        extra = ""
        if L.get("info"): extra += info(old(L.get("info_t", "Batafsil")), old(L["info"]))
        if facts: extra += info(old("Faktlar, sana va rasmiy havola"), "".join(facts))
        if srcs: extra += info(old("Manbalar"), "".join(srcs))
        p2 = '<div class="panel">%s%s%s</div>' % (vid, body, extra)
    else:
        inner = p2_old[len('<div class="panel">'):-len("</div>")]
        p2 = '<div class="panel">%s%s</div>' % (vid, inner)
    # 3. Xulosa
    if L.get("take"):
        img = re.search(r'<img [^>]*>', art[a3:b3])
        p3 = '<div class="panel"><div class="take">%s<p class="mv-take">%s</p></div></div>' % (img.group(0) if img else "", old(L["take"]))
    else:
        p3 = art[a3:b3]
    # 4. Topshiriq
    p4 = art[a4:b4]
    if L.get("task_b"):
        p4 = re.sub(r"<b>.*?</b>", "<b>%s</b>" % old(L["task_b"]), p4, count=1, flags=re.S)
    if L.get("task") is not None:
        ul = "<ul>%s</ul>" % "".join("<li>%s</li>" % old(x) for x in L["task"])
        if re.search(r"<ul>.*?</ul>", p4, re.S):
            p4 = re.sub(r"<ul>.*?</ul>", lambda m: ul, p4, count=1, flags=re.S)
        else:
            p4 = p4.replace("</b>", "</b>" + ul, 1)
    p4 = re.sub(r'<div class="hint">[^<]*saqlanadi\.?</div>', "", p4)
    art = art[:a1] + p1 + art[b1:a2] + p2 + art[b2:a3] + p3 + art[b3:a4] + p4 + art[b4:]

    # sarlavha: vaqt va nom
    if L.get("min"):
        art = re.sub(r'<span class="tag">⏱ [^<]*</span>', '<span class="tag">~%d daqiqa</span>' % L["min"], art, count=1)
    if L.get("t"):
        art = re.sub(r'(<span class="l-t"[^>]*>)[^<]*(</span>)', lambda m: m.group(1) + old(L["t"]) + m.group(2), art, count=1)
    return art

def apply(n):
    f = SRC / ("master-lab-m%d.src.html" % n)
    s = f.read_text(encoding="utf-8")
    if MARK in s:
        print("M%d: allaqachon yangilangan" % n); return
    M = C.MODULES[n]

    for lid, L in M["lessons"].items():
        a, b = lesson_span(s, lid)
        s = s[:a] + rebuild_lesson(s[a:b], n, lid, L) + s[b:]

    # Tablar, teglar: emoji yoʻq
    s = s.replace("Diqqat 🔥", "Diqqat")
    s = re.sub(r'<span class="tag">([^<]*)</span>', lambda m: '<span class="tag">%s</span>' % strip_emoji(m.group(1)).strip(), s)
    # Xarita sarlavhasi va hisoblagich: "qadam" (I–IV bosqich bilan aralashmasin)
    s = s.replace("<b>Oʻquv bosqichlari</b>", "<b>Modul yoʻli</b>")
    s = re.sub(r'(id="mapN">0 / \d+) (?:qadam|bosqich)', r"\1 qadam", s)
    s = s.replace('" bosqich";', '" qadam";')
    # Hero
    s = re.sub(r'<p class="lead">.*?</p>', lambda m: '<p class="lead">%s</p>' % old(M["lead"]), s, count=1, flags=re.S)
    s = re.sub(r'(<span class="fact">~<b>)[^<]*(</b> hafta</span>)', lambda m: m.group(1) + M["weeks"] + m.group(2), s, count=1)
    # "Har dars toʻrt qismdan…" → bitta ⓘ
    s = re.sub(r'(<section id="darslar">\s*<h2>Darslar</h2>\s*)<p class="sub">.*?</p>',
               lambda m: m.group(1) + '<p class="sub">%s</p>%s' % (old(C.SUB), info(old("Bu modul nima qilmaydi"), "<p>%s</p>" % old(C.DISCLAIMER))),
               s, count=1, flags=re.S)
    # XP sarlavhasi: 0 XP boʻlsa koʻrinmaydi
    s = s.replace('$("lvl").textContent = l;', '$("lvl").textContent = l; $("lvl").parentNode.style.visibility = S.xp ? "" : "hidden";', 1)
    # Asoschi / maslahat
    if M.get("mentor"):
        s = re.sub(r'(<div class="mentor">.*?<q>).*?(</q>)', lambda m: m.group(1) + old(M["mentor"]) + m.group(2), s, count=1, flags=re.S)
    # Modul pasporti: vaqt
    s = re.sub(r'(<div><b>Vaqt</b>)[^<]*(</div>)', lambda m: m.group(1) + old(M["pass_time"]) + m.group(2), s, count=1)
    # Keyingi qadam bloki (pasportdan oldin) + natija videosi
    nxt = ('<section id="keyingi"><div class="mv-next" data-mnext="%d">%s</div></section>\n\n  ' % (n, old(M["next"])))
    s = s.replace("<section>\n    <h2>Modul pasporti</h2>", nxt + "<section>\n    <h2>Modul pasporti</h2>", 1)
    s = s.replace('<section id="artefakt">', '<section id="artefakt">\n    <div data-kvideo="res"></div>', 1)
    # Footer: oldingi va keyingi modul
    prev = ('master-lab-m%d.html' % (n - 1), "← M%d" % (n - 1)) if n > 1 else ("master-lab-m0.html", "← M0")
    s = re.sub(r'(<footer>\s*<div class="wrap">\s*)<a class="btn btn-g" href="[^"]*">[^<]*</a>',
               lambda m: m.group(1) + '<a class="btn btn-g" href="%s">%s</a>' % prev, s, count=1)
    if n < 8:
        s = re.sub(r'<span class="btn btn-g" style="cursor:default;opacity:.7">Keyingi: ([^<]*)</span>',
                   lambda m: '<a class="btn btn-p" href="master-lab-o.html?m=%d">Keyingi: %s →</a>' % (n + 1, m.group(1)), s, count=1)
    # Video va keyingi qadam skriptlari, main atributlari
    s = s.replace("<main>", '<main data-kv-lab="master-lab" data-kv-mod="%d">' % n, 1)
    s = s.replace('<script src="js/sfx.js"></script>',
                  '<script src="js/sfx.js"></script>\n<script src="js/module-video.js" defer></script>\n<script src="js/master-next.js" defer></script>', 1)
    # CSS
    s = s.replace("{{CSS}}", "{{CSS}}" + CSS, 1)
    # Matn: soʻzlar va uzun tire (faqat koʻrinadigan matnda)
    s = text_only(s, words)
    # Modulga xos aniq tuzatishlar
    for a, b in M.get("fix", []):
        a2, b2 = old(a), old(b)
        if a2 not in s: print("  ! M%d: topilmadi: %s" % (n, a[:60]))
        s = s.replace(a2, b2)
    s = s.rstrip("\n") + "\n" + MARK + "\n"
    f.write_text(s, encoding="utf-8")
    print("M%d: yangilandi" % n)

if __name__ == "__main__":
    for n in (map(int, sys.argv[1:]) if len(sys.argv) > 1 else range(1, 9)):
        apply(n)
