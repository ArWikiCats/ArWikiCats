#!/usr/bin/python3
r"""
\s*['"]\{\} \{\}['"]\.format\(\s*(.*?)\s*,\s*(.*?)\s*\)
f"{$1} {$2}"


['"]\{\} \{\}['"]\.format\(\s*([\w\d]+)\s*,\s*([\w\d]+)\s*\)
f"{$1} {$2}"

"""


# ---
from pathlib import Path
import json

from .games_labs import summer_winter_tabs

Dir2 = Path(__file__).parent
# ---
with open(f"{Dir2}/jsons/pop_final_3.json", "r", encoding="utf-8") as f:
    pop_final_3 = json.load(f)
# ---
# 'extradited people': "أشخاص تم تسليمهم",
# 'people extradited': "أشخاص تم تسليمهم",
# 'programs\xe2\x80\x8e': "برامج",
# "the louvre":"متحف اللوفر",
# "the paralympics":"الألعاب البارالمبية",
# "heavy metal musical groups":"فرق موسيقى هيفي ميتال",
# "black metal musical groups":"فرق موسيقى بلاك ميتال" ,
# ---
typeTable_7 = {
    "air force": "قوات جوية",
    "people executed by": "أشخاص أعدموا من قبل",
    "executions": "إعدامات",
    "executed-burning": "أعدموا شنقاً",
    "executed-hanging": "أعدموا حرقاً",
    "executed-decapitation": "أعدموا بقطع الرأس",
    "executed-firearm": "أعدموا بسلاح ناري",
    "people executed-by-burning": "أشخاص أعدموا شنقاً",
    "people executed-by-hanging": "أشخاص أعدموا حرقاً",
    "people executed-by-decapitation": "أشخاص أعدموا بقطع الرأس",
    "people executed-by-firearm": "أشخاص أعدموا بسلاح ناري",
}
# ---
albums_type = {
    "folktronica": "فولكترونيكا",
    "concept": "مفاهيمية",
    "surprise": "مفاجئة",
    "comedy": "كوميدية",
    "mixtape": "ميكستايب",
    "remix": "ريمكس",
    "animation": "رسوم متحركة",
    "video": "فيديو",
    "compilation": "تجميعية",
    "live": "مباشرة",
    "jazz": "جاز",
    "eps": "أسطوانة مطولة",
    "folk": "فولك",
}
# ---
businesspeoples = {
    "video game": "ألعاب الفيديو",
    "real estate": "العقارات",
    "financial": "المالية",
    "metals": "المعادن",
    "entertainment": "الترفيه",
    "fashion": "الأزياء",
    "computer": "كمبيوتر",
    "cosmetics": "مستحضرات التجميل",
}
# ---
for iu in businesspeoples:
    pop_final_3[f"{iu} businesspeople"] = f"شخصيات أعمال في {businesspeoples[iu]}"
    pop_final_3[f"{iu} industry businesspeople"] = f"شخصيات أعمال في صناعة {businesspeoples[iu]}"
