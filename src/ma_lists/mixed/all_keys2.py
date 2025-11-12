"""
Key-label mappings for generic mixed categories.
"""

from __future__ import annotations
from ..utils.json_dir import open_json_file

from ..jobs.jobs_singers import SINGERS_TAB
from ..languages import cccccc_m, languages_key
from ..others.peoples import People_key
from ..politics.ministers import minister_keyse, ministrees_keysse
from ..sports import tennis_keys
from ..tv.films_mslslat import film_Keys_For_male, film_Keys_For_female
from .all_keys3 import ALBUMS_TYPE, pop_final_3
from .all_keys4 import new2019
from .keys2 import keys2_py
from .keys_23 import new_2023
from .Newkey import pop_final6
from ...helps import len_print

pop_of_football = open_json_file("pop_of_football") or {}

pf_keys2 = {}

pf_keys2.update(pop_of_football)

pf_keys2.update(keys2_py)
pf_keys2.update({
    "international reactions": "ردود فعل دولية",
    "domestic reactions": "ردود فعل محلية",
    "foreign involvement": "التدخل الأجنبي",
    "hostage crisis": "أزمة الرهائن",
    "violations of medical neutrality": "انتهاكات الحياد الطبي",
    "misinformation": "معلومات مضللة",
    "reactions": "ردود فعل",
    "israeli–palestinian conflict": "الصراع الإسرائيلي الفلسطيني",
    "legal issues": "قضايا قانونية",
    "stone-throwing": "رمي الحجارة",
    "temple mount and al-aqsa": "جبل الهيكل والأقصى",
    "sexual violence": "عنف جنسي",
    "hamas": "حماس",
    "the israel–hamas war": "الحرب الفلسطينية الإسرائيلية",
    "israel–hamas war": "الحرب الفلسطينية الإسرائيلية",
    "israel–hamas war protests": "احتجاجات الحرب الفلسطينية الإسرائيلية",
})

DIRECTIONS: dict[str, str] = {
    "southeast": "جنوب شرق",
    "southwest": "جنوب غرب",
    "northwest": "شمال غرب",
    "northeast": "شمال شرق",
    "north": "شمال",
    "south": "جنوب",
    "west": "غرب",
    "east": "شرق",
}

REGIONS: dict[str, str] = {
    "asia": "آسيا",
    "europe": "أوروبا",
    "africa": "إفريقيا",
    # "america":"أمريكا",
    "oceania": "أوقيانوسيا",
}

SCHOOL_LABELS: dict[str, str] = {
    "bilingual schools": "مدارس {} ثنائية اللغة",
    "high schools": "مدارس ثانوية {}",
    "middle schools": "مدارس إعدادية {}",
    "elementary schools": "مدارس إبتدائية {}",
}

WORD_AFTER_YEARS: dict[str, str] = {
    "YouTube channels": "قنوات يوتيوب",
    "births": "مواليد",
    "space probes": "مسبارات فضائية",
    "spacecraft": "مركبات فضائية",
    "spaceflight": "رحلات الفضاء",
    "works": "أعمال",
    "clashes": "اشتباكات",
    "endings": "نهايات",
    "fires": "حرائق",
    "tsunamis": "أمواج تسونامي",
    "landslides": "انهيارات أرضية",
    "floods": "فيضانات",
    "hoaxes": "خدع",
    "earthquakes": "زلازل",
    "elections": "انتخابات",
    "conferences": "مؤتمرات",
    "contests": "منافسات",
    "ballot measures": "إجراءات اقتراع",
    "ballot propositions": "اقتراحات اقتراع",
    "referendums": "استفتاءات",
    "beginnings": "بدايات",
}

TOWNS_COMMUNITIES: dict[str, str] = {
    "muslim": "إسلامية",
    "fishing": "صيد",
    "mining": "تعدين",
    "coastal": "شاطئية",
    "ghost": "أشباح",
}

