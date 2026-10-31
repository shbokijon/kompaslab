// USA M1–M8 toʻliq oqim testi (yuklab olinadigan dist/ versiya, 390px):
// har dars 4 qism → yakunlash, mini-test, vosita, nazorat roʻyxati, halollik, yakun → 250 XP.
//   PW=$(npm root -g)/playwright node tools/modules/usa/browser_test.js 1 2 ...
const path = require("path");
const { chromium } = require(process.env.PW || "playwright");
const ROOT = path.resolve(__dirname, "../../..");
(async () => {
  const ns = process.argv.slice(2).length ? process.argv.slice(2) : Array.from({length: 8}, (_, i) => String(i + 1));
  const b = await chromium.launch(); let bad = 0;
  for (const n of ns) {
    const ctx = await b.newContext({ viewport: { width: 390, height: 800 } });
    const p = await ctx.newPage(); const errs = [];
    p.on("pageerror", e => errs.push(e.message));
    p.on("dialog", d => d.dismiss());
    await ctx.route(/^https?:/, r => r.fulfill({ status: 200, contentType: "text/plain", body: "" }));
    await p.goto("file://" + ROOT + "/tools/modules/dist/usa-lab-m" + n + ".html");
    await p.waitForTimeout(300);
    const nl = await p.$$eval(".lesson", l => l.length);
    for (let k = 1; k <= nl; k++) {
      if (!(await p.$(`#l${k}.open`))) await p.click(`#l${k} .l-head`);
      for (let i = 0; i < 4; i++) await p.click(`#l${k} .tab >> nth=${i}`);
      // mini-test shu darsda boʻlsa, hamma savolga javob
      const qs = await p.$$(`#l${k} .qz`);
      for (const q of qs) { const a = await q.getAttribute("data-a"); await (await q.$(`button[data-v="${a}"]`)).click(); }
      const ta = await p.$(`#l${k} textarea[data-save]`);
      if (ta) await ta.fill("Sinov javobi " + k + ": aniq dalil va sana bilan.");
      await p.click(`[data-complete="l${k}"]`); await p.waitForTimeout(850);
    }
    for (const el of await p.$$("#toolBtn >> xpath=.. >> [data-save]")) {
      const tag = await el.evaluate(e => e.tagName);
      if (tag === "SELECT") await el.selectOption({ index: (await el.$$eval("option", o => o.length)) - 1 }); else if ((await el.getAttribute("type")) === "date") await el.fill("2027-03-01"); else await el.fill("Sinov qiymati, 12 ta soʻz: bu maydon test uchun toʻldirildi va saqlandi.");
    }
    await p.waitForTimeout(450);
    await p.click("#toolBtn"); await p.waitForTimeout(150);
    for (const c of await p.$$("#check [data-ck] input")) await c.check();
    await p.click("#ckBtn"); await p.waitForTimeout(150);
    await p.check('[data-ck="hon"] input');
    await p.click("#finBtn"); await p.waitForTimeout(400);
    const r = await p.evaluate(() => ({ xp: +document.getElementById("xpN").textContent, sw: document.documentElement.scrollWidth, broken: [...document.images].filter(i => i.complete && i.naturalWidth === 0).length, lvl: document.getElementById("lvl").textContent, badges: document.querySelectorAll(".bdg.on").length }));
    const ok = !errs.length && r.xp === 250 && r.sw <= 390 && !r.broken && r.badges === 6;
    if (!ok) bad++;
    console.log(ok ? "✓" : "✗", n, JSON.stringify({ nl, ...r }), errs.slice(0, 3));
    await ctx.close();
  }
  await b.close(); process.exit(bad ? 1 : 0);
})();
