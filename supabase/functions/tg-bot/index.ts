// Kompas Lab · talabalar boti · Supabase Edge Function "tg-bot"
//   POST /tg-bot/webhook  — Telegram update (X-Telegram-Bot-Api-Secret-Token tekshiriladi)
//   POST /tg-bot/flush    — tg_outbox navbatini yuborish (x-kompas-flush tekshiriladi)
//   POST /tg-bot/outreach — outreach_queue dagi yangi nomzodlarni admin chatiga karta qilib yuborish
//   POST /tg-bot/setup    — webhookka callback_query ni yoqish (bir martalik)
// Deploy: verify_jwt = false (Telegram va pg_net JWT yubormaydi; haqiqiylik sirlar bilan).
// Secrets (asoschi oʻzi kiritadi):
//   TG_USER_BOT_TOKEN   — talabalar boti tokeni
//   TG_ADMIN_BOT_TOKEN  — admin boti tokeni (@KompasUserInfobot, yangilangan)
//   TG_WEBHOOK_SECRET   — setWebhook dagi secret_token
//   TG_FLUSH_SECRET     — Vault dagi tg_flush_secret bilan bir xil
// Matnlar manbada amaldagi alifboda (oʻ, gʻ U+02BB; tutuq U+02BC). Yuborishda toNew() yangi alifboga oʻgiradi.
// Botda sotuv, pullik kontent va AI yoʻq. Murojaat matnlari andoza; har biri admin tasdigʻi bilan ketadi.
// 2026-11-12: hisob ulanganda shaxsiy salomlashuv (welcome.ts); saytda ulash: js/tg-link.js
// (register.html 4-qadam va dashboard.html kartasi).
import { createClient } from "jsr:@supabase/supabase-js@2";
import { buildWelcome } from "./welcome.ts";

const USER_TOKEN = Deno.env.get("TG_USER_BOT_TOKEN") ?? "";
const ADMIN_TOKEN = Deno.env.get("TG_ADMIN_BOT_TOKEN") ?? "";
const WEBHOOK_SECRET = Deno.env.get("TG_WEBHOOK_SECRET") ?? "";
const FLUSH_SECRET = Deno.env.get("TG_FLUSH_SECRET") ?? "";
const ADMIN_CHAT = 255077744;
const SITE = "https://kompaslab.uz/";
const PRIVACY_URL = Deno.env.get("TG_PRIVACY_URL") ?? "https://kompaslab.uz/maxfiylik.html";
const SUPPORT_LIMIT_PER_HOUR = 5;
const WEBHOOK_URL = "https://usxpkmbjrdllnitlzdpq.supabase.co/functions/v1/tg-bot/webhook";

const sb = createClient(
  Deno.env.get("SUPABASE_URL")!,
  Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!,
  { auth: { persistSession: false } },
);

// ---------- Yangi alifbo (js/alifbo.js bilan bir xil boʻlishi kerak) ----------
// EX: sh/ch li xorijiy soʻzlar oʻgirilmaydi. Saytdagi EX roʻyxati kengaysa, bu yerga ham qoʻshiladi.
export const EX = new Set([
  "bachelor", "research", "scholarship", "scholarships", "school", "chevening", "fellowship",
  "english", "phd", "click", "telegram", "kompaslab", "check", "checklist", "brag", "sheet",
  "shortlist", "tech", "match", "pitch", "coach", "search", "fresh",
]);
const OK = "ʻ"; // ʻ
const TUTUQ = "ʼ"; // ʼ

function convertWord(w: string): string {
  if (EX.has(w.toLowerCase().replace(/[^a-z]/gi, ""))) return w;
  return w
    .replace(new RegExp("O" + OK, "g"), "Ö").replace(new RegExp("o" + OK, "g"), "ö")
    .replace(new RegExp("G" + OK, "g"), "Ğ").replace(new RegExp("g" + OK, "g"), "ğ")
    .replace(/SH/g, "Ş").replace(/Sh/g, "Ş").replace(/sh/g, "ş")
    .replace(/CH/g, "Ç").replace(/Ch/g, "Ç").replace(/ch/g, "ç");
}

