""" """

import functools
import re

from ..helps import getLogger
from ..translations import (
    COUNTRY_LABEL_OVERRIDES,
    All_Nat,
    all_country_with_nat,
    countries_en_as_nationality_keys,
    countries_from_nat,
)
from ..translations_formats import MultiDataFormatterBaseV2, format_multi_data_v2

logger = getLogger(__name__)

# TODO: ADD SOME DATA FROM D:/categories_bot/langlinks/z2_data/COUNTRY_NAT.json
COUNTRY_NAT_DATA = {
    # French invasion of Russia
    "{en_nat} invasion of {country}": "الغزو {the_male} ل{country_ar}",
    # Afghan people imprisoned in the United States
    "{en_nat} people imprisoned-in {country}": "{males} مسجونون في {country_ar}",
    "{en_nat} people imprisoned in {country}": "{males} مسجونون في {country_ar}",
    # American spies for Nazi Germany > "جواسيس أمريكيون لصالح ألمانيا النازية"
    "{en_nat} spies for {country}": "جواسيس {males} لصالح {country_ar}",
    "{en_nat} expatriates in {country}": "{males} مغتربون في {country_ar}",
    "{en_nat} emigrants to {country}": "{males} مهاجرون إلى {country_ar}",
}

countries_en_keys = [x.get("en") for x in all_country_with_nat.values() if x.get("en")]


def fix_keys(category: str) -> str:
    category = category.lower().replace("category:", "").replace("'", "")
    category = re.sub(r"\bthe\b", "", category)
    category = re.sub(r"\s+", " ", category)

    replacements = {
        # "expatriates": "expatriate",
    }

    for old, new in replacements.items():
        category = category.replace(old, new)

    return category.strip()


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBaseV2:
    countries_from_nat_data = countries_from_nat | COUNTRY_LABEL_OVERRIDES
    countries_data = {x: {"country_ar": v} for x, v in countries_from_nat_data.items()}
    nat_data = {x: v for x, v in All_Nat.items()}
    both_bot = format_multi_data_v2(
        formatted_data=COUNTRY_NAT_DATA,
        data_list=nat_data,
        key_placeholder="{en_nat}",
        data_list2=countries_data,
        key2_placeholder="{country}",
        text_after="",
        text_before="the ",
        regex_filter=r"[\w-]",
        search_first_part=True,
        use_other_formatted_data=True,
    )
    return both_bot


@functools.lru_cache(maxsize=10000)
def resolve_country_nat_pattern(category: str) -> str:
    logger.debug(f"<<yellow>> start resolve_country_nat_pattern: {category=}")

    normalized_category = fix_keys(category)

    if normalized_category in countries_en_as_nationality_keys or normalized_category in countries_en_keys:
        logger.info(f"<<yellow>> skip resolve_country_nat_pattern: {category=}, [result=]")
        return ""

    yc_bot = _load_bot()
    result = yc_bot.create_label(normalized_category)

    if result and category.lower().startswith("category:"):
        result = "تصنيف:" + result

    logger.info_if_or_debug(f"<<yellow>> end resolve_country_nat_pattern: {category=}, {result=}", result)

    return result or ""


__all__ = [
    "resolve_country_nat_pattern",
]
