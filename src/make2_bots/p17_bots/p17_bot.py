"""

"""
import re
from ..jobs_bots.get_helps import get_con_3
from ..matables_bots.bot import All_P17, Add_to_main2_tab
from ..format_bots import Tit_ose_Nmaes, pop_format

from ...ma_lists import sport_formts_en_ar_is_p17
from ...ma_lists import en_is_P17_ar_is_mens, en_is_P17_ar_is_P17, en_is_P17_ar_is_al_women
from ...ma_lists import All_contry_with_nat_keys_is_en, contries_from_nat
from ... import malists_sport_lab as sport_lab

from ...helps.log import logger


def add_definite_article(label):
    label_without_article = re.sub(r" ", " ال", label)
    new_label = f"ال{label_without_article}"
    return new_label


def Get_P17_2(category):  # الإنجليزي اسم البلد والعربي جنسية رجال
    logger.info(
        f'<<lightblue>>>>>> Get_P17_2 "{category}" '
    )  # "united states government officials"

    # Category:United States government officials
    resolved_label = ""
    for suffix, template in en_is_P17_ar_is_mens.items():
        suffix_key = f" {suffix.strip().lower()}"
        if category.lower().endswith(suffix_key):
            country_prefix = category[: -len(suffix_key)].strip()

            mens_label = All_contry_with_nat_keys_is_en.get(country_prefix, {}).get(
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

                women_label = All_contry_with_nat_keys_is_en.get(country_prefix, {}).get(
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


def Get_P17(category):  # الإنجليزي جنسية والعربي اسم البلد
    resolved_label = ""
    con_3_lab = ""
    con_3 = ""
    contry_start = ""
    category = category.lower()
    contry_start_lab = ""
    con_3, contry_start = get_con_3(category, All_P17, "All_P17")
    contry_start_lab = All_P17.get(contry_start, "")

    if con_3 == "" and contry_start == "":
        con_3, contry_start = get_con_3(category, contries_from_nat, "contries_from_nat")
        contry_start_lab = contries_from_nat.get(contry_start, "")
    if con_3 and contry_start:
        logger.debug(f'<<lightpurple>>>>>> contry_start_lab:"{contry_start_lab}"')
        logger.debug(f'<<lightblue>> contry_start:"{contry_start}", con_3:"{con_3}"')

        FOF = ""
        if con_3 in Tit_ose_Nmaes:
            codd = Tit_ose_Nmaes[con_3]
            if codd.startswith("لل"):
                con_3_lab = "{} " + codd
                logger.debug(f'get lab from Tit_ose_Nmaes con_3_lab:"{con_3_lab}"')

        if not con_3_lab:
            con_3_lab = sport_formts_en_ar_is_p17.get(con_3.strip(), "")

        if not con_3_lab:
            con_3_lab = en_is_P17_ar_is_P17.get(con_3.strip(), "")

        if not con_3_lab:
            con_3_lab = sport_lab.Get_Sport_Format_xo_en_ar_is_P17(con_3.strip())

        if con_3_lab:
            FOF = "<<lightgreen>>sport_formts_en_ar_is_p17<<lightblue>>"
            Add_to_main2_tab(con_3, con_3_lab)

        if not con_3_lab:
            con_3_lab = pop_format.get(con_3, "")
            if con_3_lab:
                Add_to_main2_tab(con_3, con_3_lab)
                FOF = "<<lightgreen>>pop_format<<lightblue>>"

        if con_3_lab:
            logger.debug(
                f'<<lightblue>>>>>> {FOF} .startswith({contry_start}), con_3:"{con_3}"'
            )
            if con_3_lab.find("{nat}") != -1:
                resolved_label = con_3_lab.format(nat=contry_start_lab)
            else:
                resolved_label = con_3_lab.format(contry_start_lab)
            Add_to_main2_tab(contry_start, contry_start_lab)

        if con_3_lab and resolved_label == "":
            resolved_label = con_3_lab.format(contry_start_lab)
            Add_to_main2_tab(contry_start, contry_start_lab)
        if con_3_lab:
            logger.debug(
                f'<<lightblue>>>>>> Get_P17: test_60: new cnt_la "{resolved_label}" '
            )
        logger.debug(
            f'<<lightred>>>>>> con_3_lab: "{con_3_lab}", cnt_la :"{resolved_label}" == ""'
        )

    else:
        logger.info(f'<<lightred>>>>>> con_3: "{con_3}" or contry_start :"{contry_start}" == ""')

    if resolved_label:
        logger.info(f'<<lightblue>>>>>> Get_P17 cnt_la "{resolved_label}" ')

    return resolved_label
