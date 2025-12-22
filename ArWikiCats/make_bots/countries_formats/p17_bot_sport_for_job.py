"""
TODO: merge with translations_resolvers OR translations_resolvers_v2
"""
import functools
import re
from ...helps import dump_data, logger
from ...translations import (
    countries_from_nat,
    SPORTS_KEYS_FOR_JOBS,
    match_sport_key,
    apply_pattern_replacements,
)

from ..jobs_bots.get_helps import get_suffix_with_keys


sport_formts_enar_p17_jobs = {
    "international men's xoxo players": "لاعبو xoxo دوليون من {}",
    "international women's xoxo players": "لاعبات xoxo دوليات من {}",
    "international xoxo players": "لاعبو xoxo دوليون من {}",
    "men's international xoxo players": "لاعبو xoxo دوليون من {}",
    "olympics xoxo": "xoxo {} في الألعاب الأولمبية",
    "summer olympics xoxo": "xoxo {} في الألعاب الأولمبية الصيفية",
    "under-13 international xoxo managers": "مدربو xoxo تحت 13 سنة دوليون من {}",
    "under-13 international xoxo players": "لاعبو xoxo تحت 13 سنة دوليون من {}",
    "under-14 international xoxo managers": "مدربو xoxo تحت 14 سنة دوليون من {}",
    "under-14 international xoxo players": "لاعبو xoxo تحت 14 سنة دوليون من {}",
    "under-15 international xoxo managers": "مدربو xoxo تحت 15 سنة دوليون من {}",
    "under-15 international xoxo players": "لاعبو xoxo تحت 15 سنة دوليون من {}",
    "under-16 international xoxo managers": "مدربو xoxo تحت 16 سنة دوليون من {}",
    "under-16 international xoxo players": "لاعبو xoxo تحت 16 سنة دوليون من {}",
    "under-17 international xoxo managers": "مدربو xoxo تحت 17 سنة دوليون من {}",
    "under-17 international xoxo players": "لاعبو xoxo تحت 17 سنة دوليون من {}",
    "under-18 international xoxo managers": "مدربو xoxo تحت 18 سنة دوليون من {}",
    "under-18 international xoxo players": "لاعبو xoxo تحت 18 سنة دوليون من {}",
    "under-19 international xoxo managers": "مدربو xoxo تحت 19 سنة دوليون من {}",
    "under-19 international xoxo players": "لاعبو xoxo تحت 19 سنة دوليون من {}",
    "under-20 international xoxo managers": "مدربو xoxo تحت 20 سنة دوليون من {}",
    "under-20 international xoxo players": "لاعبو xoxo تحت 20 سنة دوليون من {}",
    "under-21 international xoxo managers": "مدربو xoxo تحت 21 سنة دوليون من {}",
    "under-21 international xoxo players": "لاعبو xoxo تحت 21 سنة دوليون من {}",
    "under-23 international xoxo managers": "مدربو xoxo تحت 23 سنة دوليون من {}",
    "under-23 international xoxo players": "لاعبو xoxo تحت 23 سنة دوليون من {}",
    "under-24 international xoxo managers": "مدربو xoxo تحت 24 سنة دوليون من {}",
    "under-24 international xoxo players": "لاعبو xoxo تحت 24 سنة دوليون من {}",
    "winter olympics xoxo": "xoxo {} في الألعاب الأولمبية الشتوية",
    "women's international xoxo players": "لاعبات xoxo دوليات من {}",
    "xoxo manager history": "تاريخ مدربو xoxo {}"
}


def get_sport_formts_enar_p17_jobs(suffix: str) -> str:
    """
    Return a sport label that merges templates with Arabic sport names.

    Example:
        suffix: "winter olympics softball", return: "كرة لينة {} في الألعاب الأولمبية الشتوية"
    """
    sport_key = match_sport_key(suffix)
    if not sport_key:
        return ""

    sport_label = ""

    template_label = ""
    normalized_key = suffix.replace(sport_key, "xoxo")
    normalized_key = re.sub(sport_key, "xoxo", normalized_key, flags=re.IGNORECASE)

    logger.info(f'Get_SFxo_en_ar_is P17: {suffix=}, {sport_key=}, team_xoxo:"{normalized_key}"')

    if normalized_key in sport_formts_enar_p17_jobs:
        sport_label = SPORTS_KEYS_FOR_JOBS.get(sport_key, "")
        template_label = sport_formts_enar_p17_jobs.get(normalized_key, "")

    else:
        logger.info(
            f'Get_SFxo_en_ar_is P17 team_xoxo:"{normalized_key}" not in sport_formts_enar_p17_jobs'
        )

    con_3_label = ""

    if template_label and sport_label:
        con_3_label = apply_pattern_replacements(template_label, sport_label, "xoxo")
        logger.info(f'Get_SFxo_en_ar_is P17 blab:"{con_3_label}"')
    else:
        logger.info(f'Get_SFxo_en_ar_is P17 team_xoxo:"{normalized_key}" not in sport_formts_enar_p17_jobs')

    logger.info(f'Get_SFxo_en_ar_is P17 {suffix=}, {con_3_label=}')

    return con_3_label


@functools.lru_cache(maxsize=10000)
@dump_data(1)
def get_p17_with_sport_jobs(category: str) -> str:
    """
    TODO: use FormatData method
    """
    resolved_label = ""
    category = category.lower()

    suffix, country_start = get_suffix_with_keys(category, countries_from_nat)
    country_start_lab = countries_from_nat.get(country_start, "")

    if not suffix or not country_start:
        logger.info(f'<<lightred>>>>>> {suffix=} or {country_start=} == ""')
        return ""

    logger.debug(f'<<lightblue>> {country_start=}, {suffix=}')
    logger.debug(f'<<lightpurple>>>>>> {country_start_lab=}')

    suffix_label = get_sport_formts_enar_p17_jobs(suffix.strip())

    if not suffix_label:
        logger.debug(f'<<lightred>>>>>> {suffix_label=}, resolved_label == ""')
        return ""

    if "{nat}" in suffix_label:
        resolved_label = suffix_label.format(nat=country_start_lab)
    else:
        resolved_label = suffix_label.format(country_start_lab)

    logger.debug(f'<<lightblue>>>>>> Get_P17_with_p17_sport: test_60: new cnt_la "{resolved_label}" ')

    return resolved_label


__all__ = [
    "get_p17_with_sport_jobs",
]
