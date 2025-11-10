# -*- coding: utf-8 -*-


def apply_pattern_replacement(template_label, sport_label, xoxo):
    # ---
    team_lab = ""
    # ---
    final_label = template_label.replace(xoxo, sport_label)
    if final_label.find(xoxo) == -1:
        team_lab = final_label
    # ---
    return team_lab
