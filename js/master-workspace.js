
/* Kompas Lab — Master Application Workspace v0.1 (pilot)
   Uses existing js/config.js (supabase-js 2.45.4); no privileged key in browser.
*/
(function () {
  "use strict";
  const db = window.supabase;
  const $ = id => document.getElementById(id);
  const state = { user: null, workspace: null, artifact: null, m0Started: false, firstDone: false };
  const names = ["goal", "pathway_reason", "baseline", "risk", "next_task"];
  const allowedKinds = new Set(names);
  const projectUrl = "https://usxpkmbjrdllnitlzdpq.supabase.co";
  const uuid = () => crypto.randomUUID();
  function inform(text, error) {
    const n = $("notice");
    n.textContent = text;
    n.className = "notice" + (error ? " error" : "");
  }
  function result(response) {
    if (response.error) throw response.error;
    return response.data;
  }
  function authLink() {
    try { sessionStorage.setItem("returnTo", "master-application.html"); } catch (_) {}
  }
  async function emit(eventName, buttonId) {
    if (!$("trackConsent").checked) return;
    try {
      let visitor = sessionStorage.getItem("kl_pilot_visitor");
      if (!visitor) {
        visitor = uuid();
        sessionStorage.setItem("kl_pilot_visitor", visitor);
      }
      await fetch(projectUrl + "/functions/v1/conversion-track", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          event_name: eventName,
          event_id: uuid(),
          visitor_id: visitor,
          session_id: visitor,
          course_slug: "master-lab",
          page_path: location.pathname,
          button_id: buttonId
        })
      });
    } catch (_) { /* Analytics failure must not block core product */ }
  }
  async function ensureWorkspace() {
    if (state.workspace) return state.workspace;
    if (!state.user) throw new Error("Tizimga qayta kiring.");
    state.workspace = result(await db.from("application_workspaces")
      .insert({ title: "Mening magistratura rejam", track: $("track").value, status: "active" })
      .select().single());
    return state.workspace;
  }
  async function loadM0() {
    const steps = result(await db.from("master_m0_steps").select("step,title,instruction,output_key")
      .eq("is_active", true).order("step"));
    const root = $("m0Fields");
    root.replaceChildren();
    for (const step of steps) {
      if (!allowedKinds.has(step.output_key)) continue;
      const block = document.createElement("div");
      const label = document.createElement("label");
      label.htmlFor = "m0_" + step.output_key;
      label.textContent = step.step + ". " + step.title;
      const help = document.createElement("p");
      help.className = "help";
      help.textContent = step.instruction;
      const area = document.createElement("textarea");
      area.id = label.htmlFor;
      area.maxLength = 3000;
      area.value = state.artifact?.content?.[step.output_key] || "";
      block.append(label, help, area);
      root.append(block);
    }
  }
  async function loadPrograms() {
    const root = $("programs"); root.replaceChildren();
    if (!state.workspace) return;
    const rows = result(await db.from("application_programs").select(
      "id,institution,program_name,country,official_url,admission_deadline_at,deadline_status"
    ).eq("workspace_id", state.workspace.id).order("created_at", {ascending:false}));
    for (const row of rows) {
      const outer = document.createElement("div"); outer.className = "item";
      const heading = document.createElement("strong");
      heading.textContent = row.institution + " — " + row.program_name;
      const info = document.createElement("p"); info.className = "help";
      info.textContent = [row.country,
        row.admission_deadline_at ? new Date(row.admission_deadline_at).toLocaleString("uz-UZ") : "Deadline hali yoʻq",
        row.deadline_status].filter(Boolean).join(" · ");
      outer.append(heading, info);
      if (row.official_url && /^https:\/\//i.test(row.official_url)) {
        const link = document.createElement("a");
        link.textContent = "Asl rasmiy manbani ochish";
        link.href = row.official_url;
        link.target = "_blank";
        link.rel = "noopener noreferrer";
        outer.append(link);
      }
      root.append(outer);
    }
  }
  async function loadTasks() {
    const root = $("tasks"); root.replaceChildren();
    if (!state.workspace) return;
    const rows = result(await db.from("application_tasks")
      .select("id,title,status,due_at").eq("workspace_id", state.workspace.id)
      .order("created_at", {ascending:false}));
    for (const row of rows) {
      const div = document.createElement("div"); div.className = "item row";
      const detail = document.createElement("div");
      const strong = document.createElement("strong"); strong.textContent = row.title;
      const meta = document.createElement("p"); meta.className="help";
      meta.textContent = [row.status, row.due_at ? new Date(row.due_at).toLocaleString("uz-UZ") : ""].filter(Boolean).join(" · ");
      detail.append(strong,meta);
      const btn = document.createElement("button"); btn.type="button";
      btn.textContent = row.status === "done" ? "Bajarilgan" : "Bajarildi";
      btn.className = "secondary"; btn.disabled = row.status === "done";
      btn.addEventListener("click", async () => {
        btn.disabled = true;
        try {
          result(await db.from("application_tasks")
            .update({status:"done", completed_at:new Date().toISOString()})
            .eq("id",row.id).eq("workspace_id",state.workspace.id));
          if (!state.firstDone) {
            state.firstDone=true;
            await emit("first_task_completed","finish_task");
          }
          inform("Vazifa bajarildi"); await loadTasks();
        } catch (e) { inform(e.message,true); btn.disabled=false; }
      });
      div.append(detail,btn); root.append(div);
    }
  }
  async function hydrate() {
    const workspaces = result(await db.from("application_workspaces").select("*")
      .eq("owner_id",state.user.id).order("created_at").limit(1));
    state.workspace = workspaces?.[0] || null;
    const artifacts = state.workspace ?
      result(await db.from("application_artifacts").select("*")
        .eq("workspace_id",state.workspace.id).eq("kind","m0_diagnostic").limit(1)) : [];
    state.artifact=artifacts?.[0] || null;
    $("track").value = state.workspace?.track || "undecided";
    await Promise.all([loadM0(),loadPrograms(),loadTasks()]);
    inform("Ish maydoni tayyor. M0 yoki universitetlar roʻyxatidan boshlang.");
  }
  async function init() {
    if (!db?.auth) return inform("Ulanish mavjud emas. Sahifani yangilang.",true);
    $("loginLink").addEventListener("click",authLink);
    try {
      const {data,error}=await db.auth.getUser();
      if(error && !/Auth session missing/i.test(error.message)) console.warn("Auth unavailable");
      state.user = data?.user||null;
      $("loginGate").classList.toggle("hidden",!!state.user);
      $("workspace").classList.toggle("hidden",!state.user);
      if (!state.user) {authLink();return inform("Rejani saqlash uchun akkauntga kiring.");}
      await hydrate();
    } catch(e) { inform("Ish maydonini yuklashda xatolik: "+e.message,true); }
  }
  $("m0Form").addEventListener("focusin",()=> {
    if(!state.m0Started) {state.m0Started=true; void emit("m0_started","m0_first_input");}
  });
  $("m0Form").addEventListener("submit",async e=> {
    e.preventDefault();
    try {
      const ws=await ensureWorkspace(); const values={};
      for(const name of names) values[name]=$("m0_"+name).value.trim();
      values.track=$("track").value;
      result(await db.from("application_workspaces").update({
        track:values.track,goal:values.goal || null
      }).eq("id",ws.id));
      const row={workspace_id:ws.id,kind:"m0_diagnostic",title:"M0 — boshlangʻich qaror",content:values};
      if(state.artifact) {
        state.artifact=result(await db.from("application_artifacts")
          .update({...row,version:state.artifact.version+1})
          .eq("id",state.artifact.id).eq("workspace_id",ws.id).select().single());
      } else {
        state.artifact=result(await db.from("application_artifacts").insert(row).select().single());
      }
      await emit("m0_completed","m0_saved");
      inform("M0 natijasi saqlandi.");
    } catch(e) {inform(e.message,true);}
  });
  $("programForm").addEventListener("submit",async e=> {
    e.preventDefault();
    try {
      const ws=await ensureWorkspace();
      const raw=$("deadline").value.trim(); let iso=null;
      if(raw) {
        if(!/^(?:\d{4}-\d{2}-\d{2})T\d{2}:\d{2}(?::\d{2})?(?:Z|[+-]\d{2}:\d{2})$/.test(raw)
           || !Number.isFinite(Date.parse(raw))) throw new Error("Deadline uchun ISO sana va timezone offset kerak.");
        iso=new Date(raw).toISOString();
      }
      result(await db.from("application_programs").insert({
        workspace_id:ws.id,institution:$("institution").value.trim(),program_name:$("programName").value.trim(),
        country:$("country").value.trim()||null,
        official_url:$("officialUrl").value.trim()||null,
        admission_deadline_at:iso, deadline_status:"unverified"
      }));
      $("programForm").reset();await loadPrograms();
      inform("Dastur qoʻshildi. Deadline hali verified emas.");
    } catch(e) {inform(e.message,true);}
  });
  $("taskForm").addEventListener("submit",async e=> {
    e.preventDefault();
    try {
      const ws=await ensureWorkspace();
      const raw=$("taskDue").value;
      result(await db.from("application_tasks").insert({
        workspace_id:ws.id,title:$("taskTitle").value.trim(),category:"general",
        due_at:raw ? new Date(raw).toISOString() : null,
        source_url:$("taskSource").value.trim()||null
      }));
      $("taskForm").reset();await loadTasks();inform("Vazifa saqlandi.");
    } catch(e) {inform(e.message,true);}
  });
  async function getExport() {
    if(!state.workspace) throw new Error("Avval M0 yoki dastur saqlang.");
    const workspace=state.workspace;
    const [p,t,a]=await Promise.all([
      db.from("application_programs").select("*").eq("workspace_id",workspace.id),
      db.from("application_tasks").select("*").eq("workspace_id",workspace.id),
      db.from("application_artifacts").select("*").eq("workspace_id",workspace.id)]);
    return {exported_at:new Date().toISOString(),workspace,programs:result(p),tasks:result(t),artifacts:result(a)};
  }
  function download(body,name,mime) {
    const href=URL.createObjectURL(new Blob([body],{type:mime}));
    const link=document.createElement("a");link.href=href;link.download=name;
    document.body.append(link);link.click();link.remove();
    setTimeout(()=>URL.revokeObjectURL(href),1500);
  }
  $("exportJson").addEventListener("click",async()=>{
    try {download(JSON.stringify(await getExport(),null,2),"kompas-master-reja.json","application/json");
    inform("JSON export tayyor.");}catch(e){inform(e.message,true);}
  });
  const csvCell=(value)=> {
    let str=String(value??"");
    if(/^\s*[=+\-@]/.test(str))str="'"+str;
    return '"'+str.replaceAll('"','""')+'"';
  };
  $("exportCsv").addEventListener("click",async()=>{
    try {
      const x=await getExport();
      const rows=[["TYPE","TITLE","INSTITUTION","DEADLINE_UTC","STATUS","OFFICIAL_URL"],
        ...x.programs.map(p=>["program",p.program_name,p.institution,p.admission_deadline_at,p.deadline_status,p.official_url]),
        ...x.tasks.map(t=>["task",t.title,"",t.due_at,t.status,t.source_url])];
      download("\uFEFF"+rows.map(row=>row.map(csvCell).join(",")).join("\r\n"),"kompas-master-reja.csv","text/csv;charset=utf-8");
      inform("CSV export tayyor.");
    }catch(e){inform(e.message,true);}
  });
  document.addEventListener("DOMContentLoaded",init);
})();
