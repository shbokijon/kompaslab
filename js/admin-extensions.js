/* Kompas Lab Admin Extensions v1. Uses existing design tokens and .btn/.card/.fld/.ovl styles.
   All writes happen in audited, authenticated Supabase RPCs; never trust UI-only permissions. */
(function () {
  'use strict';
  const $ = id => document.getElementById(id);
  const safe = value => String(value == null ? '' : value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  let selected = null, courseCache = [], moduleCache = [], isSuper = false;
  function notify(t){ if(typeof toast==='function') toast(t); }
  function fmtBytes(n) { if(!Number.isFinite(Number(n)))return '—';let x=Number(n),u=['B','KB','MB','GB'];let i=0;while(x>=1024&&i<u.length-1){x/=1024;i++}return x.toFixed(i?1:0)+' '+u[i]; }
  function node(tag, className, content){const el=document.createElement(tag);if(className)el.className=className;if(content!==undefined)el.textContent=content;return el;}
  async function rpc(name, args) { const r=await supabase.rpc(name,args||{});if(r.error)throw new Error(r.error.message);return r.data; }
  function selectOptions(items, selectedValue) {return items.map(x=>'<option value="'+safe(x.value)+'"'+(x.value===selectedValue?' selected':'')+'>'+safe(x.title)+'</option>').join('');}
  function modalTemplate() {
    const wrapper=node('div','ovl');wrapper.id='m-access-settings';
    wrapper.innerHTML='<div class="mdl klx-modal" role="dialog" aria-modal="true" aria-labelledby="klxTitle">'+
      '<div class="mh"><h3 id="klxTitle">🔐 Foydalanuvchini sozlash</h3><button class="mx" id="klxClose" aria-label="Yopish">×</button></div>'+
      '<div class="mb"><p id="klxWho" class="klx-muted"></p>'+
      '<div class="fr"><div class="fld"><label for="klxStatus">Hisob holati</label><select id="klxStatus"><option value="active">Faol</option><option value="restricted">Cheklangan (pullik kontent yopiq)</option><option value="suspended">Bloklangan (pullik kontent yopiq)</option></select></div>'+
      '<div class="fld"><label for="klxStaff">Admin roli</label><select id="klxStaff"><option value="student">Oʻquvchi</option><option value="support">Support Admin</option><option value="content">Content Admin</option><option value="finance">Finance Admin</option></select></div></div>'+
      '<div class="fld"><label for="klxReason">Sabab / audit izohi *</label><input id="klxReason" maxlength="400" placeholder="Masalan: 7 kunlik pilot kirish" autocomplete="off"></div>'+
      '<div class="klx-actions"><button class="btn bs bsm" id="klxSaveStatus">Holatni saqlash</button><button class="btn bs bsm" id="klxSaveRole">Rolni saqlash</button><button class="btn bs bsm klx-danger" id="klxDeleteRequest">Oʻchirish soʻrovi</button></div>'+
      '<hr class="klx-sep"><b>Lab va modul ruxsati</b>'+
      '<div class="fr klx-two"><div class="fld"><label for="klxCourse">Lab</label><select id="klxCourse"></select></div>'+
      '<div class="fld"><label for="klxModule">Modul</label><select id="klxModule"><option value="">Barcha modullar</option></select></div></div>'+
      '<div class="fld"><label for="klxExpiry">Ruxsat tugash sanasi (ixtiyoriy)</label><input id="klxExpiry" type="datetime-local"></div>'+
      '<div class="klx-actions"><button class="btn bp bsm" id="klxGrant">+ Ruxsat berish</button><button class="btn bs bsm" id="klxRevoke">Ruxsatni bekor qilish</button></div>'+
      '<div class="klx-muted klx-hint">Ruxsat toʻlovni tasdiqlamaydi. Mavjud pullik obuna alohida boshqariladi; bu yerdagi bekor qilish faqat qoʻlda berilgan ruxsatga taʼsir qiladi.</div>'+
      '<h4 class="klx-small-title">Amaldagi individual ruxsatlar</h4><div id="klxGrants" class="klx-grants"></div></div>'+
      '<div class="mf"><button class="btn bs" id="klxBottomClose">Yopish</button></div></div>';
    document.body.appendChild(wrapper);
    const close=()=>wrapper.classList.remove('open');
    $('klxClose').addEventListener('click',close);$('klxBottomClose').addEventListener('click',close);
    wrapper.addEventListener('click',e=>{if(e.target===wrapper)close();});
    $('klxCourse').addEventListener('change',showModules);
    $('klxSaveStatus').addEventListener('click',()=>execute('set_status'));
    $('klxSaveRole').addEventListener('click',()=>execute('set_staff'));
    $('klxDeleteRequest').addEventListener('click',requestDeletion);
    $('klxGrant').addEventListener('click',()=>execute('grant'));
    $('klxRevoke').addEventListener('click',()=>execute('revoke'));
  }
  async function openAccess(id,name,email){
    selected={id,name,email};
    $('klxWho').textContent=(name||'Foydalanuvchi')+' · '+(email||'');
    $('klxReason').value=''; $('klxExpiry').value='';
    $('m-access-settings').classList.add('open');
    try {
      const [state,courses,modules]=await Promise.all([
        rpc('kompas_admin_user_state',{p_target:id}),
        supabase.from('courses').select('id,slug,title').order('title'),
        supabase.from('modules').select('id,course_id,order_index,title').order('order_index')
      ]);
      if(courses.error||modules.error) throw new Error((courses.error||modules.error).message);
      if(!state)throw new Error('Ruxsat yetarli emas');
      courseCache=courses.data||[];moduleCache=modules.data||[];
      $('klxStatus').value=state.status||'active';$('klxStaff').value=state.staff||'student';
      $('klxStaff').disabled=!isSuper;$('klxSaveRole').disabled=!isSuper;$('klxDeleteRequest').hidden=!isSuper;
      $('klxCourse').innerHTML=selectOptions(courseCache.map(c=>({value:c.id,title:c.title||c.slug})));
      showModules(); renderGrants(state.grants||[]);
    }catch(e){notify('❌ '+e.message);}
  }
  function showModules(){
    const id=$('klxCourse').value;
    const list=moduleCache.filter(m=>m.course_id===id);
    $('klxModule').innerHTML='<option value="">Barcha modullar</option>'+selectOptions(list.map(m=>({value:m.id,title:'M'+m.order_index+' — '+(m.title||'Modul')})));
  }
  function renderGrants(grants){
    const target=$('klxGrants');target.replaceChildren();
    if(!grants.length){target.appendChild(node('p','klx-muted','Individual ruxsat mavjud emas'));return;}
    grants.forEach(g=>{
      const c=courseCache.find(c=>c.id===g.course_id);
      const m=moduleCache.find(m=>m.id===g.module_id);
      const row=node('div','klx-grant');
      row.appendChild(node('span','',((c&&c.title)||'Lab')+' · '+(m?'M'+m.order_index:'Barcha modullar')));
      row.appendChild(node('small','klx-muted',g.expires_at?new Date(g.expires_at).toLocaleDateString('uz-Latn'):'Muddatsiz'));
      target.appendChild(row);
    });
  }
  async function execute(action) {
    if(!selected)return;
    const reason=$('klxReason').value.trim();
    if(reason.length<3){notify('⚠️ Sababni yozing (kamida 3 belgi)');$('klxReason').focus();return;}
    const course=$('klxCourse').value||null,mod=$('klxModule').value||null;
    const value=action==='set_staff'?($('klxStaff').value==='student'?'none':$('klxStaff').value):action==='set_status'?$('klxStatus').value:null;
    const expiry=$('klxExpiry').value?new Date($('klxExpiry').value).toISOString():null;
    const detail=action==='grant'?'ruxsat berish':action==='revoke'?'qoʻlda berilgan ruxsatni bekor qilish':action==='set_staff'?'rolni almashtirish':'hisob holatini almashtirish';
    if(!confirm(selected.name+' · '+detail+'. Davom etilsinmi?'))return;
    try {
      await rpc('kompas_admin_manage_user',{p_action:action,p_target:selected.id,p_course:course,p_module:mod,p_value:value,p_expires:expiry,p_reason:reason});
      notify('✅ Oʻzgarish audit bilan saqlandi');
      const s=await rpc('kompas_admin_user_state',{p_target:selected.id});renderGrants(s.grants||[]);
    } catch(e) {notify('❌ '+e.message);}
  }
  async function requestDeletion(){
    if(!selected||!isSuper)return;
    const reason=$('klxReason').value.trim();
    if(reason.length<8){notify('⚠️ Oʻchirish sababi kamida 8 belgidan iborat boʻlsin');return;}
    const confirmText=prompt('Bu hisobni bloklaydi va oʻchirishni tekshirishga yuboradi. Toʻlov tarixi va Auth hisob hozir oʻchirilmaydi. Tasdiqlash uchun emailni aynan yozing:', '');
    if(confirmText!==selected.email){notify('Oʻchirish soʻrovi bekor qilindi');return;}
    try{
      await rpc('kompas_admin_request_deletion',{p_target:selected.id,p_reason:reason});
      $('klxStatus').value='suspended';
      notify('✅ Oʻchirish soʻrovi qayd etildi; hisob cheklangan');
      const state=await rpc('kompas_admin_user_state',{p_target:selected.id});
      renderGrants(state.grants||[]);
    }catch(e){notify('❌ '+e.message);}
  }
  // Preserve original register table rendering; extend with an extra action column.
  function decorateRegs() {
    const table=$('tbRegs')?.closest('table');if(!table)return;
    const head=table.querySelector('thead tr');if(!head.querySelector('.klx-header')){const th=node('th','klx-header','Sozlash');head.appendChild(th);}
    const rows=(typeof regsFiltered==='function'?regsFiltered():[]);
    Array.from($('tbRegs').rows).forEach((tr,i)=>{
      if(i>=rows.length||tr.querySelector('.klx-cell'))return;
      const td=node('td','klx-cell'),btn=node('button','btn bs bsm','⚙️ Sozlash');btn.type='button';
      const u=rows[i];btn.addEventListener('click',()=>openAccess(u.id,[u.first_name,u.last_name].filter(Boolean).join(' ')||u.email,u.email));
      td.appendChild(btn);tr.appendChild(td);
    });
  }
  // "Tizim holati" alohida boʻlim boʻlishi toʻxtatildi (2026-11-06): ikkalasi ham kompas_admin_usage ni oʻqirdi.
  // Endi bitta "Tizim" boʻlimi (admin.html #sec-system); bu yerdan faqat Admin Audit kartasi qoʻshiladi.
  function monitorTemplate() {
    const sec=$('sec-system');if(!sec)return;
    const card=node('div','card klx-margin');
    card.innerHTML='<div class="ch"><h2>🛡️ Admin Audit</h2><button class="btn bs bsm" id="klxRefresh">🔄 Yangilash</button></div><div id="klxAudit" class="mb klx-muted">Yuklanmoqda...</div>';
    sec.appendChild(card);
    $('klxRefresh').addEventListener('click',loadSystem);
  }
  async function loadSystem() {
    const audit=$('klxAudit');if(!audit)return;
    audit.textContent='Yuklanmoqda...';
    try {
      const x=await supabase.from('kompas_admin_audit').select('action,created_at,detail').order('created_at',{ascending:false}).limit(15);
      if(x.error)throw x.error;
      audit.replaceChildren();
      if(!x.data?.length){audit.textContent='Hozircha audit yozuvlari yoʻq';return;}
      x.data.forEach(a=>{
        const row=node('div','sd-act-row');
        row.appendChild(node('span','sd-act-dot'));
        row.appendChild(node('div','',new Date(a.created_at).toLocaleString('uz-Latn')+' · '+a.action+' · '+(a.detail?.reason||'')));
        audit.appendChild(row);
      });
    }catch(e){audit.textContent='Audit maʼlumotlari olinmadi: '+e.message;}
  }
  window.klxLoadAudit=loadSystem;
  // ---- Hamkor, mentor va jamoa ruxsatlari: email boʻyicha, roʻyxatdan oʻtmagan boʻlsa ham ----
  const KIND_LABEL={team:'Jamoa',partner:'Hamkor',mentor:'Mentor',manual:'Qoʻlda'};
  function fmtDate(v){return v?new Date(v).toLocaleDateString('uz-Latn'):'Muddatsiz';}
  function accessTemplate(){
    const navBtn=node('button','sb-item');navBtn.type='button';navBtn.id='klxNavAccess';
    navBtn.innerHTML='<span class="sb-icon">🤝</span><span class="sb-label">Ruxsatlar</span>';
    navBtn.addEventListener('click',()=>{nav('klx-access',navBtn);$('pgTitle').textContent='Hamkor va mentor ruxsatlari';loadAccess();});
    const before=$('sysNav');
    if(before)before.before(navBtn);else document.querySelector('.sb-nav')?.appendChild(navBtn);
    const sec=node('div','sec');sec.id='sec-klx-access';
    sec.innerHTML='<div class="card"><div class="ch"><h2>🤝 Ruxsat berish</h2></div><div class="mb">'+
      '<p class="klx-muted">Jamoa aʼzosi, hamkor yoki mentorga Lab yoki bitta modulni ochadi. Email hali roʻyxatdan oʻtmagan boʻlsa, ruxsat kutiladi va email tasdiqlangach avtomatik faollashadi. Toʻlov yozuvi yaratilmaydi; obuna alohida boshqariladi.</p>'+
      '<div class="fr klx-two"><div class="fld"><label for="klxaEmail">Email *</label><input id="klxaEmail" type="email" maxlength="254" autocomplete="off" placeholder="ism@example.com"></div>'+
      '<div class="fld"><label for="klxaKind">Turi</label><select id="klxaKind"><option value="team">Jamoa</option><option value="partner">Hamkor</option><option value="mentor">Mentor</option></select></div></div>'+
      '<div class="fr klx-two"><div class="fld"><label for="klxaCourse">Lab</label><select id="klxaCourse"></select></div>'+
      '<div class="fld"><label>Modullar</label><div id="klxaModules" class="klx-mods"></div></div></div>'+
      '<div class="fr klx-two"><div class="fld"><label for="klxaExpiry">Tugash sanasi (ixtiyoriy)</label><input id="klxaExpiry" type="datetime-local"></div>'+
      '<div class="fld"><label for="klxaReason">Sabab / audit izohi *</label><input id="klxaReason" maxlength="400" autocomplete="off" placeholder="Masalan: Strategiya hamkori, kontent tekshiruvi"></div></div>'+
      '<div class="klx-actions"><button class="btn bp bsm" id="klxaGrant" type="button">+ Ruxsat berish</button></div></div></div>'+
      '<div class="card klx-margin"><div class="ch"><h2>Faol ruxsatlar</h2><button class="btn bs bsm" id="klxaRefresh" type="button">🔄 Yangilash</button></div><div id="klxaList" class="mb klx-muted">Yuklanmoqda...</div></div>';
    document.querySelector('.pg')?.appendChild(sec);
    $('klxaCourse').addEventListener('change',showAccessModules);
    $('klxaGrant').addEventListener('click',grantByEmail);
    $('klxaRefresh').addEventListener('click',loadAccess);
  }
  function showAccessModules(){
    const id=$('klxaCourse').value;
    const list=moduleCache.filter(m=>m.course_id===id);
    const box=$('klxaModules');box.replaceChildren();
    const mk=(value,text,cls)=>{const l=node('label','klx-modopt'+(cls?' '+cls:''));const i=document.createElement('input');i.type='checkbox';i.value=value;l.appendChild(i);l.appendChild(document.createTextNode(' '+text));box.appendChild(l);return i;};
    const all=mk('','Barcha modullar (butun Lab)','klx-modall');all.checked=true;
    const items=list.map(m=>mk(m.id,'M'+m.order_index+' — '+(m.title||'Modul')));
    all.addEventListener('change',()=>{if(all.checked)items.forEach(i=>{i.checked=false;});});
    items.forEach(i=>i.addEventListener('change',()=>{if(i.checked)all.checked=false;else if(!items.some(x=>x.checked))all.checked=true;}));
  }
  async function loadAccessRefs(){
    if(courseCache.length&&moduleCache.length)return;
    const [c,m]=await Promise.all([
      supabase.from('courses').select('id,slug,title').order('title'),
      supabase.from('modules').select('id,course_id,order_index,title').order('order_index')
    ]);
    if(c.error||m.error)throw new Error((c.error||m.error).message);
    courseCache=c.data||[];moduleCache=m.data||[];
  }
  async function loadAccess(){
    const box=$('klxaList');box.textContent='Yuklanmoqda...';
    try{
      await loadAccessRefs();
      const withModules=courseCache.filter(c=>moduleCache.some(m=>m.course_id===c.id));
      const keep=$('klxaCourse').value;
      $('klxaCourse').innerHTML=selectOptions(withModules.map(c=>({value:c.id,title:c.title||c.slug})));
      if(keep)$('klxaCourse').value=keep;
      showAccessModules();
      const d=await rpc('kompas_admin_list_grants');
      renderAccessList(d.grants||[],d.pending||[]);
    }catch(e){box.textContent='Ruxsatlar olinmadi: '+e.message;}
  }
  function accessRow(x,pending){
    const row=node('div','klx-grant');
    const left=node('div');
    left.appendChild(node('div','',(pending?x.email:(x.name?x.name+' · ':'')+x.email)));
    left.appendChild(node('small','klx-muted',x.course_title+' · '+(x.module_index!=null?'M'+x.module_index:'Barcha modullar')+' · '+(KIND_LABEL[x.kind]||x.kind)+' · '+fmtDate(x.expires_at)+(pending?' · roʻyxatdan oʻtishni kutmoqda':'')+' · '+x.reason));
    const btn=node('button','btn bs bsm','Bekor qilish');btn.type='button';
    btn.addEventListener('click',()=>revokeAccess(pending?'pending':'grant',x.id,x.email));
    row.appendChild(left);row.appendChild(btn);return row;
  }
  function renderAccessList(grants,pending){
    const box=$('klxaList');box.replaceChildren();
    if(!grants.length&&!pending.length){box.textContent='Hozircha qoʻlda berilgan ruxsat yoʻq';return;}
    pending.forEach(x=>box.appendChild(accessRow(x,true)));
    grants.forEach(x=>box.appendChild(accessRow(x,false)));
  }
  async function grantByEmail(){
    const email=$('klxaEmail').value.trim().toLowerCase(),reason=$('klxaReason').value.trim();
    if(!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)){notify('⚠️ Emailni toʻgʻri yozing');$('klxaEmail').focus();return;}
    if(reason.length<3){notify('⚠️ Sababni yozing (kamida 3 belgi)');$('klxaReason').focus();return;}
    const course=$('klxaCourse').value;
    if(!course){notify('⚠️ Labni tanlang');return;}
    const picked=Array.from($('klxaModules').querySelectorAll('input:checked')).map(i=>i.value);
    const mods=(!picked.length||picked.includes(''))?[null]:picked;
    const expiry=$('klxaExpiry').value?new Date($('klxaExpiry').value).toISOString():null;
    const what=$('klxaCourse').selectedOptions[0].textContent+' · '+(mods[0]===null?'barcha modullar':mods.length+' ta modul');
    if(!confirm(email+' uchun ruxsat: '+what+'. Davom etilsinmi?'))return;
    let done=0,status='granted';
    try{
      for(const mod of mods){
        const r=await rpc('kompas_admin_grant_by_email',{p_email:email,p_course:course,p_module:mod,p_expires:expiry,p_kind:$('klxaKind').value,p_reason:reason});
        done++;status=r.status;
      }
      notify(status==='pending'?'✅ Saqlandi: roʻyxatdan oʻtib, emailni tasdiqlagach faollashadi':'✅ Ruxsat berildi');
      $('klxaEmail').value='';$('klxaReason').value='';$('klxaExpiry').value='';
      loadAccess();
    }catch(e){notify('❌ '+accessError(e.message)+(done?' (oldingi '+done+' ta saqlandi)':''));if(done)loadAccess();}
  }
  async function revokeAccess(kind,id,email){
    const reason=(prompt(email+' uchun ruxsatni bekor qilish sababi:','')||'').trim();
    if(reason.length<3){notify('Bekor qilish toʻxtatildi: sabab kerak');return;}
    try{await rpc('kompas_admin_revoke_access',{p_kind:kind,p_id:id,p_reason:reason});notify('✅ Ruxsat bekor qilindi');loadAccess();}
    catch(e){notify('❌ '+accessError(e.message));}
  }
  function accessError(m){
    const map={PROTECTED_ACCOUNT:'Admin yoki oʻzingizning hisobingizga ruxsat berib boʻlmaydi',PROTECTED_STAFF_ACCOUNT:'Boshqa xodim hisobini faqat Super Admin oʻzgartiradi',INVALID_EMAIL:'Email notoʻgʻri',REASON_REQUIRED:'Sabab kerak',INVALID_EXPIRY:'Tugash sanasi kelajakda va 5 yildan oshmasligi kerak',ACCESS_DENIED:'Ruxsat yetarli emas',NOT_FOUND:'Yozuv topilmadi (allaqachon bekor qilingan boʻlishi mumkin)'};
    const k=Object.keys(map).find(k=>String(m).includes(k));return k?map[k]:m;
  }
  async function initialize(){
    modalTemplate();monitorTemplate();accessTemplate();
    const old=window.renderRegs;
    if(typeof old==='function')window.renderRegs=function(){const result=old.apply(this,arguments);decorateRegs();return result;};
    try {
      const s=await supabase.auth.getSession();
      if(!s.data?.session)return;
      const me=await supabase.from('profiles').select('role').eq('id',s.data.session.user.id).single();
      isSuper=me.data?.role==='admin';
      // Restricted staff access is constrained in the database and the interface.
      if(!isSuper){
        const role=await supabase.from('kompas_staff_roles').select('role').eq('user_id',s.data.session.user.id).maybeSingle();
        const staff=role.data?.role;
        const allowed=staff==='support'?['regs']:staff==='content'?['lessons']:staff==='finance'?['payments']:[];
        document.querySelectorAll('.sb-item[onclick]').forEach(btn=>{
          const match=btn.getAttribute('onclick')?.match(/nav\('([^']+)'/);
          if(match&&!allowed.includes(match[1]))btn.hidden=true;
        });
        $('klxNavAccess').hidden=staff!=='support';
        nav(allowed[0]||'overview',null);
      }
      if($('sbRole'))$('sbRole').textContent=isSuper?'Super Admin':(await supabase.from('kompas_staff_roles').select('role').eq('user_id',s.data.session.user.id).maybeSingle()).data?.role||'Admin';
      decorateRegs();
    }catch(e){console.warn('Admin extras:',e.message);}
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',initialize);
  else initialize();
})();