// URL, email, /buyruq, @username va kod qismlariga tegmaydi.
export function toNew(s: string): string {
  return s.split(/(https?:\/\/\S+|[\w.+-]+@[\w-]+\.[\w.]+|\/[a-z_]+|@\w+|`[^`]*`)/g)
    .map((part, i) => (i % 2 === 1 ? part : part.replace(new RegExp("[\\p{L}" + OK + TUTUQ + "]+", "gu"), convertWord)))
    .join("");
}

// ---------- Telegram ----------
// deno-lint-ignore no-explicit-any
type TgResult = { ok: boolean; status: number; result?: any; description?: string };

async function tg(token: string, method: string, payload: Record<string, unknown>): Promise<TgResult> {
  if (!token) return { ok: false, status: 0, description: "token not configured" };
  const r = await fetch(`https://api.telegram.org/bot${token}/${method}`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(payload),
  });
  const j = await r.json().catch(() => ({}));
  return { ok: !!j.ok, status: r.status, result: j.result, description: j.description };
}

function send(chatId: number, textSrc: string, bot: "user" | "admin" = "user") {
  return tg(bot === "user" ? USER_TOKEN : ADMIN_TOKEN, "sendMessage", {
    chat_id: chatId,
    text: toNew(textSrc),
    disable_web_page_preview: true,
  });
}

function safeEq(a: string, b: string): boolean {
  if (!a || a.length !== b.length) return false;
  let r = 0;
  for (let i = 0; i < a.length; i++) r |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return r === 0;
}

// ---------- Matnlar ----------
const T = {
  welcome:
    "Assalomu alaykum. Bu Kompas Lab boti.\n\n" +
    "Bot nima qiladi: toʻlov qabul qilinganini va obuna muddati tugashini xabar qiladi, savolingizni jamoaga yetkazadi.\n" +
    "Darslar va toʻlov faqat saytda: " + SITE + "\n\n" +
    "Hisobingizni ulash: saytdagi kabinetda «Telegramda ulash» tugmasini bosing.\n" +
    "Hali roʻyxatdan oʻtmagan boʻlsangiz: " + SITE + "register.html?utm_source=bot&utm_medium=xat&utm_campaign=tg_start",
  linked:
    "Hisobingiz ulandi.\n\n" +
    "/holat — obuna holati\n/yordam — savol yuborish\n/toxtat — muddat eslatmalarini oʻchirish\n/maxfiylik — maxfiylik siyosati",
  badToken:
    "Havola eskirgan yoki allaqachon ishlatilgan. Kabinetda «Telegramda ulash» tugmasini qayta bosing (havola 15 daqiqa amal qiladi).",
  notLinked:
    "Hisobingiz hali ulanmagan. Saytdagi kabinetda «Telegramda ulash» tugmasini bosing: " + SITE,
  noSubs: "Faol obuna topilmadi. M0 modullari har Labda bepul: " + SITE,
  help:
    "Savolingizni bitta xabarda yozing, jamoaga yetkazaman. Odatda 1–2 ish kunida javob beramiz.\n" +
    "Toʻlov boʻyicha savolda toʻlov raqamini (masalan, T12) ham yozing.",
  received: "Xabaringiz yetkazildi. Javob shu yerga keladi.",
  limit: "Bir soatda koʻpi bilan 5 ta xabar yuborish mumkin. Keyinroq yozing.",
  remOff: "Muddat eslatmalari oʻchirildi. Qayta yoqish: /yoqish\nToʻlov xabarlari kelaveradi.",
  remOn: "Muddat eslatmalari yoqildi.",
  privacy: "Maxfiylik siyosati: " + PRIVACY_URL,
  unknown: "Buyruqlar: /holat, /yordam, /toxtat, /yoqish, /maxfiylik",
  replyThanks: "Rahmat, yozib oldik. Qoʻshimcha aytmoqchi boʻlgan narsangiz boʻlsa, shu yerga yozing, jamoaga yetkazamiz.",
  replyNo: "Tushunarli, boshqa bunday savol bilan bezovta qilmaymiz. Savol tugʻilsa, shu yerga yozing.",
};

