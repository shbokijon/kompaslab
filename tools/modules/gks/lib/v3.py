from common import U27, G26, STD

MOD = dict(
    title="Nomzod profili va dalillar",
    desc="GKS Lab M3: dalillar inventari STAR usulida, faoliyat va yutuqlarni ariza formasiga tayyorlash, zaif tomonlarni tushuntirish va o'sish traektoriyasi. Natija: dalillar inventari va profil izohi.",
    lead="Shaxsiy bayonot va o'quv rejasi dalilsiz bo'sh gapga aylanadi. Bu modulda yozishdan oldin xom ashyoni yig'asiz: nima qilgansiz, qanday natija bilan, qaysi hujjat tasdiqlaydi.",
    hero="bulb", weeks="2", next="Tavsiya xati va professor bilan aloqa",
    goals=[("bulb", "Dalillar inventari", "kamida 3 ta STAR yozuvi, har biri tekshiriladigan natija bilan"),
           ("shield", "Zaif tomon javobi", "past baho, tanaffus yoki yo'nalish o'zgarishi uchun"),
           ("seedling", "Profil izohi", "o'sish traektoriyasi bir paragrafda")],
    warn="Bu modul formalarni to'ldirmaydi, ular uchun material tayyorlaydi. Ariza formasidagi bo'limlar va mukofotlar soni har yil yo'riqnomada belgilanadi (2027 GKS-U da mukofot va sertifikatlar beshtagacha).",
    lessons=[
        dict(t="Dalillar inventari: STAR usuli", short="STAR", min=40, kind="🛠 STAR yozuvi", ic="bulb",
             hook="\"Men mas'uliyatli va tirishqoqman\" degan jumlani har nomzod yozadi va komissiya uni o'qimaydi. Bitta aniq voqea, raqam va natija esa esda qoladi.",
             body=f"""<p>STAR (Vaziyat, Vazifa, Harakat, Natija) har tajribani tekshiriladigan dalilga aylantiradi:</p>
<div class="tbl"><table><thead><tr><th>Qism</th><th>Savol</th><th>Xato</th></tr></thead><tbody>
<tr><td><b>Vaziyat</b></td><td>Qayerda, qachon, qanday sharoitda?</td><td>Uzun fon hikoyasi</td></tr>
<tr><td><b>Vazifa</b></td><td>Sizdan nima talab qilingan yoki o'zingiz nimani maqsad qilgansiz?</td><td>Jamoa vazifasini o'zinikidek berish</td></tr>
<tr><td><b>Harakat</b></td><td>Aynan siz nima qildingiz, qanday usul bilan?</td><td>\"Biz qildik\" deb shaxsiy hissani yashirish</td></tr>
<tr><td><b>Natija</b></td><td>Nima o'zgardi? Raqam, mukofot, mahsulot, saboq</td><td>Tekshirib bo'lmaydigan da'vo</td></tr>
</tbody></table></div>
<h4>Qayerdan dalil izlash</h4>
<ul><li><span class="trk">U</span> Olimpiada va tanlovlar, mustaqil loyiha, o'z-o'zini o'qitish (onlayn kurs + nima qurdingiz), jamoaviy tashabbus, oilaviy mas'uliyat.</li>
<li><span class="trk">M</span> Kurs ishi, bitiruv ishi, laboratoriya, amaliyot, dasturiy vositalar, taqdimotlar.</li>
<li><span class="trk">D</span> Magistrlik dissertatsiyasi, nashr va konferensiyalar, grant yoki loyihadagi rol, o'qitish tajribasi.</li></ul>
<div class="box info"><b>Kompas tuzgan namuna</b> (shartli): <i>Vaziyat:</i> maktabdagi fizika to'garagida tajriba asboblari yo'q edi. <i>Vazifa:</i> 9-sinf uchun mayatnik tajribasini o'tkazish. <i>Harakat:</i> telefon sensori va bepul ilova bilan o'lchash usulini tuzdim, 12 o'quvchiga o'rgatdim. <i>Natija:</i> to'garak 3 ta yangi tajribani shu usulda o'tkazdi; usulni viloyat ko'rgazmasida ko'rsatdim (sertifikat bor).</div>""",
             take="Har tajribani Vaziyat → Vazifa → Harakat → Natija qatoriga keltiring; natija tekshiriladigan bo'lsin, shaxsiy hissangiz aniq ko'rinsin.",
             task="<ul><li>Kamida 3 ta tajribangizni STAR shaklida yozing. Har biri yoniga tasdiqlovchi hujjatni qo'shing (sertifikat, havola, rahbar).</li></ul>",
             ph="1) V: ... V: ... H: ... N: ... (hujjat: ...)"),
        dict(t="Faoliyat va yutuqlarni formaga tayyorlash", short="Yutuq", min=30, kind="🎯 Mini-test", ic="scroll",
             hook="Ariza formasidagi faoliyat va mukofot bo'limlari kichik. Joy cheklangan joyda har qator saralangan bo'lishi kerak.",
             body=f"""<h4>Tanlash qoidasi</h4>
<ul><li><b>Tegishlilik:</b> tanlagan yo'nalishingizga yaqin yutuq birinchi.</li>
<li><b>Daraja:</b> xalqaro → respublika → viloyat → maktab/universitet.</li>
<li><b>Yaqinlik:</b> so'nggi 3–4 yil. <span class="trk">U</span> uchun 9–11-sinf (litsey, kollej) yillari asosiy.</li>
<li><b>Tasdiq:</b> hujjati yo'q yutuqni yozmang. 2027 GKS-U da mukofot va sertifikatlar ixtiyoriy, beshtagacha ilova qilinadi.</li></ul>
<h4>Bitta qator formati</h4>
<div class="out" style="white-space:normal"><span lang="en">Regional Physics Olympiad, 2nd place (of 140 participants), Tashkent region, 2025</span></div>
<p style="margin-top:8px">Qatnashchilar soni faqat rasmiy hujjatda bo'lsa yoziladi. Namuna Kompas tomonidan tuzilgan.</p>
<h4><span class="trk">M</span> <span class="trk">D</span> Akademik CV</h4>
<p>Agar universitet yoki dastur alohida CV so'rasa, akademik CV tartibi: ta'lim, tadqiqot tajribasi, nashrlar va taqdimotlar, mukofotlar, ko'nikmalar, tillar. Har tajriba qatori harakat fe'li bilan boshlanadi va natijaga ega bo'ladi. Fotosurat, oilaviy holat kabi ma'lumotlar talab qilinmasa qo'yilmaydi.</p>
<div class="srcs">Manba: {U27}; {G26}.</div>""",
             take="Har qator tegishli, yaqin, tasdiqlangan bo'lsin. Joy kam bo'lsa, kamroq lekin kuchliroq yutuqni qoldiring.",
             quiz=[("Hujjati bo'lmagan yutuqni ham formaga yozish mumkin, chunki komissiya tekshirmaydi.", "n", "Noto'g'ri: yutuqlar tasdiqlovchi hujjat bilan; farq ishonchni yo'qotadi."),
                   ("2027 GKS-U da mukofot va sertifikatlar ixtiyoriy, beshtagacha.", "t", "To'g'ri."),
                   ("Faoliyat ro'yxatida yo'nalishga yaqin yutuq birinchi turishi kerak.", "t", "To'g'ri: tegishlilik birinchi mezon."),
                   ("STAR da \"Harakat\" qismida jamoa nima qilganini yozish yetarli.", "n", "Noto'g'ri: aynan siz nima qilganingiz ko'rinishi kerak.")],
             task="<ul><li>Barcha yutuqlaringizni yozing, keyin 4 mezon bo'yicha eng kuchli 5 tasini tanlang.</li></ul>",
             ph="Tanlangan 5 ta: 1) ... (hujjat: ...)"),
        dict(t="Zaif tomonlarni boshqarish", short="Zaif", min=30, kind="✍ Izoh", ic="shield",
             hook="Past baho, bo'sh yil yoki yo'nalish o'zgarishini yashirsangiz, komissiya o'zi topadi va eng yomon tushuntirishni tanlaydi.",
             body=f"""<h4>Uch qadamli javob</h4>
<ol><li><b>Fakt:</b> nima bo'lgan, qisqa va aniq (bahona emas).</li>
<li><b>Javobgarlik va tuzatish:</b> nima qildingiz, qanday natija bilan.</li>
<li><b>Hozirgi dalil:</b> muammo takrorlanmasligini ko'rsatadigan yangi fakt.</li></ol>
<div class="tbl"><table><thead><tr><th>Holat</th><th>Kuchsiz javob</th><th>Kuchli javob</th></tr></thead><tbody>
<tr><td>Bir semestr past baho</td><td>\"O'qituvchi adolatsiz edi\"</td><td>Oiladagi vaziyat sababli semestr pasaygan; keyingi 3 semestr o'rtachasi tiklangan (transkript)</td></tr>
<tr><td>Bo'sh yil</td><td>Izohsiz qoldirish</td><td>Ishladim va kurs o'tdim: nima, qancha vaqt, qanday natija</td></tr>
<tr><td>Yo'nalish o'zgarishi</td><td>\"Avvalgisi qiziq emas edi\"</td><td>Eski sohadan olib kelinadigan ko'nikma va yangisiga o'tish uchun qilingan qadamlar</td></tr>
</tbody></table></div>
<div class="box warn">Zaif tomonni bayonotning markaziga qo'ymang. Bir–ikki jumla, kerakli joyda. Yo'riqnomadagi minimal baho talabiga mos kelmasangiz, tushuntirish yordam bermaydi: bu holda boshqa sikl yoki boshqa yo'lni ko'rib chiqing (M1).</div>""",
             take="Zaif tomonni fakt → tuzatish → hozirgi dalil tartibida qisqa tushuntiring; yashirmang va markazga ham qo'ymang.",
             task="<ul><li>Profilingizdagi bitta zaif nuqtani aniqlang va uch qadamli javobini yozing (60–100 so'z).</li></ul>",
             ph="Fakt: ... Tuzatish: ... Hozirgi dalil: ..."),
        dict(t="O'sish traektoriyasi va profil izohi", short="Profil", min=30, kind="✍ Profil", ic="seedling",
             hook="Komissiya bir nechta yutuqni emas, yo'nalishni ko'rmoqchi: siz qayerdan qayerga ketyapsiz va bu yo'l Koreyadagi dasturga qanday ulanadi?",
             body="""<h4>Kuzatuv → savol → harakat zanjiri</h4>
<p>Qiziqish qayerdan kelganini ko'rsatishning eng ishonchli usuli: <b>nimani kuzatdingiz</b>, <b>qanday savol tug'ildi</b>, <b>javob izlab nima qildingiz</b>. Har bo'g'in bitta dalil bilan.</p>
<h4>Profil izohi tuzilmasi (bir paragraf)</h4>
<ol><li>Bugungi nuqta: daraja, soha, eng kuchli dalil.</li>
<li>Traektoriya: 2–3 bosqich, har birida nima o'rgandingiz.</li>
<li>Bo'shliq: hali nimani bilmaysiz yoki qila olmaysiz.</li>
<li>Keyingi qadam: nega aynan Koreyadagi dastur shu bo'shliqni yopadi.</li></ol>
<div class="box info">Bu paragraf M5 (shaxsiy bayonot) va M6 (o'quv rejasi) uchun umurtqa. Uni hozir aniq yozsangiz, keyingi hujjatlar bir-biriga zid bo'lmaydi.</div>
<div class="box warn">\"Bolaligimdan orzu qilardim\" kabi umumiy ochilishlardan qoching. Traektoriya sanalar va dalillar bilan quriladi.</div>""",
             take="Profil izohi: bugungi nuqta → traektoriya → bo'shliq → keyingi qadam. Bu paragraf keyingi hujjatlarning umurtqasi.",
             task="<ul><li>Profil izohini 120–180 so'zda yozing. Har jumla uchun dalil bormi? Tekshiring.</li></ul>",
             ph="Hozir men ... Avval ... keyin ... Hali ... Shuning uchun ..."),
    ],
    tool=dict(id="inventar", short="Inventar", h2="Dalillar inventari", sub="Eng kuchli uchta dalilingiz va profil izohingiz. Keyingi modullar shu materialdan foydalanadi.",
              h3="3 dalil + profil", tag="STAR va profil", ic="bulb", btn="Inventarni saqlash", badge="Dalilchi", min=4,
              fields=[dict(k="s1", label="1-dalil (STAR)", type="area", ph="V: ... V: ... H: ... N: ... Hujjat: ..."),
                      dict(k="s2", label="2-dalil (STAR)", type="area", ph=""),
                      dict(k="s3", label="3-dalil (STAR)", type="area", ph=""),
                      dict(k="weak", label="Zaif tomon javobi", type="area", ph="Fakt → tuzatish → hozirgi dalil"),
                      dict(k="prof", label="Profil izohi", type="area", wc="120-180", ph="Bugungi nuqta, traektoriya, bo'shliq, keyingi qadam")]),
    check=dict(h2="Profil nazorati", sub="Inventarni yakunlashdan oldin.", h3="8 bandlik nazorat",
               items=["Har STAR yozuvida shaxsiy harakat aniq (\"men\").", "Har natija raqam, hujjat yoki mahsulot bilan tekshiriladi.",
                      "Yutuqlar tegishlilik bo'yicha saralangan.", "Hujjati yo'q da'vo olib tashlangan.",
                      "Zaif tomon fakt → tuzatish → dalil tartibida.", "Profil izohida umumiy ochilish (\"bolaligimdan\") yo'q.",
                      "Profil izohi sanalar va dalillarga tayanadi.", "Material M5 va M6 uchun bir joyda saqlangan."]),
    art_title="Dalillar inventari va profil izohi", art_short="Inventar",
    art=[("Dalil 1", ["s1"]), ("Dalil 2", ["s2"]), ("Dalil 3", ["s3"]), ("STAR qoralamalari", ["a1"]), ("Tanlangan yutuqlar", ["a2"]),
         ("Zaif tomon izohi", ["weak", "a3"]), ("Profil izohi", ["prof", "a4"])],
    tip="Har jumladan keyin \"qanday bilasiz?\" deb so'rang. Javobi hujjat yoki aniq fakt bo'lsa, jumla qoladi. Javobi \"menimcha\" bo'lsa, o'chiring.",
    sources=STD,
)
