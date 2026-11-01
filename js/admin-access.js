/* Kompas Lab admin extension — additive, no design-token overrides.
   Requires migration 20261101_admin_access_grants.sql.
   This script uses existing supabase, nav, toast and escHtml helpers. */
let accessSelectedUser = null;
let accessCourses = [];
let accessModules = [];
function accessUiMessage(message, isError=false) {
 const el=document.getElementById('accessMessage');
 if(!el) return;
 el.textContent=message;
 el.style.color=isError?'var(--red)':'var(--muted)';
}
async function openAccessFromReg(index) {
 const r=regsFiltered()[index];
 if(!r) return;
 accessSelectedUser=r.id;
 document.getElementById('accessPerson').textContent =
  [r.first_name,r.last_name].filter(Boolean).join(' ')+' · '+(r.email||'');
 document.getElementById('m-access').classList.add('open');
 accessUiMessage('Yuklanmoqda…');
 const {data:cs,error}=await supabase.from('courses').select('id,title,slug').order('title');
 if(error){accessUiMessage(error.message,true);return;}
 accessCourses=cs||[];
 const select=document.getElementById('accessCourse');
 select.replaceChildren(...accessCourses.map(c=>new Option(c.title,c.id)));
 await accessLoadModules();
 await accessLoadGrants();
}
async function accessLoadModules() {
 const cid=document.getElementById('accessCourse').value;
 const {data,error}=await supabase.from('modules').select('id,title,order_index').eq('course_id',cid).order('order_index');
 const el=document.getElementById('accessModule');
 if(error){accessUiMessage(error.message,true);return;}
 accessModules=data||[];
 el.replaceChildren(new Option('Butun Lab (barcha modullar)',''),...accessModules.map(m=>new Option('M'+m.order_index+' · '+m.title,m.id)));
}
async function accessLoadGrants() {
 if(!accessSelectedUser)return;
 const {data,error}=await supabase.rpc('kompas_admin_user_state',{p_target:accessSelectedUser});
 const el=document.getElementById('accessActive');
 if(error){accessUiMessage('Migration hali qoʻllanmagan yoki ruxsat yoʻq: '+error.message,true);return;}
 const items=(data?.grants||[]);
 document.getElementById('accessStatus').value=data?.status||'active';
 document.getElementById('accessStaff').value=data?.staff||'student';
 if(!items.length){el.innerHTML='<div class="empty">Maxsus ruxsat mavjud emas.</div>';accessUiMessage('Tayyor');return;}
 el.replaceChildren();
 items.forEach(g=>{
  const course=accessCourses.find(c=>c.id===g.course_id);
  const row=document.createElement('div');row.className='sd-course-row';row.style.gap='8px';
  const name=document.createElement('div');name.style.flex='1';name.style.minWidth='0';
  const title=document.createElement('strong');title.textContent=(course?.title||'Lab')+' · '+(g.module_id?'Tanlangan modul':'Barcha modullar');
  const detail=document.createElement('div');detail.style.fontSize='11px';detail.style.color='var(--muted)';
  detail.textContent=g.expires_at?'Tugash: '+new Date(g.expires_at).toLocaleDateString('uz-UZ'):'Muddatsiz';
  name.append(title,detail);
  const btn=document.createElement('button');btn.className='btn bd bsm';btn.textContent='Bekor qilish';
  btn.addEventListener('click',()=>accessRevoke(g));
  row.append(name,btn);el.appendChild(row);
 });
 accessUiMessage(items.length+' ta faol individual ruxsat');
}
async function accessRevoke(g) {
 if(!confirm('Ushbu maxsus ruxsatni bekor qilasizmi?'))return;
 const {error}=await supabase.rpc('kompas_admin_manage_user',{p_action:'revoke',p_target:accessSelectedUser,p_course:g.course_id,p_module:g.module_id,p_reason:'Individual ruxsat bekor qilindi'});
 if(error){accessUiMessage(error.message,true);return;}
 toast('Ruxsat bekor qilindi');await accessLoadGrants();
}
async function accessGrant() {
 if(!accessSelectedUser)return;
 const cid=document.getElementById('accessCourse').value;
 const mod=document.getElementById('accessModule').value;
 const expiry=document.getElementById('accessExpiry').value;
 const note=document.getElementById('accessNote').value.trim();
 if(!cid){accessUiMessage('Lab tanlang',true);return;}
 if(expiry && new Date(expiry)<=new Date()){accessUiMessage('Kelajakdagi sanani tanlang',true);return;}
 if(!confirm('Tanlangan Lab/modul uchun ruxsat berilsinmi?'))return;
 const btn=document.getElementById('accessGrantBtn');btn.disabled=true;
 try {
  const {error}=await supabase.rpc('kompas_admin_manage_user',{
   p_action:'grant',p_target:accessSelectedUser,p_course:cid,p_module:mod||null,
   p_expires:expiry?new Date(expiry).toISOString():null,p_reason:note||'Admin tomonidan individual ruxsat'
  });
  if(error)throw error;
  toast('✅ Ruxsat saqlandi');await accessLoadGrants();
 }catch(e){accessUiMessage(e.message,true);}
 finally{btn.disabled=false;}
}
async function loadSystemStats() {
 const box=document.getElementById('sysMetrics');
 box.textContent='Yuklanmoqda…';
 const {data,error}=await supabase.rpc('kompas_admin_usage');
 if(error){box.textContent='Statistika mavjud emas: '+error.message;return;}
 const metrics=[
  ['Database hajmi',data.database_bytes!=null?(data.database_bytes/1048576).toFixed(2)+' MB':'—'],
  ['Database connections','SQL monitoring'],
  ['Roʻyxatdan oʻtganlar',data.profiles_count??'—'],
  ['Lablar',data.course_count??'—'],
  ['Modullar',data.module_count??'—'],
  ['Darslar',data.lesson_count??'—']
 ];
 box.replaceChildren(...metrics.map(([name,value])=>{
  const item=document.createElement('div');item.className='ob';
  const inner=document.createElement('div');
  const val=document.createElement('div');val.className='ob-v';val.textContent=value;
  const label=document.createElement('div');label.className='ob-l';label.textContent=name;
  inner.append(val,label);item.appendChild(inner);return item;
 }));
 document.getElementById('sysFresh').textContent='Yangilandi: '+new Date(data.sampled_at).toLocaleString('uz-UZ');
 const quota=document.getElementById('sysQuota');
 if (quota && Number.isFinite(Number(data.database_bytes))) {
   // Snapshot: confirmed Supabase Free on 2026-11-01. Not a billing API reading.
   const maxBytes=500*1024*1024, used=Number(data.database_bytes);
   const pct=Math.min(100,Math.max(0,used/maxBytes*100));
   quota.replaceChildren();
   const row=document.createElement('div');row.className='mp';row.style.justifyContent='space-between';
   const label=document.createElement('span');label.textContent='Database / Free plan reference (500 MB)';
   const value=document.createElement('strong');value.textContent=pct.toFixed(1)+'%';
   row.append(label,value);
   const track=document.createElement('div');track.style.cssText='margin:10px 0 6px;background:var(--border);height:8px;border-radius:8px;overflow:hidden';
   const fill=document.createElement('div');fill.style.cssText='height:100%;background:var(--accent);border-radius:8px';
   fill.style.width=pct+'%';track.appendChild(fill);
   const caveat=document.createElement('p');caveat.style.cssText='font-size:11px;color:var(--muted)';
   caveat.textContent='Database hajmi SQL orqali oʻlchandi. 500 MB — 2026-11-01 dagi Free tarif uchun maʼlumotnoma, joriy hisob-faktura emas.';
   quota.append(row,track,caveat);
 }

}

