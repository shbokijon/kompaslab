# Dastur Umumiy sahifasi: muammo -> yechim (2026-11-18, asoschi: "mahsulot haqida emas, muammo va yechim haqida").
# split.py Umumiy sahifani shu maʼlumotdan yigʻadi. Matn amaldagi alifboda: ʻ (U+02BB), ʼ (U+02BC).
# Har dastur: h1 (muammo), lead (yechim yoʻli), probs: (ikonka, muammo, izoh, yechim).
PROBLEMS = {
"bachelor-lab": dict(
  h1="Xorijda bakalavr oʻqishni xohlaysiz.<span class=\"l2\">Yoʻli hali tarqoq.</span>",
  lead="Davlat, universitet, test va xarajatni bitta rejaga yigʻasiz. Insho va tavsiya materiallarini oʻzingiz tayyorlaysiz.",
  probs=[
    ("telescope", "Universitet tanlash taxminga qolgan", "Reyting va tanishlar maslahati sizga mos joyni koʻrsatmaydi.", "8–12 universitetni oʻz mezoningiz va rasmiy talablari bilan solishtirasiz."),
    ("calendar", "Testlar va muddatlar aralashib ketadi", "Qaysi test va ariza qachon kerakligi noaniq.", "Testlar va arizalar rasmiy muddatdan orqaga hisoblangan rejaga tushadi."),
    ("memo", "Insho yozishni hech kim oʻrgatmagan", "Nima haqida va qanday tuzilmada yozish kerakligi tushunarsiz.", "Tuzilma va baholash mezoni bilan oʻz inshoingizni yozib, tekshirasiz."),
    ("money", "Xarajat nomaʼlum", "Toʻrt yil qancha turishini oila hali hisoblamagan.", "4 yillik xarajat va universitet yordami imkoniyatini oldindan hisoblaysiz."),
  ]),
"master-lab": dict(
  h1="Magistraturaga topshirmoqchisiz.<span class=\"l2\">Qaysi dastur va qanday hujjat kerakligi noaniq.</span>",
  lead="Yoʻnalish, universitet va stipendiyani dalil bilan tanlaysiz. CV, maqsad bayonnomasi va ilmiy loyiha taklifini oʻzingiz yozasiz.",
  probs=[
    ("telescope", "Qaysi dastur sizga mos", "Dasturlar koʻp, nomlari oʻxshash, talablari har xil.", "Ilmiy yoʻnalishingizni aniqlab, 6–10 dasturni tekshirilgan roʻyxatga ajratasiz."),
    ("calendar", "Muddat va tavsiya xati kech qoladi", "Tavsiya beruvchiga vaqt kerak, muddatlar har dasturda boshqa.", "Rasmiy muddatdan orqaga hisoblangan shaxsiy reja tuzasiz."),
    ("memo", "CV va maqsad bayonnomasi qanday yoziladi", "Internetdagi namunalar sizning holatingizga mos kelmaydi.", "Tuzilma va baholash mezoni bilan matnni oʻzingiz yozasiz."),
    ("money", "Stipendiyasiz oʻqish imkonsiz", "Qaysi stipendiyaga mos kelishingiz va qachon topshirish nomaʼlum.", "Muvofiqligi va muddati tekshirilgan 3 ta stipendiyadan iborat portfel tuzasiz."),
  ]),
"phd-lab": dict(
  h1="Professorlar xatingizga javob bermayapti.<span class=\"l2\">Moliyalashtirilgan PhD rahbardan boshlanadi.</span>",
  lead="Ilmiy savolingizni aniqlaysiz, mos rahbarni topib, unga oʻzingiz yozasiz. Ilmiy loyiha taklifi va moliyalashtirish yoʻllarini tayyorlaysiz.",
  probs=[
    ("bulb", "Ilmiy savol aniq emas", "Mavzu keng, professorga nima taklif qilishni bilmaysiz.", "Mavzuni tekshirsa boʻladigan bitta ilmiy savolga toraytirasiz."),
    ("bell", "Xatlar javobsiz qoladi", "Hammaga bir xil xat yuborilsa, javob kelmasligi oson.", "Rahbarni maqolalari orqali topasiz va har biriga alohida xat yozasiz."),
    ("memo", "Ilmiy loyiha taklifi yozilmagan", "Savol, metod va reja qanday tuzilishi noaniq.", "Taklifni tuzilma va baholash mezoni bilan oʻzingiz yozasiz."),
    ("money", "Pul qayerdan kelishi chalkash", "Stipendiya, kafedra lavozimi va grant shartlari har xil.", "Moliyalashtirish yoʻllarini rasmiy manbadan solishtirasiz."),
  ]),
"gks-lab": dict(
  h1="GKS yoʻriqnomasi uzun.<span class=\"l2\">Kichik xato arizani toʻxtatishi mumkin.</span>",
  lead="Muvofiqligingizni toʻlovdan oldin tekshirasiz, trekni tanlaysiz va hujjatlarni oʻzingiz tayyorlaysiz.",
  probs=[
    ("shield", "Mos kelishingiz nomaʼlum", "Yosh, baho va boshqa shartlar har trekda boshqa.", "Muvofiqlikni bepul birinchi qismda rasmiy yoʻriqnoma boʻyicha tekshirasiz."),
    ("compass", "Qaysi trek sizniki", "Bakalavriat, magistratura, doktorantura: talab va urgʻu farq qiladi.", "Holatingizga mos trekni tanlab, faqat oʻsha talablar bilan ishlaysiz."),
    ("scroll", "Hujjat va tasdiq xatosi", "Apostil, tarjima, nusxa soni: biri chalkashsa, ariza qaytadi.", "Har hujjat manba, holat va muddati bilan bitta jadvalda yuritiladi."),
    ("bulb", "Intervyuga tayyor emassiz", "Komissiya savollariga qanday javob berishni bilmaysiz.", "Oʻz bayonotingiz va oʻquv rejangiz asosida intervyu mashq qilasiz."),
  ]),
"usa-lab": dict(
  h1="AQShda oʻqish qimmat koʻrinadi.<span class=\"l2\">Oilangizga real yoʻl bormi, hisoblab koʻrasiz.</span>",
  lead="Universitet yordami, Global UGRAD, Fulbright, magistratura va PhD yoʻllarini oila byudjeti va shartlarga qarab solishtirasiz.",
  probs=[
    ("money", "Jami xarajat nomaʼlum", "Oʻqish, yashash va sugʻurta birga qancha boʻlishini bilmaysiz.", "Universitetning rasmiy xarajat hujjatidan umumiy summani hisoblaysiz."),
    ("compass", "Qaysi yoʻl real", "Grant, universitet yordami, davlat dasturi: shartlari har xil.", "Yoʻlni oila toʻlay oladigan summa va muvofiqlik shartlariga qarab tanlaysiz."),
    ("telescope", "Yordam beradigan universitet qaysi", "Xalqaro talabaga toʻliq yordam beradigan universitetlar kam va tanlovli.", "Har universitetni rasmiy moliyaviy yordam sahifasi bilan tekshirasiz."),
    ("scroll", "Viza qoidalari chalkash", "F-1, J-1, I-20 va vatanga qaytish talabi aralashib ketadi.", "Viza turi va talablarini rasmiy manbadan oldindan bilasiz."),
  ]),
"daad-lab": dict(
  h1="Germaniyada ariza tartibi boshqacha.<span class=\"l2\">Koʻp dasturda ilmiy rahbar arizadan oldin keladi.</span>",
  lead="Sohangizdagi institut va rahbarni topasiz, unga oʻzingiz yozasiz, motivatsion xat va tadqiqot rejasini tayyorlab, DAAD portalida topshirasiz.",
  probs=[
    ("bell", "Ilmiy rahbar topilmagan", "Doktorantura va tadqiqot grantlarida rahbar roziligi odatda arizaning bir qismi.", "Sohangizdagi rahbarni topib, unga oʻzingiz xat yozasiz."),
    ("telescope", "Qaysi DAAD dasturi mos", "Bazada dastur koʻp, har birining sharti va muddati alohida.", "Har dastur shartini DAAD bazasidagi oʻz sahifasidan tekshirasiz."),
    ("memo", "Motivatsion xat va tadqiqot rejasi", "Nemis tizimi nimani kutishi tushunarsiz.", "Tuzilma va baholash mezoni bilan matnni oʻzingiz yozasiz."),
    ("books", "Til talabi aniq emas", "Nemis yoki ingliz tili kerakligi dasturga bogʻliq.", "Til talabini har dastur boʻyicha oldindan tekshirasiz. Til darsi kursga kirmaydi."),
  ]),
"tadbirkor-talaba": dict(
  h1="Biznes gʻoyangiz bor.<span class=\"l2\">Oʻqishni tashlab boʻlmaydi.</span>",
  lead="Kichik, qonuniy sinovni 30 kunda oʻtkazib, davom etish yoki toʻxtatishni dalil bilan hal qilasiz.",
  probs=[
    ("bulb", "Gʻoyaga talab bormi, nomaʼlum", "Doʻstlar maqtovi pul toʻlaydigan mijoz borligini koʻrsatmaydi.", "Muammoni haqiqiy mijozlar bilan suhbatda tekshirasiz."),
    ("seedling", "Boshlashga pul yoʻq", "Katta mablagʻsiz qanday sinash mumkinligi noaniq.", "Oddiy yechim (MVP) bilan birinchi toʻlovni olasiz."),
    ("scroll", "Huquqiy shakl va soliq", "Oʻzini oʻzi band qilgan, YATT yoki MChJ: qaysi biri mos.", "Shakl va soliqni rasmiy manba va sana bilan tanlaysiz."),
    ("chart", "Pul hisobi yuritilmaydi", "Foyda bormi yoki zararmi, bilinmaydi.", "Pul oqimini oddiy jadvalda hisoblaysiz."),
  ]),
"musofir-lab": dict(
  h1="Xorijda ishlamoqchisiz.<span class=\"l2\">Aldanib qolishdan qoʻrqasiz.</span>",
  lead="Rasmiy yoʻlni, uning talab va xarajatlarini rasmiy manbadan tekshirishni oʻrganasiz. Kompas ish yoki viza topib bermaydi.",
  probs=[
    ("shield", "Vositachiga ishonib boʻlmaydi", "Kafolat vaʼdasi, oldindan katta toʻlov, shoshiltirish.", "Firibgarlik belgilarini taniysiz va vositachini rasmiy roʻyxatdan tekshirasiz."),
    ("compass", "Qaysi rasmiy yoʻl mos", "Koreya, Buyuk Britaniya, Germaniya, Polsha: har birining oʻz tizimi.", "Yoʻllarni talab va xarajati bilan rasmiy manbadan solishtirasiz."),
    ("scroll", "Shartnoma tushunarsiz", "Ish haqi, soat va turar joy shartlari noaniq yozilgan boʻlishi mumkin.", "Shartnomani nazorat roʻyxati bilan tekshirasiz."),
    ("bell", "U yerda muammo chiqsa", "Huquqlaringiz va kimga murojaat qilishni bilmaysiz.", "Borgan mamlakatdagi huquqlar va yordam manzillarini oldindan bilasiz."),
  ]),
}
