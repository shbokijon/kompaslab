"use strict";
const fs=require("node:fs");
const path=require("node:path");
const test=require("node:test");
const assert=require("node:assert/strict");
const root=path.resolve(__dirname,"..");
const read=name=>fs.readFileSync(path.join(root,name),"utf8");

test("Legacy checkout cannot collect card numbers or initiate purchases",()=>{
  const html=read("payment.html");
  assert.doesNotMatch(html, /id=["']cardNumber(?:Payme|Bank)["']/);
  assert.doesNotMatch(html, /\.from\(DB\.payments\)\s*\.insert\(/);
  assert.doesNotMatch(html, /\.from\(DB\.enrollments\)\s*\.upsert\(/);
  assert.match(html, /async function processPayment\(\)[\s\S]{0,260}return false/);
  assert.match(html, /<button class="pay-btn" id="payBtn" disabled/);
  assert.match(html, /document\.getElementById\('payClosed'\)\.style\.display = 'flex'/);
});
test("Admin guards use database role instead of email allowlist",()=>{
  const auth=read("js/auth.js"), login=read("login.html");
  assert.match(auth,/auth\.profile\?\.role === 'admin'/);
  assert.doesNotMatch(auth,/APP_CONFIG\.adminEmails\.includes\(auth\.user\.email\)/);
  assert.doesNotMatch(login,/adminEmails\.includes/);
  assert.match(login,/profile\?\.role === 'admin'/);
});
test("Private routes never enter Service Worker Cache API",()=>{
  const sw=read("sw.js");
  assert.match(sw,/master-application/);
  assert.match(sw,/cache: "no-store"/);
  assert.match(sw,/kl-v3/);
});
test("Workspace explicitly refuses production database in a Vercel preview",()=>{
  const js=read("js/master-workspace.js");
  assert.match(js,/productionHost/);
  assert.match(js,/!productionHost/);
  assert.match(js,/db\.auth\.getUser\(\)/);
  assert.match(js,/\.from\("application_workspaces"\)/);
  assert.match(js,/\.from\("application_programs"\)/);
  assert.match(js,/\.from\("application_tasks"\)/);
  assert.match(js,/\.from\("application_artifacts"\)/);
  assert.doesNotMatch(js, /service.role.key|SERVICE_ROLE_KEY|sb_secret_/i);
});
test("Pilot page supports privacy, accessibility and source context",()=>{
  const html=read("master-application.html");
  assert.match(html,/<html lang="uz">/);
  assert.match(html,/<meta name="robots" content="noindex,nofollow">/);
  assert.match(html,/<h1>/);
  assert.match(html, /aria-live="polite"/);
  assert.match(html, /id="trackConsent"/);
  assert.match(html, /id="exportJson"/);
  assert.match(html, /id="exportCsv"/);
});
test("Existing pages link to the workspace without changing main-site default routes",()=>{
  for(const file of ["index.html","dashboard.html","master-lab-m0.html"]) {
    assert.match(read(file),/href="master-application\.html"/);
  }
});
test("Payment remains closed in checkout flow",()=>{
  assert.match(read("payment.html"),/Toʻlov vaqtincha yopiq/);
});
