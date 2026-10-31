# Master Lab — content readiness and release policy

Date: 2026-10-18. This file documents current development state, not an admission or visa guarantee.

## Product commitment
- Fully self-service: no individual mentor feedback, admissions agency service or founder-operated support loop.
- M0 (five-step decision module) is free. M1–M8 are paid and are never published as public HTML files.
- Authoring inputs: tools/modules/src/master-lab-m1.src.html … m8.src.html. build.py has site:false, paid:True for them.

## Paid delivery (2026-10-30)
- `python3 tools/modules/build.py master-lab-mN` writes the full single-page module to `tools/modules/paid/master-lab-mN.html` (gitignored, not deployed).
- Upload: admin opens `admin-paid.html` (noindex, admin only; RLS allows only admin writes) and selects the eight built files; sha256 and timestamp are recorded. Alternative: `python3 tools/modules/paid_upload.py` writes `tools/modules/paid/upload_*.sql`; running them upserts `public.paid_pages` (course_slug, module_index, html, sha256, version).
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


## M1 editorial revision — 2026-10-31
- Source: `tools/modules/src/master-lab-m1.src.html` (7 lessons; four panels each). Public syllabus and module hub have aligned descriptions.
- Preliminary pool: 12–15 programmes; evidence-checked shortlist: usually 6–10. This is editorial guidance, not an admission rule.
- "Safe/Ishonchli" rephrased to "Nisbatan mos" with no probability guarantee. Programme fit evidence counts are not admission predictions.
- QS official 2026 methodology, THE World University Rankings 2027 and ARWU 2026; check each official methodology before release.
- Scholarship coverage is programme- and country-dependent. Funding examples do not establish eligibility or award.
- Published paid module in Supabase `paid_pages` is **not automatically changed** by editing the GitHub source. The older paid_pages version remains until independent editorial sign-off, build, SHA comparison, RLS regression tests and controlled upload.
- This revision does not authorise new student entitlements, checkout changes or relaxation of existing paid content access controls.


## M2 editorial revision — 2026-10-31
- Changed 5 lesson texts and associated objectives. Source: `tools/modules/src/master-lab-m2.src.html`.
- Official evidence: Oxford graduate application and referee deadlines; Cambridge programme versus funding deadlines. Examples are **not** universal rules.
- `priority`, `rolling`, `rounds`, funding and document deadlines depend on each programme. Record cycle, time zone, official link and verification date.
- 8-week reference notice, one-week buffer, 6–10 programmes / up to three scholarships, 14-day clash window are *planning heuristics*, not official requirements.
- Tracker is a local-browser planning record. Gantt visualises approximate intervals based on user-supplied dates and a single preparation-weeks setting; it does not automatically sync official dates, contact referees or submit applications.
- The Master Lab public module hub and programme descriptions were aligned. **The full paid HTML in Supabase `paid_pages` was not overwritten.**
- Require independent review of claims, cross-browser interactive test (tracker, date/time-zone, import/export, Gantt), rebuild, SHA-256 comparison, RLS and controlled upload before paid module release.

## Learner-facing artifact naming — 2026-10-31
- User-facing M2.5 lesson: **I bosqich yakuni: Shaxsiy strategik reja**.
- User-facing M2 result/export: **Magistraturaga tayyorgarlik rejasi**.
- The artifact is a living plan; record verification date and changes in the learner's own workflow. Do not show technical `v1.0` in M2 titles, module summary or export heading.
- Preserve technical version fields, hashes, existing `localStorage` keys, database versions, authorization and release workflows.
- Reviewed other Master modules: M1 shows `Saralangan roʻyxat v1.0`; M3 `Akademik CV v1.0`; M5 `SoP v1.0`; M6 `Research Proposal v1.0`. M4/M7/M8 do not use this artifact label. Propose simpler names in their **separate** editorial passes; do not silently rewrite those modules before their approved review.
- M5's explicit document revision history and version field have a real instructional purpose. Retain that functionality and replace only confusing display labels if approved.
- Paid modules are not published solely by GitHub source edits. Supabase `paid_pages` remains unchanged until independent content/build/security release checks.


