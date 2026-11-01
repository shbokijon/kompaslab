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
 const {data,error}=await supabase.from('access_grants')
 .select('id,course_id,module_id,expires_at,revoked_at,note,created_at')
 .eq('user_id',accessSelectedUser).order('created_at',{ascending:false}).limit(60);
 const el=document.getElementById('accessActive');
 if(error){accessUiMessage('Migration hali qoʻllanmagan yoki ruxsat yoʻq: '+error.message,true);return;}
 const items=(data||[]).filter(g=>!g.revoked_at);
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
 const {error}=await supabase.rpc('admin_set_access',{p_user_id:accessSelectedUser,p_course_id:g.course_id,
 p_module_id:g.module_id,p_revoke:true,p_note:'Admin tomonidan bekor qilindi'});
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
  const {error}=await supabase.rpc('admin_set_access',{
   p_user_id:accessSelectedUser,p_course_id:cid,p_module_id:mod||null,
   p_expires_at:expiry?new Date(expiry).toISOString():null,p_note:note,p_revoke:false
  });
  if(error)throw error;
  toast('✅ Ruxsat saqlandi');await accessLoadGrants();
 }catch(e){accessUiMessage(e.message,true);}
 finally{btn.disabled=false;}
}
async function loadSystemStats() {
 const box=document.getElementById('sysMetrics');
 box.textContent='Yuklanmoqda…';
 const {data,error}=await supabase.rpc('admin_system_stats');
 if(error){box.textContent='Statistika mavjud emas: '+error.message;return;}
 const metrics=[
  ['Database hajmi',data.database_bytes!=null?(data.database_bytes/1048576).toFixed(2)+' MB':'—'],
  ['Database connections',data.database_connections??'—'],
  ['Roʻyxatdan oʻtganlar',data.registered_count??'—'],
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
 document.getElementById('sysFresh').textContent='Yangilandi: '+new Date(data.captured_at).toLocaleString('uz-UZ');
}
