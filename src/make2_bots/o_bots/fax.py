"""Helpers for resolving sports teams and language categories."""

from __future__ import annotations

from typing import Dict

from ... import malists_sport_lab as sport_lab
from ...helps.log import logger
from ...helps.print_bot import print_put
from ...ma_lists import Sports_Keys_For_Jobs, lang_ttty, languages_pop
from ..sports_bots import team_work
from .parties_bot import get_parties_lab
from .utils import get_or_set, resolve_suffix_template

LANGUAGE_CACHE: Dict[str, str] = {}


def get_teams_new(team_name: str) -> str:
    """Return the label for ``team_name`` using multiple heuristics.

    Args:
        team_name: The English club or team name to translate.

    Returns:
        The resolved Arabic label or an empty string when no mapping exists.
    """

    # إيجاد لاحقات التسميات الرياضية

    # قبل تطبيق الوظيفة
    # sports.py: len:"Teams_new":  685955
    # بعد تطبيق الوظيفة
    # sports.py: len:"Teams_new":  114691

    print_put(f'get_teams_new team:"{team_name}"')
    team_label = sport_lab.Get_New_team_xo(team_name)

    if not team_label:
        for suffix, suffix_template in team_work.Teams_new_end_keys.items():
            suffix_with_space = f" {suffix}"
            if team_name.endswith(suffix_with_space) and not team_label:
                team_prefix = team_name[: -len(suffix_with_space)]
                print_put(f'team_uu:"{team_prefix}", tat:"{suffix}" ')
                club_label = Sports_Keys_For_Jobs.get(team_prefix, "")
                if club_label:
                    if "%s" in suffix_template:
                        team_label = suffix_template % club_label
                    else:
                        team_label = suffix_template.format(club_label)
                    break

    if team_label:
        print_put(f'team_lab:"{team_label}"')

    if not team_label:
        team_label = get_parties_lab(team_name)

    return team_label


def test_language(category: str) -> str:
    """Return the label for a language-related category.

    Args:
        category: Category name containing a language prefix.

    Returns:
        The resolved Arabic label or an empty string when the category is
        unknown.
    """

    normalized_category = category.lower().strip()

    if normalized_category in LANGUAGE_CACHE:
        cached = LANGUAGE_CACHE[normalized_category]
        if cached:
            print_put(f"<<lightblue>>>> ============== test_language cache hit : {cached}")
        return cached

    resolved_label = ""
    language_label = ""
    language_suffix = ""

    for language_key, language_name in languages_pop.items():
        if normalized_category.startswith(f"{language_key.lower()} "):
            language_label = language_name
            language_suffix = normalized_category[len(f"{language_key} ") :].strip()

    if not resolved_label:
        suffix_template = lang_ttty.get(language_suffix, "")
        if suffix_template and language_label:
            resolved_label = suffix_template % language_label

    if resolved_label:
        print_put(f"<<lightblue>>>> vvvvvvvvvvvv test_language cate:{normalized_category} vvvvvvvvvvvv ")
        print_put(f'<<lightblue>>>>>> test_language: new_lab  "{resolved_label}" ')
        print_put("<<lightblue>>>> ^^^^^^^^^ test_language end ^^^^^^^^^ ")

    LANGUAGE_CACHE[normalized_category] = resolved_label
    return resolved_label


__all__ = [
    "get_teams_new",
    "test_language",
]
