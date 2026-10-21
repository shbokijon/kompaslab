# sitemap.xml ni qayta yaratadi: ochiq (kirishsiz) sahifalar.
# Roʻyxatdan oʻtganlar uchun M0 (darvozali) sahifalar kiritilmaydi; Musofir M0 ochiq.
# Ishga tushirish: python3 tools/site/sitemap.py
import datetime, re
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
SKIP = {"admin", "dashboard", "lesson", "login", "register", "reset-password", "payment", "offline", "globe-demo"}
today = datetime.date.today().isoformat()
urls = []
for p in sorted(ROOT.glob("*.html")):
    n = p.stem
    if n in SKIP:
        continue
    s = p.read_text(encoding="utf-8")
    if 'name="robots" content="noindex' in s or '<body class="locked"' in s:
        continue
    urls.append("" if n == "index" else n)
urls.sort(key=lambda u: (u != "", u))
xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f"  <url><loc>https://www.kompaslab.uz/{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n"
(ROOT / "sitemap.xml").write_text(xml, encoding="utf-8")
print(len(urls), "URL")
