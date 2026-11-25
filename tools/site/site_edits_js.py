#!/usr/bin/env python3
"""js/kompas-ui.js dagi sayt tahrirlari blokini (// <site-edits> … // </site-edits>)
js/site-edits.js ga koʻchiradi. Bu fayl kompas-ui.js yuklamaydigan sahifalarga ulanadi
(kirish, roʻyxatdan oʻtish, kabinet va b.), shunda Admin → Vebsayt hamma sahifada ishlaydi.
Ishlatish: python3 tools/site/site_edits_js.py [--check]"""
import pathlib, re, sys
R = pathlib.Path(__file__).resolve().parents[2]
src = (R / "js/kompas-ui.js").read_text(encoding="utf-8")
m = re.search(r"^// <site-edits>\n(.*?)^// </site-edits>\n", src, re.S | re.M)
if not m:
    sys.exit("kompas-ui.js da // <site-edits> belgilari topilmadi")
out = ("// AVTOMATIK: js/kompas-ui.js dagi <site-edits> bloki nusxasi. Qoʻlda tahrirlamang:\n"
       "// python3 tools/site/site_edits_js.py\n" + m.group(1))
dst = R / "js/site-edits.js"
if "--check" in sys.argv:
    ok = dst.exists() and dst.read_text(encoding="utf-8") == out
    print("site-edits.js mos" if ok else "site-edits.js ESKIRGAN: skriptni ishga tushiring")
    sys.exit(0 if ok else 1)
dst.write_text(out, encoding="utf-8")
print("yozildi:", dst.relative_to(R), len(out), "belgi")
