from _lib import les, body, lib
from common import G26, STD

L1 = dict(t="Professor tahlili va ilmiy xat (Core)", short="Xat", min=50, kind="✍ Xat", ic="telescope",
    hook="Doktorantura uchun professor bilan aloqa juda muhim: u sizning kundalik rahbaringiz bo'ladi. Xatingiz uning ishini o'qiganingizni texnik darajada ko'rsatishi kerak.",
    body=f"""<h4>Professor tahlili</h4>
<div class="tbl"><table><thead><tr><th>Nima</th><th>Qanday tekshiriladi</th></tr></thead><tbody>
<tr><td>Nashr trendi</td><td>So'nggi 3–5 yildagi maqolalar mavzusi qayerga siljiyapti</td></tr>
<tr><td>Guruh</td><td>Hozirgi doktorantlar, ularning mavzulari, bitiruvchilar qayerda</td></tr>
<tr><td>Sig'im</td><td>Laboratoriya sahifasida ochiq o'rin e'loni, loyihalar va grantlar</td></tr>
<tr><td>Hamkorlik nuqtasi</td><td>Uning maqolasidagi cheklov yoki ochiq savol va sizning usulingiz</td></tr>
</tbody></table></div>
<h4>Ilmiy xat (150–250 so'z)</h4>
<ol><li>Mavzu qatori: GKS-G doktorantura nomzodi + aniq yo'nalish.</li>
<li>Kimsiz: magistr, dissertatsiya mavzusi, asosiy natija (bir jumla).</li>
<li><b>Texnik izoh:</b> uning aniq maqolasiga (sarlavha, yil) bitta mazmunli izoh yoki savol: usulning cheklovi, kengaytirish imkoni.</li>
<li>Hamkorlik nuqtasi: sizning usulingiz yoki ma'lumotingiz shu savolga qanday qo'shiladi.</li>
<li>So'rov: shu sikl uchun laboratoriyada o'rin bormi, GKS arizasini qo'llab-quvvatlaydimi, qisqa onlayn suhbat mumkinmi.</li>
<li>Ilova: PhD CV va 1 sahifalik reja konspekti.</li></ol>
<div class="box warn">3 ta professor, har biriga alohida xat. Kafolat so'ramang; javob bo'lmasa 7–10 ish kunidan keyin bitta eslatma.</div>
<div class="srcs">Manba: {G26} (professor bilan aloqa yo'riqnomada majburiy emas).</div>""",
    take="Professorni nashr trendi, guruh, sig'im va hamkorlik nuqtasi bo'yicha tahlil qiling; xatda uning maqolasiga bitta texnik izoh bering.",
    task="<ul><li>3 professor tahlilini jadvalda yozing.</li><li>Birinchi professorga xat qoralamasini yozing (vositada).</li></ul>",
    ph="Prof. ... · trend · guruh · sig'im · hamkorlik nuqtasi")

L2 = dict(t="Onlayn ilmiy suhbat", short="Suhbat", min=40, kind="🎙 Mashq", ic="bell",
    hook="Professor javob berib, qisqa suhbat taklif qildi. Bu norasmiy intervyu: 20–30 daqiqada u siz bilan 3–4 yil ishlay olishini baholaydi.",
    body="""<h4>Tayyorgarlik</h4>
<ul><li>Uning so'nggi 3 maqolasini qayta o'qing; har biridan bitta savol tayyorlang.</li>
<li>Reja konspektingizni 5 daqiqalik bayonga aylantiring: muammo → savol → usul → nega shu laboratoriya.</li>
<li>Texnik tomondan: kamera, mikrofon, internet; vaqt mintaqasini tekshiring (Koreya Toshkentdan 4 soat oldinda).</li></ul>
<h4>Tanqidga javob</h4>
<ol><li>Savolni qayta ayting: to'g'ri tushunganingizni tasdiqlang.</li><li>Javob bering yoki ochiq ayting: \"Bu haqda hali o'ylamaganman; men buni ... orqali tekshirgan bo'lardim.\"</li><li>Tanqidni rejaga qanday qo'shishingizni ayting.</li></ol>
<h4>Sizning savollaringiz</h4>
<ul><li>Laboratoriyada doktorantning odatiy haftasi qanday?</li><li>Guruhdagi ish tili va seminarlar tartibi qanday?</li><li>Til yilida laboratoriya ishiga qanday qo'shilish mumkin?</li></ul>
<p>Savollar Kompas tuzgan ro'yxat; o'zingiznikini qo'shing.</p>
<div class="box info">Suhbatdan keyin 24 soat ichida qisqa rahmat xati va suhbatda kelishilgan keyingi qadamni yozing.</div>""",
    take="5 daqiqalik bayon, tanqidga uch qadamli javob, o'z savollaringiz va 24 soat ichida rahmat xati.",
    task="<ul><li>5 daqiqalik bayonni yozing va ovoz yozib mashq qiling.</li><li>Professorga beradigan 3 ta savolingizni yozing.</li></ul>",
    ph="Bayon: ... Savollar: 1) ...")

