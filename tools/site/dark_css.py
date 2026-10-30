# Kompas Lab — tungi rejim (dark mode) CSS generatori (2026-10-30)
# Ishga tushirish (repo ildizidan, sahifalar yigʻilgandan keyin): python3 tools/site/dark_css.py
#
# Nima qiladi: kompas-ui.css ni yuklaydigan har sahifaning CSS manbalarini (css/*.css va
# sahifa ichidagi <style> bloklari) oʻqiydi, ranglarni tungi rejimga moslab
# html[data-theme="dark"] prefiksli qoidalar yozadi va natijani css/kompas-ui.css oxiridagi
# belgilangan blokka qoʻyadi. Qoʻlda tahrirlanmaydi: manba CSS oʻzgarsa, qayta ishga tushiring.
#
# Qoidalar:
#  · fon (background): ochiq rang → toʻq; qorongʻi CSS oʻzgaruvchilar (masalan --accent) fon sifatida
#    asl qiymatda qoladi (tungi rejimda --accent matn uchun yorqinlashadi)
#  · matn (color, fill, stroke): toʻq rang → yorqin
#  · chegara (border, outline): ochiq rang → toʻq
#  · @keyframes, box-shadow va rasmlar oʻzgarmaydi
import colorsys, re, subprocess, sys
from pathlib import Path
import tinycss2

ROOT = Path(__file__).resolve().parents[2]
KUI = ROOT / "css" / "kompas-ui.css"
BEGIN, END = "/* ==== TUNGI REJIM (generator: tools/site/dark_css.py) ==== */", "/* ==== TUNGI REJIM OXIRI ==== */"
P = 'html[data-theme="dark"]'

# Qoʻlda belgilangan asosiy tokenlar (brend ranglari tungi fonda oʻqiladigan boʻlishi uchun)
FIXED = {
    "--accent": "#9fd0b6", "--accent-h": "#bfe3cf", "--accent-lit": "#1c2b24",
    "--accent2": "#e0874f", "--accent2-h": "#ec9a66", "--accent2-lit": "#2e2018",
    "--bg": "#0f1512", "--surface": "#17201b", "--border": "#2a3731", "--cream": "#121a16",
    "--text": "#e5ece7", "--muted": "#a2b4aa", "--muted2": "#71847a",
    "--gold": "#d9b65a", "--gold-lit": "#2a2412", "--green": "#6fcf9a", "--green-lit": "#15291e",
    "--red": "#f19a90", "--red-lit": "#2e1816",
}
DARK_BG_BASE = "#0f1512"

def hex2rgb(h):
    h = h.lstrip("#")
    if len(h) in (3, 4): h = "".join(c * 2 for c in h[:3])
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))

def rgb2hex(r, g, b):
    return "#%02x%02x%02x" % tuple(max(0, min(255, round(x * 255))) for x in (r, g, b))

def lum(rgb):
    def ch(c): return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def to_dark_bg(rgb):
    h, l, s = colorsys.rgb_to_hls(*rgb)
    nl = 0.075 + (1 - l) * 0.55
    return colorsys.hls_to_rgb(h, min(nl, 0.24), s * 0.45)

def to_dark_border(rgb):
    h, l, s = colorsys.rgb_to_hls(*rgb)
    return colorsys.hls_to_rgb(h, 0.2 + (1 - l) * 0.35, s * 0.35)

def to_light_text(rgb):
    h, l, s = colorsys.rgb_to_hls(*rgb)
    return colorsys.hls_to_rgb(h, 0.86 - l * 0.35, min(s, 0.45))

COLOR_RE = re.compile(r"#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|\bwhite\b")

def parse_color(tok):
    t = tok.lower()
    if t == "white": return (1, 1, 1), 1.0
    if t.startswith("#"):
        a = 1.0
        h = t[1:]
        if len(h) == 8: a = int(h[6:], 16) / 255; h = h[:6]
        elif len(h) == 4: a = int(h[3] * 2, 16) / 255; h = h[:3]
        if len(h) not in (3, 6): return None
        return hex2rgb(h), a
    nums = re.findall(r"[\d.]+%?", t)
    if len(nums) < 3: return None
    try:
        rgb = tuple(float(n.rstrip("%")) / (100 if n.endswith("%") else 255) for n in nums[:3])
        a = float(nums[3].rstrip("%")) / (100 if nums[3].endswith("%") else 1) if len(nums) > 3 else 1.0
    except ValueError:
        return None
    return rgb, a

def fmt(rgb, a):
    if a >= 0.999: return rgb2hex(*rgb)
    return "rgba(%d,%d,%d,%s)" % (*(round(x * 255) for x in rgb), ("%.3f" % a).rstrip("0").rstrip("."))

