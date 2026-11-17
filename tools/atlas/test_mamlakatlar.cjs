// Mamlakatlar xaritasi: brauzer testi (Playwright).
//   python3 -m http.server 8814 &
//   PW=$(npm root -g)/playwright node tools/atlas/test_mamlakatlar.cjs [skrinshot_papkasi]
const { chromium } = require(process.env.PW || "playwright");
const assert = require("assert");
const SHOTS = process.argv[2] || "";
(async () => {
  const b = await chromium.launch(); const errs = [];
  for (const w of [390, 1280]) {
    const ctx = await b.newContext({ viewport: { width: w, height: 900 } });
    await ctx.route(/fonts\.g|supabase|t\.me/, r => r.abort());
    const p = await ctx.newPage(); p.on("pageerror", e => errs.push(w + ": " + e.message));
    await p.goto("http://localhost:8814/mamlakatlar.html", { waitUntil: "load" });
    await p.waitForSelector("#mxMap svg path.is-on");
    assert.ok(await p.locator("#mxMap path.is-home").count() === 1, "Oʻzbekiston belgilangan");
    assert.ok(await p.locator("#mxMap .is-on").count() >= 12, "12 mamlakat");
    assert.ok(await p.locator("details.mx-c").count() === 13);
    assert.ok(await p.locator("#mx-UZB[open]").count() === 1, "Oʻzbekiston kartasi ochiq");
    await p.click('.mx-chip[data-iso="KOR"]'); await p.waitForTimeout(300);
    assert.ok(await p.locator("#mx-KOR[open]").count() === 1, "chip kartani ochadi");
    assert.ok(await p.locator("#mx-UZB[open]").count() === 0);
    assert.ok((await p.getAttribute(".mx-arc", "d")).startsWith("M"), "Toshkentdan chiziq");
    if (w === 1280) { await p.locator('#mxMap path[data-iso="JPN"]').dispatchEvent("click"); await p.waitForTimeout(300); assert.ok(await p.locator("#mx-JPN[open]").count() === 1, "xarita bosish"); }
    await p.click('.mx-layer[data-layer="flow"]'); await p.waitForTimeout(200);
    assert.ok(await p.locator("#mxMap .is-flow").count() >= 9, "flow qatlami");
    const txt = await p.textContent("h1");
    assert.ok(txt.includes("Mamlakatlar"), txt);
    const sw = await p.evaluate(() => document.documentElement.scrollWidth);
    if (w === 390) assert.ok(sw <= 392, "siljish " + sw);
    if (SHOTS) { await p.screenshot({ path: `${SHOTS}/mx-flow-${w}.png` }); await p.click('.mx-layer[data-layer="atlas"]'); await p.waitForTimeout(500); await p.screenshot({ path: `${SHOTS}/mx-${w}.png`, fullPage: false }); }
    await ctx.close();
  }
  await b.close();
  if (errs.length) { console.error(errs); process.exit(1); }
  console.log("OK mamlakatlar");
})().catch(e => { console.error(e); process.exit(1); });
