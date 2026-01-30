#!/usr/bin/python3
"""
Resolve country names categories translations

countries_names.py use only countries names without nationalities
countries_names_v2.py use countries names with nationalities

"""

import functools
from typing import Dict

import logging
from ...translations import countries_from_nat
from ...translations_formats import FormatData, MultiDataFormatterBase
from .countries_names_data import formatted_data_en_ar_only

logger = logging.getLogger(__name__)

# NOTE: ONLY_COUNTRY_NAMES should not merge to formatted_data_en_ar_only directly

ONLY_COUNTRY_NAMES = {
    "{en} political leader": "قادة {ar} السياسيون",
    "government ministers of {en}": "وزراء {ar}",
    "secretaries of {en}": "وزراء {ar}",
    "state lieutenant governors of {en}": "نواب حكام الولايات في {ar}",
    "state secretaries of state of {en}": "وزراء خارجية الولايات في {ar}",
}
formatted_data_updated = dict(formatted_data_en_ar_only)
formatted_data_updated.update(ONLY_COUNTRY_NAMES)
countries_from_nat_data: Dict[str, str] = dict(countries_from_nat)

# TODO: COUNTRY_LABEL_OVERRIDES already used in geo_names_formats.py


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBase:
    """Load and configure the country names translation bot.

    Creates and configures a FormatData instance that handles the translation
    of country-related category names using formatted data and country name mappings.

    Returns:
        MultiDataFormatterBase: Configured bot instance for country name translation.
    """
    return FormatData(
        formatted_data_updated,
        countries_from_nat_data,
        key_placeholder="{en}",
        value_placeholder="{ar}",
        text_before="the ",
        regex_filter=r"[\w-]",
    )


@functools.lru_cache(maxsize=10000)
def resolve_by_countries_names(category: str) -> str:
    """Resolve a country name category to its Arabic translation.

    Translates English category names that contain country names to their Arabic equivalents
    using the configured translation bot. This function specifically handles categories
    that use country names without nationalities (e.g., "writers from France" rather than "French writers").

    Args:
        category (str): The English category name containing country names to be translated.

    Returns:
        str: The Arabic translation of the category, or an empty string if not found.
    """
    logger.debug(f"<<yellow>> start resolve_by_countries_names: {category=}")

    nat_bot = _load_bot()
    result = nat_bot.search_all_category(category)

    logger.info_if_or_debug(f"<<yellow>> end resolve_by_countries_names: {category=}, {result=}", result)
    return result


__all__ = [
    "resolve_by_countries_names",
]
