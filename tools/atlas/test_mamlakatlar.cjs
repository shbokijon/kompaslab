// Mamlakatlar xaritasi: brauzer testi (Playwright).
//   python3 -m http.server 8814 &
//   PW=$(npm root -g)/playwright node tools/atlas/test_mamlakatlar.cjs [skrinshot_papkasi]
const { chromium } = require(process.env.PW || "playwright");
const assert = require("assert");
const SHOTS = process.argv[2] || "";
(async () => {
  const b = await chromium.launch(); const errs = [];
  for (const [w, dark] of [[390, false], [1280, false], [1280, true]]) {
    const ctx = await b.newContext({ viewport: { width: w, height: w < 500 ? 844 : 900 }, colorScheme: dark ? "dark" : "light", hasTouch: w < 500, isMobile: w < 500 });
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
    if (w < 500) {
      assert.ok(await p.locator("#mxCard.is-sheet").count() === 1, "telefonda pastki panel");
      const mh = (await p.locator("#mxMap svg").boundingBox()).height;
      assert.ok(mh >= 190, "telefonda xarita balandligi " + mh);
      await p.click("#mxCard [data-sheet=toggle]");
      assert.ok(await p.locator("#mxCard.is-full").count() === 1, "panel kattalashadi");
    }
    // tab va izoh
    await p.click('#mxCard .mx-tab[data-g="Stipendiya"]');
    assert.ok((await p.textContent("#mxCard .mx-items")).includes("GKS"));
    await p.click("#mxCard .mx-i");
    assert.ok(await p.locator("#mxCard .mx-more:not([hidden]) a").count() === 1, "manba ochiladi");
    if (SHOTS) await p.screenshot({ path: `${SHOTS}/v3-${tag}-kor.png` });
    if (w < 500) { await p.click("#mxCard [data-sheet=close]"); assert.ok(await p.locator("#mxCard.is-sheet").count() === 0, "panel yopiladi"); }
    // xarita bosish (doira)
    await p.locator('#mxMap .mx-bub[data-iso="JPN"] circle').dispatchEvent("click"); await p.waitForTimeout(200);
    assert.ok((await p.textContent("#mxCard h2")).includes("Yaponiya"), "doira bosish");
    if (w < 500) {
      const before = (await p.getAttribute("#mxMap svg", "viewBox")).split(" ").map(Number)[0];
      await p.click('.mx-chip[data-iso="USA"]'); await p.waitForTimeout(900);
      const after = (await p.getAttribute("#mxMap svg", "viewBox")).split(" ").map(Number)[0];
      assert.ok(after < before, "AQSh tanlanganda xarita suriladi");
      await p.click("#mxCard [data-sheet=close]");
    }
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
    if (SHOTS) await p.screenshot({ path: `${SHOTS}/v3-${tag}-eu.png`, fullPage: w === 390 });
    // diagrammalar
    await p.locator(".mx-charts").scrollIntoViewIfNeeded(); await p.waitForTimeout(1200);
    assert.equal(await p.locator(".mx-cpanel:not([hidden])").count(), 1, "bitta diagramma ko'rinadi");
    assert.equal(await p.locator('.mx-cpanel[data-chart="talabalar"] .mx-row').count(), 10, "talabalar: 10 ustun");
    const w0 = await p.evaluate(() => getComputedStyle(document.querySelector('.mx-cpanel[data-chart="talabalar"] .mx-rt i')).width);
    assert.ok(parseFloat(w0) > 50, "ustun o'sdi " + w0);
    await p.click('.mx-ctabs [data-chart="flow"]'); await p.waitForTimeout(1100);
    assert.equal(await p.locator('.mx-cpanel[data-chart="flow"] .mx-row').count(), 10, "flow: 10 ustun");
    if (SHOTS) await p.locator(".mx-charts").screenshot({ path: `${SHOTS}/chart-${tag}-flow.png` });
    await p.click('.mx-ctabs [data-chart="uz"]'); await p.waitForTimeout(1100);
    assert.ok(await p.locator('.mx-cpanel[data-chart="uz"] .mx-row').count() >= 3, "o'zbek talabalar");
    await p.click('.mx-ctabs [data-chart="qs"]'); await p.waitForTimeout(1100);
    if (SHOTS) await p.locator(".mx-charts").screenshot({ path: `${SHOTS}/chart-${tag}-qs.png` });
    await p.click('.mx-ctabs [data-chart="talabalar"]'); await p.waitForTimeout(1100);
    if (SHOTS) await p.locator(".mx-charts").screenshot({ path: `${SHOTS}/chart-${tag}-tal.png` });
    await p.click('.mx-cpanel[data-chart="talabalar"] button.mx-row[data-iso="DEU"]'); await p.waitForTimeout(600);
    assert.ok((await p.textContent("#mxCard h2")).includes("Germaniya"), "ustun bosilsa xaritada ochiladi");
    const sw = await p.evaluate(() => document.documentElement.scrollWidth);
    if (w === 390) assert.ok(sw <= 392, "siljish " + sw);
    await ctx.close();
  }
  await b.close();
  if (errs.length) { console.error(errs); process.exit(1); }
  console.log("OK mamlakatlar");
})().catch(e => { console.error(e); process.exit(1); });
