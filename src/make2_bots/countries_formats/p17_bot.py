""" """

from ...helps.log import logger
from ...translations import (
    SPORT_FORMTS_EN_AR_IS_P17,
    Get_Sport_Format_xo_en_ar_is_P17,
    contries_from_nat,
    en_is_P17_ar_is_P17,
)
from ..format_bots import category_relation_mapping, pop_format
from ..jobs_bots.get_helps import get_suffix_with_keys
from ..matables_bots.bot import All_P17

def Get_P17(category: str) -> str:  # الإنجليزي جنسية والعربي اسم البلد
    """
    Category input in english is nationality, return arabic as country name.

    Resolve categories that start with nationality adjectives into country labels.

    TODO: use FormatData method
    """
    resolved_label = ""
    con_3_lab = ""
    country_start_lab = ""
    category = category.lower()

    suffix, country_start = get_suffix_with_keys(category, All_P17)
    country_start_lab = All_P17.get(country_start, "")

    if not suffix and not country_start:
        suffix, country_start = get_suffix_with_keys(category, contries_from_nat)
        country_start_lab = contries_from_nat.get(country_start, "")

    if suffix and country_start:
        logger.debug(f'<<lightpurple>>>>>> country_start_lab:"{country_start_lab}"')
        logger.debug(f'<<lightblue>> country_start:"{country_start}", suffix:"{suffix}"')

        FOF = ""
        if suffix in category_relation_mapping:
            codd = category_relation_mapping[suffix]
            if codd.startswith("لل"):
                con_3_lab = "{} " + codd
                logger.debug(f'get lab from category_relation_mapping con_3_lab:"{con_3_lab}"')

        if not con_3_lab:
            con_3_lab = SPORT_FORMTS_EN_AR_IS_P17.get(suffix.strip(), "")
            if con_3_lab:
                FOF = "<<lightgreen>>SPORT_FORMTS_EN_AR_IS_P17<<lightblue>>"

        if not con_3_lab:
            con_3_lab = en_is_P17_ar_is_P17.get(suffix.strip(), "")

        if not con_3_lab:
            con_3_lab = Get_Sport_Format_xo_en_ar_is_P17(suffix.strip())

        if not con_3_lab:
            con_3_lab = pop_format.get(suffix, "")
            if con_3_lab:
                FOF = "<<lightgreen>>pop_format<<lightblue>>"

        if con_3_lab:
            if FOF:
                logger.debug(f'<<lightblue>>>>>> {FOF} .startswith({country_start}), suffix:"{suffix}"')
            if "{nat}" in con_3_lab:
                resolved_label = con_3_lab.format(nat=country_start_lab)
            else:
                resolved_label = con_3_lab.format(country_start_lab)

            logger.debug(f'<<lightblue>>>>>> Get_P17: test_60: new cnt_la "{resolved_label}" ')

        logger.debug(f'<<lightred>>>>>> con_3_lab: "{con_3_lab}", cnt_la :"{resolved_label}" == ""')

    else:
        logger.info(f'<<lightred>>>>>> suffix: "{suffix}" or country_start :"{country_start}" == ""')

    if resolved_label:
        logger.info(f'<<lightblue>>>>>> Get_P17 cnt_la "{resolved_label}" ')

    return resolved_label


__all__ = [
    "Get_P17",
]
