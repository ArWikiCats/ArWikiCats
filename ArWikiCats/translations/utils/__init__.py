# -*- coding: utf-8 -*-


def apply_pattern_replacements(template_label, sport_label, xoxo) -> str:
    """Replace placeholder tokens in a template with the provided sport label."""
    team_lab = ""
    final_label = template_label.replace(xoxo, sport_label)
    if xoxo not in final_label:
        team_lab = final_label
    return team_lab
