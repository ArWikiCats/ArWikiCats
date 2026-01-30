#!/usr/bin/python3
"""
Resolve geo names categories translations
NOTE: planned to replace pop_format in format_bots/__init__.py
"""

import functools
import logging
from typing import Dict

from ...translations import COUNTRY_LABEL_OVERRIDES, raw_region_overrides
from ...translations_formats import FormatData, MultiDataFormatterBase
from .countries_names_data import formatted_data_en_ar_only

logger = logging.getLogger(__name__)

formatted_data_updated = dict(formatted_data_en_ar_only)

geo_keys: Dict[str, str] = {
    "sanaa": "صنعاء",
    "manitoba": "مانيتوبا",
    "bologna": "بولونيا",
    "hubei": "خوبي",
    "west virginia": "فرجينيا الغربية",
}

geo_data: Dict[str, str] = COUNTRY_LABEL_OVERRIDES | raw_region_overrides | geo_keys


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBase:
    return FormatData(
        formatted_data_updated,
        geo_data,
        key_placeholder="{en}",
        value_placeholder="{ar}",
        text_before="the ",
        regex_filter=r"[\w-]",
    )


@functools.lru_cache(maxsize=10000)
def resolve_by_geo_names(category: str) -> str:
    logger.debug(f"<<yellow>> start {category=}")

    nat_bot = _load_bot()
    result = nat_bot.search_all_category(category)

    logger.info(f"<<yellow>> end {category=}, {result=}")
    return result


__all__ = [
    "resolve_by_geo_names",
]
