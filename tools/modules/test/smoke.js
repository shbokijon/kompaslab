// Modul sahifalarini tez tekshirish (Playwright).
// Ishga tushirish (repo ildizidan):
//   python3 -m http.server 8814 &            # sayt versiyasi uchun
//   PW=$(npm root -g)/playwright node tools/modules/test/smoke.js usa-lab-m0 musofir-lab-m0
// Tekshiradi: JS xatolari, 390px da gorizontal siljish, kirgan foydalanuvchiga ochilishi,
// 1-darsning 4 qismini ochib yakunlash (+XP), yuklab olinadigan versiya (dist/) ham.
const path = require("path");
const fs = require("fs");
const { chromium } = require(process.env.PW || "playwright");
const ROOT = path.resolve(__dirname, "../../..");
const MOCK = `window.supabase={createClient:()=>({
 auth:{getSession:()=>Promise.resolve({data:{session:{user:{id:'u1',email:'test@kompaslab.uz'}}}}),onAuthStateChange:()=>({data:{subscription:{unsubscribe(){}}}})},
 rpc:()=>Promise.resolve({data:{registered:13,prices:{}},error:null}),
 from:()=>{const q={select(){return q},eq(){return q},order(){return q},single(){return Promise.resolve({data:null,error:null})},then(r){return Promise.resolve({data:[],error:null}).then(r)}};return q},
 channel:()=>{const c={on(){return c},subscribe(){return c},track(){},presenceState(){return {}}};return c}})};`;
(async () => {
  const names = process.argv.slice(2);
  if (!names.length) { console.log("Modul nomini bering, masalan: usa-lab-m0"); process.exit(1); }
  const b = await chromium.launch(); let bad = 0;
  for (const n of names) for (const [kind, url] of [["sayt", "http://localhost:8814/" + n + ".html"], ["dist", "file://" + ROOT + "/tools/modules/dist/" + n + ".html"]]) {
    if (kind === "sayt" && !fs.existsSync(path.join(ROOT, n + ".html"))) continue;   // saytga chiqmagan modul
    // 2026-10-18 dan sayt versiyasi hub/dars/yakun sahifalariga boʻlingan: uni lesson_flow.js tekshiradi
    // master-lab-m1..m8.html saytda faqat darslar roʻyxati (Lab generatori), pullik modul emas
    if (kind === "sayt" && /data-kview=|data-kpage=/.test(fs.readFileSync(path.join(ROOT, n + ".html"), "utf8"))) continue;
    const ctx = await b.newContext({ viewport: { width: 390, height: 800 } }); const p = await ctx.newPage(); const errs = [];
    p.on("pageerror", e => errs.push(e.message));
    await ctx.route(/supabase-js/, r => r.fulfill({ contentType: "text/javascript", body: MOCK }));
    await ctx.route(/supabase\.co/, r => r.fulfill({ contentType: "application/json", body: "{}" }));
    try { await p.goto(url, { waitUntil: "networkidle", timeout: 15000 }); } catch (e) { console.log(n, kind, "OCHILMADI", e.message.split("\n")[0]); bad++; await ctx.close(); continue; }
    await p.waitForTimeout(600);
    const r = await p.evaluate(() => ({ locked: document.body.classList.contains("locked"), sw: document.documentElement.scrollWidth, broken: [...document.images].filter(i => i.complete && i.naturalWidth === 0).length }));
    let xp = null;
    if (!r.locked && await p.$("#l1 .tab")) {
      if (!(await p.$("#l1.open"))) await p.click("#l1 .l-head");
      for (let i = 0; i < 4; i++) await p.click(`#l1 .tab >> nth=${i}`);
      await p.click('[data-complete="l1"]'); await p.waitForTimeout(400);
      xp = await p.textContent("#xpN");
    }
    const ok = !errs.length && !r.locked && r.sw <= 390 && !r.broken && xp && +xp > 0;
    if (!ok) bad++;
    console.log((ok ? "✓" : "✗"), n, kind, JSON.stringify({ ...r, xp }), errs.slice(0, 3));
    await ctx.close();
  }
  await b.close(); process.exit(bad ? 1 : 0);
})();
