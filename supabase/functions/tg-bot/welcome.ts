// Kompas Lab · tg-bot · hisob ulangandagi shaxsiy salomlashuv (2026-11-12)
// Matn manbada amaldagi alifboda; yuborishda index.ts dagi toNew() yangi alifboga oʻgiradi.
// Halollik: raqam, vaʼda va soxta shoshilinchlik yoʻq. Faqat talabaning oʻz holati.
// deno-lint-ignore-file no-explicit-any

const SITE = "https://kompaslab.uz/";
const UTM = "utm_source=bot&utm_medium=xat&utm_campaign=tg_welcome";

// slug → [nom, M0 fayl prefiksi]
const LABS: Record<string, [string, string]> = {
  "master-lab": ["Master Lab", "master-lab"],
  "bachelor-lab": ["Bachelor Lab", "bachelor-lab"],
  "phd-lab": ["PhD Lab", "phd-lab"],
  "gks-lab": ["GKS Lab", "gks-lab"],
  "usa-lab": ["USA Lab", "usa-lab"],
  "tadbirkor-talaba": ["Tadbirkor Talaba", "tadbirkor-talaba"],
  "miggo": ["Musofir Lab", "musofir-lab"],
};
// kompas_user_state kaliti: kompas_<k>_m0_v1
const STATE_KEY: Record<string, string> = {
  master: "master-lab", bachelor: "bachelor-lab", phd: "phd-lab", gks: "gks-lab",
  usa: "usa-lab", tt: "tadbirkor-talaba", musofir: "miggo",
};
// Roʻyxatdan oʻtishdagi maqsad (user_metadata.goal)
const GOAL: Record<string, string> = {
  masters: "master-lab", bachelor: "bachelor-lab", phd: "phd-lab",
  business: "tadbirkor-talaba", work: "miggo",
};

const url = (path: string) => SITE + path + (path.includes("?") ? "&" : "?") + UTM;

export type Welcome = { text: string; button?: { text: string; url: string }; adminLine: string };

export async function buildWelcome(sb: any, userId: string, tgUsername: string | null): Promise<Welcome> {
  const { data: p } = await sb.from("profiles").select("first_name, full_name").eq("id", userId).maybeSingle();
  const name = (p?.first_name || (p?.full_name ?? "").split(" ")[0] || "").trim();
  const hello = name ? `${name}, Kompas Lab botiga xush kelibsiz.` : "Kompas Lab botiga xush kelibsiz.";

  // 1) Faol obuna
  const { data: en } = await sb.from("enrollments")
    .select("expires_at, frozen_at, payment_status, courses(title, slug)")
    .eq("user_id", userId).in("payment_status", ["paid", "partial"]);
  const now = Date.now();
  const active = (en ?? []).find((e: any) => !e.frozen_at && (!e.expires_at || Date.parse(e.expires_at) > now));

  // 2) Oxirgi ochilgan M0 va undagi joy
  let slug: string | null = null, nextLesson = 0, m0Done = false;
  const { data: st } = await sb.from("kompas_user_state").select("key, value")
    .eq("user_id", userId).like("key", "kompas_%_m0_v1").order("updated_at", { ascending: false }).limit(1);
  const row = st?.[0];
  if (row) {
    const k = /^kompas_([a-z]+)_m0_v1$/.exec(row.key)?.[1] ?? "";
    slug = STATE_KEY[k] ?? null;
    const v = row.value ?? {};
    const total = Object.keys(v.seen ?? {}).length;
    const done = v.done ?? {};
    if (total > 0) {
      for (let i = 1; i <= total; i++) if (!done["l" + i]) { nextLesson = i; break; }
      m0Done = nextLesson === 0;
    }
  }
  // 3) Boʻlmasa, roʻyxatdagi maqsad
  if (!slug) {
    const { data: au } = await sb.auth.admin.getUserById(userId);
    slug = GOAL[au?.user?.user_metadata?.goal ?? ""] ?? null;
  }

  const lines: string[] = [hello, "Hisobingiz ulandi.", ""];
  let button: Welcome["button"];

  if (active) {
    const c: any = (active as any).courses ?? {};
    lines.push(`Sizda ${c.title ?? "Lab"} obunasi bor. Muddat va bosqich: /holat`);
    button = { text: "Kabinetni ochish →", url: url("dashboard.html") };
  } else if (slug && LABS[slug]) {
    const [title, pre] = LABS[slug];
    lines.push(`Sizning yoʻlingiz: ${title}.`);
    lines.push("Kompas yoʻli 4 bosqichdan iborat: Kirish → Ketish → Kampus → Karyera. Siz hozir Kirish bosqichidasiz: tayyorgarlik va hujjatlar.");
    lines.push("");
    if (m0Done) {
      lines.push("M0 ni tugatgansiz. Keyingi qadam: tarifni tanlab, M1 ni ochish.");
      button = { text: "Tariflarni koʻrish →", url: url(`${pre}-narxlar.html`) };
    } else if (nextLesson > 1) {
      lines.push(`Keyingi qadamingiz: M0 ning ${nextLesson}-darsi. M0 bepul.`);
      button = { text: `${nextLesson}-darsni ochish →`, url: url(`${pre}-m0-${nextLesson}.html`) };
    } else {
      lines.push("Keyingi qadamingiz: M0 ning 1-darsi. M0 bepul.");
      button = { text: "1-darsni boshlash →", url: url(`${pre}-m0-1.html`) };
    }
  } else {
    lines.push("Qaysi Lab sizga mosligini kabinetdagi savol aniqlab beradi.");
    button = { text: "Kabinetni ochish →", url: url("dashboard.html") };
  }

  lines.push("",
    "Bu chatga nima keladi:",
    "• toʻlovingiz qabul qilinganda tasdiq",
    "• obunangiz muddati tugashidan oldin eslatma",
    "• savolingizga jamoa javobi (savolni shu yerga yozing)",
    "",
    "/holat: obuna holati\n/toxtat: eslatmalarni oʻchirish");

  const adminLine = "🔗 Telegram ulandi: " + (p?.full_name || "Talaba") + (tgUsername ? " · @" + tgUsername : "") +
    (slug && LABS[slug] ? " · " + LABS[slug][0] : "") + (active ? " · obunachi" : "");
  return { text: lines.join("\n"), button, adminLine };
}
