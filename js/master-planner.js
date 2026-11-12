/* Kompas Lab — Bepul reja (?lab=master|bachelor|phd|gks|usa|daad).
   Hamma maʼlumot faqat shu brauzerda (localStorage). Serverga hech narsa yuborilmaydi.
   Lab sozlamalari sahifadagi #pl-cfg da (tools/site/planner.py yigʻadi). */
(function () {
  "use strict";
  var LABS = JSON.parse(document.getElementById("pl-cfg").textContent);
  var FUND = { unknown: "hali nomaʼlum", possible: "tekshirish kerak", "self-funded": "oʻz hisobimdan" };
  var FORMAT = "kompas-planner-v2";
  var $ = function (id) { return document.getElementById(id); };

  var labKey = (new URLSearchParams(location.search).get("lab") || "").toLowerCase();
  if (!LABS[labKey]) {
    try { labKey = localStorage.getItem("kompas_planner_lab") || ""; } catch (e) { labKey = ""; }
    if (!LABS[labKey]) labKey = "master";
  }
  try { localStorage.setItem("kompas_planner_lab", labKey); } catch (e) { /* xotira yopiq */ }
  var LAB = LABS[labKey];
  var DEFAULT = { goal: "", degree: LAB.opts.length ? LAB.opts[0][0] : "", intake: "2027", countries: "", tasks: {}, programmes: [] };
  var state;

  function load() {
    try {
      var d = JSON.parse(localStorage.getItem(LAB.key) || "null");
      return d && typeof d === "object" ? Object.assign({}, DEFAULT, d) : Object.assign({}, DEFAULT);
    } catch (e) { return Object.assign({}, DEFAULT); }
  }
  function save() {
    try { localStorage.setItem(LAB.key, JSON.stringify(state)); return true; }
    catch (e) { $("dataStatus").textContent = "Brauzer xotirasiga yozib boʻlmadi. Faylga saqlang."; return false; }
  }
  function say(id, t) { $(id).textContent = t; }
  function el(tag, text) { var e = document.createElement(tag); if (text != null) e.textContent = text; return e; }

  function visibleTasks() {
    // GKS: umumiy modullar + tanlangan trek (M3-U, M3-M, M3-D …)
    return LAB.tasks.filter(function (t) {
      var m = /-([UMD])$/.exec(t.id);
      return !m || m[1] === state.degree;
    });
  }

  function header() {
    document.querySelectorAll(".pl-labs a").forEach(function (a) {
      if (a.getAttribute("data-lab") === labKey) a.setAttribute("aria-current", "page");
      else a.removeAttribute("aria-current");
    });
    document.title = "Bepul reja: " + LAB.name + " · Kompas Lab";
    $("goalQ").textContent = LAB.goal;
    $("progLabel").textContent = LAB.prog;
    var sel = $("degree");
    sel.textContent = "";
    LAB.opts.forEach(function (o) { var op = el("option", o[1]); op.value = o[0]; sel.appendChild(op); });
    $("degreeBox").hidden = !LAB.opts.length;
    var ps = $("plSale");
    if (ps) {
      ps.textContent = "";
      if (LAB.sale) {
        ps.appendChild(document.createTextNode("M0 bepul. Qolgan modullar " + LAB.name + " obunasida ochiladi: oylik tarif navbatdagi bosqichni, 6 oylik hammasini. "));
        var a = el("a", "Narx va obuna"); a.href = LAB.slug + "-narxlar.html"; ps.appendChild(a);
      }
      ps.hidden = !LAB.sale;
    }
  }

  function fields() {
    ["goal", "degree", "intake", "countries"].forEach(function (k) { if ($(k)) $(k).value = state[k] || DEFAULT[k]; });
  }

  function tasks() {
    var root = $("taskList"), list = visibleTasks(), done = 0, next = null;
    root.textContent = "";
    list.forEach(function (t) {
      var li = el("li"), cb = el("input"), lab = el("label"), id = "t_" + t.id;
      cb.type = "checkbox"; cb.id = id; cb.checked = !!state.tasks[t.id];
      if (cb.checked) done++; else if (!next) next = t;
      cb.addEventListener("change", function () { state.tasks[t.id] = cb.checked; save(); tasks(); });
      lab.htmlFor = id; lab.textContent = t.id + ": " + t.t;
      var a = el("a", "Modul"); a.href = t.h;
      li.appendChild(cb); li.appendChild(lab); li.appendChild(a);
      root.appendChild(li);
    });
    $("bar").style.width = (list.length ? done / list.length * 100 : 0) + "%";
    say("progressText", done + " / " + list.length + " bosqich belgilangan");
    var nx = $("next");
    nx.textContent = "";
    if (next) {
      nx.appendChild(el("b", "Keyingi qadam: "));
      nx.appendChild(document.createTextNode(next.id + ", " + next.t + ". "));
      var a = el("a", next.id === "M0" ? "Bepul M0 ni ochish" : "Modul sahifasi"); a.href = next.h;
      nx.appendChild(a);
      // Sotuvdagi Lab: M0 dan keyingi qadam obuna bilan ochiladi (2026-11-12)
      if (LAB.sale && next.id !== "M0") {
        nx.appendChild(document.createTextNode(" · "));
        var pr = el("a", "Narx va obuna"); pr.href = LAB.slug + "-narxlar.html";
        nx.appendChild(pr);
      }
    } else {
      nx.appendChild(el("b", "Hamma bosqich belgilangan. "));
      nx.appendChild(document.createTextNode("Saralangan roʻyxatdagi har muddatni rasmiy saytda yana bir bor tekshiring."));
    }
    nx.hidden = false;
  }

  function programmes() {
    var root = $("programmesList");
    root.textContent = "";
    if (!state.programmes.length) {
      var p = el("p", "Hozircha roʻyxat boʻsh. Universitet dasturining rasmiy havolasidan boshlang."); p.className = "pl-note";
      root.appendChild(p);
      return;
    }
    state.programmes.forEach(function (p, i) {
      var b = el("div"); b.className = "pl-prog";
      var t = el("strong", p.university + ": " + p.programme); t.setAttribute("data-alifbo", "off");
      b.appendChild(t);
      b.appendChild(el("small", "Siz qoʻshgan, Kompas tekshirmagan · Muddat: " + (p.deadline || "nomaʼlum") + " · Moliyalashtirish: " + (FUND[p.funding] || p.funding)));
      var a = el("a", "Rasmiy sahifani ochish"); a.href = p.officialUrl; a.target = "_blank"; a.rel = "noopener noreferrer";
      b.appendChild(a); b.appendChild(document.createTextNode(" · "));
      var x = el("button", "Oʻchirish"); x.type = "button"; x.className = "btn btn-g btn-sm";
      x.addEventListener("click", function () { state.programmes.splice(i, 1); save(); programmes(); });
      b.appendChild(x);
      root.appendChild(b);
    });
  }

  function clean(d) {
    var s = Object.assign({}, DEFAULT, d);
    s.tasks = s.tasks && typeof s.tasks === "object" && s.tasks !== DEFAULT.tasks ? Object.assign({}, s.tasks) : {};
    s.programmes = Array.isArray(s.programmes) && s.programmes !== DEFAULT.programmes ? s.programmes.slice() : [];
    s.programmes = s.programmes.filter(function (p) {
      try { return p && p.university && p.programme && new URL(p.officialUrl).protocol === "https:"; } catch (e) { return false; }
    }).slice(0, 40);
    return s;
  }

  function init() {
    state = clean(load());
    header(); fields(); tasks(); programmes();

    $("saveProfile").addEventListener("click", function () {
      ["goal", "degree", "intake", "countries"].forEach(function (k) { state[k] = $(k).value.trim(); });
      say("profileStatus", save() ? "Saqlandi, faqat shu qurilmada." : "Faylga saqlang.");
      tasks();
    });
    $("degree").addEventListener("change", function () { state.degree = $("degree").value; save(); tasks(); });

    $("addProgramme").addEventListener("submit", function (e) {
      e.preventDefault();
      var u;
      try { u = new URL($("officialUrl").value.trim()); } catch (err) { say("addStatus", "Havola notoʻgʻri."); return; }
      if (u.protocol !== "https:" || u.hostname.indexOf(".") < 0 || u.username || u.password) { say("addStatus", "Faqat ochiq HTTPS havolani qoʻshing."); return; }
      var d = { university: $("university").value.trim(), programme: $("programme").value.trim(), officialUrl: u.href, deadline: $("deadline").value, funding: $("funding").value, checked: false };
      if (!d.university || !d.programme || state.programmes.length >= 40) { say("addStatus", "Nomlar majburiy. Roʻyxatga koʻpi bilan 40 ta dastur qoʻshiladi."); return; }
      state.programmes.push(d); save(); programmes(); $("addProgramme").reset();
      say("addStatus", "Qoʻshildi. Talab va muddatlarni rasmiy sahifada oʻzingiz tekshiring.");
    });

    $("export").addEventListener("click", function () {
      var blob = new Blob([JSON.stringify({ format: FORMAT, lab: labKey, exported_at: new Date().toISOString(), data: state }, null, 2)], { type: "application/json" });
      var a = document.createElement("a"), url = URL.createObjectURL(blob);
      a.href = url; a.download = "kompas-reja-" + labKey + ".json";
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
      say("dataStatus", "Fayl tayyor. Uni boshqa qurilmada \"Fayldan yuklash\" bilan oching.");
    });

    $("importFile").addEventListener("change", function () {
      var f = this.files && this.files[0];
      this.value = "";
      if (!f) return;
      if (f.size > 500000) { say("dataStatus", "Fayl juda katta."); return; }
      f.text().then(function (txt) {
        var j = JSON.parse(txt);
        var ok = j && j.data && typeof j.data === "object" && (j.format === FORMAT || j.format === "kompas-master-planner-v1");
        if (!ok) throw new Error("format");
        var from = j.format === FORMAT ? j.lab : "master";
        if (from !== labKey) { say("dataStatus", "Bu fayl " + ((LABS[from] && LABS[from].name) || from) + " rejasi. Oʻsha Labni tanlab, qayta yuklang."); return; }
        if (!confirm("Shu qurilmadagi " + LAB.name + " rejasi fayldagi nusxa bilan almashtirilsinmi?")) return;
        state = clean(j.data); save(); fields(); tasks(); programmes();
        say("dataStatus", "Reja fayldan yuklandi.");
      }).catch(function () { say("dataStatus", "Fayl Kompas rejasi emas yoki buzilgan."); });
    });

    $("clear").addEventListener("click", function () {
      if (!confirm("Shu qurilmadagi " + LAB.name + " rejasini butunlay tozalaysizmi?")) return;
      try { localStorage.removeItem(LAB.key); } catch (e) { /* yopiq */ }
      state = clean({}); fields(); tasks(); programmes();
      say("dataStatus", "Reja tozalandi.");
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
