"""
Key-label mappings for generic mixed categories.
"""

from __future__ import annotations

from collections.abc import Mapping
from unittest import result

from ...helps import len_print, logger
from ..jobs.jobs_singers import SINGERS_TAB
from ..languages import MEDIA_CATEGORY_TRANSLATIONS, language_key_translations
from ..sports import TENNIS_KEYS
from ..tv.films_mslslat import film_keys_for_female, film_keys_for_male
from ..utils.json_dir import open_json_file
from .all_keys3 import ALBUMS_TYPE, pop_final_3
from .all_keys4 import new2019
from .keys2 import keys2_py
from .keys_23 import NEW_2023
from .Newkey import pop_final6

People_key = open_json_file("people/peoples.json") or {}

BASE_LABELS: dict[str, str] = {
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
    "law": "قانون",
    "books": "كتب",
    "military": "عسكرية",
    "the israel–hamas war": "الحرب الفلسطينية الإسرائيلية",
    "israel–hamas war": "الحرب الفلسطينية الإسرائيلية",
    "israel–hamas war protests": "احتجاجات الحرب الفلسطينية الإسرائيلية",
    "navy of": "بحرية",
    "gulf of": "خليج",
    "acts of": "أفعال",
}

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
    "technology": "تقانة",
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
    "comic strips": "شرائط كومكس",
    "comic": "قصص مصورة",
    "comics": "قصص مصورة",
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
    "non-fiction": "غير خيالية",
    "non fiction": "غير خيالية",
    "linguistics": "لغوية",
    "literary": "أدبية",
    "maritime": "بحرية",
    "social": "اجتماعية",
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
    "miniseries": "مسلسلات قصيرة",
    "television miniseries": "مسلسلات قصيرة تلفزيونية",
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


def _update_lowercase(data: dict[str, str], mapping: list[Mapping[str, str]], skip_existing: bool = False) -> None:
    """Populate ``data`` with lowercase keys from the provided mappings."""

    def check_skip_existing(key) -> bool:
        """Determine whether a lowercase entry should overwrite existing data."""
        if skip_existing:
            return data.get(key.lower()) is None
        return True

    for table in mapping:
        data.update(
            {
                key.lower(): v.strip()
                for key, v in table.items()
                if key.strip() and v.strip() and check_skip_existing(key)
            }
        )


def _build_book_entries(data: dict[str, str]) -> None:
    """Add literature related entries, including film/tv variants."""

    for category_key, category_label in BOOK_CATEGORIES.items():
        data[category_key] = category_label
        data[f"defunct {category_key}"] = f"{category_label} سابقة"
        data[f"{category_key} publications"] = f"منشورات {category_label}"
        lower_category = category_key.lower()
        for key, key_label in film_keys_for_female.items():
            data[f"{key.lower()} {lower_category}"] = f"{category_label} {key_label}"

        for book_type, book_label in BOOK_TYPES.items():
            data[f"{book_type.lower()} {lower_category}"] = f"{category_label} {book_label}"

    data["musical compositions"] = "مؤلفات موسيقية"

    for singers_key, singer_label in SINGERS_TAB.items():
        key_lower = singers_key.lower()
        if key_lower not in data and singer_label:
            data[key_lower] = singer_label
            data[f"{key_lower} albums"] = f"ألبومات {singer_label}"
            data[f"{key_lower} songs"] = f"أغاني {singer_label}"
            data[f"{key_lower} groups"] = f"فرق {singer_label}"
            data[f"{key_lower} duos"] = f"فرق {singer_label} ثنائية"

            data[f"{singers_key} video albums"] = f"ألبومات فيديو {singer_label}"

            for album_type, album_label in ALBUMS_TYPE.items():
                data[f"{singers_key} {album_type} albums"] = f"ألبومات {album_label} {singer_label}"
    return data


