# PhD Lab v4 (2026-10-31): Lab sahifasidagi dastur blokini modul manbalaridan yangilaydi.
#   python3 tools/modules/phd/landing.py   →  tools/landing/phd_source.html (keyin: python3 tools/landing/build.py)
# M0 darslari: tools/modules/src/phd-lab-m0.src.html; M1–M8: tools/modules/phd/mods/m<N>.py.
import html, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
import engine  # noqa: E402

SRC = ROOT / "tools/landing/phd_source.html"

M0 = dict(title="PhD yoʻli menga mosmi?", art="PhD qaror kartasi: Tayyorgarlik koʻrsatkichi, vaqt chizigʻi, 30 kunlik reja va rozilik qaydi",
          lessons=[("PhD nima va kim uchun?", "Mustaqil tadqiqot va unga masʼuliyat; kuchli va xavfli motivlar; PhD viza yoki ish kafolati emas; muqobil yoʻllar"),
                   ("Doktorantura yoʻllari xaritasi", "Rahbar atrofidagi model, tuzilmali doktorlik maktabi, maoshli PhD; har eʼlonda: kim daraja beradi, kim toʻlaydi, kim rahbar"),
                   ("Tayyorgarlikni halol baholash", "7 yoʻnalishli koʻrsatkich; taxmin va dalilni ajratish; koʻrsatkich qabul ehtimoli emas, muvofiqlik alohida tekshiriladi"),
                   ("Xavflar, moliya va oilaviy qaror", "Tadqiqot, vaqt, oila va moliya xavflari; “faqat moliyalashtirilgan” qoidasi; oʻz hisobidan PhD xarajat kalkulyatori"),
                   ("Shaxsiy yoʻl kartasi va birinchi qadam", "12–18 oylik teskari reja, mos emas roʻyxati, toʻlov shartlari, 30 kunlik reja va rozilik")])
PH = [("FAZA 0 · BEPUL", "Qaror", "M0"), ("FAZA I", "Yoʻnalish va tanlov", "M1–M2"), ("FAZA II", "Rahbar va loyiha taklifi", "M3–M4"),
      ("FAZA III", "Hujjatlar va moliya", "M5–M6"), ("FAZA IV", "Ariza va boshlash", "M7–M8")]


def strip(s):
    return html.unescape(re.sub(r"<[^>]+>", "", engine.fix(s))).strip()


def mod_html(n, title, art, lessons, free=False):
    li = "\n".join(f'          <li><span class="num">{n}.{k}</span>{html.escape(t)}<small>{html.escape(d)}</small></li>' for k, (t, d) in enumerate(lessons, 1))
    tag = '<span class="tag tag-free">BEPUL</span>' if free else ""
    cls = "mod free reveal" if free else "mod reveal"
    op = " open" if free else ""
    return (f'      <details class="{cls}"{op}>\n        <summary><div class="mod-n">M{n}</div><div><div class="mod-t">{html.escape(title)}</div>'
            f'<div class="mod-a">Natija: {html.escape(art)}</div></div><div class="mod-c">{len(lessons)} dars{tag}</div></summary>\n        <ol>\n{li}\n        </ol>\n      </details>')


def main():
    mods = [mod_html(0, M0["title"], M0["art"], M0["lessons"], True)]
    counts = {0: len(M0["lessons"])}
    for n in range(1, 9):
        M = engine.load(str(n))
        les = [(strip(L["t"]), strip(L["take"])) for L in M["lessons"]]
        counts[n] = len(les)
        mods.append(mod_html(n, strip(M["title"]), strip(M["art_title"]), les))
    total = sum(counts.values())
    s = SRC.read_text(encoding="utf-8")
    a = s.index('    <div class="mods">'); b = s.index("<!-- TESKARI REJA -->")
    tail = s[a:b]; end = tail.rindex("    </div>\n  </div>\n</section>")
    s = s[:a] + '    <div class="mods">\n' + "\n".join(mods) + "\n" + tail[end:] + s[b:]
    weeks = {"M0": "1 hafta", "M1–M2": "4–5 hafta", "M3–M4": "5–7 hafta", "M5–M6": "3–4 hafta", "M7–M8": "3–6 hafta"}
    def cnt(r):
        if r == "M0": return counts[0]
        x, y = [int(v) for v in r.replace("M", "").split("–")]
        return sum(counts[i] for i in range(x, y + 1))
    ph = "\n".join(f'      <div class="phase"><small>{a_}</small><b>{b_}</b><span>{r} · {cnt(r)} dars · {weeks[r]}</span></div>' for a_, b_, r in PH)
    s = re.sub(r'    <div class="phases reveal">\n.*?\n    </div>', lambda m: '    <div class="phases reveal">\n' + ph + "\n    </div>", s, count=1, flags=re.S)
    s = re.sub(r"\b\d+ dars, <em>4 faza", f"{total} dars, <em>4 faza", s)
    s = re.sub(r"9 modul, \d+ dars", f"9 modul, {total} dars", s)
    s = re.sub(r'<span class="fact"><b>\d+</b> dars</span>', f'<span class="fact"><b>{total}</b> dars</span>', s)
    SRC.write_text(s, encoding="utf-8")
    print("phd_source.html:", total, "dars", counts)


if __name__ == "__main__":
    main()
