# UTM havola standarti (2026-11-12)

Har tashqi havolaga kanal belgisi qo'shiladi. Sayt birinchi kelishni 30 kun eslab qoladi (`js/utm.js`, `localStorage` `kompas_utm_v1`), ro'yxatdan o'tishda `user_metadata.utm` ga, to'lov buyurtmasida `payments.utm` ga (trigger) yozadi. Hisobot: admin → Analitika → "Kanallar".

## Format

```
?utm_source=<kanal>&utm_medium=<tur>&utm_campaign=<kampaniya>
```

| Parametr | Qiymatlar |
|---|---|
| `utm_source` | `telegram_kompaslab`, `telegram_grantlar`, `instagram`, `email`, `seminar_<shahar>` (masalan `seminar_toshkent`), `bot` |
| `utm_medium` | `post`, `story`, `bio`, `reklama`, `xat`, `qr` |
| `utm_campaign` | `<lab>_<yil>_<oy>`: `master_2026_11` |

Qoidalar: faqat kichik lotin harflar, raqam va `_`. Yangi kanal qo'shilsa, shu jadvalga yoziladi. UTM'siz kelgan tashqi tashrif `ref:<domen>` bo'lib yoziladi.

## Tayyor havolalar: Master Lab, 2026-11

Master Lab M0 (ro'yxatdan o'tish talab qilinadi; `m0-access.html` UTM'ni saqlab qoladi):

| Kanal | Havola |
|---|---|
| Telegram @kompaslab, post | `https://www.kompaslab.uz/master-lab-m0.html?utm_source=telegram_kompaslab&utm_medium=post&utm_campaign=master_2026_11` |
| Telegram grantlar kanali, reklama | `https://www.kompaslab.uz/master-lab-m0.html?utm_source=telegram_grantlar&utm_medium=reklama&utm_campaign=master_2026_11` |
| Instagram, story | `https://www.kompaslab.uz/master-lab-m0.html?utm_source=instagram&utm_medium=story&utm_campaign=master_2026_11` |
| Instagram, bio | `https://www.kompaslab.uz/master-lab-m0.html?utm_source=instagram&utm_medium=bio&utm_campaign=master_2026_11` |
| Email xat | `https://www.kompaslab.uz/master-lab-m0.html?utm_source=email&utm_medium=xat&utm_campaign=master_2026_11` |
| Seminar (Toshkent), QR | `https://www.kompaslab.uz/master-lab-m0.html?utm_source=seminar_toshkent&utm_medium=qr&utm_campaign=master_2026_11` |
| Bot (@yordam_klab_bot) | `https://www.kompaslab.uz/master-lab-m0.html?utm_source=bot&utm_medium=xat&utm_campaign=master_2026_11` |

Master Lab narx sahifasi:

| Kanal | Havola |
|---|---|
| Telegram @kompaslab, post | `https://www.kompaslab.uz/master-lab-narxlar.html?utm_source=telegram_kompaslab&utm_medium=post&utm_campaign=master_2026_11` |
| Telegram grantlar kanali, reklama | `https://www.kompaslab.uz/master-lab-narxlar.html?utm_source=telegram_grantlar&utm_medium=reklama&utm_campaign=master_2026_11` |
| Instagram, story | `https://www.kompaslab.uz/master-lab-narxlar.html?utm_source=instagram&utm_medium=story&utm_campaign=master_2026_11` |
| Instagram, bio | `https://www.kompaslab.uz/master-lab-narxlar.html?utm_source=instagram&utm_medium=bio&utm_campaign=master_2026_11` |
| Email xat | `https://www.kompaslab.uz/master-lab-narxlar.html?utm_source=email&utm_medium=xat&utm_campaign=master_2026_11` |
| Seminar (Toshkent), QR | `https://www.kompaslab.uz/master-lab-narxlar.html?utm_source=seminar_toshkent&utm_medium=qr&utm_campaign=master_2026_11` |
| Bot (@yordam_klab_bot) | `https://www.kompaslab.uz/master-lab-narxlar.html?utm_source=bot&utm_medium=xat&utm_campaign=master_2026_11` |

Boshqa shahar seminari uchun `seminar_toshkent` o'rniga `seminar_samarqand` kabi yoziladi; boshqa Lab uchun sahifa nomi va `utm_campaign` almashtiriladi (`phd_2026_11`).

## Cheklovlar
- Birinchi teginish hisoblanadi: odam avval Instagram'dan, keyin Telegram'dan kelsa, Instagram yoziladi.
- 7-noyabrgacha bo'lgan tashriflarda manba yo'q; ular hisobotda `(belgisiz)`.
- Brauzer xotirasi tozalansa yoki boshqa qurilmadan kirilsa, kanal yo'qoladi.
