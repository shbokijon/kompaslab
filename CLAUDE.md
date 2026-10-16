# Kompas Lab — loyiha qoʻllanmasi (har yangi chat shu fayldan boshlaydi)

kompaslab.uz: xorijda oʻqish, stipendiya va rasmiy mehnat yoʻllariga oʻzbek tilida tayyorlov platformasi.
Shior: **"Kuzatuvdan kashfiyotga"**. Egasi: shbokijon@gmail.com (yagona admin).

## Muloqot qoidalari
- Javob **oʻzbek tilida**, qisqa, aniq; kirish va maqtov soʻzlarisiz.
- **Faktlar faqat manba bilan** (havola + sana). Maʼlumot yoʻq boʻlsa, toʻqima; "tekshirilmagan" deb yoz. Strategik masalada ishonchni foizda ber.
- **Soxta raqam yoʻq**: statistika, sharh, natija oʻylab topilmaydi. Jonli hisoblar 10 dan kam boʻlsa koʻrsatilmaydi.
- Atamalar: avval oʻzbekcha, keyin qavsda inglizcha. Oʻzbek apostrofi: `oʻ`, `gʻ` (U+02BB), `ʼ` (U+02BC).
- Foydalanuvchi odatda tayyor ishni darhol saytga chiqarishni kutadi. Pul, toʻlov, maʼlumotlar bazasi xavfsizligi yoki maʼlumot oʻchirishga oid ishlarda avval soʻra.

## Texnologiya va joylash
- Statik HTML/CSS/JS (framework yoʻq). Hosting: **Vercel** (project `prj_nY8UONOz7o0SHFbUFG264N0ISRZX`, team `team_8uGplJ2cOUVP74ZZ4DDHMsQ2`). `kompaslab.uz` → `www.kompaslab.uz`.
- GitHub `shbokijon/kompaslab`, **`main` → production** avtomatik (~1 daqiqa).
- Ish tartibi: `git checkout -b claude/<ish> origin/main` → commit → `git push -u origin claude/<ish>` → saytga: `git merge-base --is-ancestor origin/main HEAD && git push origin HEAD:main` → Vercel MCP `list_deployments` (target production) bilan READY ni tekshir.
- **Supabase** project `usxpkmbjrdllnitlzdpq`. Anon kalit ochiq (`js/config.js`). Muhim jadvallar: `profiles` (role student/admin), `courses` (slug, price_yearly, price_monthly, status), `waitlist`, `enrollments`, `payments`, `site_visits`, `pwa_events`. RPC: `kompas_public_stats()` (anon), `kompas_track_visit(p_vid)`, `kompas_pwa_event(...)`, `kompas_pwa_stats()` (admin), `fn_is_admin()`.
- `supabase-js` doim **2.45.4** ga mahkamlangan (jsdelivr UMD).
- `tools/`, `supabase/`, `schema.sql` saytga chiqmaydi (`.vercelignore`).

## Fayl xaritasi
| Fayl | Nima | Qanday tahrirlanadi |
|---|---|---|
| `index.html` | Bosh sahifa (v5: jonli hisob, kalkulyator, animatsiyalar) | **Qoʻlda**. Generator uni faqat `--index` bilan yozadi (eskirgan, ishlatma) |
| `*-lab.html`, `tadbirkor-talaba.html` | Lab sahifalari | **Generator**: `python3 tools/landing/build.py` (`labs_data.py`, `mods.json`, `render.py` + `postprocess.py`). HTML ni toʻgʻridan-toʻgʻri tahrirlasang, keyingi yaratishda yoʻqoladi |
| `*-m0.html`, M1/M2 | Interaktiv modullar | **`tools/modules/`** (pastda). `master-lab-m0.html` manbasiz — toʻgʻridan-toʻgʻri tahrirlanadi |
| `dashboard.html`, `lesson.html` | Talaba kabineti; dars pleyeri (hozir demo maʼlumot) | Qoʻlda. `dashboard.html` dagi `M0_LIST` — M0 kartochkalari |
| `admin.html` | Admin panel (roʻyxatdan oʻtganlar, CSV, narxlar, analitika) | Qoʻlda |
| `login.html`, `register.html`, `payment.html` | Kirish; toʻlov (**yopiq**, Click/Payme ulanmagan) | Qoʻlda |
| `js/config.js` | Supabase mijozi `window.supabase` | — |
| `js/live-bar.js` | Tepadagi panel: hozir saytda, roʻyxatdan oʻtganlar, bugun/hafta/oy/yil tashriflari | — |
| `js/protect.js` | Nusxa olishni cheklash + "kompaslab.uz" suv belgisi (faqat kirganlarga) | — |
| `js/pwa.js`, `sw.js`, `manifest.webmanifest`, `offline.html` | Telefonga oʻrnatish (PWA), oflayn | Rasm/CSS keshini hammaga yangilash: `sw.js` dagi `V = "kl-v1"` ni oshir |
| `css/brand.css` | Logotip komponenti `.klogo` va animatsiyasi | — |
| `img/brand/` | Logotip, favicon, ikonkalar, `og.jpg` | `python3 tools/brand/make_logo.py` |
| `img/3d/*.webp` | 3D ikonkalar (bachelor, bell, books, bulb, calendar, chart, compass, daad, gks, hourglass, lock, master, memo, miya, money, musofir, phd, scroll, seedling, shield, telescope, tt, usa) | — |

