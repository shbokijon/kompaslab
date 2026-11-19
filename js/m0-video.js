// KOMPAS LAB — m0-video.js (2026-11-19): eski nom saqlanadi (js/kompas-module.js shu faylni yuklaydi).
// Pleyer va manba endi js/module-video.js da: YouTube va Vimeo, admin → Videolar (Supabase) + data/m0-video.json.
(function () {
  if (window.KVideo || document.querySelector('script[src$="module-video.js"]')) return;
  var s = document.createElement("script"); s.src = "js/module-video.js"; s.defer = true; document.head.appendChild(s);
})();
