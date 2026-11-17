// Admin → Dizayn va saytdagi koʻrinish sozlamalari sinovi (Playwright, Supabase soxta).
//   python3 -m http.server 8814 &
//   PW=$(npm root -g)/playwright node tools/site/test_look.cjs
// Tekshiradi: 1) mavzu ranglari kontrasti (oq matn urgʻuda ≥ 4.5, urgʻu fonda ≥ 3.5);
// 2) avtomatik qoida (fasl, bayram, yil oxiridan oʻtuvchi oraliq, bir martalik sana);
// 3) standart holatda CSS qayta yozilmaydi; 4) bazadagi sozlama qoʻllanadi (mavzu, shrift, oʻlcham), 390px siljish yoʻq;
// 5) "Aa" tugmasi matnni kattalashtiradi va tanlov saqlanadi; 6) admin: koʻrinish oynasi jonli, saqlash bazaga yozadi.
const { chromium } = require(process.env.PW || "playwright");
const BASE = "http://localhost:8814/";
const STUB = `(function(){
function db(){try{return JSON.parse(localStorage.getItem('stubdb2')||'{}')}catch(e){return{}}}
function save(d){localStorage.setItem('stubdb2',JSON.stringify(d))}
function Q(t){this.t=t;this.f=[];this.op='select';this.one=0;this.vals=null}
['select','order','limit','in','gte','lte','neq','is','not','or','range','ilike'].forEach(function(k){Q.prototype[k]=function(){return this}});
Q.prototype.eq=function(k,v){this.f.push([k,v]);return this};
Q.prototype.insert=function(v){this.op='insert';this.vals=v;return this};
Q.prototype.update=function(v){this.op='update';this.vals=v;return this};
Q.prototype.single=function(){this.one=1;return this};Q.prototype.maybeSingle=function(){this.one=2;return this};
Q.prototype.run=function(){
  if(this.t==='profiles'&&this.one)return{data:{id:'a1',role:'admin',email:'a@k.uz',full_name:'Admin'},error:null};
  var all=db(),d=all[this.t]||[],f=this.f,m=function(r){return f.every(function(x){return String(r[x[0]])===String(x[1])})};
  if(this.op==='insert'){var v=Object.assign({updated_at:new Date().toISOString()},this.vals);d.push(v);all[this.t]=d;save(all);return{data:[v],error:null}}
  if(this.op==='update'){var out=[];d.forEach(function(r){if(m(r)){Object.assign(r,this.vals,{updated_at:new Date().toISOString()});out.push(r)}},this);all[this.t]=d;save(all);return{data:out,error:null}}
  var res=d.filter(m);return{data:this.one?res[0]||null:res,error:null}};
Q.prototype.then=function(a,b){return Promise.resolve(this.run()).then(a,b)};
window.supabase={createClient:function(){return{
  auth:{getSession:function(){return Promise.resolve({data:{session:{user:{id:'a1',email:'a@k.uz'}}}})},getUser:function(){return Promise.resolve({data:{user:null}})},onAuthStateChange:function(){return{data:{subscription:{unsubscribe:function(){}}}}}},
  rpc:function(n){return Promise.resolve(n==='fn_is_admin'||n==='kompas_staff_can'?{data:true,error:null}:{data:{registered:13,prices:{}},error:null})},
  from:function(t){return new Q(t)},
  channel:function(){var c={on:function(){return c},subscribe:function(){return c},track:function(){},presenceState:function(){return{}}};return c}}}};
})();`;
let fails = 0;
const ok = (c, m) => { console.log((c ? "✓ " : "✗ ") + m); if (!c) fails++; };
function lum(h) { const v = [1, 3, 5].map(i => parseInt(h.slice(i, i + 2), 16) / 255).map(c => c <= 0.03928 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4); return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2]; }
function con(a, b) { const x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); }