ART_MOVEMENTS: dict[str, str] = {
    "renaissance": "عصر النهضة",
    "bronze age": "عصر برونزي",
    "stone age": "عصر حجري",
    "pop art": "فن البوب",
    "post-impressionism": "ما بعد الإنطباعية",
    "cubism": "تكعيبية",
    "beat generation": "جيل بيت",
    "romanticism": "رومانسية",
    "prehistoric art": "فن ما قبل التاريخ",
    "contemporary art": "فن معاصر",
    "land art": "فنون أرضية",
    "surrealism": "سريالية",
    "social realism": "الواقعية الإجتماعية",
    "northern renaissance": "عصر النهضة الشمالي",
    "baroque": "باروك",
    "socialist realism": "واقعية اشتراكية",
    "postmodernism": "ما بعد الحداثة",
    "symbolism (arts)": "رمزية",
    "insular art": "فن جزيري",
    "op art": "فن بصري",
    "neoclassicism": "الكلاسيكية الجديدة",
    "orientalism": "استشراق",
    "ukiyo-e": "أوكييو-إه",
    "gothic art": "الفن القوطي",
    "futurism": "مستقبلية",
    "fauvism": "حوشية",
    "mannerism": "مانييريزمو",
    "minimalism": "تقليلية",
    "de stijl": "دي ستايل",
    "classicism": "كلاسيكية",
    "dada": "دادا",
    "constructivism": "بنائية",
    "expressionism": "المذهب التعبيري",
    "constructivism (art)": "بنائية (فنون)",
    "early netherlandish painting": "رسم عصر النهضة المبكر الهولندي",
    "german renaissance": "عصر النهضة الألماني",
    "sturm und drang": "العاصفة والاندفاع",
    "postmodern literature": "أدب ما بعد الحداثة",
    "heidelberg school": "مدرسة هايدلبرغ",
    "literary realism": "واقعية أدبية",
    "impressionism": "انطباعية",
    "realism (art movement)": "واقعية (فنون)",
    "existentialism": "وجودية",
    "magic realism": "واقعية عجائبية",
    "conceptual art": "فن تصويري",
    "art nouveau": "الفن الجديد",
    "romanesque art": "فن رومانسكي",
    "avant-garde art": "طليعية",
    "environmental art": "فن بيئي",
    "byzantine art": "فن بيزنطي",
    "purism": "النقاء",
    "abstract expressionism": "التعبيرية التجريدية",
    "academic art": "فن أكاديمي",
    "art deco": "آرت ديكو",
    "pointillism": "تنقيطية",
    "biedermeier": "بيدرماير",
    "bauhaus": "باوهاوس",
    "realism": "واقعية",
    "latin american art": "فن أمريكا اللاتينية",
    "modernismo": "الحداثة (الأدب باللغة الإسبانية)",
}

WEAPON_CLASSIFICATIONS: dict[str, str] = {
    "biological": "بيولوجية",
    "chemical": "كيميائية",
    "military nuclear": "نووية عسكرية",
    "nuclear": "نووية",
    "military": "عسكرية",
}

WEAPON_EVENTS: dict[str, str] = {
    "accidents or incidents": "حوادث",
    "accidents-and-incidents": "حوادث",
    "accidents and incidents": "حوادث",
    "accidents": "حوادث",
    "operations": "عمليات",
    "weapons": "أسلحة",
    "battles": "معارك",
    "sieges": "حصارات",
    "missiles": "صواريخ",
    "technology": "تقنية",
}

