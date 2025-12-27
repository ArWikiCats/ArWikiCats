#

structures_data = {}
# ---
pop_key_4 = {
    # "lighthouses":"منارات",
    "non-renewable resource": "موارد غير متجددة",
    "oil shale": "صخر زيتي",
    "mobile phone": "هاتف محمول",
    "bauxite": "البوكسيت",
    "biofuel": "وقود حيوي",
    "chemical": "كيميائية",
    "coal gas": "غاز الفحم",
    "coal": "الفحم",
    "coals": "الفحم",
    "condiment": "توابل",
    "copper": "النحاس",
    "electric power": "طاقة كهربائية",
    "electric": "قدرة",
    "electrical engineering": "هندسة كهربائية",
    "energy": "طاقة",
    "fossil fuel": "وقود أحفوري",
    "fossil fuels": "وقود أحفوري",
    "gas": "غاز",
    "geothermal": "حرارية جوفية",
    "gold": "الذهب",
    "hydroelectric": "كهرمائية",
    "mining": "التعدين",
    "natural gas": "غاز طبيعي",
    "nuclear": "نووية",
    "oil and gas": "النفط والغاز",
    "oil": "نفطية",
    "petroleum": "بترولية",
    "photovoltaic": "كهروضوئية",
    "non-renewable energy": "طاقة غير متجددة",
    "renewable energy": "طاقة متجددة",
    "renewable resource": "موارد متجددة",
    "sedimentary rocks": "صخور رسوبية",
    "solar": "شمسية",
    "solid fuel": "وقود صلب",
    "solid fuels": "وقود صلب",
}
# ---

for key in pop_key_4:
    key2 = key.lower()
    lab = pop_key_4[key]
    # so = f"{key2} %s"
    structures_data[f"{key2} companies of"] = f"شركات {lab} في"
    structures_data[f"{key2} companies"] = f"شركات {lab}"
    structures_data[f"{key2} firms"] = f"شركات {lab}"
    structures_data[f"{key2} firms of"] = f"شركات {lab} في"

    structures_data[f"{key2} agencies"] = f"وكالات {lab}"
    structures_data[f"{key2} disciplines"] = f"تخصصات {lab}"
    structures_data[f"{key2} museums"] = f"متاحف {lab}"
    structures_data[f"governmental {key2} organizations"] = f"منظمات {lab} حكومية"
    structures_data[f"{key2} organizations"] = f"منظمات {lab}"
    structures_data[f"{key2} organization"] = f"منظمات {lab}"
    structures_data[f"{key2} facilities"] = f"مرافق {lab}"
    structures_data[f"{key2} bunkers"] = f"مخابئ {lab}"
    structures_data[f"{key2} industry"] = f"صناعة {lab}"
    structures_data[f"{key2} industry organisations"] = f"منظمات صناعة {lab}"
    structures_data[f"{key2} industry organizations"] = f"منظمات صناعة {lab}"

    structures_data[f"{key2} geology"] = f"جيولوجيا {lab}"
    structures_data[f"{key2} mining"] = f"تعدين {lab}"
    structures_data[f"{key2} technology"] = f"تقانة {lab}"
    structures_data[f"{key2} disasters"] = f"كوارث {lab}"
    structures_data[f"{key2} issues"] = f"قضايا {lab}"
    # New_male_keys[f"{key2} economics"] = "اقتصاد {}".format(lab)

    structures_data[f"{key2} electricity"] = f"كهرباء {lab}"
    structures_data[f"{key2} fields"] = f"حقول {lab}"
    structures_data[f"{key2} infrastructure"] = f"البنية التحتية {lab}"
    structures_data[f"{key2} refineries"] = f"مصافي {lab}"
    structures_data[f"{key2} pipelines"] = f"خطوط أنابيب {lab}"

    structures_data[f"{key2} stations"] = f"محطات {lab}"
    structures_data[f"defunct {key2} stations"] = f"محطات {lab} سابقة"
    structures_data[f"disused {key2} stations"] = f"محطات {lab} مهجورة"
    structures_data["disused " + (f"{key2} stations")] = f"محطات {lab} مهجورة"
    if "طاقة" not in lab:
        structures_data[f"{key2} energy"] = f"طاقة {lab}"
        structures_data[f"{key2} power plants"] = f"محطات طاقة {lab}"
        structures_data[f"{key2} power stations"] = f"محطات طاقة {lab}"
        structures_data["proposed " + f"{key2} power stations"] = f"محطات طاقة {lab} مقترحة"
        structures_data["former " + f"{key2} power stations"] = f"محطات طاقة {lab} سابقة"
        structures_data["demolished " + f"{key2} power stations"] = f"محطات طاقة {lab} مدمرة"
    else:
        structures_data[f"{key2} power stations"] = f"محطات {lab}"
        structures_data[f"{key2} power plants"] = f"محطات {lab}"
        structures_data["proposed " + f"{key2} power stations"] = f"محطات {lab} مقترحة"
        structures_data["former " + f"{key2} power stations"] = f"محطات {lab} سابقة"
        structures_data["demolished " + f"{key2} power stations"] = f"محطات {lab} مدمرة"

    structures_data[f"{key2} politics"] = f"سياسة {lab}"
    structures_data[f"{key2} buildings"] = f"مبان {lab}"
    structures_data[f"{key2} structures"] = f"منشآت {lab}"
    structures_data[f"{key2} installations"] = f"منشآت {lab}"
    structures_data[f"{key2} logistics installations"] = f"منشآت لوجستية {lab}"
    structures_data[f"{key2} buildings and structures"] = f"مبان ومنشآت {lab}"
    structures_data[f"{key2} building and structure"] = f"مبان ومنشآت {lab}"
