from common import EDUSA_UG, ED_AID, OSU, SJSU, KSU, SEVIS, GMU, HOL, STD

MOD = dict(
    title="Xarajat va pul oqimi",
    desc="USA Lab M2: AQSh universitetining to'liq narxi (Cost of Attendance), I-20 uchun moliyaviy dalil, xalqaro talabaga ochiq va yopiq pul manbalari, ehtiyojga va natijaga asoslangan yordam farqi, arzon yo'llar va oilaviy byudjet chegarasi. Natija: AQSh pul xaritasi.",
    lead="AQShda qabul xati yetarli emas: I-20 olish uchun birinchi yil pulini hujjat bilan ko'rsatasiz. Bu modulda narx qayerdan kelishini, qaysi pul manbalari sizga yopiq ekanini va oilangiz yiliga qancha bera olishini raqam bilan aniqlaysiz.",
    hero="money", weeks="1–2", next="M3 Yordam beradigan universitetlarni topish", next_href="usa-lab-o.html?m=3",
    goals=[("money", "AQSh pul xaritasi", "narx, oila chegarasi, kerakli yordam ulushi"),
           ("scroll", "I-20 moliyaviy dalil rejasi", "qaysi hujjat qabul qilinadi, qaysi biri yo'q"),
           ("compass", "Yo'l xulosasi", "to'liq yordam, qisman yordam yoki arzon yo'l")],
    warn=f"Bu modul faqat AQSh pul mexanizmini o'rgatadi. Mamlakatlararo umumiy xarajat modeli va 4 yillik reja Bachelor Lab M12 da. Summalar har yili o'zgaradi; {HOL} universitet sahifasidan oling. Kompas Lab moliyaviy maslahatchi emas; qarorni oila bilan qabul qiling.",
    lessons=[
        dict(t="To'liq narx: Cost of Attendance", short="Narx", min=30, kind="🧮 Hisob", ic="money",
             hook="O'qish to'lovi ([[tuition]]) universitet so'raydigan pulning faqat bir qismi. AQSh universitetlari to'liq narxni [[Cost of Attendance]] deb e'lon qiladi va yordam ham, I-20 ham shu summaga qarab hisoblanadi.",
             body=f"""<h4>Narx tarkibi</h4>
<p>Kennesaw State universiteti bir yillik taxminiy xarajatni uch qatorga ajratadi: o'qish to'lovi va yig'imlar ([[tuition and fees]]), yashash xarajatlari va boshqa xarajatlar (majburiy tibbiy sug'urta, transport, kitob va shaxsiy xarajatlar). Boshqa universitetlarda ham tarkib shunga yaqin, lekin qatorlar nomi farq qiladi.</p>
<div class="tbl"><table><thead><tr><th>Qator</th><th>Qayerdan olinadi</th></tr></thead><tbody>
<tr><td>O'qish to'lovi va yig'imlar</td><td>Universitetning [[tuition and fees]] sahifasi, xalqaro yoki shtatdan tashqari ([[nonresident]]) narx</td></tr>
<tr><td>Yashash (yotoqxona, ovqat)</td><td>[[Cost of Attendance]] yoki [[housing]] sahifasi</td></tr>
<tr><td>Tibbiy sug'urta</td><td>Xalqaro talabalar bo'limi sahifasi</td></tr>
<tr><td>Kitob, transport, shaxsiy</td><td>[[Cost of Attendance]] sahifasi</td></tr>
<tr><td>Bir martalik: viza yig'imi, SEVIS I-901, aviabilet</td><td>Elchixona va ICE sahifalari (M8)</td></tr>
</tbody></table></div>
<h4>Narx o'sadi</h4>
<p>EducationUSA rejalashtirishda o'qish to'lovining har yili taxminan 6–10 foiz oshishini hisobga olishni maslahat beradi. 4 yillik bakalavriat uchun birinchi yil narxi bilan hisoblash xato.</p>
<div class="box info">Universitet sahifasidagi summa qaysi o'quv yili uchun ekanini yozib qo'ying. Kelasi yil narxi hali e'lon qilinmagan bo'lishi mumkin.</div>
<div class="srcs">Manba: {KSU}; {EDUSA_UG}; {SEVIS}. {HOL}.</div>""",
             take="To'liq narx: o'qish va yig'imlar, yashash, sug'urta, kitob va shaxsiy xarajatlar, bir martalik to'lovlar. Har yili 6–10 foiz o'sishni qo'shing.",
             task="<ul><li>Bitta universitetning xalqaro talaba uchun [[Cost of Attendance]] summasini qatorlari bilan yozing.</li><li>O'quv yili, havola va tekshirilgan sanani qo'shing.</li></ul>",
             ph="... universiteti, 2026–2027: o'qish ..., yashash ..., sug'urta ..., boshqa ... = jami ... USD; havola ..."),
        dict(t="I-20 uchun pul dalili", short="I-20", min=30, kind="📑 Hujjat", ic="scroll",
             hook="Ko'p oila uy yoki mashina bor, demak pul bor deb o'ylaydi. AQSh universiteti I-20 berishda esa mulkni emas, ishlatsa bo'ladigan pulni ko'radi.",
             body=f"""<h4>Qancha ko'rsatiladi</h4>
<p>Kennesaw State: talaba birinchi o'quv yili uchun yetarli mablag'ni ko'rsatishi kerak va hujjatlar dastur uchun taxminiy yillik summadan kam bo'lmasligi lozim. San José State ham kamida bir o'quv yilining taxminiy xarajatini so'raydi.</p>
<h4>Qaysi hujjat qabul qilinadi (San José State namunasi)</h4>
<div class="tbl"><table><thead><tr><th>Qabul qilinadi</th><th>Qabul qilinmaydi</th></tr></thead><tbody>
<tr><td>Bank xati yoki ko'chirmasi (jamg'arma yoki joriy hisob)</td><td>Ish joyidan maosh haqida xat</td></tr>
<tr><td>Muddatli omonat: bank xatida pulni istalgan vaqt jarimasiz olish mumkinligi yozilgan bo'lsa</td><td>Uy, oltin, zargarlik baholash hujjatlari</td></tr>
<tr><td>Tasdiqlangan kredit xati</td><td>Aksiya va investitsiya fondi ko'chirmalari</td></tr>
<tr><td>Stipendiya xati (davlat, xususiy yoki universitet)</td><td>Kredit liniyasi xati</td></tr>
</tbody></table></div>
<p>Shu universitetda hujjat AQSh dollarida, ingliz tilida, bank blankida, muhr yoki imzo bilan va ariza topshirilishidan oldingi 6 oy ichida berilgan bo'lishi kerak.</p>
<div class="box warn">Qoidalar universitetga qarab farq qiladi. O'z universitetingizning [[financial documents]] yoki [[I-20 request]] sahifasini o'qing. Pulni vaqtincha hisobga qo'yib turish (begona pul) halollik va viza suhbati uchun xavfli: konsul pul manbasini so'rashi mumkin.</div>
<div class="srcs">Manba: {KSU}; {SJSU}. {HOL}.</div>""",
             take="I-20 uchun kamida birinchi yil taxminiy xarajati ishlatsa bo'ladigan pul bilan ko'rsatiladi. Mulk, maosh xati va aksiyalar ko'pincha qabul qilinmaydi.",
             quiz=[("I-20 uchun oilaning uyi baholash hujjati ko'pincha yetarli dalil bo'ladi.", "n", "Noto'g'ri: San José State mulk va oltin baholash hujjatini qabul qilmaydi."),
                   ("Muddatli omonat qabul qilinishi uchun pulni jarimasiz olish mumkinligi yozilishi kerak.", "t", "To'g'ri: San José State shuni talab qiladi."),
                   ("Stipendiya xati moliyaviy dalil bo'lishi mumkin.", "t", "To'g'ri: davlat, xususiy yoki universitet stipendiyasi xati."),
                   ("Hamma universitetda hujjat talablari bir xil.", "n", "Noto'g'ri: har universitet sahifasini o'qing.")],
             task="<ul><li>Oilangiz qaysi hujjatlarni bera olishini yozing: bank ko'chirmasi, omonat, stipendiya, kredit.</li><li>Ularning birinchi yil narxini qoplashi yoki qoplamasligini hisoblang.</li></ul>",
             ph="Bank ko'chirmasi: ... USD; omonat: ... (jarimasiz olish: ha/yo'q); jami ... / birinchi yil narxi ..."),
        dict(t="Sizga ochiq va yopiq pul manbalari", short="Manbalar", min=25, kind="🧭 Xarita", ic="compass",
             hook="AQSh talabalarining ko'pi federal grant va kreditdan foydalanadi. Bu pul xalqaro talabaga yopiq, shuning uchun AQSh talabalari uchun yozilgan maslahatlarning yarmi sizga ishlamaydi.",
             body=f"""<h4>Yopiq manbalar</h4>
<p>AQSh Ta'lim vazirligi: talaba AQSh fuqarosi ham, belgilangan toifadagi fuqaro bo'lmagan shaxs ([[eligible noncitizen]]) ham bo'lmasa, federal talaba yordamini ololmaydi. Ohio State: xalqaro talabalar odatda federal, shtat va universitetning ko'p yordam turlarini ololmaydi.</p>
<h4>Ochiq bo'lishi mumkin bo'lgan manbalar</h4>
<div class="tbl"><table><thead><tr><th>Manba</th><th>Izoh</th></tr></thead><tbody>
<tr><td>Universitet yordami (ehtiyojga asoslangan)</td><td>Faqat ba'zi universitetlarda xalqaro talabaga ochiq (M3)</td></tr>
<tr><td>Universitet stipendiyasi (natijaga asoslangan)</td><td>Ko'pincha qisman; shartini o'qing (2.4)</td></tr>
<tr><td>Sport stipendiyasi</td><td>EducationUSA sport bilan shug'ullanadigan talabalarga buni ko'rib chiqishni tavsiya qiladi</td></tr>
<tr><td>Davlat dasturlari</td><td>Global UGRAD, Fulbright (M5–M6)</td></tr>
<tr><td>Kafedra moliyalashtirishi</td><td>Asosan PhD (M7)</td></tr>
<tr><td>Kampusda ishlash</td><td>F-1 talabaga o'qish davrida haftasiga 20 soatgacha (M8); asosiy manba emas</td></tr>
<tr><td>Oila</td><td>2.5 da chegarasini aniqlaysiz</td></tr>
</tbody></table></div>
<div class="box warn">\"AQShda ishlab o'qish to'lovini qoplayman\" rejasi ishlamaydi: kampusdan tashqarida ishlash yozma ruxsatsiz mumkin emas, kampusda esa soat cheklangan.</div>
<div class="srcs">Manba: {ED_AID}; {OSU}; {EDUSA_UG}; {GMU}. {HOL}.</div>""",
             take="Federal yordam xalqaro talabaga yopiq. Ochiq manbalar: universitet yordami, stipendiyalar, davlat dasturlari, kafedra moliyalashtirishi va oila. Ish daromadi asosiy manba emas.",
             task="<ul><li>Yuqoridagi 7 manbadan sizga real bo'lganlarini belgilang.</li><li>Har biri uchun bir jumla: nega real yoki nega emas.</li></ul>",
             ph="Universitet yordami: real, chunki ...; sport: yo'q; Fulbright: ... ; oila: ..."),
        dict(t="Ehtiyojga va natijaga asoslangan yordam", short="Yordam turi", min=25, kind="⚖️ Farq", ic="bulb",
             hook="\"Grant oldim\" degan gap ikki xil narsa bo'lishi mumkin: oilangiz to'lay olmaydigan qism qoplandi yoki yaxshi natijangiz uchun narxdan chegirma berildi. Ularni farqlamasangiz, universitet ro'yxatini noto'g'ri tuzasiz.",
             body=f"""<div class="tbl"><table><thead><tr><th></th><th>Ehtiyojga asoslangan ([[need-based]])</th><th>Natijaga asoslangan ([[merit-based]])</th></tr></thead><tbody>
<tr><td>Nimaga qarab</td><td>Narx va oilangiz to'lay oladigan summa orasidagi farqqa</td><td>Baho, test, yutuqlar, iste'dodga</td></tr>
<tr><td>Qanday so'raladi</td><td>Moliyaviy yordam arizasi (CSS Profile yoki universitet formasi, M4)</td><td>Ko'pincha qabul arizasi bilan avtomatik yoki alohida ariza</td></tr>
<tr><td>Kimga ko'proq mos</td><td>Oilaviy daromadi past talabaga</td><td>Natijasi kuchli, oilasi qisman to'lay oladigan talabaga</td></tr>
<tr><td>Xavf</td><td>Xalqaro talabaga ochiq universitetlar kam</td><td>Ko'pincha narxning bir qismi; qolganini oila to'laydi</td></tr>
</tbody></table></div>
<p>EducationUSA ogohlantiradi: ko'p stipendiyalar o'qish va yashash narxining faqat bir qismini qoplaydi va birinchi kurs xalqaro talabasiga berilmasligi mumkin.</p>
<h4>Shartlarni o'qing</h4>
<ul><li>Bir yilgami yoki butun o'qish davrigami?</li><li>Keyingi yillarda baho sharti bormi?</li><li>Summa qat'iymi, foizmi?</li><li>Boshqa yordam bilan birga beriladimi?</li></ul>
<div class="srcs">Manba: {EDUSA_UG}. {HOL}.</div>""",
             take="Ehtiyojga asoslangan yordam oila to'lay olmaydigan farqni qoplaydi; natijaga asoslangan yordam yutuq uchun beriladi va ko'pincha qisman. Shartlarini o'qing.",
             task="<ul><li>Sizga qaysi tur ko'proq mos: ehtiyojga yoki natijaga asoslangan? Ikki dalil bilan yozing.</li></ul>",
             ph="Menga ... mos, chunki 1) oila yiliga ... USD bera oladi; 2) natijalarim ..."),
        dict(t="Oilaviy byudjet chegarasi va yo'l xulosasi", short="Chegara", min=30, kind="🗣 Suhbat", ic="calendar",
             hook="Oila bilan \"qancha to'lay olamiz?\" degan aniq raqamni gaplashmasdan ariza boshlash xato. Bu raqam qaysi universitetlar sizga real ekanini belgilaydi.",
             body="""<h4>Chegara qanday aniqlanadi</h4>
<ol><li>Oilaning yillik daromadi va har oylik majburiy xarajatlari.</li><li>Jamg'arma: shundan qancha qismi o'qishga ajratiladi va qolgani nima uchun kerak.</li><li>Yiliga AQSh dollarida maksimal summa: \"to'lay olamiz\", \"qiyin bo'ladi\" emas, raqam.</li><li>Bu summa 4 yil (bakalavr) yoki 2 yil (magistratura) davomida takrorlanadimi?</li></ol>
<h4>Kerakli yordam ulushi</h4>
<p>Kerakli yordam = to'liq narx − oila chegarasi. Uni to'liq narxga bo'lsangiz, ulushni olasiz.</p>
<div class="tbl"><table><thead><tr><th>Kerakli yordam ulushi</th><th>Kompas tavsiyasi (qoida emas)</th></tr></thead><tbody>
<tr><td>0 (oila to'liq to'laydi)</td><td>Yordamni so'ramasangiz ham bo'ladi; natijaga asoslangan grantni qidiring</td></tr>
<tr><td>Taxminan 50 foizgacha</td><td>Natijaga asoslangan stipendiyalar va arzon yo'llar (ikki yillik kollej, arzon hududlar)</td></tr>
<tr><td>50 foizdan ko'p</td><td>Faqat xalqaro talabaga to'liq ehtiyojni qoplaydigan universitetlar (M3) yoki davlat dasturlari; parallel boshqa mamlakat</td></tr>
</tbody></table></div>
<p>EducationUSA xarajatni kamaytirish uchun turli davlat va xususiy universitetlarni, arzonroq hududlarni (janub, O'rta G'arb, qishloq joylar) va ikki yillik kollejdan o'tish yo'lini ko'rib chiqishni maslahat beradi.</p>
<div class="box warn">Kerakli yordam ulushi juda katta bo'lsa, AQSh yo'lini boshqa mamlakat bilan parallel olib boring. Kompas bunda boshqa Labni ko'rsatadi.</div>""",
             take="Oila chegarasini dollarda, yillik raqam bilan aniqlang. Kerakli yordam ulushi yo'lni belgilaydi: arzon yo'l, natijaga asoslangan grant yoki to'liq ehtiyojni qoplaydigan universitet.",
             task="<ul><li>Oila bilan suhbatdan keyin yillik maksimal summani yozing.</li><li>Bitta universitet uchun kerakli yordam ulushini hisoblang va yo'l xulosasini yozing.</li></ul>",
             ph="Oila chegarasi: yiliga ... USD, ... yil. ... universiteti narxi ... → kerakli yordam ...%. Xulosa: ..."),
    ],
    tool=dict(id="pul", short="Pul xaritasi", h2="AQSh pul xaritasi", sub="Hisoblagich: narx, o'sish va oila chegarasini kiriting; kerakli yordam ulushi va yo'l xulosasi chiqadi.",
              h3="Pul xaritasi", tag="5 maydon", ic="money", btn="Xaritani saqlash", badge="Pul xaritachi", min=4,
              pre="""<div class="fld"><label>Hisoblagich <small>AQSh dollarida, yillik</small></label><div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px"><input id="pC" type="number" min="0" placeholder="To'liq narx (COA)" style="min-height:46px;padding:10px 12px;border:2px solid var(--border);border-radius:12px;font-size:16px"><input id="pF" type="number" min="0" placeholder="Oila chegarasi" style="min-height:46px;padding:10px 12px;border:2px solid var(--border);border-radius:12px;font-size:16px"><input id="pY" type="number" min="1" max="6" placeholder="Yillar (masalan 4)" style="min-height:46px;padding:10px 12px;border:2px solid var(--border);border-radius:12px;font-size:16px"><input id="pG" type="number" min="0" step="1" placeholder="Yillik o'sish, % (6–10)" style="min-height:46px;padding:10px 12px;border:2px solid var(--border);border-radius:12px;font-size:16px"></div><div id="pOut" class="out" style="white-space:normal">Raqamlarni kiriting.</div></div>""",
              fields=[dict(k="uni", label="Universitet va o'quv yili", ph="... universiteti, 2026–2027"),
                      dict(k="narx", label="To'liq narx qatorlari", type="area", ph="O'qish ..., yashash ..., sug'urta ..., boshqa ..., bir martalik ..."),
                      dict(k="dalil", label="I-20 uchun pul dalili rejasi", type="area", ph="Bank ko'chirmasi ..., omonat ..., stipendiya ..."),
                      dict(k="manba", label="Sizga ochiq manbalar", type="area", ph="Universitet yordami ..., stipendiya ..., davlat dasturi ..., oila ..."),
                      dict(k="yol", label="Yo'l xulosasi", type="select", opts=["Oila to'liq to'laydi", "Natijaga asoslangan grant + arzon yo'l", "Faqat to'liq ehtiyojni qoplaydigan universitetlar", "AQSh + boshqa mamlakat parallel"])]),
    check=dict(h2="M2 nazorati", sub="Pul xaritasini yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Narx xalqaro talaba uchun va o'quv yili ko'rsatilgan.", "Narx qatorlari manbasi bilan yozilgan.", "Yillik o'sish hisobga olingan.",
                      "I-20 uchun qaysi hujjat qabul qilinishi universitet sahifasidan o'qilgan.", "Federal yordam yopiq ekani hisobga olingan.",
                      "Kampusda ishlash asosiy manba qilinmagan.", "Oila chegarasi dollarda, yillik raqam bilan.", "Yo'l xulosasi oila bilan muhokama qilingan."]),
    art_title="AQSh pul xaritasi", art_short="Pul xaritasi",
    art=[("Universitet va o'quv yili", ["uni"]), ("To'liq narx", ["narx", "a1"]), ("I-20 pul dalili", ["dalil", "a2"]), ("Ochiq manbalar", ["manba", "a3"]),
         ("Yordam turi", ["a4"]), ("Hisob", ["pcalc"]), ("Oila chegarasi va yo'l", ["a5", "yol"])],
    tip="AQSh universitetlari sizdan avval oilangiz qancha to'lay olishini so'raydi. Bu raqamni ular emas, siz birinchi bo'lib aniq bilishingiz kerak.",
    sources=f"{KSU}; {SJSU}; {ED_AID}; {OSU}; {EDUSA_UG}; {GMU}; {SEVIS}. {STD}",
    js="""window.KGTool = { init: function () {
  var ids = ["pC", "pF", "pY", "pG"], o = document.getElementById("pOut");
  function v(id) { var x = parseFloat(document.getElementById(id).value); return isNaN(x) ? 0 : x; }
  function fmt(n) { return Math.round(n).toLocaleString("ru-RU"); }
  function run() {
    var C = v("pC"), F = v("pF"), Y = Math.max(1, Math.min(6, Math.round(v("pY")) || 4)), G = v("pG") / 100;
    if (!C) { o.textContent = "Raqamlarni kiriting."; return; }
    var tot = 0, need = 0;
    for (var y = 0; y < Y; y++) { var c = C * Math.pow(1 + G, y); tot += c; need += Math.max(0, c - F); }
    var share = tot ? need / tot * 100 : 0, tag, cls;
    if (share <= 0) { tag = "Oila toʻliq toʻlaydi"; cls = "ok"; }
    else if (share <= 50) { tag = "Natijaga asoslangan grant + arzon yoʻl"; cls = "chk"; }
    else { tag = "Faqat toʻliq ehtiyojni qoplaydigan universitetlar yoki parallel mamlakat"; cls = "no"; }
    var txt = Y + " yillik narx: " + fmt(tot) + " USD; oila: " + fmt(F * Y) + " USD; kerakli yordam: " + fmt(need) + " USD (" + Math.round(share) + "%). Yoʻl: " + tag + ".";
    o.innerHTML = "<span class=\\"pill " + cls + "\\">" + Math.round(share) + "% yordam</span> " + KG.esc(txt);
    KG.S.notes.pcalc = txt; KG.S.notes.p_in = [C, F, Y, v("pG")].join("|"); KG.save();
  }
  if (KG.S.notes.p_in) { var p = String(KG.S.notes.p_in).split("|"); ids.forEach(function (id, i) { if (p[i] && p[i] !== "0") document.getElementById(id).value = p[i]; }); }
  ids.forEach(function (id) { document.getElementById(id).addEventListener("input", run); });
  run();
} };""",
)
