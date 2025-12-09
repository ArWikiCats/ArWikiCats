#!/usr/bin/python3
"""

TODO: use this file to replace resolve_federation_label

"""
import functools
from ..translations_formats import format_multi_data_v2, MultiDataFormatterBaseV2
from ..translations.nats.Nationality import all_country_with_nat_ar
from ..translations.sports.Sport_key import SPORT_KEY_RECORDS

sports_formatted_data = {
    "{en_nat} {en_sport} federation": "الاتحاد {the_male} {sport_team}",
}


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBaseV2:
    nats_data = {
        x: {
            "country_ar": v["ar"],
            "the_male": v["the_male"],
        }
        for x, v in all_country_with_nat_ar.items()
        if v.get("ar") and v.get("en")
    }

    sports_data = {
        x: {
            "sport_ar": v["label"],
            "sport_team": v["team"],
        }
        for x, v in SPORT_KEY_RECORDS.items()
        if v.get("label")
    }

    both_bot = format_multi_data_v2(
        formatted_data=sports_formatted_data,
        data_list=nats_data,
        key_placeholder="{en_nat}",
        data_list2=sports_data,
        key2_placeholder="{en_sport}",
        text_after="",
        text_before="the ",
        search_first_part=True,
    )
    return both_bot


def resolve_nats_sport_multi_v2(category: str) -> str:
    normalized_category = category.lower().replace("category:", "")
    both_bot = _load_bot()

    result = both_bot.search_all(normalized_category)

    if result and category.lower().startswith("category:"):
        result = "تصنيف:" + result
    return result


__all__ = [
    "resolve_nats_sport_multi_v2",
]
