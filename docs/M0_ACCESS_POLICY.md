# Kompas Lab — M0 kirish siyosati (2026-11-01)

## Mahsulot qarori
- **Barcha 12 ta rejalashtirilgan Lab uchun M0 bepul, lekin roʻyxatdan oʻtish va faol login talab qilinadi.**
- Roʻyxatdan oʻtmagan odam Lab tavsifi va darslar roʻyxatini koʻrishi mumkin; M0 matni, interaktiv topshiriqlar va yakuniy natija ochilmaydi.
- M1–M8 (yoki eski versiyalardagi M1–M16) uchun **alohida faol obuna/entitlement** tekshiruvi saqlanadi; M0 hisobining borligi pullik modullarni ochmaydi.
- Kompas Start — Lab M0 emas, ixtiyoriy roʻyxatdan oʻtiladigan bepul kirish mahsuloti; unga bu qoida tatbiq qilinmaydi.
- 18 yoshdan kichiklar uchun ota-ona/vasiy roziligi, tegishli kurs va toʻlov siyosati mustaqil saqlanadi.

## Server tomonidagi cheklov
- Vercel Routing Middleware **m0, m0-N, m0-yakun** (.html va clean URL) soʻrovlarini tutadi. Haqiqiy foydalanuvchi tekshiruvi Supabase Auth /auth/v1/user orqali serverda amalga oshiriladi.
- Middleware faqat server tomonidan tasdiqlangan **HttpOnly, Secure, SameSite=Lax, host-only** cookie orqali M0 HTML ni qaytaradi; cookie yoʻq/yaroqsiz boʻlsa `m0-access.html` sahifasiga qaytaradi.
- Brauzerdagi Supabase Auth sessiyasi `/api/m0-session` orqali tekshiriladi va qisqa muddatli M0 cookieʼga almashtiriladi. Cookie parol yoki refresh token saqlamaydi.
- **UI/CSS guard xavfsizlik chegarasi emas**; foydalanuvchi `view-source`, toʻgʻridan-toʻgʻri dars URL yoki network request orqali ham M0 ni ololmasligi kerak.
- Middleware xato yoki Supabase Auth uzilishida `fail closed` ishlaydi. Auth bor, ammo cookie muddati tugagan boʻlsa, bridge uni yangilaydi.
- M0 sahifalar `Cache-Control: private, no-store` bilan beriladi; service worker M0 HTML ni **cache** qilmaydi.

## Bosqichma-bosqich joriy etish
1. GitHub feature branch → Vercel preview deploy; **productionga avtomatik chiqarilmasin**.
2. Mehmonlar uchun 302 bridge va M0 matni tarqalmasligini, login qilinganlarga 200, cookie muddati oʻtganda qayta login oqimini test qilish.
3. Barcha mavjud M0 sahifalar va kelajakdagi Lablar bir xil qoida bilan ishlashini tekshirish.
4. Shaxsiy progressni Supabaseʼda saqlash uchun alohida `m0_progress` user-owned jadvali + RLS va sync xizmatini qoʻshish (hozirgi HTML progressi localStorageʼda).
5. A/B: M0 roʻyxatdan oʻtish konversiyasi va dars yakunlash koʻrsatkichlarini o'lchash, natija asosida tahlil qilish.

## Qabul testlari
| Holat | Kutiladigan natija |
|---|---|
| GET /bachelor-lab-m0 yoki /bachelor-lab-m0.html; cookie yoʻq | 302 → m0-access.html |
| GET /musofir-lab-m0-1.html; cookie yoʻq | 302 → m0-access.html (istisno bekor) |
| Mavjud, yaroqli Supabase Auth token + API almashinuvi | Set-Cookie; M0 sahifaga ruxsat |
| Soxta, muddati oʻtgan yoki bekor qilingan JWT | Ruxsat yoʻq |
| GET /bachelor-lab.html; login yoʻq | 200: public katalog |
| GET /m0-access.html; login yoʻq | Bepul roʻyxatdan oʻtish / kirish |
| M1–M8/16 | Avvalgi obuna/RPC nazorati saqlanadi |
| Offline yoki service worker cache | M0 HTML oshkor qilinmaydi |
