/* Bosh sahifa: interaktiv grafiklar. Maʼlumot faqat sahifada, hech qayerga yuborilmaydi. 2026-11-13 */
(function () {
  "use strict";
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function snd(n) { try { if (window.KSfx && KSfx.play) KSfx.play(n); } catch (e) {} }

  /* 1. Piramida: Lab nima */
  var pyr = $("[data-pyr]");
  if (pyr) {
    var out = $("[data-pyr-out]");
    $$("button", pyr).forEach(function (b) {
      b.addEventListener("click", function () {
        $$("button", pyr).forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        out.innerHTML = "<b>" + b.getAttribute("data-t") + "</b>" + b.getAttribute("data-d");
        snd("pick");
      });
    });
  }

  /* 2. Dars tuzilmasi: 4 qismni ochib koʻrish */
  var dars = $("[data-dars]");
  if (dars) {
    var bar = $("[data-dars-bar]"), msg = $("[data-dars-msg]");
    var btns = $$("button", dars);
    btns.forEach(function (b) {
      b.addEventListener("click", function () {
        b.setAttribute("aria-pressed", b.getAttribute("aria-pressed") === "true" ? "false" : "true");
        var n = btns.filter(function (x) { return x.getAttribute("aria-pressed") === "true"; }).length;
        bar.style.width = (n / btns.length * 100) + "%";
        if (n === btns.length) { msg.textContent = "Dars yakunlandi. Haqiqiy darsda shu yerda XP olasiz."; msg.className = "dars-msg ok"; snd("pick"); }
        else { msg.textContent = n + " / " + btns.length + " qism ochildi"; msg.className = "dars-msg"; }
      });
    });
  }

  /* 3. Yoʻl tablari */
  var tabs = $("[data-yt]");
  if (tabs) {
    var tb = $$("[role=tab]", tabs);
    tb.forEach(function (t, i) {
      t.addEventListener("click", function () { sel(i); });
      t.addEventListener("keydown", function (e) {
        if (e.key === "ArrowRight") { sel((i + 1) % tb.length); tb[(i + 1) % tb.length].focus(); }
        if (e.key === "ArrowLeft") { var j = (i - 1 + tb.length) % tb.length; sel(j); tb[j].focus(); }
      });
    });
    function sel(i) {
      tb.forEach(function (t, k) {
        t.setAttribute("aria-selected", k === i ? "true" : "false");
        t.tabIndex = k === i ? 0 : -1;
        var p = document.getElementById(t.getAttribute("aria-controls"));
        if (p) p.hidden = k !== i;
      });
      snd("pick");
    }
  }

  /* 3a. Soha qadamlari */
  var soha = $("[data-soha]");
  if (soha) {
    var tip = $("[data-soha-tip]");
    $$("button", soha).forEach(function (b) {
      b.addEventListener("click", function () {
        $$("button", soha).forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        tip.textContent = b.getAttribute("data-tip");
      });
    });
  }

  /* 3b. 12 oylik reja (Gantt) */
  var gn = $("[data-gantt]");
  if (gn) {
    var OY = ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr"];
    var QS = ["Yan", "Fev", "Mar", "Apr", "May", "Iyn", "Iyl", "Avg", "Sen", "Okt", "Noy", "Dek"];
    var ROWS = [
      ["Saralangan roʻyxat", 1, 2, "t"], ["Til sertifikati", 2, 5, "t"], ["Akademik CV", 3, 4, "h"],
      ["Maqsad bayonnomasi", 4, 6, "h"], ["Tavsiya xatlari", 5, 7, "h"], ["Ariza topshirish", 7, 8, "s"],
      ["Natija va viza", 9, 10, "q"], ["Joʻnash oldi nazorat", 11, 12, "q"]
    ];
    var start = $("[data-gn-start]"), gout = $("[data-gn-out]"), filt = null;
    var now = new Date().getMonth();
    OY.forEach(function (m, i) { var o = document.createElement("option"); o.value = i; o.textContent = m; if (i === now) o.selected = true; start.appendChild(o); });
    function mname(n, s) { var k = (Number(start.value) + n - 1) % 12; return s ? QS[k] : OY[k]; }
    function draw() {
      var h = "<div class=\"mh\" style=\"text-align:left\">OY</div>";
      for (var m = 1; m <= 12; m++) {
        var cs = [];
        ROWS.forEach(function (r) { if (m >= r[1] && m <= r[2] && cs.indexOf(r[3]) < 0 && (!filt || filt === r[3])) cs.push(r[3]); });
        var dots = cs.map(function (c) { return "<i class=\"c-" + c + "\"></i>"; }).join("");
        h += "<div class=\"mh" + (cs.length ? " on" : "") + "\">" + m + "<br>" + mname(m, true) + "<span class=\"md\">" + dots + "</span></div>";
      }
      ROWS.forEach(function (r) {
        h += "<div class=\"rl\">" + r[0] + "</div>";
        h += "<button type=\"button\" class=\"bar c-" + r[3] + (filt && filt !== r[3] ? " dim" : "") + "\" style=\"grid-column:" + (r[1] + 1) + " / " + (r[2] + 2) + "\" data-i=\"" + r[0] + "\" data-a=\"" + r[1] + "\" data-b=\"" + r[2] + "\" aria-label=\"" + r[0] + "\"></button>";
      });
      $(".gn-in", gn).innerHTML = h;
      $$(".bar", gn).forEach(function (b) {
        b.addEventListener("click", function () {
          var a = +b.getAttribute("data-a"), z = +b.getAttribute("data-b");
          gout.innerHTML = "<b>" + b.getAttribute("data-i") + ":</b> " + a + "–" + z + "-oy (" + mname(a) + " – " + mname(z) + ")";
        });
      });
    }
    start.addEventListener("change", function () { draw(); gout.textContent = ""; });
    $$("[data-gn-f]").forEach(function (b) {
      b.addEventListener("click", function () { var f = b.getAttribute("data-gn-f"); filt = filt === f ? null : f; draw(); });
    });
    draw();
  }

  /* 3c. Tayyorgarlik koʻrsatkichi (namuna) */
  var rd = $("[data-rd]");
  if (rd) {
    var fg = $(".fg", rd), num = $("[data-rd-n]", rd), nx = $("[data-rd-next]");
    var C = 2 * Math.PI * 84;
    fg.style.strokeDasharray = C;
    var ins = $$("input", rd);
    function upd() {
      var sum = 0, low = null;
      ins.forEach(function (i) {
        var v = +i.value; sum += v;
        i.closest("label").querySelector("output").textContent = v + "%";
        if (!low || v < +low.value) low = i;
      });
      var avg = Math.round(sum / ins.length);
      num.textContent = avg + "%";
      fg.style.strokeDashoffset = C * (1 - avg / 100);
      nx.innerHTML = avg === 100 ? "<b>Hammasi tayyor.</b> Ariza topshirishingiz mumkin." : "<b>Keyingi qadam:</b> " + low.getAttribute("data-next");
    }
    ins.forEach(function (i) { i.addEventListener("input", upd); });
    upd();
  }

  /* 3d. Qabuldan keyin */
  var qk = $("[data-qk]");
  if (qk) {
    var qb = $$("button", qk), qm = $("[data-qk-msg]");
    qb.forEach(function (b) {
      b.addEventListener("click", function () {
        b.setAttribute("aria-pressed", b.getAttribute("aria-pressed") === "true" ? "false" : "true");
        var n = qb.filter(function (x) { return x.getAttribute("aria-pressed") === "true"; }).length;
        if (n === qb.length) { qm.textContent = "Chamadonni yigʻishingiz mumkin. Oq yoʻl!"; qm.className = "qk-msg ok"; snd("pick"); }
        else { qm.textContent = n + " / " + qb.length + " bajarildi"; qm.className = "qk-msg"; }
      });
    });
  }
})();
