// Authenticated browser session -> short-lived, HttpOnly cookie for Vercel M0 routing.
// The credential is *verified* by Supabase Auth before the cookie is issued.
const COOKIE = "__Host-kl_m0_access";
const NO_STORE = { "Cache-Control": "no-store", "Content-Type": "application/json; charset=utf-8" };

function clearCookie() {
  return COOKIE + "=; Path=/; Secure; HttpOnly; SameSite=Lax; Max-Age=0";
}
function json(data, status, extraHeaders = {}) {
  return new Response(JSON.stringify(data), { status, headers: { ...NO_STORE, ...extraHeaders } });
}

export default {
  async fetch(request) {
  if (!["POST", "DELETE"].includes(request.method))
    return json({ error: "method_not_allowed" }, 405, { Allow: "POST, DELETE" });

  // Cookies cannot be mutated by cross-site scripts.
  const origin = request.headers.get("origin");
  const reqOrigin = new URL(request.url).origin;
  if (!origin || origin !== reqOrigin) return json({ error: "invalid_origin" }, 403);

  if (request.method === "DELETE")
    return json({ ok: true }, 200, { "Set-Cookie": clearCookie() });

  if (!(request.headers.get("content-type") || "").startsWith("application/json"))
    return json({ error: "invalid_content_type" }, 415);
  const size = Number(request.headers.get("content-length") || 0);
  if (size > 10000) return json({ error: "too_large" }, 413);

  let body;
  try { body = await request.json(); } catch (_) { return json({ error: "invalid_json" }, 400); }
  const token = typeof body?.access_token === "string" ? body.access_token : "";
  if (token.length < 100 || token.length > 6000 || token.split(".").length !== 3)
    return json({ error: "invalid_token" }, 400);

  const base = process.env.SUPABASE_URL;
  const anonKey = process.env.SUPABASE_ANON_KEY;
  if (!base || !anonKey) return json({ error: "not_configured" }, 503);

  try {
    const result = await fetch(base.replace(/\/$/, "") + "/auth/v1/user", {
      headers: { apikey: anonKey, Authorization: "Bearer " + token },
      signal: AbortSignal.timeout(5000), cache: "no-store"
    });
    if (!result.ok) return json({ error: "not_authenticated" }, 401);
    const user = await result.json();
    if (!user?.id || user.role === "anon" || user.is_anonymous === true) return json({ error: "not_authenticated" }, 401);

    // Expiration is trusted only *after* Auth has verified the token.
    const rawPayload = token.split(".")[1].replace(/-/g, "+").replace(/_/g, "/");
    const payload = JSON.parse(Buffer.from(rawPayload, "base64").toString("utf8"));
    const remaining = Math.floor(Number(payload.exp) - Date.now() / 1000);
    if (!Number.isFinite(remaining) || remaining < 15)
      return json({ error: "token_expired" }, 401);
    const age = Math.min(remaining, 3600);
    const cookie = COOKIE + "=" + token + "; Path=/; Secure; HttpOnly; SameSite=Lax; Max-Age=" + age;
    return json({ ok: true }, 200, { "Set-Cookie": cookie });
  } catch (_) {
    return json({ error: "auth_unavailable" }, 503);
  }
  }
};
