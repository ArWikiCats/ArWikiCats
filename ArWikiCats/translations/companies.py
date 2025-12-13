COMPANY_TYPE_TRANSLATIONS = {
    "privately held": "خاصة",
    "airliner": "طائرات",
    "condiment": "توابل",
    "academic": "أكاديمية",
    "magazine": "مجلات",
    "natural gas": "غاز طبيعي",
    "comics": "قصص مصورة",
    "marvel comics": "مارفال كومكس",
    "mass media": "وسائل إعلام",
    "television": "تلفاز",
    "manga": "مانغا",
    "coal": "فحم",
    "coal gas": "غاز الفحم",
    "oil shale": "صخر زيتي",
    "oil": "زيت الوقود",
    "gas": "غاز",
    "nuclear": "نووية",
    "renewable energy": "طاقة متجددة",
    "agriculture": "زراعة",
    "airlines": "طيران",
    "aluminium": "ألومنيوم",
    "architecture": "هندسة معمارية",
    "automotive": "سيارات",
    "banks": "بنوك",
    "holding": "قابضة",
    "biotechnology": "تقانة حيوية",
    "building materials": "مواد بناء",
    "cargo airlines": "شحن جوي",
    "aviation": "طيران",
    "airline": "خطوط جوية",
    "cement": "أسمنت",
    "chemical": "كيميائية",
    "clothing": "ملابس",
    "computer": "حوسبة",
    "construction": "بناء",
    "construction and civil engineering": "بناء وهندسة مدنية",
    "cosmetics": "مستحضرات التجميل",
    "defence": "دفاعية",
    "design": "تصميم",
    "distribution": "توزيع",
    "education": "تعليم",
    "electronics": "إلكترونيات",
    "energy": "طاقة",
    "photovoltaic": "خلايا كهروضوئية",
    "hydroelectric": "كهرمائية",
    "electric power": "طاقة كهربائية",
    "engineering": "هندسية",
    "electrical engineering": "هندسة كهربائية",
    # "entertainment":"ترفيهية",
    "entertainment": "ترفيه",
    "eyewear": "نظارات",
    "financial": "مالية",
    "financial services": "خدمات مالية",
    "business services": "خدمات أعمال تجارية",
    "food": "أطعمة",
    "food and drink": "أطعمة ومشروبات",
    "gambling": "مقامرة",
    "glassmaking": "الزجاج",
    "health care": "رعاية صحية",
    "health clubs": "نوادي صحية",
    "horticultural": "بستنة",
    "household and personal product": "المنتجات المنزلية والشخصية",
    "insurance": "تأمين",
    "internet": "إنترنت",
    "internet service providers": "تزويد خدمة الإنترنت",
    "investment": "استثمارية",
    "jewellery": "مجوهرات",
    # "law":"مؤسسات قانون",
    "management consulting": "استشارات إدارية",
    "manufacturing": "تصنيع",
    "map": "خرائط",
    "marketing": "تسويق",
    "media": "إعلامية",
    "metal": "معادن",
    "mining": "تعدين",
    "vehicle manufacturing": "تصنيع مركبات",
    # "motor vehicle manufacturers":"تصنيع السيارات",
    "motor vehicle manufacturers": "مصانع سيارات",
    "music": "الموسيقى",
    "paint and coatings": "رسم وطلاء",
    "pharmaceutical": "أدوية",
    "printing": "طباعة",
    "property": "ممتلكات",
    "public utilities": "مرافق عمومية",
    "cruise ships": "سفن سياحية",
    "music publishing": "نشر موسيقى",
    "publishing": "نشر",
    "pulp and paper": "اللب والورق",
    "submarine": "غواصات",
    "rail": "سكك حديدية",
    "railway": "سكك حديدية",
    "car rental": "تأجير السيارات",
    "real estate": "عقارية",
    "real estate services": "خدمات عقارية",
    "retail": "تجارة التجزئة",
    "security": "أمن",
    "fraternal service": "خدمات أخوية",
    "service": "خدمات",
    "shipbuilding": "سفن",
    "shipyards": "حوض بناء سفن",
    "software": "برمجيات",
    "sugar": "السكر",
    "technology": "تكنولوجيا",
    "information technology": "تكنولوجيا المعلومات",
    "tobacco": "التبغ",
    "transport": "نقل",
    "travel": "سفر",
    "travel insurance": "تأمين السفر",
    "travel and holiday": "السفر والعطلات",
    "urban regeneration": "تطوير حضري",
    "utilities": "مرافق عمومية",
    "veterinary": "بيطرة",
    "video game": "ألعاب فيديو",
    "waste management": "إدارة المخلفات",
    "hotel chains": "سلاسل فندقية",
    "hospitality": "ضيافة",
    "hotel and leisure": "فنادق وترفيه",
    "hotels": "فنادق",
    "road transport": "نقل بري",
    "water transport": "نقل مائي",
    "shipping": "نقل بحري",
    "wine": "نبيذ",
    "alcohol": "كحول",
    "drink": "مشروبات",
    "water": "مياه",
    "postal": "بريد",
    "storage": "تخزين",
    "trucking": "نقل بالشاحنات",
    "logistics": "لوجستية",
    "military logistics": "لوجستية عسكرية",
    "wholesalers": "بيع بالجملة",
}
# ---
companies_keys3 = {}
companies_data = {}
# ---
for company_type, arabic_label in COMPANY_TYPE_TRANSLATIONS.items():  # Media company founders
    company_type_lower = company_type.lower()
    # so = f"{company_type_lower} %s"
    companies_data[f"{company_type_lower} company"] = f"شركات {arabic_label}"
    companies_data[f"{company_type_lower} offices"] = f"مكاتب {arabic_label}"

    companies_data[f"{company_type_lower} companies of"] = f"شركات {arabic_label} في"
    companies_data[f"defunct {company_type_lower} companies"] = f"شركات {arabic_label} سابقة"

    # NOTE: CHANGE_KEY_MAPPINGS[f"defunct {x} companies"] = f"defunct-{x}-companies"
    companies_data[f"defunct-{company_type_lower}-companies"] = f"شركات {arabic_label} سابقة"

    companies_data[f"defunct {company_type_lower}"] = f"{arabic_label} سابقة"
    companies_data[f"defunct {company_type_lower} of"] = f"{arabic_label} سابقة في"
    companies_data[f"{company_type_lower} firms of"] = f"شركات {arabic_label} في"
    companies_data[f"{company_type_lower} services"] = f"خدمات {arabic_label}"
    companies_data[f"{company_type_lower} firms"] = f"شركات {arabic_label}"
    companies_data[f"{company_type_lower} franchises"] = f"امتيازات {arabic_label}"
    companies_data[f"{company_type_lower} accidents-and-incidents"] = f"حوادث {arabic_label}"
    companies_data[f"{company_type_lower} accidents and incidents"] = f"حوادث {arabic_label}"
    companies_data[f"{company_type_lower} accidents or incidents"] = f"حوادث {arabic_label}"
    companies_data[f"{company_type_lower} accidents"] = f"حوادث {arabic_label}"
    companies_data[f"{company_type_lower} incidents"] = f"حوادث {arabic_label}"
    companies_data[f"{company_type_lower} software"] = f"برمجيات {arabic_label}"
    companies_data[f"{company_type_lower} databases"] = f"قواعد بيانات {arabic_label}"
    companies_data[f"{company_type_lower} agencies"] = f"وكالات {arabic_label}"
    companies_data[f"{company_type_lower} disciplines"] = f"تخصصات {arabic_label}"
    companies_data[f"{company_type_lower} museums"] = f"متاحف {arabic_label}"
    companies_data[f"{company_type_lower} organizations"] = f"منظمات {arabic_label}"
    companies_data[f"{company_type_lower} organization"] = f"منظمات {arabic_label}"
    companies_data[f"{company_type_lower} facilities"] = f"مرافق {arabic_label}"
    companies_data[f"{company_type_lower} bunkers"] = f"مخابئ {arabic_label}"
    companies_data[f"{company_type_lower} industry"] = f"صناعة {arabic_label}"
    companies_data[f"{company_type_lower} industry organisations"] = f"منظمات صناعة {arabic_label}"
    companies_data[f"{company_type_lower} industry organizations"] = f"منظمات صناعة {arabic_label}"
    # companies_data[f"{key2} of"] = "{} في".format(lab)
