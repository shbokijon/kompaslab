from _lib import les, body, lib
from common import U27, STD

V1 = lib(1)

GPA = body(1, 3) + f"""
<h4>Sinfdagi o'rin va izoh</h4>
<ul><li>Maktab yoki litsey sinf (oqim) bo'yicha o'rningizni rasmiy ma'lumotnoma bilan bera olsa, bu \"yuqori 20 foiz\" yo'lini ochadi.</li>
<li>Oxirgi yillarda baho o'sgan bo'lsa, bu o'sish traektoriyasining dalili: uni shaxsiy bayonotda bir jumla bilan, transkriptga tayanib ko'rsating.</li>
<li>2027 GKS-U da konvertatsiya jadvali yo'riqnomaning A ilovasida; maktab tasdiqlagan konvertatsiya talab qilinishi mumkin.</li></ul>
<div class="srcs">Manba: {U27}.</div>"""

MOD = dict(
    title="Nomzod profili",
    desc="GKS Lab M3-U (bakalavriat): potensialni dalil bilan ko'rsatish, qiziqishning kelib chiqishi, baholarni taqdim etish va zaif tomonlarni tushuntirish. Natija: faoliyat vaqt chizig'i, akademik profil izohi, zaif tomonlar javoblari.",
    lead="Bakalavriat nomzodidan tadqiqot kutilmaydi, lekin o'sish va qiziqish dalili kutiladi. Bu modulda shaxsiy bayonot uchun xom ashyoni yig'asiz: nima qilgansiz, qiziqish qayerdan kelgan, baholaringiz nimani ko'rsatadi.",
    hero="bulb", weeks="2", next="M4-U Shaxsiy bayonot", next_href="gks-lab-m4-u.html",
    goals=[("calendar", "Faoliyat vaqt chizig'i", "9–11-sinf (litsey, kollej) yillari, har bosqich dalil bilan"),
           ("seedling", "Akademik profil izohi", "baholar, qiziqish va o'sish bir paragrafda"),
           ("shield", "Zaif tomonlar javoblari", "fakt → tuzatish → hozirgi dalil")],
    warn="Bu modul formalarni to'ldirmaydi, ular uchun material tayyorlaydi. 2027 GKS-U da mukofot va sertifikatlar ixtiyoriy, beshtagacha ilova qilinadi; baho talabi va konvertatsiya yo'riqnomadan (31.10.2026 holatiga).",
    lessons=[
        les(3, 1, t="Potensial qanday isbotlanadi", short="Potensial"),
        les(3, 4, t="Qiziqishning kelib chiqishi", short="Qiziqish"),
        les(1, 3, t="Baholarni taqdim etish", short="Baho", body=GPA, kind="🎯 Mini-test",
            quiz=[("2027 GKS-U da 100 ballik shkalada 80 va undan yuqori baho talabga javob beradi.", "t", "To'g'ri: bu uch yo'ldan biri."),
                  ("5 ballik tizimda 3.0 o'rtacha baho talabga yetadi.", "n", "Noto'g'ri: minimal 3.23/5.0."),
                  ("Bahoni CV yoki formada o'zingiz 4.0 shkalaga aylantirib yozishingiz kerak.", "n", "Noto'g'ri: asl shkalada yozing; konvertatsiyani muassasa tasdiqlaydi."),
                  ("Sinfdagi o'rinni faqat rasmiy ma'lumotnoma bilan ko'rsatish mumkin.", "t", "To'g'ri.")]),
        les(3, 3, t="Zaif tomonlarni boshqarish", short="Zaif"),
    ],
    tool=dict(id="profil", short="Profil", h2="Profil va baho", sub="Vaqt chizig'i, profil izohi va zaif tomon javobi. GPA tekshiruvi hisobni o'zi qiladi.",
              h3="Nomzod profili", tag="GPA + 3 maydon", ic="bulb", btn="Profilni saqlash", badge="Profilchi", min=3,
              pre=V1["tool"]["pre"],
              fields=[dict(k="tl", label="Faoliyat vaqt chizig'i", hint="yil · faoliyat · natija · hujjat", type="area", ph="2024 · viloyat olimpiadasi · 2-o'rin · diplom"),
                      dict(k="weak", label="Zaif tomon javobi", type="area", ph="Fakt → tuzatish → hozirgi dalil"),
                      dict(k="prof", label="Akademik profil izohi", type="area", wc="120-180", ph="Bugungi nuqta, traektoriya, bo'shliq, keyingi qadam")]),
    check=dict(h2="Profil nazorati", sub="Inventarni yakunlashdan oldin.", h3="8 bandlik nazorat",
               items=["Har STAR yozuvida shaxsiy harakat aniq (\"men\").", "Har natija raqam, hujjat yoki mahsulot bilan tekshiriladi.",
                      "Yutuqlar tegishlilik bo'yicha saralangan; 5 tadan oshmaydi.", "Baho asl shkalada, talabga moslik yo'li aniq.",
                      "Zaif tomon fakt → tuzatish → dalil tartibida.", "Profil izohida umumiy ochilish (\"bolaligimdan\") yo'q.",
                      "Qiziqish kuzatuv → savol → harakat zanjiri bilan ko'rsatilgan.", "Material M4-U uchun bir joyda saqlangan."]),
    art_title="Nomzod profili", art_short="Profil",
    art=[("Faoliyat vaqt chizig'i", ["tl", "a1"]), ("Qiziqishning kelib chiqishi", ["a2"]), ("Baholar", ["gpa", "a3"]),
         ("Zaif tomonlar javoblari", ["weak", "a4"]), ("Akademik profil izohi", ["prof"])],
    tip=lib(3)["tip"], sources=STD, js=V1["js"],
)
