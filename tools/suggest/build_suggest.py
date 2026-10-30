# ═══════════════════════════════════════════════════════════════
#  Avtomatik taklif (autocomplete) maʼlumotlari: data/suggest/*.json
#
#    python3 tools/suggest/build_suggest.py
#
#  Manbalar:
#   · Universitetlar: Hipo "university-domains-list" (MIT litsenziya)
#     https://github.com/Hipo/university-domains-list  (world_universities_and_domains.json)
#     Yangilash: faylni shu papkaga qayta yuklab, skriptni ishga tushiring.
#   · Mamlakat nomlari: Unicode CLDR (Node.js Intl.DisplayNames, "uz" va "en").
#   · Fanlar, stipendiyalar, tillar, sertifikatlar, shaharlar: shu fayldagi qoʻlda tuzilgan
#     roʻyxatlar. Faqat nomlar: muddat, kvota, muvofiqlik kabi oʻzgaruvchan fakt yoʻq (Yadro/Qobiq).
# ═══════════════════════════════════════════════════════════════
import json, subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent.parent / "data" / "suggest"

# Fan nomlari (inglizcha, dastur nomida ishlatiladigan shaklda); S = odatda MSc/MEng, A = odatda MA
SUBJECTS = {
 "S": ["Accounting and Finance", "Actuarial Science", "Advanced Computer Science", "Aerospace Engineering", "Agricultural Economics",
  "Agricultural Science", "Analytical Chemistry", "Animal Science", "Applied Geophysics", "Applied Mathematics", "Applied Physics",
  "Applied Statistics", "Aquaculture", "Artificial Intelligence", "Astrophysics", "Atmospheric Science", "Automotive Engineering",
  "Big Data Analytics", "Biochemistry", "Bioinformatics", "Biomedical Engineering", "Biomedical Science", "Biotechnology",
  "Building Information Modelling", "Business Analytics", "Chemical Engineering", "Chemistry", "Civil Engineering", "Climate Change",
  "Clinical Psychology", "Cloud Computing", "Computational Science", "Computer Engineering", "Computer Science", "Construction Management",
  "Cyber Security", "Data Science", "Digital Marketing", "Drug Discovery", "Earth Sciences", "Ecology", "Econometrics", "Economics",
  "Electrical Engineering", "Electronic Engineering", "Embedded Systems", "Energy Engineering", "Energy Systems", "Engineering Geology",
  "Engineering Management", "Environmental Engineering", "Environmental Science", "Epidemiology", "Exploration Geophysics", "Finance",
  "Financial Engineering", "Food Science", "Food Technology", "Forensic Science", "Genetics", "Geographic Information Systems (GIS)",
  "Geology", "Geophysics", "Geotechnical Engineering", "Geothermal Energy", "Global Health", "Health Data Science", "Human-Computer Interaction",
  "Hydrogeology", "Hydrology", "Industrial Engineering", "Information Security", "Information Systems", "Information Technology",
  "Logistics and Supply Chain Management", "Machine Learning", "Marine Biology", "Materials Science", "Materials Engineering",
  "Mathematical Finance", "Mathematics", "Mechanical Engineering", "Mechatronics", "Medical Physics", "Microbiology", "Mining Engineering",
  "Molecular Biology", "Nanotechnology", "Neuroscience", "Nuclear Engineering", "Nutrition", "Ocean Science", "Operations Research",
  "Petroleum Engineering", "Petroleum Geoscience", "Pharmacology", "Pharmaceutical Sciences", "Physics", "Plant Science", "Power Systems",
  "Project Management", "Public Health", "Quantum Technologies", "Remote Sensing", "Renewable Energy", "Robotics", "Software Engineering",
  "Soil Science", "Statistics", "Structural Engineering", "Sustainable Development", "Telecommunications", "Transport Engineering",
  "Urban Planning", "Water Resources Management", "Water and Environmental Engineering", "Wireless Communications", "Zoology"],
 "A": ["Applied Linguistics", "Architecture", "Art History", "Comparative Literature", "Creative Writing", "Development Studies",
  "Diplomacy", "Education", "Educational Leadership", "English Literature", "Film Studies", "Global Governance", "History",
  "Human Rights", "International Development", "International Relations", "Journalism", "Linguistics", "Media and Communication",
  "Philosophy", "Political Science", "Public Policy", "Sociology", "TESOL", "Translation and Interpreting"],
 "B": ["International Business", "Management", "Marketing", "Human Resource Management", "Tourism Management", "Hospitality Management",
  "Entrepreneurship and Innovation", "Public Administration", "Social Work", "Psychology", "Law"],
}
DEGREES = ["MSc", "MA", "MRes", "MEng", "MPhil", "MBA", "LLM", "MPH", "MS", "MPA", "MEd", "MArch", "PhD"]