## Modullar (`tools/modules/`)
- Manba: `src/<nom>.src.html` (`{{CSS}}` oʻrniga `m0.css`). Yigʻish: `python3 tools/modules/build.py [nom]`.
  - sayt versiyasi → repo ildizida `<nom>.html` (config.js, live-bar, protect, logotip, PWA, darvoza)
  - yuklab olinadigan → `tools/modules/dist/<nom>.html` (rasmlar ichida; git'ga kirmaydi). Foydalanuvchiga `SendUserFile` bilan yuboriladi.
- Yangi modul: eng yaqin manbadan nusxa ol → `build.py` dagi `MODULES` ga qoʻsh → yigʻ → tekshir → Lab sahifasi va dashboard'ga bogʻla.
- Tekshiruv: `python3 -m http.server 8814 &` keyin `PW=$(npm root -g)/playwright node tools/modules/test/smoke.js <nom>` (JS xatosi, 390px, darvoza, 1-dars +XP; sayt va dist).
- Sandbox'dan Supabase va jsdelivr ochilmaydi: Playwright'da `route` bilan mock qilinadi (smoke.js ga qara).

### Modul andozasi (hamma modulda bir xil)
- Geymifikatsiya: **250 XP**, 3 daraja (Kuzatuvchi 0 → Izlanuvchi 80 → Kashfiyotchi 170 → yakun 250), yoʻl xaritasi, 6 ta nishon, toast, konfetti; `prefers-reduced-motion` hurmat qilinadi.
- Har dars 4 qism: **Diqqat 🔥 / Asosiy qism / Xulosa / Topshiriq**; 4 tasi ochilmaguncha dars yakunlanmaydi.
- Javoblar faqat `localStorage` da: kalit `kompas_<lab>_m0_v1` (masalan `kompas_usa_m0_v1`).
- Oxirida avtomatik yigʻiladigan **Qaror va rozilik** bayonoti (18+, toʻlov qaytarilmasligi, Kompas vositachi emas).
- **Tayyorgarlik koʻrsatkichi (Readiness Score)** Lab sahifasidagi test bilan **aynan bir xil** (ogʻirliklar, 70/45 chegaralari, "x" bloklovchi javoblar).
- Narxlar `kompas_public_stats().prices[slug]` dan jonli olinadi (`data-py`, `data-pm`); HTML dagi raqam zaxira.
- Faktlar bloki: "Tekshirildi / Rasmiy / Ehtiyot" belgisi, sana va havola.
- Kirish darvozasi: sayt versiyasida faqat roʻyxatdan oʻtganlar (va admin); `file://` da ochiq. **Istisno: Musofir M0 hamma uchun ochiq**, himoyasiz, ulashish tugmasi bor.

### Holat (2026-10-17)
| Lab | Slug | Modullar (darslar) | Tayyor |
|---|---|---|---|
| Bachelor | bachelor-lab | 17 (86) | M0 saytda |
| Master | master-lab | 9 (59) | M0 saytda; M1, M2 faqat yuklab olinadigan (`dist/`) |
| PhD | phd-lab | `phd-lab.html` ga qara | M0 saytda |
| GKS | gks-lab | 12 (54) | M0 saytda |
| USA | usa-lab | 12 (72) | M0 saytda |
| DAAD | daad-lab | 9 (51) | M0 yoʻq |
| Tadbirkor Talaba | tadbirkor-talaba | 10 (54) | M0 saytda |
| Musofir | miggo | 8 (44) | M0 saytda (ochiq) |
Modul va dars nomlari: `tools/landing/mods.json` (DAAD: `labs_data.py` → `DAAD_MODS`).

## Ochiq masalalar (foydalanuvchi qarori kutilmoqda)
1. **Xavfsizlik:** `fn_mark_payment_paid`, `fn_set_module_access`, `fn_upsert_lesson_content` anon/authenticated tomonidan chaqirilishi mumkin (ichida ruxsat tekshiruvi yoʻq yoki yetarli emas). Toʻlov ochilishidan oldin `revoke execute` qilinishi shart. Foydalanuvchi hali tasdiqlamagan.
2. **Toʻlov:** Click/Payme merchant maʼlumotlari yoʻq; `payment.html` yopiq va eskirgan (karta raqamini oʻzi soʻraydi — PCI DSS ga zid). Toʻgʻri yoʻl: provayderning oʻz sahifasiga yoʻnaltirish + webhook.
3. Ommaviy oferta va maxfiylik siyosati sahifasi yoʻq ("toʻlov qaytarilmaydi" qoidasi uchun kerak).
4. M0 progressi faqat brauzerda (qurilmalar orasida koʻchmaydi) — bazaga yozish rejada.
5. Mobil ilova: hozir PWA; doʻkon ilovasi signal boʻlganda (Android avval).