// ---------- Hisob ulanganda: shaxsiy salomlashuv ----------
async function sendLinkedWelcome(chatId: number, userId: string, username: string | null): Promise<void> {
  try {
    const w = await buildWelcome(sb, userId, username);
    const r = await tg(USER_TOKEN, "sendMessage", {
      chat_id: chatId,
      text: toNew(w.text),
      disable_web_page_preview: true,
      ...(w.button ? { reply_markup: { inline_keyboard: [[{ text: toNew(w.button.text), url: w.button.url }]] } } : {}),
    });
    if (!r.ok) await send(chatId, T.linked);
    await send(ADMIN_CHAT, w.adminLine, "user");
  } catch (e) {
    console.error("welcome", e instanceof Error ? e.message : e);
    await send(chatId, T.linked);
  }
}

// ---------- /holat ----------
async function statusText(userId: string): Promise<string> {
  const { data } = await sb
    .from("enrollments")
    .select("plan, phase, track, expires_at, payment_status, frozen_at, courses(title, slug)")
    .eq("user_id", userId)
    .in("payment_status", ["paid", "partial"]);
  const now = Date.now();
  const rows = (data ?? []).filter((e) => !e.frozen_at && (!e.expires_at || Date.parse(e.expires_at) > now));
  if (!rows.length) return T.noSubs;

  const plan: Record<string, string> = { monthly: "Oylik", "6m": "6 oylik" };
  const lines: string[] = ["Faol obunalar:\n"];
  for (const e of rows) {
    // deno-lint-ignore no-explicit-any
    const c = (e as any).courses ?? {};
    let tarif = plan[e.plan as string] ?? String(e.plan ?? "");
    if (e.plan === "monthly" && e.phase) {
      const { data: lbl } = await sb.rpc("fn_tg_phase_label", { p_slug: c.slug, p_phase: e.phase, p_track: e.track });
      tarif += `, ${e.phase}-bosqich` + (lbl ? ` (${lbl})` : "");
    }
    const exp = e.expires_at
      ? new Date(e.expires_at).toLocaleDateString("ru-RU", { timeZone: "Asia/Tashkent" })
      : "muddatsiz";
    lines.push(`${c.title ?? "Lab"} — ${tarif}\nMuddat: ${exp} gacha`);
  }
  return lines.join("\n");
}

// ---------- Murojaat kartalari (outreach_queue) ----------
type Variant = { t: string; kb?: [string, string][] };
const SEG: Record<string, string> = {
  pay_failed: "🔴 Toʻlov oʻtmadi",
  m0_done: "🟢 M0 tugadi, toʻlov yoʻq",
  m0_stalled: "🟠 M0 da toʻxtadi",
  reg_no_m0: "⚪️ Roʻyxatdan oʻtdi, M0 ochmadi",
};
const LETTER = ["A", "B"];

// deno-lint-ignore no-explicit-any
function btn(text: string, data: string): any {
  return { text: toNew(text), callback_data: data };
}

// deno-lint-ignore no-explicit-any
function rows2<T>(xs: T[]): T[][] {
  const out: T[][] = [];
  for (let i = 0; i < xs.length; i += 2) out.push(xs.slice(i, i + 2));
  return out;
}

async function linkOf(userId: string) {
  const { data } = await sb.from("tg_links").select("chat_id, blocked_at, tg_username")
    .eq("user_id", userId).maybeSingle();
  return data;
}