# ---
film_production_company = {
    "Yash Raj": "ياش راج",
    "Illumination Entertainment": "إليمونيشن للترفيه",
    "Walt Disney Animation Studios": "استديوهات والت ديزني للرسوم المتحركة",
    "Carolco Pictures": "كارلوكو بيكشرز",
    "Aardman Animations": "آردمان انيمشنز",
    "Soyuzmultfilm": "سويز مولتفيلم",
    "Weinstein Company": "شركة وينشتاين",
    "Castle Rock Entertainment": "كاسل روك للترفيه",
    "United Artists": "يونايتد آرتيست",
    "Mosfilm": "موسفيلم",
    "National Geographic Society": "منظمة ناشيونال جيوغرافيك",
    "Showtime (TV network)": "شوتايم",
    "Touchstone Pictures": "توتشستون بيكشرز",
    "Rooster Teeth": "أسنان الديك",
    "Blue Sky Studios": "استديوهات بلو سكاي",
    "Bad Robot Productions": "باد روبوت للإنتاج",
    "TMS Entertainment": "تي أم أس إنترتنيمنت",
    "Sony Pictures Entertainment": "سوني بيكشرز إنترتنمنت",
    "sony pictures animation": "سوني بيكشرز أنيماشين",
    "Toei Company": "شركة توي",
    "Toho": "توهو",
    "Universal Studios": "يونيفرسل ستوديوز",
    "Walt Disney Company": "ديزني",
    "Paramount Pictures": "باراماونت بيكتشرز",
    "20th Century Fox": "تونتيث سينتشوري فوكس",
    "DreamWorks Animation": "دريمووركس أنيماشين",
    "Pixar": "بيكسار",
    "Metro-Goldwyn-Mayer": "مترو غولدوين ماير",
    "Lucasfilm": "لوكاس فيلم",
    "Amblin Entertainment": "أمبلين للترفيه",
    "DreamWorks": "دريم ووركس",
    "Funimation": "شركة فنميشن للترفيه",
    "Columbia Pictures": "كولومبيا بيكتشرز",
    "Marvel Studios": "استوديوهات مارفل",
    "HBO": "هوم بوكس أوفيس",
    "Warner Bros.": "وارنر برذرز",
}
for production, pro_lab in film_production_company.items():
    pop_final_3[production] = pro_lab
    pop_final_3[f"{production} films"] = f"أفلام {pro_lab}"


pop_final_3.update(summer_winter_tabs)


def Add_companies():
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
    for roo in Roood:
        oi = Roood[roo]["si"]
        pop_final_3[roo] = oi
        for dd in tyui:
            pop_final_3[f"{roo} {dd}"] = f"{tyui[dd]} {oi}"

        oi2 = Roood[roo]["bb"]
        pop_final_3[f"defunct {roo} of"] = f"{oi2} سابقة في"
        pop_final_3[f"defunct {roo}"] = f"{oi2} سابقة"
        for dd in tyui2:
            pop_final_3[f"{roo} {dd}"] = f"{tyui2[dd]} {oi2}"
            typeTable_7[f"{roo} {dd}"] = f"{tyui2[dd]} {oi2}"
            pop_final_3[f"{roo} {dd} of"] = f"{tyui2[dd]} {oi2} في"


Add_companies()


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
    "Standardized tests" : "اختبارات قياسية",
    "distance education" : "التعليم عن بعد",
    "education controversies" : "خلافات متعلقة بالتعليم",
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
pop_final_3.update(tab2)

for ke2, ke2_lab in buildings_keys.items():
    ke_2 = ke2.lower()
    if ke2_lab:
        zaz = f"{ke2_lab}  في السجل الوطني للأماكن التاريخية في "
        pop_final_3[f"christian {ke2}"] = f"{ke2_lab} مسيحية"

        pop_final_3[f"defunct {ke2}"] = f"{ke2_lab} سابقة"
        # pop_final_3['{} on the National Register of Historic Places in'.format(ke2)] = za
        pop_final_3[f"{ke2} on national-register-of-historic-places in"] = zaz
        pop_final_3[f"{ke2} on the-national-register-of-historic-places in"] = zaz
        pop_final_3[ke_2] = ke2_lab
        # ---
        pop_final_3[f"{ke2} disasters"] = f"كوارث {ke2_lab}"

# ---
Ambassadors_tab = {}