SCHOLARSHIPS = [
 ("Chevening", "GB"), ("Fulbright", "US"), ("Global UGRAD", "US"), ("DAAD", "DE"), ("Global Korea Scholarship (GKS)", "KR"),
 ("MEXT", "JP"), ("JDS", "JP"), ("Erasmus Mundus", ""), ("Erasmus+", ""), ("Stipendium Hungaricum", "HU"),
 ("Türkiye Bursları", "TR"), ("Chinese Government Scholarship (CSC)", "CN"), ("El-yurt umidi", "UZ"),
 ("Eiffel Excellence Scholarship", "FR"), ("Swiss Government Excellence Scholarships", "CH"), ("Holland Scholarship", "NL"),
 ("Swedish Institute Scholarships for Global Professionals", "SE"), ("Italian Government Scholarships (MAECI)", "IT"),
 ("Korean Government Scholarship (KGSP)", "KR"), ("Czech Government Scholarships", "CZ"), ("Slovak Government Scholarships", "SK"),
 ("Polish Government Scholarships (NAWA)", "PL"), ("University scholarship", ""), ("Teaching assistantship", ""), ("Research assistantship", ""),
]
LANGUAGES = ["English", "Uzbek", "Russian", "Karakalpak", "Kazakh", "Kyrgyz", "Tajik", "Turkmen", "Turkish", "Azerbaijani", "German",
 "French", "Spanish", "Italian", "Portuguese", "Dutch", "Swedish", "Polish", "Czech", "Hungarian", "Korean", "Japanese", "Chinese (Mandarin)",
 "Arabic", "Persian", "Hindi", "Urdu", "Malay", "Indonesian"]
TESTS = ["IELTS Academic", "IELTS General Training", "TOEFL iBT", "PTE Academic", "Duolingo English Test", "Cambridge C1 Advanced",
 "Cambridge C2 Proficiency", "TOPIK I", "TOPIK II", "JLPT N1", "JLPT N2", "JLPT N3", "JLPT N4", "JLPT N5", "TestDaF",
 "Goethe-Zertifikat B2", "Goethe-Zertifikat C1", "DSH", "DELF B2", "DALF C1", "TCF", "DELE B2", "HSK 4", "HSK 5", "HSK 6",
 "TÖMER", "GRE General", "GMAT", "SAT"]
CITIES_UZ = ["Tashkent", "Samarkand", "Bukhara", "Andijan", "Namangan", "Fergana", "Kokand", "Margilan", "Nukus", "Karshi", "Termez",
 "Urgench", "Khiva", "Jizzakh", "Gulistan", "Navoi", "Chirchik", "Angren", "Almalyk", "Shakhrisabz"]
FIELDS_UZ = ["Energetika", "Qayta tiklanuvchi energiya", "Geologiya", "Geofizika", "Gidrogeologiya", "Neft va gaz", "Togʻ-kon ishi",
 "Ekologiya", "Atrof-muhit muhandisligi", "Suv resurslari", "Qishloq xoʻjaligi", "Oziq-ovqat texnologiyasi", "Biologiya", "Biotexnologiya",
 "Kimyo", "Fizika", "Matematika", "Statistika", "Kompyuter fanlari", "Sunʼiy intellekt", "Maʼlumotlar fani", "Kiberxavfsizlik",
 "Dasturiy injiniring", "Elektrotexnika", "Mashinasozlik", "Qurilish muhandisligi", "Arxitektura", "Shaharsozlik", "Transport va logistika",
 "Tibbiyot", "Jamoat salomatligi", "Farmatsevtika", "Psixologiya", "Iqtisodiyot", "Moliya", "Menejment", "Marketing", "Huquq",
 "Xalqaro munosabatlar", "Davlat boshqaruvi", "Taʼlim", "Tilshunoslik", "Jurnalistika"]


def country_names(codes):
    js = ("const c=" + json.dumps(sorted(codes)) + ";const u=new Intl.DisplayNames(['uz'],{type:'region'}),e=new Intl.DisplayNames(['en'],{type:'region'});"
          "const o={};for(const k of c){try{o[k]=[u.of(k),e.of(k)]}catch(x){}}console.log(JSON.stringify(o))")
    out = json.loads(subprocess.check_output(["node", "-e", js], text=True))
    # CLDR "Qo‘shma" (U+2018) → loyiha standarti U+02BB
    return {k: [v[0].replace("‘", "ʻ").replace("'", "ʻ"), v[1]] for k, v in out.items()}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    src = json.loads((HERE / "world_universities_and_domains.json").read_text(encoding="utf-8"))
    seen, unis = set(), []
    for u in src:
        name, cc = u["name"].strip(), (u.get("alpha_two_code") or "").upper()
        if not name or (name, cc) in seen:
            continue
        seen.add((name, cc))
        unis.append([name, cc])
    unis.sort(key=lambda x: x[0].lower())
    codes = {cc for _, cc in unis if cc} | {cc for _, cc in SCHOLARSHIPS if cc}
    countries = country_names(codes)
    (OUT / "universities.json").write_text(json.dumps(unis, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    small = dict(
        countries=countries,
        subjects={k: v for k, v in SUBJECTS.items()},
        degrees=DEGREES,
        scholarships=SCHOLARSHIPS,
        languages=LANGUAGES,
        tests=TESTS,
        cities_uz=CITIES_UZ,
        fields_uz=FIELDS_UZ,
        source={"universities": "Hipo university-domains-list (MIT), https://github.com/Hipo/university-domains-list",
                "countries": "Unicode CLDR via Intl.DisplayNames"},
    )
    (OUT / "lists.json").write_text(json.dumps(small, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print("universities:", len(unis), "countries:", len(countries),
          "| sizes:", (OUT / "universities.json").stat().st_size, (OUT / "lists.json").stat().st_size)


if __name__ == "__main__":
    main()
