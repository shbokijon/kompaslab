# PhD Lab v4 — tahririy va texnik nazorat reyestri (31.10.2026)

Holat: **REVIEW-ONLY**. Branch `claude/phd-lab-v4-content`, PR ochiq, merge yoʻq. Bazaga (`paid_pages`, `modules`, `lessons`) hech narsa yozilmagan.
Asos: asoschi yuklagan `PhD_Lab_M0..M8.html` (55 dars) va `Kompas_Lab_Editorial_Governance_Master_Prompt_v1.md`.

## 1. Tuzilma qarori
| | Oldin (saytda) | Endi |
|---|---|---|
| M0 | 6 dars, "Qaror darvozasi" | 5 dars, "PhD yoʻli menga mosmi?" |
| M1–M8 | rejada, 65 dars (eski reja) | pullik, 50 dars (6/6/7/7/6/6/6/6) |
| Jami | — | 55 dars, 9 modul |
| Fazalar | — | I M1–M2 Yoʻnalish va tanlov, II M3–M4 Rahbar va loyiha taklifi, III M5–M6 Hujjatlar va moliya, IV M7–M8 Ariza va boshlash |

## 2. Muammolar reyestri (yuklangan fayllar)
| # | Muammo | Daraja | Qaror |
|---|---|---|---|
| 1 | Yuklangan fayllar Kompas qobigʻida emas (boshqa palitra, shrift, maket) | P0 | Kontent PhD engine (USA engine nusxasi) orqali Kompas andozasiga koʻchirildi; CSS/dizayn oʻzgarmadi |
| 2 | XP 260–308, 250 emas | P0 | Har modul 250 XP (browser_test: 8/8 = 250) |
| 3 | Notoʻgʻri localStorage kaliti | P1 | `kompas_phd_m<N>_v1` |
| 4 | Tayyorgarlik slayderi Lab testidan farq qiladi | P1 | M0.3 Lab testi bilan bir xil mezon |
| 5 | U+2018 va ASCII apostrof, kirill yoʻq, imlo xatolari (belgilangmang ×2, supervison, Harajat, universietga, Topsirilgan) | P1 | Tuzatildi; manba `oʻ/gʻ` U+02BB, `ʼ` U+02BC |
| 6 | Tarjima qilinmagan inglizcha matn | P2 | Oʻzbekchaga oʻgirildi; atama `lang="en"` bilan |
| 7 | Takrorlangan Xulosa, kesilgan xarita yorliqlari, notoʻgʻri breadcrumb | P2 | Tuzatildi |
| 8 | Research Lab / Kompas Core vaʼdalari (qurilmagan) | P1 | Modullardan olib tashlandi |
| 9 | Lab sahifasi: UKRI "xalqaro talabalar 30% gacha" | P1 | Rasmiy sahifada faqat "limited"; olib tashlandi |
| 10 | Lab sahifasi: asoschi ismi, EYUF stipendianti, "2025-yil 2-tanlov" | P0 (yuridik) | Manbadan olib tashlandi (polish allaqachon yashirardi) |
| 11 | Lab sahifasi: ATAS "30 ish kuni" | P1 | Olib tashlandi; rasmiy sahifaga havola |
| 12 | Lab sahifasi: oylik "Barcha modullar" | P1 | Generator faza qoidasini qoʻyadi (`MONTHLY_EXTRA`) |
| 13 | M8 karyera darsi bor, jadvalda "Oʻrgatilmaydi" | P2 | "Faqat umumiy yoʻnalish (M8.6)" |

