import { next } from "@vercel/functions";

// All Lab M0 URLs (including each lesson and the final exercise) are private.
// Public Lab descriptions, Kompas Start and payment pages are NOT affected.
const M0_PATH = /^\/(?:maktab-lab|bachelor-lab|master-lab|phd-lab|gks-lab|erasmus-lab|erasmus-plus-lab|usa-lab|daad-lab|mext-lab|tadbirkor-talaba|tt-lab|musofir-lab|ai-amaliyot-lab|research-lab)-m0(?:-[1-9]\d*|-yakun)?(?:\.html)?\/?$/i;
const COOKIE = "__Host-kl_m0_access";
const NO_STORE = { "Cache-Control": "private, no-store", "Vary": "Cookie" };

function readCookie(header, key) {
  for (const item of (header || "").split(";")) {
    const part = item.trim();
    if (part.startsWith(key + "=")) return part.slice(key.length + 1);
  }
  return null;
}

function toBridge(url) {
  const target = url.pathname + url.search;
  const bridge = new URL("/m0-access.html", url);
  bridge.searchParams.set("next", target);
  return new Response(null, {
    status: 302,
    headers: { ...NO_STORE, Location: bridge.toString() }
  });
}

export const config = { matcher: "/:path*" };

export default async function middleware(request) {
  const url = new URL(request.url);
  if (!M0_PATH.test(url.pathname)) return next();

  const token = readCookie(request.headers.get("cookie"), COOKIE);
  const base = process.env.SUPABASE_URL;
  const anonKey = process.env.SUPABASE_ANON_KEY;
  if (!token || !base || !anonKey) return toBridge(url);

  // Validate the JWT against the Auth server; never trust an unverified cookie.
  // We do not rely on email, user_metadata, or client-side UI for access decisions.
  try {
    const res = await fetch(base.replace(/\/$/, "") + "/auth/v1/user", {
      method: "GET",
      headers: { apikey: anonKey, Authorization: "Bearer " + token },
      signal: AbortSignal.timeout(5000),
      cache: "no-store"
    });
    if (res.ok) {
      const user = await res.json();
      if (user && user.id && user.role !== "anon") return next({ headers: NO_STORE });
    }
  } catch (_) {
    // Fail closed; the bridge can renew a valid Supabase browser session.
  }
  return toBridge(url);
}