async function accessSaveStatus() {
 const status=document.getElementById('accessStatus').value;
 const reason=document.getElementById('accessReason').value.trim();
 if(reason.length<3){accessUiMessage('Sabab kamida 3 belgi boʻlishi shart',true);return;}
 if(!confirm('Foydalanuvchi holatini '+status+' qilib oʻzgartirasizmi?'))return;
 const {error}=await supabase.rpc('kompas_admin_manage_user',{
   p_action:'set_status',p_target:accessSelectedUser,p_value:status,p_reason:reason
 });
 if(error){accessUiMessage(error.message,true);return;}
 toast('Holat saqlandi');await accessLoadGrants();
}
async function accessSaveStaff() {
 const v=document.getElementById('accessStaff').value;
 const reason=document.getElementById('accessReason').value.trim();
 if(reason.length<3){accessUiMessage('Sabab kamida 3 belgi boʻlishi shart',true);return;}
 if(!confirm('Cheklangan admin rolini '+v+' qilib oʻzgartirasizmi?'))return;
 const {error}=await supabase.rpc('kompas_admin_manage_user',{
   p_action:'set_staff',p_target:accessSelectedUser,p_value:v==='student'?'none':v,p_reason:reason
 });
 if(error){accessUiMessage(error.message,true);return;}
 toast('Rol saqlandi');await accessLoadGrants();
}
async function accessRequestDeletion() {
 const reason=document.getElementById('accessReason').value.trim();
 if(reason.length<8){accessUiMessage('Oʻchirish soʻrovi sababi kamida 8 belgi',true);return;}
 if(!confirm('Hisob SUSPENDED boʻladi va oʻchirish tekshiruvi yaratiladi. Davom etilsinmi?'))return;
 const {error}=await supabase.rpc('kompas_admin_request_deletion',{p_target:accessSelectedUser,p_reason:reason});
 if(error){accessUiMessage(error.message,true);return;}
 toast('Oʻchirish soʻrovi yaratildi. Auth hisobi hali oʻchirilmagan.');await accessLoadGrants();
}