def _build_weapon_entries() -> dict[str, str]:
    """Expand weapon classifications with related events."""
    data = {}
    for w_class, w_class_label in WEAPON_CLASSIFICATIONS.items():
        for event_key, event_label in WEAPON_EVENTS.items():
            data[f"{w_class} {event_key}"] = f"{event_label} {w_class_label}"

    return data


def _build_direction_region_entries() -> dict[str, str]:
    """Add entries that combine geographic directions with regions."""
    data = {}
    for direction_key, direction_label in DIRECTIONS.items():
        for region_key, region_label in REGIONS.items():
            data[f"{direction_key} {region_key}"] = f"{direction_label} {region_label}"
    return data


def _build_towns_entries(data) -> None:
    """Add town and community variants for different descriptors."""

    for category, label in TOWNS_COMMUNITIES.items():
        data[f"{category} communities"] = f"مجتمعات {label}"
        data[f"{category} towns"] = f"بلدات {label}"
        data[f"{category} villages"] = f"قرى {label}"
        data[f"{category} cities"] = f"مدن {label}"


def _build_of_variants(data, data_list, data_list2) -> dict[str, str]:
    """Add "of" variants for categories and map them to Arabic labels."""
    for tab in data_list:
        for key, value in tab.items():
            new_key = f"{key.lower()} of"
            if data.get(new_key) or key.endswith(" of"):
                continue
            data[new_key] = value

    for tab2 in data_list2:
        for key2, value2 in tab2.items():
            new_key2 = f"{key2} of"
            if data.get(new_key2) or key2.endswith(" of"):
                continue
            data[new_key2] = f"{value2} في"

    return data


def _build_literature_area_entries(data) -> None:
    """Add entries for literature and arts areas linked with film keys."""

    for area, area_label in LITERATURE_AREAS.items():
        data[f"children's {area}"] = f"{area_label} الأطفال"
        for key, key_label in film_keys_for_male.items():
            data[f"{key.lower()} {area.lower()}"] = f"{area_label} {key_label}"


def _build_cinema_entries(data) -> None:
    """Add mappings for cinema and television related categories."""

    for key, label in CINEMA_CATEGORIES.items():
        data[key] = label
        data[f"{key} set"] = f"{label} تقع أحداثها"
        data[f"{key} produced"] = f"{label} أنتجت"
        data[f"{key} filmed"] = f"{label} صورت"
        data[f"{key} basedon"] = f"{label} مبنية على"
        # data[f"{key} based on"] = f"{label} مبنية على"
        data[f"{key} based"] = f"{label} مبنية"
        data[f"{key} shot"] = f"{label} مصورة"


