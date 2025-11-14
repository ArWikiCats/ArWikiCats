#!/usr/bin/python3
"""


"""

import re
from ..utils.match_nats_keys import match_nat_key
from ..sports.Sport_key import SPORTS_KEYS_FOR_TEAM
from ..nats.Nationality import all_country_with_nat_ar
from ...helps.print_bot import output_test
from ..utils import apply_pattern_replacement
from ...helps.log import logger
from ...ma_lists_formats.format_data import FormatData

format_labels_with_nat = {
    "natar national xoxo teams": "منتخبات xoxo وطنية natar",
    "natar xoxo championships": "بطولة natar xoxo",
    "ladies natar xoxo championships": "بطولة natar xoxo للسيدات",
    "natar xoxo tour": "بطولة natar xoxo",
    "women's natar xoxo tour": "بطولة natar xoxo للسيدات",
    "ladies natar xoxo tour": "بطولة natar xoxo للسيدات",
}


def get_template_label_new(key, key_placeholder, normalized_team, data):

    bot = FormatData(data, {}, key_placeholder=key_placeholder, value_placeholder="")

    return bot.get_template(key, normalized_team)


def get_template_label(key, key_placeholder, normalized_team, data):
    # ---
    normalized_key = re.sub(rf"\b{key}\b", key_placeholder, f" {normalized_team.strip()} ", flags=re.IGNORECASE)
    # ---
    logger.debug(f"{normalized_key=}")
    # ---
    template_label = data.get(normalized_key.strip(), "")
    # ---
    return template_label


def match_sports_labels_with_nat(normalized_team: str, sport_key: str) -> str:
    template_label, sport_label = "", ""
    # ---
    nationality_key = match_nat_key(normalized_team.strip())
    sport_label = SPORTS_KEYS_FOR_TEAM.get(sport_key, "")
    # ---
    if not nationality_key:
        logger.debug("nationality_key not found")
        return template_label, sport_label
    # ---
    logger.debug(f"{nationality_key=}")
    # ---
    output_test(f'nationality_key:"{str(nationality_key)}"')
    # ---
    normalized_nat_key = re.sub(
        f" {nationality_key} ", " natar ", f" {normalized_team.strip()} ", flags=re.IGNORECASE
    )
    # ---
    logger.debug(f"{normalized_nat_key=}")
    # ---
    template_label = format_labels_with_nat.get(normalized_nat_key.strip(), "")
    # ---
    nationality_label = all_country_with_nat_ar.get(nationality_key, {}).get("ar", "")
    output_test(f'nat_lab:"{nationality_label}"')
    # ---
    if template_label and nationality_label:
        template_label = template_label.replace("natar", nationality_label)
    # ---
    logger.debug(f"{template_label=}, {sport_label=}")
    # ---
    return template_label, sport_label


def match_sports_labels_with_nat_new(normalized_team: str, sport_key: str) -> str:
    template_label, sport_label = "", ""
    # ---
    nationality_key = match_nat_key(normalized_team.strip())
    # ---
    sport_label = SPORTS_KEYS_FOR_TEAM.get(sport_key, "")
    # ---
    if not nationality_key:
        logger.debug("nationality_key not found")
        return template_label, sport_label
    # ---
    logger.debug(f"{nationality_key=}")
    # ---
    output_test(f'nationality_key:"{str(nationality_key)}"')
    # ---
    template_label = get_template_label(nationality_key, "natar", normalized_team, format_labels_with_nat)
    # ---
    nationality_label = all_country_with_nat_ar.get(nationality_key, {}).get("ar", "")
    # ---
    if template_label and nationality_label:
        template_label = template_label.replace("natar", nationality_label)
    # ---
    logger.debug(f"{template_label=}, {sport_label=}")
    # ---
    return template_label, sport_label


def Get_New_team_xo_with_nat(normalized_team: str, sport_key: str) -> str:
    team_lab = ""
    # ---
    template_label, sport_label = match_sports_labels_with_nat(normalized_team, sport_key)
    # ---
    if template_label and sport_label:
        team_lab = apply_pattern_replacement(template_label, sport_label, "xoxo")
    # ---
    return team_lab


__all__ = [
    "get_template_label",
    "match_sports_labels_with_nat",
    "match_sports_labels_with_nat_new",
    "Get_New_team_xo_with_nat",
]
