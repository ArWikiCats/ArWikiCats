#!/usr/bin/python3
"""
This resolver uses two different formatting data sets to resolve
categories that mention relations/conflicts between two countries.

"""

import functools

from ...helps import getLogger

logger = getLogger(__name__)
from ...translations import (
    COUNTRY_LABEL_OVERRIDES,
    All_Nat,
    all_country_ar,
    all_country_with_nat,
    countries_en_as_nationality_keys,
    countries_nat_en_key,
)
from ...translations_formats import FormatDataDouble, FormatDataDoubleV2
from ..nats_as_country_names import nats_keys_as_country_names

countries_en_keys = [x.get("en") for x in all_country_with_nat.values() if x.get("en")]


formatted_data_v1 = {
    # P17_PREFIXES: Mapping[str, str] = {}
    "{en} treaties": "معاهدات {ar}",
    "{en} conflict": "صراع {ar}",
    "{en} proxy conflict": "صراع {ar} بالوكالة",
    "{en} relations": "علاقات {ar}",
    "{en} sports relations": "علاقات {ar} الرياضية",
}

formatted_data_v2 = {
    # RELATIONS_FEMALE: Mapping[str, str] = {}
    "{en} military relations": "العلاقات {the_female} العسكرية",
    "{en} sports relations": "العلاقات {the_female} الرياضية",
    "{en} joint economic efforts": "الجهود الاقتصادية المشتركة {the_female}",
    "{en} relations": "العلاقات {the_female}",
    "{en} border crossings": "معابر الحدود {the_female}",
    "{en} border towns": "بلدات الحدود {the_female}",
    "{en} border": "الحدود {the_female}",
    "{en} clashes": "الاشتباكات {the_female}",
    "{en} wars": "الحروب {the_female}",
    "{en} war": "الحرب {the_female}",
    "{en} war of independence": "حرب الاستقلال {the_female}",
    "{en} border war": "حرب الحدود {the_female}",
    "{en} war films": "أفلام الحرب {the_female}",
    "{en} war video games": "ألعاب فيديو الحرب {the_female}",
    # RELATIONS_MALE: Mapping[str, str] = {}
    "{en} conflict video games": "ألعاب فيديو الصراع {the_male}",
    "{en} conflict legal issues": "قضايا قانونية في الصراع {the_male}",
    "{en} conflict": "الصراع {the_male}",
    "{en} football rivalry": "التنافس {the_male} في كرة القدم",
}


@functools.lru_cache(maxsize=1)
def _load_all_country_labels_v2() -> dict[str, dict[str, str]]:
    data = dict(countries_nat_en_key)
    # nats_data = { x: v for x, v in All_Nat.items() }
    # nats_data.update({ x: v for x, v in nats_keys_as_country_names.items() })
    data.update(
        {
            "ireland": {
                "male": "أيرلندي",
                "males": "أيرلنديون",
                "female": "أيرلندية",
                "females": "أيرلنديات",
                "the_male": "الأيرلندي",
                "the_female": "الأيرلندية",
                "en": "ireland",
                "ar": "أيرلندا",
            }
        }
    )
    return data


@functools.lru_cache(maxsize=1)
def _load_all_country_labels_v1() -> dict[str, str]:
    all_country_labels = dict(all_country_ar)
    all_country_labels.update(
        {
            "saint kitts and nevis": "سانت كيتس ونيفيس",
            "serbia and montenegro": "صربيا والجبل الأسود",
            "south vietnam": "فيتنام الجنوبية",
            "dominica": "دومينيكا",
            "saint vincent and grenadines": "سانت فنسنت وجزر غرينادين",
            "somaliland": "أرض الصومال",
            "eswatini": "إسواتيني",
            "são tomé and príncipe": "ساو تومي وبرينسيب",
            "serbia-and-montenegro": "صربيا والجبل الأسود",
            "nato": "الناتو",
            "austrian empire": "الإمبراطورية النمساوية",
            "tokelau": "توكيلاو",
            "saint lucia": "سانت لوسيا",
            "european union": "الاتحاد الأوروبي",
        }
    )
    all_country_labels.update({k: v for k, v in COUNTRY_LABEL_OVERRIDES.items() if "(" not in k})
    return all_country_labels


