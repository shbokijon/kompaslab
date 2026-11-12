/* Kompas Lab · Telegram botni hisobga ulash (2026-11-12)
 * Talaba saytda tugmani bosadi → t.me/yordam_klab_bot?start=<token> → bot /start <token> ni
 * fn_tg_consume_token bilan tg_links ga yozadi va shaxsiy salomlashuv xabarini yuboradi.
 * Bot foydalanuvchiga oʻzi birinchi yoza olmaydi (Telegram Bot API), shuning uchun «Start» shart.
 * Kerak: window.supabase (sessiya bilan). RPC: fn_tg_link_token() (authenticated).
 * Jadval: tg_links (RLS tg_links_own_read: faqat oʻz qatori).
 * API:
 *   KompasTgLink.isLinked()            → Promise<boolean>
 *   KompasTgLink.prepare(aEl)          → tokenni oldindan olib, <a> ga havola qoʻyadi
 *   KompasTgLink.watch(onLinked)       → 3 daqiqagacha har 3 soniyada tekshiradi
 *   KompasTgLink.mountCard(containerEl)→ ulanmagan boʻlsa kabinet kartasini chizadi
 */
(function () {
  "use strict";
  var BOT = "yordam_klab_bot";
  var TOKEN_TTL_MS = 12 * 60 * 1000; // bazada 15 daqiqa; zaxira bilan 12
  var tok = null, tokAt = 0, watching = false;

  function sb() { return window.supabase && typeof window.supabase.rpc === "function" ? window.supabase : null; }

  async function uid() {
    var s = sb(); if (!s) return null;
    try { var r = await s.auth.getSession(); return r && r.data && r.data.session ? r.data.session.user.id : null; }
    catch (e) { return null; }
  }

  async function isLinked() {
    var s = sb(), id = await uid();
    if (!s || !id) return false;
    var r = await s.from("tg_links").select("chat_id, blocked_at").eq("user_id", id).maybeSingle();
    return !!(r && r.data && r.data.chat_id && !r.data.blocked_at);
  }

  async function freshUrl() {
    if (tok && Date.now() - tokAt < TOKEN_TTL_MS) return "https://t.me/" + BOT + "?start=" + tok;
    var s = sb(); if (!s) throw new Error("no client");
    var r = await s.rpc("fn_tg_link_token");
    if (r.error || !r.data) throw r.error || new Error("no token");
    tok = r.data; tokAt = Date.now();
    return "https://t.me/" + BOT + "?start=" + tok;
  }

  function prepare(a, onClickExtra) {
    if (!a) return;
    a.setAttribute("target", "_blank");
    a.setAttribute("rel", "noopener");
    freshUrl().then(function (u) { a.href = u; }).catch(function () { a.href = "https://t.me/" + BOT; });
    a.addEventListener("click", function (e) {
      if (a.dataset.ktgDone) return; // ulandi: tugma endi oddiy havola
      if (!tok || Date.now() - tokAt >= TOKEN_TTL_MS) {
        e.preventDefault();
        freshUrl().then(function (u) { a.href = u; window.location.href = u; })
          .catch(function () { window.location.href = "https://t.me/" + BOT; });
      }
      if (typeof onClickExtra === "function") onClickExtra();
    });
  }

  function watch(onLinked) {
    if (watching) return; watching = true;
    var tries = 0;
    var t = setInterval(async function () {
      tries++;
      var ok = false;
      try { ok = await isLinked(); } catch (e) { ok = false; }
      if (ok || tries >= 60) { clearInterval(t); watching = false; }
      if (ok && typeof onLinked === "function") onLinked();
    }, 3000);
  }

  var CSS = ".ktg-card{display:flex;gap:14px;align-items:flex-start;background:#fff;border:1px solid #e0e8e4;border-left:4px solid #2d4a3e;border-radius:14px;padding:16px 18px;margin:0 0 18px}" +
    ".ktg-ico{flex:0 0 40px;height:40px;border-radius:50%;background:#e8f0ec;display:flex;align-items:center;justify-content:center}" +
    ".ktg-b{flex:1;min-width:0}.ktg-t{font-weight:700;color:#1a2e26;margin:0 0 4px;font-size:15px}" +
    ".ktg-p{margin:0 0 10px;color:#4a5f56;font-size:14px;line-height:1.5}" +
    ".ktg-btn{display:inline-block;background:#2d4a3e;color:#fff;text-decoration:none;font-weight:700;font-size:14px;padding:9px 16px;border-radius:9px}" +
    ".ktg-btn:hover{background:#1e3329}.ktg-h{display:block;margin-top:8px;color:#6b7f76;font-size:12.5px}" +
    ".ktg-ok{color:#2d4a3e;font-weight:700;font-size:14px}" +
    ".ktg-x{flex:0 0 auto;border:0;background:none;color:#9aada6;font-size:18px;line-height:1;cursor:pointer;padding:2px 4px}";
  var ICON = "<svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" aria-hidden=\"true\"><path fill=\"#2d4a3e\" d=\"M21.5 4.2 2.9 11.4c-1.3.5-1.3 1.2-.2 1.6l4.8 1.5 1.8 5.6c.2.6.4.8.9.8.4 0 .6-.2.9-.4l2.3-2.2 4.7 3.5c.9.5 1.5.2 1.7-.8l3.1-14.6c.3-1.3-.5-1.8-1.4-1.2zM9.7 14.4l-.4 4-1.4-4.6 10.6-6.7z\"/></svg>";
  var HIDE_KEY = "kompas_tg_card_hide_v1";

  async function mountCard(box) {
    if (!box) return;
    try { if (localStorage.getItem(HIDE_KEY) && Date.now() - Number(localStorage.getItem(HIDE_KEY)) < 7 * 864e5) return; } catch (e) {}
    if (!(await uid())) return;
    if (await isLinked()) return;
    if (!document.getElementById("ktg-css")) {
      var st = document.createElement("style"); st.id = "ktg-css"; st.textContent = CSS; document.head.appendChild(st);
    }
    box.innerHTML =
      "<div class=\"ktg-card\" role=\"region\" aria-label=\"Telegram bot\">" +
        "<div class=\"ktg-ico\">" + ICON + "</div>" +
        "<div class=\"ktg-b\">" +
          "<p class=\"ktg-t\">Telegram botni hisobingizga ulang</p>" +
          "<p class=\"ktg-p\">Toʻlovingiz qabul qilingani, obunangiz muddati va savollaringizga javob shu botga keladi. Bot faqat sizning hisobingizga oid xabar yozadi.</p>" +
          "<a class=\"ktg-btn\" id=\"ktgBtn\" href=\"https://t.me/" + BOT + "\">Telegramda ulash</a>" +
          "<span class=\"ktg-h\" id=\"ktgHint\">Telegram ochiladi: «Start» (Boshlash) tugmasini bosing.</span>" +
        "</div>" +
        "<button type=\"button\" class=\"ktg-x\" id=\"ktgX\" aria-label=\"Yopish\">×</button>" +
      "</div>";
    box.hidden = false;
    prepare(document.getElementById("ktgBtn"), function () {
      document.getElementById("ktgHint").textContent = "Botda «Start» ni bosgach, bu yer oʻzi yangilanadi.";
      watch(function () {
        box.querySelector(".ktg-b").innerHTML = "<p class=\"ktg-ok\">Telegram ulandi. Botdagi xabarni koʻring.</p>";
        var x = document.getElementById("ktgX"); if (x) x.remove();
        setTimeout(function () { box.hidden = true; }, 6000);
      });
    });
    document.getElementById("ktgX").addEventListener("click", function () {
      try { localStorage.setItem(HIDE_KEY, String(Date.now())); } catch (e) {}
      box.hidden = true;
    });
  }

  window.KompasTgLink = { isLinked: isLinked, prepare: prepare, watch: watch, mountCard: mountCard, freshUrl: freshUrl };
})();