async function outreachCards(): Promise<{ carded: number; failed: number }> {
  const { data } = await sb.from("outreach_queue").select("id, user_id, segment, ctx, variants")
    .eq("status", "new").order("id").limit(10);
  let carded = 0, failed = 0;
  for (const o of data ?? []) {
    const { data: p } = await sb.from("profiles").select("full_name, email, phone").eq("id", o.user_id).maybeSingle();
    const l = await linkOf(o.user_id);
    const linked = !!l && !l.blocked_at;
    const v = (o.variants ?? []) as Variant[];
    // deno-lint-ignore no-explicit-any
    const ctx = (o.ctx ?? {}) as any;

    const head = [
      SEG[o.segment] ?? o.segment,
      [p?.full_name ?? "—", ctx.lab_title, ctx.detail].filter(Boolean).join(" · "),
      "Telegram: " + (linked ? "ulangan" + (l?.tg_username ? " @" + l.tg_username : "") : (l?.blocked_at ? "botni bloklagan" : "ulanmagan")),
      "Aloqa: " + (p?.phone || "tel yoʻq") + " · " + (p?.email || "email yoʻq"),
      "",
    ];
    const body: string[] = [];
    v.forEach((x, i) => {
      body.push(`${LETTER[i]}) ${x.t}`);
      if (x.kb?.length) body.push("[" + x.kb.map((k) => k[0]).join("] [") + "]");
      body.push("");
    });
    if (!linked) body.push("Bot bu odamga yoza olmaydi. Matnni oling va oʻzingiz yuboring.");

    const kb = linked
      ? [[btn("Yuborish A", `o:${o.id}:0`), btn("Yuborish B", `o:${o.id}:1`)], [btn("Oʻtkazib yuborish", `o:${o.id}:s`)]]
      : [[btn("A matni", `o:${o.id}:0`), btn("B matni", `o:${o.id}:1`)],
         [btn("Qoʻlda yubordim", `o:${o.id}:m`), btn("Oʻtkazib yuborish", `o:${o.id}:s`)]];

    // Karta talabalar botidan yuboriladi: tugma bosilishi shu botning webhookiga tushadi.
    const r = await tg(USER_TOKEN, "sendMessage", {
      chat_id: ADMIN_CHAT,
      text: toNew(head.concat(body).join("\n")).slice(0, 4000),
      disable_web_page_preview: true,
      reply_markup: { inline_keyboard: kb },
    });
    if (r.ok && r.result) {
      await sb.from("outreach_queue").update({
        status: "carded", carded_at: new Date().toISOString(), admin_message_id: r.result.message_id,
      }).eq("id", o.id).eq("status", "new");
      carded++;
    } else {
      await sb.from("outreach_queue").update({ last_error: `${r.status} ${r.description ?? ""}`.slice(0, 300) }).eq("id", o.id);
      failed++;
    }
    await new Promise((res) => setTimeout(res, 60));
  }
  return { carded, failed };
}

