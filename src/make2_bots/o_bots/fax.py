"""
from  make.make2_bots.ma_bots import fax
# Get_Teams_new(team)
# test_Lang(cate)

"""

from ... import malists_sport_lab as sport_lab
from ...ma_lists import Sports_Keys_For_Jobs
from ...ma_lists import languages_pop, lang_ttty

from .parties_bot import get_parties_lab
from ..sports_bots import team_work
from ...helps.print_bot import print_put

LANGUAGE_CACHE = {}


def Get_Teams_new(team_name: str) -> str:
    # إيجاد لاحقات التسميات الرياضية

    # قبل تطبيق الوظيفة
    # sports.py: len:"Teams_new":  685955
    # بعد تطبيق الوظيفة
    # sports.py: len:"Teams_new":  114691

    print_put(f'Get_Teams_new team:"{team_name}"')
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


def test_Lang(category: str) -> str:
    normalized_category = category.lower()

    if normalized_category in LANGUAGE_CACHE:
        if LANGUAGE_CACHE[normalized_category]:
            print_put(
                f"<<lightblue>>>> ============== test_Lang_Cash : {LANGUAGE_CACHE[normalized_category]}"
            )
        return LANGUAGE_CACHE[normalized_category]

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
        print_put(f"<<lightblue>>>> vvvvvvvvvvvv test_Lang cate:{normalized_category} vvvvvvvvvvvv ")
        print_put(f'<<lightblue>>>>>> test_Lang: new_lab  "{resolved_label}" ')
        print_put("<<lightblue>>>> ^^^^^^^^^ test_Lang end ^^^^^^^^^ ")

    LANGUAGE_CACHE[normalized_category] = resolved_label
    return resolved_label
