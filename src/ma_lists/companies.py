
New_Company = {
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
for kes, lab in New_Company.items():  # Media company founders
    keys2 = kes.lower()
    # so = f"{keys2} %s"
    companies_data[f"{keys2} company"] = f"شركات {lab}"
    # ---
    companies_data[f"{keys2} offices"] = f"مكاتب {lab}"

    companies_data[f"{keys2} companies of"] = f"شركات {lab} في"
    companies_data[f"defunct {keys2} companies"] = f"شركات {lab} سابقة"
    companies_data[f"defunct-{keys2}-companies"] = f"شركات {lab} سابقة"
    companies_data[f"defunct {keys2}"] = f"{lab} سابقة"
    companies_data[f"defunct {keys2} of"] = f"{lab} سابقة في"
    companies_data[f"{keys2} firms of"] = f"شركات {lab} في"
    companies_data[f"{keys2} services"] = f"خدمات {lab}"
    companies_data[f"{keys2} firms"] = f"شركات {lab}"
    companies_data[f"{keys2} franchises"] = f"امتيازات {lab}"
    # ---
    companies_data[f"{keys2} accidents-and-incidents"] = f"حوادث {lab}"
    companies_data[f"{keys2} accidents and incidents"] = f"حوادث {lab}"
    companies_data[f"{keys2} accidents or incidents"] = f"حوادث {lab}"
    companies_data[f"{keys2} accidents"] = f"حوادث {lab}"
    companies_data[f"{keys2} incidents"] = f"حوادث {lab}"
    companies_data[f"{keys2} software"] = f"برمجيات {lab}"
    companies_data[f"{keys2} databases"] = f"قواعد بيانات {lab}"
    # ---
    companies_data[f"{keys2} agencies"] = f"وكالات {lab}"
    companies_data[f"{keys2} disciplines"] = f"تخصصات {lab}"
    companies_data[f"{keys2} museums"] = f"متاحف {lab}"
    companies_data[f"{keys2} organizations"] = f"منظمات {lab}"
    companies_data[f"{keys2} organization"] = f"منظمات {lab}"
    companies_data[f"{keys2} facilities"] = f"مرافق {lab}"
    companies_data[f"{keys2} bunkers"] = f"مخابئ {lab}"
    companies_data[f"{keys2} industry"] = f"صناعة {lab}"
    companies_data[f"{keys2} industry organisations"] = f"منظمات صناعة {lab}"
    companies_data[f"{keys2} industry organizations"] = f"منظمات صناعة {lab}"
    # companies_data[f"{key2} of"] = "{} في".format(lab)
# ---
companies_to_jobs = {}
# ---

for ggg in New_Company.keys():
    companies_to_jobs[f"{ggg} owners"] = {
        "mens": f"ملاك {New_Company[ggg]}",
        "womens": f"مالكات {New_Company[ggg]}",
    }
    companies_to_jobs[f"{ggg} founders"] = {
        "mens": f"مؤسسو {New_Company[ggg]}",
        "womens": f"مؤسسات {New_Company[ggg]}",
    }
    companies_to_jobs[f"{ggg} company founders"] = {
        "mens": f"مؤسسو شركات {New_Company[ggg]}",
        "womens": f"مؤسسات شركات {New_Company[ggg]}",
    }


# def Add_companies():
tyui = {
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
tyui2 = {
    "accident": "حوادث",
    "accidents": "حوادث",
    "institutions": "مؤسسات",
    "disasters": "كوارث",
}
Roood = {
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

for roo in Roood:
    oi = Roood[roo]["si"]
    companies_keys3[roo] = oi
    for dd in tyui:
        companies_keys3[f"{roo} {dd}"] = f"{tyui[dd]} {oi}"

    oi2 = Roood[roo]["bb"]
    companies_keys3[f"defunct {roo} of"] = f"{oi2} سابقة في"
    companies_keys3[f"defunct {roo}"] = f"{oi2} سابقة"
    for dd in tyui2:
        companies_keys3[f"{roo} {dd}"] = f"{tyui2[dd]} {oi2}"
        typeTable_update[f"{roo} {dd}"] = f"{tyui2[dd]} {oi2}"
        companies_keys3[f"{roo} {dd} of"] = f"{tyui2[dd]} {oi2} في"
