// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — utm.js (2026-11-12)
//  Kanal oʻlchovi: birinchi teginish (first touch), 30 kun.
//  · ?utm_source=…&utm_medium=…&utm_campaign=… boʻlsa, localStorage ga yoziladi
//    (allaqachon yozilgan va 30 kundan yangi boʻlsa, ustidan yozilmaydi).
//  · M0 darvozasi (m0-access.html?next=/master-lab-m0.html?utm_…) ichidagi UTM ham olinadi.
//  · UTM yoʻq, lekin boshqa saytdan kelgan boʻlsa: source = "ref:<domen>", medium = "referral".
//  Oʻqish: window.KompasUTM.get() → {source, medium, campaign, content, term, page, at} yoki null.
//  Havola standarti: docs/UTM.md
// ═══════════════════════════════════════════════════════════════
(function () {
  if (window.KompasUTM) return;
  var K = "kompas_utm_v1", TTL = 30 * 864e5;
  var KEYS = ["source", "medium", "campaign", "content", "term"];

  function clean(v) { return String(v).slice(0, 60).replace(/[^\w\-.:]/g, "_"); }
  function parse(q) {
    var p, o = {};
    try { p = new URLSearchParams(q || ""); } catch (e) { return null; }
    KEYS.forEach(function (k) { var v = p.get("utm_" + k); if (v) o[k] = clean(v); });
    return o.source ? o : null;
  }
  function read() {
    try {
      var x = JSON.parse(localStorage.getItem(K) || "null");
      if (x && x.source && Date.now() - x.at < TTL) return x;
    } catch (e) {}
    return null;
  }

  var cur = parse(location.search);
  if (!cur) {
    try {
      var nx = new URLSearchParams(location.search).get("next");
      if (nx && nx.indexOf("?") >= 0) cur = parse(nx.split("?")[1]);
    } catch (e) {}
  }
  if (!cur && document.referrer) {
    try {
      var h = new URL(document.referrer).hostname.replace(/^www\./, "");
      if (h && !/(^|\.)kompaslab\.uz$/.test(h) && !/(^|\.)click\.uz$/.test(h)) cur = { source: clean("ref:" + h), medium: "referral" };
    } catch (e) {}
  }
  if (cur && !read()) {
    cur.at = Date.now();
    cur.page = location.pathname.slice(0, 80);
    try { localStorage.setItem(K, JSON.stringify(cur)); } catch (e) {}
  }

  window.KompasUTM = {
    get: function () {
      var x = read();
      if (!x) return null;
      var o = {};
      KEYS.forEach(function (k) { if (x[k]) o[k] = x[k]; });
      o.page = x.page || null;
      o.at = new Date(x.at).toISOString();
      return o;
    }
  };
})();
