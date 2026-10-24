# Kompas Atlas va Kompas Pro — PRD v0.1
Sana: 2026-10-24 · Maqom: taklif, tariflar faollashtirilmagan.

## 1. Product positioning
**Kompas Atlas** — rasmiy, sanasi ko‘rsatilgan ochiq imkoniyat ma’lumotlari: registrlar, university/scholarship dasturlari, Careers havolalari, davlatga xos viza va ish qoidalari.
**Kompas Core** — pullik Lab kontenti va tekshiriladigan artefaktlar.
**Kompas Pro** — foydalanuvchining qaror va vazifalarini nazorat qiluvchi opt-in ish tizimi: shortlisting, evidence-based matching, alerts, application tracking.
Pro *visa consulting*, ishga joylashtirish yoki admission guarantee emas.

## 2. ICP / JTBD
- Birlamchi ICP: 21–32 yoshdagi O‘zbekistonlik STEM talabasi/yosh mutaxassis; bitirishiga 0–18 oy qolgan; bir nechta mamlakatda professional internship/research/early-career ishni qidirmoqda.
- Ikkilamchi ICP: bakalavr/magistr arizachisi, post-study yo‘lini erta rejalashtiradi.
- Boshqa auditoriya: E-9 mehnat migranti; Musofir/MigGo ichida alohida himoya moduli, umumiy Pro ni unga sotmaslik.
- JTBD: “Diplom va ko‘nikmalarimni hisobga olganda, qaysi rasmiy imkoniyatlarga qarash, qaysilarini rad etish, qachon nima qilish va manbani qanday tekshirishni bilmoqchiman.”
- WTP hozir tekshirilmagan.

## 3. Taklif qilinayotgan packaging
| | Free | Core (alohida Lab) | Pro add-on |
|---|---|---|---|
| Rasmiy Atlas | Ha | Ha | Ha |
| Filtr va rasmiy havola | Ha | Ha | Ha |
| Darslar, CV/SoP rubrikalari | Yo‘q | Ha | Core bilan |
| Saved opportunities | 3 ta (gipoteza) | 3 ta | Chegarasiz (fair-use) |
| Evidence-based relevance matching | Yo‘q | Yo‘q | Ha |
| Deadline/rule-change watch | Yo‘q | Qo‘lda | Ha |
| Application tracker / shortlist | Qo‘lda | Asosiy | Kengaytirilgan |
| Notifier / data export | Eksport | Eksport | Ha |

**Narx sinovi, amaldagi tarif emas:** Core obuna uchun Pro +29–39 ming so‘m/oy; Bundle +10–25% chegirma; mustaqil Pro tarifini hozir ochmaslik. Oldin 30 ta foydalanuvchi pilot va to‘lov dalili. Marketing va payment bazasiga bu fayldan avtomatik narx olib yozilmasin.

## 4. Data semantics (eng muhim cheklov)
Alohida obyektlar:
1. `employer`: davlat/ro‘yxatdagi yuridik nom va rasmiy identifikator;
2. `sponsor_status`: litsenziya/akkreditatsiya/oldingi petition, tur, period, manba;
3. `job_posting`: ishning URL, kompaniya, joy, talablar, e’lon sanasi, sana/expiry;
4. `work_route`: qonuniy ishlash yo‘li; mamlakat, versiya, eligibility maydonlari;
5. `user_opportunity`: foydalanuvchi tomonidan saqlangan link va shaxsiy izohlar.

**Hech qachon** UK sponsor licence, Canada positive LMIA, US historical H-1B petition, EU EURES vacancy, Singapore EP, Korea EPS statuslarini bitta `sponsorship_available=true` belgisiga aylantirmang.
“Employer authorised”, “Job may be open”, “Individual eligibility” — alohida maydonlar.