MOD = dict(
    title="Professor bilan muloqot va yakunlash",
    desc="GKS Lab M5-D (doktorantura): professor tahlili va ilmiy xat, onlayn ilmiy suhbat, shaxsiy bayonot va izchillik auditi, intervyu, natija va jo'nash. Natija: 3 professorga xat, reja konspekti, suhbat tayyorgarligi, yakuniy paket.",
    lead="Oxirgi modulda professor bilan aloqa, shaxsiy bayonot va yakuniy paket birlashadi. Hamma hujjatlardagi faktlar bir xil bo'lishi va intervyuda har jumlani himoya qila olishingiz kerak.",
    hero="bell", weeks="3", next="", next_href="",
    goals=[("telescope", "3 professorga xat va reja konspekti", "har biri uning ishiga texnik izoh bilan"),
           ("bell", "Suhbat tayyorgarligi", "5 daqiqalik bayon va savollar"),
           ("scroll", "Yakuniy paket", "izchillik auditi, intervyu va jo'nash rejasi")],
    warn="Sanalar va qoidalar 2026 GKS-G yo'riqnomasidan, 31.10.2026 holatiga; 2027 GKS-G yo'riqnomasi chiqqach yangilanadi. Xat, bayonot va reja konspektini o'zingiz yozasiz.",
    lessons=[
        L1, L2,
        les(5, 2, t="Shaxsiy bayonot va izchillik auditi", short="Audit", body=body(5, 1) + "\n" + body(6, 5),
            task="<ul><li>Bayonot skeletini yozing va to'liq matnni vositaga kiriting.</li><li>CV, ilmiy reja, bayonot va tavsiya beruvchiga berilgan varaqadagi faktlarni solishtiring.</li></ul>",
            ph="Mos kelmagan faktlar: ..."),
        les(8, 3, t="Intervyu, natija va jo'nash", short="Yakun", body=body(8, 1) + "\n" + body(8, 3) + "\n" + body(8, 4), kind="🎯 Mini-test",
            quiz=[("2026 GKS-G da NIIED ikkinchi bosqichida og'zaki intervyu yo'q.", "t", "To'g'ri: intervyu elchixona yoki universitet bosqichida."),
                  ("2026 GKS-G da Koreyaga kirishdan oldingi sug'urta badallari qoplanadi.", "n", "Noto'g'ri: yo'riqnomaga ko'ra qoplanmaydi."),
                  ("Universitet tanlovi muddatini o'tkazib yuborish xavfli, chunki tanlov qisqa vaqtda qilinadi.", "t", "To'g'ri: 2026 siklida 12-iyun, 18:00 (KST)."),
                  ("Intervyu javoblarini so'zma-so'z yodlash eng yaxshi usul.", "n", "Noto'g'ri: kalit so'zlar va misol bilan mashq qiling.")],
            task="<ul><li>Intervyu uchun 5 asosiy savolga kalit so'zlar va misol yozing.</li><li>Jo'nash oldi ro'yxatini va B-rejani yozing.</li></ul>",
            ph="Savollar: ... Jo'nash: ... B-reja: ..."),
    ],
    tool=dict(id="yakun-d", short="Paket", h2="Xatlar, bayonot va yakuniy paket", sub="Doktorantura arizasining yakuniy materiallari.",
              h3="Yakuniy paket", tag="5 maydon", ic="bell", btn="Paketni saqlash", badge="Hamkor", min=4,
              fields=[dict(k="mail1", label="1-professorga xat", type="area", wc="150-250", ph="Subject: ..."),
                      dict(k="consp", label="1 sahifalik reja konspekti", type="area", wc="250-400", ph="Muammo · savol · usul · nega shu laboratoriya · vaqt"),
                      dict(k="full", label="Shaxsiy bayonot (to'liq matn)", type="area", wc="450-900", ph=""),
                      dict(k="audit", label="Izchillik auditi", type="area", ph="Fakt · hujjatlar · mos/mos emas"),
                      dict(k="dep", label="Jo'nash oldi ro'yxati yoki B-reja", type="area", ph="")]),
    check=dict(h2="Yakuniy nazorat", sub="Yuborish va suhbatdan oldin.", h3="10 bandlik nazorat",
               items=["3 professor tahlil qilingan; har xat alohida.", "Har xatda maqolaga texnik izoh va bitta aniq so'rov.",
                      "Reja konspekti 1 sahifadan oshmaydi.", "Suhbat uchun 5 daqiqalik bayon mashq qilingan.",
                      "Bayonot forma bandlariga javob beradi va ilmiy rejani takrorlamaydi.", "Nashr, sana, baho barcha hujjatlarda bir xil.",
                      "Barcha muddatlar Toshkent vaqtiga o'girilgan.", "Paket yo'riqnoma tartibida, ikkinchi shaxs tekshirgan.",
                      "Jo'nash oldi ro'yxati rasmiy manbalardan.", "B-reja yozilgan."]),
    art_title="Professor bilan muloqot va yakuniy paket", art_short="Paket",
    art=[("Professorlar tahlili", ["a1"]), ("1-professorga xat", ["mail1"]), ("Reja konspekti", ["consp"]),
         ("Suhbat tayyorgarligi", ["a2"]), ("Shaxsiy bayonot va audit", ["full", "audit", "a3"]), ("Intervyu, jo'nash va B-reja", ["dep", "a4"])],
    tip="Professor bilan suhbatdan keyin u sizni bir jumlada qanday tasvirlashini o'ylab ko'ring. Shu jumla sizning ilmiy rejangiz bilan bir xil bo'lishi kerak.",
    sources=STD,
)
