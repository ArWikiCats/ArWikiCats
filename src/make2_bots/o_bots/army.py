"""
from ..o_bots.army import test_Army
"""

import re

from ...ma_lists import All_contry_with_nat, All_contry_with_nat_keys_is_en
from ...ma_lists import sport_formts_en_p17_ar_nat

from ...ma_lists import (
    military_format_women_without_al_from_end,
    military_format_women_without_al,
    military_format_women,
    military_format_men,
)

from ...helps.log import logger

TEST_ARMY_CACHE = {}

def test_Army(category):
    if category in TEST_ARMY_CACHE:
        if TEST_ARMY_CACHE[category]:
            logger.debug(
                f"<<lightblue>>>> ============== test_Army_Cash : {TEST_ARMY_CACHE[category]}"
            )
        return TEST_ARMY_CACHE[category]

    category = category.lower()
    category_suffix = ""
    resolved_label = ""
    women_label = ""
    men_label = ""

    logger.info(
        f"<<lightblue>>>> vvvvvvvvvvvv test_Army start, (category:{category}) vvvvvvvvvvvv "
    )

    for country, country_details in All_contry_with_nat.items():
        if resolved_label:
            break
        # ---
        english_country = country_details.get("en", "")
        women_labels = country_details.get("women", "")
        men_labels = country_details.get("men", "")

        if english_country:
            english_country = f"{english_country.lower()} "

        english_country_suffix = f" {english_country.lower()}"

        localized_country = f"{country.lower()} "

        country_without_article = english_country
        if country_without_article.startswith("the "):
            country_without_article = country_without_article[len("the ") :].strip()

        if category.endswith(english_country_suffix):
            print("cate.endswith(contry2_end)")

        if women_labels == "" and men_labels == "":
            logger.debug('women_labs and men_labs == ""')
            continue

        if (
            category.startswith(english_country)
            or category.startswith(country_without_article)
            or category.startswith(localized_country)
        ):
            women_label = women_labels
            men_label = men_labels

            matched_prefix = ""
            if category.startswith(english_country):
                category_suffix = category[len(english_country) :].strip()
                matched_prefix = english_country

            elif category.startswith(country_without_article):
                category_suffix = category[len(country_without_article) :].strip()
                matched_prefix = country_without_article

            elif category.startswith(localized_country):
                category_suffix = category[len(localized_country) :].strip()
                matched_prefix = localized_country

            logger.debug(
                f'<<lightblue>>>>>> get startswith All_contry_with_nat ({matched_prefix}), '
                f'category_suffix:"{category_suffix}"'
            )
            break

    if not resolved_label:
        # 16-11-2020
        # Category:Unmanned_aerial_vehicles_of_Jordan > طائرات بدون طيار أردنية
        for prefix_without_article, prefix_label in military_format_women_without_al_from_end.items():
            prefix_with_space = f"{prefix_without_article} "
            if not category.startswith(prefix_with_space):
                continue
            # ---
            suffix_key = category[len(prefix_with_space) :].strip()
            country_label = All_contry_with_nat_keys_is_en.get(suffix_key, {}).get(
                "women", ""
            )
            if country_label:
                logger.debug(f'<<lightblue>>>>>> con_labe: "{country_label}" ')
                resolved_label = prefix_label.format(nat=country_label)
                logger.debug(
                    f'<<lightblue>>>>>> con_77_from_end: new resolved_label  "{resolved_label}" '
                )

    if not resolved_label:
        category_suffix_label = military_format_women_without_al.get(category_suffix, "")
        if category_suffix_label:
            # FOF = "<<lightgreen>>military_format_women_without_al<<lightblue>> "
            logger.debug('<<lightblue>>>>>> women_lab: "{women_label}" ')

            resolved_label = category_suffix_label.format(nat=women_label)
            logger.debug(
                f'<<lightblue>>>>>> test_880: new resolved_label  "{resolved_label}" '
            )

    extended_suffix = category_suffix
    suffix_prefix_template = ""  # بادئة
    suffix_label = ""

    if not resolved_label:
        endswith_table = {
            " civilians": "مدنيو {}",
            " generals": "جنرالات {}",
            " accidents and incidents": "حوادث {}",
        }
        for suffix, suffix_template in endswith_table.items():
            if not extended_suffix.endswith(suffix):
                continue
            if resolved_label:
                break
            extended_suffix = extended_suffix.replace(suffix, "", 1)
            suffix_prefix_template = suffix_template
            suffix_label = military_format_women.get(extended_suffix, "")

            if suffix_label:
                # FOF = "<<lightgreen>>military_format_women<<lightblue>> "
                logger.debug(f'<<lightblue>>>>>> women_lab: "{women_label}" ')
                women_label_no_article = re.sub(r" ", " ال", women_label)
                women_label = f"ال{women_label_no_article}"
                resolved_label = suffix_label.format(nat=women_label)
                logger.debug(
                    f'<<lightblue>>>>>> test_880: new resolved_label  "{resolved_label}" '
                )
                resolved_label = suffix_prefix_template.format(resolved_label)
            # ---

    # military_format_men :
    # Category:French_labour_law
    if not resolved_label:  #
        category_suffix_label = military_format_men.get(category_suffix, "")
        if category_suffix_label and men_label:
            # FOF = "<<lightgreen>>military_format_men<<lightblue>>"
            men_label_no_article = re.sub(r" ", " ال", men_label)
            men_label = f"ال{men_label_no_article}"
            resolved_label = category_suffix_label.format(nat=men_label)
            logger.debug(
                f'<<lightblue>>>>>> test_880: new resolved_label  "{resolved_label}" '
            )

    # sport_formts_en_p17_ar_nat :
    # Category:China Basketball Federation
    if not resolved_label:  #
        category_suffix_label = sport_formts_en_p17_ar_nat.get(category_suffix, "")
        if category_suffix_label and men_label:
            # FOF = "<<lightgreen>>sport_formts_en_p17_ar_nat<<lightblue>>"
            men_label_no_article = re.sub(r" ", " ال", men_label)
            men_label = f"ال{men_label_no_article}"
            resolved_label = category_suffix_label.format(nat=men_label)
            logger.debug(
                f'<<lightblue>>>>>> test_880: new resolved_label  "{resolved_label}" '
            )

    if resolved_label:
        TEST_ARMY_CACHE[category] = resolved_label

    logger.info("<<lightblue>>>> ^^^^^^^^^ test_Army end ^^^^^^^^^ ")
    return resolved_label
