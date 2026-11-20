# USA M0 v2 (2026-11-20): Bakalavr/Magistratura M0 v2 andozasi (4 qadam, javoblardan baho va reja).
# Bir marta ishga tushiriladi: src/bachelor-lab-m0.page.html qobigʻi (head, CSS, darvoza) olinadi,
# USA matni va JS qoʻyiladi → src/usa-lab-m0.page.html. Keyin page.html toʻgʻridan-toʻgʻri tahrirlanadi.
#   python3 tools/modules/usa/m0_v2.py && python3 tools/modules/build.py usa-lab-m0
# Matn bu faylda YANGI alifboda; conv() manba alifbosiga (oʻ, gʻ U+02BB, sh, ch, ʼ U+02BC) oʻtkazadi.
import pathlib

SRC = pathlib.Path(__file__).resolve().parents[1] / "src"
B = (SRC / "bachelor-lab-m0.page.html").read_text(encoding="utf-8")
MAP = {"ö": "oʻ", "Ö": "Oʻ", "ğ": "gʻ", "Ğ": "Gʻ", "ş": "sh", "Ş": "Sh", "ç": "ch", "Ç": "Ch"}


def conv(t):
    return "".join(MAP.get(c, c) for c in t.replace("'", "ʼ"))


head = B[:B.index("<header class=\"top\">")]
head = head.replace("<title>M0: sizning bakalavr rejangiz · Bakalavr dasturi · Kompas Lab</title>",
                    conv("<title>M0: AQŞga öqiş rejangiz · USA dasturi · Kompas Lab</title>"))
head = head.replace('<meta name="description" content="Bakalavr dasturi bepul M0: 4 ta savolga javob bering va 12 daqiqada shaxsiy bahongiz, ariza rejangiz va birinchi vazifangizni oling.">',
                    conv('<meta name="description" content="USA dasturi bepul M0: 4 ta savolga javob bering va 12 daqiqada AQŞga borish yölingiz, bahongiz, rejangiz va birinçi vazifangizni oling.">'))
gate_start = B.index("<div class=\"toast\" id=\"toast\"")
js_start = B.index("<script>\n// ── Bakalavr M0 v2")
tail_scripts = B[gate_start:js_start]
tail_scripts = tail_scripts.replace('var RET = "bachelor-lab-m0.html";', 'var RET = "usa-lab-m0.html";')
tail_scripts = tail_scripts.replace("Bakalavr dasturi M0 bepul.", "USA dasturi M0 bepul.")
end = B[B.index("<style>.kp-wm"):]

