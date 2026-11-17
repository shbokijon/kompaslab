// Mamlakatlar xaritasi: brauzer testi (Playwright).
//   python3 -m http.server 8814 &
//   PW=$(npm root -g)/playwright node tools/atlas/test_mamlakatlar.cjs [skrinshot_papkasi]
const { chromium } = require(process.env.PW || "playwright");
const assert = require("assert");
const SHOTS = process.argv[2] || "";
(async () => {
  const b = await chromium.launch(); const errs = [];
  for (const [w, dark] of [[390, false], [1280, false], [1280, true]]) {
    const ctx = await b.newContext({ viewport: { width: w, height: 900 }, colorScheme: dark ? "dark" : "light" });
    await ctx.route(/fonts\.g|supabase|t\.me/, r => r.abort());
    const p = await ctx.newPage(); p.on("pageerror", e => errs.push(w + ": " + e.message));
    await p.goto("http://localhost:8814/mamlakatlar.html", { waitUntil: "load" });
    await p.waitForSelector("#mxMap svg .mx-bub");
    const tag = `${w}${dark ? "-dark" : ""}`;
    // boshlanish: Oʻzbekiston kartasi
    assert.ok((await p.textContent("#mxCard h2")).includes("zbekiston"), "Oʻzbekiston kartasi");
    assert.equal(await p.locator("#mxMap .mx-bub").count(), 10, "talabalar qatlami: 10 doira");
    // mamlakat tanlash
    await p.click('.mx-chip[data-iso="KOR"]'); await p.waitForTimeout(1500);
    assert.ok((await p.textContent("#mxCard h2")).includes("Koreya"));
    assert.equal(await p.locator("#mxCard .mx-kpi").count(), 3, "3 ta asosiy raqam");
    assert.ok((await p.textContent("#mxCard .mx-kpi b")).replace(/\s/g, "") === "3513", "sanab chiqish tugaydi");
    assert.ok((await p.getAttribute(".mx-arc", "d")).startsWith("M"), "Toshkentdan chiziq");
    // tab va izoh
    await p.click('#mxCard .mx-tab[data-g="Stipendiya"]');
    assert.ok((await p.textContent("#mxCard .mx-items")).includes("GKS"));
    await p.click("#mxCard .mx-i");
    assert.ok(await p.locator("#mxCard .mx-more:not([hidden]) a").count() === 1, "manba ochiladi");
    if (SHOTS && w === 1280) await p.screenshot({ path: `${SHOTS}/v2-${tag}-kor.png` });
    // xarita bosish (doira)
    await p.locator('#mxMap .mx-bub[data-iso="JPN"] circle').dispatchEvent("click"); await p.waitForTimeout(200);
    assert.ok((await p.textContent("#mxCard h2")).includes("Yaponiya"), "doira bosish");
    // qatlamlar
    await p.click('.mx-layer[data-layer="flow"]'); await p.waitForTimeout(300);
    assert.equal(await p.locator("#mxMap .mx-bub").count(), 10, "flow: 10 doira");
    await p.click('.mx-layer[data-layer="qs"]'); await p.waitForTimeout(300);
    assert.equal(await p.locator("#mxMap .mx-bub").count(), 9, "qs: 9 doira");
    assert.ok((await p.locator("#mxMap .mx-bub text").allTextContents()).includes("#1"));
    // hudud
    await p.click('[data-zoom="eu"]'); await p.waitForTimeout(900);
    const vb = (await p.getAttribute("#mxMap svg", "viewBox")).split(" ").map(Number);
    assert.ok(vb[2] < 200, "Yevropa yaqinlashdi " + vb);
    if (SHOTS) await p.screenshot({ path: `${SHOTS}/v2-${tag}-eu.png`, fullPage: w === 390 });
    const sw = await p.evaluate(() => document.documentElement.scrollWidth);
    if (w === 390) assert.ok(sw <= 392, "siljish " + sw);
    await ctx.close();
  }
  await b.close();
  if (errs.length) { console.error(errs); process.exit(1); }
  console.log("OK mamlakatlar");
})().catch(e => { console.error(e); process.exit(1); });
