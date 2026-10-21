// M0 modul sahifalari oqimi (hub → dars → yakun) tekshiruvi (Playwright).
// Ishga tushirish (repo ildizidan):
//   python3 -m http.server 8814 &
//   PW=$(npm root -g)/playwright node tools/modules/test/lesson_flow.js gks-lab-m0 master-lab-m0
// Tekshiradi: dars sahifasida faqat bitta dars koʻrinadi, 4 qism + yakunlash → tabrik oynasi va +XP,
// "Keyingi dars" 2-dars sahifasini ochadi, hub da 1 dars yakunlangan va kompas strelkasi bor,
// yakun sahifasida vositalar va qaror koʻrinadi, JS xatosi yoʻq.
const { chromium } = require(process.env.PW || "playwright");
const MOCK = `window.supabase={createClient:()=>({auth:{getSession:()=>Promise.resolve({data:{session:{user:{id:'u1'}}}}),onAuthStateChange:()=>({data:{subscription:{unsubscribe(){}}}})},rpc:()=>Promise.resolve({data:{prices:{}},error:null}),from:()=>{const q={select(){return q},eq(){return q},then(r){return Promise.resolve({data:[]}).then(r)}};return q},channel:()=>{const c={on(){return c},subscribe(){return c},track(){},presenceState(){return {}}};return c}})};`;
(async () => {
  const b = await chromium.launch(); let fails = 0;
  for (const base of process.argv.slice(2)) {
    const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
    await ctx.route(/supabase-js/, r => r.fulfill({ contentType: "text/javascript", body: MOCK }));
    await ctx.route(/fonts\.g|supabase\.co/, r => r.abort());
    const p = await ctx.newPage(); const errs = []; p.on("pageerror", e => errs.push(e.message));
    await p.goto(`http://localhost:8814/${base}-1.html`, { waitUntil: "load" }); await p.waitForTimeout(500);
    const vis = await p.evaluate(() => [...document.querySelectorAll(".lesson")].filter(l => l.offsetParent).map(l => l.id));
    for (let i = 0; i < 4; i++) await p.click(`.lesson.kl-cur .tab >> nth=${i}`);
    await p.click(".lesson.kl-cur [data-complete]"); await p.waitForTimeout(500);
    const dlg = await p.evaluate(() => document.querySelector(".kl-done.on") !== null);
    const xp = await p.textContent("#xpN");
    await p.click(".kl-done a"); await p.waitForLoadState("load"); await p.waitForTimeout(400);
    const url2 = p.url(); const vis2 = await p.evaluate(() => [...document.querySelectorAll(".lesson")].filter(l => l.offsetParent).map(l => l.id));
    await p.goto(`http://localhost:8814/${base}.html`); await p.waitForTimeout(500);
    const hub = await p.evaluate(() => ({ done: document.querySelectorAll(".kl-hub-route .is-done").length, btn: (document.querySelector(".kl-hub-actions .btn-p") || {}).textContent, needle: !!document.querySelector(".kl-route-needle") }));
    await p.goto(`http://localhost:8814/${base}-yakun.html`); await p.waitForTimeout(500);
    const yk = await p.evaluate(() => ({ tools: [...document.querySelectorAll("#vositalar .tool")].filter(t => t.offsetParent).length, qaror: !!(document.querySelector("#qaror") || {}).offsetParent, sw: document.documentElement.scrollWidth }));
    const ok = vis.length === 1 && dlg && +xp >= 20 && url2.endsWith("-2.html") && vis2[0] === "l2" && hub.done === 1 && hub.needle && yk.tools > 0 && yk.qaror && yk.sw <= 390 && !errs.length;
    if (!ok) fails++;
    console.log(ok ? "✓" : "✗", base, JSON.stringify({ vis, dlg, xp, url2: url2.split("/").pop(), vis2, hub, yk }), errs.slice(0, 2));
    await ctx.close();
  }
  await b.close(); process.exit(fails ? 1 : 0);
})();
