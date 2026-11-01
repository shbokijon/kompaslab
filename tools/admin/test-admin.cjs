// Admin UI smoke checks. Mocked identity/data: never contacts production Supabase.
const {chromium}=require(process.env.PW || 'playwright');
const BASE=process.env.BASE||'http://127.0.0.1:8814';
const MOCK = `
window.supabase={createClient:()=>({
 auth:{
  getSession:()=>Promise.resolve({data:{session:{user:{id:'aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa',email:'admin@example.test'}}}}),
  onAuthStateChange:()=>({data:{subscription:{unsubscribe(){}}}}),
  signOut:()=>Promise.resolve({})
 },
 rpc:(name)=>Promise.resolve({data:
    name==='kompas_admin_usage'?{database_bytes:12000000,course_count:12,module_count:66,lesson_count:366,profiles_count:2}:
    name==='kompas_admin_user_state'?{status:'active',staff:'student',grants:[]}:
    name==='kompas_staff_can'?true:
    {registered:2,waitlist:0,prices:{}},error:null}),
 from:(name)=>{
  const q={
    select(){return q},eq(){return q},neq(){return q},order(){return q},
    limit(){return q},single(){return Promise.resolve({data:{id:'aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa',role:'admin',first_name:'Test',full_name:'Test Admin',email:'admin@example.test'},error:null})},
    maybeSingle(){return q.single()},
    update(){return q},insert(){return q},delete(){return q},upsert(){return q},
    then(cb){const data=name==='courses'?[{id:'bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb',slug:'master-lab',title:'Master Lab',status:'draft',price:699000}]:
        name==='modules'?[{id:'cccccccc-cccc-4ccc-8ccc-cccccccccccc',course_id:'bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb',order_index:0,title:'M0'}]:
        name==='profiles'?[{id:'dddddddd-dddd-4ddd-8ddd-dddddddddddd',first_name:'Sinov',last_name:'Talaba',email:'student@example.test',created_at:new Date().toISOString(),enrollments:[]}]:[];
      return Promise.resolve({data,error:null}).then(cb);}
  };return q;
 }
})};
`;
(async()=>{
 const browser=await chromium.launch({headless:true});
 let failures=0;
 for(const width of [390,1280]){
  const ctx=await browser.newContext({viewport:{width,height:840}});
  await ctx.route('**/supabase-js@**', r=>r.fulfill({contentType:'application/javascript',body:MOCK}));
  await ctx.route(/fonts\.googleapis|fonts\.gstatic|supabase\.co/, r=>r.abort());
  const p=await ctx.newPage(),errors=[];
  p.on('pageerror',e=>errors.push(e.message));
  await p.goto(BASE+'/admin.html',{waitUntil:'load'});
  await p.waitForTimeout(700);
  const panelVisible=await p.evaluate(()=>getComputedStyle(document.body).display!=='none');
  await p.click('.sb-item[onclick*="regs"]');
  await p.waitForTimeout(100);
  const settings=await p.locator('#tbRegs .klx-cell button').count();
  if(settings) {
    await p.locator('#tbRegs .klx-cell button').first().click();
    await p.waitForTimeout(200);
  }
  const modal=await p.locator('#m-access-settings.open').count();
  const course=await p.locator('#klxCourse option').count();
  await p.click('#klxClose');
  await p.click('#klxNavSystem');
  await p.waitForTimeout(300);
  const metrics=await p.locator('.klx-metric').count();
  const overflow=await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth+2);
  const ok=panelVisible&&settings>0&&modal===1&&course>0&&metrics>=5&&!overflow&&!errors.length;
  if(!ok)failures++;
  console.log(ok?'PASS':'FAIL',width,JSON.stringify({panelVisible,settings,modal,course,metrics,overflow,errors:errors.slice(0,3)}));
  await ctx.close();
 }
 await browser.close();
 process.exit(failures?1:0);
})().catch(e=>{console.error(e);process.exit(1)});
