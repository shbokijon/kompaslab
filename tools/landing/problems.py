# Dastur Umumiy sahifasi: muammo -> yechim (2026-11-18, asoschi: "mahsulot haqida emas, muammo va yechim haqida").
# split.py Umumiy sahifani shu maʼlumotdan yigʻadi. Matn amaldagi alifboda: ʻ (U+02BB), ʼ (U+02BC).
# h1: ikki qator (muammo); lead: i ichida.
# probs: (ikonka, muammo, muammo izohi [i], yechim qisqa, yechim batafsil [i])
def h(a, b):
    return f'<span>{a}</span><span class="l2">{b}</span>'

PROBLEMS = {
"bachelor-lab": dict(
  h1=h("Xorijda bakalavr oʻqimoqchisiz.", "Lekin qayerdan boshlashni bilmaysiz."),
  lead="Hammasini bitta rejaga yigʻasiz, insho va tavsiya materiallarini oʻzingiz tayyorlaysiz.",
  probs=[
    ("telescope", "Qaysi universitet mos, bilmaysiz", "Reyting va tanishlar maslahati sizga mos joyni koʻrsatmaydi.", "Oʻz mezoningiz bilan", "8–12 universitetni rasmiy talablari bilan solishtirib, oʻzingizga mosini ajratasiz."),
    ("calendar", "Test va muddatlar aralashib ketgan", "Qaysi test qachon kerakligi chalkash.", "Teskari kalendar", "Testlar va arizalar rasmiy muddatdan orqaga hisoblangan rejaga tushadi."),
    ("memo", "Insho yozishni hech kim oʻrgatmagan", "Nima haqida yozish, qanday boshlash tushunarsiz.", "Tuzilma va mezon", "Inshoni oʻzingiz yozasiz va baholash mezoni bilan oʻzingiz tekshirasiz."),
    ("money", "Xarajat nomaʼlum", "Toʻrt yil qancha turishini oila hali hisoblamagan.", "Toʻrt yillik hisob", "Oʻqish va yashash xarajatini, universitet yordami imkonini oldindan hisoblaysiz."),
  ]),
"master-lab": dict(
  h1=h("Magistraturaga topshirmoqchisiz.", "Qaysi dastur va qanday hujjat kerakligi noaniq."),
  lead="Universitet va stipendiyani dalil bilan tanlaysiz, hujjatlarni oʻzingiz yozasiz.",
  probs=[
    ("telescope", "Qaysi dastur sizga mos", "Dasturlar koʻp, nomlari bir-biriga oʻxshaydi.", "Tekshirilgan roʻyxat", "Ilmiy yoʻnalishingizni aniqlab, 6–10 dasturni rasmiy talablari bilan saralaysiz."),
    ("calendar", "Tavsiya xati kech qoladi", "Tavsiya beruvchiga vaqt kerak, muddat esa har dasturda boshqa.", "Shaxsiy reja", "Reja rasmiy muddatdan orqaga hisoblanadi, tavsiyani qachon soʻrash oldindan koʻrinadi."),
    ("memo", "CV va maqsad bayonnomasi", "Internetdagi namunalar sizning holatingizga toʻgʻri kelmaydi.", "Tuzilma va mezon", "Matnni oʻzingiz yozasiz va baholash mezoni bilan tekshirasiz. Tayyor matn berilmaydi."),
    ("money", "Stipendiyasiz oʻqib boʻlmaydi", "Qaysi stipendiyaga mos kelishingiz va qachon topshirish nomaʼlum.", "Uchta stipendiya", "Muvofiqligi va muddati tekshirilgan uchta stipendiyani tanlab, portfel tuzasiz."),
  ]),
"phd-lab": dict(
  h1=h("Professorlar xatingizga javob bermayapti.", "Moliyalashtirilgan PhD toʻgʻri rahbardan boshlanadi."),
  lead="Ilmiy savolingizni aniqlaysiz, mos rahbarni topib, unga oʻzingiz yozasiz. Ilmiy loyiha taklifi va moliyalashtirish yoʻllarini tayyorlaysiz.",
  probs=[
    ("bulb", "Ilmiy savol aniq emas", "Mavzu keng, professorga nima taklif qilishni bilmaysiz.", "Bitta savolga toraytirish", "Mavzuni tekshirsa boʻladigan bitta ilmiy savolga toraytirasiz."),
    ("bell", "Xatlar javobsiz qoladi", "Hammaga bir xil xat yuborilsa, javob kelishi qiyin.", "Har biriga alohida xat", "Rahbarni maqolalari orqali topasiz va xatni uning ishiga bogʻlab yozasiz."),
    ("memo", "Loyiha taklifi yozilmagan", "Taklifni qanday tuzish noaniq.", "Tuzilma va mezon", "Taklifni oʻzingiz yozasiz va baholash mezoni bilan tekshirasiz."),
    ("money", "Pul qayerdan kelishi chalkash", "Stipendiya va grant shartlari bir-biriga oʻxshamaydi.", "Rasmiy taqqoslash", "Moliyalashtirish yoʻllarini rasmiy manbadan solishtirasiz."),
  ]),
"gks-lab": dict(
  h1=h("GKS yoʻriqnomasi uzun.", "Bitta xato hujjat arizani toʻxtatishi mumkin."),
  lead="Avval toʻlovsiz muvofiqligingizni tekshirasiz. Keyin trek tanlab, hujjatlarni oʻzingiz tayyorlaysiz.",
  probs=[
    ("shield", "Mos kelasizmi, nomaʼlum", "Yosh va baho shartlari har trekda boshqacha.", "Bepul tekshiruv", "Muvofiqlikni birinchi qismda, toʻlovdan oldin rasmiy yoʻriqnoma boʻyicha tekshirasiz."),
    ("compass", "Qaysi trek sizniki", "Har trekning oʻz talabi bor.", "Bitta trek", "Holatingizga mos trekni tanlab, faqat oʻsha talablar bilan ishlaysiz."),
    ("scroll", "Hujjat va tasdiq xatosi", "Apostil yoki tarjimadagi kichik xato arizani qaytarishi mumkin.", "Bitta jadval", "Hamma hujjat holati va muddati bilan bitta jadvalda turadi."),
    ("bulb", "Intervyudan qoʻrqasiz", "Komissiya nima soʻrashini bilmaysiz.", "Mashq", "Oʻz bayonotingiz va oʻquv rejangiz asosida intervyu mashq qilasiz."),
  ]),
"usa-lab": dict(
  h1=h("AQShda oʻqish qimmat koʻrinadi.", "Lekin oilangizga mos yoʻl boʻlishi mumkin."),
  lead="Universitet yordami, Global UGRAD, Fulbright, magistratura va PhD yoʻllarini oila byudjeti va shartlarga qarab solishtirasiz.",
  probs=[
    ("money", "Jami xarajat nomaʼlum", "Oʻqish va yashash birga qancha turishini bilmaysiz.", "Rasmiy hisob", "Universitetning rasmiy xarajat hujjatidan umumiy summani hisoblaysiz."),
    ("compass", "Qaysi yoʻl real", "Grant va universitet yordami shartlari bir-biriga oʻxshamaydi.", "Byudjetga qarab tanlash", "Yoʻlni oila toʻlay oladigan summa va muvofiqlik shartlariga qarab tanlaysiz."),
    ("telescope", "Yordam beradigan universitet qaysi", "Xalqaro talabaga toʻliq yordam beradigan universitetlar kam va tanlovli.", "Rasmiy sahifa", "Har universitetni moliyaviy yordam sahifasi bilan tekshirasiz."),
    ("scroll", "Viza chalkash", "F-1, J-1 va I-20 aralashib ketadi.", "Oldindan bilish", "Viza turi va talablarini rasmiy manbadan oldindan bilasiz."),
  ]),
"daad-lab": dict(
  h1=h("Germaniyada ariza tartibi boshqacha.", "Koʻp dasturda avval ilmiy rahbar topiladi."),
  lead="Rahbar topishdan DAAD portaligacha hamma qadamni oʻzingiz qilasiz.",
  probs=[
    ("bell", "Ilmiy rahbar yoʻq", "Doktorantura va tadqiqot grantlarida rahbar roziligi odatda arizaning bir qismi.", "Rahbarni topish", "Sohangizdagi rahbarni topib, unga oʻzingiz xat yozasiz."),
    ("telescope", "Qaysi DAAD dasturi mos", "Bazada dastur koʻp, har birining oʻz sharti bor.", "Rasmiy baza", "Har dastur shartini DAAD bazasidagi oʻz sahifasidan tekshirasiz."),
    ("memo", "Motivatsion xat", "Germaniyada xat nimani koʻrsatishi kerakligi noaniq.", "Tuzilma va mezon", "Xat va tadqiqot rejasini oʻzingiz yozasiz, mezon bilan tekshirasiz."),
    ("books", "Til talabi aniq emas", "Nemis yoki ingliz tili kerakligi dasturga bogʻliq.", "Oldindan tekshirish", "Til talabini har dastur boʻyicha oldindan bilasiz. Til darsi kursga kirmaydi."),
  ]),
"tadbirkor-talaba": dict(
  h1=h("Biznes gʻoyangiz bor.", "Lekin oʻqishni tashlab boʻlmaydi."),
  lead="Kichik, qonuniy sinovni 30 kunda oʻtkazib, davom etish yoki toʻxtatishni dalil bilan hal qilasiz.",
  probs=[
    ("bulb", "Gʻoyaga talab bormi", "Doʻstlar maqtovi pul toʻlaydigan mijoz borligini koʻrsatmaydi.", "Mijoz bilan suhbat", "Muammoni haqiqiy mijozlar bilan gaplashib tekshirasiz."),
    ("seedling", "Boshlashga pul yoʻq", "Katta mablagʻsiz qanday sinash mumkinligi noaniq.", "Oddiy yechim (MVP)", "Kichik yechim bilan birinchi toʻlovni olasiz."),
    ("scroll", "Huquqiy shakl va soliq", "Qaysi shakl mos va soliq qancha, noaniq.", "Rasmiy manba", "Shakl va soliqni rasmiy manba va sana bilan tanlaysiz."),
    ("chart", "Foyda bormi, bilinmaydi", "Pul kirib-chiqadi, hisob yuritilmaydi.", "Oddiy jadval", "Pul oqimini oddiy jadvalda hisoblaysiz."),
  ]),
"musofir-lab": dict(
  h1=h("Xorijda ishlamoqchisiz.", "Aldanib qolishdan qoʻrqasiz."),
  lead="Rasmiy yoʻl talablari va xarajatini manbadan tekshirishni oʻrganasiz. Kompas ish yoki viza topib bermaydi.",
  probs=[
    ("shield", "Vositachiga ishonib boʻlmaydi", "Kafolat vaʼda qiladi va oldindan pul soʻraydi.", "Belgilarni tanish", "Firibgarlik belgilarini taniysiz va vositachini rasmiy roʻyxatdan tekshirasiz."),
    ("compass", "Qaysi rasmiy yoʻl mos", "Har mamlakatning oʻz tizimi bor.", "Solishtirish", "Yoʻllarni talab va xarajati bilan rasmiy manbadan solishtirasiz."),
    ("scroll", "Shartnoma tushunarsiz", "Ish haqi va soat noaniq yozilgan boʻlishi mumkin.", "Nazorat roʻyxati", "Shartnomani band-band tekshirasiz."),
    ("bell", "U yerda muammo chiqsa-chi", "Huquqlaringiz va kimga murojaat qilishni bilmaysiz.", "Yordam manzillari", "Borgan mamlakatdagi huquqlar va yordam manzillarini oldindan bilasiz."),
  ]),
}