BODY = r'''<header class="top">
  <div class="wrap">
    <a class="logo" href="usa-lab.html"><span class="klogo klogo-sm"><img class="klogo-b" src="img/brand/logo-base.webp" alt="" width="128" height="128"><img class="klogo-a" src="img/brand/logo-arrow.webp" alt="" width="128" height="128"></span>Kompas Lab <small>· AQŞ rejasi</small></a>
    <div class="xp" aria-live="polite">
      <span class="who" id="who"></span>
      <span class="lvl" id="lvl"></span>
      <span class="xp-pill" id="xpPill" hidden><img src="img/3d/bulb.webp" width="160" height="160" alt=""><span id="xpN">0</span>&nbsp;XP</span>
    </div>
  </div>
  <div class="xp-bar"><i id="xpBar"></i></div>
</header>

<div class="gate" id="gate">
  <div class="gate-c">
    <img class="float" src="img/3d/lock.webp" width="160" height="160" alt="">
    <h1 id="gateT">Bir soniya…</h1>
    <p id="gateP">Hisobingiz tekşirilmoqda.</p>
    <div id="gateA" hidden>
      <a class="btn btn-p" href="register.html" data-ret>Bepul röyxatdan ötiş</a>
      <a class="btn btn-g" href="login.html" data-ret>Kiriş</a>
      <small>Reja tuziş bepul. Röyxatdan ötgaç, şu sahifaga qaytasiz.</small>
    </div>
  </div>
</div>

<main data-kword="Qadam" data-kyakun="Natija: yöl, baho va reja" data-yakun-meta="Sizning yölingiz, bahongiz, rejangiz va I bosqiç vazifalari">
<div class="wrap">

  <div class="hero">
    <div class="hero-g">
      <div>
        <div class="crumb"><a href="index.html">Kompas Lab</a> · <a href="usa-lab.html">USA dasturi</a> · Modul 0</div>
        <span class="badge">Bepul · 12 daqiqa</span>
        <h1><span class="nb">AQŞga öqişga borish</span> <span class="nb">rejangizni</span> <span class="nb">12 daqiqada tuzamiz</span></h1>
        <p class="lead"><span class="ln"><b>4 ta savol</b>, ~12 daqiqa.</span><span class="ln"><span class="nb">Natijada: <b>Sizga oçiq yöl</b>,</span> <span class="nb"><b>bahongiz</b> va <b>bosqiçma-bosqiç rejangiz</b>.</span></span><span class="ln"><i>Parvoz uzoq, reja qisqa.</i></span></p>
        <div class="facts"><span class="fact"><b>4</b> savol</span><span class="fact">~<b>12</b> daqiqa</span><span class="fact">Natija: <b>yöl va reja</b></span></div>
        <p class="hint"><span class="ln">Javoblaringiz hisobingizda saqlanadi, <span class="nb">Kompas Lab jamoasi ularni köra oladi.</span></span><span class="ln">Tayyor rejani <b>oilangizga</b> yuboriş mumkin.</span></p>
      </div>
      <img class="hero-art float" src="img/3d/usa.webp" width="160" height="160" alt="">
    </div>
    <div class="kv" data-kvideo="l0"></div>
  </div>

  <nav class="map" aria-hidden="true" hidden><a class="node" href="#l1" data-node="l1"><span class="dot">1</span>Muddat</a><a class="node" href="#l2" data-node="l2"><span class="dot">2</span>Yöl</a><a class="node" href="#l3" data-node="l3"><span class="dot">3</span>Tayyorgarlik</a><a class="node" href="#l4" data-node="l4"><span class="dot">4</span>Pul</a></nav>

  <section id="darslar">
    <h2>Sizni nima kutadi</h2>
    <p class="sub">Har qadam 2–3 daqiqa.</p>
    <div class="lessons">

      <!-- QADAM 1 -->
      <article class="lesson" id="l1" data-lesson="l1">
        <button class="l-head" type="button" aria-expanded="false">
          <span class="l-ic"><img src="img/3d/calendar.webp" width="160" height="160" alt="" loading="lazy"><span class="ok">✓</span></span>
          <span><span class="l-n">Dars 0.1</span><span class="l-t" style="display:block">Qaçon öqişni boşlaysiz?</span>
            <span class="l-m"><span class="tag">2 daqiqa</span><span class="tag">Natija: neça hafta bor</span><span class="tag xp">+50 XP</span></span></span>
          <span class="chev">▾</span>
        </button>
        <div class="l-body">
          <div class="panel">
            <div class="prog"><span>1 / 4</span><i><b style="width:25%"></b></i><span>~10 daqiqa qoldi</span></div>
            <div class="q">
              <h3>AQŞda qaçon öqişni boşlamoqçisiz?</h3>
              <div class="chips two" data-one="start"><button type="button" class="chip" data-v="2027k" aria-pressed="false">2027 kuzi</button><button type="button" class="chip" data-v="2028k" aria-pressed="false">2028 kuzi</button><button type="button" class="chip" data-v="2029k" aria-pressed="false">2029 kuzi</button><button type="button" class="chip" data-v="x" aria-pressed="false">Hali bilmayman</button></div>
            </div>
            <div class="q">
              <h3>Hozir qayerdasiz?</h3>
              <div class="chips two" data-one="stage"><button type="button" class="chip" data-v="sch" aria-pressed="false">Maktab, litsey yoki kollej</button><button type="button" class="chip" data-v="u12" aria-pressed="false">Universitet, 1–2 kurs</button><button type="button" class="chip" data-v="u34" aria-pressed="false">Universitet, 3–4 kurs</button><button type="button" class="chip" data-v="g0" aria-pressed="false">Bitirganman, iş tajribasi 2 yildan kam</button><button type="button" class="chip" data-v="g2" aria-pressed="false">Bitirganman, 2+ yil iş tajribasi</button></div>
            </div>
            <div class="q">
              <h3>Aniq ariza muddatini bilasizmi?</h3>
              <p class="qs">Bilmasangiz, böş qoldiring: taxminiy sanani özimiz qöyamiz.</p>
              <div class="in-row"><input type="date" id="dlDate" aria-label="Ariza muddati"></div>
            </div>
            <div class="fb" id="fb1" role="status"></div>
            <details class="more"><summary>Qaysi sanadan hisoblaymiz?</summary><p>Reja eng erta ariza muddatidan orqaga hisoblanadi va 4 hafta zaxira qoladi. AQŞda yagona muddat yöq: har universitet va dastur öz sanasini qöyadi. Siz aniq sana kiritmasangiz, taxminiy sana qöyiladi: bakalavr uçun öqiş yilining 1-yanvari, magistratura va PhD uçun oldingi yilning 1-dekabri. Fulbright uçun ötgan siklning muddati 30.06.2026 bölgan (<a href="https://uz.usembassy.gov/fulbright-foreign-student-program/" target="_blank" rel="noopener">AQŞ elçixonasi</a>), Global UGRAD uçun oxirgi eʼlon qilingan muddat 15.12.2024 (<a href="https://uz.usembassy.gov/global-undergraduate-exchange-program/" target="_blank" rel="noopener">AQŞ elçixonasi</a>). 20.11.2026 holatiga ikkalasining yangi sikli eʼlon qilinmagan. Aniq sanani universitet yoki dastur sahifasidan oling.</p></details>
            <div class="kv" data-kvideo="l1"></div>
          </div>
          <div class="l-foot"><span class="hint" data-hint>Ikkita savolga javob bering.</span><button class="btn btn-p" type="button" data-complete="l1" data-xp="50">Keyingi qadam →</button></div>
        </div>
      </article>

      <!-- QADAM 2 -->
      <article class="lesson" id="l2" data-lesson="l2">
        <button class="l-head" type="button" aria-expanded="false">
          <span class="l-ic"><img src="img/3d/compass.webp" width="160" height="160" alt="" loading="lazy"><span class="ok">✓</span></span>
          <span><span class="l-n">Dars 0.2</span><span class="l-t" style="display:block">AQŞga qaysi yöl bilan borasiz?</span>
            <span class="l-m"><span class="tag">3 daqiqa</span><span class="tag">Natija: sizga oçiq yöl</span><span class="tag xp">+50 XP</span></span></span>
          <span class="chev">▾</span>
        </button>
        <div class="l-body">
          <div class="panel">
            <div class="prog"><span>2 / 4</span><i><b style="width:50%"></b></i><span>~8 daqiqa qoldi</span></div>
            <div class="q">
              <h3>Nimaga topşirasiz?</h3>
              <div class="chips col" data-one="route"><button type="button" class="chip" data-v="bak" aria-pressed="false">Bakalavr: töliq 4 yillik daraja</button><button type="button" class="chip" data-v="ugrad" aria-pressed="false">Bir semestr almaşinuv (Global UGRAD)</button><button type="button" class="chip" data-v="mag" aria-pressed="false">Magistratura</button><button type="button" class="chip" data-v="phd" aria-pressed="false">PhD</button><button type="button" class="chip" data-v="x" aria-pressed="false">Hali aniq emas</button></div>
              <div class="fb warn" id="fbRoute" role="status"></div>
            </div>
            <div class="q">
              <h3>Qaysi sohada?</h3>
              <div class="in-row"><input type="text" id="field" data-suggest="field" placeholder="Masalan: Informatika, Geologiya, Iqtisodiyot" aria-label="Soha" autocomplete="off"></div>
              <div class="chips"><button type="button" class="chip" id="fieldX" aria-pressed="false">Hali bilmayman</button></div>
            </div>
            <div class="fb" id="fb2" role="status"></div>
            <details class="more"><summary>Bu yöllar qanday farq qiladi</summary><p>Bakalavr va magistratura F-1 talaba vizasi bilan, UGRAD va Fulbright J-1 almaşinuv vizasi bilan. Hukumat pulidagi J-1 dasturidan keyin 2 yil vatanda yaşaş talabi bor. UGRAD diplom bermaydi: bu Özbekistonda öqiyotgan bakalavr talabasi uçun bir semestr. Fulbright Özbekiston uçun magistratura va kamida 2 yillik iş tajribasini söraydi. Batafsil M5 va M6 da.</p></details>
            <div class="kv" data-kvideo="l2"></div>
          </div>
          <div class="l-foot"><span class="hint" data-hint>Ikkita savolga javob bering.</span><button class="btn btn-p" type="button" data-complete="l2" data-xp="50">Keyingi qadam →</button></div>
        </div>
      </article>

      <!-- QADAM 3 -->
      <article class="lesson" id="l3" data-lesson="l3">
        <button class="l-head" type="button" aria-expanded="false">
          <span class="l-ic"><img src="img/3d/scroll.webp" width="160" height="160" alt="" loading="lazy"><span class="ok">✓</span></span>
          <span><span class="l-n">Dars 0.3</span><span class="l-t" style="display:block">Arizangiz uçun nimalar tayyor?</span>
            <span class="l-m"><span class="tag">3 daqiqa</span><span class="tag">Natija: birinçi yetişmaydigan qism</span><span class="tag xp">+50 XP</span></span></span>
          <span class="chev">▾</span>
        </button>
        <div class="l-body">
          <div class="panel">
            <div class="prog"><span>3 / 4</span><i><b style="width:75%"></b></i><span>~5 daqiqa qoldi</span></div>
            <div class="q">
              <h3>Baholaringiz qanday?</h3>
              <p class="qs">Oxirgi 2 yildagi attestat, tabel yoki diplom ilovasi.</p>
              <div class="chips two" data-one="grades"><button type="button" class="chip" data-v="a" aria-pressed="false">Aʼlo</button><button type="button" class="chip" data-v="y" aria-pressed="false">Yaxşi</button><button type="button" class="chip" data-v="o" aria-pressed="false">Örta</button><button type="button" class="chip" data-v="x" aria-pressed="false">Aytişim qiyin</button></div>
            </div>
            <div class="q">
              <h3>Nimalar tayyor?</h3>
              <div class="doc"><b>Ingliz tili sertifikati <small>TOEFL, IELTS yoki universitet qabul qiladigan boşqa test</small></b><div class="chips" data-doc="lang"><button type="button" class="chip" data-v="2" aria-pressed="false">Bor</button><button type="button" class="chip" data-v="1" aria-pressed="false">Tayyorlanyapman</button><button type="button" class="chip" data-v="0" aria-pressed="false">Yöq</button></div></div>
              <div class="doc"><b>SAT yoki GRE <small>talab qilinişini universitet sahifasidan tekşirasiz</small></b><div class="chips" data-doc="test"><button type="button" class="chip" data-v="2" aria-pressed="false">Bor yoki kerak emas</button><button type="button" class="chip" data-v="1" aria-pressed="false">Tayyorlanyapman</button><button type="button" class="chip" data-v="0" aria-pressed="false">Bilmayman</button></div></div>
              <div class="doc"><b>Tavsiya xati <small>öqituvçi yoki rahbaringiz yozadi</small></b><div class="chips" data-doc="ref"><button type="button" class="chip" data-v="2" aria-pressed="false">Kelişilgan</button><button type="button" class="chip" data-v="1" aria-pressed="false">Söramoqçiman</button><button type="button" class="chip" data-v="0" aria-pressed="false">Yöq</button></div></div>
              <div class="doc"><b>Inşo yoki maqsad bayonnomasi <small>Siz haqingizda 1 sahifa</small></b><div class="chips" data-doc="ess"><button type="button" class="chip" data-v="2" aria-pressed="false">Bor</button><button type="button" class="chip" data-v="1" aria-pressed="false">Yozyapman</button><button type="button" class="chip" data-v="0" aria-pressed="false">Yöq</button></div></div>
            </div>
            <div class="q">
              <h3>30 soniyalik sinov: qaysi universitet işonçli?</h3>
              <div class="game" data-game="0" data-a="x"><p>"Sayt .com da, «Kafolatli qabul, I-20 3 kunda» deb yozilgan."</p><div class="chips two"><button type="button" class="chip" data-v="i" aria-pressed="false">Işonçli</button><button type="button" class="chip" data-v="x" aria-pressed="false">Xavfli</button></div><div class="fb" role="status"><b>Xavfli.</b> Kafolat va şoşiltiriş birinçi qizil bayroq. Pul tölaşdan oldin akkreditatsiya va SEVP ni tekşirasiz (M1.2).</div></div>
              <div class="game" data-game="1" data-a="i"><p>"Muassasa CHEA bazasida bor va DHS ning SEVP qidiruvida çiqadi."</p><div class="chips two"><button type="button" class="chip" data-v="i" aria-pressed="false">Işonçli</button><button type="button" class="chip" data-v="x" aria-pressed="false">Xavfli</button></div><div class="fb" role="status"><b>Işonçli.</b> Akkreditatsiya diplomni, SEVP esa I-20 va talaba vizasini körsatadi. Narx va yordamni keyin alohida tekşirasiz.</div></div>
            </div>
            <div class="fb" id="fb3" role="status"></div>
            <div class="kv" data-kvideo="l3"></div>
          </div>
          <div class="l-foot"><span class="hint" data-hint>Baholar va har qatorga javob bering.</span><button class="btn btn-p" type="button" data-complete="l3" data-xp="50">Keyingi qadam →</button></div>
        </div>
      </article>

      <!-- QADAM 4 -->
      <article class="lesson" id="l4" data-lesson="l4">
        <button class="l-head" type="button" aria-expanded="false">
          <span class="l-ic"><img src="img/3d/money.webp" width="160" height="160" alt="" loading="lazy"><span class="ok">✓</span></span>
          <span><span class="l-n">Dars 0.4</span><span class="l-t" style="display:block">Oilangiz yiliga qança bera oladi?</span>
            <span class="l-m"><span class="tag">2 daqiqa</span><span class="tag">Natija: pul holatingiz</span><span class="tag xp">+50 XP</span></span></span>
          <span class="chev">▾</span>
        </button>
        <div class="l-body">
          <div class="panel">
            <div class="prog"><span>4 / 4</span><i><b style="width:100%"></b></i><span>~2 daqiqa qoldi</span></div>
            <div class="q">
              <h3>Oilangiz öqiş va yaşaşga yiliga qança ajrata oladi?</h3>
              <p class="qs">AQŞ dollarida, taxminan. I-20 uçun universitet birinçi yil pulini hujjat bilan söraydi.</p>
              <div class="chips col" data-one="fund"><button type="button" class="chip" data-v="a40" aria-pressed="false">40 000 dollardan köp</button><button type="button" class="chip" data-v="a15" aria-pressed="false">15 000 – 40 000 dollar</button><button type="button" class="chip" data-v="a5" aria-pressed="false">5 000 – 15 000 dollar</button><button type="button" class="chip" data-v="a0" aria-pressed="false">5 000 dollardan kam</button><button type="button" class="chip" data-v="x" aria-pressed="false">Oilam bilan hali gaplaşmaganman</button></div>
            </div>
            <div class="fb" id="fb4" role="status"></div>
            <details class="more"><summary>Nega aynan yillik summa?</summary><p>Xalqaro talabaga federal yordam yopiq (AQŞ Taʼlim vazirligi). Universitet yordam berişdan oldin oilangiz qança tölay olişini hisoblaydi, I-20 esa birinçi yil narxini hujjat bilan söraydi. Şuning uçun yöl oila summasidan boşlab tanlanadi (M2).</p></details>
          </div>
          <div class="l-foot"><span class="hint" data-hint>Bitta variantni tanlang.</span><button class="btn btn-p" type="button" data-complete="l4" data-xp="50">Natijamni körsat →</button></div>
        </div>
      </article>
    </div>
  </section>

  <section id="vositalar" data-yakun-title="Sizning natijangiz">
    <div id="natija">
      <h2>Sizning natijangiz</h2>
      <div class="rcard">
        <div class="st">Sizning yölingiz</div>
        <div class="rt" id="rRoute" style="font-weight:800;margin:4px 0 2px"></div>
        <div class="lv" id="rLv">…</div>
        <div class="sc"><b id="rSc">0</b> / 100 · <span id="rWk"></span></div>
        <div class="bars" id="rBars"></div>
        <details class="more" style="text-align:left"><summary>Bu ball qanday hisoblandi?</summary><p>Ball faqat sizning javoblaringizdan olinadi: vaqt, yöl, baholar, ingliz tili, hujjatlar, pul. U qabul yoki viza ehtimolini bildirmaydi, faqat qayerdan boşlaşni körsatadi. "Yöl" 70 dan oşmaydi: universitet röyxati I bosqiçda tuziladi.</p></details>
        <div class="kv" data-kvideo="res"></div>
      </div>
      <div class="rtxt" id="rTxt"></div>
      <div class="fb warn rmiss" id="rMiss"></div>

      <h2 style="margin-top:28px">Sizning rejangiz</h2>
      <p class="sub" id="rSpan"></p>
      <ol class="ph" id="rPh"></ol>
      <div class="row" style="margin-top:12px"><button class="btn btn-g" type="button" id="copyBtn">Rejani nusxalaş</button></div>
      <p class="hint">Nusxani oilangizga yuboring: yöl, sanalar va pul savoli bir joyda.</p>
    </div>
  </section>

  <section id="qaror">
    <div class="tasks">
      <h3>Sizning I bosqiç vazifalaringiz</h3>
      <div class="tprog"><i><b></b></i><span>Rejangiz 20% tayyor</span></div>
      <ol class="tl" id="rTasks"></ol>
      <p class="rnote">Qulf belgisi bor vazifalar USA dasturining I bosqiçida (M1–M2). Har biriga alohida dars va vosita bor.</p>
    </div>
    <div class="cta">
      <a class="btn btn-p" href="tolov.html?lab=usa-lab&amp;plan=monthly" data-snd="nav" id="ctaBtn">I bosqiçni boşlaş</a>
      <p class="hint"><span data-pm>99 000</span> söm · 1 ta bosqiç (30 kun). <a href="usa-lab-narxlar.html">Töliq dastur bilan soliştiriş</a></p>
      <p class="hint">18 yoşga tölmagan bölsangiz, obunani ota-onangiz rasmiylaştiradi.</p>
    </div>
    <div class="quote">
      <img src="img/3d/compass.webp" alt="" width="30" height="30">
      <div>
        <q>Men stipendiyani ikkinçi urinişda yutganman. Birinçi safar hujjatlar bor edi, lekin ular bitta hikoyaga ulanmagan edi. Bu reja şu xatoni qaytarmaslik uçun.</q>
        <small>Asosçi · University of Leeds doktoranti</small>
      </div>
    </div>
    <details class="more"><summary>Kompas Lab nima qiladi va nima qilmaydi</summary><p>Kompas Lab inşo va hujjatni sizning örningizga yozmaydi, qabul, yordam yoki vizani kafolatlamaydi va viza böyiça yuridik maslahat bermaydi. Siz darslar va vositalar yordamida özingiz tayyorlanasiz. Şartlar <a href="oferta.html">ommaviy ofertada</a>.</p></details>
  </section>
</div>
</main>

<footer>
  <div class="wrap">
    <a class="btn btn-g" href="usa-lab.html">← USA dasturi sahifasi</a>
  </div>
</footer>

'''