// deno-lint-ignore no-explicit-any
async function onCallback(cq: any): Promise<void> {
  const data: string = cq.data ?? "";
  const ack = (text?: string) =>
    tg(USER_TOKEN, "answerCallbackQuery", { callback_query_id: cq.id, ...(text ? { text: toNew(text) } : {}) });

  // Admin qarori: o:<id>:<0|1|s|m>
  let m = /^o:(\d+):([01sm])$/.exec(data);
  if (m) {
    if (cq.from?.id !== ADMIN_CHAT) { await ack(); return; }
    const id = Number(m[1]), act = m[2];
    const { data: o } = await sb.from("outreach_queue").select("id, user_id, status, variants").eq("id", id).maybeSingle();
    if (!o) { await ack("Topilmadi"); return; }
    if (o.status !== "carded") { await ack("Allaqachon hal qilingan: " + o.status); return; }
    const msgId = cq.message?.message_id;
    const mark = async (label: string) => {
      if (msgId) {
        await tg(USER_TOKEN, "editMessageReplyMarkup", {
          chat_id: ADMIN_CHAT, message_id: msgId, reply_markup: { inline_keyboard: [[btn(label, "x")]] },
        });
      }
    };
    const now = new Date().toISOString();

    if (act === "s" || act === "m") {
      await sb.from("outreach_queue").update({ status: act === "s" ? "skipped" : "manual", decided_at: now })
        .eq("id", id).eq("status", "carded");
      await mark(act === "s" ? "✓ Oʻtkazib yuborildi" : "✓ Qoʻlda yuborildi");
      await ack();
      return;
    }

    const i = Number(act);
    const v = ((o.variants ?? []) as Variant[])[i];
    if (!v) { await ack("Variant yoʻq"); return; }
    const l = await linkOf(o.user_id);

    if (!l || l.blocked_at) {
      // Ulanmagan: nusxa olish uchun matnni adminga yuboramiz, holat oʻzgarmaydi.
      await send(ADMIN_CHAT, v.t, "user");
      await ack("Matn yuborildi, nusxa oling");
      return;
    }

    const kb = v.kb?.length ? { inline_keyboard: rows2(v.kb.map(([t, k]) => btn(t, `r:${o.id}:${k}`))) } : undefined;
    const r = await tg(USER_TOKEN, "sendMessage", {
      chat_id: l.chat_id, text: toNew(v.t), disable_web_page_preview: true, ...(kb ? { reply_markup: kb } : {}),
    });
    if (r.ok) {
      await sb.from("outreach_queue").update({ status: "sent", chosen: i, decided_at: now }).eq("id", id);
      await mark(`✓ ${LETTER[i]} yuborildi`);
      await ack("Yuborildi");
    } else {
      if (r.status === 403) await sb.from("tg_links").update({ blocked_at: now }).eq("chat_id", l.chat_id);
      await sb.from("outreach_queue").update({
        status: "failed", decided_at: now, last_error: `${r.status} ${r.description ?? ""}`.slice(0, 300),
      }).eq("id", id);
      await mark("✗ Yuborilmadi");
      await ack("Yuborilmadi: " + (r.description ?? r.status));
    }
    return;
  }

  // Talaba javobi: r:<id>:<kalit>
  m = /^r:(\d+):([a-z]{1,10})$/.exec(data);
  if (m) {
    const id = Number(m[1]), key = m[2];
    const chatId = cq.message?.chat?.id;
    const { data: o } = await sb.from("outreach_queue")
      .select("id, user_id, segment, variants, chosen, reply_key").eq("id", id).maybeSingle();
    if (!o) { await ack(); return; }
    const l = await linkOf(o.user_id);
    if (!l || l.chat_id !== chatId) { await ack(); return; }
    const v = ((o.variants ?? []) as Variant[])[o.chosen ?? 0];
    const label = v?.kb?.find((k) => k[1] === key)?.[0];
    if (!label) { await ack(); return; }

    if (!o.reply_key) {
      await sb.from("outreach_queue").update({ reply_key: key, replied_at: new Date().toISOString() }).eq("id", id);
    }
    if (cq.message?.message_id) {
      await tg(USER_TOKEN, "editMessageReplyMarkup", {
        chat_id: chatId, message_id: cq.message.message_id, reply_markup: { inline_keyboard: [] },
      });
    }
    await send(chatId, key === "no" ? T.replyNo : T.replyThanks);
    const { data: p } = await sb.from("profiles").select("full_name").eq("id", o.user_id).maybeSingle();
    await send(ADMIN_CHAT, `💬 Javob: ${p?.full_name ?? "Talaba"} · ${SEG[o.segment] ?? o.segment}\n→ ${label}`, "user");
    await ack();
    return;
  }

  await ack();
}

