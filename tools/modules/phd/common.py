# PhD Lab M1–M8 (v4): umumiy manba havolalari. Tekshirildi: 2026-10-31 (har biri ochilib, mazmuni solishtirilgan).
# Qoida (2026-10-31): manbalar faqat universitetlar va masʼul tashkilotlar sahifalari.
# Blog, agentlik, yigʻuvchi (FindAPhD va h.k.) va yangilik saytlari manba sifatida ishlatilmaydi.
# Matnda oddiy apostrof (') yoziladi; engine.fix() uni U+02BB / U+02BC ga aylantiradi.
def a(url, text):
    return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{text}</a>'


DATE = "31.10.2026"
HOL = f"{DATE} holatiga"
STD = f"Faktlar {HOL}; har sikl rasmiy sahifadan qayta tekshiring. Muddat, summa, muvofiqlik va viza qoidalari oʻzgaradi."

# Buyuk Britaniya
UKRI_STUD = a("https://www.ukri.org/apply-for-funding/ukri-funded-studentships/", "UKRI: [[UKRI-funded studentships]] (yangilangan 07.04.2026)")
UKRI_SOE = a("https://www.ukri.org/publications/statement-of-expectations-for-doctoral-training/", "UKRI: [[Statement of Expectations for Doctoral Training]] (2024)")
LEEDS = a("https://www.leeds.ac.uk/research-applying/doc/applying-research-degrees", "[[University of Leeds: Applying for research degrees]]")
KCL = a("https://www.kcl.ac.uk/study/postgraduate-research/how-to-apply/writing-your-research-proposal", "[[King's College London: Writing your research proposal]]")
ATAS = a("https://www.gov.uk/guidance/academic-technology-approval-scheme", "GOV.UK: [[Academic Technology Approval Scheme]] (yangilangan 24.03.2026)")
VISA = a("https://www.gov.uk/student-visa", "GOV.UK: [[Student visa]]")
UKRIO = a("https://ukrio.org/research-integrity/the-concordat-to-support-research-integrity/", "UKRIO: [[The Concordat to Support Research Integrity]] (2025)")

# Yevropa
MSCA = a("https://marie-sklodowska-curie-actions.ec.europa.eu/actions/doctoral-networks", "Yevropa Komissiyasi: [[MSCA Doctoral Networks]] (yangilangan 29.09.2026)")
EURAXESS = a("https://euraxess.ec.europa.eu/jobs/search", "EURAXESS (Yevropa Komissiyasi): ish va doktorantura oʻrinlari")

# Ilmiy baholash
DORA = a("https://sfdora.org/read/", "DORA: San-Fransisko deklaratsiyasi")
