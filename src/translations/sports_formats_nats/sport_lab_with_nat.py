#!/usr/bin/python3
""" """

import re

from ...helps.jsonl_dump import dump_data
from ...helps.log import logger
from ..nats.Nationality import en_nats_to_ar_label
from ..sports.Sport_key import SPORTS_KEYS_FOR_TEAM
from ..utils import apply_pattern_replacement
from ..utils.match_nats_keys import match_nat_key
from ...translations_formats.format_data import FormatData

format_labels_with_nat = {
    "natar national xoxo teams": "منتخبات xoxo وطنية natar",
    "natar xoxo championships": "بطولة natar xoxo",
    "ladies natar xoxo championships": "بطولة natar xoxo للسيدات",
    "natar xoxo tour": "بطولة natar xoxo",
    "women's natar xoxo tour": "بطولة natar xoxo للسيدات",
    "ladies natar xoxo tour": "بطولة natar xoxo للسيدات",
}


nat_bot = FormatData(format_labels_with_nat, en_nats_to_ar_label, key_placeholder="natar", value_placeholder="natar")


def get_template_label(key: str, key_placeholder: str, normalized_team: str, data: dict) -> str:
    return nat_bot.get_template(key, normalized_team)


@dump_data(enable=1)
def match_sports_labels_with_nat(normalized_team: str) -> str:
    """Match sports labels using the newer placeholder-based approach."""
    template_label = ""

    nationality_key = match_nat_key(normalized_team.strip())
    if not nationality_key:
        logger.debug("nationality_key not found")
        return ""

    logger.debug(f"{nationality_key=}")
    logger.debug(f'nationality_key:"{str(nationality_key)}"')

    template_label = get_template_label(nationality_key, "natar", normalized_team, format_labels_with_nat)

    nationality_label = en_nats_to_ar_label.get(nationality_key.lower(), "")
    logger.debug(f'nat_lab:"{nationality_label}"')

    if template_label and nationality_label:
        template_label = template_label.replace("natar", nationality_label)

    logger.debug(f"{template_label=}, {nationality_label=}, {nationality_key=}")

    if "natar" in template_label:
        return ""

    return template_label


@dump_data(enable=True)
def Get_New_team_xo_with_nat(normalized_team: str, sport_key: str) -> str:
    """Construct a team label that merges sport and nationality templates."""
    team_lab = ""

    template_label = match_sports_labels_with_nat(normalized_team)

    sport_label = SPORTS_KEYS_FOR_TEAM.get(sport_key, "")

    if template_label and sport_label:
        team_lab = apply_pattern_replacement(template_label, sport_label, "xoxo")

    return team_lab


__all__ = [
    "match_sports_labels_with_nat",
]