// ---------- Webhook ----------
// deno-lint-ignore no-explicit-any
async function onUpdate(u: any): Promise<void> {
  if (u.callback_query) { await onCallback(u.callback_query); return; }
  const m = u.message;
  if (!m || !m.chat || typeof m.text !== "string") return;
  const chatId: number = m.chat.id;
  const text: string = m.text.trim();

  // Admin javobi: admin uzatilgan xabarga "Reply" qiladi.
  if (chatId === ADMIN_CHAT && m.reply_to_message) {
    const { data } = await sb.from("tg_support").select("user_chat_id")
      .eq("admin_message_id", m.reply_to_message.message_id).maybeSingle();
    if (data) {
      const r = await send(data.user_chat_id, "Kompas Lab javobi:\n\n" + text);
      await send(ADMIN_CHAT, r.ok ? "Yuborildi." : "Yuborilmadi: " + (r.description ?? r.status));
      return;
    }
  }
  if (m.chat.type !== "private") return;

  const [cmdRaw, ...rest] = text.split(/\s+/);
  const cmd = cmdRaw.startsWith("/") ? cmdRaw.split("@")[0].toLowerCase() : "";
  const arg = rest.join(" ");

  const { data: link } = await sb.from("tg_links").select("user_id").eq("chat_id", chatId).maybeSingle();

  switch (cmd) {
    case "/start": {
      if (/^[A-Za-z0-9_-]{20,64}$/.test(arg)) {
        const username = m.from?.username ?? null;
        const { data: uid, error } = await sb.rpc("fn_tg_consume_token", {
          p_token: arg, p_chat_id: chatId, p_username: username,
        });
        if (!error && uid) await sendLinkedWelcome(chatId, uid as string, username);
        else await send(chatId, T.badToken);
        return;
      }
      await send(chatId, link ? T.linked : T.welcome);
      return;
    }
    case "/holat":
      await send(chatId, link ? await statusText(link.user_id) : T.notLinked);
      return;
    case "/yordam":
    case "/help":
    case "/support":
      await send(chatId, T.help);
      return;
    case "/toxtat":
    case "/yoqish":
      if (!link) { await send(chatId, T.notLinked); return; }
      await sb.from("tg_links").update({ reminders_on: cmd === "/yoqish" }).eq("chat_id", chatId);
      await send(chatId, cmd === "/yoqish" ? T.remOn : T.remOff);
      return;
    case "/maxfiylik":
    case "/privacy":
      await send(chatId, T.privacy);
      return;
  }
  if (cmd) { await send(chatId, T.unknown); return; }

  // Oddiy matn = yordam soʻrovi. Soatiga cheklov.
  const since = new Date(Date.now() - 3600_000).toISOString();
  const { count } = await sb.from("tg_support").select("admin_message_id", { count: "exact", head: true })
    .eq("user_chat_id", chatId).gte("created_at", since);
  if ((count ?? 0) >= SUPPORT_LIMIT_PER_HOUR) { await send(chatId, T.limit); return; }

  let who = "Ulanmagan foydalanuvchi";
  if (link) {
    const { data: p } = await sb.from("profiles").select("full_name").eq("id", link.user_id).maybeSingle();
    who = (p?.full_name ?? "Talaba") + " · " + link.user_id.slice(0, 8);
  }
  const head = "Yordam soʻrovi\n" + who + (m.from?.username ? " · @" + m.from.username : "") +
    "\n(Javob berish uchun shu xabarga Reply qiling)\n\n";
  // Admin xabari foydalanuvchi botidan keladi: Reply ham shu botning webhookiga tushadi.
  const r = await tg(USER_TOKEN, "sendMessage", { chat_id: ADMIN_CHAT, text: toNew(head) + text });
  if (r.ok && r.result) {
    await sb.from("tg_support").insert({ admin_message_id: r.result.message_id, user_chat_id: chatId });
    await send(chatId, T.received);
  } else {
    console.error("support forward failed", r.status, r.description);
    await send(chatId, "Xabar yetkazilmadi. Keyinroq urinib koʻring yoki kompaslab.uz@gmail.com ga yozing.");
  }
}

