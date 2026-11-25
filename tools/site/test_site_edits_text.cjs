// Admin → Vebsayt: murakkab bloklarda matn boʻlaklari (kind 'text', 2026-11-25) va kompas-ui.js siz sahifalar.
//   python3 -m http.server 8814 &
//   PW=$(npm root -g)/playwright node tools/site/test_site_edits_text.cjs
const fs = require("fs");
const { chromium } = require(process.env.PW || "playwright");
const BASE = "http://localhost:8814/";
const STUB = eval(fs.readFileSync(__dirname + "/test_site_edits.cjs", "utf8").match(/const STUB = (`[\s\S]*?`);/)[1]);
let fails = 0;
const ok = (c, m) => { console.log((c ? "✓ " : "✗ ") + m); if (!c) fails++; };
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 1280, height: 900 } });
  let restRows = [];
  await ctx.route(/fonts\.g|supabase\.co|open-meteo|t\.me|vimeo/, r => r.abort());
  await ctx.route(/supabase-js/, r => r.fulfill({ contentType: "text/javascript", body: STUB }));
  await ctx.route(/supabase\.co\/rest\/v1\/site_edits/, r => {
    const u = new URL(r.request().url()), pg = (u.searchParams.get("page") || "").replace(/^eq\./, "");
    r.fulfill({ contentType: "application/json", body: JSON.stringify(restRows.filter(x => x.page === pg && x.status === "active").map(({ id, sel, kind, guard, value }) => ({ id, sel, kind, guard, value }))) });
  });
  const errs = [];
  const page = async (url) => { const p = await ctx.newPage(); p.on("pageerror", e => errs.push(url + ": " + e.message)); await p.goto(BASE + url, { waitUntil: "load" }); await p.waitForTimeout(1200); return p; };
  const sh = p => p.locator("#kse-host");

  // 1) murakkab blok (ikonka + ⓘ + tugmalar): hero .wrap
  let p = await page("bachelor-lab.html?kedit=1");
  await p.evaluate(() => localStorage.removeItem("stubdb"));
  await p.click("header .crumb", { position: { x: 200, y: 6 } });
  await sh(p).locator('[data-a="up"]').click();
  const lbl = await sh(p).locator(".lbl").textContent();
  ok(/^<div/.test(lbl), "ota blok tanlandi: " + lbl.slice(0, 40));
  ok(!(await sh(p).locator('[data-a="edit"]').isDisabled()), "murakkab blokda tahrirlash tugmasi ochiq");
  const before = await p.evaluate(() => ({ img: document.querySelectorAll("header .wrap img").length, det: document.querySelectorAll("header .wrap details").length, a: document.querySelectorAll("header .wrap a[data-snd]").length }));
  await sh(p).locator('[data-a="edit"]').click();
  const nTa = await sh(p).locator("textarea[data-ti]").count();
  ok(nTa >= 5, "matn boʻlaklari maydonlari: " + nTa);
  // sahifadagi tugma matnini bosish mos maydonni tanlaydi
  await p.click("header .km-cta a.btn-g");
  const fi = await p.evaluate(() => { const a = document.getElementById("kse-host").shadowRoot.activeElement; return a && a.getAttribute("data-ti"); });
  const want = await p.evaluate(() => { const K = KSiteEdits, el = document.querySelector("header .wrap"); return String(K.tnodes(el).findIndex(n => n.parentNode.classList && n.parentNode.classList.contains("btn-g"))); });
  ok(fi === want, "sahifada bosilgan matn maydoni tanlandi (" + fi + ")");
  ok(p.url().includes("bachelor-lab.html"), "tugma bosilganda sahifa ochilmadi");
  const ta = sh(p).locator('textarea[data-ti="' + want + '"]');
  await ta.fill("Narxlar va tariflar");
  ok(await p.evaluate(() => document.querySelector("header .km-cta a.btn-g").textContent) === "Narxlar va tariflar", "sahifada darhol koʻrinadi");
  await ta.press("ArrowLeft"); // sahifa ←/→ navigatsiyasi ishlamasin
  await p.waitForTimeout(200);
  ok(p.url().includes("bachelor-lab.html"), "maydonda ← bosish sahifani almashtirmadi");
  // boʻsh maydon saqlanmaydi
  const first = sh(p).locator('textarea[data-ti="0"]');
  const v0 = await first.inputValue();
  await first.fill(" ");
  await sh(p).locator('[data-a="save"]').click();
  ok(/böş|boʻsh/.test(await sh(p).locator(".msg").textContent()), "boʻsh maydon rad etildi");
  await first.fill(v0);
  await sh(p).locator('textarea[data-ti="0"]').fill("Barcha dasturlar ögiş");
  await sh(p).locator('[data-a="save"]').click();
  await p.waitForTimeout(400);
  const db = await p.evaluate(() => JSON.parse(localStorage.getItem("stubdb") || "[]"));
  const row = db.find(r => r.kind === "text");
  ok(!!row, "text yozuvi saqlandi");
  const val = row && JSON.parse(row.value);
  ok(val && val.n === nTa && Object.keys(val.c).length === 2, "value: n=" + (val && val.n) + ", oʻzgargan " + (val && Object.keys(val.c).join(",")));
  ok(val && val.c["0"] === "Barcha dasturlar oʻgish", "amaldagi alifboda saqlandi: " + (val && val.c["0"]));
  ok(row && row.guard && row.guard.length > 10, "guard yozildi");
  const after = await p.evaluate(() => ({ img: document.querySelectorAll("header .wrap img").length, det: document.querySelectorAll("header .wrap details").length, a: document.querySelectorAll("header .wrap a[data-snd]").length }));
  ok(JSON.stringify(before) === JSON.stringify(after), "tuzilma oʻzgarmadi " + JSON.stringify(after));
  // qayta ochilganda muharrir qoʻllaydi va "tahrirlangan" deydi
  await p.close();
  p = await page("bachelor-lab.html?kedit=1");
  ok(await p.evaluate(() => document.querySelector("header .km-cta a.btn-g").textContent) === "Narxlar va tariflar", "muharrir qayta ochilganda oʻzgarish bor");
  ok(!(await sh(p).locator(".lost").count()), "topilmagan oʻzgarish yoʻq");
  await p.click("header .km-cta small", { position: { x: 5, y: 5 } });
  await sh(p).locator('[data-a="up"]').click(); await sh(p).locator('[data-a="up"]').click();
  ok(/tahrirlangan/.test(await sh(p).locator(".lbl").textContent()), "panel: Matni tahrirlangan");
  // ichki qismni oddiy tahrirlash bloklanadi (ustidagi blok tahrirlangan)
  await sh(p).locator('[data-a="desel"]').click();
  await p.goto(BASE + "bachelor-lab.html?kedit=0"); await p.close();

  // 2) saytda qoʻllash (anon REST)
  restRows = db.map(r => Object.assign({}, r, { page: "bachelor-lab.html" }));
  p = await page("bachelor-lab.html");
  await p.evaluate(() => { for (const k of Object.keys(localStorage)) if (/^kompas_edits_v1/.test(k)) localStorage.removeItem(k); });
  await p.reload({ waitUntil: "load" }); await p.waitForTimeout(1200);
  const t = await p.evaluate(() => [document.querySelector("header .crumb a").textContent, document.querySelector("header .km-cta a.btn-g").textContent, document.querySelector("header .wrap").getAttribute("data-kse-tid")]);
  ok(t[0] === "Barça dasturlar ögiş" && t[1] === "Narxlar va tariflar", "saytda qoʻllandi (yangi alifboda): " + t.slice(0, 2).join(" | "));
  ok(!!t[2], "data-kse-tid belgisi");
  await p.close();
  // tugunlar soni mos kelmasa qoʻllanmaydi
  restRows = restRows.map(r => r.kind === "text" ? Object.assign({}, r, { id: 99, value: JSON.stringify(Object.assign({}, val, { n: val.n + 1 })) }) : r);
  await ctx.clearCookies();
  p = await page("bachelor-lab.html?edits=1");
  await p.evaluate(() => { for (const k of Object.keys(localStorage)) if (/^kompas_edits_v1/.test(k)) localStorage.removeItem(k); });
  await p.reload({ waitUntil: "load" }); await p.waitForTimeout(1200);
  ok(await p.evaluate(() => document.querySelector("header .crumb a").textContent) === "Dasturlar", "tugunlar soni mos kelmasa qoʻllanmadi");
  await p.close();

  // 3) kompas-ui.js siz sahifa: site-edits.js (login soxta sessiyada kabinetga oʻtadi, shuning uchun sources)
  const PG = "sources.html";
  p = await page(PG);
  const hs = await p.evaluate(() => { const el = document.querySelector("h1,h2"); return { sel: KSiteEdits.path(el), guard: KSiteEdits.guard(el), n: KSiteEdits.tnodes(el).length }; });
  ok(await p.evaluate(() => !!window.KSiteEdits && !document.querySelector('script[src*="kompas-ui.js"]')), PG + ": KSiteEdits bor (faqat site-edits.js)");
  await p.close();
  restRows = [{ id: 51, page: PG, kind: "text", status: "active", sel: hs.sel, guard: hs.guard, value: JSON.stringify({ n: hs.n, c: { "0": "Sinov sarlavha" } }) }];
  p = await page(PG);
  await p.evaluate(() => { for (const k of Object.keys(localStorage)) if (/^kompas_edits_v1/.test(k)) localStorage.removeItem(k); });
  await p.reload({ waitUntil: "load" }); await p.waitForTimeout(1200);
  ok(await p.evaluate(() => document.querySelector("h1,h2").textContent.trim().startsWith("Sinov sarlavha")), PG + ": text oʻzgarishi qoʻllandi");
  await p.goto(BASE + PG + "?kedit=1", { waitUntil: "load" }); await p.waitForTimeout(1200);
  ok(await sh(p).locator(".pn").count() === 1, PG + ": muharrir paneli chiqdi");
  const h = await p.evaluate(() => { const el = document.querySelector("h1,h2"); return el && el.textContent.trim().slice(0, 30); });
  await p.click("h1,h2 >> nth=0");
  ok(!(await sh(p).locator('[data-a="edit"]').isDisabled()), PG + ": sarlavha tahrirlanadi (" + h + ")");
  await p.goto(BASE + PG + "?kedit=0"); await p.close();

  ok(!errs.length, "JS xatosi yoʻq " + errs.join(" | "));
  await b.close();
  console.log(fails ? fails + " ta xato" : "Hammasi oʻtdi");
  process.exit(fails ? 1 : 0);
})();