## 5. Matching (rules first, ML later)
Foydalanuvchi majburiy ro‘yxatdan o‘tmasdan Atlasga kira olishi shart. Faqat `Menga mos` yoqilganda ixtiyoriy soha, daraja, qiziqayotgan mamlakat, ko‘nikma, tajriba va muddat olinadi. Pasport nusxasi, tug‘ilgan to‘liq sana va oila daromadi kerak emas.
- **Eligibility gate**: joriy rasmiy qonunga asoslangan qat’iy shart; noma’lum bo‘lsa `unknown`, bo‘sh noma’lum sonlardan ehtimollik chiqarmaslik. Viza tanlov/saralash ehtimoli hisoblanmaydi.
- **Relevance**: sektor, skill, degree, location, ish rejimi va tajriba haqidagi dalillarga asoslangan izohli `mos / qisman / noma’lum`.
- **Readiness**: ish beruvchi va mamlakat rasmiy talablaridan yetishmayotgan hujjat/sertifikat/deadline, ammo yuridik xulosa emas.
- Har natija: `why matched`, `what remains unverified`, `source_url`, `source_last_checked`.
- LLM faqat matnni tushuntirsin; yuridik hard-gate logic yoki tekshirilmagan xulosalarni LLM hal qilmasin.

## 6. MVP va navbat
**Stage 0 (implemented):** UK license-only employer explorer; global official-source landing; curated, separately verified Careers portals.
**Stage 1:** Mobile testing (real iOS Safari & Android Chrome), compact data, job links curation, 30 user pilot, saved shortlist in localStorage.
**Stage 2:** Targeted UK+Netherlands+NZ official registers; source lifecycle, daily/weekly sync, stale flags; 2–3 pilot industry segments.
**Stage 3:** rules-based matching, jobs with live URL and role evidence, deadlines, application status; privacy and payment reviewed.
**Stage 4:** optionally Core+Pro bundle, alert notifications and synchronization only after signal.

## 7. Measurement and kill criteria
Pilot segment n=30, 2 weeks:
- `activation` = >=3 real opportunities manually saved, >=18/30 (experimental target);
- `return` = >=9/30 revisit verified opportunities within 14 days;
- `intent to pay` = >=5 users leave nonrefundable deposit? **NO**: run refundable or properly documented paid trial only, without collecting payment until legal terms exist;
- `signal` = >=5 of 30 voluntarily pay for usable feature after correct checkout/terms; otherwise freeze Pro pricing.
- `quality` = 0 material mislabelled sponsor/visa claims; >=95% curated live link checks within 30 days.
- `reliability` = no source update failure hides stale info.
If quality fails, pause user-visible matching. If WTP fails, preserve free Atlas and end paid Pro pilot.

## 8. Unit economics (formulalar, fakt emas)
`Monthly contribution/user = Price - payment fee - per-user infrastructure - support allocation - data licensing fees`.
`Payback months = CAC / contribution`.
`TAM = global reachable applicants × eligible ratio × yearly price`.
`SAM = selected segments × current process need × annual WTP`.
`SOM = SAM × achievable share`.
Bu raqamlarning inputlari customer discovery orqali o‘lchanmaguncha “katta bozor” da’vosi yo‘q.

## 9. Risk and security
- **CRITICAL:** aniq moslik bo‘lmaganida “visa eligibility confirmed” deyish. Explicit unknown; source audit trail, release gating.
- **HIGH:** noto‘g‘ri yuridik shaxs/brand name match; exact official identifier talab qilish; manual review.
- **HIGH:** eskirgan visa rule, salary threshold, job expiry; source timestamp, TTL, auto-disable/stale.
- **HIGH:** Careers sahifalarni ruxsatsiz scrape qilish; robots/TOS/API va qayta ishlatish litsenziyasini tekshirish. Faqat deep link xavfsiz start.
- **HIGH:** CV, immigration, personal data leakage; opt-in, minimization, no storage of full passports; consent/erasure/export.
- **HIGH:** multi-tenant RLS bypass, admin RPC misuse; Supabase `auth.uid()` owner policies, service key never client, signed webhook authorization and audit logs.
- **MEDIUM:** notification noise, over-notifying; digest setting, opt-out, rate-limit.
- **LOW:** decorative map performance; reduced-motion and progressive rendering.

## 10. Founder decision
`Free Atlas + Core Lab + optional Pro Add-on` — recommended as a reversible experiment. Paid Pro not launch-ready. First prove that target users complete more real tasks than with LinkedIn/EURES/official portals alone. Professional-level privacy and citation discipline is a requirement, not a tier-specific paid feature.