def map_colors(value, kind):
    def rep(m):
        p = parse_color(m.group(0))
        if not p: return m.group(0)
        rgb, a = p
        L = lum(rgb)
        sat = colorsys.rgb_to_hls(*rgb)[2]
        if kind == "bg":
            if rgb == (1.0, 1.0, 1.0) and a < 0.5: return m.group(0)  # toʻq bloklardagi shaffof oq qatlam
            if L > 0.6: return fmt(to_dark_bg(rgb), a)
            return m.group(0)
        if kind == "border":
            if rgb == (1.0, 1.0, 1.0) and a < 0.5: return m.group(0)
            if L > 0.55: return fmt(to_dark_border(rgb), a)
            return m.group(0)
        if kind == "text":
            if L < 0.2 or (L < 0.3 and sat < 0.3): return fmt(to_light_text(rgb), a)
            return m.group(0)
        return m.group(0)
    return COLOR_RE.sub(rep, value)

def classify(prop):
    if prop in ("background", "background-color", "background-image"): return "bg"
    if prop.startswith("border") or prop.startswith("outline"): return "border"
    if prop in ("color", "fill", "stroke", "caret-color", "text-decoration-color", "-webkit-text-fill-color"): return "text"
    return None

def dark_var(name, value):
    if name in FIXED: return FIXED[name]
    v = value.strip()
    m = COLOR_RE.fullmatch(v)
    if not m: return None
    p = parse_color(v)
    if not p: return None
    rgb, a = p
    L = lum(rgb); sat = colorsys.rgb_to_hls(*rgb)[2]
    if L > 0.6: return fmt(to_dark_bg(rgb), a)
    if L < 0.2 or (L < 0.35 and sat < 0.3): return fmt(to_light_text(rgb), a)
    return None

def prefix(sel):
    out = []
    for part in sel.split(","):
        s = part.strip()
        if not s: continue
        if s.startswith(":root"): out.append(P + s[5:])
        elif s == "html" or s.startswith("html.") or s.startswith("html[") or s.startswith("html:"): out.append(P + s[4:])
        elif s.startswith("html "): out.append(P + s[4:])
        else: out.append(P + " " + s)
    return ",".join(out)

FLIPPED_DARK = set()  # yorugʻ rejimda toʻq, tungi rejimda yorqinlashgan oʻzgaruvchilar (fon uchun aslini saqlaymiz)
FLIPPED_LIGHT = set()  # yorugʻ rejimda ochiq, tungi rejimda toʻq boʻlgan oʻzgaruvchilar
ORIG = {}

def fix_var_refs(value, kind):
    def rep(m):
        n = m.group(1)
        if kind == "bg" and n in FLIPPED_DARK: return "var(--ko%s)" % n[1:]
        if kind == "text" and n in FLIPPED_LIGHT: return "var(--ko%s)" % n[1:]
        return m.group(0)
    return re.sub(r"var\((--[\w-]+)\)", rep, value)

def process_rules(rules, out, varsout):
    for r in rules:
        if r.type == "qualified-rule":
            sel = tinycss2.serialize(r.prelude).strip()
            decls = tinycss2.parse_declaration_list(r.content, skip_whitespace=True, skip_comments=True)
            new = []
            for d in decls:
                if d.type != "declaration": continue
                val = tinycss2.serialize(d.value).strip()
                imp = " !important" if d.important else ""
                if d.name.startswith("--"):
                    if sel.strip() in (":root", "html", ":root,html", "html,:root") or sel.startswith(":root"):
                        dv = dark_var(d.name, val)
                        if dv: varsout.setdefault(d.name, dv)
                    continue
                kind = classify(d.lower_name)
                if not kind: continue
                nv = fix_var_refs(map_colors(val, kind), kind)
                if nv != val: new.append("%s:%s%s" % (d.lower_name, nv, imp))
            if new:
                out.append((prefix(sel), ";".join(new)))
        elif r.type == "at-rule" and r.lower_at_keyword in ("media", "supports") and r.content:
            inner = []
            process_rules(tinycss2.parse_rule_list(r.content, skip_whitespace=True, skip_comments=True), inner, varsout)
            if inner:
                out.append(("@" + r.lower_at_keyword + " " + tinycss2.serialize(r.prelude).strip(), inner))

def collect_sources():
    files = subprocess.run(["git", "ls-files", "*.html"], cwd=ROOT, capture_output=True, text=True).stdout.split()
    css = []
    for f in ("css/home.css", "css/globe.css", "css/kompas-ui.css"):
        s = (ROOT / f).read_text(encoding="utf-8")
        if BEGIN in s: s = s.split(BEGIN)[0]
        css.append(s)
    seen = set()
    for f in files:
        s = (ROOT / f).read_text(encoding="utf-8")
        if "css/kompas-ui.css" not in s: continue
        for b in re.findall(r"<style[^>]*>(.*?)</style>", s, re.S):
            if b not in seen:
                seen.add(b); css.append(b)
    return css

