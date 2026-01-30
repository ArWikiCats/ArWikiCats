"""University labelling helpers."""

from __future__ import annotations

import functools
import logging
from typing import Dict

from ..translations import CITY_TRANSLATIONS_LOWER
from ..translations_formats import FormatData

logger = logging.getLogger(__name__)

CITY_LOWER = {
    "chandler, oklahoma": "تشاندلر (أوكلاهوما)",
    "changchun": "تشانغتشون",
    "changde": "تشانغده",
    "changhua county": "مقاطعة تشانغوا",
    "changning, hunan": "تشانغ نينغ، هونان",
    "changnyeong county": "محافظة تشانغنيونغ",
    "changsha": "تشانغشا",
    "changzhi": "تشانغ تشى",
    "changzhou": "تشانغتشو",
    "chanhassen, minnesota": "تشانهاسين (منيسوتا)",
    "chania": "خانية",
    "channahon, illinois": "تشاناهون (إلينوي)",
    "chaohu": "شاوهو",
    "chaoyang, liaoning": "تشاويانغ",
    "chaozhou": "شاوزو",
    "chapayevsk": "تشاباييفسك",
    "chapin, south carolina": "تشابين (كارولاينا الجنوبية)",
    "chaplin, connecticut": "تشابين (كونيتيكت)",
    "chapmanville, west virginia": "تشامبانفيل (فرجينيا الغربية)",
    "chardon, ohio": "تشاردن",
    "port townsend, washington": "بورت تاونسند",
    "portage": "بورتج",
    "portage la prairie": "بورتاج لابريري",
    "portage, indiana": "بورتاغ",
    "portage, wisconsin": "بورتاغ (ويسكونسن)",
    "portalegre, portugal": "بورتاليغري (البرتغال)",
    "portales, new mexico": "بورتاليس",
    "porter": "بورتر",
    "porterville, california": "بورتيرفيل (كاليفورنيا)",
    "portland, maine": "بورتلاند (مين)",
    "portland, oregon": "بورتلاند (أوريغن)",
    "porto": "بورتو",
    "porto alegre": "بورتو أليغري",
    "porto-novo": "بورتو نوفو",
    "portola valley, california": "بورتولا فالي (كاليفورنيا)",
    "portorož": "بورتوروز",
    "portsmouth, new hampshire": "بورتسموث (نيوهامشير)",
    "portsmouth, ohio": "بورتسموث (أوهايو)",
    "portsmouth, rhode island": "بورتسموث (رود آيلاند)",
    "portsmouth, virginia": "بورتسموث (فرجينيا)",
    "portuguese malacca": "ملقا البرتغالية",
    "porvoo": "بورفو",
    "posadas, misiones": "بوساداس (ميسيونيس)",
    "posey": "بوسي",
    "potenza": "بوتنسا",
}

CITY_LOWER.update(CITY_TRANSLATIONS_LOWER)

MAJORS: Dict[str, str] = {
    "medical sciences": "للعلوم الطبية",
    "international university": "الدولية",
    "art": "للفنون",
    "arts": "للفنون",
    "biology": "للبيولوجيا",
    "chemistry": "للشيمية",
    "computer science": "للكمبيوتر",
    "economics": "للاقتصاد",
    "education": "للتعليم",
    "engineering": "للهندسة",
    "geography": "للجغرافيا",
    "geology": "للجيولوجيا",
    "history": "للتاريخ",
    "law": "للقانون",
    "mathematics": "للرياضيات",
    "technology": "للتكنولوجيا",
    "physics": "للفيزياء",
    "psychology": "للصحة",
    "sociology": "للأمن والسلوك",
    "political science": "للسياسة",
    "social science": "للأمن والسلوك",
    "social sciences": "للأمن والسلوك",
    "science and technology": "للعلوم والتكنولوجيا",
    "science": "للعلوم",
    "reading": "للقراءة",
    "applied sciences": "للعلوم التطبيقية",
}

UNIVERSITIES_TABLES: Dict[str, str] = {
    "national maritime university": "جامعة {} الوطنية البحرية",
    "national university": "جامعة {} الوطنية",
}

for major, arabic_label in MAJORS.items():
    normalized_major = major.lower()
    template = f"جامعة {{}} {arabic_label}"
    UNIVERSITIES_TABLES[f"university of {normalized_major}"] = template
    UNIVERSITIES_TABLES[f"university-of-{normalized_major}"] = template
    UNIVERSITIES_TABLES[f"university of the {normalized_major}"] = template
    UNIVERSITIES_TABLES[f"university-of-the-{normalized_major}"] = template

# Build formatted_data for FormatData bot
_formatted_university_data = {}
for key, template in UNIVERSITIES_TABLES.items():
    ar_template = template.replace("{}", "{city_ar}")
    # Patterns for "{city} {university_key}"
    _formatted_university_data[f"{{city}} {key}"] = ar_template
    # Patterns for "{university_key}, {city}"
    _formatted_university_data[f"{key}, {{city}}"] = ar_template
    # Patterns for "{university_key} {city}"
    _formatted_university_data[f"{key} {{city}}"] = ar_template

_university_bot = FormatData(
    formatted_data=_formatted_university_data,
    data_list=CITY_LOWER,
    key_placeholder="{city}",
    value_placeholder="{city_ar}",
)


def _normalise_category(category: str) -> str:
    """Lowercase and strip ``category`` while removing ``Category:`` prefix."""

    normalized = category.lower().strip()
    if normalized.startswith("category:"):
        normalized = normalized[len("category:") :].strip()
    return normalized


@functools.lru_cache(maxsize=2048)
def resolve_university_category(category: str) -> str:
    """
    Resolve a normalized university-related category into its Arabic university label.

    Returns:
        str: The Arabic university label formatted with the resolved city name, or an empty string if no mapping is found.
    """

    normalized_category = _normalise_category(category)

    logger.info(f"<<lightblue>>>> vvvvvvvvvvvv start, (category:{normalized_category}) vvvvvvvvvvvv ")

    university_label = _university_bot.search(normalized_category)

    if university_label:
        logger.info(f"<<lightblue>>>>>>: new {university_label=} ")

    logger.info("<<lightblue>>>> ^^^^^^^^^ end ^^^^^^^^^ ")
    return university_label


__all__ = [
    "resolve_university_category",
]