JS = r'''<script>
// ── USA M0 v2 (2026-11-20): 4 qadam, javoblardan yöl, baho va reja (Bakalavr M0 v2 andozasi) ──
(function () {
  var KEY = "kompas_usa_m0_v1", LAB = "usa-lab";
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var S = { xp: 0, done: {}, seen: {}, open: "l1", ans: {} };
  try { var raw = localStorage.getItem(KEY); if (raw) { var o = JSON.parse(raw); for (var k in o) S[k] = o[k]; } } catch (e) {}
  // Eski 6 darslik M0 holati: javobsiz "done" belgilari yangi qadamlarga mos emas
  if (S.v !== 2) { S.v = 2; S.xp = 0; S.done = {}; S.seen = {}; S.ans = {}; }
  if (!S.ans || typeof S.ans !== "object") S.ans = {};
  if (!S.done) S.done = {};
  if (!S.seen) S.seen = {};
  var A = S.ans;
  if (!A.docs) A.docs = {};
  if (!A.game) A.game = {};
  function save() { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {} }
  function nf(n) { return String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, " "); }
  function $(id) { return document.getElementById(id); }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", "\"": "&quot;" }[c]; }); }
  var view = document.body.getAttribute("data-kview") || "";
  var DAY = 86400000;

  var MAX = 250, LEVELS = [[1, "1-daraja: Kuzatuvçi"], [80, "2-daraja: Izlanuvçi"], [170, "3-daraja: Kaşfiyotçi"], [250, "Rejangiz tayyor"]];
  function renderXp(bump) {
    var pill = $("xpPill");
    pill.style.display = S.xp ? "" : "none";
    $("xpN").textContent = S.xp;
    $("xpBar").style.width = Math.min(100, S.xp / MAX * 100) + "%";
    var l = ""; LEVELS.forEach(function (x) { if (S.xp >= x[0]) l = x[1]; });
    $("lvl").textContent = l;
    if (bump) { pill.classList.remove("pop"); void pill.offsetWidth; pill.classList.add("pop"); }
  }
  var tt;
  function toast(msg, img) {
    if (window.KSfx && img === "lock") KSfx.play("warn");
    $("toastT").textContent = msg; $("toastImg").src = "img/3d/" + (img || "bulb") + ".webp";
    var t = $("toast"); t.classList.add("show"); clearTimeout(tt); tt = setTimeout(function () { t.classList.remove("show"); }, 2600);
  }
  function confetti() {
    if (window.KSfx) KSfx.play("win");
    if (reduce) return;
    var colors = ["#c4622d", "#2d4a3e", "#d9a441", "#1a7a4a", "#e9a27a"];
    for (var i = 0; i < 46; i++) {
      var c = document.createElement("i"); c.className = "cf";
      c.style.left = Math.random() * 100 + "vw"; c.style.background = colors[i % colors.length];
      c.style.animationDuration = (1.6 + Math.random() * 1.6) + "s"; c.style.animationDelay = Math.random() * .3 + "s";
      document.body.appendChild(c); setTimeout(function (el) { el.remove(); }.bind(null, c), 3600);
    }
  }
  function award(id, xp, msg, img) {
    if (S.done[id]) return false;
    S.done[id] = true; var x0 = S.xp; S.xp = Math.min(MAX, S.xp + xp); if (window.KSfx) KSfx.gain(x0, S.xp); save(); renderXp(true);
    if (msg) toast((xp ? "+" + xp + " XP · " : "") + msg, img);
    return true;
  }

  var lessons = document.querySelectorAll(".lesson");
  lessons.forEach(function (l) {
    var p = l.querySelector(".panel"); if (p) p.classList.add("on");
    if (view === "lesson" && document.body.getAttribute("data-klesson") === l.id) S.seen[l.id] = [0];
    l.querySelector(".l-head").addEventListener("click", function () {
      var on = !l.classList.contains("open");
      lessons.forEach(function (x) { x.classList.remove("open"); });
      l.classList.toggle("open", on);
    });
  });

  function pressed(box, fn) { box.querySelectorAll(".chip").forEach(function (c) { c.setAttribute("aria-pressed", fn(c.getAttribute("data-v")) ? "true" : "false"); }); }
  document.querySelectorAll("[data-one]").forEach(function (box) {
    var k = box.getAttribute("data-one");
    box.querySelectorAll(".chip").forEach(function (c) {
      c.addEventListener("click", function () { A[k] = c.getAttribute("data-v"); if (window.KSfx) KSfx.play("tab"); save(); renderAll(); });
    });
  });
  document.querySelectorAll("[data-doc]").forEach(function (box) {
    var k = box.getAttribute("data-doc");
    box.querySelectorAll(".chip").forEach(function (c) {
      c.addEventListener("click", function () { A.docs[k] = +c.getAttribute("data-v"); if (window.KSfx) KSfx.play("tab"); save(); renderAll(); });
    });
  });
  document.querySelectorAll("[data-game]").forEach(function (g) {
    var k = g.getAttribute("data-game");
    g.querySelectorAll(".chip").forEach(function (c) {
      c.addEventListener("click", function () { A.game[k] = c.getAttribute("data-v"); save(); renderAll(); });
    });
  });
  var fld = $("field"), fx = $("fieldX");
  if (fld) {
    fld.value = A.field || "";
    var ft; fld.addEventListener("input", function () { clearTimeout(ft); ft = setTimeout(function () { A.field = fld.value.trim(); if (A.field) A.fieldX = false; save(); renderAll(); }, 350); });
    fld.addEventListener("change", function () { A.field = fld.value.trim(); if (A.field) A.fieldX = false; save(); renderAll(); });
  }
  if (fx) fx.addEventListener("click", function () { A.fieldX = !A.fieldX; if (A.fieldX) { A.field = ""; if (fld) fld.value = ""; } save(); renderAll(); });
  var dd = $("dlDate");
  if (dd) {
    dd.value = A.date || "";
    dd.addEventListener("change", function () { A.date = dd.value; save(); renderAll(); });
  }

  // ── Sana hisobi (taxminiy; aniq sana universitet yoki dastur sahifasidan) ──
  function today() { var t = new Date(); t.setHours(0, 0, 0, 0); return t; }
  function iso(d) { return d.getFullYear() + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2); }
  function D(s) { return new Date(s + "T00:00:00"); }
  var Y = { "2027k": 2027, "2028k": 2028, "2029k": 2029 };
  var passed = false;
  function deadline() {
    passed = false;
    if (A.date) return D(A.date);
    if (!A.start) return null;
    var y = Y[A.start];
    if (!y) return new Date(today().getTime() + 52 * 7 * DAY);
    var r = A.route, d;
    if (r === "mag" && A.fund === "a0") d = D((y - 1) + "-06-30");      // Fulbright: ötgan sikl 30.06.2026 (faraz)
    else if (r === "mag" || r === "phd") d = D((y - 1) + "-12-01");
    else if (r === "ugrad") d = D((y - 1) + "-12-15");                   // oxirgi eʼlon: 15.12.2024
    else d = D(y + "-01-01");
    if (d <= today()) { passed = true; }
    return d;
  }
  function weeks() { var d = deadline(); return d ? Math.max(0, Math.round((d - today()) / DAY / 7)) : null; }
  function prepWeeks() { var w = weeks(); return w == null ? null : Math.max(0, w - 4); }
  function fmt(d) { var m = ["yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avgust", "sentabr", "oktabr", "noyabr", "dekabr"]; return d.getDate() + "-" + m[d.getMonth()] + ", " + d.getFullYear(); }
  function short(d) { return ("0" + d.getDate()).slice(-2) + "." + ("0" + (d.getMonth() + 1)).slice(-2) + "." + d.getFullYear(); }

  var ROUTE = { bak: "Bakalavr (F-1)", ugrad: "Global UGRAD (J-1, bir semestr)", mag: "Magistratura (F-1 yoki Fulbright J-1)", phd: "PhD (F-1, kafedra moliyasi)", x: "Yöl hali aniq emas" };
  var DOCS = { lang: "ingliz tili sertifikati", test: "SAT yoki GRE", ref: "tavsiya xati", ess: "inşo yoki maqsad bayonnomasi" };
  var DOC_KEYS = ["lang", "test", "ref", "ess"];
  var DOC_ORDER = ["lang", "ref", "test", "ess"];
  var DIM = ["Vaqt", "Yöl", "Baholar", "Ingliz tili", "Hujjatlar", "Pul"];
  function eligible() {
    var r = A.route, s = A.stage;
    if (r === "ugrad") return s === "u12" ? 1 : s === "u34" ? 0.5 : 0;   // oxirgi kurs mos emas; kamida 1 yil qoliği kerak
    if (r === "mag" || r === "phd") return (s === "g0" || s === "g2" || s === "u34") ? 1 : 0;
    if (r === "bak") return s === "sch" ? 1 : 0.5;
    return 0.5;
  }
  function answered(id) {
    if (id === "l1") return !!(A.start || A.date) && !!A.stage;
    if (id === "l2") return !!A.route && !!(A.field || A.fieldX);
    if (id === "l3") return DOC_KEYS.every(function (k) { return A.docs[k] != null; }) && !!A.grades;
    if (id === "l4") return !!A.fund;
    return false;
  }
  function moneyScore() {
    var f = A.fund, r = A.route;
    if (r === "ugrad") return f === "x" ? 50 : 75;
    if (r === "phd") return { a40: 85, a15: 75, a5: 65, a0: 60, x: 40 }[f] || 40;
    if (r === "mag") return { a40: 85, a15: 55, a5: 40, a0: 35, x: 15 }[f] || 15;
    return { a40: 85, a15: 60, a5: 40, a0: 25, x: 15 }[f] || 15;
  }
  function scores() {
    var pw = prepWeeks(), v = [];
    v[0] = pw == null ? 20 : passed ? 15 : pw >= 32 ? 90 : pw >= 24 ? 70 : pw >= 14 ? 45 : 20;
    var e = eligible(), fk = !!A.field;
    v[1] = !A.route || A.route === "x" ? 20 : e === 0 ? 25 : e === 1 && fk ? 70 : 45;
    v[2] = { a: 85, y: 65, o: 40, x: 35 }[A.grades] || 35;
    v[3] = A.docs.lang === 2 ? 85 : A.docs.lang === 1 ? 45 : 15;
    var s = 0; ["test", "ref", "ess"].forEach(function (k) { s += +A.docs[k] || 0; }); v[4] = Math.round(s / 6 * 100);
    v[5] = moneyScore();
    return v;
  }
  function avg(v) { return Math.round(v.reduce(function (a, b) { return a + b; }, 0) / v.length); }
  function level(a) { return a >= 70 ? "Topşirişga yaqin" : a >= 45 ? "Yarim yölda" : "Yöl boşida"; }
  function order(v) { return v.map(function (x, i) { return { v: x, i: i }; }).sort(function (a, b) { return a.v - b.v || a.i - b.i; }); }
  function firstMissing(keys) { for (var i = 0; i < keys.length; i++) if (!(+A.docs[keys[i]] === 2)) return keys[i]; return null; }

  function fb(id, html, warn) { var e = $(id); if (!e) return; e.innerHTML = html || ""; e.classList.toggle("show", !!html); if (warn != null) e.classList.toggle("warn", !!warn); }
  function render1() {
    var w = weeks(), pw = prepWeeks();
    if (w == null) { fb("fb1", ""); return; }
    if (passed) { fb("fb1", "Bu yil uçun taxminiy muddat (" + fmt(deadline()) + ") ötib ketgan. Bir yil keyingi startni tanlang yoki dastur sahifasidan aniq sanani kiriting.", true); return; }
    var est = A.date ? "" : " Sana taxminiy: aniq sanani universitet yoki dastur sahifasidan topib, yuqoriga kiriting.";
    var msg = pw >= 32 ? "Bu bemalol yetadi." : pw >= 24 ? "Yetadi, agar hozir boşlasangiz." : pw >= 14 ? "Tiğiz: testni qayta topşirişga vaqt kam qoladi." : "Juda tiğiz. Rejada keyingi mavsum ham körsatiladi.";
    fb("fb1", "Ariza muddatigaça <b>" + w + " hafta</b> bor: " + pw + " hafta tayyorgarlik va 4 hafta zaxira. " + msg + "<br><small>Taxminiy ariza muddati: " + fmt(deadline()) + "." + est + "</small>", pw < 14);
  }
  function render2() {
    var r = A.route, s = A.stage, m = "";
    if (r === "ugrad" && s === "u34") m = "UGRAD dan keyin öz universitetingizda kamida bir öquv yili qoliği kerak. 3-kursda bölsangiz, sikl vaqtini tekşiring; oxirgi kurs talabasi ariza bera olmaydi.";
    else if (r === "ugrad" && s && s !== "u12") m = "Global UGRAD faqat Özbekistonda kunduzgi bakalavriatda öqiyotgan talabalar uçun. Sizga bakalavr yoki magistratura yöli mosroq.";
    else if ((r === "mag" || r === "phd") && s === "sch") m = "Magistratura va PhD uçun bakalavr diplomi kerak. Hozir sizga bakalavr yöli mos: uni tanlang yoki <a href=\"bachelor-lab.html\">Bakalavr dasturi</a>ni köring.";
    else if (r === "mag" && s === "g0") m = "Fulbright uçun kamida 2 yillik iş tajribasi kerak. Universitet yordami yoki kafedra moliyasi bilan magistratura ham mumkin (M7).";
    else if (r === "bak" && (s === "g0" || s === "g2")) m = "Bakalavr diplomingiz bölsa, magistratura yoki PhD yöli sizga köproq mos kelişi mumkin.";
    fb("fbRoute", m, true);
    if (fx) fx.setAttribute("aria-pressed", A.fieldX ? "true" : "false");
    if (!answered("l2")) { fb("fb2", ""); return; }
    var hint = { bak: "I va II bosqiç (M1–M4) siz uçun asosiy, keyin viza (M8).", ugrad: "Siz uçun asosiy modullar: M1 va M5, keyin viza (M8).", mag: "Siz uçun asosiy modullar: M1–M2, Fulbright (M6) va magistratura moliyasi (M7).", phd: "Siz uçun asosiy modullar: M1–M2, PhD moliyasi (M7) va viza (M8).", x: "M1–M2 hamma yöl uçun umumiy: yölni şu yerda aniqlaysiz." }[r];
    fb("fb2", "Sizning yölingiz: <b>" + esc(ROUTE[r]) + (A.field ? " · " + esc(A.field) : "") + "</b>. " + hint);
  }
  function render3() {
    document.querySelectorAll("[data-game]").forEach(function (g) {
      var k = g.getAttribute("data-game"), a = A.game[k];
      pressed(g, function (v) { return v === a; });
      var f = g.querySelector(".fb"); if (f) f.classList.toggle("show", a != null);
    });
    if (!answered("l3")) { fb("fb3", ""); return; }
    var have = 0; DOC_KEYS.forEach(function (k) { if (A.docs[k] === 2) have++; });
    var miss = firstMissing(DOC_ORDER), t = "4 tadan <b>" + have + " tasi</b> tayyor.";
    if (miss === "lang") t += " Birinçi yetişmaydigani: <b>ingliz tili sertifikati</b>. Imtihonga oldindan yoziliş kerak, ball yetmasa qayta topşirasiz.";
    else if (miss === "ref") t += " Birinçi yetişmaydigani: <b>tavsiya xati</b>. Uni boşqa odam yozadi, unga vaqt kerak.";
    else if (miss === "test") t += " Birinçi yetişmaydigani: <b>SAT yoki GRE</b>. Avval universitetingiz uni talab qilişini tekşiring: köp dasturda ixtiyoriy bölişi mumkin.";
    else if (miss) t += " Birinçi yetişmaydigani: <b>" + DOCS[miss] + "</b>.";
    else t += " Hammasi bor. Endi ularni har universitetga moslaş qoladi.";
    fb("fb3", t);
  }
  function render4() {
    if (!answered("l4")) { fb("fb4", ""); return; }
    var r = A.route, f = A.fund, t;
    if (f === "x") t = "Bu normal hol. Natijadagi rejani oilangizga körsating va şu hafta gaplaşing: AQŞ yöli aynan şu raqamdan boşlanadi.";
    else if (r === "ugrad") t = "UGRAD da aviabilet, öqiş, yaşaş va suğurtani dastur qoplaydi. Pul savoli sizga keyin, bakalavr yoki magistratura uçun kerak böladi.";
    else if (r === "phd") t = "AQŞda PhD köpinça kafedra paketi bilan: stipendiya va öqiş tölovidan ozod qiliş. Paketni soliştiriş M7 da.";
    else if (f === "a40") t = "Yaxşi. Universitetni yordam siyosatiga qaramay tanlaş mumkin; natija grantini baribir qidiring.";
    else if (r === "mag") t = f === "a0" ? "Bu summada sizga Fulbright yoki moliyalaştiradigan kafedra kerak. Rejadagi muddat Fulbright ning ötgan sikliga qarab qöyildi." : "Magistratura köpinça öz hisobidan. Sizga Fulbright, moliyalaştiradigan kafedra yoki natija granti kerak böladi (M6–M7).";
    else t = f === "a15" ? "Sizga natija grantlari va arzonroq yöllar (ikki yillik kollej, arzon hududlar) mos. Hisob M2 da." : "Sizga xalqaro talabaga ham töliq ehtiyojni qoplaydigan universitetlar kerak. Ular kam va tanlovli, şuning uçun parallel boşqa mamlakatni ham körib çiqing (M3).";
    fb("fb4", t);
  }
  var HINT = { l1: "Ikkita savolga javob bering.", l2: "Ikkita savolga javob bering.", l3: "Baholar va har qatorga javob bering.", l4: "Bitta variantni tanlang." };
  function renderSteps() {
    lessons.forEach(function (l) {
      var id = l.id, ok = answered(id), h = l.querySelector("[data-hint]");
      l.classList.toggle("done", !!S.done[id]);
      if (h) h.textContent = ok ? (S.done[id] ? "Javob saqlangan." : "Tayyor.") : HINT[id];
    });
  }

  function nextHref(id) { var n = +id.slice(1); return n < lessons.length ? LAB + "-m0-" + (n + 1) + ".html" : LAB + "-m0-yakun.html"; }
  document.querySelectorAll("[data-complete]").forEach(function (b) {
    b.addEventListener("click", function () {
      var id = b.getAttribute("data-complete");
      if (!answered(id)) { toast(HINT[id], "lock"); return; }
      if (S.done[id]) { location.href = nextHref(id); return; }
      award(id, +b.getAttribute("data-xp") || 50, "", "seedling");
      renderAll();
    });
  });

  var TODAY_TASK = [
    "Qiziqqan 3 ta universitet yoki dasturning rasmiy sahifasidan ariza muddatini toping. Eng yaqinini 1-qadamga kiriting: reja qayta hisoblanadi.",
    "AQŞ elçixonasining almaşinuv dasturlari sahifasini oçing va tanlagan yölingizga eng yaqin dasturning şartlarini öqing. Har şart yoniga «mos» yoki «mos emas» deb yozing.",
    "Oxirgi 2 yildagi baholaringizni bitta jadvalga yozing. AQŞ universiteti ularni transkript orqali köradi.",
    "TOEFL, IELTS yoki boşqa testni tanlang va eng yaqin imtihon sanasini test taşkilotining rasmiy saytidan toping.",
    "",
    "Oila bilan 15 daqiqa gaplaşing: yiliga öqiş va yaşaşga neça dollar ajrata olasiz? Raqamni yozing. I-20 aynan şu savoldan boşlanadi."
  ];
  var DOC_TASK = {
    test: "Közlagan 3 universitetingiz SAT yoki GRE ni talab qilişini qabul sahifasidan tekşiring: talab, ixtiyoriy yoki qabul qilinmaydi.",
    ref: "Sizni yaxşi taniydigan 2 ta öqituvçi yoki rahbarni tanlang. Bu hafta ulardan biridan rejangizni aytib beriş uçun 10 daqiqa vaqt söring.",
    ess: "Sizga eng köp taʼsir qilgan bitta kiçik voqeani 5 jumlada yozing. Bu inşoning xomaşyosi."
  };
  // I bosqiçdagi haqiqiy darslar (M1, M2)
  var P1 = ["M1.1 Universitet turlari", "M1.2 Universitet haqiqiymi?", "M1.3 AQŞ darajasi qanday tuzilgan", "M1.4 Sohangiz qayerda kuçli", "M2.1 Töliq narx qança", "M2.2 I-20 uçun pul dalili", "M2.3 Qaysi pul sizga oçiq"];
  var PH = [["I", "Tizim va pul", "Universitet tekşiruv kartasi va AQŞ pul xaritasi (M1–M2)"], ["II", "Bakalavr yordami", "Yordam beradigan universitetlar röyxati va yordam arizasi (M3–M4)"], ["III", "Davlat dasturlari", "Global UGRAD va Fulbright kartasi (M5–M6)"], ["IV", "Magistratura, PhD va viza", "Moliya paketi taqqoslaşi, viza va maqom röyxati (M7–M8)"]];
  var REL = { bak: [1, 1, 0, 1], ugrad: [1, 0, 1, 1], mag: [1, 0, 1, 1], phd: [1, 0, 0, 1], x: [1, 1, 1, 1] };
  function renderResult() {
    if (!$("rLv")) return;
    var miss = ["l1", "l2", "l3", "l4"].filter(function (id) { return !answered(id); });
    var mEl = $("rMiss");
    if (miss.length) {
      mEl.innerHTML = "Natija töliq emas. Javob berilmagan: " + miss.map(function (id) { return "<a href=\"" + LAB + "-m0-" + id.slice(1) + ".html\">" + id.slice(1) + "-qadam</a>"; }).join(", ") + ".";
      mEl.classList.add("show");
    } else { mEl.innerHTML = ""; mEl.classList.remove("show"); }
    var v = scores(), a = avg(v), o = order(v), low = [o[0].i, o[1].i];
    $("rRoute").textContent = ROUTE[A.route || "x"] + (A.field ? " · " + A.field : "");
    $("rLv").textContent = level(a);
    $("rSc").textContent = a;
    var w = weeks();
    $("rWk").textContent = w == null ? "sana hali yöq" : passed ? "bu yilgi muddat ötgan" : "ariza muddatigaça " + w + " hafta";
    $("rBars").innerHTML = v.map(function (x, i) {
      return "<div class=\"bar" + (low.indexOf(i) >= 0 ? " low" : "") + "\"><span>" + DIM[i] + "</span><i><b style=\"width:" + x + "%\"></b></i><em>" + x + "</em></div>";
    }).join("");
    var strong = o.slice().reverse().filter(function (x) { return x.v >= 65; }).slice(0, 2).map(function (x) { return DIM[x.i].toLowerCase(); });
    var md = firstMissing(["ref", "test", "ess"]);
    var lowName = low.map(function (i) { return i === 4 && md ? DOCS[md] : DIM[i].toLowerCase(); });
    var t = strong.length ? "<p>Sizning kuçli tomoningiz: <b>" + strong.join(" va ") + "</b>.</p>" : "<p>Hozirça hamma yönalişda iş bor. Bu normal: köpçilik şu holatdan boşlaydi.</p>";
    t += "<p>Birinçi yopiladigan joylar: <b>" + lowName.join(" va ") + "</b>.</p>";
    t += "<p>Sizga <b>I bosqiç</b> mos, çunki universitetni tekşiriş va oila summasini hisoblaş hamma yöl uçun birinçi qadam: qaysi universitet real ekanini aynan şu ikkisi körsatadi.</p>";
    $("rTxt").innerHTML = t;

    var dl = deadline(), t0 = today(), end = dl && !passed ? new Date(dl.getTime() - 28 * DAY) : null;
    var minEnd = new Date(t0.getTime() + 8 * 7 * DAY), tight = false;
    if (!end || end < minEnd) { tight = !!end; end = end && end > t0 ? end : minEnd; }
    var step = (end - t0) / 4, rel = REL[A.route || "x"];
    $("rSpan").textContent = (dl && !passed ? "Ariza muddati: " + fmt(dl) + ". Hammasi tayyor bölişi kerak sana: " + fmt(end) + "." : "Sana hali aniq emas, reja taxminiy.") + (tight ? " Vaqt juda tiğiz: keyingi mavsumni ham körib çiqing." : "");
    $("rPh").innerHTML = PH.map(function (p, k) {
      var a1 = new Date(t0.getTime() + step * k), a2 = new Date(t0.getTime() + step * (k + 1));
      return "<li" + (k === 0 ? " class=\"on\"" : "") + "><span class=\"n\">" + p[0] + "</span><span><b>" + p[1] + "</b><small>" + p[2] + "</small><small>" + short(a1) + " – " + short(a2) + (rel[k] ? "" : " · Sizning yölingiz uçun qöşimça") + "</small></span></li>";
    }).join("");

    var wi = low[0], task = wi === 4 ? DOC_TASK[md || "ref"] : TODAY_TASK[wi];
    var h = "<li class=\"free\"><span class=\"k\">1</span><span><b>Bugun qiling (bepul):</b> " + esc(task) + "<label><input type=\"checkbox\" id=\"taskDone\"" + (A.task ? " checked" : "") + "> Bajardim</label></span></li>";
    P1.forEach(function (x, k) { h += "<li class=\"lk\"><span class=\"k\">" + (k + 2) + "</span><span>" + esc(x) + "<img src=\"img/3d/lock.webp\" alt=\"qulf\" width=\"18\" height=\"18\"></span></li>"; });
    $("rTasks").innerHTML = h;
    var td = $("taskDone");
    if (td) td.addEventListener("change", function () { A.task = td.checked; save(); if (td.checked) toast("Zör. Birinçi vazifa bajarildi", "seedling"); });

    S.res = { avg: a, low: low, at: iso(t0) };
    if (!miss.length && award("dec", 50, "Rejangiz tayyor", "seedling")) setTimeout(confetti, 400);
    save();
  }
  var cb = $("copyBtn");
  if (cb) cb.addEventListener("click", function () {
    var txt = "AQŞda öqiş: mening rejam (Kompas Lab)\n" + $("rRoute").textContent + "\n" + $("rLv").textContent + ", " + $("rSc").textContent + "/100, " + $("rWk").textContent + "\n" + $("rTxt").innerText + "\n" + $("rSpan").textContent + "\n" +
      [].map.call(document.querySelectorAll("#rPh li"), function (li) { return li.innerText.replace(/\n+/g, " · "); }).join("\n");
    if (navigator.clipboard) navigator.clipboard.writeText(txt).then(function () { toast("Nusxalandi", "memo"); }, function () { prompt("Nusxalang:", txt); });
    else prompt("Nusxalang:", txt);
  });

  function renderAll() {
    document.querySelectorAll("[data-one]").forEach(function (box) { var k = box.getAttribute("data-one"); pressed(box, function (v) { return A[k] === v; }); });
    document.querySelectorAll("[data-doc]").forEach(function (box) { var k = box.getAttribute("data-doc"); pressed(box, function (v) { return A.docs[k] === +v; }); });
    render1(); render2(); render3(); render4(); renderSteps();
  }

  try {
    fetch("https://usxpkmbjrdllnitlzdpq.supabase.co/rest/v1/rpc/kompas_public_stats", {
      method: "POST",
      headers: { "Content-Type": "application/json", apikey: "%ANON%" },
      body: "{}"
    }).then(function (r) { return r.ok ? r.json() : null; }).then(function (d) {
      var p = d && d.prices && d.prices[LAB]; if (!p) return;
      if (p.m) document.querySelectorAll("[data-pm]").forEach(function (el) { el.textContent = nf(p.m); });
    }).catch(function () {});
  } catch (e) {}

  renderAll(); renderXp(false); save();
  if (view === "yakun") renderResult();
})();
</script>
'''

import re
anon = re.search(r'apikey: "([^"]+)"', B).group(1)
out = head + conv(BODY) + tail_scripts + conv(JS).replace("%ANON%", anon) + end
(SRC / "usa-lab-m0.page.html").write_text(out, encoding="utf-8")
print("yozildi: src/usa-lab-m0.page.html", len(out))
