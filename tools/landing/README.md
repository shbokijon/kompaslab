# Landing sahifalari: qanday tahrirlanadi

Sahifalar qoʻlda emas, shu papkadagi fayllardan yaratiladi. HTML faylni toʻgʻridan-toʻgʻri tahrirlasangiz, keyingi yaratishda oʻzgarish yoʻqoladi.

| Nimani oʻzgartirasiz | Qayerda | Saytga qachon chiqadi |
|---|---|---|
| Narx (yillik, oylik) | Supabase → Table Editor → `courses` → `price_yearly`, `price_monthly` (va toʻlov uchun `price`) | Darhol: sahifa narxni bazadan oʻqiydi. Bu yerdagi raqam faqat zaxira |
| Lab sahifasi matni, modullar, savollar | `labs_data.py` (Lablar), `mods.json` (modul va dars nomlari) | `build.py` ishga tushirilib, commit qilingandan keyin (~1 daqiqa, Vercel) |
| Bosh sahifa matni, katalog | `gen_index.py` | Shunday |
| PhD Lab sahifasi | `phd_source.html` + `phd_polish.py` | Shunday |
| Dizayn (rang, shrift) | `base.css`, `render.py` dagi `POLISH_CSS` | Shunday |

Yaratish: repo ildizidan `python3 tools/landing/build.py`.

Qoidalar:
- Kodda faqat qoʻsh qoʻshtirnoq (`"`). Matndagi `'` avtomatik ravishda `ʻ` (oʻ, gʻ) yoki `ʼ` ga aylanadi.
- Atamalar: avval oʻzbekcha, keyin qavsda inglizcha. `render.py` dagi `TERMS` roʻyxati "Readiness Score" kabi atamalarni avtomatik tuzatadi.
- Jonli hisob (roʻyxatdan oʻtganlar, kutish roʻyxati) 10 dan kam boʻlsa koʻrsatilmaydi: `LIVE_MIN` (`render.py`).
- `tools/` papkasi saytga chiqmaydi (`.vercelignore`).
