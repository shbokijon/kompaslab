// Pullik modul oʻquvchisi (<lab>-o.html) va modul sahifasidagi tugma (js/paid-module.js).
//   python3 -m http.server 8814 &   (repo ildizida)
//   PW=$(npm root -g)/playwright node tools/modules/test/paid_reader.js
// Supabase mock: sessiya va RPC javoblari stsenariy boʻyicha. Paid HTML tools/modules/paid/ dan.
const fs = require("fs");
const path = require("path");
const { chromium } = require(process.env.PW || "playwright");
const BASE = "http://127.0.0.1:8814/";
const ROOT = path.resolve(__dirname, "../../..");
// Lab: PAID_LAB=gks-lab node … (standart master-lab)
const LAB = process.env.PAID_LAB || "master-lab";
// Modul kalitlari (?m=) va bazadagi tartib raqami; GKS: umumiy oʻzak + U/M/D treklari
const KEYS = LAB === "gks-lab" ? ["m1", "m2", "m3-u", "m4-u", "m5-u", "m3-m", "m4-m", "m5-m", "m3-d", "m4-d", "m5-d"] : ["1", "2", "3", "4", "5", "6", "7", "8"];
const H = LAB === "gks-lab" ? { 3: "m3-u", 4: "m4-u", 5: "m5-u", 6: "m4-m", 8: "m5-d" } : {};   // test kalitlari
const k = n => H[n] || String(n);
const file = key => LAB + "-" + (key[0] === "m" ? key : "m" + key);

function mock(sc) {
  return `(function(){var SC=${JSON.stringify(sc)};
  window.supabase={createClient:function(){return{
    auth:{getSession:function(){return Promise.resolve({data:{session:SC.session?{user:{id:"u1",email:"t@k.uz"}}:null}})},
          getUser:function(){return Promise.resolve({data:{user:SC.session?{id:"u1",email:"t@k.uz"}:null}})},
          onAuthStateChange:function(){return{data:{subscription:{unsubscribe:function(){}}}}}},
    rpc:function(n,a){
      if(n==="fn_is_admin")return Promise.resolve({data:!!SC.admin,error:null});
      if(n==="fn_my_access")return Promise.resolve({data:SC.access||{access:false,unlocked_modules:0},error:null});
      if(n==="fn_paid_page")return fetch("/__paid/"+a.p_module_index).then(function(r){return r.json()});
      return Promise.resolve({data:{registered:13,prices:{}},error:null})},
    from:function(){var q={select:function(){return q},eq:function(){return q},order:function(){return q},limit:function(){return q},upsert:function(){return Promise.resolve({})},insert:function(){return Promise.resolve({})},maybeSingle:function(){return Promise.resolve({data:null,error:null})},single:function(){return Promise.resolve({data:null,error:null})},then:function(r){return Promise.resolve({data:[],error:null}).then(r)}};return q},
    channel:function(){var c={on:function(){return c},subscribe:function(){return c},track:function(){},presenceState:function(){return{}}};return c}}}};})();`;
}

async function run(browser, name, sc, url, check) {
  const ctx = await browser.newContext({ viewport: { width: 390, height: 844 } });
  const errors = [];
  await ctx.route(/supabase-js/, r => r.fulfill({ contentType: "text/javascript", body: mock(sc) }));
  await ctx.route(/fonts\.g|supabase\.co|open-meteo|t\.me/, r => r.abort());
  await ctx.route(/\/__paid\/\d+/, r => {
    const m = +r.request().url().match(/(\d+)$/)[1];
    let data = sc.paid;
    if (data === "html") data = { ok: true, version: "t", html: fs.readFileSync(path.join(ROOT, "tools/modules/paid/" + file(KEYS[m - 1]) + ".html"), "utf8") };
    r.fulfill({ contentType: "application/json", body: JSON.stringify({ data, error: null }) });
  });
  const page = await ctx.newPage();
  page.on("pageerror", e => errors.push(e.message));
  await page.goto(BASE + url, { waitUntil: "load" });
  await page.waitForTimeout(1200);
  const res = await check(page);
  const sw = await page.evaluate(() => document.documentElement.scrollWidth);
  const ok = res === true && errors.length === 0 && sw <= 392;
  console.log((ok ? "OK   " : "FAIL ") + name + (ok ? "" : "  -> " + JSON.stringify({ res, errors: errors.slice(0, 3), sw })));
  await ctx.close();
  return ok;
}

(async () => {
  const browser = await chromium.launch();
  const t = (sel) => async p => (await p.textContent(sel)) || "";
  let all = true;
  const R = async (...a) => { all = (await run(browser, ...a)) && all; };

  await R("reader: kirmagan → Kirish", { session: false }, LAB + "-o.html?m=" + k(3),
    async p => (await t("#t")(p)).includes("Avval kiring") && (await p.evaluate(() => sessionStorage.getItem("returnTo"))) === LAB + "-o.html?m=" + k(3));
  await R("reader: obunasiz → Obuna kerak", { session: true, paid: { ok: false, reason: "no_access" } }, LAB + "-o.html?m=" + k(3),
    async p => (await t("#t")(p)).includes("Obuna kerak"));
  await R("reader: qulf → keyinroq", { session: true, paid: { ok: false, reason: "locked", unlocked_modules: 3 } }, LAB + "-o.html?m=" + k(5),
    async p => (await t("#t")(p)).includes("Bu modul hali"));
  await R("reader: notoʻgʻri m", { session: true }, LAB + "-o.html?m=12",
    async p => (await t("#t")(p)).includes("topilmadi"));
  for (const key of KEYS) {
    await R("reader: obunachi → " + key + " ochildi", { session: true, paid: "html" }, LAB + "-o.html?m=" + key, async p => {
      const n = await p.locator("article.lesson").count();
      if (!n) return "dars yoʻq";
      await p.locator("article.lesson .l-head").first().click();
      await p.waitForTimeout(300);
      const tabs = await p.locator("article.lesson").first().locator('.tab').count();
      return tabs === 4 ? true : "tablar " + tabs;
    });
  }
  await R("hub: mehmon → qulf", { session: false }, file(k(4)) + ".html",
    async p => (await t(".kl-lock [data-paid-t]")(p)).includes("obuna bilan"));
  await R("hub: obunachi → Modulni ochish", { session: true, access: { access: true, unlocked_modules: 9 } }, file(k(4)) + ".html",
    async p => (await p.getAttribute(".kl-lock [data-paid-row] a.btn-p", "href")) === LAB + "-o.html?m=" + (LAB === "gks-lab" ? k(4) : 4) && (await p.locator(".kl-lessons .kl-st.is-locked").count()) === 0);
  await R("hub: boʻlib toʻlash, M6 hali yopiq", { session: true, access: { access: true, unlocked_modules: 3 } }, file(k(6)) + ".html",
    async p => (await t(".kl-lock [data-paid-t]")(p)).includes("keyinroq"));
  await R("hub: admin → ochiq", { session: true, admin: true }, file(k(8)) + ".html",
    async p => (await p.getAttribute(".kl-lock [data-paid-row] a.btn-p", "href")) === LAB + "-o.html?m=" + (LAB === "gks-lab" ? k(8) : 8));

  await browser.close();
  console.log(all ? "\nHAMMASI OʻTDI" : "\nXATO BOR");
  process.exit(all ? 0 : 1);
})();
