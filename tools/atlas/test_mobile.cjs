/* Atlas mobile smoke and timing tests. Browser emulation, NOT real iPhone/Android. */
"use strict";
const {chromium, webkit} = require(process.env.PW || "playwright");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const BASE = process.env.ATLAS_BASE || "http://127.0.0.1:8814";
const ROOT = path.resolve(__dirname, "../..");
const LITE = JSON.parse(fs.readFileSync(path.join(ROOT,"data/uk-sponsors-lite.json"),"utf8"));
const SKIP_REMOTE = [/fonts\.googleapis\.com/, /fonts\.gstatic\.com/];
const scenarios = [
 {name:"Android Chromium 360px",engine:chromium,viewport:{width:360,height:800},isMobile:true,hasTouch:true,deviceScaleFactor:2},
 {name:"Android Chromium 412px",engine:chromium,viewport:{width:412,height:915},isMobile:true,hasTouch:true,deviceScaleFactor:2.625},
 {name:"iPhone WebKit 390px",engine:webkit,viewport:{width:390,height:844},isMobile:true,hasTouch:true,deviceScaleFactor:3},
 {name:"Desktop Chromium",engine:chromium,viewport:{width:1280,height:900},isMobile:false,hasTouch:false,deviceScaleFactor:1},
];
async function testScenario(s){
 const browser = await s.engine.launch({headless:true});
 const context = await browser.newContext({viewport:s.viewport,isMobile:s.isMobile,hasTouch:s.hasTouch,deviceScaleFactor:s.deviceScaleFactor});
 const page = await context.newPage();
 const errors=[];
 page.on("pageerror",e=>errors.push(e.message));
 await page.route("**/*",route=>{
   const u=route.request().url();
   if(SKIP_REMOTE.some(re=>re.test(u)))return route.abort();
   return route.continue();
 });
 const started=Date.now();
 await page.goto(BASE+"/uk-sponsors.html",{waitUntil:"domcontentloaded",timeout:25000});
 await page.waitForFunction(()=>document.querySelector("#datasetStatus")?.textContent==="Rasmiy nusxa",{timeout:30000});
 const elapsed=Date.now()-started;
 const pageState=await page.evaluate(()=>({
   width:document.documentElement.scrollWidth,
   viewport:window.innerWidth,
   cards:document.querySelectorAll(".sponsor").length,
   mapDots:document.querySelectorAll("#ukMapDots circle").length,
   careers:[...document.querySelectorAll(".career-card a")].map(a=>({href:a.href,rel:a.rel,target:a.target})),
   loadMs:+document.documentElement.dataset.atlasLoadMs || 0,
 }));
 assert.ok(pageState.width <= pageState.viewport+2,`Horizontal overflow: ${pageState.width} > ${pageState.viewport}`);
 assert.ok(pageState.cards>0 && pageState.cards<=24,"Initial pagination must render 1..24 results");
 assert.ok(pageState.mapDots >= 5,"City map needs data markers");
 assert.ok(pageState.careers.length>=5,"Expected curated careers links");
 for(const a of pageState.careers){
  assert.ok(a.href.startsWith("https://"),"External careers must use https");
  assert.ok(a.rel.includes("noopener") && a.target==="_blank","External links require tab isolation");
 }
 // Verify search actually changes results, then reset to all.
 await page.locator("#q").fill("University");
 await page.waitForTimeout(450);
 const searchCount=await page.locator("#resultsCount").textContent();
 assert.ok(searchCount && !searchCount.includes("122,455"),"Keyword filter should narrow sponsors");
 await page.locator("#reset").click();
 // Verify city dropdown matches selection, and mapping updates without errors.
 const options=await page.locator("#city option").allTextContents();
 assert.ok(options.includes("Leeds"),"Expected Leeds in official data");
 await page.locator("#city").selectOption({label:"Leeds"});
 const selected=await page.locator("#city").inputValue();
 assert.equal(selected,"Leeds");
 assert.ok((await page.locator("#results .sponsor").count())>0);
 assert.equal(errors.length,0,"Unexpected JavaScript errors: "+errors.join("; "));
 console.log(JSON.stringify({scenario:s.name,elapsedMs:elapsed,loadMs:pageState.loadMs,scrollWidth:pageState.width,sponsorCards:pageState.cards,mapCities:pageState.mapDots,careers:pageState.careers.length}));
 await context.close();await browser.close();
}
(async()=>{
 assert.ok(LITE.rows && LITE.rows.length>10000,"Compact data missing");
 for(const scenario of scenarios)await testScenario(scenario);
 console.log("Atlas mobile browser emulation: PASS. Physical device testing still required.");
})().catch(err=>{console.error(err);process.exit(1)});
