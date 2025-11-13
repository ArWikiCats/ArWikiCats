#!/usr/bin/python3
"""


"""

import re

from .sport_lab_with_nat import Get_New_team_xo_with_nat
from .team_job import New_team_xo_jobs, New_team_xo_labels, sport_formts_enar_p17_jobs
from .te3 import New_team_xo_team_labels
from .sport_lab2 import wrap_team_xo_normal_2025
from ..utils.match_sport_keys import match_sport_key
from ..utils import apply_pattern_replacement
from ..sports import SPORT_FORMTS_ENAR_P17_TEAM
from ..sports.Sport_key import SPORTS_KEYS_FOR_LABEL, SPORTS_KEYS_FOR_TEAM, SPORTS_KEYS_FOR_JOBS
from ...helps.print_bot import print_put, output_test


def Get_Sport_Format_xo_en_ar_is_P17(con_3: str) -> str:  # sport_formts_enar_p17_jobs
    # ---
    # len:"SPORT_FORMTS_EN_AR_IS_P17":  572927 قبل بدء الوظيفة
    # ---
    # sports.py: len:"SPORT_FORMTS_EN_AR_IS_P17":  175  , len:"SPORT_FORMTS_ENAR_P17_TEAM":  1434  , len:"sport_formts_enar_p17_jobs":  27
    # ---
    # labs = SPORT_FORMTS_FEMALE_NAT.get(con_3 , "")
    con_3_label = ""
    # ---
    sport_key = match_sport_key(con_3)
    # ---
    if not sport_key:
        return ""
    # ---
    sport_label = ""
    template_label = ""
    # ---
    normalized_key = con_3.replace(sport_key, "xoxo")
    normalized_key = re.sub(sport_key, "xoxo", normalized_key, flags=re.IGNORECASE)
    # ---
    print_put(f'Get_SFxo_en_ar_is P17: con_3:"{con_3}", sport_key:"{sport_key}", team_xoxo:"{normalized_key}"')
    # ---
    if normalized_key in sport_formts_enar_p17_jobs:
        sport_label = SPORTS_KEYS_FOR_JOBS[sport_key]
        template_label = sport_formts_enar_p17_jobs.get(normalized_key, "")
    # ---
    elif normalized_key in SPORT_FORMTS_ENAR_P17_TEAM:
        sport_label = SPORTS_KEYS_FOR_TEAM[sport_key]
        template_label = SPORT_FORMTS_ENAR_P17_TEAM.get(normalized_key, "")
    # ---
    else:
        print_put(f'Get_SFxo_en_ar_is P17 team_xoxo:"{normalized_key}" not in sport_formts_enar_p17_jobs or SPORT_FORMTS_ENAR_P17_TEAM')
    # ---
    if template_label and sport_label:
        con_3_label = apply_pattern_replacement(template_label, sport_label, "xoxo")
        print_put(f'Get_SFxo_en_ar_is P17 blab:"{con_3_label}"')
    else:
        print_put(f'Get_SFxo_en_ar_is P17 team_xoxo:"{normalized_key}" not in sport_formts_enar_p17_jobs')
    # ---
    if con_3_label:
        print_put(f'Get_SFxo_en_ar_is P17 con_3:"{con_3}", con_3_label:"{con_3_label}"')
    # ---
    return con_3_label


def Get_New_team_xo_normal(normalized_team: str, sport_key: str) -> str:
    # ---
    team_lab = ""
    # ---
    # team_xo = re.sub(sport_key , 'xoxo' , team_xo, flags=re.IGNORECASE)
    # ---
    print_put(f'Get_Sport Get_New_team_xo_normal P17, sport_key:"{sport_key}", team_xo:"{normalized_team}"')
    # ---
    sport_label = ""
    template_label = ""
    sport_label_source = {}
    # ---
    if normalized_team in New_team_xo_team_labels:
        # TTTY = "team"
        template_label = New_team_xo_team_labels.get(normalized_team, "")
        # sport_label = SPORTS_KEYS_FOR_TEAM.get(sport_key , "")
        sport_label_source = SPORTS_KEYS_FOR_TEAM
    # ---
    elif normalized_team in New_team_xo_jobs:
        # TTTY = "jobs"
        template_label = New_team_xo_jobs.get(normalized_team, "")
        # sport_label = SPORTS_KEYS_FOR_JOBS.get(sport_key , "")
        sport_label_source = SPORTS_KEYS_FOR_JOBS
    # ---
    elif normalized_team in New_team_xo_labels:
        # TTTY = "labels"
        template_label = New_team_xo_labels.get(normalized_team, "")
        # sport_label = SPORTS_KEYS_FOR_LABEL.get(sport_key , "")
        sport_label_source = SPORTS_KEYS_FOR_LABEL
    # ---
    if not sport_label_source:
        return ""
    # ---
    sport_label = sport_label_source.get(sport_key, "")
    # ---
    if not sport_label:
        output_test(f'Get_New_team_xo sp_lab == "" , for sport_key "{sport_key}" ')
    # ---
    if template_label and sport_label:
        team_lab = apply_pattern_replacement(template_label, sport_label, "xoxo")
    # ---
    return team_lab


def Get_New_team_xo(team: str) -> str:
    # ---
    # إيجاد تسميات نصوص رياضية مثل
    # world champion national football teams
    # New_team_xo_team_labels["world champion national {} teams".format(team2)] =  f"أبطال بطولة العالم {team2_lab}"
    # ---
    # print_put('Get_New_team_xo team:"%s"' % team)
    # ---
    # قبل تطبيق New_team_xo_jobs
    # sports.py: len:"Teams new":  695795
    # بعد تطبيق New_team_xo_jobs and New_team_xo_team_labels
    # sports.py: len:"New_team_xo_jobs":  1462 , len:"New_team_xo_team_labels":  21
    # ---
    team_lab = ""
    # ---
    sport_key = match_sport_key(team)
    # ---
    if not sport_key:
        return ""
    # ---
    team_lab = wrap_team_xo_normal_2025(team)
    # ---
    if not team_lab:
        normalized_team = re.sub(f" {sport_key} ", " xoxo ", f" {team.strip()} ", flags=re.IGNORECASE).strip()
        # ---
        # team_xo = re.sub(sport_key , 'xoxo' , team_xo, flags=re.IGNORECASE)
        # ---
        print_put(f'Get_Sport Get_New_team_xo P17: team:"{team}", sport_key:"{sport_key}", team_xo:"{normalized_team}"')
        # ---
        # if not team_lab: team_lab = Get_New_team_xo_normal(normalized_team, sport_key)
        # ---
        if not team_lab:
            team_lab = Get_New_team_xo_with_nat(normalized_team, sport_key)
    # ---
    return team_lab


__all__ = [
    "Get_Sport_Format_xo_en_ar_is_P17",
    "Get_New_team_xo_normal",
    "Get_New_team_xo",
]