def build_pf_keys2(pop_of_football, pop_of_without_in, pop_of_with_in) -> dict[str, str]:
    """Build the master mapping used across the ``translations`` package."""

    data = {}

    data.update(pop_of_football)

    for competition_key, competition_label in pop_of_football.items():
        data[f"{competition_key} medalists"] = f"فائزون بميداليات {competition_label}"

    data.update(keys2_py)
    data.update(BASE_LABELS)
    data.update(_build_direction_region_entries())
    data.update(pop_of_with_in)
    pop_of_without_in = dict(pop_of_without_in)

    pop_of_without_in_del = {"explorers": "مستكشفون", "historians": "مؤرخون"}
    for key in pop_of_without_in_del:
        pop_of_without_in.pop(key, None)

    _update_lowercase(data, [pop_of_without_in], skip_existing=True)

    _build_of_variants(data, [pop_of_without_in], [pop_of_with_in])

    for school_category, school_template in SCHOOL_LABELS.items():
        data[f"private {school_category}"] = school_template.format("خاصة")
        data[f"public {school_category}"] = school_template.format("عامة")

    _update_lowercase(data, [WORD_AFTER_YEARS], skip_existing=False)

    _build_towns_entries(data)

    data.update({key.lower(): value for key, value in ART_MOVEMENTS.items()})

    tato_type = {
        "treason": "خيانة",
        "harassment": "مضايقة",
        "archaeological parks": "متنزهات أثرية",
        "architecture museums": "متاحف معمارية",
        "architecture schools": "مدارس عمارة",
        "architecture-schools": "مدارس عمارة",
        "arms trafficking": "الاتجار بالأسلحة",
        "arson": "إحراق الممتلكات",
        "assault": "الاعتداء",
        "attempted murder": "الشروع في القتل",
        "attempted rape": "محاولة الاغتصاب",
        "bank buildings": "مباني بنوك",
        "blackmail": "الابتزاز",
        "blasphemy": "ازدراء الدين",
        "bribery": "الرشوة",
        "building collapses": "انهيارات مباني",
        "burglary": "السطو",
        "child pornography offenses": "جرائم استغلال الأطفال في المواد الإباحية",
        "child sexual abuse": "الاعتداء الجنسي على الأطفال",
        "commercial buildings": "مبان تجارية",
        "cruelty to animals": "القسوة على الحيوانات",
        "culpable homicide": "القتل العمد",
        "cybercrime": "الجريمة الإلكترونية",
        "depriving others of their civil rights": "حرمان الآخرين من حقوقهم المدنية",
        "drama schools": "مدارس درامية",
        "drug offenses": "جرائم المخدرات",
        "embezzlement": "الاختلاس",
        "ethnic groups": "مجموعات عرقية",
        "financial services": "خدمات مالية",
        "hate crimes": "جرائم الكراهيه",
        "historical societies": "جمعيات تاريخية",
        "history museums": "متاحف تاريخية",
        "history organizations": "منظمات تاريخ",
        "holocaust denial offenses": "جرائم إنكار الهولوكوست",
        "hospital buildings": "مباني مستشفيات",
        "incest": "زنى المحارم",
        "independent schools": "مدارس مستقلة",
        "insider trading": "التجارة من الباطن",
        "international crimes": "الجرائم الدولية",
        "international schools": "مدارس دولية",
        "law schools": "مدارس قانون",
        "learned societies": "جمعيات علمية",
        "making false statements": "تقديم بيانات كاذبة",
        "management consulting": "استشارات إدارية",
        "manslaughter": "قتل خطأ",
        "marine art museums": "متاحف فن بحري",
        "marine art": "فن بحري",
        "metals": "المعادن",
        "military academies": "أكاديميات عسكرية",
        "military and war museums": "متاحف عسكرية وحربية",
        "military research": "أبحاث عسكرية",
        "misusing public funds": "إساءة استخدام الأموال العامة",
        "music schools": "مدارس موسيقى",
        "naval museums": "متاحف بحرية",
        "obstruction of justice": "إعاقة سير العدالة",
        "perverting course of justice": "تحريف مسار العدالة",
        "police officers": "ضباط شرطة",
        "private schools": "مدارس خاصة",
        "professional associations": "جمعيات تخصصية",
        "public utilities": "مرافق عمومية",
        "racial hatred offences": "جرائم الكراهية العنصرية",
        "racketeering": "ابتزاز الأموال",
        "rape": "الاغتصاب",
        "real estate services": "خدمات عقارية",
        "refusing to convert to christianity": "رفض اعتناق المسيحية",
        "refusing to convert to islam": "رفض اعتناق الإسلام",
        "robbery": "السرقة",
        "science museums": "متاحف علمية",
        "sex crimes": "الجرائم الجنسية",
        "sex offences": "جرائم جنسية",
        "sexual assault": "اعتداء جنسي",
        "soliciting murder": "التماس القتل",
        "sports museums": "متاحف رياضية",
        "sports schools": "مدارس رياضية",
        "stalking": "المطاردة",
        "tax crimes": "الجرائم الضريبية",
        "teaching hospitals": "مستشفيات تعليمية",
        "trade associations": "اتحادات تجارية",
        "transportation museums": "متاحف النقل",
        "under construction": "تحت الإنشاء",
        "video gaming": "ألعاب الفيديو",
        "witchcraft": "السحر",
        "world war i museums": "متاحف الحرب العالمية الأولى",
        "world war ii museums": "متاحف الحرب العالمية الثانية",
    }

    data.update({key.lower(): value for key, value in tato_type.items()})

    weapon_data = _build_weapon_entries()
    data.update(weapon_data)

    _build_of_variants(data, [], [weapon_data])

    minister_keys_2 = {
        "ministers of": "وزراء",
        "government ministers of": "وزراء",
        "women's ministers of": "وزيرات",
        "deputy prime ministers of": "نواب رؤساء وزراء",
        "finance ministers of": "وزراء مالية",
        "foreign ministers of": "وزراء خارجية",
        "prime ministers of": "رؤساء وزراء",
        "sport-ministers": "وزراء رياضة",
        "sports-ministers": "وزراء رياضة",
        "ministers of power": "وزراء طاقة",
        "ministers-of power": "وزراء طاقة",
    }
    data.update(minister_keys_2)

    for key, value in pop_final_3.items():
        lower_key = key.lower()
        if lower_key not in data and value:
            data[lower_key] = value

    _build_book_entries(data)
    _build_literature_area_entries(data)
    _build_cinema_entries(data)

    return data


