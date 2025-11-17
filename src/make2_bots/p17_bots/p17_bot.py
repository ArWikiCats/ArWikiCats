"""

"""
import re
from ..jobs_bots.get_helps import get_con_3
from ..matables_bots.bot import All_P17
from ..format_bots import category_relation_mapping, pop_format

from ...translations import SPORT_FORMTS_EN_AR_IS_P17, Get_Sport_Format_xo_en_ar_is_P17
from ...translations import en_is_P17_ar_is_mens, en_is_P17_ar_is_P17, en_is_P17_ar_is_al_women
from ...translations import all_country_with_nat_keys_is_en, contries_from_nat

from ...helps.log import logger


def add_definite_article(label: str) -> str:
    label_without_article = re.sub(r" ", " ال", label)
    new_label = f"ال{label_without_article}"
    return new_label


def Get_P17_2(category: str) -> str:  # الإنجليزي اسم البلد والعربي جنسية رجال
    logger.info(
        f'<<lightblue>>>>>> Get_P17_2 "{category}" '
    )  # "united states government officials"

    # Category:United States government officials
    resolved_label = ""
    for suffix, template in en_is_P17_ar_is_mens.items():
        suffix_key = f" {suffix.strip().lower()}"
        if category.lower().endswith(suffix_key):
            country_prefix = category[: -len(suffix_key)].strip()

            mens_label = all_country_with_nat_keys_is_en.get(country_prefix, {}).get(
                "mens", ""
            )
            if mens_label:
                logger.debug(f'<<lightblue>>>>>> mens: "{mens_label}" ')
                resolved_label = template.format(mens_label)
                logger.debug(
                    f'<<lightblue>>>>>> en_is_P17_ar_is_mens: new cnt_la  "{resolved_label}" '
                )
    # ---
    if not resolved_label:
        for suffix, template in en_is_P17_ar_is_al_women.items():
            suffix_key = f" {suffix.strip().lower()}"
            if category.lower().endswith(suffix_key):
                country_prefix = category[: -len(suffix_key)].strip()

                women_label = all_country_with_nat_keys_is_en.get(country_prefix, {}).get(
                    "women", ""
                )
                if women_label:
                    women_label = add_definite_article(women_label)
                    logger.debug(f'<<lightblue>>>>>> women: "{women_label}" ')
                    resolved_label = template.format(women_label)
                    logger.debug(
                        f'<<lightblue>>>>>> en_is_P17_ar_is_al_women: new cnt_la  "{resolved_label}" '
                    )

    return resolved_label


def Get_P17(category: str) -> str:  # الإنجليزي جنسية والعربي اسم البلد
    resolved_label = ""
    con_3_lab = ""
    con_3 = ""
    country_start = ""
    category = category.lower()
    country_start_lab = ""
    con_3, country_start = get_con_3(category, "All_P17")
    country_start_lab = All_P17.get(country_start, "")

    if con_3 == "" and country_start == "":
        con_3, country_start = get_con_3(category, "contries_from_nat")
        country_start_lab = contries_from_nat.get(country_start, "")
    if con_3 and country_start:
        logger.debug(f'<<lightpurple>>>>>> country_start_lab:"{country_start_lab}"')
        logger.debug(f'<<lightblue>> country_start:"{country_start}", con_3:"{con_3}"')

        FOF = ""
        if con_3 in category_relation_mapping:
            codd = category_relation_mapping[con_3]
            if codd.startswith("لل"):
                con_3_lab = "{} " + codd
                logger.debug(f'get lab from category_relation_mapping con_3_lab:"{con_3_lab}"')

        if not con_3_lab:
            con_3_lab = SPORT_FORMTS_EN_AR_IS_P17.get(con_3.strip(), "")

        if not con_3_lab:
            con_3_lab = en_is_P17_ar_is_P17.get(con_3.strip(), "")

        if not con_3_lab:
            con_3_lab = Get_Sport_Format_xo_en_ar_is_P17(con_3.strip())

        if con_3_lab:
            FOF = "<<lightgreen>>SPORT_FORMTS_EN_AR_IS_P17<<lightblue>>"

        if not con_3_lab:
            con_3_lab = pop_format.get(con_3, "")
            if con_3_lab:
                FOF = "<<lightgreen>>pop_format<<lightblue>>"

        if con_3_lab:
            logger.debug(
                f'<<lightblue>>>>>> {FOF} .startswith({country_start}), con_3:"{con_3}"'
            )
            if "{nat}" in con_3_lab:
                resolved_label = con_3_lab.format(nat=country_start_lab)
            else:
                resolved_label = con_3_lab.format(country_start_lab)

        if con_3_lab and resolved_label == "":
            resolved_label = con_3_lab.format(country_start_lab)
        if con_3_lab:
            logger.debug(
                f'<<lightblue>>>>>> Get_P17: test_60: new cnt_la "{resolved_label}" '
            )
        logger.debug(
            f'<<lightred>>>>>> con_3_lab: "{con_3_lab}", cnt_la :"{resolved_label}" == ""'
        )

    else:
        logger.info(f'<<lightred>>>>>> con_3: "{con_3}" or country_start :"{country_start}" == ""')

    if resolved_label:
        logger.info(f'<<lightblue>>>>>> Get_P17 cnt_la "{resolved_label}" ')

    return resolved_label
