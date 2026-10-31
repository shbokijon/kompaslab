from common import U27, G26, SIK, STD

MOD = dict(
    title="Paketni yig'ish va topshirish",
    desc="GKS Lab M7: onlayn ariza va muddatlar, fayl, format va nusxalar, ikkinchi shaxs tekshiruvi va xatolar filtri, teskari taqvim. Natija: topshirishga tayyor paket va taqvim.",
    lead="Kuchli hujjatlar kech yoki noto'g'ri tartibda topshirilsa, ularni hech kim o'qimaydi. Bu modulda paketni yo'riqnoma tartibida yig'asiz, ikkinchi odamga tekshirtirasiz va muddatdan orqaga qarab taqvim tuzasiz.",
    hero="hourglass", weeks="2", next="Intervyu, natija va jo'nash",
    goals=[("hourglass", "Teskari taqvim", "ariza muddatidan orqaga hisoblangan bosqichlar"),
           ("scroll", "Paket ro'yxati", "yo'riqnoma tartibida, fayl nomlari bilan"),
           ("shield", "Ikkinchi shaxs tekshiruvi", "tekshiruvchi va uning izohlari")],
    warn="Sanalar 2027 GKS-U (sentabr 2026 da e'lon qilingan) va 2026 GKS-G yo'riqnomalaridan, 31.10.2026 holatiga, Koreya vaqti (KST) bilan. 2027 GKS-G yo'riqnomasi 2026 sikli tartibiga ko'ra taxminan fevralda chiqadi; yangi sanalarni rasmiy e'londan oling.",
    lessons=[
        dict(t="Onlayn ariza va muddatlar", short="Muddat", min=35, kind="🎯 Mini-test", ic="calendar",
             hook="Koreya vaqti O'zbekistondan 4 soat oldinda. \"18:00 gacha\" deb yozilgan muddat Toshkentda soat 14:00 da yopiladi.",
             body=f"""<h4><span class="trk">U</span> 2027 GKS-U jadvali</h4>
<div class="tbl"><table><thead><tr><th>Bosqich</th><th>Elchixona treki</th><th>Universitet treki</th></tr></thead><tbody>
<tr><td>Ariza</td><td>15.09.2026, 11:00 – 30.09.2026, 18:00 (KST), onlayn</td><td>Har universitet o'zi belgilaydi, 2026-yil noyabrigacha</td></tr>
<tr><td>1-bosqich natijasi</td><td>16-oktabrgacha</td><td>Noyabrda</td></tr>
<tr><td>Hujjatlar NIIED ga</td><td>30-oktabrgacha</td><td>30-noyabrgacha</td></tr>
<tr><td>2-bosqich natijasi</td><td>Noyabr ichida</td><td>Dekabr ichida</td></tr>
<tr><td>3-bosqich (universitet)</td><td>23-dekabr, 18:00 gacha</td><td>Yo'q</td></tr>
<tr><td>Universitet tanlovini bildirish</td><td>29-dekabr, 18:00 gacha</td><td>—</td></tr>
<tr><td>Yakuniy e'lon</td><td colspan="2">Taxminan 07.01.2027, Study in Korea saytida</td></tr>
</tbody></table></div>
<h4><span class="trk">M</span> <span class="trk">D</span> 2026 GKS-G jadvali (o'tgan sikl, namuna)</h4>
<ul><li>Elchixona treki: onlayn ariza 12.02.2026, 11:00 – 25.02.2026, 18:00 (KST); 1-bosqich natijasi 17-mart; hujjatlar NIIED ga 1-aprelgacha; 2-bosqich may boshi; universitet natijasi iyun boshi; universitet tanlovi 12-iyun, 18:00 gacha; yakuniy e'lon iyun oxiri.</li>
<li>Universitet treki: muddatni universitet belgilaydi; hujjatlar NIIED ga 1-maygacha; yakuniy e'lon iyun oxiri.</li></ul>
<div class="box warn">Oxirgi kunga qoldirmang. Portal yuklamasi, fayl hajmi yoki imzo muammosi oxirgi soatlarda tuzatib bo'lmaydi. O'z muddatingizni rasmiy muddatdan kamida 3 kun oldin qo'ying.</div>
<div class="srcs">Manba: {U27}; {G26}; {SIK}.</div>""",
             take="Muddatlar KST bilan: Toshkentdan 4 soat oldin yopiladi. O'z muddatingizni rasmiydan kamida 3 kun oldin qo'ying.",
             quiz=[("2027 GKS-U elchixona treki onlayn arizasi 30.09.2026, 18:00 (KST) da yopilgan.", "t", "To'g'ri."),
                   ("KST bo'yicha 18:00 Toshkent vaqti bilan ham 18:00.", "n", "Noto'g'ri: Koreya 4 soat oldinda, Toshkentda 14:00."),
                   ("Universitet trekida muddatni har universitet o'zi belgilaydi.", "t", "To'g'ri."),
                   ("2027 GKS-G sanalari 2026 sikli bilan aynan bir xil bo'lishi kafolatlangan.", "n", "Noto'g'ri: yangi sanalar yangi yo'riqnomadan olinadi.")],
             task="<ul><li>O'z treking va yo'lingiz bo'yicha barcha muddatlarni Toshkent vaqtiga o'girib yozing.</li></ul>",
             ph="Ariza yopiladi: ... (Toshkent: ...)"),
        dict(t="Fayl, format va nusxalar", short="Fayl", min=30, kind="📁 Paket", ic="scroll",
             hook="Komissiya \"scan_0012.jpg\" nomli 18 ta faylni ochishni xohlamaydi. Tartibli paket ham hujjatning bir qismi.",
             body="""<h4>Yig'ish qoidalari</h4>
<ul><li><b>Tartib:</b> yo'riqnomadagi raqamlash bo'yicha (1-formadan boshlab). Tartib yo'riqnomada berilgan bo'lsa, o'zgartirmang.</li>
<li><b>Format:</b> skanerlar aniq, to'liq sahifa, rangli muhr ko'rinadi; telefon surati soyali va qiyshiq bo'lmasin. PDF ga birlashtirish talab qilingan bo'lsa, shunday qiling.</li>
<li><b>Fayl nomi:</b> Raqam_Familiya_Hujjat (masalan, 03_Karimov_StudyPlan.pdf).</li>
<li><b>Imzo:</b> imzo talab qilingan har forma imzolangan va sanasi qo'yilgan.</li>
<li><b>Asl va nusxa:</b> qaysi hujjat asl, qaysi nusxa (M1 jadvalidan). Asl hujjatlar pochta orqali ketsa, kuzatuv raqami bilan yuboring.</li>
<li><b>Zaxira:</b> hamma narsaning skaneri va onlayn ariza bo'limlarining skrinshoti sizda qolsin.</li></ul>
<div class="box info">Elchixona trekida ba'zi asl hujjatlar (masalan, tavsiya xatining asli) keyingi bosqichda so'raladi. Ularni asrang, buklamang va asl nusxani berib yubormang, agar yo'riqnoma talab qilmasa.</div>""",
             take="Paket yo'riqnoma tartibida, aniq skanerlar, tushunarli fayl nomlari va imzolar bilan. Hamma narsaning zaxirasi sizda qoladi.",
             task="<ul><li>Paket ro'yxatini fayl nomlari bilan yozing: raqam · fayl nomi · asl yoki nusxa · holat.</li></ul>",
             ph="01_Familiya_ApplicationForm.pdf · forma · tayyor ..."),
        dict(t="Ikkinchi shaxs tekshiruvi va xatolar filtri", short="Tekshiruv", min=30, kind="🔍 Filtr", ic="shield",
             hook="O'z hujjatingizdagi xatoni ko'rish qiyin: miya yozganingizni emas, yozmoqchi bo'lganingizni o'qiydi.",
             body="""<h4>Keng tarqalgan xatolar filtri</h4>
<div class="tbl"><table><thead><tr><th>Xato</th><th>Qanday topiladi</th></tr></thead><tbody>
<tr><td>Ism yozilishi turlicha</td><td>Barcha hujjatda ismni pasport bilan solishtiring</td></tr>
<tr><td>Universitet yoki dastur nomi boshqa joyda boshqacha</td><td>Ariza, bayonot, reja bo'yicha qidiring</td></tr>
<tr><td>Shablon matn qolgan</td><td>\"[University name]\" kabi qavslarni qidiring</td></tr>
<tr><td>Muddati o'tgan sertifikat</td><td>Har sertifikat sanasini tekshiring</td></tr>
<tr><td>Hajm chegarasidan oshgan</td><td>Formadagi chegara bilan sanang</td></tr>
<tr><td>Tekshirib bo'lmaydigan da'vo</td><td>Har raqamga hujjat qo'ying</td></tr>
</tbody></table></div>
<h4>Ikkinchi shaxs</h4>
<ul><li>Tekshiruvchi: ingliz (yoki koreys) tilini yaxshi biladigan, siz bilan bir xil fikrlamaydigan odam.</li>
<li>Unga yo'riqnoma va M7 nazorat ro'yxatini bering; u ro'yxat bo'yicha tekshiradi, matnni qayta yozmaydi.</li>
<li>Izohlarni yozib boring va har biriga qaror chiqaring.</li></ul>""",
             take="Xatolar filtri va ikkinchi odam: ism, nomlar, shablon qoldiqlari, sanalar, hajm, dalilsiz da'vo.",
             task="<ul><li>Tekshiruvchini tanlang va sanani belgilang. Filtrni o'zingiz bir marta o'tkazib, topilgan xatolarni yozing.</li></ul>",
             ph="Tekshiruvchi: ... sana: ... Topilgan xatolar: ..."),
        dict(t="Teskari taqvim", short="Taqvim", min=25, kind="🛠 Taqvim", ic="hourglass",
             hook="\"Hali vaqt bor\" eng xavfli fikr. Teskari taqvim har ishni muddatdan orqaga qarab joylaydi va qancha vaqt qolganini aniq ko'rsatadi.",
             body="""<h4>Bosqichlar (muddatdan orqaga)</h4>
<div class="tbl"><table><thead><tr><th>Muddatdan oldin</th><th>Nima tayyor bo'lishi kerak</th></tr></thead><tbody>
<tr><td>12 hafta</td><td>Hujjatlar ro'yxati, universitet tanlovi (M1, M2)</td></tr>
<tr><td>10 hafta</td><td>Apostil va tarjima boshlangan; tavsiya so'ralgan (M4)</td></tr>
<tr><td>8 hafta</td><td>Dalillar inventari (M3); professorga xatlar (M, D)</td></tr>
<tr><td>6 hafta</td><td>Bayonot va reja birinchi qoralamalari (M5, M6)</td></tr>
<tr><td>4 hafta</td><td>O'zaro tahrir; tavsiya xati olingan</td></tr>
<tr><td>2 hafta</td><td>Yakuniy versiyalar, paket yig'ilgan, ikkinchi shaxs tekshiruvi</td></tr>
<tr><td>3 kun</td><td>Shaxsiy muddat: onlayn ariza yuborilgan</td></tr>
</tbody></table></div>
<p>Bu Kompas tavsiya qilgan jadval. Agar sizda 12 haftadan kam qolgan bo'lsa, bosqichlarni parallel yuriting va eng uzoq ishni (apostil, tavsiya) birinchi boshlang.</p>
<p>Pastdagi vositaga muddatni kiritsangiz, sanalarni o'zi hisoblaydi.</p>""",
             take="Har ishni muddatdan orqaga joylang; eng uzoq jarayonlar (apostil, tavsiya) birinchi. Shaxsiy muddat rasmiydan 3 kun oldin.",
             task="<ul><li>Vositada taqvimni hisoblang va har bosqichga mas'ul va izoh yozing.</li></ul>",
             ph="Qaysi bosqich men uchun eng xavfli va nega: ..."),
    ],
    tool=dict(id="taqvim", short="Taqvim", h2="Teskari taqvim va paket", sub="Rasmiy muddatni kiriting: bosqich sanalari Toshkent vaqtini hisobga olib chiqadi.",
              h3="Taqvim va paket ro'yxati", tag="sana + ro'yxat", ic="hourglass", btn="Taqvimni saqlash", badge="Rejalovchi", min=3,
              fields=[dict(k="dl", label="Rasmiy ariza muddati", hint="Koreya vaqti bo'yicha kun", type="date"),
                      dict(k="yol7", label="Trek va yo'l", type="select", opts=["U: elchixona treki", "U: universitet treki", "M/D: elchixona treki", "M/D: universitet treki"]),
                      dict(k="pk", label="Paket ro'yxati", hint="raqam · fayl nomi · asl/nusxa · holat", type="area", ph=""),
                      dict(k="tek", label="Ikkinchi shaxs tekshiruvchi va sana", type="text", ph="Ism, sana")]),
    check=dict(h2="Topshirish nazorati", sub="\"Yuborish\" tugmasidan oldin.", h3="10 bandlik nazorat",
               items=["Barcha muddatlar Toshkent vaqtiga o'girilgan.", "Paket yo'riqnoma tartibida.",
                      "Skanerlar aniq, to'liq sahifa, muhr ko'rinadi.", "Fayl nomlari tushunarli va bir xil formatda.",
                      "Imzo talab qilingan har forma imzolangan va sanalangan.", "Ism hamma hujjatda pasport bilan bir xil.",
                      "Shablon qoldiqlari yo'q.", "Sertifikatlar muddati o'tmagan.",
                      "Ikkinchi shaxs tekshiruvi o'tkazilgan.", "Hamma narsaning zaxira nusxasi va skrinshoti bor."]),
    art_title="Topshirish paketi va taqvim", art_short="Paket",
    art=[("Muddatlar (Toshkent vaqti)", ["a1"]), ("Teskari taqvim", ["cal", "a4"]), ("Paket ro'yxati", ["pk", "a2"]),
         ("Ikkinchi shaxs tekshiruvi", ["tek", "a3"]), ("Trek va yo'l", ["yol7"])],
    tip="Arizani yuborgandan keyin portaldagi har sahifani PDF yoki skrinshot qilib saqlang. Keyingi bosqichda nimani yozganingizni aniq bilishingiz kerak.",
    sources=STD,
    js="""window.KGTool = { init: function () {
  var inp = document.getElementById("f_dl"), out = document.getElementById("toolOut");
  var ST = [[84, "Hujjatlar roʻyxati va universitet tanlovi (M1, M2)"], [70, "Apostil va tarjima boshlangan; tavsiya soʻralgan (M4)"], [56, "Dalillar inventari (M3); professorga xatlar"], [42, "Bayonot va reja qoralamalari (M5, M6)"], [28, "Oʻzaro tahrir; tavsiya xati olingan"], [14, "Yakuniy versiyalar, paket, ikkinchi shaxs tekshiruvi"], [3, "Shaxsiy muddat: onlayn ariza yuborilgan"]];
  var MON = ["yan", "fev", "mar", "apr", "may", "iyn", "iyl", "avg", "sen", "okt", "noy", "dek"];
  function fmt(d) { return d.getDate() + "-" + MON[d.getMonth()] + " " + d.getFullYear(); }
  function run() {
    if (!inp.value) { out.hidden = true; return; }
    var dl = new Date(inp.value + "T00:00:00"), now = new Date(); now.setHours(0, 0, 0, 0);
    var lines = ST.map(function (s) { var d = new Date(dl.getTime() - s[0] * 86400000); return fmt(d) + (d < now ? " (oʻtgan)" : "") + ": " + s[1]; });
    var left = Math.round((dl - now) / 86400000);
    lines.push(fmt(dl) + ": rasmiy muddat, KST 18:00 boʻlsa Toshkentda 14:00" + (left >= 0 ? " (" + left + " kun qoldi)" : " (oʻtgan)"));
    out.hidden = false; out.textContent = lines.join("\\n");
    if (window.KG) { KG.S.notes.cal = lines.join("\\n"); KG.save(); }
  }
  inp.addEventListener("change", run); inp.addEventListener("input", run); run();
} };""",
)
