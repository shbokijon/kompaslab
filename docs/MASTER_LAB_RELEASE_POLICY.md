# Master Lab — content readiness and release policy

Date: 2026-10-18. This file documents current development state, not an admission or visa guarantee.

## Product commitment
- Fully self-service: no individual mentor feedback, admissions agency service or founder-operated support loop.
- M0 (five-step decision module) is free. M1–M8 are paid-course drafts and must not become publicly accessible as unprotected HTML.
- Existing authoring inputs: tools/modules/src/master-lab-m1.src.html through master-lab-m8.src.html. The build config intentionally has site:false for these.
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
| M1 | Ilmiy yo‘nalish va universitet | master-lab-m1.src.html | Source draft, not public |
| M2 | Muddatlar va ish tizimi | master-lab-m2.src.html | Source draft, not public |
| M3 | Akademik CV | master-lab-m3.src.html | Source draft, not public |
| M4 | Tavsiya xatlari va professor | master-lab-m4.src.html | Source draft, not public |
| M5 | Maqsad bayonnomasi (SoP) | master-lab-m5.src.html | Source draft, not public |
| M6 | Ilmiy loyiha taklifi | master-lab-m6.src.html | Source draft, not public |
| M7 | Stipendiyalar va funding | master-lab-m7.src.html | Source draft, source audit required |
| M8 | Intervyu, visa, jo‘nash | master-lab-m8.src.html | Source draft, immigration expert review required |

## No-payment release gate
Keep payment.html closed until: production identity/legal documentation, merchant contract, proper provider-hosted checkout, signed webhook verification, correct product pricing, idempotency, receipt/refund handling, security tests, availability tests, RLS tests with two different accounts, and independent editorial signoff.

## Verification
Change through PR; inspect Vercel deployment and domain after merge. GitHub changes alone do not prove public site deploy success.
