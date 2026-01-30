#!/usr/bin/python3
"""

countries_names.py use only countries names without nationalities
countries_names_v2.py use countries names with nationalities

"""

import functools

import logging
from ...translations import countries_nat_en_key
from ...translations_formats import FormatDataV2
from ..nationalities_resolvers.data import country_names_and_nats_data
from .countries_names_data import formatted_data_en_ar_only

logger = logging.getLogger(__name__)

countries_nat_en_key_example = {
    "yemen": {
        "ar": "اليمن",
        "en": "Yemen",
        "male": "يمني",
        "female": "يمنية",
        "the_male": "اليمني",
        "the_female": "اليمنية",
    }
}

new_data: dict[str, str] = {
    "national assembly of {en}": "الجمعية الوطنية {the_female}",
    # the_female
    "dependent territories of {en}": "أقاليم ما وراء البحار {the_female}",
    "supreme court of {en}": "المحكمة العليا {the_female}",
}

# NOTE: patterns with only en-ar should be in formatted_data_en_ar_only countries_names.py to handle countries without gender details
# NOTE: patterns with only en-ar-time should be in COUNTRY_YEAR_DATA to handle countries-time without gender details

all_data: dict[str, str] = {
    # the_female
    "{en} cup-of-nations": "كأس الأمم {the_female}",
    "{en} cup of nations": "كأس الأمم {the_female}",
    "women's {en} cup of nations": "كأس الأمم {the_female} للسيدات",
    "women's {en} cup-of-nations": "كأس الأمم {the_female} للسيدات",
    "{en} cup-of-nations players": "لاعبو كأس الأمم {the_female}",
    "{en} cup of nations players": "لاعبو كأس الأمم {the_female}",
    "women's {en} cup of nations players": "لاعبات كأس الأمم {the_female} للسيدات",
    "women's {en} cup-of-nations players": "لاعبات كأس الأمم {the_female} للسيدات",
    # males - en_is_P17_ar_is_mens
    "{en} political leaders": "قادة سياسيون {males}",
    "{en} political leader": "قادة سياسيون {males}",
    "{en} government officials": "مسؤولون حكوميون {males}",
    # female - military_format_women_without_al_from_end
    # Category:Unmanned_aerial_vehicles_of_Jordan > طائرات بدون طيار أردنية
    "unmanned military aircraft-of {en}": "طائرات عسكرية بدون طيار {female}",
    "unmanned military aircraft of {en}": "طائرات عسكرية بدون طيار {female}",
    "unmanned aerial vehicles-of {en}": "طائرات بدون طيار {female}",
    "unmanned aerial vehicles of {en}": "طائرات بدون طيار {female}",
}

all_data.update(country_names_and_nats_data)


@functools.lru_cache(maxsize=1)
def _load_bot() -> FormatDataV2:
    """Load and configure the country names v2 translation bot.

    Creates and configures a FormatDataV2 instance that handles the translation
    of country-related category names with nationalities using formatted data
    and nationality mappings.

    Returns:
        FormatDataV2: Configured bot instance for country name with nationality translation.
    """
    nats_data = {x: v for x, v in countries_nat_en_key.items() if v.get("ar")}
    formatted_data = all_data | new_data | formatted_data_en_ar_only

    return FormatDataV2(
        formatted_data=formatted_data,
        data_list=nats_data,
        key_placeholder="{en}",
        text_before="the ",
    )


@functools.lru_cache(maxsize=10000)
def resolve_by_countries_names_v2(category: str) -> str:
    """Resolve a country name category (with nationalities) to its Arabic translation.

    Translates English category names that contain country names with nationalities
    to their Arabic equivalents using the configured translation bot. This function
    specifically handles categories that use nationalities (e.g., "French writers"
    rather than "writers from France").

    Args:
        category (str): The English category name containing country names with nationalities to be translated.

    Returns:
        str: The Arabic translation of the category, or an empty string if not found.
    """
    logger.debug(f"<<yellow>> start: {category=}")

    nat_bot = _load_bot()
    result = nat_bot.search_all_category(category)

    logger.info(f"<<yellow>> end: {category=}, {result=}")
    return result


__all__ = [
    "resolve_by_countries_names_v2",
]
