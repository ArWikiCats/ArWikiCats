#!/usr/bin/python3
""" """

import re

from ...helps.log import logger
from ...translations_formats.format_data import FormatData
from ..nats.Nationality import en_nats_to_ar_label
from ..sports.Sport_key import SPORTS_KEYS_FOR_TEAM
from ..utils import apply_pattern_replacement
from ..utils.match_nats_keys import match_nat_key

format_labels_with_nat = {
    "natar national xoxo teams": "منتخبات xoxo وطنية natar",
    "natar xoxo championships": "بطولة natar xoxo",
    "ladies natar xoxo championships": "بطولة natar xoxo للسيدات",
    "natar xoxo tour": "بطولة natar xoxo",
    "women's natar xoxo tour": "بطولة natar xoxo للسيدات",
    "ladies natar xoxo tour": "بطولة natar xoxo للسيدات",
}


def normalize_category(category):
    bot = FormatData(format_labels_with_nat, en_nats_to_ar_label, key_placeholder="natar", value_placeholder="natar")
    key = bot.match_key(category)
    result = ""
    if key:
        result = bot.normalize_category(category, key)
    return result


def get_template_label(key, key_placeholder, normalized_team, data):
    normalized_key = re.sub(rf"\b{key}\b", key_placeholder, f" {normalized_team.strip()} ", flags=re.IGNORECASE)
    logger.debug(f"{normalized_key=}")
    template_label = data.get(normalized_key.strip(), "")
    return template_label


def match_sports_labels_with_nat(normalized_team: str) -> str:
    template_label = ""
    nationality_key = match_nat_key(normalized_team.strip())
    if not nationality_key:
        logger.debug("nationality_key not found")
        return template_label
    logger.debug(f"{nationality_key=}")
    logger.debug(f'nationality_key:"{str(nationality_key)}"')
    normalized_nat_key = re.sub(f" {nationality_key} ", " natar ", f" {normalized_team.strip()} ", flags=re.IGNORECASE)
    logger.debug(f"{normalized_nat_key=}")
    template_label = format_labels_with_nat.get(normalized_nat_key.strip(), "")
    nationality_label = en_nats_to_ar_label.get(nationality_key.lower(), "")
    logger.debug(f'nat_lab:"{nationality_label}"')
    if template_label and nationality_label:
        template_label = template_label.replace("natar", nationality_label)
    logger.debug(f"{template_label=}, {nationality_label=}, {nationality_key=}")
    if "natar" in template_label:
        return ""
    return template_label


def match_sports_labels_with_nat_new(normalized_team: str) -> str:
    template_label = ""
    nationality_key = match_nat_key(normalized_team.strip())
    if not nationality_key:
        logger.debug("nationality_key not found")
        return ""
    logger.debug(f"{nationality_key=}")
    logger.debug(f'nationality_key:"{str(nationality_key)}"')
    template_label = get_template_label(nationality_key, "natar", normalized_team, format_labels_with_nat)
    nationality_label = en_nats_to_ar_label.get(nationality_key.lower(), "")
    if template_label and nationality_label:
        template_label = template_label.replace("natar", nationality_label)
    logger.debug(f"{template_label=}, {nationality_label=}, {nationality_key=}")
    if "natar" in template_label:
        return ""
    return template_label


def Get_New_team_xo_with_nat(normalized_team: str, sport_key: str) -> str:
    team_lab = ""
    sport_label = SPORTS_KEYS_FOR_TEAM.get(sport_key, "")
    template_label = match_sports_labels_with_nat(normalized_team)
    if template_label and sport_label:
        team_lab = apply_pattern_replacement(template_label, sport_label, "xoxo")
    return team_lab


__all__ = [
    "get_template_label",
    "match_sports_labels_with_nat",
    "match_sports_labels_with_nat_new",
    "Get_New_team_xo_with_nat",
]