BOOK_CATEGORIES: dict[str, str] = {
    # "live albums":"ألبومات مباشرة",
    "newspaper": "صحف",
    "conferences": "مؤتمرات",
    "events": "أحداث",
    "festivals": "مهرجانات",
    "albums": "ألبومات",
    "awards": "جوائز",
    "bibliographies": "ببليوجرافيات",
    "books": "كتب",
    "migrations": "هجرات",
    "video albums": "ألبومات فيديو",
    "classical albums": "ألبومات كلاسيكية",
    "comedy albums": "ألبومات كوميدية",
    "compilation albums": "ألبومات تجميعية",
    "mixtape albums": "ألبومات ميكستايب",
    "comic book": "كتب قصص مصورة",
    "comic strips": "شرائط مصورة",
    "comic": "قصص مصورة",
    "comics": "قصص مصورة",
    # "compositions": "تراكيب",
    # "compositions": "مؤلفات موسيقية",
    "cookbooks": "كتب طبخ",
    "crime": "جريمة",
    "dictionaries": "قواميس",
    "documentaries": "وثائقيات",
    "documents": "وثائق",
    "encyclopedias": "موسوعات",
    "essays": "مقالات",
    "films": "أفلام",
    "graphic novels": "روايات مصورة",
    "handbooks and manuals": "كتيبات وأدلة",
    "handbooks": "كتيبات",
    "journals": "نشرات دورية",
    "lectures": "محاضرات",
    "magazines": "مجلات",
    "manga": "مانغا",
    "manuals": "أدلة",
    "manuscripts": "مخطوطات",
    "marvel comics": "مارفال كومكس",
    "mmoirs": "مذكرات",
    "movements": "حركات",
    "musicals": "مسرحيات غنائية",
    "newspapers": "صحف",
    "novellas": "روايات قصيرة",
    "novels": "روايات",
    "operas": "أوبيرات",
    "organized crime": "جريمة منظمة",
    "paintings": "لوحات",
    "plays": "مسرحيات",
    "poems": "قصائد",
    "publications": "منشورات",
    "screenplays": "نصوص سينمائية",
    "short stories": "قصص قصيرة",
    "soundtracks": "موسيقى تصويرية",
    "texts": "نصوص",
    "treaties": "اتفاقيات",
    "webcomic": "ويب كومكس",
    "webcomics": "ويب كومكس",
    "websites": "مواقع ويب",
    "wikis": "ويكيات",
}


BOOK_TYPES: dict[str, str] = {
    # "pirate":"قراصنة",
    "anti-war": "مناهضة للحرب",
    "anti-revisionist": "مناهضة للتحريفية",
    "biographical": "سير ذاتية",
    "children's": "أطفال",
    "childrens": "أطفال",
    "cannabis": "قنب",
    "etiquette": "آداب التعامل",
    "illuminated": "مذهبة",
    "incidents": "حوادث",
    "magic": "سحر",
    "travel guide": "دليل سفر",
    "travel": "سفر",
    "structural": "هيكلية",
    "agricultural": "زراعية",
    "astronomical": "فلكية",
    "chemical": "كيميائية",
    "commercial": "تجارية",
    "economical": "اقتصادية",
    "educational": "تعليمية",
    "environmental": "بيئية",
    "experimental": "تجريبية",
    "historical": "تاريخية",
    "industrial": "صناعية",
    "internal": "داخلية",
    "international": "دولية",
    "legal": "قانونية",
    "magical": "سحرية",
    "medical": "طبية",
    "musical": "موسيقية",
    "nautical": "بحرية",
    "political": "سياسية",
    "residential": "سكنية",
    "reference": "مرجعية",
    "academic": "أكاديمية",
    "biography": "سيرة ذاتية",
    "education": "تعليم",
    "fiction": "خيالية",
    "linguistics": "لغوية",
    "literary": "أدبية",
    "maritime": "بحرية",
    "social": "اجتماعية",
    "non-fiction": "غير خيالية",
    "youth": "شبابية",
    "arts": "فنية",
    "media": "إعلامية",
    "writing": "الكتابة",
    # "realist":"واقعية",
    # "strategy":"استراتيجية",
    # "transportation":"نقل",
    # "military":"عسكرية",
    # "defense":"دفاعية",
    # "government":"حكومية",
    # "training":"تدريبية",
    # "warfare":"حربية",
    # "research":"بحثية",
    # "logistics":"لوجستية",
}


LITERATURE_AREAS: dict[str, str] = {
    "literature": "أدب",
    "folklore": "فلكور",
    "poetry": "شعر",
    "film": "فيلم",
}

