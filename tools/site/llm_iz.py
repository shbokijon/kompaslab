# "LLM izi" hisoboti (2026-11-12): sahifalardagi koʻrinadigan matnda qoliplarni sanaydi.
# Faqat hisobot, matnga tegmaydi.
#   python3 tools/site/llm_iz.py            → eng "ogʻir" 20 sahifa (tools/site/llm_iz_hisobot.md)
#   python3 tools/site/llm_iz.py index.html → bitta sahifa, har topilma bilan
# Qoliplar (asoschi roʻyxati, 2026-11-12):
#   kolon   — "X: Y" qolipi (qisqa yorliq + ikki nuqta + davomi)
#   ogoh    — ogohlantirish va istisno soʻzlari (faqat, emas, kafolat, tekshiring, ehtiyot, istisno …)
#   zanjir  — ot birikmalari zanjiri: feʼlsiz, 6+ soʻzli yoki 2+ "va" li ot iborasi
#   emas    — "shunchaki X emas", "emas, balki", "nafaqat … balki"
#   uchlik  — uchlik roʻyxat: "X, Y va Z" va aynan 3 bandli <ul>/<ol>
#   yuzsiz  — "Kompas … beradi/oʻrgatadi" ohangi (gap egasi Kompas/Lab/dastur)
#   uzun    — 20 soʻzdan uzun gap
# Ball = ogʻirlik × soni, 1 000 soʻzga keltirilgan (sahifa uzunligi taʼsir qilmasin); 150 soʻzdan qisqa sahifa kirmaydi.
import re, sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKIP = {"admin.html", "admin-paid.html", "globe-demo.html", "offline.html", "payment.html", "lesson.html",
        "uk-sponsors.html", "nl-sponsors.html", "ca-lmia.html", "oferta.html", "maxfiylik.html"}
BLOCK = {"p", "li", "h1", "h2", "h3", "h4", "h5", "td", "th", "div", "section", "summary", "details", "dd", "dt",
         "blockquote", "figcaption", "label", "button", "a", "small", "b", "strong", "span", "header", "footer", "nav", "main", "br", "option"}
HARD = {"p", "li", "h1", "h2", "h3", "h4", "h5", "td", "th", "div", "section", "summary", "dd", "dt", "blockquote",
        "figcaption", "label", "button", "header", "footer", "nav", "main", "br", "option", "a"}
W = {"kolon": 1.0, "ogoh": 0.6, "zanjir": 1.0, "emas": 2.0, "uchlik": 0.8, "yuzsiz": 1.5, "uzun": 1.0}


