from common import SIK, MEXT, CAMPUSCHINA, SIC, SH, SH_UZ, TB, DSU, FTC, HOL, STD

MOD = dict(
    title="Davlat stipendiyalari",
    desc="Bachelor Lab M11: stipendiyalar manzarasi, GKS va MEXT bakalavriat yo'nalishlari, Xitoy hukumati stipendiyasi (CSC), Stipendium Hungaricum va Italiya DSU, Türkiye Bursları va boshqa dasturlarni tekshirish. Natija: 5–8 dasturli stipendiya ro'yxati.",
    lead="Davlat stipendiyalari xorijda bakalavr o'qishning eng to'liq moliyalashtirish yo'llaridan biri. Har birining o'z muvofiqlik shartlari, ariza kanali va majburiyatlari bor. Bu modulda ularni bitta mezon bilan baholaysiz va o'zingizga mos 5–8 dasturni tanlaysiz.",
    hero="money", weeks="2", next="M12 Universitet grantlari va moliyaviy reja", next_href="bachelor-lab-m12.html",
    goals=[("money", "Stipendiya ro'yxati", "5–8 dastur, rasmiy havola bilan"),
           ("shield", "Muvofiqlik tekshiruvi", "fuqarolik, yosh, baho, til, daraja"),
           ("scroll", "Majburiyatlar xaritasi", "qaytish sharti, til yili, o'qish yo'nalishi cheklovi")],
    warn=f"Stipendiya shartlari, kvotalari va muddatlari har yili yangi e'londa chiqadi. Bu moduldagi ma'lumot {HOL}; ariza berishdan oldin joriy yil yo'riqnomasini to'liq o'qing. Hech kim stipendiyani kafolatlay olmaydi.",
    lessons=[
        dict(t="Stipendiyalar manzarasi", short="Manzara", min=25, kind="🎯 Mini-test", ic="compass",
             hook="Stipendiya lotereya emas, shartlari yozilgan dastur. Shartni o'qimasdan ariza berish vaqtni yo'qotadi, shartni o'qib berish esa imkoniyatni oshiradi.",
             body="""<h4>Uch manba</h4>
<div class="tbl"><table><thead><tr><th>Manba</th><th>Kim beradi</th><th>Misol</th></tr></thead><tbody>
<tr><td>Davlat</td><td>Qabul qiluvchi mamlakat hukumati</td><td>GKS, MEXT, CSC, Stipendium Hungaricum, Türkiye Bursları</td></tr>
<tr><td>Universitet</td><td>Universitetning o'zi (M12)</td><td>Ehtiyojga yoki yutuqqa asoslangan grantlar</td></tr>
<tr><td>Tashkilot</td><td>Jamg'arma, kompaniya</td><td>Har biri alohida tekshiriladi</td></tr>
</tbody></table></div>
<h4>To'liq va qisman</h4>
<p>To'liq stipendiya odatda o'qish to'lovi, oylik nafaqa, ba'zan aviabilet, sug'urta va til yilini qoplaydi. Qisman stipendiya faqat o'qish to'lovining bir qismini qoplaydi; qolganini boshqa manbadan topish kerak.</p>
<h4>Muvofiqlik shartlarini o'qish</h4>
<ol><li><b>Fuqarolik</b>: O'zbekiston hamkor davlatlar ro'yxatidami?</li><li><b>Yosh</b>: yuqori chegara ko'pincha aniq sana bilan beriladi.</li><li><b>Baho</b>: minimal o'rtacha yoki foiz.</li><li><b>Til</b>: sertifikat talab qilinadimi yoki til yili beriladimi.</li><li><b>Daraja va soha</b>: bakalavr uchun ochiqmi, qaysi sohalar.</li><li><b>Cheklovlar</b>: boshqa stipendiya bilan birga olish, qayta ariza.</li></ol>
<div class="box warn">\"Stipendiyani kafolatlaymiz\" degan agent yoki kanal firibgar bo'lishi ehtimoli yuqori. Davlat stipendiyalariga ariza rasmiy portal orqali va odatda bepul beriladi (M12 L5).</div>""",
             take="Stipendiya davlat, universitet yoki tashkilotdan; to'liq yoki qisman. Avval olti muvofiqlik shartini tekshiring, keyin vaqt sarflang.",
             quiz=[("Qisman stipendiya hamma xarajatni qoplaydi.", "n", "Noto'g'ri: odatda faqat o'qish to'lovining bir qismini."),
                   ("Davlat stipendiyasiga ariza odatda rasmiy portal orqali beriladi.", "t", "To'g'ri: agent shart emas."),
                   ("Yosh chegarasi aniq sana bilan berilishi mumkin.", "t", "To'g'ri: masalan, \"... yildan keyin tug'ilgan\"."),
                   ("Agent to'lov evaziga stipendiyani kafolatlay oladi.", "n", "Noto'g'ri: hech kim kafolat bera olmaydi.")],
             task="<ul><li>Sizga qiziq 6–8 stipendiyaning nomini va rasmiy saytini yozing.</li><li>Har biri uchun olti muvofiqlik shartidan qaysi biri sizga to'sqinlik qilishi mumkinligini belgilang.</li></ul>",
             ph="1) GKS-U — sayt: ... ; to'siq: ... 2) ..."),
        dict(t="Koreya va Yaponiya", short="GKS, MEXT", min=30, kind="🗺 Ikki trek", ic="gks",
             hook="GKS va MEXT bakalavriat stipendiyalari to'liq moliyalashtirish va til yilini beradi. Ikkalasida ham ariza kanali (trek) strategik qaror.",
             body=f"""<h4>GKS bakalavriat (GKS-U), Koreya</h4>
<ul><li>Odatda qoplaydi: aviabilet, o'qish to'lovi, oylik nafaqa, joylashish puli, tibbiy sug'urta va bir yillik koreys tili kursi.</li>
<li>Ikki asosiy trek: <b>elchixona treki</b> (Koreya elchixonasi orqali, mamlakat kvotasi bilan) va <b>universitet treki</b> (to'g'ridan-to'g'ri Koreya universitetiga). Bir siklda odatda bitta trek tanlanadi.</li>
<li>Muvofiqlik: Koreya fuqarosi bo'lmaslik, yosh chegarasi, baho talabi (masalan 100 ballik shkalada 80 yoki sinfda yuqori 20 foiz). Aniq qiymatlar joriy yo'riqnomada.</li>
<li>Batafsil tayyorgarlik: <a href="gks-lab.html">GKS Lab</a>.</li></ul>
<h4>MEXT bakalavriat, Yaponiya</h4>
<ul><li>Yaponiya Ta'lim vazirligi (MEXT) stipendiyasi: odatda o'qish to'lovi, oylik nafaqa, aviabilet va bir yillik tayyorlov (yapon tili va asosiy fanlar).</li>
<li>Bakalavr uchun asosiy kanal: <b>elchixona tavsiyasi</b> (Yaponiya elchixonasi orqali yozma imtihon va intervyu). Ba'zi universitetlar o'z tavsiyasi bilan ham nomzod ko'rsatadi.</li>
<li>Yozma imtihon (matematika, fan, til) jiddiy tayyorgarlik talab qiladi.</li>
<li>MEXT Lab tayyorlanmoqda; hozircha rasmiy manbalar.</li></ul>
<div class="box info">Trek tanlovi: elchixona trekida raqobat mamlakat ichida, universitet trekida universitetga qarab. O'z profilingizga qarab tanlang va yo'riqnomadagi qoidani o'qing.</div>
<div class="srcs">Manba: {SIK}; {MEXT}. {HOL}.</div>""",
             take="GKS-U va MEXT to'liq stipendiya va til yilini beradi. GKS'da elchixona yoki universitet treki, MEXT'da asosan elchixona tavsiyasi va yozma imtihon.",
             task="<ul><li>GKS-U va MEXT uchun muvofiqlik shartlarini joriy yo'riqnomadan yozing.</li><li>Ikkalasidan biri mos bo'lsa, trekni va sababini yozing.</li></ul>",
             ph="GKS-U: yosh ..., baho ..., trek: ... chunki ... MEXT: ..."),
        dict(t="Xitoy hukumati stipendiyasi (CSC)", short="CSC", min=30, kind="🧭 Kanallar", ic="books",
             hook="Xitoy hukumati stipendiyasi bir nechta kanal orqali beriladi. Kanalni noto'g'ri tushunish ko'p o'quvchining arizasini boshidan to'xtatadi.",
             body=f"""<h4>Kanallar</h4>
<div class="tbl"><table><thead><tr><th>Kanal</th><th>Qanday</th><th>Ariza kimga</th></tr></thead><tbody>
<tr><td>Ikki tomonlama dastur (ko'pincha \"A turi\" deb ataladi)</td><td>Xitoy elchixonasi yoki mamlakatdagi mas'ul tashkilot orqali</td><td>Elchixona/mas'ul tashkilot va CSC portali</td></tr>
<tr><td>Universitet dasturi (\"B turi\")</td><td>Xitoy universiteti nomzodlarni tanlab, CSC ga tavsiya qiladi</td><td>Universitetning o'zi va CSC portali</td></tr>
<tr><td>Boshqa maxsus dasturlar</td><td>Muayyan kelishuv yoki mintaqa uchun</td><td>E'longa qarab</td></tr>
</tbody></table></div>
<h4>Hujjatlar (odatda)</h4>
<p>CSC portalidagi ariza formasi, attestat va baholar (notarial tarjima), o'qish rejasi, tavsiya xatlari, tibbiy ko'rik formasi ([[Foreigner Physical Examination Form]]), pasport, til sertifikati.</p>
<h4>Universitet va til tanlash</h4>
<ul><li>Bakalavr dasturlarining ko'pi xitoy tilida; stipendiya bir yillik til tayyorlovini o'z ichiga olishi mumkin.</li><li>Ingliz tilidagi bakalavr dasturlari cheklangan; har universitet ro'yxatini alohida tekshiring.</li><li>Sohangiz bo'yicha kuchli universitetni tanlang (M2), keyin uning CSC kanalini.</li></ul>
<div class="box warn">CSC portalida ariza bepul. \"Universitetdan qabul xati olib beramiz\" deb pul so'raydigan vositachilardan ehtiyot bo'ling; universitet xalqaro bo'limi bilan to'g'ridan-to'g'ri yozishing.</div>
<div class="srcs">Manba: {CAMPUSCHINA}; {SIC}; universitetlarning xalqaro talabalar sahifalari. {HOL}.</div>""",
             take="CSC ikki tomonlama (elchixona) va universitet kanallari orqali beriladi. Avval sohangiz bo'yicha universitet va til, keyin kanal.",
             task="<ul><li>Sohangiz bo'yicha 2 Xitoy universitetini toping va ularning CSC kanalini yozing.</li><li>Dastur tili va til yili bor-yo'qligini yozing.</li></ul>",
             ph="... universiteti — kanal: ..., til: ..., til yili: ..."),
        dict(t="Vengriya va Italiya", short="SH, DSU", min=30, kind="🗺 Yevropa", ic="seedling",
             hook="Vengriya va Italiyada davlat ta'limini moliyalashtirishning ikki xil mantig'i bor: biri hukumatlararo stipendiya, ikkinchisi ehtiyojga asoslangan mintaqaviy yordam.",
             body=f"""<h4>Stipendium Hungaricum (Vengriya)</h4>
<ul><li>Vengriya hukumatining ikki tomonlama kelishuvlar asosidagi stipendiyasi. O'zbekiston hamkor davlat; O'zbekiston tomonidan mas'ul tashkilot ([[Sending Partner]]) Oliy ta'lim, fan va innovatsiyalar vazirligi.</li>
<li>gov.uz e'loniga ko'ra (25.12.2024), 2025/2026 o'quv yili uchun O'zbekistonga 170 tagacha o'rin ajratilgan; ariza Vengriyadagi koordinator, Tempus jamg'armasi platformasi orqali onlayn beriladi. Keyingi yillar kvotasi va muddati yangi e'londa.</li>
<li>Odatda qoplaydi: o'qish to'lovidan ozod qilish, oylik nafaqa, yotoqxona yoki turar joy uchun hissa, tibbiy sug'urta.</li></ul>
<h4>Italiya: mintaqaviy ta'lim huquqi stipendiyalari (DSU)</h4>
<ul><li>Bu yagona davlat dasturi emas: har mintaqaning o'z agentligi ([[diritto allo studio]]) bor va xalqaro talabalar ham ariza bera oladi.</li>
<li>Asosan <b>ehtiyojga asoslangan</b>: oila daromadi va mulki haqidagi hujjatlar (xalqaro talabalar uchun maxsus hisoblangan ko'rsatkich) talab qilinadi. Bu hujjatlarni O'zbekistonda tayyorlash, tarjima va legallashtirish vaqt oladi.</li>
<li>Odatda: pul stipendiyasi, yotoqxona, ovqatlanish va o'qish to'lovidan ozod qilish. Keyingi yillarda baho (kreditlar) sharti bor.</li>
<li>12 yillik ta'lim talabini unutmang (M1).</li></ul>
<div class="srcs">Manba: {SH}; {SH_UZ}; {DSU}; tegishli mintaqaviy DSU agentliklari sahifalari. {HOL}.</div>""",
             take="Stipendium Hungaricum: O'zbekiston hamkor, Tempus platformasi orqali ariza. Italiya DSU: mintaqaviy, ehtiyojga asoslangan, daromad hujjatlari erta tayyorlanadi.",
             task="<ul><li>Stipendium Hungaricum joriy yil e'lonini toping va muddat hamda sohangizdagi dasturlarni yozing.</li><li>Italiya qiziq bo'lsa, bitta mintaqa DSU agentligining xalqaro talabalar uchun hujjatlar ro'yxatini yozing.</li></ul>",
             ph="SH: e'lon ..., muddat ..., dasturlar ... DSU (...): hujjatlar ..."),
        dict(t="Turkiya va boshqalar", short="Türkiye", min=25, kind="🛠 Baholash", ic="shield",
             hook="Türkiye Bursları bitta onlayn ariza bilan ko'p universitetni qamrab oladi. Boshqa dasturlarni esa bitta universal mezon bilan tez baholashni o'rganasiz.",
             body=f"""<h4>Türkiye Bursları</h4>
<ul><li>Turkiya hukumati stipendiyasi; bitta onlayn ariza orqali bir nechta universitet va dastur tanlanadi.</li><li>Odatda qoplaydi: o'qish to'lovi, oylik nafaqa, yotoqxona, tibbiy sug'urta, bir martalik aviabilet va bir yillik turk tili kursi.</li><li>Tanlov: hujjatlar va intervyu. Ariza oynasi odatda yilning boshida; joriy e'lonni rasmiy saytdan tekshiring.</li></ul>
<h4>Universal baholash: 6 nuqta</h4>
<div class="tbl"><table><thead><tr><th>№</th><th>Mezon</th><th>Savol</th></tr></thead><tbody>
<tr><td>1</td><td>Muvofiqlik</td><td>Fuqarolik, yosh, baho, daraja mosmi? (majburiy shart)</td></tr>
<tr><td>2</td><td>Qoplov</td><td>To'liqmi yoki qisman? Nima kiradi?</td></tr>
<tr><td>3</td><td>Kanal</td><td>Elchixona, universitet yoki to'g'ridan-to'g'ri?</td></tr>
<tr><td>4</td><td>Muddat</td><td>Hujjatlarga ulguraman?</td></tr>
<tr><td>5</td><td>Raqobat</td><td>Profilim qanchalik mos?</td></tr>
<tr><td>6</td><td>Majburiyat</td><td>Qaytish sharti, xizmat, soha cheklovi bormi va u menga maqbulmi?</td></tr>
</tbody></table></div>
<p>Muvofiqlik \"yo'q\" bo'lsa, boshqa mezonlarni ko'rmang: dastur siz uchun emas.</p>
<div class="box warn">Stipendiya e'lonini faqat rasmiy saytdan oling. Telegram kanallaridagi \"to'liq stipendiya, hujjatsiz\" e'lonlarining ko'pi firibgarlik yoki eskirgan.</div>
<div class="srcs">Manba: {TB}; {FTC}. {HOL}.</div>""",
             take="Türkiye Bursları: bitta onlayn ariza, to'liq qoplov va til yili. Har dasturni 6 nuqta bilan baholang; muvofiqlik majburiy shart: u bajarilmasa, qolgan ball hisobga olinmaydi.",
             task="<ul><li>Pastdagi vositada 5–8 dasturni 6 nuqta bo'yicha baholang.</li><li>Eng mos 3 tasini ustuvor deb belgilang.</li></ul>",
             ph="Türkiye Bursları: muvofiqlik ha, qoplov to'liq, kanal onlayn, muddat ..., raqobat ..., majburiyat ..."),
    ],
    tool=dict(id="royxat", short="Ro'yxat", h2="Stipendiya ro'yxati", sub="5–8 dastur: muvofiqlik, qoplov, kanal, muddat, majburiyat va rasmiy havola.",
              h3="Stipendiya ro'yxati", tag="5 maydon", ic="money", btn="Ro'yxatni saqlash", badge="Stipendiya izlovchi", min=4,
              fields=[dict(k="s13", label="1–3 dastur (ustuvor)", hint="nomi · mamlakat · muvofiqlik · qoplov · kanal · muddat · majburiyat · havola", type="area", ph="GKS-U · Koreya · mos · to'liq · elchixona · ... · til yili · https://..."),
                      dict(k="s48", label="4–8 dastur", type="area", ph="..."),
                      dict(k="mos_emas", label="Mos kelmagan dasturlar va sababi", type="area", ph="... — yosh chegarasi"),
                      dict(k="hujjat", label="Stipendiyalar uchun umumiy hujjatlar", type="area", ph="Attestat (apostil), tavsiya xatlari, o'qish rejasi ..."),
                      dict(k="reja", label="Keyingi qadamlar", hint="sana bilan", type="area", ph="Joriy e'lonni kuzatish: ..., hujjat: ...")]),
    check=dict(h2="Stipendiya nazorati", sub="Ro'yxatni yakunlashdan oldin tekshiring.", h3="8 bandlik nazorat",
               items=["Har dastur rasmiy saytdan olingan, Telegram e'lonidan emas.", "Muvofiqlik har dastur uchun tekshirilgan.",
                      "Qoplov to'liq yoki qisman ekani yozilgan.", "Ariza kanali (trek) aniqlangan.", "Muddat joriy e'londan yoki \"kutilmoqda\" deb belgilangan.",
                      "Majburiyatlar (qaytish, til yili, soha) o'qilgan.", "Hech qanday agentga to'lov qilinmaydi.", "Ro'yxatda 5–8 dastur bor."]),
    art_title="Stipendiya ro'yxati", art_short="Stipendiya",
    art=[("Manzara va muvofiqlik", ["a1"]), ("Ustuvor dasturlar (1–3)", ["s13"]), ("Boshqa dasturlar (4–8)", ["s48"]),
         ("Koreya, Yaponiya, Xitoy", ["a2", "a3"]), ("Vengriya, Italiya, Turkiya", ["a4", "a5"]), ("Mos kelmaganlar", ["mos_emas"]),
         ("Umumiy hujjatlar", ["hujjat"]), ("Keyingi qadamlar", ["reja"])],
    tip="Har stipendiya e'lonini PDF qilib saqlang va yonidagi sanani yozing. Keyingi yil shartlar o'zgarsa, nimani o'zgarganini darhol ko'rasiz.",
    sources=f"{SIK}; {MEXT}; {CAMPUSCHINA}; {SIC}; {SH}; {SH_UZ}; {TB}; {DSU}; {FTC}. {STD}",
    js="""window.KGTool = { check: function () {
  var t = (KG.nv("s13") + "\\n" + KG.nv("s48")).split(/\\n+/).filter(function (x) { return x.trim().length > 3; }).length;
  return t < 5 ? ("Roʻyxatda kamida 5 dastur boʻlsin (hozir " + t + " qator)") : "";
} };""",
)
