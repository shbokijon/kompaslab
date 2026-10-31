# PhD Lab sahifasi alohida shablondan qurilgan (phd_source.html).
# Bu skript unga umumiy dizayn qatlami, narx, qaytarish qoidasi va jonli maʼlumotni qoʻllaydi.
import re
from render import six_card, calc_html, MONTHLY_EXTRA, BASE_CSS, EXTRA_CSS, POLISH_CSS, ROOT, HERE, WHO_CARD, REFUND, FOOTER, LIVE_JS, WHY_LAB_FAQ, PRO_PLANNED, HONEST_NOTE, icon, polish, uz_fix, fmt

Y, M = 999000, 129000

def R(s, a, b, n=1, opt=False):
    c = s.count(a)
    if opt and c == 0:
        return s
    assert c == n, (a[:70], c)
    return s.replace(a, b)

def build():
    s = (HERE / "phd_source.html").read_text(encoding="utf-8")
    s = re.sub(r"<style>.*?</style>", lambda m: "<style>" + BASE_CSS + EXTRA_CSS + POLISH_CSS + "</style>", s, count=1, flags=re.S)
    s = s.replace("family=Outfit:wght@300;400;500;600;700;800;900&family=Caladea:ital,wght@0,400;0,700;1,400;1,700&family=JetBrains+Mono:wght@400;600", "family=Outfit:wght@400;500;600;700;800;900&family=Caladea:ital,wght@0,400;0,700;1,400;1,700&family=JetBrains+Mono:wght@400;600;700;800")
    s = R(s, '<div class="logo-m">🧭</div><span class="logo-t">Kompas Lab <span>· PhD</span></span>', '<div class="logo-m"><img src="img/3d/compass.webp" alt="" width="34" height="34"></div><span class="logo-t">Kompas Lab <span>PhD</span></span>')
    s = R(s, '<a href="#asoschi">Asoschi</a>', '<a href="#qanday">Qanday tuzilgan</a>')
    # "Ochiq gap": natija va kafolat boʻyicha umumiy izoh (render.HONEST_NOTE)
    s = R(s, "<li>\"PhD kafolati\" izlayotganlar — bunday kafolat yoʻq</li>\n        </ul>\n      </div>\n    </div>",
          "<li>\"PhD kafolati\" izlayotganlar — bunday kafolat yoʻq</li>\n        </ul>\n      </div>\n    </div>\n    <p class=\"honest\">" + HONEST_NOTE + "</p>")
    s = s.replace("🔔 Kutish roʻyxati", "Kutish roʻyxati").replace("Ochilganda xabar</button>", "Ochilganda xabar bering</button>")
    s = R(s, '<div class="badge">⚗️ PhD Lab · v3.1</div>', icon("phd", "hero-i float", "PhD Lab"))
    s = R(s, '<div class="facts">', '<div class="facts">', 1)
    # asoschi boʻlimi: ism va EYUF olib tashlanadi, jadval qoladi
    a = s.index('<section class="alt" id="asoschi">')
    b = s.index("<!-- NARX -->")
    sec = s[a:b]
    sec = re.sub(r'<div class="f-card reveal">.*?</ul>\s*</div>', WHO_CARD, sec, count=1, flags=re.S)
    sec = sec.replace('id="asoschi"', 'id="qanday"').replace('class="wrap founder"', 'class="wrap method"')
    sec = R(sec, "<h2>Faqat oʻzim oʻtgan <em>yoʻlni oʻrgataman.</em></h2>", "<h2>Shaxsiy tajriba qayerda bor va qayerda yoʻq</h2>")
    sec = R(sec, "Men hozir PhDʼning birinchi yilidaman. Shuning uchun dastur qamrovi tajribam bilan chegaralangan va bu ochiq yoziladi.", "Asoschi hozir PhDʼning birinchi yilida. Shuning uchun dastur qamrovi uning tajribasi bilan chegaralangan va bu ochiq yoziladi.")
    sec = R(sec, "<tr><td>El-yurt umidi tanlovi va intervyusi</td><td class=\"y\">Ha</td><td>Toʻliq; raqamlar rasmiy manbadan</td></tr>\n", "", opt=True)
    s = s[:a] + sec + s[b:]
    s = R(s, "El-yurt umidi: asoschi tajribasi<small>Tanlov bosqichlari mantigʻi, hujjatlar, intervyuga tayyorgarlik — asoschining 2025-yil 2-tanlov tajribasi; kvota, yosh va til talablari faqat Qobiqʼda, rasmiy sahifadan</small>",
          "El-yurt umidi: tanlov bosqichlari<small>Tanlov bosqichlari mantigʻi, hujjatlar, intervyuga tayyorgarlik; kvota, yosh va til talablari faqat Qobiqʼda, rasmiy sahifadan</small>", opt=True)
    s = R(s, "El-yurt umidi paneli (asoschi tajribasi) va boshqa panellar mantigʻi;", "El-yurt umidi va boshqa stipendiya panellari mantigʻi;", opt=True)
    s = R(s, "Darsda asoschining 2025-yil 2-tanlov tajribasi; yosh, til va kvota faqat rasmiy sahifadan.", "Yosh, til va kvota faqat rasmiy sahifadan.", opt=True)
    # narx
    s = R(s, "<h2>Obuna asosida. <em>M0 bepul.</em></h2>", "<h2>Obuna: oylik, 6 oylik yoki yillik. M0 bepul.</h2>")
    s = R(s, '<div class="price">999 000</div><div class="per">soʻm · 12 oy</div>', f'<div class="price" data-py="phd-lab">{fmt(Y)}</div><div class="per">soʻm, 12 oy uchun</div>')
    s = R(s, '<div class="price">129 000</div><div class="per">soʻm · har oy uzaytiriladi</div>', f'<div class="price" data-pm="phd-lab">{fmt(M)}</div><div class="per">soʻm, har oy</div>')
    s = R(s, '<div class="price">0</div><div class="per">soʻm · muddatsiz</div>', '<div class="price">0</div><div class="per">soʻm, muddatsiz</div>')
    s = s.replace("<li>Istalgan oy bekor qilinadi</li>", "<li>Istalgan oy toʻxtatiladi</li>")
    # Tartib: M0, Oylik, 6 oylik (asosiy, narx bazada boʻlsa), Yillik — render.pricing bilan bir xil
    a = s.index('      <div class="plan main reveal">')
    blk = s[a:s.index('    <div class="calc', a)]
    y_card = blk[:blk.index('      <div class="plan reveal">')]
    m_card = blk[blk.index('      <div class="plan reveal">'):blk.rindex('    </div>')]
    y_card = y_card.replace('<div class="plan main reveal">\n        <span class="tag-top">Asosiy reja</span>\n', '<div class="plan reveal">\n').replace('class="btn btn-p" data-wl', 'class="btn btn-g" data-wl')
    m_card = m_card.replace("<li>Barcha modullar, obuna faol ekan</li>", "<li>Bir oylik kirish</li>").replace("</ul>", "".join(f"<li>{x}</li>" for x in MONTHLY_EXTRA) + "</ul>", 1)
    s_card = "      " + six_card("phd-lab", "Kutish roʻyxati", "plan main reveal") + "\n"
    s = s[:a] + m_card + s_card + y_card + blk[blk.rindex('    </div>'):] + s[a + len(blk):]
    calc = calc_html(Y, M, "phd-lab")
    s = re.sub(r'<div class="calc reveal">.*?</div>\s*</div>', '<div class="calc">' + calc + "</div>\n    " + PRO_PLANNED + "\n    <div class=\"refund\">" + REFUND + "</div>", s, count=1, flags=re.S)
    s = R(s, "<div><b>Bekor qilish</b>Obuna istalgan vaqtda bekor qilinadi; toʻlangan davr oxirigacha kirish saqlanadi. Qaytarish shartlari toʻlovdan oldin toʻliq matnda koʻrsatiladi.</div>",
          "<div><b>Bekor qilish</b>Avtomatik yechish yoʻq: har davr uchun oʻzingiz toʻlaysiz. Toʻlamasangiz, toʻlangan davr tugashi bilan kirish yopiladi.</div>")
    s = s.replace("<h3>M0 — Qaror darvozasi</h3>", "<h3>M0, qaror moduli</h3>")
    # savollar: «Nega Lab?»
    q, a2 = WHY_LAB_FAQ
    i = s.index('<div class="faq')
    j = s.index("</div>", s.rindex("</details>", i, s.index("</section>", i)))
    s = s[:j] + f"<details><summary>{q}</summary><p>{a2}</p></details>\n    " + s[j:]
    # footer
    s = re.sub(r"<footer>.*?</footer>", FOOTER, s, count=1, flags=re.S)
    # CTA tugmalari
    s = s.replace("💬 Telegramʼda soʻrash", "Telegramda savol berish").replace("💬 Telegram'da so'rash", "Telegramda savol berish")
    # jonli narx va kutish roʻyxati
    s = R(s, "</body>", "<script>\n(function () {\n" + LIVE_JS + "})();\n</script>\n</body>")
    s = s.replace('<div class="facts">', '<div class="facts">', 1)
    k = s.index("</div>", s.index('<div class="facts">'))
    s = s[:k + 6] + '\n      <div class="live" data-live-wl="phd-lab"><i></i><span></span></div>' + s[k + 6:]
    s = s.replace(' class="reveal"', "").replace(" reveal\"", "\"")
    out = uz_fix(polish(s))
    (ROOT / "phd-lab.html").write_text(out, encoding="utf-8")
    print("phd-lab.html", len(out))

if __name__ == "__main__":
    build()
