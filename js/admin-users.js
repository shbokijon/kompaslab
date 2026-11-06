/* Kompas Lab — Admin: "Foydalanuvchilar" (2026-11-06)
 * Eski "Talabalar" va "Roʻyxatdan oʻtganlar" bir xil profiles jadvalini ikki marta koʻrsatardi.
 * Endi bitta jadval: bir odam bir qator, holat va jarayon haqiqiy maʼlumotdan hisoblanadi:
 *   enrollments (obuna), kompas_user_state (M0 XP), kompas_m0_events (oxirgi faoliyat),
 *   kompas_access_grants (qoʻlda ruxsat), kompas_account_state (cheklash).
 * Bazaga yozmaydi. Chegaralar (issiq lid: M0 ≥ 60%, "faol emas": 3 kun) taxminiy, tuzatish mumkin: CFG.
 * admin.html dagi eski loadRegs/renderRegs/regsFiltered/exportRegsCSV shu yerda almashtiriladi;
 * js/admin-extensions.js renderRegs ni oʻrab "Sozlash" ustunini qoʻshadi (jadval id: tbRegs).
 */
(function () {
  'use strict';
  var CFG = { hotPct: 60, idleDays: 3, soonDays: 7 };
  var M0N = { master: 'Master', bachelor: 'Bachelor', phd: 'PhD', gks: 'GKS', usa: 'USA', daad: 'DAAD', tt: 'Tadbirkor Talaba', musofir: 'Musofir' };
  var SUS = /@(?:[\w-]+\.)*(?:oastify\.com|burpcollaborator\.net|mailinator\.com|guerrillamail\.[a-z]+|10minutemail\.[a-z]+|yopmail\.com|tempmail\.[a-z]+|trashmail\.[a-z]+|sharklasers\.com|example\.(?:com|org))$/i;
  var FILTERS = [
    ['all', 'Hammasi'], ['subs', 'Obunachilar'], ['free', 'Bepul (M0)'], ['hot', '🔥 Issiq lidlar'],
    ['idle', 'Boshlamaganlar'], ['soon', 'Tugayotgan'], ['expired', 'Muddati tugagan'], ['sus', 'Shubhali']
  ];
  var DAY = 86400000;
  var _flt = 'all';
  var $ = function (id) { return document.getElementById(id); };
  var esc = function (s) { return typeof escHtml === 'function' ? escHtml(s == null ? '' : String(s)) : String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  function ddmm(iso) { var d = new Date(iso); return isNaN(d) ? '' : ('0' + d.getDate()).slice(-2) + '.' + ('0' + (d.getMonth() + 1)).slice(-2) + '.' + d.getFullYear(); }
  function ok(r) { return r && !r.error ? (r.data || []) : []; }

  function build(p, st, evLast, grants, acct, signins) {
    var now = Date.now(), enr = p.enrollments || [];
    var live = [], expired = [], pending = [], frozen = [];
    enr.forEach(function (e) {
      var paid = e.payment_status === 'paid' || e.payment_status === 'partial' || e.payment_status === 'confirmed';
      var exp = e.expires_at ? new Date(e.expires_at).getTime() : null;
      if (paid && e.frozen_at) frozen.push(e);
      else if (paid && (exp == null || exp > now)) live.push(e);
      else if (paid) expired.push(e);
      else if (e.payment_status === 'pending') pending.push(e);
    });
    var m0 = [], lastState = 0;
    (st[p.id] || []).forEach(function (r) {
      var m = /^kompas_([a-z]+)_m0_v1$/.exec(r.key);
      var t = Date.parse(r.updated_at) || 0; if (t > lastState) lastState = t;
      if (m) m0.push({ lab: M0N[m[1]] || m[1], pct: Math.min(100, Math.round((+((r.value || {}).xp) || 0) / 250 * 100)) });
    });
    m0.sort(function (a, b) { return b.pct - a.pct; });
    var best = m0[0] || { lab: null, pct: 0 };
    var nextExp = live.map(function (e) { return e.expires_at ? new Date(e.expires_at).getTime() : null; }).filter(Boolean).sort()[0] || null;
    var g = (grants[p.id] || 0), a = acct[p.id] || 'active';
    var status, cls;
    if (a !== 'active') { status = 'Cheklangan'; cls = 'trd'; }
    else if (live.length) { status = 'Obunachi' + (nextExp ? ' · ' + ddmm(nextExp) + ' gacha' : ''); cls = 'tgr'; }
    else if (frozen.length) { status = 'Muzlatilgan'; cls = 'tgd'; }
    else if (expired.length) { status = 'Muddati tugagan'; cls = 'tgd'; }
    else if (pending.length) { status = 'Toʻlov kutilmoqda'; cls = 'tgd'; }
    else if (g) { status = 'Qoʻlda ruxsat'; cls = 'ta'; }
    else { status = 'Roʻyxatdan oʻtgan'; cls = 'tg'; }
    var last = Math.max(evLast[p.id] || 0, lastState, signins[p.id] || 0);
    p._x = {
      live: live, expired: expired, pending: pending, status: status, cls: cls, pct: best.pct, m0lab: best.lab, nextExp: nextExp, grants: g,
      tip: m0.map(function (x) { return x.lab + ' M0: ' + x.pct + '%'; }).join('\n'),
      last: last, sus: SUS.test(p.email || ''),
      isSub: live.length > 0
    };
    return p;
  }

  function match(r, f) {
    var x = r._x, age = (Date.now() - new Date(r.created_at).getTime()) / DAY;
    if (f === 'subs') return x.isSub;
    if (f === 'free') return !x.isSub;
    if (f === 'hot') return !x.isSub && x.pct >= CFG.hotPct;
    if (f === 'idle') return !x.isSub && x.pct === 0 && !x.last && age >= CFG.idleDays;
    if (f === 'soon') return x.isSub && x.nextExp && x.nextExp - Date.now() <= CFG.soonDays * DAY;
    if (f === 'expired') return !x.isSub && x.expired.length > 0;
    if (f === 'sus') return x.sus;
    return true;
  }

  window.loadRegs = async function () {
    var tb = $('tbRegs');
    tb.innerHTML = '<tr><td colspan="10" style="text-align:center;color:var(--muted);padding:20px">Yuklanmoqda...</td></tr>';
    var res = await Promise.all([
      supabase.from('profiles').select('id, first_name, last_name, email, phone, education, goal, stage, created_at, enrollments(id, payment_status, plan, expires_at, frozen_at, course:courses(slug, title))').neq('role', 'admin').order('created_at', { ascending: false }).limit(2000),
      supabase.from('kompas_user_state').select('user_id, key, value, updated_at').limit(10000),
      supabase.from('kompas_m0_events').select('user_id, created_at').order('created_at', { ascending: false }).limit(5000),
      supabase.from('kompas_access_grants').select('user_id, expires_at').is('revoked_at', null),
      supabase.from('kompas_account_state').select('user_id, status'),
      // Oxirgi kirish: migratsiya 20261106_admin_last_sign_in.sql qoʻllangach ishlaydi; boʻlmasa jim oʻtkaziladi
      supabase.rpc('kompas_admin_last_sign_ins')
    ]);
    if (res[0].error) { tb.innerHTML = '<tr><td colspan="10" style="color:var(--red);padding:20px">Xatolik: ' + esc(res[0].error.message) + '</td></tr>'; return; }
    var st = {}, evLast = {}, grants = {}, acct = {}, signins = {}, now = Date.now();
    ok(res[5]).forEach(function (r) { var t = Date.parse(r.last_sign_in_at) || 0; if (t) signins[r.user_id] = t; });
    ok(res[1]).forEach(function (r) { (st[r.user_id] = st[r.user_id] || []).push(r); });
    ok(res[2]).forEach(function (r) { var t = Date.parse(r.created_at) || 0; if (t > (evLast[r.user_id] || 0)) evLast[r.user_id] = t; });
    ok(res[3]).forEach(function (r) { if (!r.expires_at || new Date(r.expires_at).getTime() > now) grants[r.user_id] = (grants[r.user_id] || 0) + 1; });
    ok(res[4]).forEach(function (r) { acct[r.user_id] = r.status; });
    window._regs = (res[0].data || []).map(function (p) { return build(p, st, evLast, grants, acct, signins); });
    var pill = $('pRegs'); if (pill) pill.textContent = window._regs.length;
    window.renderRegs();
  };

  window.regsFiltered = function () {
    var q = (($('regQ') || {}).value || '').trim().toLowerCase();
    var days = parseInt((($('regPeriod') || {}).value) || '0', 10), since = days ? Date.now() - days * DAY : 0;
    return (window._regs || []).filter(function (r) {
      if (since && new Date(r.created_at).getTime() < since) return false;
      if (!match(r, _flt)) return false;
      if (!q) return true;
      return [r.first_name, r.last_name, r.email, r.phone].join(' ').toLowerCase().indexOf(q) >= 0;
    });
  };

  window.regCourses = function (r) {
    var x = r._x || {};
    var s = (r.enrollments || []).map(function (e) { return (e.course && (e.course.title || e.course.slug) || '?') + ' (' + e.payment_status + (e.plan ? ', ' + e.plan : '') + ')'; });
    if (!s.length && x.m0lab) s.push(x.m0lab + ' M0 ' + x.pct + '%');
    return s.join(', ');
  };

  function chips() {
    var box = $('regChips'); if (!box) return;
    var all = window._regs || [];
    box.innerHTML = FILTERS.map(function (f) {
      var n = all.filter(function (r) { return match(r, f[0]); }).length;
      if (f[0] === 'sus' && !n && _flt !== 'sus') return '';
      return '<button type="button" class="chip' + (_flt === f[0] ? ' on' : '') + '" data-f="' + f[0] + '">' + f[1] + ' <b>' + n + '</b></button>';
    }).join('');
    box.querySelectorAll('.chip').forEach(function (b) { b.addEventListener('click', function () { _flt = b.getAttribute('data-f'); window.renderRegs(); }); });
  }

  function courseCell(r) {
    var x = r._x, t = x.live.map(function (e) { return '<span class="tag ta" style="margin:1px 3px 1px 0">' + esc((e.course && (e.course.title || e.course.slug)) || '—') + '</span>'; });
    if (!t.length && x.m0lab) t.push('<span class="tag tg" title="Bepul M0 moduli">🧭 ' + esc(x.m0lab) + ' M0</span>');
    return t.join('') || '<span class="tag tg">—</span>';
  }

  window.renderRegs = function () {
    chips();
    var rows = window.regsFiltered(), tb = $('tbRegs'), all = window._regs || [];
    $('regSummary').textContent = rows.length + ' / ' + all.length + ' kishi';
    if (!rows.length) { tb.innerHTML = '<tr><td colspan="10" style="text-align:center;color:var(--muted);padding:20px">Hech kim topilmadi</td></tr>'; if (typeof delRefresh === 'function') delRefresh('tbRegs'); return; }
    tb.innerHTML = rows.map(function (r, i) {
      var x = r._x, name = ((r.first_name || '') + ' ' + (r.last_name || '')).trim() || r.email || '—';
      return '<tr><td><input type="checkbox" class="dsel" value="' + r.id + '" onchange="delRefresh(\'tbRegs\')"></td>' +
        '<td style="color:var(--muted);font-size:11px">' + (i + 1) + '</td>' +
        '<td><button type="button" class="lnk-user" onclick="viewStudent(\'' + r.id + '\',\'' + esc(name).replace(/'/g, '') + '\')" title="Profilni ochish"><span class="snm">' + esc(name) + '</span><span class="sem" translate="no">' + esc(r.email || '') + '</span></button>' + (x.sus ? ' <span class="tag trd" title="Skaner yoki bir martalik email belgisi">shubhali</span>' : '') + '</td>' +
        '<td>' + esc(r.phone || '—') + '</td>' +
        '<td>' + courseCell(r) + '</td>' +
        '<td><div class="mp" title="' + esc(x.tip || 'M0 boshlanmagan') + '"><div class="mpb"><div class="mpf" style="width:' + x.pct + '%"></div></div><span class="mpv">' + x.pct + '%</span></div></td>' +
        '<td><span class="tag ' + x.cls + '">' + esc(x.status) + '</span></td>' +
        '<td style="font-size:12px;color:var(--muted)" title="' + (x.last ? esc(new Date(x.last).toLocaleString('uz-Latn')) : '') + '">' + (x.last ? esc(timeSince(new Date(x.last).toISOString())) : 'hali yoʻq') + '</td>' +
        '<td style="font-size:11px;color:var(--muted);font-family:\'JetBrains Mono\',\'IBM Plex Sans\',monospace">' + esc((r.created_at || '').slice(0, 10)) + '</td></tr>';
    }).join('');
    if (typeof delRefresh === 'function') delRefresh('tbRegs');
  };

  window.exportRegsCSV = function () {
    var rows = window.regsFiltered();
    if (!rows.length) { toast('⚠️ Roʻyxat boʻsh'); return; }
    downloadCSV('foydalanuvchilar-' + new Date().toISOString().slice(0, 10) + '.csv',
      ['Ism', 'Familiya', 'Email', 'Telefon', 'Taʼlim', 'Maqsad', 'Holat', 'Kurslar', 'M0 jarayon %', 'Oxirgi faoliyat', 'Sana'],
      rows.map(function (r) { var x = r._x; return [r.first_name || '', r.last_name || '', r.email || '', r.phone || '', r.education || '', r.goal || '', x.status, window.regCourses(r), x.pct, x.last ? new Date(x.last).toISOString().slice(0, 19).replace('T', ' ') : '', (r.created_at || '').slice(0, 19).replace('T', ' ')]; }));
    toast('✅ CSV yuklab olindi');
  };
})();
