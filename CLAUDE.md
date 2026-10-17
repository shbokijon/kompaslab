# Kompas Lab — loyiha qoʻllanmasi (har yangi chat shu fayldan boshlaydi)

kompaslab.uz: xorijda oʻqish, stipendiya va rasmiy mehnat yoʻllariga oʻzbek tilida tayyorlov platformasi.
Shior: **"Kuzatuvdan kashfiyotga"**. Egasi: shbokijon@gmail.com (yagona admin).

## Muloqot qoidalari
- Javob **oʻzbek tilida**, qisqa, aniq; kirish va maqtov soʻzlarisiz.
- **Faktlar faqat manba bilan** (havola + sana). Maʼlumot yoʻq boʻlsa, toʻqima; "tekshirilmagan" deb yoz. Strategik masalada ishonchni foizda ber.
- **Soxta raqam yoʻq**: statistika, sharh, natija oʻylab topilmaydi. Jonli hisoblar 10 dan kam boʻlsa koʻrsatilmaydi.
- Atamalar: avval oʻzbekcha, keyin qavsda inglizcha. Oʻzbek apostrofi: `oʻ`, `gʻ` (U+02BB), `ʼ` (U+02BC).
- **Shrift zaxirasi (2026-10-17):** DM Serif Display, Outfit va JetBrains Mono'da U+02BB yoʻq (DM Serif'da U+02BC ham yoʻq). Har sahifada asosiy shrift havolasidan keyin `IBM Plex Sans` + `Playfair Display` faqat `text=%CA%BB%CA%BC` (2 belgi) bilan yuklanadi va har `font-family` roʻyxatida ikkinchi oʻrinda turadi. Yangi sahifa yoki shrift qoʻshilsa, shu juftlikni saqla. JetBrains Mono ishlatilgan har sahifada yuklanishi shart.
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
| `login.html`, `register.html`, `reset-password.html`, `payment.html` | Kirish; roʻyxatdan oʻtish (taʼlim va maqsad `user_metadata` ga yoziladi); parolni tiklash (`/reset`); toʻlov (**yopiq**, Click/Payme ulanmagan) | Qoʻlda |
| `js/config.js` | Supabase mijozi `window.supabase` | — |
| `js/globe.js`, `css/globe.css`, `data/globe.json` | Bosh sahifadagi "Toshkentdan qayerga?" globusi (Canvas 2D, samolyot, chegaralar, shaharlar). Mamlakat→Lab roʻyxati `DEST` da (`c` — ob-havo olinadigan poytaxt). Qatlamlar: **Xarita / Ob-havo** (hozirgi, Open-Meteo Forecast API, kun-tun chizigʻi, yomgʻir/qor/chaqmoq effektlari) / **Iqlim** (oxirgi 12 toʻliq oy, Open-Meteo Historical API ERA5; saralash: issiq yoz ≥25°C, sovuq qish ≤0°C, yomgʻirli ≥1000 mm). Toʻliq ekran, aylanish tezligi/yoʻnalishi, tanlov `localStorage` `kompas_globe_v1`. Mamlakat tanlanganda samolyot Toshkentdan bir marta uchadi (kamera yoʻnalishni koʻrsatadi, qoʻngach yaqinlashadi; kartochkada "qayta uchish"). **Xarita qatlamida ob-havo/iqlim koʻrsatilmaydi va yuklanmaydi**; Ob-havo/Iqlim qatlamida mamlakat kartochkasida chiqadi; Open-Meteo CC BY 4.0 — manba havolasi sahifada qolishi shart. Prototip: `globe-demo.html` (noindex) | Maʼlumot: `tools/globe/build_globe.py` (Natural Earth 1:110m) |
| `js/journey.js` | Kabinetdagi "Mening yoʻlim": kompas (keyingi qadam), vaqt chizigʻi (Lab darslari / surʼat vs maqsad sanasi), hujjatlar javoni (M0 xp≥250, Master M1–M8 `done.fin`), haftalik ritm. Faqat localStorage (`kompas_journey_v1`) | Lab darslar soni `LABS` da qoʻlda |
| `js/live-bar.js` | Tepadagi panel: hozir saytda, roʻyxatdan oʻtganlar, bugun/hafta/oy/yil tashriflari | — |
| `js/sfx.js` | Tovush effektlari (Web Audio sintez, fayl yoʻq). Modullarda: tab, tugma, +XP, nishon, daraja, yakun (konfetti), ogohlantirish (`lock` toast); bosh sahifada: hero va globus (`[data-sfx]` ichida, `data-snd="pick"` kabi). 🔊/🔇 tugmasi modul sarlavhasida yoki `[data-sfx-slot]` da, tanlov `localStorage` `kompas_sfx`. Modullar `KSfx.gain()` / `KSfx.play()` ni chaqiradi; dist versiyaga `build.py` ichiga joylaydi | Yangi modulda: `<script src="js/sfx.js"></script>` toast'dan keyin + award/confetti/toast ilmoqlari (mavjud manbadan nusxa) |
| `js/protect.js` | Nusxa olishni cheklash + "kompaslab.uz" suv belgisi (faqat kirganlarga) | — |
| `js/pwa.js`, `sw.js`, `manifest.webmanifest`, `offline.html` | Telefonga oʻrnatish (PWA), oflayn | Rasm/CSS keshini hammaga yangilash: `sw.js` dagi `V = "kl-v1"` ni oshir |
| `css/brand.css` | Logotip komponenti `.klogo` va animatsiyasi | — |
| `img/brand/` | Logotip, favicon, ikonkalar, `og.jpg` | `python3 tools/brand/make_logo.py` |
| `img/3d/*.webp` | 3D ikonkalar (bachelor, bell, books, bulb, calendar, chart, compass, daad, gks, hourglass, lock, master, memo, miya, money, musofir, phd, scroll, seedling, shield, telescope, tt, usa) | — |

