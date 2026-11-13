// Admin → Vebsayt va jonli muharrir sinovi (Playwright, Supabase soxta mijoz bilan).
//   python3 -m http.server 8814 &
//   PW=$(npm root -g)/playwright node tools/site/test_site_edits.cjs
// Tekshiradi: 1) kompas-ui.js va admin-site.js dagi norm/path/guard bir xil;
// 2) muharrir: tanlash → matnni tahrirlash → saqlash (amaldagi alifboda) → yashirish → koʻrsatish;
// 3) saytda qoʻllash (anon REST): yashirish, matn, guard boʻyicha topish, guard mos kelmasa qoʻllamaslik;
// 4) admin.html Vebsayt boʻlimi: boʻlimlar roʻyxati va yashirish tugmasi.
const { chromium } = require(process.env.PW || "playwright");
const BASE = "http://localhost:8814/";
// Soxta supabase-js: maʼlumot localStorage "stubdb" da (sahifalar orasida saqlanadi)
const STUB = `(function(){
function db(){try{return JSON.parse(localStorage.getItem('stubdb')||'[]')}catch(e){return[]}}
function save(d){localStorage.setItem('stubdb',JSON.stringify(d))}
function Q(t){this.t=t;this.f=[];this.op='select';this.one=0;this.vals=null}
Q.prototype.select=function(){return this};
Q.prototype.eq=function(k,v){this.f.push([k,v]);return this};
Q.prototype.order=function(){return this};Q.prototype.limit=function(){return this};
Q.prototype.insert=function(v){this.op='insert';this.vals=v;return this};
Q.prototype.update=function(v){this.op='update';this.vals=v;return this};
Q.prototype.single=function(){this.one=1;return this};Q.prototype.maybeSingle=function(){this.one=2;return this};
Q.prototype.run=function(){
  if(this.t==='profiles'&&this.one)return{data:{id:'a1',role:'admin',email:'a@k.uz',full_name:'Admin'},error:null};
  if(this.t!=='site_edits')return{data:this.one?null:[],error:null};
  var d=db(),f=this.f,m=function(r){return f.every(function(x){return String(r[x[0]])===String(x[1])})};
  if(this.op==='insert'){var v=Object.assign({status:'active',guard:''},this.vals);
    if(d.some(function(r){return r.status==='active'&&v.status==='active'&&r.page===v.page&&r.sel===v.sel&&r.kind===v.kind}))return{data:null,error:{code:'23505',message:'dup'}};
    v.id=d.reduce(function(a,r){return Math.max(a,r.id)},0)+1;v.updated_at=new Date().toISOString();d.push(v);save(d);return{data:v,error:null}}
  if(this.op==='update'){var out=[];d.forEach(function(r){if(m(r)){Object.assign(r,this.vals);out.push(r)}},this);save(d);return{data:this.one?out[0]||null:out,error:null}}
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

(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 1280, height: 900 } });
  let restRows = [];
  // Playwright: keyin qoʻshilgan route birinchi ishlaydi, shuning uchun umumiy blok birinchi
  await ctx.route(/fonts\.g|supabase\.co|open-meteo|t\.me|vimeo/, r => r.abort());
  await ctx.route(/supabase-js/, r => r.fulfill({ contentType: "text/javascript", body: STUB }));
  await ctx.route(/supabase\.co\/rest\/v1\/site_edits/, r => {
    const u = new URL(r.request().url()), pg = (u.searchParams.get("page") || "").replace(/^eq\./, "");
    r.fulfill({ contentType: "application/json", body: JSON.stringify(restRows.filter(x => x.page === pg && x.status === "active").map(({ id, sel, kind, guard, value }) => ({ id, sel, kind, guard, value }))) });
  });
  const errs = [];
  const page = async (url) => { const p = await ctx.newPage(); p.on("pageerror", e => errs.push(url + ": " + e.message)); await p.goto(BASE + url, { waitUntil: "load" }); await p.waitForTimeout(700); return p; };

  // 1) funksiyalar bir xil
  let p = await page("index.html?kedit=0");
  await p.addScriptTag({ url: BASE + "js/admin-site.js" }).catch(() => {});
  const same = await p.evaluate(() => {
    const A = window.KSiteEdits, B = WS._t; let n = 0, bad = [];
    document.querySelectorAll("body *").forEach(el => { n++; if (A.path(el) !== B.path(el) || A.guard(el) !== B.guard(el)) bad.push(A.path(el)); });
    return { n, bad: bad.slice(0, 3), conv: A.norm("Oʻzbekiston Şahar Ğalaba Çiroq") === A.norm("Ozbekiston Shahar Galaba Chiroq") };
  });
  ok(same.n > 100 && !same.bad.length, "norm/path/guard ikkala faylda bir xil (" + same.n + " element) " + same.bad.join(" "));
  ok(same.conv, "norm alifboga bogʻliq emas");
  await p.close();

  // 2) muharrir
  p = await page("index.html?kedit=1");
  await p.evaluate(() => localStorage.setItem("stubdb", "[]"));
  await p.reload({ waitUntil: "load" }); await p.waitForTimeout(1200);
  ok(await p.evaluate(() => !!document.getElementById("kse-host")), "muharrir paneli chiqdi");
  const h2 = await p.evaluate(() => { const h = document.querySelector("#lab-nima h2") || document.querySelector("section h2"); h.setAttribute("data-t", "1"); return h.textContent; });
  await p.click("[data-t]");
  await p.waitForTimeout(150);
  const sh = (s) => p.evaluate((s) => { const b = document.getElementById("kse-host").shadowRoot.querySelector(s); if (b) b.click(); return !!b; }, s);
  ok(await sh('[data-a="edit"]:not([disabled])'), "sarlavha tanlandi, tahrirlash tugmasi faol");
  await p.evaluate(() => { const h = document.querySelector("[data-t]"); h.innerHTML = "Yangi sarlavha: Öqiş va Çet <b>el</b>"; });
  await sh('[data-a="save"]'); await p.waitForTimeout(300);
  let db = await p.evaluate(() => JSON.parse(localStorage.getItem("stubdb")));
  const hr = db.find(r => r.kind === "html");
  ok(hr && hr.value === "Yangi sarlavha: Oʻqish va Chet <b>el</b>", "matn amaldagi alifboda saqlandi: " + (hr && hr.value));
  ok(hr && hr.guard && hr.guard.length > 5, "guard yozildi");
  ok(await p.evaluate(() => /Öqiş/.test(document.querySelector("[data-t]").textContent)), "sahifada yangi alifboda koʻrinadi");
  // boʻlimni yashirish
  await p.evaluate(() => document.getElementById("globus").setAttribute("data-g", "1"));
  await p.click("[data-g]", { position: { x: 5, y: 5 } }); await p.waitForTimeout(100);
  // ichki element tanlangan boʻlishi mumkin: #globus gacha ko'tarilamiz
  for (let i = 0; i < 6; i++) { const isG = await p.evaluate(() => /#globus/.test(document.getElementById("kse-host").shadowRoot.querySelector(".lbl").textContent)); if (isG) break; await sh('[data-a="up"]'); }
  await sh('[data-a="hide"]'); await p.waitForTimeout(300);
  db = await p.evaluate(() => JSON.parse(localStorage.getItem("stubdb")));
  ok(db.some(r => r.kind === "hide" && r.sel === "#globus" && r.status === "active"), "#globus yashirildi");
  ok(await p.evaluate(() => document.getElementById("globus").hasAttribute("data-kse-hidden")), "muharrirda xira koʻrinadi");
  // havola bosilganda sahifa almashmasligi (Tanlash rejimi)
  const before = p.url();
  await p.click("footer a[href]").catch(() => {}); await p.waitForTimeout(300);
  ok(p.url() === before, "Tanlash rejimida havola ochilmaydi");
  // qayta yuklash: yozuvlar qoʻllanadi
  await p.reload({ waitUntil: "load" }); await p.waitForTimeout(1500);
  ok(await p.evaluate(() => document.getElementById("globus").hasAttribute("data-kse-hidden") && /Öqiş/.test(document.querySelector("[data-kse-id]").textContent)), "qayta ochilganda muharrir oʻzgarishlarni koʻrsatadi");
  restRows = db.map(r => Object.assign({ page: "index.html" }, r));
  // chiqish
  await sh('[data-a="exit"]'); await p.waitForLoadState("load"); await p.waitForTimeout(800);
  ok(await p.evaluate(() => !document.getElementById("kse-host") && !/kedit/.test(location.search)), "muharrirdan chiqildi");
  await p.close();

  // 3) saytda qoʻllash (anon)
  p = await page("index.html");
  let st = await p.evaluate(() => ({ g: getComputedStyle(document.getElementById("globus")).display, t: (document.querySelector('[data-kse="t"]') || {}).textContent || "" }));
  ok(st.g === "none", "saytda #globus yashirin");
  ok(/Öqiş va Çet el/.test(st.t), "saytda yangi matn (yangi alifboda): " + st.t);
  // guard boʻyicha topish (yoʻl notoʻgʻri) va guard mos kelmasa qoʻllamaslik
  const gd = await p.evaluate(() => { const s = document.getElementById("asoschi"); return window.KSiteEdits.guard(s); });
  restRows = [
    { id: 50, page: "narxlar.html", sel: "body > section:nth-of-type(99)", kind: "hide", guard: "", value: null, status: "active" },
  ];
  restRows.push({ id: 51, page: "index.html", sel: "body > section:nth-of-type(1)", kind: "hide", guard: gd, value: null, status: "active" });
  restRows.push({ id: 52, page: "index.html", sel: "#lab-nima", kind: "hide", guard: "notogri", value: null, status: "active" });
  await p.evaluate(() => localStorage.clear());
  await p.reload({ waitUntil: "load" }); await p.waitForTimeout(1200);
  st = await p.evaluate(() => ({ a: getComputedStyle(document.getElementById("asoschi")).display, l: getComputedStyle(document.getElementById("lab-nima")).display, first: getComputedStyle(document.querySelector("body > section")).display }));
  ok(st.a === "none" && st.first !== "none", "yoʻl notoʻgʻri boʻlsa guard boʻyicha topildi, boshqa boʻlim yashirilmadi");
  ok(st.l !== "none", "guard mos kelmasa yashirilmaydi");
  await p.close();
  // ?edits=0
  p = await page("index.html?edits=0");
  ok(await p.evaluate(() => getComputedStyle(document.getElementById("asoschi")).display !== "none"), "?edits=0 oʻchiradi");
  await p.close();

  // 4) admin bo'limi
  p = await ctx.newPage(); p.on("pageerror", e => errs.push("admin: " + e.message));
  await p.goto(BASE + "admin.html", { waitUntil: "load" }); await p.waitForTimeout(800);
  await p.evaluate(() => { document.body.style.display = ""; localStorage.setItem("stubdb", "[]"); });
  await p.evaluate(() => nav("website", document.getElementById("wsNav")));
  await p.waitForTimeout(1500);
  const ad = await p.evaluate(() => ({ rows: document.querySelectorAll("#wsBlocks tr").length, opts: document.querySelectorAll("#wsPage option").length, txt: document.getElementById("wsBlocks").textContent.slice(0, 200) }));
  ok(ad.rows > 5 && ad.opts > 50, "admin: boʻlimlar (" + ad.rows + " qator) va sahifalar (" + ad.opts + ")");
  await p.evaluate(() => { const cb = [...document.querySelectorAll('#wsBlocks input[type=checkbox]')].find(c => c.dataset.sel === "#yol-4k"); cb.click(); });
  await p.waitForTimeout(600);
  db = await p.evaluate(() => JSON.parse(localStorage.getItem("stubdb")));
  ok(db.some(r => r.sel === "#yol-4k" && r.kind === "hide" && r.guard), "admin: #yol-4k yashirildi");
  ok(await p.evaluate(() => /Ya(sh|ş)iri/.test(document.getElementById("wsEdits").textContent)), "admin: oʻzgarishlar jadvalida chiqdi");
  await p.evaluate(() => { const cb = [...document.querySelectorAll('#wsBlocks input[type=checkbox]')].find(c => c.dataset.sel === "#yol-4k"); cb.click(); });
  await p.waitForTimeout(600);
  db = await p.evaluate(() => JSON.parse(localStorage.getItem("stubdb")));
  ok(db.find(r => r.sel === "#yol-4k").status === "off", "admin: qayta koʻrsatildi (status off)");
  await p.evaluate(() => WS.pick("master-lab-narxlar.html")); await p.waitForTimeout(1200);
  ok(await p.evaluate(() => document.querySelectorAll("#wsBlocks tr").length > 3), "admin: Lab sahifasi boʻlimlari");
  await p.close();

  ok(!errs.length, "JS xatosi yoʻq " + errs.slice(0, 3).join(" | "));
  await b.close();
  console.log(fails ? fails + " ta xato" : "Hammasi oʻtdi");
  process.exit(fails ? 1 : 0);
})();
