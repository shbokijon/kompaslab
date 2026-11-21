# Bakalavr v2 (2026-11-21): eski 16 modul (mods_v1/) darslarini yangi 8 modulga yigʻish uchun yordamchi.
# Eski matn amaldagi alifboda va oddiy apostrof bilan (engine.fix() oʻgiradi).
# Eski dars matni (body) yangi darsda ⓘ "Batafsil" ostiga oʻtadi (info_old); modul havolalari yangi raqamga.
import importlib.util, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
_C = {}

# eski modul → yangi modul (32-hujjat, 5-bölim)
NEW = {1: 1, 2: 1, 3: 3, 4: 2, 5: 2, 6: 3, 7: 3, 8: 4, 9: 5, 10: 5, 11: 6, 12: 6, 13: 7, 14: 7, 15: 8, 16: 8}

# 32-hujjat, 3-bölim: eski matndagi LLM izlari (ⓘ ostida qoladigan qism uchun)
FIXES = [
    ("Kompas Lab'ning yondashuvi: mamlakat bo'yicha emas, soha bo'yicha kuchli joyni izlash.",
     "Avval soha bo'yicha kuchli universitetlarni toping, keyin mamlakatni tanlang."),
    ("Asbob emas, haftalik yangilash odati muhim.", "Jadvalni har hafta bir xil kunda 10 daqiqa yangilang."),
    ("U ariza emas, lekin barcha insholar va intervyu uchun asos bo'ladi.", "Bu bayon insho va intervyu uchun xomashyo: bir sahifa, oddiy til."),
    ("Bayon yuqori ilmiy ish emas. ", ""),
    ("Varaqa faktlar beradi, matn emas. O'qituvchi o'z so'zlari bilan yozadi.", "Varaqaga faqat fakt yozing. Xatni o'qituvchi o'z so'zlari bilan yozadi."),
    ("<b>Eng muhimini birinchi qo'ying</b>: tartib muhimlik bo'yicha.", "<b>Eng muhim faoliyat</b> ro'yxat boshida tursin."),
    ("Yechim taklifini emas, muammoni qabul qiling; yechimni o'zingiz toping.", "Ular qayerda qiynalganini aytsin, qanday tuzatishni o'zingiz hal qilasiz."),
    ("Javobni yod olmang, tuzilmasini yod oling.", "Tuzilmani yodlang, jumlani har safar yangidan tuzing."),
    ("O'zaro tahrir fikr beradi, matn emas.", "O'zaro tahrirdan fikr olasiz, matnni o'zingiz yozasiz."),
    ("Kompas freymvorki: ", "Tuzilma: "),
    ("Kompas Lab tavsiya etadigan tuzilma: ", "Qulay tuzilma: "),
]


def mod(n):
    if n not in _C:
        spec = importlib.util.spec_from_file_location("bach_v1_m%d" % n, HERE / "mods_v1" / ("m%d.py" % n))
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        _C[n] = m.MOD
    return _C[n]


def _refs(t, cur):
    def rng(m):
        a, b = NEW[int(m.group(1))], NEW[int(m.group(2))]
        return "M%d" % a if a == b else "M%d–M%d" % (a, b)
    t = re.sub(r"\bM(\d{1,2})[–-]M(\d{1,2})\b", rng, t)
    t = re.sub(r"\bM(\d{1,2}) L\d\b", lambda m: "M%d" % NEW[int(m.group(1))], t)
    t = re.sub(r"\bM(\d{1,2})(?:\.\d)?\b", lambda m: "M%d" % NEW.get(int(m.group(1)), int(m.group(1))), t)
    t = re.sub(r"\s?\(L\d\)", "", t)
    t = re.sub(r"\bL\d\b", "shu modul", t)
    t = t.replace("M%d da " % cur, "shu modulda ").replace("M%d dagi " % cur, "shu moduldagi ")
    return t


def clean(t, cur):
    for a, b in FIXES:
        t = t.replace(a, b)
    t = t.replace(" — ", ": ")
    return _refs(t, cur)


def les(cur, *refs, quiz=True):
    """Bir yoki bir nechta eski darsdan yangi dars: birinchisi asos (ic, kind, ph), body lar ⓘ ostiga."""
    parts = []
    base = None
    for n, k in refs:
        L = dict(mod(n)["lessons"][k - 1])
        if base is None:
            base = L
        parts.append((L["t"], clean(L["body"], cur)))
    out = dict(base)
    out.pop("body", None)
    if len(parts) == 1:
        out["info_old"] = parts[0][1]
    else:
        out["info_old"] = "".join("<h4>%s</h4>%s" % (t, b) for t, b in parts)
    q = None
    for n, k in refs:
        q = q or mod(n)["lessons"][k - 1].get("quiz")
    out["quiz"] = q if quiz else None
    if not out["quiz"] and "Mini-test" in out.get("kind", ""):
        alt = [mod(n)["lessons"][k - 1]["kind"] for n, k in refs[1:] if "Mini-test" not in mod(n)["lessons"][k - 1]["kind"]]
        out["kind"] = alt[0] if alt else "Tahlil"
    if out.get("ph"):
        out["ph"] = out["ph"].replace(" — ", ": ")
    return out


def fields(n, keys=None):
    F = mod(n)["tool"]["fields"]
    out = []
    for f in F:
        if keys is None or f["k"] in keys:
            f = dict(f)
            if f.get("ph"):
                f["ph"] = f["ph"].replace(" — ", ": ")
            out.append(f)
    return out