// ---------- Navbat ----------
async function flush(): Promise<{ sent: number; failed: number }> {
  const { data } = await sb.from("tg_outbox").select("id, bot, chat_id, text_src, attempts")
    .is("sent_at", null).lt("attempts", 5).order("id").limit(50);
  let sent = 0, failed = 0;
  for (const row of data ?? []) {
    const r = await send(row.chat_id, row.text_src, row.bot === "admin" ? "admin" : "user");
    if (r.ok) {
      await sb.from("tg_outbox").update({ sent_at: new Date().toISOString(), attempts: row.attempts + 1 }).eq("id", row.id);
      sent++;
    } else {
      // 403: foydalanuvchi botni bloklagan. Qayta urinilmaydi.
      const final = r.status === 403 || r.status === 400;
      await sb.from("tg_outbox").update({
        attempts: final ? 5 : row.attempts + 1, last_error: `${r.status} ${r.description ?? ""}`.slice(0, 300),
      }).eq("id", row.id);
      if (r.status === 403 && row.bot === "user") {
        await sb.from("tg_links").update({ blocked_at: new Date().toISOString() }).eq("chat_id", row.chat_id);
      }
      failed++;
    }
    await new Promise((res) => setTimeout(res, 40)); // ~25 xabar/soniya
  }
  return { sent, failed };
}

// ---------- Webhookka callback_query ni yoqish ----------
async function setup(): Promise<Record<string, unknown>> {
  if (!WEBHOOK_SECRET) return { ok: false, error: "TG_WEBHOOK_SECRET yoʻq" };
  const info = await tg(USER_TOKEN, "getWebhookInfo", {});
  if (!info.ok) return { ok: false, error: "getWebhookInfo", status: info.status };
  const prevUrl: string = info.result?.url ?? "";
  // Webhook oʻrnatilmagan boʻlsa, shu funksiyaning oʻz manzili ishlatiladi.
  const url = prevUrl || WEBHOOK_URL;
  const prev = { url: prevUrl || null, allowed_updates: info.result?.allowed_updates ?? null };
  const r = await tg(USER_TOKEN, "setWebhook", {
    url, secret_token: WEBHOOK_SECRET, allowed_updates: ["message", "callback_query"],
  });
  const after = await tg(USER_TOKEN, "getWebhookInfo", {});
  return {
    ok: r.ok, description: r.description ?? null, prev,
    now: { url: after.result?.url ?? null, allowed_updates: after.result?.allowed_updates ?? null,
           last_error: after.result?.last_error_message ?? null },
  };
}

const json = (o: unknown, status = 200) =>
  new Response(JSON.stringify(o), { status, headers: { "content-type": "application/json" } });

export async function handle(req: Request): Promise<Response> {
  if (req.method !== "POST") return new Response("Method Not Allowed", { status: 405 });
  const path = new URL(req.url).pathname;

  if (path.endsWith("/webhook")) {
    if (!safeEq(req.headers.get("x-telegram-bot-api-secret-token") ?? "", WEBHOOK_SECRET)) {
      return new Response("Forbidden", { status: 403 });
    }
    try { await onUpdate(await req.json()); } catch (e) { console.error("onUpdate", e instanceof Error ? e.message : e); }
    return new Response("ok"); // Telegram qayta yubormasligi uchun har doim 200
  }

  // Quyidagi marshrutlar faqat Vault siri bilan (pg_net orqali) chaqiriladi.
  if (!safeEq(req.headers.get("x-kompas-flush") ?? "", FLUSH_SECRET)) {
    return new Response("Forbidden", { status: 403 });
  }
  if (path.endsWith("/flush")) return json(await flush());
  if (path.endsWith("/outreach")) return json(await outreachCards());
  if (path.endsWith("/setup")) return json(await setup());

  return new Response("Not Found", { status: 404 });
}

Deno.serve(handle);
