# Kompas Lab · M0 access & Vercel usage (2026-11-01)

## M0 product policy
M0 is **free** (no subscription or payment), not universally publicly accessible.

| Lab | M0 presence | Access |
|---|---|---|
| Bachelor | Exists | Registered and active user; admin |
| Master | Exists | Registered and active user; admin |
| PhD | Exists | Registered and active user; admin |
| GKS | Exists | Registered and active user; admin |
| USA | Exists | Registered and active user; admin |
| DAAD | Exists (one-page M0) | Registered and active user; admin |
| Tadbirkor Talaba | Exists | Registered and active user; admin |
| Musofir | Exists | **Public exception**, safety / scam-prevention guidance |
| Maktab | Not yet published | **Fail closed** until verifiable guardian consent is implemented |
| Research / AI / remaining proposed Labs | Not yet published | Their future `<lab>-m0[-lesson|-yakun]` routes automatically use the registered-user gate if `js/kompas-ui.js` is loaded |

Implementation: `js/kompas-ui.js` contains a pathname-scoped gate. It runs only on `*-m0`, `*-m0-N` and `*-m0-yakun` pages, including Vercel clean URLs. It uses Supabase Auth `getUser()` (verified server-side) and the existing `kompas_account_active()` RPC. The gate reuses current `--accent`, `--surface`, `--border`, fonts and form conventions without touching course page layouts.

**Important security boundary:** These pages remain static HTML. UI gating does not make HTML source confidential: the page source and cached copies may still expose free M0 content. Paid materials must remain in Supabase `paid_pages` with existing `fn_paid_page` authorization. If M0 ever needs strong paywall-like confidentiality, move HTML delivery to a backend auth-gated endpoint, not this browser-side overlay.

**Special case:** Maktab Lab must implement and independently verify lawful parental/guardian consent before its M0 can open. The current guard fails closed for `maktab-lab`.

## Vercel Usage integration

- Frontend: Admin → Tizim monitoringi → Vercel Usage.
- Endpoint: `GET /api/admin/vercel-usage` implemented as framework-free Vercel Node.js Function at `api/admin/vercel-usage.mjs`.
- Authorization: user Supabase access token (Authorization Bearer); backend verifies token via `/auth/v1/user`, then checks `fn_is_admin()` and `kompas_account_active()`. Only full Admin may read billing records.
- Backend Vercel API: `GET https://api.vercel.com/v1/billing/charges` with server-owned `VERCEL_API_TOKEN`, fixed team scope, past 30 complete UTC days. FOCUS 1.3 newline-delimited JSON is parsed server-side, aggregated into billed cost per service. The frontend gets only aggregates, no provider token.
- **This returns team-wide billing charges, not current Vercel resource quotas or per-project consumption.** Vercel documents the billing scope as available to Pro and Enterprise teams; Hobby may be unsupported.
- Browser does not see `VERCEL_API_TOKEN`; no CORS open policy; GET only; no-store, JWT + Admin + Active check; upstream timeout and response-size limit.
- Deployment requires variables **set in Vercel Project Settings → Environment Variables**, targeting appropriate preview and production environments:
  - `VERCEL_API_TOKEN` — sensitive, scoped to correct team with billing read access; create directly in Vercel, never paste into chat / GitHub.
  - `SUPABASE_ANON_KEY` — the public (anon/publishable) key, required for the Auth verification and RPC; backend never uses the service-role key.
  - `SUPABASE_URL` — optional, project URL already has fixed public default.
  - `VERCEL_TEAM_ID` — optional, defaults to the known team.
- Connected Vercel API returned 403 for team-scoped env settings; user needs to approve the Vercel team-access consent link before the connector can configure project settings. Even then, create the sensitive `VERCEL_API_TOKEN` directly within Vercel UI, rather than exposing its value through a tool transcript.

## Acceptance checklist
1. Guest visits Bachelor/DAAD M0 hub, lesson & yakun — sees login/register gate, original layout remains hidden.
2. Active registered account on those paths — original free M0 opens, without a payment or enrollment.
3. Suspended account — denied, even when a stale browser session exists.
4. Musofir M0 — guest can read safety material.
5. Maktab M0 (when created) — fail-closed until consent verification exists.
6. Paid modules — unchanged `fn_paid_page` gating.
7. GET usage without JWT → 401; student JWT → 403; inactive admin → 403; valid admin missing Vercel token → 503; valid admin & proper team credential → summary; provider 403 → generic error (no token leakage).
8. Visual regression on desktop/mobile and test login redirect returnTo.
9. Check Vercel Preview READY, then authenticated smoke tests before merging to `main`.
