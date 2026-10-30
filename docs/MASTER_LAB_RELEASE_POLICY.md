# Master Lab — content readiness and release policy

Date: 2026-10-18. This file documents current development state, not an admission or visa guarantee.

## Product commitment
- Fully self-service: no individual mentor feedback, admissions agency service or founder-operated support loop.
- M0 (five-step decision module) is free. M1–M8 are paid and are never published as public HTML files.
- Authoring inputs: tools/modules/src/master-lab-m1.src.html … m8.src.html. build.py has site:false, paid:True for them.

## Paid delivery (2026-10-30)
- `python3 tools/modules/build.py master-lab-mN` writes the full single-page module to `tools/modules/paid/master-lab-mN.html` (gitignored, not deployed).
- `python3 tools/modules/paid_upload.py` writes `tools/modules/paid/upload_*.sql`; running them upserts `public.paid_pages` (course_slug, module_index, html, sha256, version).
- `paid_pages` RLS: admin only. Students get the HTML only from `fn_paid_page(course, module)` (security definer, authenticated only): checks enrollment payment_status paid/partial, frozen_at, expires_at and `fn_module_position(module) <= unlocked_modules`. Reasons returned: auth, no_access, frozen, expired, locked, missing.
- `master-lab-o.html?m=N` (noindex) calls the RPC and renders the page with document.write in the same origin, so localStorage keys `kompas_master_mN_v1`, relative assets, sfx, watermark and protect.js keep working.
- Module hubs `master-lab-mN.html` include `js/paid-module.js`: for admin or an entitled subscriber the lock box becomes "Modulni ochish". This is display only; the server check is in fn_paid_page.
- dashboard.html: for master-lab, module rows link to M0 / master-lab-o.html?m=N, lock state comes from the enrollment (unlocked_modules), progress is read from the modules' localStorage.
- Migration: `supabase/migrations/20261030_master_paid_pages.sql` (also fixes fn_set_module_access, which anonymous callers could run). Test: `tools/modules/test/paid_reader.js`.
- After any content edit: rebuild, regenerate upload SQL, run it, compare sha256.
- Existing marketing syllabus: master-lab.html lists M0–M8 (59 lesson positions). A list of lessons is not equal to 59 fully reviewed and published lessons.
- New free product: master-planner.html: goal, intake year, user-maintained shortlist, tasks, export. It does NOT implement official eligibility, real-time deadline checks, or automatic source verification.
- Secure payment checkout remains disabled while registration/e-signature, merchant contract and provider integration are pending.

## Editorial gates required for EACH lesson
1. Learning outcome, essential concepts, first-principles explanation, task and objectively checkable answer/rubric.
2. Uzbek name first, international English term in parentheses; consistent throughout 12 Labs.
3. Every factual claim with claim text, first-party URL, issuing authority, scope, academic cycle, checked at, next review due, reviewer ID and review status. No invented verification dates.
4. Distinguish evergreen educational method (Yadro) from country/year-dependent facts (Qobiq).
5. No publication if factual claims are stale, incorrect, unsourced, or reviewer-required expert approval is absent.
6. Content audit: official requirements, tuition, funding, visa, deadlines, programme descriptions and change log must be supported by original issuers, not third-party summaries.
7. User testing on 360px viewport, screen readers/keyboard, slow network, export, accessibility and no fake functionality.
8. Paid content access must be authorized server-side and via RLS; subscription confirmed by payment provider server callback only.
9. Reviewer approval must be independent of original author for high-risk facts.
10. Reviewer approval and rollback path recorded before publication.

## Module readiness checklist (all require verification and integration)
| Module | Topic | Current repository asset | Release readiness |
|---|---|---|---|
| M0 | Qanday ishlaydi, diagnostika | master-lab-m0.html | Public free experience exists; content refresh/audit pending |
| M1 | Ilmiy yo‘nalish va universitet | master-lab-m1.src.html | Built for paid delivery; editorial review pending |
| M2 | Muddatlar va ish tizimi | master-lab-m2.src.html | Built for paid delivery; editorial review pending |
| M3 | Akademik CV | master-lab-m3.src.html | Built for paid delivery; editorial review pending |
| M4 | Tavsiya xatlari va professor | master-lab-m4.src.html | Built for paid delivery; editorial review pending |
| M5 | Maqsad bayonnomasi (SoP) | master-lab-m5.src.html | Built for paid delivery; editorial review pending |
| M6 | Ilmiy loyiha taklifi | master-lab-m6.src.html | Built for paid delivery; editorial review pending |
| M7 | Stipendiyalar va funding | master-lab-m7.src.html | Built for paid delivery; facts dated 16.10.2026, source re-check required before sale |
| M8 | Intervyu, visa, jo‘nash | master-lab-m8.src.html | Built for paid delivery; immigration expert review required before sale |

## No-payment release gate
Keep payment.html closed until: production identity/legal documentation, merchant contract, proper provider-hosted checkout, signed webhook verification, correct product pricing, idempotency, receipt/refund handling, security tests, availability tests, RLS tests with two different accounts, and independent editorial signoff.

## Verification
Change through PR; inspect Vercel deployment and domain after merge. GitHub changes alone do not prove public site deploy success.

## Navigation architecture (2026-10-18)

- Master course landing: master-lab.html (short hub with premium original CSS and hero).
- Syllabus: master-lab-dastur.html (9 modules, 59 lesson titles from the existing syllabus).
- M0 module hub: master-lab-m0-darslar.html (5 standalone lessons).
- M0 free lessons: master-lab-m0-1.html through master-lab-m0-5.html. These educational pages are free and do not grant any paid entitlements; they reuse the original lesson copy.
- M0 legacy interactive tools: master-lab-m0.html#tool-rs, #tool-dl, #qaror (kept temporarily for backward compatibility, legacy login gate and tool state).
- Shared local progress key: kompas_master_m0_v1. No cross-device guarantee.
- M1–M8 module outlines: master-lab-modul.html?m=1..8. Outlines are public; complete paid content remains private (existing tools/modules/build.py keeps site:false).
- Dedicated course source/pricing/FAQ pages: master-lab-manbalar.html, master-lab-narxlar.html, master-lab-savollar.html.
- Course pages should be short; module pages enumerate their lessons; full lesson content belongs only on its separate URL.
- M1–M8 actual lesson release requires server-side authorization, source validation, release tests and payment webhook integration.
- The site-wide landing remains in its original long form for now to avoid breaking its coupled compass, pricing and live-stat scripts. It needs a separate refactor sprint; do not replace the approved premium design.
