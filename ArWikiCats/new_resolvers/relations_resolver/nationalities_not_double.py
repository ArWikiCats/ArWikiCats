#!/usr/bin/python3
"""

input: `American remakes of Argentine films`
result: `أفلام أمريكية مأخوذة من أفلام أرجنتينية`

input: `Mexican television series based on non-Mexican television series`
result: `مسلسلات تلفزيونية مكسيكية مبنية على مسلسلات تلفزيونية غير مكسيكية`

input: `Non-Argentine television series based on Argentine television series`
result: `مسلسلات تلفزيونية غير أرجنتينية مبنية على مسلسلات تلفزيونية أرجنتينية`

"""

import functools

from ...helps import logger
from ...translations import All_Nat
from ...translations_formats import format_multi_data_v2
from ...translations_formats import MultiDataFormatterBaseV2

formatted_data_tv_or_films = {
    "{en_1} {tv_or_film} based on {en_2} {tv_or_film}": "{tv_or_film} {female_1} مبنية على {tv_or_film} {female_2}",
    # Bulgarian television series based on South Korean television series
    # "{en_1} films based on {en_2} films": "أفلام {female_1} مبنية على أفلام {female_2}",
    # "{en_1} television series based on {en_2} television series": "مسلسلات تلفزيونية {female_1} مبنية على مسلسلات تلفزيونية {female_2}",
    # Mexican television series based on non-Mexican television series
    # "{en_1} television series based on non-{en_2} television series": "مسلسلات تلفزيونية {female_1} مبنية على مسلسلات تلفزيونية غير {female_2}",
    # "{en_1} films based on non-{en_2} films": "أفلام {female_1} مبنية على أفلام غير {female_2}",
    "{en_1} {tv_or_film} based on non-{en_2} {tv_or_film}": "{tv_or_film} {female_1} مبنية على {tv_or_film} غير {female_2}",
    # Non-Argentine television series based on Argentine television series
    # "non-{en_1} television series based on {en_2} television series": "مسلسلات تلفزيونية غير {female_1} مبنية على مسلسلات تلفزيونية {female_2}",
    # "non-{en_1} films based on {en_2} films": "أفلام غير {female_1} مبنية على أفلام {female_2}",
    "non-{en_1} {tv_or_film} based on {en_2} {tv_or_film}": "{tv_or_film} غير {female_1} مبنية على {tv_or_film} {female_2}",
    # American remakes of Argentine films
    # "{en_1} remakes of {en_2} films": "أفلام {female_1} مأخوذة من أفلام {female_2}",
    # "{en_1} remakes of {en_2} television series": "مسلسلات تلفزيونية {female_1} مأخوذة من مسلسلات تلفزيونية {female_2}",
    "{en_1} remakes of {en_2} {tv_or_film}": "{tv_or_film} {female_1} مأخوذة من {tv_or_film} {female_2}",
}

formatted_data = {
    "television remakes of films": "مسلسلات تلفزيونية مأخوذة من أفلام",
}
for key, value in formatted_data_tv_or_films.items():
    formatted_data[key.replace("{tv_or_film}", "films")] = value.replace("{tv_or_film}", "أفلام")
    formatted_data[key.replace("{tv_or_film}", "television series")] = value.replace(
        "{tv_or_film}", "مسلسلات تلفزيونية"
    )

formatted_data.update({x.replace("based on", "basedon"): v for x, v in formatted_data.items() if "based on" in x})

formatted_data.update({x.replace("non-", "non "): v for x, v in formatted_data.items() if "non-" in x})

nats_data_1 = {x: {"female_1": v["female"]} for x, v in All_Nat.items()}
nats_data_2 = {x: {"female_2": v["female"]} for x, v in All_Nat.items()}


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBaseV2:
    _bot = format_multi_data_v2(
        formatted_data=formatted_data,
        data_list=nats_data_1,
        data_list2=nats_data_2,
        key_placeholder="{en_1}",
        key2_placeholder="{en_2}",
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


#


@functools.lru_cache(maxsize=10000)
def two_nationalities_but_not_double_resolver(category: str) -> str:
    category = fix_keys(category)
    logger.debug(f"<<yellow>> start two_nationalities_but_not_double_resolver: {category=}")

    # Handling special case: "television remakes of films"
    if category == "television remakes of films":
        return "مسلسلات تلفزيونية مأخوذة من أفلام"

    nat_bot = _load_bot()
    result = nat_bot.search_all_category(category)
    logger.info_if_or_debug(f"<<yellow>> end two_nationalities_but_not_double_resolver: {category=}, {result=}", result)
    return result


__all__ = [
    "two_nationalities_but_not_double_resolver",
]
