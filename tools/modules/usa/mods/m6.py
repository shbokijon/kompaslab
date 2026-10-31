from common import EMB_FUL, EMB_FUL_EXP, FUL_IIE, HARVARD_212E, DOS_WAIVER, EMB_EXCH, HOL, STD

MOD = dict(
    title="Fulbright magistraturasi",
    desc="USA Lab M6: O'zbekiston uchun Fulbright Foreign Student Program — shartlar, ustuvor sohalar, tanlov bosqichlari, ariza tarkibi va halollik qoidalari, sikl kalendari, J-1 va 2 yillik vatanda yashash talabi. Natija: Fulbright muvofiqlik va reja kartasi.",
    lead="Fulbright O'zbekistondan AQShda magistratura uchun asosiy davlat stipendiyasi. Bu modulda dastur O'zbekiston uchun aynan nimani talab qilishini, tanlov qanday o'tishini va J-1 majburiyati kelajak rejangizga qanday ta'sir qilishini o'rganasiz.",
    hero="master", weeks="2", next="M7 Magistratura va PhD moliyasi", next_href="usa-lab-o.html?m=7",
    goals=[("shield", "Fulbright muvofiqlik xulosasi", "har shart: mos / tekshirish kerak / mos emas"),
           ("calendar", "Sikl kalendari", "e'lon, muddat, intervyu, testlar, safar"),
           ("compass", "J-1 qarori", "2 yillik talab va kelajak rejasi mosligi")],
    warn=f"Maqsad bayonnomasi, CV va tavsiya xatini yozish Master Lab M3–M5 da o'rgatiladi; bu modul ularni takrorlamaydi. Bu yerda faqat Fulbright ga xos talablar. Elchixona sahifasidagi ma'lumot {HOL}; yangi sikl e'lonida o'zgarishi mumkin.",
    lessons=[
        dict(t="Dastur va O'zbekiston uchun shartlar", short="Shartlar", min=30, kind="✅ Tekshiruv", ic="shield",
             hook="Fulbright ko'pchilik o'ylagandek \"eng a'lochilar uchun PhD granti\" emas. O'zbekistonda bu ish tajribasi bor mutaxassislar uchun magistratura dasturi va uning shartlari aniq yozilgan.",
             body=f"""<h4>Nima (2027–2028 sikli e'loni)</h4>
<p>Aspirant va yosh mutaxassislarga AQShda 2 yilgacha magistratura darajasini olish imkoniyati. Tanlov ochiq va natijaga asoslangan.</p>
<h4>Shartlar</h4>
<div class="tbl"><table><thead><tr><th>Shart</th><th>Izoh</th></tr></thead><tbody>
<tr><td>O'zbekiston fuqarosi, ariza va tanlov davomida O'zbekistonda yashaydi</td><td>Hozir xorijda yashayotganlar mos emas</td></tr>
<tr><td>Bakalavriatni tugatgan, bakalavr diplomi bor</td><td>Diplom qo'lda bo'lishi kerak</td></tr>
<tr><td>Kamida 2 yillik kasbiy tajriba</td><td>Eng ko'p uchraydigan to'siq</td></tr>
<tr><td>Tibbiyot bitiruvchilari bemor bilan bevosita ishlaydigan dasturga kira olmaydi</td><td>Jamoat salomatligi kabi yondosh sohalar mumkin</td></tr>
<tr><td>AQShda yaqinda uzoq tajribasi yo'q nomzodlarga kuchli ustunlik</td><td>—</td></tr>
</tbody></table></div>
<h4>Ustuvor sohalar (2027–2028)</h4>
<ul><li>Sun'iy intellekt, ma'lumotlar fani va raqamli ko'nikmalar (kompyuter fanlari, kiberxavfsizlik, mas'uliyatli AI).</li><li>AI va muhim minerallar iqtisodiyotiga xizmat qiladigan STEM: yarimo'tkazgichlar, geologiya, kon muhandisligi, materialshunoslik, energetika tizimlari.</li><li>Yadro muhandisligi va fuqarolik yadro siyosati.</li><li>Kosmos, masofadan zondlash va aerokosmik muhandislik.</li><li>Muhandislik (qurilish, ekologiya, energetika), qayta tiklanadigan energiya, resurslarni boshqarish, qishloq xo'jaligi va agrotexnologiya.</li></ul>
<p>Dastur boshqa sohalarga ham ochiq. 2026-yil 5-iyunda elchixona Fulbright ni muhim minerallar, energetika va ilg'or texnologiya sohalarida kengaytirish va El-yurt umidi jamg'armasining sherik moliyalashtirishini e'lon qilgan.</p>
<h4>Nima qoplanadi</h4>
<p>J-1 viza ko'magi, o'qish va yig'imlar, tibbiy sug'urta, oylik stipendiya, kitob va jihozlar, AQShga borish-kelish aviabileti.</p>
<div class="srcs">Manba: {EMB_FUL}; {EMB_FUL_EXP}. {HOL}.</div>""",
             take="Fulbright O'zbekiston uchun: magistratura, 2 yilgacha; bakalavr diplomi, 2 yillik tajriba, O'zbekistonda yashash. Ustuvor sohalar STEM va texnologiya, lekin boshqalar ham ochiq.",
             quiz=[("O'zbekistondan Fulbright Foreign Student Program magistratura uchun.", "t", "To'g'ri: elchixona e'loni."),
                   ("Ish tajribasi talab qilinmaydi.", "n", "Noto'g'ri: kamida 2 yillik kasbiy tajriba."),
                   ("Hozir xorijda yashayotgan O'zbekiston fuqarosi ariza bera oladi.", "n", "Noto'g'ri: ariza va tanlov davomida O'zbekistonda yashash kerak."),
                   ("Geologiya va energetika tizimlari 2027–2028 siklida ustuvor sohalar qatorida.", "t", "To'g'ri.")],
             task="<ul><li>Har shart bo'yicha o'zingizni belgilang: mos / tekshirish kerak / mos emas.</li><li>Sohangiz ustuvor ro'yxatdami? Qaysi band?</li></ul>",
             ph="Fuqarolik va yashash: mos; diplom: ...; 2 yil tajriba: ... (... dan beri); soha: ... — ustuvor: ha/yo'q"),
        dict(t="Tanlov bosqichlari va joylashtirish", short="Tanlov", min=25, kind="🧭 Jarayon", ic="compass",
             hook="Fulbright da universitetga o'zingiz ariza bermaysiz. Tanlov va joylashtirish boshqa tartibda ishlaydi va buni bilish kutish davridagi ko'p xavotirni olib tashlaydi.",
             body=f"""<h4>Olti bosqich (elchixona sahifasi)</h4>
<ol><li>Muddatdan keyin arizalarning texnik tekshiruvi.</li><li>Mustaqil o'quvchilar paneli arizalarni standart mezonlar bilan baholaydi.</li><li>Eng yuqori ball olganlar AQSh elchixonasida intervyuga chaqiriladi.</li><li>Intervyudan o'tganlar orasidan nomzodlar ko'rsatiladi.</li><li>Nomzodlar TOEFL va GRE yoki GMAT ga ro'yxatdan o'tadi; test xarajati elchixona vaucherlari bilan qoplanadi.</li><li>Yakuniy tanlov J. William Fulbright stipendiya kengashining tasdig'i, mablag' va muvaffaqiyatli akademik joylashtirishga bog'liq.</li></ol>
<h4>Joylashtirish</h4>
<p>Elchixona sahifasiga ko'ra, nomzodlar joylashtirish jarayonida qatnashmaydi va faqat yakuniy natija haqida xabar oladi. IIE ning umumiy tavsifida joylashtirishning ikki turi bor: IIE jamoasi nomzod uchun universitetlarga ariza beradigan tur va nomzod o'zi ariza beradigan tur. O'zbekiston uchun qaysi biri qo'llanishini elchixona e'lonidan oling.</p>
<div class="box info">Intervyu tayyorgarligining umumiy usullari (STAR, o'zini tanishtirish, yozib olish) Master Lab M8 da. Bu yerda Fulbright ga xos savol: siz qaytgandan keyin O'zbekistonga nima olib kelasiz?</div>
<div class="srcs">Manba: {EMB_FUL}; {FUL_IIE}. {HOL}.</div>""",
             take="Bosqichlar: texnik tekshiruv, o'quvchilar paneli, elchixonada intervyu, nomzodlik, testlar, kengash tasdig'i va joylashtirish. Joylashtirishda nomzod ishtirok etmaydi.",
             task="<ul><li>Olti bosqichning har biri uchun siz nima tayyorlashingiz kerakligini bir jumlada yozing.</li></ul>",
             ph="1) texnik: to'liq ariza ... 2) panel: ... 3) intervyu: ... 4) ... 5) testlar: ... 6) ..."),
        dict(t="Ariza tarkibi va halollik", short="Ariza", min=30, kind="📝 Reja", ic="memo",
             hook="Fulbright arizasidagi har bir insho original bo'lishi shart. Elchixona plagiat yoki AI yozgan matn arizani muvofiq emas deb topishga olib kelishini aniq yozgan.",
             body=f"""<h4>Ariza tarkibi (e'londan)</h4>
<div class="tbl"><table><thead><tr><th>Qism</th><th>Izoh</th><th>Qayerda o'rganiladi</th></tr></thead><tbody>
<tr><td>Onlayn ariza (IIE portali)</td><td>Muddatgacha; kech yoki to'liq bo'lmagan ariza ko'rilmaydi</td><td>Shu modul</td></tr>
<tr><td>Insholar</td><td>Original bo'lishi kerak; elchixonaning plagiat va insho ko'rsatmalari hujjatini o'qing</td><td>Yozish: Master Lab M5</td></tr>
<tr><td>Rezyume</td><td>Elchixona maslahatlari sahifasi bor</td><td>Master Lab M3</td></tr>
<tr><td>Tavsiya xati</td><td>Elchixonaning bo'sh formasi bilan</td><td>Master Lab M4</td></tr>
<tr><td>TOEFL va GRE yoki GMAT</td><td>Nomzod sifatida ko'rsatilganlar topshiradi, vaucher bilan</td><td>Mustaqil tayyorgarlik; kursga kirmaydi</td></tr>
</tbody></table></div>
<h4>Fulbright ga xos tekshiruv</h4>
<ul><li>Insho soni, hajmi va savollari: faqat joriy sikl ko'rsatmasidan.</li><li>Rezyume formati: elchixona maslahatlari bo'yicha.</li><li>Tavsiya xati: faqat elchixona formasi bilan.</li></ul>
<div class="box warn">AI dan matn yozdirish va boshqa birovning inshosini moslash Fulbright da arizani yopadi. Kompas Lab ham tayyor matn bermaydi: insholarni o'zingiz yozasiz, freymvork Master Lab da.</div>
<div class="srcs">Manba: {EMB_FUL}. {HOL}.</div>""",
             take="Ariza: onlayn shakl, original insholar, rezyume, elchixona formasidagi tavsiya, nomzodlar uchun testlar. Plagiat yoki AI matni arizani yopadi.",
             task="<ul><li>Joriy sikl sahifasidagi insho ko'rsatmalari hujjatini toping va savollar sonini yozing.</li><li>Har qism uchun tayyorlik holatingizni belgilang.</li></ul>",
             ph="Insho ko'rsatmasi: ... ta savol, ... (havola). Rezyume: ...; tavsiya: ...; ingliz tili: ..."),
        dict(t="Sikl kalendari", short="Kalendar", min=25, kind="📅 Kalendar", ic="calendar",
             hook="Fulbright muddati bilan safar orasida taxminan bir yil bor. Ariza muddatidan orqaga hisoblamasangiz, tavsiya va tajriba hujjatlarini oxirgi haftada yig'asiz.",
             body=f"""<h4>2027–2028 sikli</h4>
<div class="tbl"><table><thead><tr><th>Bosqich</th><th>Sana</th></tr></thead><tbody>
<tr><td>Ariza muddati</td><td>30.06.2026 (yopilgan)</td></tr>
<tr><td>Intervyu, nomzodlik, testlar</td><td>Muddatdan keyin; aniq sanalar sahifada ko'rsatilmagan</td></tr>
<tr><td>Safar</td><td>2027-yil bahor–kuz</td></tr>
</tbody></table></div>
<p>Keyingi sikl (2028–2029) uchun e'lon {HOL} topilmadi. 2027–2028 siklida muddat iyun oxiri bo'lgan; bu keyingi sikl uchun kafolat emas.</p>
<h4>Orqaga hisoblash (taxminiy, e'lon chiqqach aniqlanadi)</h4>
<ol><li>Muddatdan 6 oy oldin: muvofiqlik va tajriba hujjatlari.</li><li>4 oy oldin: tavsiya beruvchilar bilan kelishish.</li><li>3 oy oldin: insho qoralamalari.</li><li>1 oy oldin: tahrir va to'liq ariza.</li><li>Muddatdan 1 hafta oldin topshirish.</li></ol>
<div class="box info">Elchixonaning almashinuv dasturlari sahifasini oyiga bir marta tekshiring va Fulbright sahifasidagi yangilanish sanasini yozib boring.</div>
<div class="srcs">Manba: {EMB_FUL}; {EMB_EXCH}. {HOL}.</div>""",
             take="2027–2028 muddati 30.06.2026 da yopilgan; keyingi sikl e'lon qilinmagan. E'lon chiqqach muddatdan orqaga 6 oylik reja tuzing.",
             task="<ul><li>Keyingi sikl muddati iyun oxiri bo'lsa deb faraz qilib, 6 oylik teskari rejangizni yozing va uni \"faraz\" deb belgilang.</li></ul>",
             ph="Faraz: muddat 30.06.2027. Yanvar: ...; mart: ...; aprel: ...; may: ...; iyun: ..."),
        dict(t="J-1 va 2 yillik vatanda yashash talabi", short="J-1", min=25, kind="⚖️ Qaror", ic="bell",
             hook="Fulbright tugagach AQShda ishlab qolishni rejalashtirgan nomzod qonuniy to'siqqa uriladi. Bu to'siqni ariza berishdan oldin bilish kerak.",
             body=f"""<h4>Elchixona e'loni</h4>
<p>Grant J-1 vizasi bilan; grant tugagach, J-1 talablariga ko'ra kamida 2 yil o'z mamlakatiga qaytishi kerak.</p>
<h4>212(e) qanday ishlaydi (Harvard xalqaro ofisi)</h4>
<ul><li>Qo'llanadi: J-1 egasi AQSh hukumati, o'z hukumati yoki xalqaro tashkilot mablag'i bilan moliyalashtirilgan bo'lsa; malakasi [[Exchange Visitor Skills List]] da bo'lsa; yoki AQShda klinik tibbiy ta'lim olayotgan bo'lsa.</li><li>Cheklaydi: immigratsion viza, H yoki L vizasi va AQSh ichida boshqa maqomga o'tish, vatanda 2 yil bo'lmaguncha.</li><li>Qanday bilinadi: DS-2019 formasi va J-1 vizadagi belgi; noaniq bo'lsa, Davlat departamentidan [[Advisory Opinion]] so'raladi.</li></ul>
<h4>Ozod qilish</h4>
<p>Davlat departamenti sahifasida asoslardan biri sifatida favqulodda qiyinchilik yoki ta'qib ko'rsatilgan; bunda DS-3035 arizasi bilan birga USCIS ga Form I-612 topshiriladi. Ozod qilish oddiy yo'l emas va unga tayanib reja tuzilmaydi.</p>
<div class="box warn">Kompas Lab viza bo'yicha yuridik maslahat bermaydi. Shaxsiy holat bo'yicha universitet xalqaro ofisi yoki immigratsiya advokati bilan maslahatlashing.</div>
<div class="srcs">Manba: {EMB_FUL}; {HARVARD_212E}; {DOS_WAIVER}. {HOL}.</div>""",
             take="Fulbright J-1 bilan: grantdan keyin kamida 2 yil vatanda yashash talabi. Bu immigratsion viza, H, L va maqom o'zgartirishni cheklaydi. AQShda qolish rejasi bo'lsa, Fulbright mos emas.",
             task="<ul><li>5 yillik rejangizni yozing: magistraturadan keyin qayerda ishlaysiz?</li><li>Bu reja 2 yillik talab bilan mosmi? Ha yoki yo'q va nega.</li></ul>",
             ph="Reja: 2028–2030 magistratura, keyin ... 2 yillik talab bilan mos: ha, chunki ..."),
    ],
    tool=dict(id="fulbright", short="Karta", h2="Fulbright muvofiqlik va reja kartasi", sub="Muvofiqlikni tez tekshirish, kalendar va J-1 qarori.",
              h3="Fulbright kartasi", tag="5 maydon", ic="master", btn="Kartani saqlash", badge="Fulbright nomzodi", min=4,
              pre="""<div class="fld"><label>Tez tekshiruv <small>2027–2028 e'loni shartlari</small></label><div class="cklist" id="fbQ">
<label class="ck"><input type="checkbox" data-u="1"><span>O'zbekiston fuqarosiman va ariza hamda tanlov davomida O'zbekistonda yashayman</span></label>
<label class="ck"><input type="checkbox" data-u="2"><span>Bakalavr diplomim bor</span></label>
<label class="ck"><input type="checkbox" data-u="3"><span>Kamida 2 yillik kasbiy tajribam bor</span></label>
<label class="ck"><input type="checkbox" data-u="4"><span>Bemor bilan bevosita ishlaydigan klinik dasturni ko'zlamayman</span></label>
<label class="ck"><input type="checkbox" data-u="5"><span>Grantdan keyin kamida 2 yil O'zbekistonda yashashga tayyorman</span></label>
</div><div id="fbOut" class="out" style="white-space:normal">Belgilang.</div></div>""",
              fields=[dict(k="soha", label="Soha va ustuvorlik", ph="... — ustuvor ro'yxatda: ..."),
                      dict(k="tajriba", label="Tajriba dalili", hint="qayerda, qachondan, qanday hujjat", type="area", ph="... (2023-yildan), ish joyidan ma'lumotnoma"),
                      dict(k="kalendar", label="Teskari kalendar (faraz)", type="area", ph="Faraz: muddat ...; ..."),
                      dict(k="j1", label="J-1 va 5 yillik reja mosligi", type="area", ph="..."),
                      dict(k="qaror", label="Qaror", type="select", opts=["Keyingi siklga topshiraman", "Tajriba to'plab keyin topshiraman", "Boshqa yo'l: universitet orqali (M7)", "Mos emas"])]),
    check=dict(h2="M6 nazorati", sub="Kartani yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Shartlar joriy elchixona sahifasidan o'qilgan.", "2 yillik tajriba hujjat bilan tasdiqlanadi.", "Sohaning ustuvorlikka mosligi aniqlangan.",
                      "Tanlov bosqichlari va joylashtirish tartibini bilaman.", "Insho ko'rsatmalari hujjati topilgan.", "Insholarni o'zim yozaman, AI matni ishlatilmaydi.",
                      "Teskari kalendar faraz deb belgilangan.", "J-1 va 2 yillik talab rejamga mosligi tekshirilgan."]),
    art_title="Fulbright muvofiqlik va reja kartasi", art_short="Karta",
    art=[("Muvofiqlik", ["fbcalc", "a1"]), ("Soha", ["soha"]), ("Tajriba dalili", ["tajriba"]), ("Tanlov bosqichlari", ["a2"]), ("Ariza tarkibi", ["a3"]),
         ("Kalendar", ["kalendar", "a4"]), ("J-1 qarori", ["j1", "a5"]), ("Qaror", ["qaror"])],
    tip="Fulbright komissiyasi ikki narsani bir vaqtda ko'radi: AQShda nima o'rganasiz va qaytgach O'zbekistonda nima qilasiz. Ikkinchi savolga javobsiz birinchisi ham kuchsiz.",
    sources=f"{EMB_FUL}; {EMB_FUL_EXP}; {FUL_IIE}; {HARVARD_212E}; {DOS_WAIVER}; {EMB_EXCH}. {STD}",
    js="""window.KGTool = { init: function () {
  var box = document.getElementById("fbQ"), o = document.getElementById("fbOut");
  var cbs = box.querySelectorAll("input[data-u]");
  function run() {
    var n = 0, st = [];
    cbs.forEach(function (c) { if (c.checked) n++; st.push(c.checked ? 1 : 0); c.parentNode.classList.toggle("on", c.checked); });
    var ok = n === cbs.length;
    var txt = ok ? "2027–2028 eʼloni shartlari boʻyicha mos. Keyingi sikl eʼlonida qayta tekshiring." : "Belgilanmagan bandlar: " + (cbs.length - n) + " ta. Har biri arizani yopishi mumkin; avval shu bandlarni hal qiling.";
    o.innerHTML = "<span class=\\"pill " + (ok ? "ok" : "no") + "\\">" + n + "/" + cbs.length + "</span> " + KG.esc(txt);
    KG.S.notes.fbcalc = n + "/" + cbs.length + ": " + txt; KG.S.notes.fb_in = st.join(""); KG.save();
  }
  if (KG.S.notes.fb_in) { String(KG.S.notes.fb_in).split("").forEach(function (v, i) { if (cbs[i]) cbs[i].checked = v === "1"; }); }
  cbs.forEach(function (c) { c.addEventListener("change", run); });
  run();
} };""",
)
