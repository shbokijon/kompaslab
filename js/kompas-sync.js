// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — kompas-sync.js (2026-11-05)
//  1) Modul progressini hisobga bogʻlaydi: kompas_user_state jadvali.
//     Faqat xp, done, seen, open, lv yoziladi. Javob matni (notes, jadvallar)
//     talaba brauzerida qoladi.
//  2) M0 sahifalarida oʻqish voqealarini yozadi: kompas_m0_events
//     (dars ochildi, qism ochildi, dars yakunlandi, faol vaqt, modul yakuni).
//  Kirmagan foydalanuvchi uchun hech narsa yubormaydi. Jadval boʻlmasa yoki
//  tarmoq xatosi boʻlsa, jim toʻxtaydi: sahifa ishlashiga taʼsir qilmaydi.
//  Foydalanish: window.KompasSync.ready (Promise) — serverdan holat olingach.
// ═══════════════════════════════════════════════════════════════
(function () {
  if (window.KompasSync) return;
  var sb = window.supabase;
  var KS = window.KompasSync = { ready: Promise.resolve(false), meta: meta };
  if (!sb || !sb.auth || typeof sb.from !== "function" || !window.localStorage) return;

  var KEY_RE = /^kompas_[a-z]+_m[0-9a-z]{1,6}_v1$/;
  var KEEP = ["xp", "done", "seen", "open", "lv"];
  var META = "kompas_sync_meta_v1";
  var LS = window.localStorage, rawSet = Storage.prototype.setItem;
  var user = null, stateOff = false, eventsOff = false, pending = {}, timer = null, remote = {};

  function parse(s) { try { var o = JSON.parse(s); return o && typeof o === "object" ? o : null; } catch (e) { return null; } }
  function meta() { return parse(LS.getItem(META)) || {}; }
  function touch(k, t) { var m = meta(); m[k] = t || Date.now(); rawSet.call(LS, META, JSON.stringify(m)); }
  function slim(o) { var r = {}; KEEP.forEach(function (k) { if (o && o[k] !== undefined) r[k] = o[k]; }); return r; }
  function union(a, b) { var s = (a || []).slice(); (b || []).forEach(function (x) { if (s.indexOf(x) < 0) s.push(x); }); return s; }

  // Ikki qurilmadagi progressni birlashtirish: hech qachon kamaymaydi
  function merge(local, remote, localNewer) {
    var out = local ? JSON.parse(JSON.stringify(local)) : {};
    if (!remote) return out;
    out.xp = Math.max(+out.xp || 0, +remote.xp || 0);
    out.done = out.done || {};
    Object.keys(remote.done || {}).forEach(function (k) { if (remote.done[k]) out.done[k] = true; });
    out.seen = out.seen || {};
    Object.keys(remote.seen || {}).forEach(function (k) { out.seen[k] = union(out.seen[k], remote.seen[k]); });
    ["open", "lv"].forEach(function (k) { if (remote[k] !== undefined && (!localNewer || out[k] === undefined)) out[k] = remote[k]; });
    return out;
  }

  function push(k) { pending[k] = 1; clearTimeout(timer); timer = setTimeout(flushState, 2500); }
  function flushState() {
    if (!user || stateOff) return;
    var rows = Object.keys(pending).map(function (k) {
      var o = parse(LS.getItem(k)); return o ? { key: k, value: slim(merge(o, remote[k], true)), updated_at: new Date(meta()[k] || Date.now()).toISOString() } : null;
    }).filter(Boolean);
    pending = {};
    if (!rows.length) return;
    sb.from("kompas_user_state").upsert(rows, { onConflict: "user_id,key" }).then(function (r) {
      if (r && r.error && /does not exist|PGRST20|42P01|permission/i.test(r.error.message + " " + r.error.code)) stateOff = true;
    }, function () {});
  }

  // ── M0 voqealari ──────────────────────────────────────────
  var M = window.KMOD, q = [], lab = null, mod = null, lesson = null;
  if (M && /-m0$/.test(M.base)) {
    lab = M.base.replace(/-m0$/, "");
    mod = "m0";
    var v = document.body && document.body.getAttribute("data-kview");
    lesson = v === "lesson" ? document.body.getAttribute("data-klesson") : v === "yakun" ? "yakun" : "hub";
  }
  function ev(event, extra) {
    if (!lab || eventsOff) return;
    var e = { lab: lab, module: mod, lesson: lesson, section: null, event: event, active_sec: 0 };
    for (var k in extra) e[k] = extra[k];
    q.push(e);
  }
  function flushEvents(beacon) {
    if (!user || eventsOff || !q.length) return;
    var rows = q.splice(0, 50);
    if (beacon && typeof SUPABASE_URL !== "undefined" && user.token) {
      try {
        fetch(SUPABASE_URL + "/rest/v1/kompas_m0_events", {
          method: "POST", keepalive: true,
          headers: { "Content-Type": "application/json", apikey: SUPABASE_ANON_KEY, Authorization: "Bearer " + user.token, Prefer: "return=minimal" },
          body: JSON.stringify(rows)
        }).catch(function () {});
      } catch (e) {}
      return;
    }
    sb.from("kompas_m0_events").insert(rows).then(function (r) {
      if (r && r.error && /does not exist|PGRST20|42P01|permission/i.test(r.error.message + " " + r.error.code)) eventsOff = true;
    }, function () {});
  }

  // Modul holati oʻzgarganda nima yangi boʻlganini aniqlash
  var prev = M ? slim(parse(LS.getItem(M.key)) || {}) : null;
  function diff(next) {
    if (!prev) return;
    var ns = next.seen || {}, ps = prev.seen || {};
    Object.keys(ns).forEach(function (id) {
      (ns[id] || []).forEach(function (i) {
        if ((ps[id] || []).indexOf(i) < 0 && typeof i === "number") ev("section", { lesson: /^l\d{1,2}$/.test(id) ? id : lesson, section: i });
      });
    });
    Object.keys(next.done || {}).forEach(function (id) {
      if (next.done[id] && !(prev.done || {})[id] && /^l\d{1,2}$/.test(id)) ev("done", { lesson: id });
    });
    if ((+next.xp || 0) >= 250 && (+prev.xp || 0) < 250) ev("finish", { lesson: "yakun" });
    prev = next;
  }

  // localStorage yozuvlarini kuzatish (modul kodi oʻzgarmaydi)
  Storage.prototype.setItem = function (k, val) {
    rawSet.apply(this, arguments);
    if (this !== LS || !KEY_RE.test(k)) return;
    touch(k);
    if (M && k === M.key) diff(slim(parse(val) || {}));
    push(k);
  };

  // Faol vaqt: sahifa koʻrinib turgan va oxirgi 60 soniyada harakat boʻlgan soniyalar
  var active = 0, lastAct = Date.now();
  if (lab) {
    ["pointerdown", "keydown", "scroll", "touchstart"].forEach(function (t) {
      window.addEventListener(t, function () { lastAct = Date.now(); }, { passive: true, capture: true });
    });
    setInterval(function () {
      if (document.visibilityState === "visible" && Date.now() - lastAct < 60000) active++;
      if (active >= 60) { ev("active", { active_sec: active }); active = 0; }
    }, 1000);
  }
  setInterval(function () { flushEvents(false); }, 15000);
  document.addEventListener("visibilitychange", function () {
    if (document.visibilityState !== "hidden") return;
    if (active > 0) { ev("active", { active_sec: Math.min(active, 900) }); active = 0; }
    flushEvents(true);
    flushState();
  });

  // ── Kirish, serverdan holatni olish ───────────────────────
  KS.ready = sb.auth.getSession().then(function (r) {
    var s = r && r.data && r.data.session;
    if (!s || !s.user) return false;
    user = { id: s.user.id, token: s.access_token };
    sb.auth.onAuthStateChange(function (e, ns) { if (ns && ns.access_token) user.token = ns.access_token; if (e === "SIGNED_OUT") user = null; });
    if (lab) { ev("view"); setTimeout(function () { flushEvents(false); }, 1500); }
    return sb.from("kompas_user_state").select("key,value,updated_at").then(function (res) {
      if (res.error) { if (/does not exist|PGRST20|42P01/i.test(res.error.message + " " + res.error.code)) stateOff = true; return false; }
      var m = meta(), seenKeys = {}, changed = false, changedM = false;
      (res.data || []).forEach(function (row) {
        if (!KEY_RE.test(row.key)) return;
        seenKeys[row.key] = 1; remote[row.key] = row.value;
        var loc = parse(LS.getItem(row.key)), rt = Date.parse(row.updated_at) || 0;
        var merged = merge(loc, row.value, (m[row.key] || 0) > rt);
        if (JSON.stringify(slim(merged)) !== JSON.stringify(slim(loc || {}))) {
          rawSet.call(LS, row.key, JSON.stringify(merged)); touch(row.key, Math.max(rt, m[row.key] || 0)); changed = true; if (M && row.key === M.key) changedM = true;
        }
        if (JSON.stringify(slim(merged)) !== JSON.stringify(row.value)) push(row.key);
      });
      for (var i = 0; i < LS.length; i++) { var k = LS.key(i); if (KEY_RE.test(k) && !seenKeys[k]) push(k); }
      if (M && changed) {
        prev = slim(parse(LS.getItem(M.key)) || {});
        // Boshqa qurilmadagi progress shu modulga qoʻshildi: sahifani bir marta yangilab, toʻgʻri holatni koʻrsatamiz
        var rk = "kompas_sync_reload_" + M.key;
        try { if (changedM && !sessionStorage.getItem(rk)) { sessionStorage.setItem(rk, "1"); location.reload(); } } catch (e) {}
      }
      return changed;
    });
  }).catch(function () { return false; });
})();
