# Umumiy dars kutubxonasi (gks/lib/v1.py … v8.py) dan darslarni olish.
# les(4, 3, t="Yangi sarlavha") → v4 dagi 3-dars nusxasi, berilgan maydonlar almashtirilgan.
import importlib.util, sys
from pathlib import Path

LIB = Path(__file__).resolve().parent.parent / "lib"
_cache = {}


def lib(n):
    if n not in _cache:
        spec = importlib.util.spec_from_file_location(f"gkslib{n}", LIB / f"v{n}.py")
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        _cache[n] = m.MOD
    return _cache[n]


def les(n, k, **kw):
    d = dict(lib(n)["lessons"][k - 1])
    d.setdefault("quiz", None)
    d.update(kw)
    return d


def body(n, k):
    return lib(n)["lessons"][k - 1]["body"]