CINEMA_CATEGORIES: dict[str, str] = {
    "films": "أفلام",
    "film series": "سلاسل أفلام",
    "television characters": "شخصيات تلفزيونية",
    "television series": "مسلسلات تلفزيونية",
    "television miniseries": "مسلسلات قصيرة",
    "television news": "أخبار تلفزيونية",
    "television programs": "برامج تلفزيونية",
    "television programmes": "برامج تلفزيونية",
    "television commercials": "إعلانات تجارية تلفزيونية",
    "television films": "أفلام تلفزيونية",
    "radio programs": "برامج إذاعية",
    "television shows": "عروض تلفزيونية",
    "video games": "ألعاب فيديو",
    "comics": "قصص مصورة",
    "marvel comics": "مارفال كومكس",
}


for direction_key, direction_label in DIRECTIONS.items():
    for region_key, region_label in REGIONS.items():
        arabic_label = f"{direction_label} {region_label}"
        combined_key = f"{direction_key} {region_key}"
        pf_keys2[combined_key] = arabic_label
# ---
pop_of_football_lower = {x.lower(): y for x, y in pop_of_football.items()}
# ---
for competition_key, competition_label in pop_of_football.items():
    pf_keys2[f"{competition_key} medalists"] = f"فائزون بميداليات {competition_label}"
# ---
pop_of_with_in = open_json_file("pop_of_with_in") or {}
# ---
pf_keys2.update(pop_of_with_in)
# ---
for population_key, population_label in pop_of_with_in.items():
    pf_keys2[f"{population_key} of"] = f"{population_label} في"
# ---
for school_category, school_template in SCHOOL_LABELS.items():
    pf_keys2[f"private {school_category}"] = school_template.format("خاصة")
    pf_keys2[f"public {school_category}"] = school_template.format("عامة")

pop_of_without_in = open_json_file("pop_of_without_in") or {}
# ---
pf_keys2.update({key.lower(): value for key, value in pop_of_without_in.items() if key.lower() not in pf_keys2})
pf_keys2.update({f"{key.lower()} of": value for key, value in pop_of_without_in.items()})
# ---
pf_keys2["navy of"] = "بحرية"
pf_keys2["gulf of"] = "خليج"
# ---

pf_keys2.update({x.lower(): v for x, v in WORD_AFTER_YEARS.items()})
# ---

for tt, tt_lab in TOWNS_COMMUNITIES.items():
    pf_keys2[f"{tt} communities"] = f"مجتمعات {tt_lab}"
    pf_keys2[f"{tt} towns"] = f"بلدات {tt_lab}"
    pf_keys2[f"{tt} villages"] = f"قرى {tt_lab}"
    pf_keys2[f"{tt} cities"] = f"مدن {tt_lab}"

pf_keys2.update({x.lower(): v for x, v in ART_MOVEMENTS.items()})

Tato_type = open_json_file("Tato_type") or {}

pf_keys2.update({x.lower(): v for x, v in Tato_type.items()})

for x, x_lab in WEAPON_CLASSIFICATIONS.items():
    for mis, mis_lab in WEAPON_EVENTS.items():
        pf_keys2[f"{x} {mis}"] = f"{mis_lab} {x_lab}"
        pf_keys2[f"{x} {mis} of"] = f"{mis_lab} {x_lab} في"

pop_of_without_in.update(ministrees_keysse)

pf_keys2.update(minister_keyse)

for po_3 in pop_final_3:
    poh = po_3.lower()
    if poh not in pf_keys2 and pop_final_3[po_3]:
        pf_keys2[poh] = pop_final_3[po_3]


for bo, bo_lab in BOOK_CATEGORIES.items():
    pf_keys2[bo] = bo_lab
    pf_keys2[f"defunct {bo}"] = f"{bo_lab} سابقة"
    pf_keys2[f"{bo} publications"] = f"منشوات {bo_lab}"

    bo2 = bo.lower()

    for ke, ke_lab in film_Keys_For_female.items():
        pf_keys2[f"{ke.lower()} {bo2}"] = f"{bo_lab} {ke_lab}"

    for fyy, fyy_lab in BOOK_TYPES.items():
        pf_keys2[f"{fyy.lower()} {bo2}"] = f"{bo_lab} {fyy_lab}"

