(function(){
'use strict';
var KEY='kompas-master-planner-v1';
var TASKS=[
['M0','Oʻz maqsadim va dastur turini aniqladim'],
['M1','Dastur/ilmiy yoʻnalish uchun saralangan roʻyxat (Shortlist) tuzdim'],
['M2','Muddatlar va ishlar rejasini tayyorladim'],
['M3','Akademik CV tayyorladim'],
['M4','Tavsiya beruvchilar va zarur aloqa rejasini tuzdim'],
['M5','Maqsad bayonnomasini (Statement of Purpose, SoP) yozdim'],
['M6','Kerak boʻlsa ilmiy loyiha taklifini (Research Proposal) tayyorladim'],
['M7','Grant va xarajatlarni rasmiy manbalardan tekshirdim'],
['M8','Intervyu va joʻnash uchun reja tuzdim']
];
var FUND={unknown:'hali nomaʼlum',possible:'tekshirish kerak','self-funded':'oʻz hisobimdan'};
var DEFAULT={goal:'',degree:'taught',intake:'2027',countries:'',tasks:{},programmes:[]};
var state;
function $ (id){return document.getElementById(id)}
function load(){try{var d=JSON.parse(localStorage.getItem(KEY)||'null');return d&&typeof d==='object'?Object.assign({},DEFAULT,d):Object.assign({},DEFAULT)}catch(e){return Object.assign({},DEFAULT)}}
function save(){try{localStorage.setItem(KEY,JSON.stringify(state));return true}catch(e){$('dataStatus').textContent='Brauzer xotirasiga yozib boʻlmadi. Eksport orqali saqlang.';return false}}
function status(id,t){$(id).textContent=t}
function fields(){['goal','degree','intake','countries'].forEach(function(x){$(x).value=state[x]||DEFAULT[x]})}
function tasks(){var root=$('taskList');root.textContent='';var completed=0;TASKS.forEach(function(t){var li=document.createElement('li');var lab=document.createElement('label');var cb=document.createElement('input');cb.type='checkbox';cb.checked=!!state.tasks[t[0]];if(cb.checked)completed++;cb.addEventListener('change',function(){state.tasks[t[0]]=cb.checked;save();tasks()});lab.appendChild(cb);lab.appendChild(document.createTextNode(t[0]+': '+t[1]));li.appendChild(lab);root.appendChild(li)});$('bar').style.width=(completed/TASKS.length*100)+'%';$('progressText').textContent=completed+' / '+TASKS.length+' bosqich belgilangan'}
function programmes(){var root=$('programmesList');root.textContent='';if(!state.programmes.length){var p=document.createElement('p');p.className='ss-note';p.textContent='Hozircha dasturlar kiritilmagan. Universitet dasturining rasmiy havolasidan boshlang.';root.appendChild(p);return}
state.programmes.forEach(function(p,i){var block=document.createElement('div');block.className='ss-programme';var title=document.createElement('strong');title.textContent=p.university+' — '+p.programme;block.appendChild(title);
var small=document.createElement('small');small.textContent='Holat: foydalanuvchi qoʻshgan, Kompas tekshirmagan · Oxirgi muddat: '+(p.deadline||'nomaʼlum')+' · Moliyalashtirish: '+(FUND[p.funding]||p.funding);block.appendChild(small);
var a=document.createElement('a');a.href=p.officialUrl;a.target='_blank';a.rel='noopener noreferrer';a.textContent='Rasmiy deb koʻrsatilgan havolani tekshirish';block.appendChild(a);
var btn=document.createElement('button');btn.textContent='Oʻchirish';btn.type='button';btn.addEventListener('click',function(){state.programmes.splice(i,1);save();programmes()});block.appendChild(document.createElement('br'));block.appendChild(btn);root.appendChild(block)})}
function init(){state=load();if(!state.tasks||typeof state.tasks!=='object')state.tasks={};if(!Array.isArray(state.programmes))state.programmes=[];
fields();tasks();programmes();
$('saveProfile').addEventListener('click',function(){['goal','degree','intake','countries'].forEach(function(k){state[k]=$(k).value.trim()});status('profileStatus',save()?'Saqlandi — faqat shu qurilmada.':'Eksport qiling.')});
$('addProgramme').addEventListener('submit',function(e){e.preventDefault();var u=$('officialUrl').value.trim();var valid;try{valid=new URL(u)}catch(err){status('addStatus','Havola toʻgʻri emas.');return}if(valid.protocol!=='https:'||!valid.hostname.includes('.')||valid.username||valid.password){status('addStatus','Faqat ochiq HTTPS havolalarini qoʻshing.');return}
var d={university:$('university').value.trim(),programme:$('programme').value.trim(),officialUrl:valid.href,deadline:$('deadline').value,funding:$('funding').value,checked:false};if(!d.university||!d.programme||state.programmes.length>=40){status('addStatus','Nomlar majburiy. Roʻyxatga koʻpi bilan 40 ta dastur qoʻshiladi.');return}state.programmes.push(d);save();programmes();$('addProgramme').reset();status('addStatus','Dastur qoʻshildi. Uning rasmiyligini va talablarini oʻzingiz tekshiring.')});
$('export').addEventListener('click',function(){var blob=new Blob([JSON.stringify({format:'kompas-master-planner-v1',exported_at:new Date().toISOString(),data:state},null,2)],{type:'application/json'});var a=document.createElement('a');var u=URL.createObjectURL(blob);a.href=u;a.download='kompas-master-reja.json';document.body.appendChild(a);a.click();a.remove();setTimeout(function(){URL.revokeObjectURL(u)},1000);status('dataStatus','JSON fayli tayyorlandi.')});
$('clear').addEventListener('click',function(){if(!confirm('Shu qurilmadagi Kompas Master rejasini butunlay tozalaysizmi?'))return;localStorage.removeItem(KEY);state=load();fields();tasks();programmes();status('dataStatus','Mahalliy reja tozalandi.')})
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();