# ---
companies_to_jobs = {}
# ---

for company_type, label in COMPANY_TYPE_TRANSLATIONS.items():
    companies_to_jobs[f"{company_type} owners"] = {
        "males": f"ملاك {label}",
        "females": f"مالكات {label}",
    }
    companies_to_jobs[f"{company_type} founders"] = {
        "males": f"مؤسسو {label}",
        "females": f"مؤسسات {label}",
    }
    companies_to_jobs[f"{company_type} company founders"] = {
        "males": f"مؤسسو شركات {label}",
        "females": f"مؤسسات شركات {label}",
    }


COMPANY_COLLECTION_PREFIXES = {
    "manufacturers": "مصانع",
    "manufacturing": "تصنيع",
    "manufacturing companies": "شركات تصنيع",
    "privately held companies": "شركات خاصة",
    "companies": "شركات",
    "franchises": "امتيازات",
    "policy": "سياسات",
    "stations": "محطات",
    "tickets": "تذاكر",
}
COMPANY_EVENT_PREFIXES = {
    "accident": "حوادث",
    "accidents": "حوادث",
    "institutions": "مؤسسات",
    "disasters": "كوارث",
}
COMPANY_CATEGORY_CONTEXT = {
    "distance education": {"si": "التعليم عن بعد", "bb": "تعليم عن بعد"},
    "government-owned": {"si": "مملوكة للحكومة", "bb": "مملوكة للحكومة"},
    "design": {"si": "تصميم", "bb": "تصميم"},
    "holding": {"si": "قابضة", "bb": "قابضة"},
    "railway": {"si": "السكك الحديدية", "bb": "سكك حديد"},
    "rail industry": {"si": "السكك الحديدية", "bb": "سكك حديد"},
    "truck": {"si": "الشاحنات", "bb": "شاحنات"},
    "bus": {"si": "الباصات", "bb": "باصات"},
    "airline": {"si": "الخطوط الجوية", "bb": "خطوط جوية"},
    "cargo airlines": {"si": "الشحن الجوي", "bb": "شحن جوي"},
    "entertainment": {"si": "ترفيه", "bb": "الترفيه"},
    "airlines": {"si": "طيران", "bb": "طيران"},
    "aviation": {"si": "الطيران", "bb": "طيران"},
    "transport": {"si": "النقل", "bb": "نقل"},
    "road transport": {"si": "النقل البري", "bb": "نقل بري"},
    "privately held": {"si": "خاصة", "bb": "خاصة"},
    "road": {"si": "الطرق", "bb": "طرق"},
    "water transport": {"si": "النقل المائي", "bb": "نقل مائي"},
    "ferry transport": {"si": "النقل بالعبارات", "bb": "نقل عبارات"},
    "shipping": {"si": "النقل البحري", "bb": "نقل بحري"},
    "motor vehicle": {"si": "السيارات", "bb": "سيارات"},
    "vehicle": {"si": "المركبات", "bb": "مركبات"},
    "locomotive": {"si": "القاطرات", "bb": "قاطرات"},
    "rolling stock": {"si": "القطارات", "bb": "قطارات"},
}
companies_keys3 = {}
typeTable_update = {}

for category_key in COMPANY_CATEGORY_CONTEXT:
    singular_label = COMPANY_CATEGORY_CONTEXT[category_key]["si"]
    companies_keys3[category_key] = singular_label
    for suffix_key, suffix_label in COMPANY_COLLECTION_PREFIXES.items():
        companies_keys3[f"{category_key} {suffix_key}"] = f"{suffix_label} {singular_label}"

    plural_label = COMPANY_CATEGORY_CONTEXT[category_key]["bb"]
    companies_keys3[f"defunct {category_key} of"] = f"{plural_label} سابقة في"
    companies_keys3[f"defunct {category_key}"] = f"{plural_label} سابقة"
    for event_key, event_label in COMPANY_EVENT_PREFIXES.items():
        companies_keys3[f"{category_key} {event_key}"] = f"{event_label} {plural_label}"
        typeTable_update[f"{category_key} {event_key}"] = f"{event_label} {plural_label}"
        companies_keys3[f"{category_key} {event_key} of"] = f"{event_label} {plural_label} في"


New_Company = COMPANY_TYPE_TRANSLATIONS