pf_keys2["musical compositions"] = "مؤلفات موسيقية"


for nos, nos_lab in LITERATURE_AREAS.items():
    nos2 = nos.lower()
    pf_keys2[f"children's {nos}"] = f"{nos_lab} الأطفال"

    for ke, ke_lab in film_Keys_For_male.items():
        pf_keys2[f"{ke.lower()} {nos2}"] = f"{nos_lab} {ke_lab}"

for key, keylab in CINEMA_CATEGORIES.items():
    pf_keys2[key] = keylab
    pf_keys2[f"{key} set"] = f"{keylab} تقع أحداثها"
    pf_keys2[f"{key} produced"] = f"{keylab} أنتجت"
    pf_keys2[f"{key} filmed"] = f"{keylab} صورت"
    pf_keys2[f"{key} basedon"] = f"{keylab} مبنية على"
    # pf_keys2["{} based on".format(key)] = "{} مبنية على".format(keylab)
    pf_keys2[f"{key} based"] = f"{keylab} مبنية"
    pf_keys2[f"{key} shot"] = f"{keylab} مصورة"

for xfxx, xfxx_lab in SINGERS_TAB.items():  # all_keys3
    xc2 = xfxx.lower()
    if xc2 not in pf_keys2 and xfxx_lab:
        pf_keys2[xc2] = xfxx_lab
        pf_keys2[f"{xc2} albums"] = f"ألبومات {xfxx_lab}"
        pf_keys2[f"{xc2} songs"] = f"أغاني {xfxx_lab}"
        pf_keys2[f"{xc2} groups"] = f"فرق {xfxx_lab}"
        pf_keys2[f"{xc2} duos"] = f"فرق {xfxx_lab} ثنائية"

        pf_keys2[f"{xfxx} video albums"] = f"ألبومات فيديو {xfxx_lab}"

        for ty, ty_lab in ALBUMS_TYPE.items():
            pf_keys2[f"{xfxx} {ty} albums"] = f"ألبومات {ty_lab} {xfxx_lab}"

pf_keys2.update({k.lower(): v.strip() for k, v in tennis_keys.items() if k.strip() and v.strip() and not pf_keys2.get(k.lower())})

pf_keys2.update({k.lower(): v.strip() for k, v in pop_final6.items() if k.strip() and v.strip() and not pf_keys2.get(k.lower())})

pf_keys2.update({k.lower(): v.strip() for k, v in cccccc_m.items() if k.strip() and v.strip() and not pf_keys2.get(k.lower())})

pf_keys2.update({k.lower(): v.strip() for k, v in languages_key.items() if k.strip() and v.strip()})

pf_keys2.update({k.lower(): v.strip() for k, v in People_key.items() if k.strip() and v.strip()})

pf_keys2.update({k.lower(): v.strip() for k, v in new2019.items() if k.strip() and v.strip()})

pf_keys2.update({k22.lower(): v22.strip() for k22, v22 in new_2023.items() if k22.strip() and v22.strip()})

pf_keys2["law"] = "قانون"
pf_keys2["books"] = "كتب"
pf_keys2["military"] = "عسكرية"

mmmm = [
    "gymnastics",
    "polo",
    "cycle",
    "running",
    "football",
    "rugby",
    "shooting",
    "racing",
    "tennis",
    "handball",
    "volleyball",
    "sailing",
    "wrestling",
    "skiing",
    "surfing",
    "motor",
    "rally",
]

del pop_final_3
del keys2_py

len_print.data_len("all_keys2.py", {
    "pf_keys2": pf_keys2,
    "pop_of_without_in": pop_of_without_in,
    "pop_of_football_lower": pop_of_football_lower,
    "WORD_AFTER_YEARS": WORD_AFTER_YEARS,
    "BOOK_CATEGORIES": BOOK_CATEGORIES,
    "BOOK_TYPES": BOOK_TYPES,
})

__all__ = [
    "pf_keys2",
    "pop_of_without_in",
    "pop_of_football_lower",
    "WORD_AFTER_YEARS",
    "BOOK_CATEGORIES",
    "BOOK_TYPES",
]