# ---

buildings_keys = {
    "lighthouses": "منارات",
    "Road bridges": "جسور طرق",
    "synagogues": "كنس",
    "ferries": "عبارات",
    "bridges": "جسور",
    "bridge": "جسور",
    "Astronomical observatories": "مراصد فلكية",
    "road incidents": "حوادث طرق",
    "Hotels": "فنادق",
    "Hospitals": "مستشفيات",
    "roads": "طرق",
    "owers": "أبراج",
    "Schools": "مدارس",
    "studios": "استديوهات",
    "Recording studios": "استديوهات تسجيل",
    "structures": "منشآت",
    "Industrial buildings and structures": "مبان ومنشآت صناعية",
    "transport buildings and structures": "مبان ومنشآت نقل",
    "Agricultural buildings and structures": "مبان ومنشآت زراعية",
    "buildings and structures": "مبان ومنشآت",
    "Cemeteries": "مقابر",
    # 'burials': "مدافن",
    "burials": "مدفونون",
    "Clubhouses": "نوادي",
    "buildings": "مباني",
    "supermarkets": "محلات سوبر ماركت",
    "restaurants": "مطاعم",
    "commercial buildings": "مباني تجارية",
    "bank buildings": "مباني بنوك",
    "architecture museums": "متاحف معمارية",
    "History Museums": "متاحف تاريخية",
    "Transportation Museums": "متاحف النقل",
    "Science Museums": "متاحف علمية",
    "Sports Museums": "متاحف رياضية",
    "Military and war Museums": "متاحف عسكرية وحربية",
    "fountains": "نوافير",
    "sports venues": "ملاعب رياضية",
    "canals": "ممرات مائية",
    "towers": "أبراج",
    "clock towers": "أبراج ساعة",
    "laboratories": "مختبرات",
    "libraries": "مكتبات",
    "facilities": "مرافق",
    "Mines": "مناجم",
    "monuments and memorials": "معالم أثرية ونصب تذكارية",
    "monuments and structures": "معالم أثرية ومنشآت",
    "burial monuments and structures": "معالم ومنشآت أماكن الدفن",
    "monuments": "معالم أثرية",
    "memorials": "نصب تذكارية",
    "theatres": "مسارح",
    "palaces": "قصور",
    "Museums": "متاحف",
    "Nature centers": "مراكز طبيعية",
    "sculpture": "منحوتات",
    "Outdoor sculptures": "منحوتات خارجية",
    "medical education": "تعليم طبي",
    "islamic education": "تعليم إسلامي",
    "places of worship": "أماكن عبادة",
    "skyscrapers": "ناطحات سحاب",
    "skyscraper hotels": "فنادق ناطحات سحاب",
    "transportation": "وسائل نقل",
    "memorials and cemeteries": "نصب تذكارية ومقابر",
    "universities and colleges": "جامعات وكليات",
    "schools": "مدارس",
    # "state universities": "جامعات ولايات",
    "public universities": "جامعات حكومية",
    "national universities": "جامعات وطنية",
    "state universities and colleges": "جامعات وكليات ولايات",
    "islamic universities and colleges": "جامعات وكليات إسلامية",
    "national universities and colleges": "جامعات وكليات وطنية",
    "public universities and colleges": "جامعات وكليات حكومية",
}

sub_buildings_keys = {
    "libraries": "مكتبات",
    "universities": "جامعات",
    "colleges": "كليات",
    "universities and colleges": "جامعات وكليات",
    "schools": "مدارس",
}

tab2 = {
    "Standardized tests": "اختبارات قياسية",
    "distance education": "التعليم عن بعد",
    "education controversies": "خلافات متعلقة بالتعليم",
}

for en1, ar1 in sub_buildings_keys.items():
    tab2[f"{en1}"] = f"{ar1}"

    # tab2[f"state {en1}"] = f"{ar1} ولايات"
    tab2[f"federal {en1}"] = f"{ar1} فيدرالية"

    tab2[f"government {en1}"] = f"{ar1} حكومية"
    tab2[f"public {en1}"] = f"{ar1} حكومية"

    tab2[f"national {en1}"] = f"{ar1} وطنية"
    tab2[f"islamic {en1}"] = f"{ar1} إسلامية"

buildings_keys.update(tab2)

pop_final_3_update = {}

for ke2, ke2_lab in buildings_keys.items():
    ke_2 = ke2.lower()
    if ke2_lab:
        zaz = f"{ke2_lab}  في السجل الوطني للأماكن التاريخية في "
        pop_final_3_update[f"christian {ke2}"] = f"{ke2_lab} مسيحية"

        pop_final_3_update[f"defunct {ke2}"] = f"{ke2_lab} سابقة"
        # pop_final_3_update['{} on the National Register of Historic Places in'.format(ke2)] = za
        pop_final_3_update[f"{ke2} on national-register-of-historic-places in"] = zaz
        pop_final_3_update[f"{ke2} on the-national-register-of-historic-places in"] = zaz
        pop_final_3_update[ke_2] = ke2_lab
        pop_final_3_update[f"{ke2} disasters"] = f"كوارث {ke2_lab}"
