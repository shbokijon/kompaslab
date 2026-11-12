/* Kompas Lab — Admin: Analitika → "M0 voronkasi va talabalar" (2026-11-12)
 * Maʼlumot: kompas_admin_m0_overview() (bitta RPC, bazaga yozmaydi).
 * Tartib:
 *   1) Voronka: odam boʻyicha (bir odam bir marta), admin hisoblari kirmaydi.
 *      Har qadamda: soni, roʻyxatdan oʻtganlarga nisbatan %, oldingi qadamdan oʻtish %.
 *   2) Lablar: boshlagan / ≥1 dars / yakunlagan / vaqt + darslar boʻyicha tushish.
 *   3) Talabalar: bir odam bir qator (bir necha Lab boʻlsa bitta qatorda), holat filtrlari, qidiruv.
 * Holat: Email tasdiqlanmagan → M0 ochilmagan → Oʻqiyapti / Toʻxtagan (CFG.idleDays) → Yakunlagan.
 */
(function () {
  'use strict';
  var CFG = { idleDays: 3 };
  var DAY = 86400000;
  var LESSONS = { 'master-lab': 5, 'bachelor-lab': 5, 'phd-lab': 6, 'gks-lab': 5, 'usa-lab': 6, 'tadbirkor-talaba': 5, 'musofir-lab': 6 };
  var LAB = { 'master-lab': 'Master', 'bachelor-lab': 'Bachelor', 'phd-lab': 'PhD', 'gks-lab': 'GKS', 'usa-lab': 'USA', 'daad-lab': 'DAAD',
    'mext-lab': 'MEXT', 'tadbirkor-talaba': 'Tadbirkor Talaba', 'musofir-lab': 'Musofir' };
  var STAGE = { school: 'Maktab', college: 'Litsey/kollej', bachelor: 'Bakalavr', bachelor_done: 'Bakalavr bitirgan', master: 'Magistrant',
    master_done: 'Magistr bitirgan', phd: 'Doktorant', work: 'Ishlaydi' };
  var SECT = ['Diqqat 🔥', 'Asosiy qism', 'Xulosa', 'Topshiriq'];
  var ST = {
    finished: ['Yakunlagan', 'tgr'], active: ['Oʻqiyapti', 'ta'], stuck: ['Toʻxtagan', 'trd'],
    noop: ['M0 ochilmagan', 'tgd'], unconfirmed: ['Email tasdiqlanmagan', 'tg']
  };
  var FILTERS = [['all', 'Hammasi'], ['stuck', 'Toʻxtagan'], ['active', 'Oʻqiyapti'], ['finished', 'Yakunlagan'], ['noop', 'M0 ochilmagan'], ['unconfirmed', 'Email tasdiqlanmagan']];
  var state = { people: [], flt: 'all', q: '' };

  var $ = function (id) { return document.getElementById(id); };
  var esc = function (s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  var labName = function (s) { return LAB[s] || s; };
  var pct = function (a, b) { return b ? Math.round(a / b * 100) : 0; };
  function ddmm(t) { var d = new Date(t); return ('0' + d.getDate()).slice(-2) + '.' + ('0' + (d.getMonth() + 1)).slice(-2) + '.' + d.getFullYear(); }
  function ago(t) {
    if (!t) return '—';
    var d = Math.floor((Date.now() - t) / DAY);
    var rel = d <= 0 ? 'bugun' : d === 1 ? 'kecha' : d + ' kun oldin';
    return '<span title="' + ddmm(t) + '">' + rel + '</span>';
  }

  // Bir odam — bir yozuv (RPC har Lab uchun alohida qator beradi)
  function group(rows) {
    var map = {}, list = [];
    rows.forEach(function (u) {
      var k = (u.email || '') + '|' + (u.signed_up || '') + '|' + (u.name || '');
      var p = map[k];
      if (!p) {
        p = map[k] = { name: u.name, email: u.email, confirmed: !!u.confirmed, signed: Date.parse(u.signed_up) || 0,
          stage: u.stage, detail: u.detail, works: u.works, labs: [], minutes: 0, last: 0 };
        list.push(p);
      }
      if (u.lab) {
        var t = Date.parse(u.last_seen) || 0;
        p.labs.push({ lab: u.lab, done: u.done || 0, total: LESSONS[u.lab] || null, finished: !!u.finished,
          lesson: u.last_lesson, section: u.last_section, minutes: u.minutes || 0, last: t });
        p.minutes += u.minutes || 0;
        if (t > p.last) p.last = t;
      }
    });
    list.forEach(function (p) {
      p.labs.sort(function (a, b) { return b.last - a.last; });
      var anyFin = p.labs.some(function (l) { return l.finished; });
      var open = p.labs.filter(function (l) { return !l.finished; });
      var fresh = open.length && Date.now() - open[0].last <= CFG.idleDays * DAY;
      // Bitta Labni yakunlab, boshqasida toʻxtagan odam "Yakunlagan" boʻlib qoladi (M0 maqsadiga yetgan)
      if (!p.labs.length) p.st = p.confirmed ? 'noop' : 'unconfirmed';
      else if (fresh) p.st = 'active';
      else if (anyFin) p.st = 'finished';
      else p.st = 'stuck';
      p.started = p.labs.length > 0;
      p.lesson1 = p.labs.some(function (l) { return l.done > 0; });
      p.fin = anyFin;
      p.key = ((p.name || '') + ' ' + (p.email || '') + ' ' + p.labs.map(function (l) { return labName(l.lab); }).join(' ')).toLowerCase();
    });
    return list;
  }

  function renderFunnel(people) {
    var n = function (f) { return people.filter(f).length; };
    var steps = [
      ['Roʻyxatdan oʻtgan', people.length],
      ['Emailni tasdiqlagan', n(function (p) { return p.confirmed; })],
      ['M0 ni ochgan', n(function (p) { return p.started; })],
      ['Kamida 1 dars tugatgan', n(function (p) { return p.lesson1; })],
      ['M0 ni yakunlagan', n(function (p) { return p.fin; })]
    ];
    var top = steps[0][1] || 1;
    // Eng katta yoʻqotish (oldingi qadamdan ketganlar soni boʻyicha)
    var worst = -1, worstLoss = 0;
    for (var i = 1; i < steps.length; i++) { var loss = steps[i - 1][1] - steps[i][1]; if (loss > worstLoss) { worstLoss = loss; worst = i; } }
    var html = steps.map(function (s, i) {
      var conv = i ? pct(s[1], steps[i - 1][1]) : null;
      return '<div class="m0f-row' + (i === worst ? ' m0f-worst' : '') + '">' +
        '<div class="m0f-lbl">' + (i + 1) + '. ' + s[0] + '</div>' +
        '<div class="m0f-bar"><span style="width:' + Math.max(s[1] ? 2 : 0, pct(s[1], top)) + '%"></span></div>' +
        '<div class="m0f-n"><b>' + s[1] + '</b> <small>' + pct(s[1], top) + '%</small></div>' +
        '<div class="m0f-c">' + (i ? '← ' + conv + '%' + (i === worst ? ' · eng katta yoʻqotish (' + worstLoss + ')' : '') : '') + '</div></div>';
    }).join('');
    var ob = n(function (p) { return !!p.stage; });
    $('m0Funnel').innerHTML = html + '<div class="m0-note">Kabinetdagi savolga javob berganlar: <b>' + ob + '</b> (' + pct(ob, top) + '%). Bu qadam M0 dan oldin shart emas, shuning uchun zanjirga kirmaydi.<br>' +
      '% — roʻyxatdan oʻtganlarga nisbatan; ← — oldingi qadamdan oʻtganlar. Bir odam bir marta sanaladi, admin hisoblari kirmaydi.</div>';
  }

  function renderLabs(people, lessons) {
    var by = {};
    people.forEach(function (p) {
      p.labs.forEach(function (l) {
        var x = by[l.lab] = by[l.lab] || { lab: l.lab, users: 0, l1: 0, fin: 0, min: 0, stuck: 0 };
        x.users++; if (l.done > 0) x.l1++; if (l.finished) x.fin++; x.min += l.minutes;
        if (!l.finished && Date.now() - l.last > CFG.idleDays * DAY) x.stuck++;
      });
    });
    var les = {};
    (lessons || []).forEach(function (l) { (les[l.lab] = les[l.lab] || []).push(l); });
    var labs = Object.keys(by).map(function (k) { return by[k]; }).sort(function (a, b) { return b.users - a.users || a.lab.localeCompare(b.lab); });
    if (!labs.length) { $('m0Labs').innerHTML = ''; return; }
    var rows = labs.map(function (x) {
      var ls = (les[x.lab] || []).slice().sort(function (a, b) { return a.lesson.localeCompare(b.lesson, 'en', { numeric: true }); });
      var drop = ls.map(function (l) {
        return '<span class="m0-ls" title="' + esc(l.lesson.replace('l', '')) + '-dars: ' + l.reached + ' ochgan, ' + l.done + ' tugatgan">' +
          esc(l.lesson.replace('l', '')) + '<i>' + l.reached + '→' + l.done + '</i></span>';
      }).join('');
      return '<tr><td><b>' + esc(labName(x.lab)) + '</b>' + (LESSONS[x.lab] ? '<div class="m0-sub">' + LESSONS[x.lab] + ' dars</div>' : '') + '</td>' +
        '<td>' + x.users + '</td><td>' + x.l1 + ' <small class="m0-sub">' + pct(x.l1, x.users) + '%</small></td>' +
        '<td>' + x.fin + ' <small class="m0-sub">' + pct(x.fin, x.users) + '%</small></td>' +
        '<td>' + (x.stuck ? '<span class="tag trd">' + x.stuck + '</span>' : '0') + '</td>' +
        '<td>' + Math.round(x.min / x.users) + ' daq</td><td class="m0-lscell">' + (drop || '—') + '</td></tr>';
    }).join('');
    $('m0Labs').innerHTML = '<div class="tbl-scroll"><table class="tbl"><thead><tr><th>Lab</th><th>Boshlagan</th><th>≥1 dars</th><th>Yakunlagan</th><th>Toʻxtagan</th><th>Oʻrtacha vaqt</th>' +
      '<th>Darslar: ochgan → tugatgan</th></tr></thead><tbody>' + rows + '</tbody></table></div>';
  }

  function renderChips() {
    var cnt = {}; state.people.forEach(function (p) { cnt[p.st] = (cnt[p.st] || 0) + 1; });
    $('m0Chips').innerHTML = FILTERS.map(function (f) {
      var c = f[0] === 'all' ? state.people.length : (cnt[f[0]] || 0);
      return '<button class="chip' + (state.flt === f[0] ? ' on' : '') + '" role="tab" aria-selected="' + (state.flt === f[0]) + '" data-f="' + f[0] + '">' + f[1] + '<b>' + c + '</b></button>';
    }).join('');
  }

  var ORDER = { stuck: 0, active: 1, finished: 2, noop: 3, unconfirmed: 4 };
  function renderTable() {
    var q = state.q.trim().toLowerCase();
    var list = state.people.filter(function (p) { return (state.flt === 'all' || p.st === state.flt) && (!q || p.key.indexOf(q) >= 0); });
    list.sort(function (a, b) { return (ORDER[a.st] - ORDER[b.st]) || ((b.last || b.signed) - (a.last || a.signed)); });
    $('m0Count').textContent = list.length + ' ta';
    $('tbM0').innerHTML = list.map(function (p) {
      var s = ST[p.st];
      var labs = p.labs.map(function (l) {
        var where = l.finished ? 'yakunlagan ✓' : l.lesson ? l.lesson.replace('l', '') + '-dars' + (l.section != null ? ', ' + SECT[l.section] : '') : 'modul sahifasi';
        var w = l.total ? pct(l.done, l.total) : 0;
        return '<div class="m0-lab"><div><b>' + esc(labName(l.lab)) + '</b> ' + l.done + ' / ' + (l.total || '?') + ' <span class="m0-sub">· ' + esc(where) + '</span></div>' +
          '<div class="m0-pb"><span style="width:' + (l.finished ? 100 : w) + '%"></span></div></div>';
      }).join('') || '<span class="m0-sub">—</span>';
      var stage = p.stage ? (STAGE[p.stage] || p.stage) + (p.detail ? ' · ' + p.detail : '') + (p.works ? ' · ishlaydi' : '') : '—';
      return '<tr><td>' + esc(p.name || '—') + '<div class="m0-sub">' + esc(p.email || '') + '</div></td>' +
        '<td><span class="tag ' + s[1] + '">' + s[0] + '</span></td><td style="min-width:200px">' + labs + '</td>' +
        '<td>' + esc(stage) + '</td><td>' + (p.minutes ? p.minutes + ' daq' : '—') + '</td>' +
        '<td>' + ago(p.last) + '</td><td>' + (p.signed ? ddmm(p.signed) : '—') + '</td></tr>';
    }).join('') || '<tr><td colspan="7" style="text-align:center;color:var(--muted);padding:16px">' + (state.people.length ? 'Bu filtrda hech kim yoʻq' : 'Hozircha maʼlumot yoʻq') + '</td></tr>';
  }

  async function load() {
    var box = $('m0Funnel'); if (!box) return;
    box.innerHTML = '<div class="m0-note">Yuklanmoqda...</div>';
    var r = await supabase.rpc('kompas_admin_m0_overview');
    if (r.error || !r.data) { box.innerHTML = '<div class="m0-note">Oʻqilmadi: ' + esc(r.error && r.error.message) + '</div>'; return; }
    state.people = group(r.data.users || []);
    renderFunnel(state.people);
    renderLabs(state.people, r.data.lessons);
    renderChips();
    renderTable();
  }

  document.addEventListener('click', function (e) {
    var b = e.target.closest && e.target.closest('#m0Chips .chip');
    if (!b) return;
    state.flt = b.getAttribute('data-f'); renderChips(); renderTable();
  });
  document.addEventListener('input', function (e) {
    if (e.target && e.target.id === 'm0Q') { state.q = e.target.value; renderTable(); }
  });

  window.loadM0Overview = load;
})();
