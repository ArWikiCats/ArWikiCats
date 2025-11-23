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
from ..utils.match_sport_keys import match_sport_key

format_labels_with_nat = {
    "natar national xoxo teams": "منتخبات xoxo وطنية natar",
    "natar xoxo championshipszz": "بطولة natar xoxo",
    "natar xoxo championships": "بطولة natar xoxo",
    "ladies natar xoxo championships": "بطولة natar xoxo للسيدات",
    "natar xoxo tour": "بطولة natar xoxo",
    "women's natar xoxo tour": "بطولة natar xoxo للسيدات",
    "ladies natar xoxo tour": "بطولة natar xoxo للسيدات",
}

nat_bot = FormatData(format_labels_with_nat, en_nats_to_ar_label, key_placeholder="natar", value_placeholder="natar")


@dump_data(enable=1)
def normalize_nat_and_sport(normalized_team: str) -> str:
    """
    Match sports labels using the newer placeholder-based approach.

    input: "british xoxo championshipszz", output: "بطولة المملكة المتحدة xoxo"
    """
    template_label = ""

    nationality_key = match_nat_key(normalized_team.strip())
    if not nationality_key:
        logger.debug("nationality_key not found")
        return ""

    logger.debug(f"{nationality_key=}")
    logger.debug(f'nationality_key:"{str(nationality_key)}"')

    template_label = nat_bot.get_template(nationality_key, normalized_team)

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

    template_label = normalize_nat_and_sport(normalized_team)

    sport_label = SPORTS_KEYS_FOR_TEAM.get(sport_key, "")

    if template_label and sport_label:
        team_lab = apply_pattern_replacement(template_label, sport_label, "xoxo")

    return team_lab


def compare_to_create_label(team: str) -> str:
    """Resolve modern team labels using nationality and template data."""
    sport_key = match_sport_key(team)

    if not sport_key:
        print(f"compare_to_create_label(): no sport key in: {team=} ")
        return ""

    normalized_team = re.sub(f" {sport_key} ", " xoxo ", f" {team.strip()} ", flags=re.IGNORECASE).strip()
    logger.info(f'Get_Sport Get_New_team_xo P17: team:"{team}", sport_key:"{sport_key}", team_xo:"{normalized_team}"')

    team_lab = Get_New_team_xo_with_nat(normalized_team, sport_key)

    return team_lab


__all__ = [
    "normalize_nat_and_sport",
    "compare_to_create_label",
]
