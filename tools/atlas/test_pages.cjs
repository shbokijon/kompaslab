// Atlas registr sahifalari va Bepul reja: brauzer testi (Playwright).
//   python3 -m http.server 8814 &
//   PW=$(npm root -g)/playwright node tools/atlas/test_pages.cjs [skrinshot_papkasi]
// Registr maʼlumoti sinov nusxasi bilan almashtiriladi (haqiqiy kompaniya emas, saytga chiqmaydi).
const { chromium } = require(process.env.PW || "playwright");
const assert = require("assert");
const SHOTS = process.argv[2] || "";
const BASE = "http://localhost:8814/";
const NL = { schema: 1, source: "x", last_updated: "2026-10-05", retrieved_at: "2026-10-30", count: 3, fields: ["name", "kvk"],
  rows: [["Alfa Test B.V.", "11111111"], ["Beta Test B.V.", "22222222"], ["Shell Test N.V.", "33333333"]] };
const CA = { schema: 1, source: "x", period: "2026-Q1", retrieved_at: "2026-10-30", count: 2, provinces: ["Alberta", "Ontario"],
  fields: [], rows: [["Acme Test Inc.", "Ontario", "Toronto, ON", "21231-Software engineers", "High-wage", 2], ["Farm Test Ltd", "Alberta", "Red Deer, AB", "85100-Livestock labourers", "Agricultural stream", 3]] };

(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, acceptDownloads: true });
  await ctx.route(/fonts\.g|supabase|t\.me/, r => r.abort());
  await ctx.route(/data\/nl-sponsors\.json/, r => r.fulfill({ contentType: "application/json", body: JSON.stringify(NL) }));
  await ctx.route(/data\/ca-lmia\.json/, r => r.fulfill({ contentType: "application/json", body: JSON.stringify(CA) }));
  const errs = [];
  const open = async (u) => { const p = await ctx.newPage(); p.on("pageerror", e => errs.push(u + ": " + e.message)); await p.goto(BASE + u, { waitUntil: "load" }); await p.waitForTimeout(400); return p; };

  // NL qidiruv
  let p = await open("nl-sponsors.html");
  assert.equal(await p.locator(".ar-card").count(), 3);
  await p.fill("#arQ", "beta"); await p.waitForTimeout(300);
  assert.equal(await p.locator(".ar-card").count(), 1);
  assert.equal(await p.locator(".ar-card h3").first().textContent(), "Beta Test B.V.");
  await p.fill("#arQ", "shell"); await p.waitForTimeout(300);
  assert.equal(await p.locator(".ar-card h3").first().textContent(), "Shell Test N.V.", "nom alifbo bilan buzilmasligi kerak");
  if (SHOTS) await p.screenshot({ path: SHOTS + "/nl.png", fullPage: true });
  await p.close();

  // CA qidiruv + provinsiya
  p = await open("ca-lmia.html");
  assert.equal(await p.locator(".ar-card").count(), 2);
  await p.selectOption("#arF", "Alberta"); await p.waitForTimeout(200);
  assert.equal(await p.locator(".ar-card").count(), 1);
  await p.fill("#arQ", "software"); await p.waitForTimeout(300);
  assert.equal(await p.locator(".ar-empty").count(), 1);
  if (SHOTS) await p.screenshot({ path: SHOTS + "/ca.png", fullPage: true });
  await p.close();

  // Maʼlumot yoʻq bo'lsa: ogohlantirish, JS xatosi yoʻq
  const ctx2 = await b.newContext({ viewport: { width: 390, height: 844 } });
  await ctx2.route(/fonts\.g|supabase|t\.me/, r => r.abort());
  await ctx2.route(/data\/nl-sponsors\.json/, r => r.fulfill({ status: 404, body: "" }));
  const p2 = await ctx2.newPage(); p2.on("pageerror", e => errs.push("nl404: " + e.message));
  await p2.goto(BASE + "nl-sponsors.html"); await p2.waitForTimeout(400);
  assert.ok((await p2.getAttribute("#arStat", "class")).includes("warn"));
  await ctx2.close();

  // Bepul reja: GKS treki
  p = await open("master-planner.html?lab=gks");
  assert.equal(await p.locator("#taskList li").count(), 6);
  await p.selectOption("#degree", "D"); await p.waitForTimeout(150);
  const ids = await p.locator("#taskList label").allTextContents();
  assert.ok(ids.some(t => t.startsWith("M3-D")) && !ids.some(t => t.startsWith("M3-U")));
  await p.check("#t_M0");
  assert.ok((await p.textContent("#next")).includes("M1"));
  // eksport → tozalash → import
  const [dl] = await Promise.all([p.waitForEvent("download"), p.click("#export")]);
  const file = await dl.path();
  p.once("dialog", d => d.accept()); await p.click("#clear"); await p.waitForTimeout(150);
  assert.equal(await p.isChecked("#t_M0"), false);
  p.once("dialog", d => d.accept());
  await p.setInputFiles("#importFile", file); await p.waitForTimeout(400);
  assert.equal(await p.isChecked("#t_M0"), true, "import ishlamadi");
  if (SHOTS) await p.screenshot({ path: SHOTS + "/reja-gks.png", fullPage: true });
  await p.close();

  // Master: eski kalit (kabinet oʻqiydi) saqlanadi
  p = await open("master-planner.html?lab=master");
  await p.check("#t_M1");
  const key = await p.evaluate(() => JSON.parse(localStorage.getItem("kompas-master-planner-v1")).tasks.M1);
  assert.equal(key, true);
  await p.close();

  // Atlas va maqolalar
  for (const u of ["atlas.html", "atlas-talaba-ishi.html", "atlas-professorga-xat.html", "atlas-ingliz-tili-testi.html"]) {
    p = await open(u);
    const sw = await p.evaluate(() => document.documentElement.scrollWidth);
    assert.ok(sw <= 392, u + " overflow " + sw);
    if (SHOTS) await p.screenshot({ path: SHOTS + "/" + u.replace(".html", ".png"), fullPage: true });
    await p.close();
  }
  assert.deepEqual(errs, []);
  console.log("Atlas va Bepul reja testlari: OK");
  await b.close();
})().catch(e => { console.error(e); process.exit(1); });