(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 1280, height: 900 } });
  let restVal = null;
  await ctx.route(/fonts\.g|supabase\.co|open-meteo|t\.me|vimeo/, r => r.abort());
  await ctx.route(/supabase-js/, r => r.fulfill({ contentType: "text/javascript", body: STUB }));
  await ctx.route(/supabase\.co\/rest\/v1\/site_settings/, r => r.fulfill({ contentType: "application/json", body: JSON.stringify(restVal ? [{ value: restVal, updated_at: "2026-11-17T10:00:00Z" }] : []) }));
  await ctx.route(/supabase\.co\/rest\/v1\/site_edits/, r => r.fulfill({ contentType: "application/json", body: "[]" }));
  const errs = [];
  const open = async (url, w) => {
    const p = await ctx.newPage(); if (w) await p.setViewportSize({ width: w, height: 800 });
    p.on("pageerror", e => errs.push(url + ": " + e.message));
    await p.goto(BASE + url, { waitUntil: "load" }); await p.waitForTimeout(600); return p;
  };

  // 1–3
  let p = await open("index.html");
  const K = await p.evaluate(() => ({ th: KLook.THEMES, klook: document.documentElement.getAttribute("data-klook"), aa: !!document.querySelector(".kl-fs .kl-fs-b") }));
  for (const [id, t] of Object.entries(K.th)) if (t.c) {
    ok(con(t.c.a2, "#ffffff") >= 4.5 && con(t.c.a2, t.c.bg) >= 3.5 && con("#1a2e26", t.c.bg) >= 7, `kontrast: ${id} (oq ${con(t.c.a2, "#ffffff").toFixed(2)}, fon ${con(t.c.a2, t.c.bg).toFixed(2)})`);
  }
  ok(!K.klook, "standart holatda CSS qayta yozilmaydi");
  ok(K.aa, "“Aa” tugmasi bor");
  const R = await p.evaluate(() => {
    const base = { mode: "auto", seasons: true, hol: { ramazon: { on: true, from: "2027-02-08", to: "2027-03-09" } } };
    const r = (d, x) => KLook.resolve(Object.assign({}, base, x || {}, { _date: d })).id;
    return {
      kuz: r("2026-11-17"), qish: r("2027-01-20"), yoz: r("2026-07-01"), navruz: r("2027-03-21"), yy1: r("2026-12-31"), yy2: r("2027-01-02"),
      mus: r("2026-09-01"), ram: r("2027-02-20"), off: r("2027-03-21", { hol: { navruz: { on: false, from: "03-15", to: "03-25" } } }),
      noS: r("2026-11-17", { seasons: false }), man: KLook.resolve({ mode: "manual", theme: "bahor" }).id, bad: KLook.merge({ fs: 9, theme: "x", font: "y" })
    };
  });
  ok(R.kuz === "kuz" && R.qish === "qish" && R.yoz === "yoz", "fasllar: kuz/qish/yoz");
  ok(R.navruz === "navruz" && R.mus === "mustaqillik", "Navroʻz va Mustaqillik");
  ok(R.yy1 === "yangiyil" && R.yy2 === "yangiyil", "Yangi yil oraligʻi yil oxiridan oʻtadi");
  ok(R.ram === "ramazon", "Ramazon (bir martalik sana)");
  ok(R.off === "bahor" && R.noS === "standart" && R.man === "bahor", "oʻchirilgan bayram, fasl yoʻq, qoʻlda rejim");
  ok(R.bad.fs === 1.2 && R.bad.theme === "standart" && R.bad.font === "kompas", "notoʻgʻri qiymat chegaraga keltiriladi");
  const fs0 = await p.evaluate(() => parseFloat(getComputedStyle(document.querySelector("body p") || document.body).fontSize));
  const h0 = await p.evaluate(() => { const h = document.querySelector("h1"); return h ? parseFloat(getComputedStyle(h).fontSize) : 0; });
  await p.close();

  // 4) bazadagi sozlama
  restVal = { mode: "manual", theme: "qish", font: "lora", fs: 1.1, hs: 1.1, sp: 0.85, r: 0.5, w: 1.1, reader: true };
  await ctx.clearCookies();
  p = await open("index.html");
  await p.evaluate(() => localStorage.removeItem("kompas_ui_v1"));
  await p.reload({ waitUntil: "load" }); await p.waitForTimeout(700);
  let st = await p.evaluate(() => {
    const cs = getComputedStyle(document.documentElement), h = document.querySelector("h1");
    return { th: document.documentElement.getAttribute("data-ktheme"), a2: cs.getPropertyValue("--accent2").trim(), rw: document.documentElement.getAttribute("data-klook"),
      hf: h ? getComputedStyle(h).fontFamily : "", hs: h ? parseFloat(getComputedStyle(h).fontSize) : 0,
      bf: getComputedStyle(document.body).fontFamily, ps: parseFloat(getComputedStyle(document.querySelector("body p") || document.body).fontSize),
      font: !!document.getElementById("klook-font") };
  });
  ok(st.th === "qish" && st.a2 === "#3f6889", "mavzu qoʻllandi: qish (" + st.a2 + ")");
  ok(st.rw === "1" && /Lora/.test(st.hf) && /Source Sans 3/.test(st.bf) && st.font, "shrift: sarlavha Lora, matn Source Sans 3 (" + st.hf.slice(0, 40) + ")");
  ok(Math.abs(st.ps / fs0 - 1.1) < 0.03, `matn 110% (${fs0} → ${st.ps})`);
  ok(!h0 || Math.abs(st.hs / h0 - 1.21) < 0.06, `sarlavha 110%×110% (${h0} → ${st.hs})`);
  ok(await p.evaluate(() => { document.documentElement.setAttribute("data-theme", "dark"); const v = getComputedStyle(document.documentElement).getPropertyValue("--accent2").trim(); document.documentElement.setAttribute("data-theme", "light"); return v !== "#3f6889"; }), "tungi rejimda mavzu ranglari qoʻllanmaydi");

  // 5) Aa
  await p.click(".kl-fs .kl-fs-b"); await p.click('.kl-fs [data-fs="1"]'); await p.waitForTimeout(150);
  const ps2 = await p.evaluate(() => parseFloat(getComputedStyle(document.querySelector("body p") || document.body).fontSize));
  ok(Math.abs(ps2 / fs0 - 1.1 * 1.12) < 0.04 && await p.evaluate(() => localStorage.getItem("kompas_fs") === "1.12"), `A+ → 112% (${ps2}), tanlov saqlandi`);
  await p.close();
  for (const u of ["index.html", "master-lab.html", "narxlar.html", "mamlakatlar.html", "master-lab-dastur.html"]) {
    const q = await open(u, 390);
    const ov = await q.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
    ok(ov <= 1, `390px siljish yoʻq: ${u} (${ov}px, matn 123%)`);
    await q.close();
  }
  const q2 = await open("index.html?look=0");
  ok(await q2.evaluate(() => !document.documentElement.getAttribute("data-ktheme")), "?look=0 oʻchiradi");
  await q2.close();

  // 6) admin
  restVal = null;
  p = await open("admin.html");
  await p.evaluate(() => { document.body.style.display = ""; localStorage.removeItem("stubdb2"); localStorage.removeItem("kompas_fs"); });
  await p.evaluate(() => nav("look", document.getElementById("lkNav")));
  await p.waitForSelector(".lk-t", { timeout: 8000 });
  ok(await p.locator(".lk-t").count() === 10 && await p.locator(".lk-fc").count() === 8, "admin: 10 mavzu, 8 shrift juftligi");
  await p.click('.lk-t[data-t="bahor"]'); await p.waitForTimeout(200);
  const fr = p.frame({ url: /index\.html/ }) || p.frames()[1];
  ok(await fr.evaluate(() => document.documentElement.getAttribute("data-ktheme")) === "bahor", "koʻrinish oynasi jonli: bahor");
  ok(/Saqlanmagan/.test(await p.textContent("#lkDirty")), "saqlanmagan oʻzgarish belgisi");
  await p.evaluate(() => { const r = document.querySelector('input[oninput*="\'fs\'"]'); r.value = 108; r.dispatchEvent(new Event("input")); });
  ok(await fr.evaluate(() => getComputedStyle(document.documentElement).getPropertyValue("--kt-fs").trim()) === "1.08", "matn slayderi jonli (1.08)");
  await p.click(".lk-seg button:has-text('Avtomatik')"); await p.waitForTimeout(100);
  ok(await p.locator(".lk-hol tr").count() === 6, "avtomatik: 6 bayram qatori");
  await p.click("#lkSave"); await p.waitForTimeout(300);
  const dbv = await p.evaluate(() => JSON.parse(localStorage.getItem("stubdb2") || "{}").site_settings || []);
  ok(dbv.length === 1 && dbv[0].key === "ui" && dbv[0].value.mode === "auto" && dbv[0].value.fs === 1.08 && !("_date" in dbv[0].value), "saqlash: site_settings ga yozildi");
  ok(!/Saqlanmagan/.test(await p.textContent("#lkDirty")), "saqlangandan keyin belgi yoʻqoladi");
  await p.click(".lk-fc >> nth=4"); await p.waitForTimeout(150);
  ok(/Noto Serif/.test(await fr.evaluate(() => { const h = document.querySelector("h1"); return h ? getComputedStyle(h).fontFamily : ""; })), "shrift tanlovi jonli (Noto)");
  await p.screenshot({ path: "/tmp/look_admin.png" });
  await p.close();

  ok(!errs.length, "JS xatosi yoʻq" + (errs.length ? ": " + errs.slice(0, 3).join(" | ") : ""));
  await b.close();
  console.log(fails ? `\n${fails} ta xato` : "\nHammasi oʻtdi");
  process.exit(fails ? 1 : 0);
})();
