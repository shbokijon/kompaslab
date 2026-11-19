// ═══════════════════════════════════════════════════════════════
//  KOMPAS LAB — module-video.js (2026-11-19)
//  Modul va dars videolari: YouTube yoki Vimeo. Joy: [data-kvideo="l1|l2…|res|l0"].
//  Manba (ustunlik tartibida):
//    1) Supabase RPC kompas_module_videos(course_slug, module_index): admin → Videolar boʻlimi.
//       M0 hammaga; pullik modul faqat shu modulga kirish huquqi borlarga (server tekshiradi).
//    2) data/m0-video.json (faqat M0, eski qoʻlda roʻyxat): { "<lab>-m0": { "l1": { "yt": "…", "title": "…", "sec": 40 } } }
//  Ikki rejim:
//    • M0 sahifalari (window.KMOD): joriy dars / hub (l0) / yakun (res) uchun bitta video.
//    • Pullik modul (<main data-kv-lab="master-lab" data-kv-mod="3">): sahifadagi hamma joy.
//  Video yoʻq joyda hech narsa koʻrinmaydi va tashqi saytga soʻrov ketmaydi.
//  Maxfiylik: YouTube bosilmaguncha faqat muqova (i.ytimg.com), pleyer youtube-nocookie.com dan;
//  Vimeo bosilgandan keyin player.vimeo.com (dnt=1). CSP frame-src ikkalasiga ruxsat beradi.
// ═══════════════════════════════════════════════════════════════
(function () {
  if (window.KVideo) return;
  var body = document.body; if (!body) return;

  function ytId(v) {
    v = String(v || "").trim();
    if (/^[\w-]{11}$/.test(v)) return v;
    var m = /(?:youtu\.be\/|[?&]v=|\/embed\/|\/shorts\/|\/live\/)([\w-]{11})/.exec(v);
    return m ? m[1] : null;
  }
  function vimeo(v) {
    v = String(v || "").trim();
    var m = /^(\d{6,12})(?:[\/?#:](?:h=)?([0-9a-f]{6,20}))?$/i.exec(v) ||
            /vimeo\.com\/(?:video\/|.*\/)?(\d{6,12})(?:\/([0-9a-f]{6,20}))?/i.exec(v);
    if (!m) return null;
    var h = m[2] || ((/[?&]h=([0-9a-f]{6,20})/i.exec(v) || [])[1]) || "";
    return { id: m[1], h: h };
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
      ".kvid-t{position:absolute;left:14px;right:14px;bottom:12px;color:#f4f3ef;font-size:14px;font-weight:700;text-align:center;pointer-events:none}" +
      ".kvid-cap{font-size:12.5px;color:var(--muted,#6b6b6b);margin-top:7px;text-align:center}" +
      "@media (prefers-reduced-motion:reduce){.kvid-play span{transition:none}}";
    document.head.appendChild(s);
  }

  // v: { p: "youtube"|"vimeo", v: "<ID yoki havola>", title, sec, min }  (eski JSON: { yt: … })
  function mount(host, v) {
    if (!host || !v || host.querySelector(".kvid")) return false;
    var prov = v.p || (v.yt ? "youtube" : /vimeo/i.test(v.v || "") ? "vimeo" : "youtube");
    var raw = v.v || v.yt, src = null, thumb = "";
    if (prov === "vimeo") {
      var vm = vimeo(raw); if (!vm) return false;
      src = "https://player.vimeo.com/video/" + vm.id + "?autoplay=1&dnt=1&title=0&byline=0&portrait=0" + (vm.h ? "&h=" + vm.h : "");
    } else {
      var id = ytId(raw); if (!id) return false;
      src = "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1&rel=0&playsinline=1";
      thumb = "https://i.ytimg.com/vi/" + id + "/hqdefault.jpg";
    }
    css();
    var title = v.title ? String(v.title) : "Video";
    var len = v.sec ? (+v.sec) + " soniya" : v.min ? (+v.min) + " daqiqa" : "";
    var cap = "Video" + (len ? ": " + len : "") + (prov === "vimeo" ? " · Vimeo orqali" : " · YouTube orqali");
    var w = document.createElement("figure"); w.className = "kvid";
    w.innerHTML =
      '<div class="kvid-box">' +
      (thumb ? '<img src="' + thumb + '" alt="" loading="lazy" width="480" height="360">' : '<span class="kvid-t">' + esc(title) + "</span>") +
      '<button type="button" class="kvid-play" aria-label="Videoni koʻrish: ' + esc(title) + '"><span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg></span></button>' +
      "</div>" +
      '<figcaption class="kvid-cap">' + esc(cap) + "</figcaption>";
    var im = w.querySelector("img"); if (im) im.addEventListener("error", function () { im.remove(); });
    w.querySelector(".kvid-play").addEventListener("click", function () {
      var box = w.querySelector(".kvid-box"), f = document.createElement("iframe");
      f.src = src; f.title = title;
      f.allow = "autoplay; encrypted-media; picture-in-picture; fullscreen";
      f.allowFullscreen = true;
      f.referrerPolicy = "strict-origin-when-cross-origin";
      box.innerHTML = ""; box.appendChild(f);
      if (window.KSfx && KSfx.play) try { KSfx.play("tab"); } catch (e) {}
    });
    host.insertBefore(w, host.firstChild);
    return true;
  }

  function fromDb(lab, mod) {
    var sb = window.supabase;
    if (!sb || typeof sb.rpc !== "function") return Promise.resolve({});
    return sb.rpc("kompas_module_videos", { p_course_slug: lab, p_module_index: mod })
      .then(function (r) { return (r && !r.error && r.data && typeof r.data === "object") ? r.data : {}; })
      .catch(function () { return {}; });
  }
  function fromJson(key) {
    return fetch("data/m0-video.json", { cache: "no-cache" })
      .then(function (r) { return r.ok ? r.json() : {}; })
      .then(function (d) { return (d && d[key]) || {}; })
      .catch(function () { return {}; });
  }

  window.KVideo = { mount: mount };

  var M = window.KMOD;
  if (M && M.base) {
    // M0 rejimi
    var view = body.getAttribute("data-kview");
    var lid = view === "lesson" ? body.getAttribute("data-klesson") : view === "hub" ? "l0" : view === "yakun" ? "res" : null;
    if (!lid) return;
    var lab0 = String(M.base).replace(/-m0$/, "");
    Promise.all([fromJson(M.base), fromDb(lab0, 0)]).then(function (a) {
      var v = (a[1] && a[1][lid]) || (a[0] && a[0][lid]); if (!v) return;
      var host = document.querySelector('[data-kvideo="' + lid + '"]');
      if (!host) { var art = document.getElementById(lid); if (!art) return; var ps = art.querySelectorAll(".l-body > .panel"); host = ps[1] || ps[0]; }
      mount(host, v);
    });
    return;
  }

  var main = document.querySelector("main[data-kv-lab]");
  if (!main) return;
  var lab = main.getAttribute("data-kv-lab"), mod = +main.getAttribute("data-kv-mod");
  if (!lab || !(mod >= 0) || !document.querySelector("[data-kvideo]")) return;
  fromDb(lab, mod).then(function (d) {
    document.querySelectorAll("[data-kvideo]").forEach(function (el) {
      var v = d[el.getAttribute("data-kvideo")]; if (v) mount(el, v);
    });
  });
})();