NN_table = {}
NN_table2 = {
    "south african": {"men": "جنوب إفريقي", "women": "جنوب إفريقية"},
    "democratic republic of the congo": {
        "men": "كونغوي الديمقراطي",
        "women": "كونغوية الديمقراطية",
    },
    "bissau-guinean": {"men": "غيني البيساوي", "women": "غينية البيساوية"},
    "south american": {"men": "أمريكي الجنوبي", "women": "أمريكية الجنوبية"},
    "north american": {"men": "أمريكي الشمالي", "women": "أمريكية الشمالية"},
    "northern ireland": {"men": "أيرلندي الشمالي", "women": "أيرلندية الشمالية"},
    "hong kong": {"men": "هونغ كونغي", "women": "هونغ كونغية"},
    "equatoguinean": {"men": "غيني الاستوائي", "women": "غينية الاستوائية"},
    "east timorese": {"men": "تيموري الشرقي", "women": "تيمورية الشرقية"},
    "south korean": {"men": "كوري الجنوبي", "women": "كورية الجنوبية"},
    "north korean": {"men": "كوري الشمالي", "women": "كورية الشمالية"},
}
tennis_key = {
    "european athletics championships": "بطولة أوروبا لألعاب القوى",
    "deaflympics": "ديفلمبياد",
    "badminton in the summer olympics": "تنس الريشة في الألعاب الأولمبية الصيفية",
    "asian athletics championships": "بطولة آسيا لألعاب القوى",
    "racewalking": "سباق المشي",
    "european athletics indoor championships": "بطولة أوروبا لألعاب القوى داخل الصالات",
    "european championships": "بطولات أوروبا",
    "swiss cup": "كأس سويسرا لكرة القدم",
    "world championships-in-athletics athletes": "عداؤو بطولة العالم لألعاب القوى",
    "world championships in athletics athletes": "عداؤو بطولة العالم لألعاب القوى",
    "world championships in athletics": "بطولة العالم لألعاب القوى",
    "world championships-in-athletics": "بطولة العالم لألعاب القوى",
    "dutch tt": "كأس هولندا السياحية",
    "world table tennis championships": "بطولات عالمية لتنس الطاولة",
    "world touring car championship": "بطولة العالم لسيارات السياحة",
    "gcc champions league": "كأس الخليج للأندية",
    "german formula three championship": "بطولة فورمولا 3 الألمانية",
    "800 metres": "800 متر",
    "world champions": "أبطال العالم",
    "world championships": "بطولات العالم",
    "association football leagues": "دوريات كرة قدم",
    "figure skating in the winter universiade": "التزلج الفني في الألعاب الجامعية الشتوية",
    "copa argentina": "كوبا أرجنتينا",
    "golf tournaments": "بطولات غولف",
    "cycle racing": "سباق دراجات",
    "cycling competitions": "مسابقات الدراجات",
    "motorcycle racing": "سباق الدراجات النارية",
    "motorcycle racing series": "سلسلة سباقات الدراجات النارية",
    "horse races": "سباقات الخيل",
    "national championships": "بطولات وطنية",
    "rowing competitions": "منافسات تجديف",
    "arab athletics championships": "البطولة العربية لألعاب القوى",
    "badminton in the 2016 summer olympics": "كرة الريشة في الألعاب الأولمبية الصيفية 2016",
    "sports in the summer olympics": "رياضات في الألعاب الأولمبية الصيفية",
    "ice hockey tournaments": "منافسات هوكي للجليد",
    "ligue 1": "الدوري الفرنسي الدرجة الأولى",
    "world baseball classic": "عالم البيسبول الكلاسيكي",
    "international association football competitions": "منافسات كرة قدم دولية",
    "formula e": "فورمولا إي",
    "formula one": "فورمولا ون",
    "portuguese grand prix": "جائزة البرتغال الكبرى",
    "six nations championship": "بطولة الأمم الستة",
    "combination events": "مزيج أحداث",
    "auto racing": "سباق سيارات",
    "auto racing series": "سلسة سباق سيارات",
    "brd năstase țiriac trophy": "بطولة بوخارست للتنس",
    "brisbane international": "بطولة برزبين للتنس",
    "chennai open": "بطولة تشيناي المفتوحة للتنس",
    "australian open (tennis)": "بطولة أستراليا المفتوحة للتنس",
    "barcelona open (tennis)": "بطولة برشلونة للتنس",
    "canadian open (tennis)": "بطولة كندا للأساتذة",
    "chile open (tennis)": "بطولة تشيلي للتنس",
    "china open (tennis)": "بطولة الصين المفتوحة",
    "italian open (tennis)": "روما للماسترز",
    "madrid open (tennis)": "مدريد للماسترز",
    "mexican open (tennis)": "بطولة أكابولكو للتنس",
    "miami open (tennis)": "ميامي للماسترز",
    "qatar open (tennis)": "بطولة قطر المفتوحة للتنس",
    "shanghai masters (tennis)": "شنغهاي للماسترز",
    "australian open tennis": "بطولة أستراليا المفتوحة للتنس",
    "barcelona open tennis": "بطولة برشلونة للتنس",
    "canadian open tennis": "بطولة كندا للأساتذة",
    "chile open tennis": "بطولة تشيلي للتنس",
    "china open tennis": "بطولة الصين المفتوحة",
    "italian open tennis": "روما للماسترز",
    "madrid open tennis": "مدريد للماسترز",
    "mexican open tennis": "بطولة أكابولكو للتنس",
    "miami open tennis": "ميامي للماسترز",
    "qatar open tennis": "بطولة قطر المفتوحة للتنس",
    "shanghai masters tennis": "شنغهاي للماسترز",
    "cincinnati masters": "سنسيناتي للماسترز",
    "citi open": "بطولة واشنطن المفتوحة",
    "davis cup": "كأس ديفيز",
    "delray beach international tennis championships": "بطولة دلراي بيتش الدولية للتنس",
    "dubai tennis championships": "بطولة دبي للتنس",
    "fed cups": "كأس فيد",
    "fed cup": "كأس فيد",
    "french open": "دورة رولان غاروس الدولية",
    "geneva open": "بطولة جنيف المفتوحة",
    "gerry weber open": "بطولة هالي المفتوحة",
    "grand prix hassan ii": "بطولة الدار البيضاء للتنس",
    "hopman cup": "كأس هوبمان",
    "indian wells masters": "إنديان ويلز للماسترز",
    "istanbul open": "بطولة إسطنبول المفتوحة",
    "kremlin cup": "كأس الكرملين",
    "monte-carlo masters": "مونتي كارلو للماسترز",
    "nottingham open": "بطولة نوتنغهام المفتوحة",
    "open sud de france": "بطولة مونبلييه المفتوحة للتنس",
    "open de nice côte d'azur": "بطولة نيس المفتوحة للتنس",
    "paris masters": "باريس للماسترز",
    "portugal open": "البرتغال المفتوحة",
    "rai open": "راي المفتوحة",
    "rio open": "بطولة ريو للتنس",
    "rosmalen grass court championships": "بطولة روزمالين العشبية للتنس",
    "seoul open": "سول المفتوحة",
    "stockholm open": "بطولة ستوكهولم المفتوحة للتنس",
    "stuttgart open": "بطولة شتوتغارت المفتوحة",
    "swedish open": "بطولة السويد المفتوحة للتنس",
    "swiss indoors": "بطولة بازل للتنس",
    "sydney international": "بطولة سيدني للتنس",
    "tennis napoli cup": "كأس نابولي لكرة المضرب",
    "the championships, wimbledon": "بطولة ويمبلدون",
    "tunis open": "دورة تونس المفتوحة للتنس",
    "u.s. men's clay court championships": "بطولة هيوستن للتنس",
    "u.s. national indoor tennis championships": "بطولة ممفيس المفتوحة للتنس",
    "valencia open": "بطولة فالنسيا المفتوحة",
    "world tennis championship": "بطولة مبادلة العالمية للتنس",
    "zagreb indoors": "بطولة زغرب للتنس",
    "itf women's world tennis tour": "الجولة العالمية لتنس السيدات",
}
