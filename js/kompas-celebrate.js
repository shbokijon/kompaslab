/* Kompas Lab — tabrik oynasi (2026-11-06)
 * KCelebrate.show({ kind: "donat" | "tolov", title, text, amount, button, href })
 *   donat : smayl stiker + ikki karnay + mushakbozlik (terrakota/oltin)
 *   tolov : kompas nishoni (strelka shimolga burilib, belgi chiqadi) + oltin halqa mushakbozlik
 * Faqat server "paid" deb tasdiqlagandan keyin chaqiriladi (donat.js, dashboard.html).
 * prefers-reduced-motion: harakatsiz koʻrinish, mushakbozliksiz. Tovush: KSfx.play("win"), boʻlsa.
 */
(function () {
  "use strict";
  if (window.KCelebrate) return;

  var C = { green: "#2d4a3e", terra: "#c4622d", cream: "#f4f3ef", gold: "#c9a84c", goldD: "#a8862f" };
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  var CSS = "" +
    ".kc-ov{position:fixed;inset:0;z-index:9999;display:flex;align-items:center;justify-content:center;padding:16px;background:rgba(20,34,28,.55);backdrop-filter:blur(3px);opacity:0;transition:opacity .25s}" +
    ".kc-ov.is-in{opacity:1}" +
    ".kc-cv{position:fixed;inset:0;pointer-events:none}" +
    ".kc-card{position:relative;width:min(420px,100%);background:#fff;border-radius:24px;padding:28px 24px 22px;text-align:center;box-shadow:0 30px 80px rgba(0,0,0,.25);transform:translateY(18px) scale(.96);transition:transform .45s cubic-bezier(.2,1.4,.4,1)}" +
    ".kc-ov.is-in .kc-card{transform:none}" +
    ".kc-stage{position:relative;height:150px;margin:-70px auto 6px;width:300px;max-width:100%}" +
    ".kc-stk{position:absolute;left:50%;top:0;width:132px;height:132px;margin-left:-66px;filter:drop-shadow(0 10px 18px rgba(0,0,0,.18));animation:kcPop .7s cubic-bezier(.2,1.6,.4,1) both}" +
    ".kc-horn{position:absolute;bottom:4px;width:118px;height:60px}" +
    ".kc-horn.l{left:-6px;transform-origin:100% 70%;animation:kcBlowL 1.1s ease-in-out .35s 3 both}" +
    ".kc-horn.r{right:-6px;transform-origin:0 70%;animation:kcBlowR 1.1s ease-in-out .35s 3 both}" +
    ".kc-wave{opacity:0;animation:kcWave 1.1s ease-out .45s 3}" +
    ".kc-wave.w2{animation-delay:.6s}" +
    ".kc-needle{transform-origin:50px 50px;animation:kcNeedle 1.2s cubic-bezier(.3,1.5,.5,1) .2s both,kcDim .4s ease 1.2s forwards}" +
    ".kc-tick{stroke-dasharray:60;stroke-dashoffset:60;animation:kcTick .5s ease-out 1.2s forwards}" +
    ".kc-card h3{font-family:Cambria,Caladea,'Playfair Display',serif;font-size:26px;color:" + C.green + ";margin:4px 0 6px}" +
    ".kc-amt{display:inline-block;font-family:'JetBrains Mono','IBM Plex Sans',monospace;font-weight:800;font-size:15px;color:" + C.goldD + ";background:#fdf6dc;border:1px solid #ecd9a0;border-radius:999px;padding:4px 12px;margin:2px 0 10px}" +
    ".kc-card p{color:#5f7169;font-size:15px;line-height:1.55;margin:0 0 18px}" +
    ".kc-btn{display:inline-block;font:inherit;font-weight:700;border:0;cursor:pointer;background:" + C.terra + ";color:#fff;padding:12px 26px;border-radius:12px;box-shadow:0 6px 22px rgba(196,98,45,.3);text-decoration:none}" +
    ".kc-x{position:absolute;top:10px;right:12px;border:0;background:none;font-size:22px;color:#9aada6;cursor:pointer;line-height:1}" +
    "@keyframes kcPop{0%{transform:scale(.2) rotate(-25deg);opacity:0}70%{transform:scale(1.08) rotate(6deg);opacity:1}100%{transform:none}}" +
    "@keyframes kcBlowL{0%,100%{transform:rotate(18deg)}50%{transform:rotate(8deg) translateY(-4px)}}" +
    "@keyframes kcBlowR{0%,100%{transform:rotate(-18deg)}50%{transform:rotate(-8deg) translateY(-4px)}}" +
    "@keyframes kcWave{0%{opacity:0;transform:scale(.6)}30%{opacity:1}100%{opacity:0;transform:scale(1.25)}}" +
    "@keyframes kcNeedle{0%{transform:rotate(200deg)}100%{transform:rotate(0)}}" +
    "@keyframes kcTick{to{stroke-dashoffset:0}}" +
    "@keyframes kcDim{to{opacity:.18}}" +
    "@media (prefers-reduced-motion:reduce){.kc-stk,.kc-horn,.kc-wave,.kc-needle{animation:none!important;opacity:.18}.kc-wave{opacity:.8}.kc-tick{animation:none;stroke-dashoffset:0}.kc-card{transition:none}}";

  // Oʻziga xos smayl: oltin doira, oʻng koʻz qisilgan, terrakota yonoqlar, kompas strelkali “choʻqqi”
  var SMILE = '<svg class="kc-stk" viewBox="0 0 120 120" aria-hidden="true">' +
    '<circle cx="60" cy="62" r="52" fill="' + C.gold + '"/><circle cx="60" cy="62" r="52" fill="none" stroke="#fff" stroke-width="5"/>' +
    '<path d="M60 4 L68 18 L52 18 Z" fill="' + C.terra + '"/>' +
    '<circle cx="42" cy="54" r="6" fill="' + C.green + '"/>' +
    '<path d="M71 55 q7 -7 14 0" stroke="' + C.green + '" stroke-width="5" fill="none" stroke-linecap="round"/>' +
    '<circle cx="34" cy="72" r="7" fill="' + C.terra + '" opacity=".45"/><circle cx="86" cy="72" r="7" fill="' + C.terra + '" opacity=".45"/>' +
    '<path d="M38 74 q22 26 44 0" stroke="' + C.green + '" stroke-width="6" fill="#fff" stroke-linecap="round" stroke-linejoin="round"/></svg>';

  // Karnay: uzun mis truba, ogʻzidan tovush toʻlqinlari
  function horn(side) {
    var flip = side === "r" ? ' transform="translate(118 0) scale(-1 1)"' : "";
    return '<svg class="kc-horn ' + side + '" viewBox="0 0 118 60" aria-hidden="true"><g' + flip + '>' +
      '<path d="M4 40 L70 33 L70 41 Z" fill="' + C.goldD + '"/>' +
      '<path d="M68 30 C84 28 92 16 100 10 L100 62 C92 56 84 46 68 44 Z" fill="' + C.gold + '" stroke="' + C.goldD + '" stroke-width="2"/>' +
      '<rect x="0" y="35" width="10" height="10" rx="3" fill="' + C.terra + '"/>' +
      '<path class="kc-wave" d="M106 22 q8 14 0 28" stroke="' + C.terra + '" stroke-width="3" fill="none" stroke-linecap="round"/>' +
      '<path class="kc-wave w2" d="M112 14 q12 22 0 44" stroke="' + C.terra + '" stroke-width="3" fill="none" stroke-linecap="round"/>' +
      '</g></svg>';
  }

  // Tolov nishoni: kompas, strelka aylanib shimolga toʻxtaydi, keyin belgi chiziladi
  var BADGE = '<svg class="kc-stk" viewBox="0 0 100 100" aria-hidden="true">' +
    '<circle cx="50" cy="50" r="46" fill="' + C.cream + '" stroke="' + C.green + '" stroke-width="6"/>' +
    '<g fill="' + C.green + '" font-family="JetBrains Mono,monospace" font-size="9" font-weight="700" text-anchor="middle"><text x="50" y="16">N</text></g>' +
    '<g class="kc-needle"><path d="M50 18 L57 50 L50 46 L43 50 Z" fill="' + C.terra + '"/><path d="M50 82 L57 50 L50 54 L43 50 Z" fill="' + C.green + '" opacity=".35"/></g>' +
    '<circle cx="50" cy="50" r="5" fill="' + C.gold + '"/>' +
    '<path class="kc-tick" d="M33 62 L45 73 L69 49" stroke="' + C.green + '" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>';

  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function fmt(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, " "); }

  // Mushakbozlik: raketa koʻtariladi, choʻqqida halqa boʻlib portlaydi
  function fireworks(cv, kind) {
    var ctx = cv.getContext("2d"), dpr = Math.min(window.devicePixelRatio || 1, 2), W, H;
    function size() { W = innerWidth; H = innerHeight; cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0); }
    size();
    var pal = kind === "tolov" ? [C.gold, "#e6c97a", C.green, "#fff"] : [C.terra, C.gold, "#e88a55", C.green, "#fff"];
    var rockets = [], sparks = [], t0 = performance.now(), launched = 0, total = kind === "tolov" ? 6 : 8;
    function launch() {
      var x = W * (0.15 + Math.random() * 0.7);
      rockets.push({ x: x, y: H + 10, vy: -(H * 0.012 + Math.random() * 3), ty: H * (0.12 + Math.random() * 0.28), c: pal[launched % pal.length] });
      launched++;
    }
    function burst(r) {
      var n = kind === "tolov" ? 40 : 54, ring = kind === "tolov";
      for (var i = 0; i < n; i++) {
        var a = (i / n) * Math.PI * 2, s = ring ? 3.4 : 1.5 + Math.random() * 3.4;
        sparks.push({ x: r.x, y: r.y, vx: Math.cos(a) * s, vy: Math.sin(a) * s, life: 1, c: Math.random() < 0.7 ? r.c : pal[(i % pal.length)] });
      }
    }
    var raf;
    function frame(now) {
      var el = now - t0;
      if (launched < total && el > launched * 320) launch();
      ctx.clearRect(0, 0, W, H);
      rockets = rockets.filter(function (r) {
        r.y += r.vy; ctx.fillStyle = r.c; ctx.beginPath(); ctx.arc(r.x, r.y, 2.4, 0, 7); ctx.fill();
        if (r.y <= r.ty) { burst(r); return false; } return true;
      });
      sparks = sparks.filter(function (p) {
        p.x += p.vx; p.y += p.vy; p.vy += 0.045; p.vx *= 0.985; p.life -= 0.012;
        ctx.globalAlpha = Math.max(p.life, 0); ctx.fillStyle = p.c; ctx.beginPath(); ctx.arc(p.x, p.y, 2.2, 0, 7); ctx.fill();
        return p.life > 0;
      });
      ctx.globalAlpha = 1;
      if (launched < total || rockets.length || sparks.length) raf = requestAnimationFrame(frame);
    }
    raf = requestAnimationFrame(frame);
    addEventListener("resize", size);
    return function () { cancelAnimationFrame(raf); removeEventListener("resize", size); };
  }

  function show(o) {
    o = o || {};
    var kind = o.kind === "tolov" ? "tolov" : "donat";
    if (!document.getElementById("kc-css")) {
      var st = document.createElement("style"); st.id = "kc-css"; st.textContent = CSS; document.head.appendChild(st);
    }
    var ov = document.createElement("div");
    ov.className = "kc-ov"; ov.setAttribute("role", "dialog"); ov.setAttribute("aria-modal", "true"); ov.setAttribute("aria-labelledby", "kcTitle");
    var stage = kind === "tolov" ? BADGE : horn("l") + SMILE + horn("r");
    ov.innerHTML = '<canvas class="kc-cv"></canvas><div class="kc-card">' +
      '<button type="button" class="kc-x" aria-label="Yopish">×</button>' +
      '<div class="kc-stage">' + stage + '</div>' +
      '<h3 id="kcTitle">' + esc(o.title || (kind === "tolov" ? "Obuna ochildi" : "Rahmat!")) + '</h3>' +
      (o.amount ? '<div class="kc-amt">' + fmt(o.amount) + ' soʻm</div>' : "") +
      '<p>' + esc(o.text || "") + '</p>' +
      (o.href ? '<a class="kc-btn" href="' + esc(o.href) + '">' + esc(o.button || "Davom etish") + '</a>'
              : '<button type="button" class="kc-btn">' + esc(o.button || "Davom etish") + '</button>') +
      '</div>';
    document.body.appendChild(ov);
    var stop = reduce ? function () {} : fireworks(ov.querySelector(".kc-cv"), kind);
    requestAnimationFrame(function () { ov.classList.add("is-in"); });
    try { if (window.KSfx) window.KSfx.play("win"); } catch (e) {}
    var prev = document.activeElement, btn = ov.querySelector(".kc-btn");
    if (btn) btn.focus();
    function close() {
      stop(); ov.classList.remove("is-in");
      setTimeout(function () { if (ov.parentNode) ov.parentNode.removeChild(ov); }, 260);
      document.removeEventListener("keydown", onKey);
      if (prev && prev.focus) prev.focus();
    }
    function onKey(e) { if (e.key === "Escape") close(); }
    document.addEventListener("keydown", onKey);
    ov.querySelector(".kc-x").addEventListener("click", close);
    if (btn && btn.tagName === "BUTTON") btn.addEventListener("click", close);
    ov.addEventListener("click", function (e) { if (e.target === ov) close(); });
    return close;
  }

  window.KCelebrate = { show: show };
})();
