# Kompas Lab landing sahifalarini qayta yaratish.
# Ishga tushirish (repo ildizidan): python3 tools/landing/build.py
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from render import page, ROOT
from labs_data import LABS, DAAD_MODS

mods = json.loads((HERE / "mods.json").read_text(encoding="utf-8"))
mods["DAAD"] = DAAD_MODS
for key, lab in LABS.items():
    lab["key"] = key
    html = page(lab, mods[key])
    (ROOT / lab["file"]).write_text(html, encoding="utf-8")
    print(lab["file"], len(html), sum(len(m["lessons"]) for m in mods[key]))

import gen_index, phd_polish
gen_index.build()
phd_polish.build()