@functools.lru_cache(maxsize=1)
def double_bot_v1() -> FormatDataDouble:
    """
    Create and return a cached FormatDataDouble instance for handling country names in English and Arabic.
    This function loads all country labels using _load_all_country_labels_v1() and initializes a FormatDataDouble object
    with predefined formatting parameters, including placeholders for English and Arabic labels, a splitter for parsing,
    an Arabic joiner, and sorting of Arabic labels.
    Returns:
        FormatDataDouble: An instance configured for double-language country name processing.
    """
    all_country_labels = _load_all_country_labels_v1()
    _bot = FormatDataDouble(
        formatted_data=formatted_data_v1,
        data_list=all_country_labels,
        key_placeholder="{en}",
        value_placeholder="{ar}",
        splitter=r"[−–\- ]",
        ar_joiner=" و",
        sort_ar_labels=True,
    )

    return _bot


@functools.lru_cache(maxsize=1)
def double_bot_v2() -> FormatDataDoubleV2:
    """
    Creates and returns a FormatDataDoubleV2 instance configured for processing country names.
    This function loads all country labels using the internal helper function _load_all_country_labels_v2().
    It then initializes a FormatDataDoubleV2 object with the following parameters:
    - formatted_data: Set to formatted_data_v2 (presumably predefined formatted data).
    - data_list: The list of all country labels loaded.
    - key_placeholder: "{en}" for English placeholders.
    - splitter: A regex pattern "[ -–]" to split on spaces, hyphens, or en dashes.
    - sort_ar_labels: True to sort Arabic labels.
    Returns:
        FormatDataDoubleV2: An instance of FormatDataDoubleV2 configured for double-format processing of country names.
    """
    all_country_labels = _load_all_country_labels_v2()
    _bot = FormatDataDoubleV2(
        formatted_data=formatted_data_v2,
        data_list=all_country_labels,
        key_placeholder="{en}",
        splitter=r"[−–\- ]",
        sort_ar_labels=True,
    )

    return _bot


def fix_keys(category: str) -> str:
    """Fix known issues in category keys before searching.

    Args:
        category: The original category key.
    """
    # Fix specific known issues with category keys
    category = category.lower().replace("category:", "")
    category = category.replace("'", "")
    return category.strip()


@functools.lru_cache(maxsize=10000)
def resolve_v1(category: str) -> str:
    """
    Examples:
        >>> # Example of a dual-country resolution (v1)
        >>> resolve_v1("jordan–iraq relations")
        'علاقات الأردن والعراق'
        >>> # Example of skipping a single country key
        >>> resolve_v1("jordan")
    """
    logger.debug(f"<<yellow>> start resolve_v1: {category=}")

    all_country_labels = _load_all_country_labels_v1()
    if category in all_country_labels:
        # NOTE: only country key should be handled by other resolvers
        logger.info(f"<<yellow>> skip resolve_v1: one country key only {category=}, [result=]")
        return ""

    result = double_bot_v1().search_all_category(category)
    logger.info_if_or_debug(f"<<yellow>> end resolve_v1: {category=}, {result=}", result)
    return result


@functools.lru_cache(maxsize=10000)
def resolve_v2(category: str) -> str:
    """
    Examples:
        >>> # Example of a dual-country resolution (v2)
        >>> resolve_v2("jordan–iraq relations")
        'العلاقات الأردنية العراقية'
        >>> # Example of skipping a single country key
        >>> resolve_v2("jordan")
    """
    category = category.replace("democratic republic of congo", "democratic-republic-of-congo")
    category = category.replace("republic of congo", "republic-of-congo")
    logger.debug(f"<<yellow>> start resolve_v2: {category=}")

    nat_data = _load_all_country_labels_v2()
    if category in nat_data:
        # NOTE: only nationality key should be handled by other resolvers
        logger.info(f"<<yellow>> skip resolve_v2: one nationality key only {category=}, [result=]")
        return ""

    result = double_bot_v2().search_all_category(category)
    logger.info_if_or_debug(f"<<yellow>> end resolve_v2: {category=}, {result=}", result)
    return result


def resolve_countries_names_double(category: str) -> str:
    category = fix_keys(category)
    # logger.debug(f"<<yellow>> start resolve_countries_names_double: {category=}")

    if category in countries_en_as_nationality_keys or category in countries_en_keys:
        logger.info(f"<<yellow>> skip resolve_countries_names_double: {category=}, [result=]")
        return ""

    result = resolve_v2(category) or resolve_v1(category)

    # logger.info_if_or_debug(f"<<yellow>> end resolve_countries_names_double: {category=}, {result=}", result)
    return result


__all__ = [
    "resolve_countries_names_double",
]
