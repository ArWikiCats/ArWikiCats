#!/usr/bin/python3
"""
"""

from ...helps.jsonl_dump import dump_data
from ...helps.log import logger
from ...translations import (
    All_Nat,
    SPORT_FORMATS_FOR_P17,
    en_nats_to_ar_label,
)
from ..jobs_bots.get_helps import get_suffix_with_keys


# @functools.lru_cache(maxsize=None)
@dump_data(enable=True)
def load_SPORT_FORMATS_FOR_P17(category: str, check_the: bool = False) -> str:
    """
    TODO: use FormatData method

    Example:
        category:Yemeni under-13 baseball teams", result: "فرق كرة قاعدة يمنية تحت 13 سنة"
    """
    normalized_category = category.lower()

    sport_format_key, country_start = get_suffix_with_keys(normalized_category, All_Nat, "nat", check_the=check_the)

    logger.debug(f"sport_lab_oioioi_load {normalized_category=}: {sport_format_key=} {country_start=}")

    if not country_start or not sport_format_key:
        return ""

    country_label = en_nats_to_ar_label.get(country_start, "")

    if not country_label:
        return ""

    sport_format_label = SPORT_FORMATS_FOR_P17.get(sport_format_key, "")

    if not sport_format_label:
        return ""

    category_label = sport_format_label.format(nat=country_label)
    logger.debug(f'<<lightblue>>xxx sport_lab_oioioi_load: new category_label  "{category_label}"')

    return category_label
