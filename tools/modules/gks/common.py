# Umumiy manba havolalari (GKS M1–M8). Tekshirildi: 2026-10-31.
def a(url, text):
    return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'

U27 = a("https://gksscholarship.com/wp-content/uploads/2026/09/2027-GKS-U-Application-Guidelines-English.pdf", "2027 GKS-U yo'riqnomasi (inglizcha matn)")
G26 = a("https://www.esteri.it/wp-content/uploads/2026/02/2026-GKS-G-Application-Guidelines-English.pdf", "2026 GKS-G yo'riqnomasi (inglizcha matn)")
SIK = a("https://www.studyinkorea.go.kr", "Study in Korea (NIIED rasmiy portali)")
JA = a("https://www.koreajoongangdaily.com/korea/gksu-2027-what-international-students-need-to-know-before-applying/12878569", "Korea JoongAng Daily, 16.09.2026")
APO = a("https://gov.uz/oz/advice/72/document/2620", "gov.uz: rasmiy hujjatlarga apostil qo'yish")
TOPIK = a("https://www.topik.go.kr", "TOPIK rasmiy sayti")

STD = f"{U27}; {G26}; {SIK}. Faktlar 31.10.2026 holatiga; har sikl yangi yo'riqnoma bilan qayta tekshiring. Koreyscha va inglizcha matn farq qilsa, koreyscha versiya ustun."