## M3 editorial revision — 2026-10-31
- Canonical authoring file: `tools/modules/src/master-lab-m3.src.html`; six lessons, four panels each. Public M3, syllabus and route descriptions aligned.
- Verified against Oxford CV/résumé guidance, Cambridge postgraduate supporting documents, official Europass CV, Council of Europe CEFR, IELTS research and Think. Check. Submit.
- Academic CV requirement is course-specific: Oxford says most courses do **not** require separate uploaded CV, Cambridge postgraduate requires CV. Course instructions override fixed country and page-count claims.
- Europass can be an optional format; not mandatory-only. GPA remains in original scale, no invented STAR metrics, no fake publications or DOI. CEFR and IELTS scores are not automatically equated.
- Actual Word button downloads an **HTML-based `.doc`**, not `.docx`. UI and marketing copy now reflect current implementation. PDF is browser print-to-PDF. Do not claim a native DOCX exporter exists.
- Learner-facing M3 result: **Akademik CV**, with an actual supporting export format explanation. Remove superficial `v1.0` from M3 presentation only; preserve existing technical `localStorage` key `kompas_master_m3_v1`.
- CSS, module panels, input identifiers, local state key and paid entitlement workflow unchanged.
- Supabase `paid_pages` module_index=3 remains at version `2026-10-30+suggest` until an independently reviewed rebuild and controlled update. No database write was made.
- Before release: build HTML, compare content hash, verify quiz answer/XP, STAR builder, CV sections, print PDF and Word-mos DOC behaviour across browsers; check paid authorization, RLS and state backwards-compatibility. University-specific CV policy must not be presented as universal.


## M4 editorial revision — 2026-10-31
- Canonical lesson source: `tools/modules/src/master-lab-m4.src.html` (6 lessons, 4 panels each).
- Fact-check: Oxford registers 3 referees and can assess once 2 references arrive; Cambridge normally needs 2, Gates Cambridge 3; Chevening nominates 2 and successful interview-stage applicants upload the letters. Reference submission is programme-specific.
- Referee independence is essential; applicant may provide CV and factual evidence but must not misrepresent authored reference as referee's own.
- FERPA waiver is a privacy/access choice, not an admission guarantee. The M4.1 interactive quiz answers were updated to reflect that.
- A 6–8-week initial request, 150–200-word email and 7–10 working day follow-up are editorial planning guidance, not university requirements. The email builder's 150–200-word XP check is unchanged and explicitly described as an exercise-only gate.
- Research supervisor pre-contact is programme- and department-dependent. Taught master's applicants are not expected to contact professors where it is unnecessary.
- Outreach Log adds 10 **calendar** days and does not send reminders or emails. The referee scoring model is an unvalidated heuristic, not an admissions likelihood.
- Replaced learner-facing "faza" with "bosqich" in M4 source and public hub, retained styles, modules, user state keys and interactive structure.
- The GitHub source and public syllabus/hub are updated; Supabase paid module `master-lab` index 4 remains on version `2026-10-30+suggest`. Full paid lessons are **not** yet updated for subscribers.
- Release gate: editorial approval, compiled HTML rebuild, hash confirmation, quiz/score, date calculations, email builder, CSV export, mobile/browser regression and RLS/paid-access checks before controlled `paid_pages` replacement.

## Module readiness checklist (all require verification and integration)
| Module | Topic | Current repository asset | Release readiness |
|---|---|---|---|
| M0 | Qanday ishlaydi, diagnostika | master-lab-m0.html | Public free experience exists; content refresh/audit pending |
| M1 | Ilmiy yo‘nalish va universitet | master-lab-m1.src.html | 2026-10-31 editorial draft revised; independent review, rebuild and paid_pages update pending |
| M2 | Muddatlar va ish tizimi | master-lab-m2.src.html | 2026-10-31 editorial revision in source; independent review, rebuild, SHA comparison, paid_pages update and RLS tests pending |
| M3 | Akademik CV | master-lab-m3.src.html | 2026-10-31 editorial revision in GitHub; paid_pages rebuild, security and browser tests pending |
| M4 | Tavsiya xatlari va professor | master-lab-m4.src.html | 2026-10-31 editorial revision in source; separate paid_pages build, QA and authorization tests pending |
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
