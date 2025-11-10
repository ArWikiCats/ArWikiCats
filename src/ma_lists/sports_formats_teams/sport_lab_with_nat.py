#!/usr/bin/python3
"""


"""

import re
from .te3 import New_team_xo_team_labels
from ..utils.match_nats_keys import match_nat_key
from ..sports.Sport_key import Sports_Keys_For_Team
from ..nats.Nationality import All_contry_with_nat_ar
from ...helps.print_bot import output_test


def apply_pattern_replacement(template_label, sport_label, xoxo):
    # ---
    team_lab = ""
    # ---
    final_label = template_label.replace(xoxo, sport_label)
    if final_label.find(xoxo) == -1:
        team_lab = final_label
    # ---
    return team_lab


def get_template_label(key, key_placeholder, normalized_team, data):
    # ---
    template_label = ""
    # ---
    normalized_key = re.sub(f"\b{key}\b", key_placeholder, f" {normalized_team.strip()} ", flags=re.IGNORECASE)
    # ---
    template_label = data.get(normalized_key.strip(), "")
    # ---
    return template_label


def match_nat_new_team_xo_team_labels(normalized_team: str, sport_key: str) -> str:
    template_label, sport_label = "", ""
    # ---
    nationality_key = match_nat_key(normalized_team.strip())
    # ---
    if not nationality_key:
        return template_label, sport_label
    # ---
    output_test(f'nationality_key:"{str(nationality_key)}"')
    # ---
    normalized_nat_key = re.sub(
        f" {nationality_key} ", " natar ", f" {normalized_team.strip()} ", flags=re.IGNORECASE
    )
    # ---
    normalized_nat_key = normalized_nat_key.strip()
    # ---
    if normalized_nat_key in New_team_xo_team_labels:
        # TTTY = "team"
        template_label = New_team_xo_team_labels.get(normalized_nat_key, "")
        # ---
        nationality_label = All_contry_with_nat_ar.get(nationality_key, {}).get("ar", "")
        output_test(f'nat_lab:"{nationality_label}"')
        # ---
        sport_label = Sports_Keys_For_Team.get(sport_key, "")
        output_test(f'sp_lab:"{sport_label}"')
        # ---
        if template_label and nationality_label:
            template_label = template_label.replace("natar", nationality_label)
    # ---
    return template_label, sport_label


def match_nat_new_team_xo_team_labels_new(normalized_team: str, sport_key: str) -> str:
    # ---
    nationality_key = match_nat_key(normalized_team.strip())
    # ---
    if not nationality_key:
        return "", ""
    # ---
    nationality_label = All_contry_with_nat_ar.get(nationality_key, {}).get("ar", "")
    # ---
    sport_label = Sports_Keys_For_Team.get(sport_key, "")
    # ---
    output_test(f'nationality_key:"{str(nationality_key)}"')
    # ---
    template_label = get_template_label(nationality_key, "natar", normalized_team, New_team_xo_team_labels)
    # ---
    if template_label and nationality_label:
        template_label = template_label.replace("natar", nationality_label)
    # ---
    return template_label, sport_label


def Get_New_team_xo_with_nat(normalized_team: str, sport_key: str) -> str:
    team_lab = ""
    # ---
    template_label, sport_label = match_nat_new_team_xo_team_labels(normalized_team, sport_key)
    # ---
    if template_label and sport_label:
        team_lab = apply_pattern_replacement(template_label, sport_label, "xoxo")
    # ---
    return team_lab
