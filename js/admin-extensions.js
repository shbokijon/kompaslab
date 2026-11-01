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
  function monitorTemplate() {
    const navBtn=node('button','sb-item');navBtn.type='button';navBtn.id='klxNavSystem';navBtn.innerHTML='<span class="sb-icon">🩺</span><span class="sb-label">Tizim holati</span>';
    navBtn.addEventListener('click',()=>{nav('klx-system',navBtn);$('pgTitle').textContent='Tizim holati';loadSystem();});
    const navParent=document.querySelector('.sb-nav');
    const settings=navParent?.querySelector('[onclick*="settings"]');
    if(settings)settings.before(navBtn); else navParent?.appendChild(navBtn);
    const sec=node('div','sec');sec.id='sec-klx-system';
    sec.innerHTML='<div class="card"><div class="ch"><h2>🩺 Supabase va Vercel</h2><button class="btn bs bsm" id="klxRefresh">🔄 Yangilash</button></div><div class="mb">'+
      '<p class="klx-muted">Faqat tasdiqlangan real metrikalar koʻrsatiladi; hisoblanmagan usage nol sifatida tasvirlanmaydi.</p>'+
      '<div id="klxUsage" class="klx-monitor-grid">Yuklanmoqda...</div></div></div>'+
      '<div class="card klx-margin"><div class="ch"><h2>🛡️ Admin Audit</h2></div><div id="klxAudit" class="mb klx-muted">Yuklanmoqda...</div></div>';
    document.querySelector('.pg')?.appendChild(sec);
    $('klxRefresh').addEventListener('click',loadSystem);
  }
  async function loadSystem() {
    const el=$('klxUsage'); el.textContent='Yuklanmoqda...';
    try {
      const d=await rpc('kompas_admin_usage');
      const dbSize=fmtBytes(d.database_bytes);
      const figures=[
        ['Database footprint',dbSize,'PostgreSQL umumiy hajmi, quota emas'],
        ['Lablar',d.course_count,'Supabase courses'],
        ['Modullar',d.module_count,'Supabase modules'],
        ['Darslar',d.lesson_count,'Supabase lessons'],
        ['Foydalanuvchilar',d.profiles_count,'Supabase profiles'],
        ['Vercel usage','Ulanmagan','Maxfiy API token serverda konfiguratsiya qilinishi kerak']
      ];
      el.replaceChildren();
      figures.forEach(([name,value,help])=>{
        const card=node('div','klx-metric');
        card.appendChild(node('div','klx-muted',name));card.appendChild(node('strong','klx-number',String(value)));
        card.appendChild(node('small','klx-muted',help));el.appendChild(card);
      });
      const x=await supabase.from('kompas_admin_audit').select('action,created_at,detail').order('created_at',{ascending:false}).limit(15);
      if(x.error)throw x.error;
      const audit=$('klxAudit');
      audit.replaceChildren();
      if(!x.data?.length){audit.textContent='Hozircha audit yozuvlari yoʻq';return;}
      x.data.forEach(a=>{
        const row=node('div','sd-act-row');
        row.appendChild(node('span','sd-act-dot'));
        row.appendChild(node('div','',new Date(a.created_at).toLocaleString('uz-Latn')+' · '+a.action+' · '+(a.detail?.reason||'')));
        audit.appendChild(row);
      });
    }catch(e){el.textContent='Metrika olinmadi: '+e.message;$('klxAudit').textContent='Audit maʼlumotlari olinmadi';}
  }
  async function initialize(){
    modalTemplate();monitorTemplate();
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
        $('klxNavSystem').hidden=true;
        nav(allowed[0]||'overview',null);
      }
      if($('sbRole'))$('sbRole').textContent=isSuper?'Super Admin':(await supabase.from('kompas_staff_roles').select('role').eq('user_id',s.data.session.user.id).maybeSingle()).data?.role||'Admin';
      decorateRegs();
    }catch(e){console.warn('Admin extras:',e.message);}
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',initialize);
  else initialize();
})();
