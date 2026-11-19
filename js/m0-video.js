// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — m0-video.js (2026-11-19)
//  M0 darsiga YouTube video: "Asosiy qism" boshida pleyer.
//  Roʻyxat: data/m0-video.json ({ "<modul>": { "<dars id>": { "yt": "<ID yoki havola>", "title": "...", "min": 8 } } }).
//  Yozuvi yoʻq darsda hech narsa qoʻshilmaydi va YouTube yuklanmaydi.
//  Maxfiylik: bosilmaguncha faqat muqova rasmi (i.ytimg.com); pleyer youtube-nocookie.com dan,
//  bosilgandan keyin. Videoni YouTube'da "Roʻyxatsiz" (Unlisted) qilib yuklang: havolasi bor
//  har kim koʻra oladi, shuning uchun bu usul faqat bepul M0 uchun.
//  Yuklovchi: js/kompas-module.js (dars koʻrinishida).
// ═══════════════════════════════════════════════════════════════
(function () {
  var M = window.KMOD, body = document.body;
  if (!M || !body) return;
  // 2026-11-19: dars sahifasidan tashqari hub (kalit "l0") va yakun ("res") ham; joy: [data-kvideo] (boʻlmasa "Asosiy qism")
  var view = body.getAttribute("data-kview");
  var lid = view === "lesson" ? body.getAttribute("data-klesson") : view === "hub" ? "l0" : view === "yakun" ? "res" : null;
  if (!lid) return;

  function ytId(v) {
    v = String(v || "").trim();
    if (/^[\w-]{11}$/.test(v)) return v;
    var m = /(?:youtu\.be\/|[?&]v=|\/embed\/|\/shorts\/|\/live\/)([\w-]{11})/.exec(v);
    return m ? m[1] : null;
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  function css() {
    if (document.getElementById("kvid-css")) return;
    var s = document.createElement("style"); s.id = "kvid-css";
    s.textContent =
      ".kvid{margin:0 0 18px}" +
      ".kvid-box{position:relative;aspect-ratio:16/9;border-radius:14px;overflow:hidden;background:#1d2420;box-shadow:0 1px 3px rgba(0,0,0,.12)}" +
      ".kvid-box img,.kvid-box iframe{position:absolute;inset:0;width:100%;height:100%;border:0;object-fit:cover}" +
      ".kvid-play{all:unset;position:absolute;inset:0;cursor:pointer;display:flex;align-items:center;justify-content:center}" +
      ".kvid-play:focus-visible{outline:3px solid #c9a84c;outline-offset:-3px}" +
      ".kvid-play span{width:68px;height:68px;border-radius:50%;background:#2d4a3e;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 18px rgba(0,0,0,.35);transition:transform .15s}" +
      ".kvid-play:hover span{transform:scale(1.07)}" +
      ".kvid-play svg{width:26px;height:26px;margin-left:4px;fill:#fff}" +
      ".kvid-cap{font-size:12.5px;color:var(--muted,#6b6b6b);margin-top:7px;text-align:center}" +
      "@media (prefers-reduced-motion:reduce){.kvid-play span{transition:none}}";
    document.head.appendChild(s);
  }

  function mount(v) {
    var id = ytId(v && v.yt); if (!id) return;
    var slot = document.querySelector('[data-kvideo="' + lid + '"]'), host, art;
    if (!slot) {
      art = document.getElementById(lid); if (!art) return;
      var panels = art.querySelectorAll(".l-body > .panel");
      host = panels[1] || panels[0];
    } else host = slot;
    if (!host || host.querySelector(".kvid")) return;
    css();
    var title = v.title ? String(v.title) : "Dars videosi";
    var cap = "Video" + (v.sec ? ": " + (+v.sec) + " soniya" : v.min ? ": " + (+v.min) + " daqiqa" : "") + " · YouTube orqali";
    var w = document.createElement("figure"); w.className = "kvid";
    w.innerHTML =
      '<div class="kvid-box">' +
      '<img src="https://i.ytimg.com/vi/' + id + '/hqdefault.jpg" alt="" loading="lazy" width="480" height="360">' +
      '<button type="button" class="kvid-play" aria-label="Videoni koʻrish: ' + esc(title) + '"><span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg></span></button>' +
      "</div>" +
      '<figcaption class="kvid-cap">' + esc(cap) + "</figcaption>";
    var im = w.querySelector("img"); im.addEventListener("error", function () { im.remove(); });
    w.querySelector(".kvid-play").addEventListener("click", function () {
      var box = w.querySelector(".kvid-box"), f = document.createElement("iframe");
      f.src = "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1&rel=0&playsinline=1";
      f.title = title;
      f.allow = "autoplay; encrypted-media; picture-in-picture; fullscreen";
      f.allowFullscreen = true;
      f.referrerPolicy = "strict-origin-when-cross-origin";
      box.innerHTML = ""; box.appendChild(f);
      if (window.KSfx && KSfx.play) try { KSfx.play("tab"); } catch (e) {}
    });
    host.insertBefore(w, host.firstChild);
  }

  fetch("data/m0-video.json", { cache: "no-cache" })
    .then(function (r) { return r.ok ? r.json() : {}; })
    .then(function (d) { var m = d && d[M.base]; if (m && m[lid]) mount(m[lid]); })
    .catch(function () {});
})();
