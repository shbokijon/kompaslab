# GKS M1–M8 yetkazishdan oldingi tekshiruv (loyiha qoʻllanmasi 8-boʻlim, 1–6-bandlar).
#   python3 tools/modules/gks/check.py [1 2 ...]
# 7-band (brauzer) alohida: tools/modules/test/paid_reader.js va gks/browser_test.js.
import re, subprocess, sys, tempfile
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.err, self.text, self.skip = [], [], [], 0
    def handle_starttag(self, t, a):
        if t in VOID: return
        self.stack.append(t)
        if t in ("script", "style"): self.skip += 1
    def handle_endtag(self, t):
        if t in VOID: return
        if not self.stack or self.stack[-1] != t:
            self.err.append(f"</{t}> kutilmagan (stek: {self.stack[-3:]})"); return
        self.stack.pop()
        if t in ("script", "style"): self.skip -= 1
    def handle_data(self, d):
        if not self.skip: self.text.append(d)


def check(n):
    out = []
    src = (ROOT / f"tools/modules/src/gks-lab-m{n}.src.html").read_text(encoding="utf-8")
    page = (ROOT / f"tools/modules/paid/gks-lab-m{n}.html").read_text(encoding="utf-8")
    for name, s in (("src", src), ("paid", page)):
        p = P(); p.feed(s); p.close()
        if p.err or p.stack: out.append(f"{name}: teglar balansi: {p.err[:3]} ochiq: {p.stack}")
    # 2) JS sintaksisi
    for i, js in enumerate(re.findall(r"<script(?![^>]*src=)[^>]*>(.*?)</script>", page, flags=re.S)):
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
            f.write(js)
        r = subprocess.run(["node", "--check", f.name], capture_output=True, text=True)
        if r.returncode: out.append(f"JS #{i}: {r.stderr.strip()[:200]}")
    # 3) dars tuzilmasi
    nl = len(re.findall(r'<article class="lesson"', src))
    for tab in ("Diqqat 🔥", "Asosiy qism", "Xulosa", "Topshiriq"):
        c = src.count(f'role="tab">{tab}<')
        if c != nl: out.append(f"tab '{tab}': {c} ≠ {nl} dars")
    # 4) qobiq
    if "<main>" not in src: out.append("<main> yoʻq")
    # 5) imlo (koʻrinadigan matn: script/style tashqarisi)
    p = P(); p.feed(src); txt = "".join(p.text)
    if "'" in txt: out.append("ASCII apostrof matnda: " + repr(txt[max(0, txt.index("'") - 30):txt.index("'") + 30]))
    if re.search("[\u0400-\u04ff]", src): out.append("kirill harfi bor")
    if re.search("[\u00d6\u00f6\u011e\u011f\u015e\u015f\u00c7\u00e7]", src): out.append("manbada yangi alifbo harfi bor")
    w = sorted(set(re.findall("\\w*[oOgG]\u02bc\\w*", txt)))
    if w: print(f"   ? M{n}: o/g + U+02BC bor, tekshiring: {w[:8]}")
    # 6) yangi alifbo skripti zaxira shriftdan keyin
    i, j = src.find("text=%CA%BB%CA%BC"), src.find('<script src="js/alifbo.js">')
    if not (0 < i < j): out.append("alifbo.js zaxira shrift havolasidan keyin emas")
    if "kp-wm" not in page: out.append("suv belgisi yoʻq")
    return out


if __name__ == "__main__":
    ns = [int(x) for x in sys.argv[1:]] or list(range(1, 9))
    bad = 0
    for n in ns:
        r = check(n)
        print(f"M{n}:", "OK" if not r else "")
        for x in r: print("   -", x)
        bad += len(r)
    sys.exit(1 if bad else 0)