## 3. Manbalar reyestri (hammasi 31.10.2026 da ochib tekshirildi)
| Manba | Havola | Ishlatilgan joy |
|---|---|---|
| UKRI-funded studentships (yangilangan 07.04.2026) | https://www.ukri.org/apply-for-funding/ukri-funded-studentships/ | M0, M2, M6, Lab sahifasi |
| UKRI Statement of Expectations for Doctoral Training | https://www.ukri.org/publications/statement-of-expectations-for-doctoral-training/ | M3, M8 |
| University of Leeds: Applying for research degrees | https://www.leeds.ac.uk/research-applying/doc/applying-research-degrees | M2, M5, M7 |
| King's College London: Writing your research proposal (1 500–3 000 soʻz) | https://www.kcl.ac.uk/study/postgraduate-research/how-to-apply/writing-your-research-proposal | M1, M4 |
| GOV.UK ATAS (yangilangan 24.03.2026) | https://www.gov.uk/guidance/academic-technology-approval-scheme | M0, M8 |
| GOV.UK Student visa (6 oy oldin ariza) | https://www.gov.uk/student-visa | M8 |
| UKRIO Concordat to Support Research Integrity (2025) | https://ukrio.org/research-integrity/the-concordat-to-support-research-integrity/ | M1, M4, M5 |
| MSCA Doctoral Networks (yangilangan 29.09.2026) | https://marie-sklodowska-curie-actions.ec.europa.eu/actions/doctoral-networks | M2, M6 |
| EURAXESS | https://euraxess.ec.europa.eu/jobs/search | M2 |
| DORA | https://sfdora.org/read/ | M1, M3 — **asoschi qarori**: DORA masʼul tashkilot sifatida qabul qilinadimi |

Agregatorlar (FindAPhD va h.k.), blog va agentliklar manba sifatida ishlatilmagan.

## 4. Texnik taʼsir
- Yangi: `tools/modules/phd/` (engine, common, mods/m1–m8, check.py, en_check.cjs, browser_test.js, landing.py), `src/phd-lab-m1..m8.src.html`, `phd-lab-o.html`, `supabase/migrations/20261031_phd_lab_katalog.sql` (**qoʻllanmagan**).
- Oʻzgargan: `src/phd-lab-m0.src.html` → `phd-lab-m0*.html`; `phd-lab-m0-6.html` oʻchirildi, `vercel.json` redirect → `phd-lab-m0-5`; `tools/landing/phd_source.html`, `phd_polish.py`, `split.py` (PAID_READER); `dashboard.html` (PAGE_COURSES phd-lab), `js/journey.js` (PhD 55 dars), `admin-paid.html` (matn), `master-planner.html` (planner.py).
- Pullik HTML `tools/modules/paid/` da (git va saytga chiqmaydi); anon uchun ochiq fayl yoʻq.
- Tekshiruvlar: phd/check.py 8/8 OK; en_check 0; teglar, `node --check`, alifbo, apostrof 32 fayl OK; browser_test 8/8 (250 XP, 390px, 6 nishon); `PAID_LAB=phd-lab paid_reader.js` HAMMASI OʻTDI; `lesson_flow.js phd-lab-m0` OK; `site_crawl.js` 195 sahifa, xato 0, buzilgan havola 0.

## 5. Asoschi qarori kutilayotgan masalalar
1. **M0 rozilik bayonotidagi "toʻlov qaytarilmaydi"**: ommaviy oferta va yurist tasdigʻisiz huquqiy vaʼda. Hozir andozadagi matn qoldirilgan.
2. **Bazaga katalog**: migratsiya eski PhD darslarini oʻchiradi (`kompas.phd_replace = 'yes'` bilan). Qaytarib boʻlmaydi; `lessons` ga bogʻlangan progress jadvallari tekshirilishi kerak.
3. **Pullik modullarni yuklash** (`admin-paid.html`): faqat merge va katalogdan keyin.
4. **Eski M0 progressi**: kalit `kompas_phd_m0_v1` saqlangan, lekin `l3`, `l4` maʼnosi oʻzgardi (eski 0.3 → yangi 0.4). Oʻtgan talabada darslar notoʻgʻri belgilanishi mumkin. Variant: kalitni `_v2` ga oʻzgartirish (progress nolga tushadi).
5. **DORA** manba sifatida (3-boʻlim).
6. **Eski Master sahifalari**: `tools/landing/build.py` Master Lab sahifalarini boshqacha chiqaradi (main dagi HTML generatorga mos emas). Bu PR da Master oʻzgarishlari qaytarildi; alohida tekshirish kerak.

## 6. Toʻxtatish mezonlari (kill criteria)
- Biror fakt rasmiy sahifada tasdiqlanmasa: matndan olinadi, "tekshirilmagan" deb qoldirilmaydi.
- Pullik HTML anon soʻrovda ochilsa: yuklash toʻxtatiladi.
- Merge oldidan site_crawl yoki paid_reader xato bersa: merge qilinmaydi.
- Har sikl (UKRI, MSCA, ATAS, viza qoidalari) yangilanganda M0, M2, M6, M8 qayta tekshiriladi.
