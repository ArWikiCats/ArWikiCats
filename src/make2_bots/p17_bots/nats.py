"""
from ..p17_bots import nats
"""

import re
from ...ma_lists import sport_formts_for_p17, nat_p17_oioi, match_sport_key
from ...ma_lists import Sports_Keys_For_Team
from ..matables_bots.bot import add_to_new_players, Add_to_main2_tab  # Add_to_main2_tab()
from ... import malists_sport_lab as sport_lab
from ...ma_lists import All_Nat, Nat_women
from ..jobs_bots.get_helps import get_con_3

from ...helps.log import logger

NAT_OTHERS_CACHE = {}


def make_sport_formats_p17(category_key: str) -> str:
    """Resolve a sport format label for P17 lookups."""

    logger.info(f'<<lightblue>>>>>> make_sport_formats_p17: category_key:"{category_key}"')

    cached_label = sport_formts_for_p17.get(category_key, "")
    if cached_label:
        logger.debug(f"\tfind lab in sport_formts_for_p17: {cached_label}")
        return cached_label

    resolved_label = ""
    # ---
    sport_key = match_sport_key(category_key)
    # ---
    if not sport_key:
        return ""

    sport_label = ""
    placeholder_template = ""

    placeholder_key = category_key.replace(sport_key, "oioioi")
    placeholder_key = re.sub(sport_key, "oioioi", placeholder_key, flags=re.IGNORECASE)
    logger.debug(
        f'make_sport_formats_p17 category_key:"{category_key}", '
        f'sport_key:"{sport_key}", placeholder_key:"{placeholder_key}"'
    )

    if placeholder_key in nat_p17_oioi:
        sport_label = Sports_Keys_For_Team.get(sport_key, "")
        if not sport_label:
            logger.debug(f' sport_key:"{sport_key}" not in Sports_Keys_For_Team ')
        placeholder_template = nat_p17_oioi[placeholder_key]
        if placeholder_template and sport_label:
            formatted_label = placeholder_template.replace("oioioi", sport_label)
            if "oioioi" not in formatted_label:
                resolved_label = formatted_label
                logger.debug(
                    f'make_sport_formats_p17 formatted_label:"{resolved_label}"'
                )
    else:
        logger.debug(
            f'make_sport_formats_p17 placeholder_key:"{placeholder_key}" not in nat_p17_oioi'
        )

    if resolved_label:
        logger.info(
            f'make_sport_formats_p17 category_key:"{category_key}", resolved_label:"{resolved_label}"'
        )

    return resolved_label


def find_nat_others(category: str, reference_category: str="") -> str:
    """Resolve fallback national labels for sport categories."""
    if category in NAT_OTHERS_CACHE:
        return NAT_OTHERS_CACHE[category]

    logger.info(f"<<lightblue>>>> vvvvvvvvvvvv find_nat_others category:{category} vvvvvvvvvvvv ")

    category_label = ""

    normalized_category = category.lower()

    sport_format_key, country_start = get_con_3(normalized_category, Nat_women, "nat")

    if sport_format_key and country_start:
        sport_format_label = sport_lab.Get_sport_formts_female_nat(sport_format_key)
        if sport_format_label:
            category_label = sport_format_label.format(nat=Nat_women[country_start])
            logger.debug(
                f'<<lightblue>>xxx sport_formts_female_nat: new category_label  "{category_label}"'
            )

    if sport_format_key and country_start and category_label == "":
        sport_format_label = make_sport_formats_p17(sport_format_key)
        country_label = All_Nat[country_start].get("ar", "")
        if sport_format_label and country_label:
            Add_to_main2_tab(sport_format_key, sport_format_label)

            category_label = sport_format_label.format(nat=country_label)
            Add_to_main2_tab(category_label, country_label)
            logger.debug(
                f'<<lightblue>>>>>> sport_formts_for_p17: new category_label  "{category_label}"'
            )
            add_to_new_players(category, category_label)

    logger.info("<<lightblue>>>> ^^^^^^^^^ find_nat_others end ^^^^^^^^^ ")

    NAT_OTHERS_CACHE[category] = category_label

    return category_label
