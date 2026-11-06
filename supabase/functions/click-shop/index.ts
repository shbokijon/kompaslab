// Click SHOP-API: Prepare (action=0) va Complete (action=1).
// Click kabinetiga ikkala manzil ham shu funksiyaga beriladi:
//   Prepare URL : https://usxpkmbjrdllnitlzdpq.supabase.co/functions/v1/click-shop/prepare
//   Complete URL: https://usxpkmbjrdllnitlzdpq.supabase.co/functions/v1/click-shop/complete
// Deploy: verify_jwt = false (Click JWT yubormaydi; haqiqiylik sign_string bilan tekshiriladi).
// Secrets: CLICK_SECRET_KEY (asoschi oʻzi kiritadi), CLICK_SERVICE_ID=114929.
// Pul va obuna mantigʻi bazada: fn_payment_prepare / fn_payment_complete (faqat service_role).
import { createClient } from "jsr:@supabase/supabase-js@2";
import { crypto } from "jsr:@std/crypto@1";
import { encodeHex } from "jsr:@std/encoding@1/hex";

const SECRET = Deno.env.get("CLICK_SECRET_KEY") ?? "";
const SERVICE_ID = Deno.env.get("CLICK_SERVICE_ID") ?? "";
const sb = createClient(
  Deno.env.get("SUPABASE_URL")!,
  Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!,
  { auth: { persistSession: false } },
);

type P = Record<string, string>;

export async function md5(s: string): Promise<string> {
  return encodeHex(await crypto.subtle.digest("MD5", new TextEncoder().encode(s)));
}

export function signSource(p: P, secret: string): string {
  // Prepare:  click_trans_id + service_id + SECRET + merchant_trans_id + amount + action + sign_time
  // Complete: ... merchant_trans_id + merchant_prepare_id + amount + action + sign_time
  const prep = p.action === "1" ? (p.merchant_prepare_id ?? "") : "";
  return p.click_trans_id + p.service_id + secret + p.merchant_trans_id + prep + p.amount + p.action + p.sign_time;
}

function safeEq(a: string, b: string): boolean {
  if (a.length !== b.length) return false;
  let r = 0;
  for (let i = 0; i < a.length; i++) r |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return r === 0;
}

async function readParams(req: Request): Promise<P> {
  const ct = req.headers.get("content-type") ?? "";
  const out: P = {};
  if (ct.includes("application/json")) {
    const j = await req.json();
    for (const [k, v] of Object.entries(j ?? {})) out[k] = v == null ? "" : String(v);
  } else {
    const f = new URLSearchParams(await req.text());
    for (const [k, v] of f) out[k] = v;
  }
  return out;
}

function reply(p: P, error: number, note: string, id: number | null) {
  const body: Record<string, unknown> = {
    click_trans_id: Number(p.click_trans_id) || p.click_trans_id || null,
    merchant_trans_id: p.merchant_trans_id ?? null,
    error,
    error_note: note,
  };
  body[p.action === "1" ? "merchant_confirm_id" : "merchant_prepare_id"] = id;
  return new Response(JSON.stringify(body), { headers: { "content-type": "application/json; charset=utf-8" } });
}

const REQUIRED = ["click_trans_id", "service_id", "merchant_trans_id", "amount", "action", "sign_time", "sign_string"];

export async function handle(req: Request): Promise<Response> {
  if (req.method !== "POST") return new Response("Method Not Allowed", { status: 405 });
  let p: P;
  try { p = await readParams(req); } catch { return reply({}, -8, "Error in request from click", null); }

  if (!SECRET || !SERVICE_ID) return reply(p, -8, "Error in request from click", null); // sozlanmagan
  if (REQUIRED.some((k) => !p[k]) || (p.action === "1" && !p.merchant_prepare_id)) {
    return reply(p, -8, "Error in request from click", null);
  }
  if (p.action !== "0" && p.action !== "1") return reply(p, -3, "Action not found", null);
  if (p.service_id !== SERVICE_ID) return reply(p, -8, "Error in request from click", null);

  const expected = await md5(signSource(p, SECRET));
  if (!safeEq(expected, p.sign_string.toLowerCase())) return reply(p, -1, "SIGN CHECK FAILED!", null);

  if (!/^\d{1,18}$/.test(p.merchant_trans_id)) return reply(p, -5, "User does not exist", null);
  const amount = Number(p.amount);
  if (!Number.isFinite(amount)) return reply(p, -2, "Incorrect parameter amount", null);

  const payload = { ...p, sign_string: undefined, received_at: new Date().toISOString() };

  const { data, error } = p.action === "0"
    ? await sb.rpc("fn_payment_prepare", {
      p_order_no: Number(p.merchant_trans_id), p_method: "click",
      p_trans_id: p.click_trans_id, p_amount: amount, p_payload: payload,
    })
    : await sb.rpc("fn_payment_complete", {
      p_order_no: Number(p.merchant_trans_id), p_prepare_id: Number(p.merchant_prepare_id),
      p_method: "click", p_trans_id: p.click_trans_id, p_amount: amount,
      p_provider_error: Number(p.error || 0), p_payload: payload,
    });

  if (error || !data || !data[0]) {
    console.error("click-shop db", p.action, p.merchant_trans_id, error?.message);
    return reply(p, -7, "Failed to update user", null);
  }
  const r = data[0] as { code: number; note: string; prepare_id?: number; confirm_id?: number };
  return reply(p, r.code, r.note, (r.prepare_id ?? r.confirm_id) ?? null);
}

Deno.serve(handle);
