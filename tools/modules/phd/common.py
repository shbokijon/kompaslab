# PhD Lab M1–M8: umumiy manba havolalari. Tekshirildi: 2026-11-07.
# Qoida (2026-10-31): manbalar faqat universitetlar va masʼul tashkilotlar sahifalari
# (UKRI, Yevropa Komissiyasi, GOV.UK, UKRIO, DORA, universitetlar).
# Blog, agentlik, reyting yigʻuvchi va yangilik saytlari manba sifatida ishlatilmaydi.
# Matnda oddiy apostrof (') yoziladi; engine.fix() uni U+02BB / U+02BC ga aylantiradi.
def a(url, text):
    return f'<a href="{url}" target="_blank" rel="noopener">{text}</a>'


DATE = "07.11.2026"
HOL = f"{DATE} holatiga"
STD = f"Faktlar {HOL}; tanlagan dasturingiz sahifasidan qayta tekshiring. Muddat, summa, kvota va muvofiqlik shartlari har sikl o'zgaradi."

LEEDS = a("https://www.leeds.ac.uk/pgr/apply", "Leeds universiteti: Applying for research degrees")
UKRI = a("https://www.ukri.org/apply-for-funding/ukri-funded-studentships/", "UKRI: UKRI-funded studentships")
UKRIEXP = a("https://www.ukri.org/publications/statement-of-expectations-for-doctoral-training/", "UKRI: Statement of expectations for doctoral training")
MSCA = a("https://marie-sklodowska-curie-actions.ec.europa.eu/actions/doctoral-networks", "Yevropa Komissiyasi: MSCA Doctoral Networks")
EURAXESS = a("https://euraxess.ec.europa.eu/jobs/search", "EURAXESS: Jobs and Opportunities")
KCL = a("https://www.kcl.ac.uk/study/postgraduate-research/how-to-apply/writing-your-research-proposal", "King's College London: Writing your research proposal")
UKRIO = a("https://ukrio.org/research-integrity/the-concordat-to-support-research-integrity/", "UKRIO: The Concordat to Support Research Integrity")
DORA = a("https://sfdora.org/resource/guidance-on-the-responsible-use-of-quantitative-indicators-in-research-assessment/", "DORA: miqdoriy ko'rsatkichlardan mas'uliyat bilan foydalanish")
ATAS = a("https://www.gov.uk/guidance/academic-technology-approval-scheme", "GOV.UK: Academic Technology Approval Scheme (ATAS)")
VISA = a("https://www.gov.uk/student-visa", "GOV.UK: Student visa")
