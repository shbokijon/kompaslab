Deno.serve(async (req) => {
  try {
    const token = Deno.env.get("TELEGRAM_BOT_TOKEN") || ""
    const chat  = Deno.env.get("TELEGRAM_ADMIN_CHAT_ID") || ""
    const body  = await req.json()
    const type  = body.type || ""
    const data  = body.data || {}

    let text = ""

    if (type === "new_user") {
      text = "Yangi talaba!\n\n"
        + "Ism: " + (data.full_name || "Nomsiz") + "\n"
        + "Email: " + (data.email || "") + "\n"
        + "Vaqt: " + new Date().toLocaleString("uz-UZ") + "\n\n"
        + "Admin: https://kompaslab.uz/admin.html"
    } else if (type === "new_payment") {
      text = "Yangi to'lov!\n\n"
        + "Talaba: " + (data.full_name || "Noma'lum") + "\n"
        + "Kurs: " + (data.course || "---") + "\n"
        + "Summa: " + (data.amount || "0") + " so'm\n"
        + "Vaqt: " + new Date().toLocaleString("uz-UZ") + "\n\n"
        + "Admin: https://kompaslab.uz/admin.html"
    } else if (type === "test") {
      text = "Kompas Lab - Test muvaffaqiyatli! Telegram ishlayapti."
    }

    if (text && token && chat) {
      const url = "https://api.telegram.org/bot" + token + "/sendMessage"
      await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ chat_id: chat, text: text })
      })
    }

    return new Response(JSON.stringify({ ok: true }), {
      headers: { "Content-Type": "application/json" }
    })
  } catch (err) {
    const msg = err instanceof Error ? err.message : String(err)
    return new Response(JSON.stringify({ error: msg }), {
      status: 500,
      headers: { "Content-Type": "application/json" }
    })
  }
})