def main():
    sources = collect_sources()
    # 1) oʻzgaruvchilarni yigʻish va qaysilari "aylanishini" aniqlash
    varsout = {}
    allrules = []
    for c in sources:
        rules = tinycss2.parse_stylesheet(c, skip_whitespace=True, skip_comments=True)
        for r in rules:
            if r.type == "qualified-rule" and tinycss2.serialize(r.prelude).strip().startswith(":root"):
                for d in tinycss2.parse_declaration_list(r.content, skip_whitespace=True, skip_comments=True):
                    if d.type == "declaration" and d.name.startswith("--"):
                        val = tinycss2.serialize(d.value).strip()
                        ORIG.setdefault(d.name, val)
                        dv = dark_var(d.name, val)
                        if dv:
                            varsout.setdefault(d.name, dv)
                            p = parse_color(val) if COLOR_RE.fullmatch(val) else None
                            if p:
                                (FLIPPED_DARK if lum(p[0]) < 0.35 else FLIPPED_LIGHT).add(d.name)
        allrules.append(rules)
    out = []
    for rules in allrules:
        process_rules(rules, out, varsout)
    # takrorlarni olib tashlash (tartibni saqlab)
    seen, uniq = set(), []
    def key(x): return x[0] + "{" + (x[1] if isinstance(x[1], str) else repr(x[1])) + "}"
    for x in out:
        k = key(x)
        if k not in seen: seen.add(k); uniq.append(x)
    lines = [BEGIN, "/* Qoʻlda tahrirlamang. Mavzu: html[data-theme] (js/kompas-ui.js qoʻyadi). */"]
    root = ["color-scheme:dark"]
    for n in sorted(FLIPPED_DARK | FLIPPED_LIGHT):
        root.append("--ko%s:%s" % (n[1:], ORIG[n]))
    for n, v in sorted(varsout.items()):
        root.append("%s:%s" % (n, v))
    lines.append("%s{%s}" % (P, ";".join(root)))
    lines.append("%s body{background:var(--bg,%s)}" % (P, DARK_BG_BASE))
    def emit(items, ind=""):
        for sel, body in items:
            if isinstance(body, str): lines.append("%s%s{%s}" % (ind, sel, body))
            else:
                lines.append("%s%s{" % (ind, sel)); emit(body, ind + "  "); lines.append(ind + "}")
    emit(uniq)
    # Qoʻlda qoʻshimchalar: generator topa olmaydigan joylar
    lines.append(EXTRA)
    lines.append(END)
    s = KUI.read_text(encoding="utf-8")
    if BEGIN in s: s = s.split(BEGIN)[0].rstrip() + "\n"
    s = s.rstrip() + "\n\n" + "\n".join(lines) + "\n"
    KUI.write_text(s, encoding="utf-8")
    print("tungi rejim:", len(uniq), "qoida,", len(varsout), "oʻzgaruvchi ->", KUI.relative_to(ROOT))

EXTRA = r'''/* qoʻlda */
html[data-theme="dark"] .nav,html[data-theme="dark"] .kl-tabbar{background:rgba(15,21,18,.9)}
html[data-theme="dark"] .dark,html[data-theme="dark"] section.dark{background:#16261f}
html[data-theme="dark"] footer{background:#0a0f0c}
html[data-theme="dark"] img.i3d,html[data-theme="dark"] .st-i{filter:none}
html[data-theme="dark"] input,html[data-theme="dark"] select,html[data-theme="dark"] textarea{background-color:var(--surface);color:var(--text);border-color:var(--border)}
html[data-theme="dark"] ::placeholder{color:var(--muted2)}
html[data-theme="dark"] #globus canvas{filter:brightness(.8) contrast(1.05)}
html[data-theme="dark"] .k4x-trav circle:first-child{fill:#f4f3ef}
html[data-theme="dark"] .k4x-bg{background-image:radial-gradient(circle at 1px 1px,rgba(159,208,182,.14) 1px,transparent 1.6px),radial-gradient(ellipse 60% 50% at 15% 30%,rgba(159,208,182,.06),transparent 70%),radial-gradient(ellipse 50% 45% at 85% 70%,rgba(224,135,79,.07),transparent 70%)}
html[data-theme="dark"] .k4x-s.on:not(.later) .k4x-dot{background:#2d4a3e;color:#fff}
.kl-theme{display:inline-flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:10px;border:1px solid var(--border,#e0e8e2);background:var(--surface,#fff);color:var(--text,#1a2e26);cursor:pointer;font-size:16px;line-height:1;flex:none;padding:0}
.kl-theme:hover{border-color:var(--accent,#2d4a3e)}
.kl-theme svg{width:18px;height:18px}
.kl-theme-float{position:fixed;left:14px;bottom:14px;z-index:300;box-shadow:0 4px 14px rgba(0,0,0,.18)}
header.top .kl-theme{margin-left:auto;margin-right:8px}
'''

if __name__ == "__main__":
    main()