## Modullar (`tools/modules/`)
- Manba: `src/<nom>.src.html` (`{{CSS}}` oʻrniga `m0.css`). Yigʻish: `python3 tools/modules/build.py [nom]`.
  - sayt versiyasi → repo ildizida `<nom>.html` (config.js, live-bar, protect, logotip, PWA, darvoza)
  - yuklab olinadigan → `tools/modules/dist/<nom>.html` (rasmlar ichida; git'ga kirmaydi). Foydalanuvchiga `SendUserFile` bilan yuboriladi.
- Master M3–M8 manbalari umumiy generator bilan yaratilgan (qobiq M2 andozasi); endi `src/*.src.html` ni toʻgʻridan-toʻgʻri tahrirla. Pullik modullarda faktlar "16.10.2026 holatiga" belgilangan: har sikl yangilash kerak (M7, M8).
- Yangi modul: eng yaqin manbadan nusxa ol → `build.py` dagi `MODULES` ga qoʻsh → yigʻ → tekshir → Lab sahifasi va dashboard'ga bogʻla.
- Tekshiruv: `python3 -m http.server 8814 &` keyin `PW=$(npm root -g)/playwright node tools/modules/test/smoke.js <nom>` (JS xatosi, 390px, darvoza, 1-dars +XP; sayt va dist).
- Sandbox'dan Supabase va jsdelivr ochilmaydi: Playwright'da `route` bilan mock qilinadi (smoke.js ga qara).

### Modul andozasi (hamma modulda bir xil)
- Geymifikatsiya: **250 XP**, 3 daraja (Kuzatuvchi 0 → Izlanuvchi 80 → Kashfiyotchi 170 → yakun 250), yoʻl xaritasi, 6 ta nishon, toast, konfetti; `prefers-reduced-motion` hurmat qilinadi.
- Har dars 4 qism: **Diqqat 🔥 / Asosiy qism / Xulosa / Topshiriq**; 4 tasi ochilmaguncha dars yakunlanmaydi.
- Javoblar faqat `localStorage` da: kalit `kompas_<lab>_m0_v1` (masalan `kompas_usa_m0_v1`).
- Oxirida avtomatik yigʻiladigan **Qaror va rozilik** bayonoti (18+, toʻlov qaytarilmasligi, Kompas vositachi emas).
- **Tayyorgarlik koʻrsatkichi (Readiness Score)** Lab sahifasidagi test bilan **aynan bir xil** (ogʻirliklar, 70/45 chegaralari, "x" bloklovchi javoblar).
- Narxlar `kompas_public_stats().prices[slug]` dan jonli olinadi (`data-py`, `data-pm`); HTML dagi raqam zaxira. **Mavsum (4 oy) = 3 × oylik** (`data-ps`), bazada alohida ustun yoʻq.
- Faktlar bloki: "Tekshirildi / Rasmiy / Ehtiyot" belgisi, sana va havola.
- Kirish darvozasi: sayt versiyasida faqat roʻyxatdan oʻtganlar (va admin); `file://` da ochiq. **Istisno: Musofir M0 hamma uchun ochiq**, himoyasiz, ulashish tugmasi bor.
- **Suv belgisi ("kompaslab.uz") hamma modulda shart**: `build.py` `WATERMARK` ni har sayt va yuklab olinadigan versiyaga qoʻshadi (oxirgi `</body>` oldidan; kirishdan qatʼi nazar; chop etishda yashirin). Qoʻlda yuritiladigan `master-lab-m0.html` va `lesson.html` da ham bor.

### Holat (2026-10-17)
| Lab | Slug | Modullar (darslar) | Tayyor |
|---|---|---|---|
| Bachelor | bachelor-lab | 17 (86) | M0 saytda |
| Master | master-lab | 9 (59) | M0 saytda; M1–M8 faqat yuklab olinadigan (`dist/`) |
| PhD | phd-lab | `phd-lab.html` ga qara | M0 saytda |
| GKS | gks-lab | 12 (54) | M0 saytda |
| USA | usa-lab | 12 (72) | M0 saytda |
| DAAD | daad-lab | 9 (51) | M0 yoʻq |
| Tadbirkor Talaba | tadbirkor-talaba | 10 (54) | M0 saytda |
| Musofir | miggo | 8 (44) | M0 saytda (ochiq) |
Modul va dars nomlari: `tools/landing/mods.json` (DAAD: `labs_data.py` → `DAAD_MODS`).

## Obuna modeli (2026-10-17 tasdiqlangan)
- 3 tarif: **Oylik**, **Mavsum, 4 oy** (asosiy, 3 oy narxida), **Yillik**. M0 bepul.
- Oylikda modullar har oy bitta faza boʻyicha ochiladi (natija topshirilsa ertaroq); Mavsum va Yillikda hammasi birdaniga.
- Hozircha faqat sahifalardagi matn va narx: haqiqiy cheklov toʻlov va server tomonidagi kirish huquqi bilan birga qilinadi (pastdagi 1–2-bandlar).
- Narx taqqoslash (`render.std_calc`): yillik reja oylik bilan emas, **Mavsum + oylik jamlanmasining eng arzoni** bilan solishtiriladi (`best_short`). Natija: 699/99 → yillik 10+ oyda foydali; Tadbirkor va Musofirda 12 oyda ham 3 × Mavsum arzon (narxni qayta koʻrish kerak).
- **Kompas Pro (2026-10-17):** yillik tarif ostida "Rejada" belgisi bilan (`render.PRO_PLANNED`, bosh sahifada ham): muddat eslatmalari, stipendiyalar bazasi, koʻrsatkich tarixi, sinxronlash. Qurilmaguncha narxga kirmaydi. Shu sababli tariflardan qurilmagan "muddat eslatmalari (Telegram)" vaʼdalari olib tashlandi.
- Asoschi iqtiboslari: Master M0 iqtibosi ismsiz va EYUF siz ("Asoschi"), EYUF 3.4.13 yurist bilan hal boʻlguncha. Footerda YATT maʼlumoti hozircha yoʻq.
- `robots.txt` va `sitemap.xml` ildizda; yangi ochiq sahifa qoʻshilsa, sitemap ga qoʻsh.

## Ochiq masalalar (foydalanuvchi qarori kutilmoqda)
1. **Xavfsizlik:** `fn_mark_payment_paid`, `fn_set_module_access`, `fn_upsert_lesson_content` anon/authenticated tomonidan chaqirilishi mumkin (ichida ruxsat tekshiruvi yoʻq yoki yetarli emas). Toʻlov ochilishidan oldin `revoke execute` qilinishi shart. Foydalanuvchi hali tasdiqlamagan.
2. **Toʻlov:** Click/Payme merchant maʼlumotlari yoʻq; `payment.html` yopiq va eskirgan (karta raqamini oʻzi soʻraydi — PCI DSS ga zid). Toʻgʻri yoʻl: provayderning oʻz sahifasiga yoʻnaltirish + webhook.
3. Ommaviy oferta va maxfiylik siyosati sahifasi yoʻq ("toʻlov qaytarilmaydi" qoidasi uchun kerak).
4. M0 progressi faqat brauzerda (qurilmalar orasida koʻchmaydi) — bazaga yozish rejada.
5. **Roʻyxatdan oʻtish maʼlumoti:** `profiles.education/goal` hech qachon toʻldirilmagan (mijozda UPDATE huquqi yoʻq). 2026-10-17 dan ular `user_metadata` ga yoziladi; `fn_create_profile` triggeriga qoʻshish va eski yozuvlarni toʻldirish — bazaga oid, tasdiq kutilmoqda. Supabase Auth → Redirect URLs da `https://www.kompaslab.uz/reset-password.html` boʻlishi kerak (tekshirilmagan).
6. Mobil ilova: hozir PWA; doʻkon ilovasi signal boʻlganda (Android avval).
