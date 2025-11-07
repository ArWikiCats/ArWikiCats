"""Key-label mappings for generic mixed categories.

This module historically contained a large amount of inline dictionary
manipulation.  The refactored version keeps the data unchanged while providing
structured helper functions, type hints and documentation to make future
maintenance straightforward.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Final

from ..jobs.jobs_singers import singers_tab
from ..languages import cccccc_m, languages_key
from ..others.peoples import People_key
from ..politics.ministers import minister_keyse, ministrees_keysse
from ..sports import tennis_keys
from ..tv.films_mslslat import film_Keys_For_female, film_Keys_For_male
from .all_keys3 import albums_type, pop_final_3
from .all_keys4 import new2019
from .key_registry import KeyRegistry, load_json_mapping
from .keys2 import keys2_py
from .keys_23 import new_2023
from .Newkey import pop_final6

BASE_LABELS: Final[dict[str, str]] = {
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
}

DIRECTIONS: Final[dict[str, str]] = {
    "southeast": "جنوب شرق",
    "southwest": "جنوب غرب",
    "northwest": "شمال غرب",
    "northeast": "شمال شرق",
    "north": "شمال",
    "south": "جنوب",
    "west": "غرب",
    "east": "شرق",
}

REGIONS: Final[dict[str, str]] = {
    "asia": "آسيا",
    "europe": "أوروبا",
    "africa": "إفريقيا",
    "oceania": "أوقيانوسيا",
}

SCHOOL_LABELS: Final[dict[str, str]] = {
    "bilingual schools": "مدارس {} ثنائية اللغة",
    "high schools": "مدارس ثانوية {}",
    "middle schools": "مدارس إعدادية {}",
    "elementary schools": "مدارس إبتدائية {}",
}

WORD_AFTER_YEARS: Final[dict[str, str]] = {
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

TOWNS_COMMUNITIES: Final[dict[str, str]] = {
    "muslim": "إسلامية",
    "fishing": "صيد",
    "mining": "تعدين",
    "coastal": "شاطئية",
    "ghost": "أشباح",
}

ART_MOVEMENTS: Final[dict[str, str]] = {
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

WEAPON_CLASSIFICATIONS: Final[dict[str, str]] = {
    "biological": "بيولوجية",
    "chemical": "كيميائية",
    "military nuclear": "نووية عسكرية",
    "nuclear": "نووية",
    "military": "عسكرية",
}

WEAPON_EVENTS: Final[dict[str, str]] = {
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

BOOK_CATEGORIES: Final[dict[str, str]] = {
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
    "short stories": "قصص صيرة",
    "soundtracks": "موسيقى تصويرية",
    "texts": "نصوص",
    "treaties": "اتفاقيات",
    "webcomic": "ويب كومكس",
    "webcomics": "ويب كومكس",
    "websites": "مواقع ويب",
    "wikis": "ويكيات",
}

BOOK_TYPES: Final[dict[str, str]] = {
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
}

LITERATURE_AREAS: Final[dict[str, str]] = {
    "literature": "أدب",
    "folklore": "فلكور",
    "poetry": "شعر",
    "film": "فيلم",
}

CINEMA_CATEGORIES: Final[dict[str, str]] = {
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


def _update_lowercase(target: KeyRegistry, mapping: Mapping[str, str], *, skip_existing: bool = False) -> None:
    """Apply ``KeyRegistry.update_lowercase`` with a descriptive name."""

    target.update_lowercase(mapping, skip_existing=skip_existing)


def _build_school_entries(registry: KeyRegistry) -> None:
    """Populate school related variants in ``registry``."""

    for school_category, template in SCHOOL_LABELS.items():
        registry.data[f"private {school_category}"] = template.format("خاصة")
        registry.data[f"public {school_category}"] = template.format("عامة")


def _build_direction_region_entries(registry: KeyRegistry) -> None:
    """Add entries that combine geographic directions with regions."""

    registry.add_cross_product(
        DIRECTIONS,
        REGIONS,
        key_template="{first} {second}",
        value_template="{first_label} {second_label}",
    )


def _build_population_variants(registry: KeyRegistry, pop_of_football: Mapping[str, str]) -> None:
    """Add derived entries for population based dictionaries."""

    for competition_key, competition_label in pop_of_football.items():
        registry.data[f"{competition_key} medalists"] = f"فائزون بميداليات {competition_label}"

    pop_of_with_in = load_json_mapping("pop_of_with_in")
    registry.update(pop_of_with_in)
    for population_key, population_label in pop_of_with_in.items():
        registry.data[f"{population_key} of"] = f"{population_label} في"

    pop_of_without_in = load_json_mapping("pop_of_without_in")
    pop_of_without_in.update(ministrees_keysse)
    registry.update_lowercase(pop_of_without_in, skip_existing=True)
    registry.update(
        {f"{key.lower()} of": value for key, value in pop_of_without_in.items() if key},
    )
    registry.data["navy of"] = "بحرية"
    registry.data["gulf of"] = "خليج"

    # Keep a module level reference for legacy imports that expect the
    # dictionary with additional ministerial categories.
    globals()["pop_of_without_in"] = pop_of_without_in


def _build_word_after_years(registry: KeyRegistry) -> None:
    """Merge entries that usually appear after years."""

    registry.update({key.lower(): value for key, value in WORD_AFTER_YEARS.items()})


def _build_towns_entries(registry: KeyRegistry) -> None:
    """Add town and community variants for different descriptors."""

    for category, label in TOWNS_COMMUNITIES.items():
        registry.data[f"{category} communities"] = f"مجتمعات {label}"
        registry.data[f"{category} towns"] = f"بلدات {label}"
        registry.data[f"{category} villages"] = f"قرى {label}"
        registry.data[f"{category} cities"] = f"مدن {label}"


def _build_art_movement_entries(registry: KeyRegistry) -> None:
    """Add artistic movement names with lowercase keys."""

    registry.update({key.lower(): value for key, value in ART_MOVEMENTS.items()})


def _build_weapon_entries(registry: KeyRegistry) -> None:
    """Expand weapon classifications with related events."""

    for classification, classification_label in WEAPON_CLASSIFICATIONS.items():
        for event_key, event_label in WEAPON_EVENTS.items():
            registry.data[f"{classification} {event_key}"] = f"{event_label} {classification_label}"
            registry.data[f"{classification} {event_key} of"] = f"{event_label} {classification_label} في"


def _build_book_entries(registry: KeyRegistry) -> None:
    """Add literature related entries, including film/tv variants."""

    for category_key, category_label in BOOK_CATEGORIES.items():
        registry.data[category_key] = category_label
        registry.data[f"defunct {category_key}"] = f"{category_label} سابقة"
        registry.data[f"{category_key} publications"] = f"منشوات {category_label}"
        lower_category = category_key.lower()
        for key, key_label in film_Keys_For_female.items():
            registry.data[f"{key.lower()} {lower_category}"] = f"{category_label} {key_label}"
        for book_type, book_label in BOOK_TYPES.items():
            registry.data[f"{book_type.lower()} {lower_category}"] = f"{category_label} {book_label}"

    registry.data["musical compositions"] = "مؤلفات موسيقية"

    for singers_key, singer_label in singers_tab.items():
        lower = singers_key.lower()
        if lower not in registry.data and singer_label:
            registry.data[lower] = singer_label
            registry.data[f"{lower} albums"] = f"ألبومات {singer_label}"
            registry.data[f"{lower} songs"] = f"أغاني {singer_label}"
            registry.data[f"{lower} groups"] = f"فرق {singer_label}"
            registry.data[f"{lower} duos"] = f"فرق {singer_label} ثنائية"
            registry.data[f"{singers_key} video albums"] = f"ألبومات فيديو {singer_label}"
            for album_type, album_label in albums_type.items():
                registry.data[f"{singers_key} {album_type} albums"] = f"ألبومات {album_label} {singer_label}"


def _build_literature_area_entries(registry: KeyRegistry) -> None:
    """Add entries for literature and arts areas linked with film keys."""

    for area, area_label in LITERATURE_AREAS.items():
        registry.data[f"children's {area}"] = f"{area_label} الأطفال"
        for key, key_label in film_Keys_For_male.items():
            registry.data[f"{key.lower()} {area}"] = f"{area_label} {key_label}"


def _build_cinema_entries(registry: KeyRegistry) -> None:
    """Add mappings for cinema and television related categories."""

    for key, label in CINEMA_CATEGORIES.items():
        registry.data[key] = label
        registry.data[f"{key} set"] = f"{label} تقع أحداثها"
        registry.data[f"{key} produced"] = f"{label} أنتجت"
        registry.data[f"{key} filmed"] = f"{label} صورت"
        registry.data[f"{key} basedon"] = f"{label} مبنية على"
        registry.data[f"{key} based"] = f"{label} مبنية"
        registry.data[f"{key} shot"] = f"{label} مصورة"


def build_pf_keys2() -> dict[str, str]:
    """Build the master mapping used across the ``ma_lists`` package."""

    registry = KeyRegistry()
    pop_of_football = load_json_mapping("pop_of_football")
    registry.update(pop_of_football)
    registry.update(keys2_py)
    registry.update(BASE_LABELS)

    _build_direction_region_entries(registry)
    _build_population_variants(registry, pop_of_football)
    _build_school_entries(registry)
    _build_word_after_years(registry)
    _build_towns_entries(registry)
    _build_art_movement_entries(registry)

    tato_type = load_json_mapping("Tato_type")
    registry.update({key.lower(): value for key, value in tato_type.items()})

    _build_weapon_entries(registry)

    registry.update(minister_keyse)

    for key, value in pop_final_3.items():
        lower = key.lower()
        if lower not in registry.data and value:
            registry.data[lower] = value

    _build_book_entries(registry)
    _build_literature_area_entries(registry)
    _build_cinema_entries(registry)

    registry.update_lowercase(tennis_keys, skip_existing=True)
    registry.update_lowercase(pop_final6, skip_existing=True)
    registry.update_lowercase(cccccc_m, skip_existing=True)
    _update_lowercase(registry, languages_key)
    _update_lowercase(registry, People_key)
    _update_lowercase(registry, new2019)
    registry.update_lowercase(new_2023)

    registry.data["law"] = "قانون"
    registry.data["books"] = "كتب"
    registry.data["military"] = "عسكرية"

    # Expose the lowercase helper dictionary for legacy imports.
    globals()["pop_of_football_lower"] = {key.lower(): value for key, value in pop_of_football.items()}

    return registry.data


pf_keys2: dict[str, str] = build_pf_keys2()

# Backwards compatibility alias used by legacy imports.
Word_After_Years = WORD_AFTER_YEARS

__all__ = [
    "pf_keys2",
    "pop_of_without_in",
    "pop_of_football_lower",
    "Word_After_Years",
]
