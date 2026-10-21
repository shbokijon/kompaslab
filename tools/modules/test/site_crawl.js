// Butun saytni tekshirish (Playwright): har .html sahifa 390px va 1280px da ochiladi.
// Ishga tushirish (repo ildizidan):
//   python3 -m http.server 8814 &
//   PW=$(npm root -g)/playwright node tools/modules/test/site_crawl.js
// Xato hisoblanadi: JS xatosi, 390px da gorizontal siljish, mavjud boʻlmagan ichki sahifaga havola.
const { chromium } = require(process.env.PW || "playwright");
const fs = require("fs"), path = require("path");
const ROOT = path.resolve(__dirname, "../../..");
const MOCK = `window.supabase={createClient:()=>({auth:{getSession:()=>Promise.resolve({data:{session:{user:{id:'u1',email:'t@k.uz'}}}}),getUser:()=>Promise.resolve({data:{user:null}}),onAuthStateChange:()=>({data:{subscription:{unsubscribe(){}}}})},rpc:()=>Promise.resolve({data:{registered:13,prices:{}},error:null}),from:()=>{const q={select(){return q},eq(){return q},order(){return q},limit(){return q},upsert(){return Promise.resolve({})},insert(){return Promise.resolve({})},single(){return Promise.resolve({data:null,error:null})},maybeSingle(){return Promise.resolve({data:null,error:null})},then(r){return Promise.resolve({data:[],error:null}).then(r)}};return q},channel:()=>{const c={on(){return c},subscribe(){return c},track(){},presenceState(){return {}}};return c}})};`;
const SKIP = new Set(["admin.html", "globe-demo.html", "offline.html"]);
(async () => {
  const files = fs.readdirSync(ROOT).filter(f => f.endsWith(".html") && !SKIP.has(f));
  const b = await chromium.launch(); const bad = []; const missing = new Map();
  for (const w of [390, 1280]) {
    const ctx = await b.newContext({ viewport: { width: w, height: 800 } });
    await ctx.route(/supabase-js/, r => r.fulfill({ contentType: "text/javascript", body: MOCK }));
    await ctx.route(/fonts\.g|supabase\.co|open-meteo|t\.me/, r => r.abort());
    for (const f of files) {
      const p = await ctx.newPage(); const errs = []; p.on("pageerror", e => errs.push(e.message));
      try { await p.goto("http://localhost:8814/" + f, { waitUntil: "load", timeout: 15000 }); } catch (e) { errs.push("goto " + e.message.split("\n")[0]); }
      await p.waitForTimeout(350);
      const r = await p.evaluate(() => ({ sw: document.documentElement.scrollWidth, links: [...document.querySelectorAll("a[href]")].map(a => a.getAttribute("href")) })).catch(() => ({ sw: 0, links: [] }));
      if (w === 390 && r.sw > 392) errs.push("overflow " + r.sw);
      if (w === 390) for (const h of r.links) {
        if (/^(https?:|mailto:|tel:|#|javascript:)/.test(h)) continue;
        const fn = h.split(/[?#]/)[0]; if (!fn) continue;
        if (!fs.existsSync(path.join(ROOT, fn.endsWith(".html") ? fn : fn + ".html")) && !fs.existsSync(path.join(ROOT, fn))) missing.set(fn, (missing.get(fn) || []).concat(f));
      }
      if (errs.length) bad.push([w, f, errs.slice(0, 2)]);
      await p.close();
    }
    await ctx.close();
  }
  console.log("Sahifalar:", files.length, "· xatoli:", bad.length, "· buzilgan havola:", missing.size);
  bad.forEach(x => console.log("✗", JSON.stringify(x)));
  for (const [k, v] of missing) console.log("✗ havola", k, "←", [...new Set(v)].slice(0, 4).join(", "));
  await b.close(); process.exit(bad.length || missing.size ? 1 : 0);
})();
