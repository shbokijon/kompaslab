// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — alifbo.js (2026-10-30)
//  Sahifa matnini yangi oʻzbek lotin alifbosida koʻrsatadi
//  (21.10.2026 qonuni: Oʻ→Ö, Gʻ→Ğ, Sh→Ş, Ch→Ç; tutuq belgisi ʼ qoladi).
//  · Manba fayllar amaldagi alifboda qoladi: faqat koʻrinadigan matn oʻgiriladi,
//    JS kalitlari, localStorage, URL va kod oʻzgarmaydi.
//  · Inglizcha va xorijiy soʻzlar (EX) hamda URL/email oʻgirilmaydi.
//  · Oʻgirilmaydi: script, style, code, pre, textarea, input, [translate="no"],
//    [data-alifbo="off"], lang="uz" dan boshqa til (masalan lang="en"). Eski alifbo: ?alifbo=eski yoki localStorage kompas_alifbo=eski.
// ═══════════════════════════════════════════════════════════════
(function () {
  var MODE = "yangi";
  try {
    var q = /[?&]alifbo=(eski|yangi)/.exec(location.search);
    if (q) localStorage.setItem("kompas_alifbo", q[1]);
    MODE = localStorage.getItem("kompas_alifbo") || "yangi";
  } catch (e) {}
  window.KAlifbo = { mode: MODE, set: function (m) { try { localStorage.setItem("kompas_alifbo", m); } catch (e) {} location.reload(); } };
  if (MODE !== "yangi") return;
  document.documentElement.setAttribute("data-alifbo", "yangi");

  var EX = new Set(["anchor", "approach", "architecture", "archive", "ashford", "bachelor", "bachelor's", "batch", "benchmark", "berkshire", "birch", "british", "catch", "chain", "chair", "challenge", "chambers", "chance", "change", "channel", "chapter", "chapters", "character", "characters", "charge", "charges", "charity", "charset", "chart", "chartered", "chat", "chatbot", "chatbots", "chatgpt", "cheap", "check", "checking", "checklist", "checkout", "checks", "chelmsford", "chelsea", "cheltenham", "chemical", "chemistry", "cheongju", "cheshire", "chester", "chevening", "chiba", "chicago", "chichester", "chief", "child", "childhood", "children", "china", "chinese", "chip", "choice", "chonnam", "choose", "chosen", "chosun", "chung", "chungnam", "church", "coach", "coaching", "dashboard", "dutch", "each", "english", "fachhochschule", "fellowship", "finish", "finished", "fintech", "fischer", "fish", "forschungsvorhaben", "french", "fresh", "greenwich", "hampshire", "harrow", "hochschule", "internship", "internships", "ipswich", "lancashire", "leadership", "machine", "machines", "manchester", "march", "master's", "match", "matches", "matching", "mechanical", "mechanics", "membership", "merchandise", "merchant", "michigan", "motivationsschreiben", "much", "munich", "niche", "norwich", "outreach", "ownership", "partnership", "partnerships", "pitch", "polish", "publish", "published", "push", "research", "researcher", "researchers", "researchgate", "rich", "rush", "schedule", "scheme", "schemes", "schmidt", "scholar", "scholarship", "scholarships", "school", "schooling", "schools", "schuman", "schwarzman", "search", "shallow", "shanghai", "share", "sharebtn", "shared", "sharing", "shbokijon", "sheet", "sheffield", "shell", "shenzhen", "shibuya", "shield", "shift", "ship", "shire", "shokhrukh", "shop", "short", "shortlist", "shot", "should", "shoulder", "show", "shows", "shrewsbury", "shrink", "sketch", "snapshot", "spanish", "speech", "sponsorship", "stretch", "studentship", "such", "switch", "syshint", "tashkent", "teach", "teacher", "teaching", "tech", "technical", "technician", "techniques", "technische", "technology", "umich", "universität", "vimeoshort", "visibilitychange", "wash", "washington", "watch", "watched", "which", "wiltshire", "workshop", "workshops", "yorkshire", "zulassungsbescheid", "zurich", "zürich"]);
  var SUF = /^(lar)?(im|ing|ingiz|imiz|i|si|ni)?(da|dan|ga|ka|qa|ni|ning|dagi|dek|day|gacha|siz|li|mi|ning)?$/;
  var APO = "ʻ‘'`’";
  var LINK = /(https?:\/\/\S+|www\.\S+|[\w.+-]+@[\w-]+(?:\.[\w-]+)+|@[\w.]+|\b[\w-]+(?:\.[\w-]+)*\.(?:uz|com|org|edu|uk|kr|jp|de|net|io|gov|me|app|eu|nl|se|ch|fr|cn|sg|ca|au|info)\b\S*)/i;
  var WORD = /[A-Za-zÀ-ÖØ-öø-ÿĀ-žʻʼ'‘’`]+/g;

  function sh(w) {
    // sh/ch → ş/ç (katta-kichik harfni saqlab)
    return w.replace(/([Ss])([Hh])|([Cc])([Hh])/g, function (m, s, h, c, h2) {
      var up = (s || c) === (s || c).toUpperCase();
      return s ? (up ? "Ş" : "ş") : (up ? "Ç" : "ç");
    });
  }
  function og(w) {
    // oʻ/gʻ (va ' ‘ ` ’ variantlari) → ö/ğ; boshqa unli+ʻ → tutuq ʼ
    return w.replace(/([OoGg])[ʻ‘'`’](?=[A-Za-zÀ-ÿ])/g, function (m, l) {
      return { O: "Ö", o: "ö", G: "Ğ", g: "ğ" }[l];
    }).replace(/([aeiuAEIU])ʻ/g, "$1ʼ");
  }
  function word(w) {
    var lw = w.toLowerCase();
    if (!/[ʻ‘'`’]|sh|ch/i.test(w)) return w;
    // apostrof bilan boshlangan qoʻshimcha: Researchʼda → ildizni saqlash
    var cut = w.search(/ʼ/);
    if (cut > 0) return word(w.slice(0, cut)) + w.slice(cut, cut + 1) + word(w.slice(cut + 1));
    if (EX.has(lw.replace(/[’']s$/, "")) || EX.has(lw)) return w;
    for (var n = lw.length - 1; n >= 5; n--) {
      if (EX.has(lw.slice(0, n)) && SUF.test(lw.slice(n))) return w.slice(0, n) + og(w.slice(n));
    }
    return sh(og(w));
  }
  function conv(t) {
    if (!t || !/[ʻ‘'`’]|sh|ch/i.test(t)) return t;
    var parts = t.split(LINK), out = "";
    for (var i = 0; i < parts.length; i++) {
      var p = parts[i];
      if (p === undefined) continue;
      out += (i % 2) ? p : p.replace(WORD, word);
    }
    return out;
  }
  window.KAlifbo.conv = conv;

  var SKIP = { SCRIPT: 1, STYLE: 1, CODE: 1, PRE: 1, TEXTAREA: 1, INPUT: 1, KBD: 1, SAMP: 1, NOSCRIPT: 1, TEMPLATE: 1 };
  function skip(el) {
    for (; el && el.nodeType === 1; el = el.parentNode) {
      if (SKIP[el.nodeName] || el.isContentEditable) return true;
      if (el.getAttribute("translate") === "no" || el.getAttribute("data-alifbo") === "off") return true;
      var lg = el.getAttribute("lang");
      if (lg && !/^uz/i.test(lg)) return true;   // lang="en" kabi xorijiy matn (namuna jumlalar) oʻgirilmaydi
    }
    return false;
  }
  var ATTR = ["placeholder", "title", "aria-label", "alt", "data-tip"];
  function attrs(el) {
    for (var i = 0; i < ATTR.length; i++) {
      var v = el.getAttribute && el.getAttribute(ATTR[i]);
      if (v) { var c = conv(v); if (c !== v) el.setAttribute(ATTR[i], c); }
    }
    if (el.nodeName === "INPUT" && /^(button|submit|reset)$/i.test(el.type) && el.value) { var cv = conv(el.value); if (cv !== el.value) el.value = cv; }
  }
  // Atributlar (placeholder, title, aria-label…) uchun: element oʻzi textarea/input yoki translate="no"
  // boʻlsa ham atributi oʻgiriladi; faqat ajdod oʻtkazib yuborilgan boʻlsa yoki elementning oʻzi
  // lang="en" / data-alifbo="off" boʻlsa oʻgirilmaydi.
  function attrSkip(el) {
    if (el.getAttribute("data-alifbo") === "off") return true;
    var lg = el.getAttribute("lang");
    if (lg && !/^uz/i.test(lg)) return true;
    return skip(el.parentNode);
  }
  function walk(root) {
    if (!root) return;
    if (root.nodeType === 3) { if (!skip(root.parentNode)) { var c = conv(root.nodeValue); if (c !== root.nodeValue) root.nodeValue = c; } return; }
    if (root.nodeType !== 1) return;
    if (!attrSkip(root)) attrs(root);
    if (skip(root)) { if (root.querySelectorAll) root.querySelectorAll("[placeholder],[title],[aria-label],[alt],[data-tip]").forEach(function (e) { if (!attrSkip(e)) attrs(e); }); return; }
    var tw = document.createTreeWalker(root, 5, null), n;
    while ((n = tw.nextNode())) {
      if (n.nodeType === 1) { if (!attrSkip(n)) attrs(n); continue; }
      if (skip(n.parentNode)) continue;
      var v = n.nodeValue, cc = conv(v);
      if (cc !== v) n.nodeValue = cc;
    }
  }
  function run() {
    var t = conv(document.title); if (t !== document.title) document.title = t;
    walk(document.body);
    new MutationObserver(function (ms) {
      for (var i = 0; i < ms.length; i++) {
        var m = ms[i];
        if (m.type === "characterData") walk(m.target);
        else if (m.type === "attributes") { if (!attrSkip(m.target)) attrs(m.target); }
        else for (var j = 0; j < m.addedNodes.length; j++) walk(m.addedNodes[j]);
      }
    }).observe(document.body, { childList: true, subtree: true, characterData: true, attributes: true, attributeFilter: ATTR });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run); else run();
})();