class Text(HTMLParser):
    """Koʻrinadigan matnni bloklarga ajratib oladi: script/style, hidden, lang≠uz, translate=no tashlanadi."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0; self.stack = []; self.blocks = [""]; self.lists = []; self.uls = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        hide = tag in ("script", "style", "noscript", "template", "svg", "head", "title") or "hidden" in a \
            or (a.get("lang") and not a["lang"].startswith("uz")) or a.get("translate") == "no" or a.get("aria-hidden") == "true"
        if tag in ("br", "img", "input", "meta", "link", "hr", "source", "wbr"):
            if tag == "br": self.blocks.append("")
            return
        self.stack.append(hide)
        if hide: self.skip += 1
        if tag in HARD: self.blocks.append("")
        else: self.blocks[-1] += " "
        if tag in ("ul", "ol") and not self.skip: self.lists.append(0)
        if tag == "li" and self.lists: self.lists[-1] += 1

    def handle_endtag(self, tag):
        if tag in ("br", "img", "input", "meta", "link", "hr", "source", "wbr"): return
        if tag in ("ul", "ol") and self.lists and not self.skip: self.uls.append(self.lists.pop())
        if self.stack and self.stack.pop(): self.skip -= 1
        if tag in HARD: self.blocks.append("")
        else: self.blocks[-1] += " "

    def handle_data(self, d):
        if not self.skip: self.blocks[-1] += d


VERB = re.compile(r"(?i)(di|adi|aydi|ydi|ladi|moqda|yapti|ing|ingiz|asiz|ysiz|siz|miz|dir|mi|sa|gan|ib|may|maydi|mas|mang|ylik|ylar|ar|ish|moq|ladi|ilsin|sin|kerak|mumkin|bor|yoʻq|lar|i|edi|sangiz|ganda|guncha|gach)$")
WARN = re.compile(r"(?i)\b(faqat|emas|kafolat\w*|tekshiring|tekshirish\w*|ehtiyot\w*|istisno\w*|lekin|biroq|ammo|shart emas|mumkin emas|tavsiya etilmaydi|hech qanday|qatʼiy|xavf\w*|diqqat)\b")
EMAS = re.compile(r"(?i)(shunchaki\b[^.!?]{0,80}\bemas|emas,\s*balki|nafaqat\b[^.!?]{0,120}\bbalki)")
TRI = re.compile(r"(?i)\b[\wʻʼ'-]+(?: [\wʻʼ'-]+){0,3}, [\wʻʼ'-]+(?: [\wʻʼ'-]+){0,3} va [\wʻʼ'-]+")
FACE = re.compile(r"(?i)\b(Kompas(?: Lab)?|Lab|dastur|modul|platforma)(?:\s\w+){0,4}\s\w*(beradi|oʻrgatadi|koʻrsatadi|yordam beradi|taqdim etadi|tayyorlaydi|qamraydi|ochadi|tushuntiradi)\b")
COLON = re.compile(r"(?:^|[.!?]\s+)([^\s:.!?][^:.!?]{0,40}):\s+\S")


def sentences(block):
    block = re.sub(r"\s+", " ", block).strip()
    if not block: return []
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-ZʻOʼ\"«(0-9])", block) if s.strip()]


def scan(path):
    p = Text(); p.feed(path.read_text(encoding="utf-8"))
    blocks = [re.sub(r"\s+", " ", b).strip() for b in p.blocks]
    blocks = [b for b in blocks if len(b) > 1]
    hits = {k: [] for k in W}
    words = 0
    for b in blocks:
        for s in sentences(b):
            ws = re.findall(r"[\wʻʼ'-]+", s); n = len(ws); words += n
            if n == 0: continue
            if COLON.search(s) and n >= 3: hits["kolon"].append(s)
            hits["ogoh"] += [s] * min(2, len(WARN.findall(s)))
            if EMAS.search(s): hits["emas"].append(s)
            if TRI.search(s) and n >= 6: hits["uchlik"].append(s)
            if FACE.search(s): hits["yuzsiz"].append(s)
            if n > 20: hits["uzun"].append(s)
            last = ws[-1].lower()
            if re.search(r"soʻm|\d{2,}", s): pass
            elif (n >= 6 and not VERB.search(last) and not s.endswith("?")) or s.count(" va ") >= 2 and not VERB.search(last):
                hits["zanjir"].append(s)
    hits["uchlik"] += ["<ul>, 3 band"] * sum(1 for c in p.uls if c == 3)
    raw = sum(W[k] * len(v) for k, v in hits.items())
    return words, hits, (raw * 1000 / words if words else 0)


def main(args):
    if args:
        for f in args:
            words, hits, sc = scan(ROOT / f)
            print(f"# {f}: {words} soʻz, ball {sc:.0f}")
            for k, v in hits.items():
                print(f"\n## {k} ({len(v)})")
                for s in v[:40]: print("  -", s[:200])
        return
    rows = []
    for f in sorted(ROOT.glob("*.html")):
        if f.name in SKIP: continue
        words, hits, sc = scan(f)
        if words < 150: continue
        rows.append((sc, f.name, words, {k: len(v) for k, v in hits.items()}))
    rows.sort(reverse=True)
    # Turlar: sotuv/sayt sahifalari (tahrirning asosiy maqsadi), modul roʻyxati sahifalari, M0 (bir xil DOM: faqat hub sanaladi)
    def kind(f):
        if re.search(r"-m0-(\d+|yakun)\.html$", f): return "m0dars"
        if re.search(r"-m0\.html$", f): return "m0"
        if re.search(r"-m\d+(-[a-z])?\.html$", f) or f.endswith("-o.html"): return "modul"
        return "sotuv"
    rows = [r for r in rows if kind(r[1]) != "m0dars"]
    sale = [r for r in rows if kind(r[1]) == "sotuv"]
    mods = [r for r in rows if kind(r[1]) == "modul"]
    m0s = [r for r in rows if kind(r[1]) == "m0"]
    tot = {k: sum(r[3][k] for r in rows) for k in W}
    out = ["# \"LLM izi\" hisoboti", "", f"Sana: 2026-11-12. Skript: `tools/site/llm_iz.py`. Sahifalar: {len(rows)} (150 soʻzdan uzun).",
           "Ball = ogʻirlik × soni, 1 000 soʻzga. Ogʻirliklar: " + ", ".join(f"{k} {w}" for k, w in W.items()) + ".", "",
           "M0 darslari (`*-m0-N.html`) hub bilan bir xil DOM bilan keladi, shuning uchun faqat `*-m0.html` sanaladi.", ""]
    HDR = ["| # | Sahifa | Soʻz | Ball | X: Y | Ogohl. | Zanjir | Emas/balki | Uchlik | Yuzsiz | Uzun gap |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    def table(title, rs, n):
        out.extend([title, ""] + HDR)
        for i, (sc, f, words, h) in enumerate(rs[:n], 1):
            out.append(f"| {i} | `{f}` | {words} | {sc:.0f} | {h['kolon']} | {h['ogoh']} | {h['zanjir']} | {h['emas']} | {h['uchlik']} | {h['yuzsiz']} | {h['uzun']} |")
        out.append("")
    table("## Eng ogʻir 20 sahifa: sayt va Lab sotuv sahifalari", sale, 20)
    table("## M0 modullari", m0s, 20)
    table("## Modul roʻyxati sahifalari (eng ogʻir 10; \"X: Y\" asosan darslar roʻyxatidagi \"Natija:\" qatorlari)", mods, 10)
    out += ["## Tahrir tartibidagi sahifalar", "", "| Sahifa | Oʻrin | Soʻz | Ball | X: Y | Ogohl. | Zanjir | Emas/balki | Uchlik | Yuzsiz | Uzun gap |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    rank = {r[1]: i for i, r in enumerate(sale + m0s + mods, 1)}
    rank.update({r[1]: i for i, r in enumerate(sale, 1)})
    for f in ["index.html", "master-lab.html", "master-lab-narxlar.html", "master-lab-m0.html"]:
        r = next((x for x in rows if x[1] == f), None)
        if r:
            h = r[3]; out.append(f"| `{f}` | {rank[f]} | {r[2]} | {r[0]:.0f} | {h['kolon']} | {h['ogoh']} | {h['zanjir']} | {h['emas']} | {h['uchlik']} | {h['yuzsiz']} | {h['uzun']} |")
    out += ["", "## Jami (hamma sahifa)", ""] + [f"- {k}: {v}" for k, v in tot.items()]
    out += ["", "Cheklov: qoliplar oddiy qoidalar bilan sanaladi (soʻz va tinish belgilari). \"Zanjir\" va \"yuzsiz\" taxminiy: yanglish topilma boʻlishi mumkin. Har sahifa tafsiloti: `python3 tools/site/llm_iz.py <fayl>`."]
    (ROOT / "tools/site/llm_iz_hisobot.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    main(sys.argv[1:])