def wrap_build_pf_keys2() -> tuple[dict[str, str], dict[str, str], dict[str, str]]:
    """Wrap the ``build_pf_keys2`` function with additional data loading."""

    pop_of_football = open_json_file("population/pop_of_football.json") or {}
    pop_of_without_in = open_json_file("population/pop_of_without_in.json") or {}
    pop_of_with_in = open_json_file("population/pop_of_with_in.json") or {}

    pf_keys2: dict[str, str] = build_pf_keys2(pop_of_football, pop_of_without_in, pop_of_with_in)

    _update_lowercase(pf_keys2, [TENNIS_KEYS, pop_final6, MEDIA_CATEGORY_TRANSLATIONS], skip_existing=True)
    _update_lowercase(pf_keys2, [language_key_translations, People_key, new2019, NEW_2023], skip_existing=False)

    pop_of_football_lower = {key.lower(): value for key, value in pop_of_football.items()}

    return pf_keys2, pop_of_without_in, pop_of_football_lower


def _handle_the_prefix(label_index: dict[str, str]) -> dict[str, str]:
    """Handle 'the ' prefix in country labels."""
    new_keys = {}
    for key, value in list(label_index.items()):
        if not key.lower().startswith("the ") or not value:
            continue

        trimmed_key = key[len("the ") :].strip()
        if trimmed_key in label_index:
            continue
        new_keys.setdefault(trimmed_key, value)

    logger.debug(f">> _handle_the_prefix() Added {len(new_keys)} entries without 'the ' prefix.")
    return new_keys


pf_keys2, pop_of_without_in, pop_of_football_lower = wrap_build_pf_keys2()

no_the = _handle_the_prefix(pf_keys2)
pf_keys2.update(no_the)


def get_from_pf_keys2(text: str) -> str:
    """Look up the Arabic label for a term in the ``pf_keys2`` mapping."""
    label = pf_keys2.get(text, "")
    logger.info(f">> get_from_pf_keys2() Found: {label}")
    return label


len_print.data_len(
    "all_keys2.py",
    {
        "People_key": People_key,
        "pf_keys2": pf_keys2,
        "pop_of_without_in": pop_of_without_in,
        "pop_of_football_lower": pop_of_football_lower,
        "WORD_AFTER_YEARS": WORD_AFTER_YEARS,
        "BOOK_CATEGORIES": BOOK_CATEGORIES,
        "BOOK_TYPES": BOOK_TYPES,
    },
)

__all__ = [
    "get_from_pf_keys2",
    "pf_keys2",
    "pop_of_without_in",
    "pop_of_football_lower",
    "WORD_AFTER_YEARS",
    "BOOK_CATEGORIES",
]