async function loadAuditLog() {
 const box=document.getElementById('adminAuditList');
 if(!box)return;
 box.textContent='Yuklanmoqda…';
 const {data,error}=await supabase.from('kompas_admin_audit')
 .select('id,action,created_at,actor_id,target_id,detail').order('created_at',{ascending:false}).limit(50);
 if(error){box.textContent='Audit maʼlumotlari ochilmadi: '+error.message;return;}
 if(!data?.length){box.textContent='Audit tarixi boʻsh.';return;}
 const table=document.createElement('table');table.className='tbl';
 const head=document.createElement('thead'),hrow=document.createElement('tr');
 for(const title of ['Sana','Amal','Ijrochi','Nishon']) {
  const th=document.createElement('th');th.textContent=title;hrow.appendChild(th);
 }
 head.append(hrow);table.append(head);
 const body=document.createElement('tbody');
 for(const entry of data) {
  const tr=document.createElement('tr');
  for(const value of [new Date(entry.created_at).toLocaleString('uz-UZ'),entry.action,entry.actor_id,entry.target_id||'—']) {
   const td=document.createElement('td');td.textContent=value;td.style.wordBreak='break-word';tr.append(td);
  }
  body.append(tr);
 }
 table.append(body);box.replaceChildren(table);
}

/* Server-side Vercel billing usage. Backend validates Supabase JWT and Admin role,
 * never receives a provider token from the browser. */
async function loadVercelUsage() {
 const box=document.getElementById('vercelUsageBox');
 if(!box)return;
 box.textContent='Vercel billing usage yuklanmoqda…';
 try {
   const {data,error}=await supabase.auth.getSession();
   if(error || !data?.session?.access_token) throw new Error('Admin hisobingizga qayta kiring.');
   const resp=await fetch('/api/admin/vercel-usage',{
     method:'GET',
     headers:{Authorization:'Bearer '+data.session.access_token},
     cache:'no-store',
     credentials:'same-origin'
   });
   const body=await resp.json();
   if(!resp.ok) {
     const messages={
       VERCEL_TOKEN_NOT_CONFIGURED:'Vercel server tokeni hali sozlanmagan. Vercel → Project Settings → Environment Variables da VERCEL_API_TOKEN qoʻshing.',
       AUTH_SERVER_NOT_CONFIGURED:'Serverda SUPABASE_ANON_KEY sozlanmagan.',
       VERCEL_PERMISSION_DENIED:'Ushbu token yoki jamoa rolida billing usage oʻqish ruxsati yoʻq.',
       VERCEL_TOKEN_INVALID:'Vercel tokeni yaroqsiz yoki muddati tugagan.',
       ADMIN_ONLY:'Bu maʼlumotni faqat Super Admin koʻradi.',
       LOGIN_REQUIRED:'Hisobingizga qayta kiring.'
     };
     throw new Error(messages[body.error] || ('Vercel: '+(body.error||resp.status)));
   }
   const fmt=new Intl.NumberFormat('en-US',{style:'currency',currency:body.currency||'USD'});
   box.replaceChildren();
   const heading=document.createElement('div');
   heading.style.cssText='font-size:20px;font-weight:800;color:var(--accent)';
   heading.textContent=fmt.format(body.totalBilled || 0);
   const text=document.createElement('p');
   text.style.cssText='font-size:12px;color:var(--muted);margin:5px 0 12px';
   text.textContent='Jamoa miqyosidagi billed cost · '+new Date(body.from).toLocaleDateString('uz-UZ')+' — '+new Date(body.to).toLocaleDateString('uz-UZ')+' (UTC, oxirgi kun kiritilmagan)';
   box.append(heading,text);
   if(body.services?.length){
     const table=document.createElement('table');table.className='tbl';
     const tr=document.createElement('tr');
     ['Servis','Toʻlov','Satrlar'].forEach(label=>{
       const th=document.createElement('th');th.textContent=label;tr.appendChild(th);
     });
     const thead=document.createElement('thead');thead.append(tr);table.appendChild(thead);
     const tbody=document.createElement('tbody');
     body.services.forEach(item=>{
       const tr=document.createElement('tr');
       [item.service,fmt.format(item.billed),String(item.items)].forEach(label=>{
         const td=document.createElement('td');td.textContent=label;tr.appendChild(td);
       });
       tbody.appendChild(tr);
     });
     table.appendChild(tbody);
     const scroll=document.createElement('div');scroll.className='tbl-scroll';scroll.appendChild(table);
     box.appendChild(scroll);
   }else{
     const empty=document.createElement('p');empty.textContent='Ushbu davrda hisoblangan charge mavjud emas.';box.appendChild(empty);
   }
   const caveat=document.createElement('p');
   caveat.style.cssText='font-size:11px;color:var(--muted);margin-top:10px';
   caveat.textContent='Manba: Vercel FOCUS billing API. Bu tarif limiti, qolgan quota yoki aynan Kompas Lab loyihasi xarajati emas.';
   box.appendChild(caveat);
 } catch(e) {
   box.replaceChildren();
   const err=document.createElement('p');err.style.cssText='font-size:12px;color:var(--red)';
   err.textContent=e.message;
   const link=document.createElement('a');link.href='https://vercel.com/dashboard';
   link.target='_blank';link.rel='noopener noreferrer';link.textContent='Vercel Usage sahifasini ochish';
   box.append(err,link);
 }
}
