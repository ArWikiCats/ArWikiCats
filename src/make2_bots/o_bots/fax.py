"""
from  make.make2_bots.ma_bots import fax
# Get_Teams_new(team)
# test_Lang(cate)

"""

from .. import malists_sport_lab as sport_lab
from ..ma_lists import Sports_Keys_For_Jobs
from ..ma_lists import languages_pop, lang_ttty

from .parties_bot import get_parties_lab
from ..make2_bots.sports_bots import team_work
from ..helps.print_bot import print_put, fafa2

test_Lang_Cash = {}


def Get_Teams_new(team):
    # إيجاد لاحقات التسميات الرياضية

    # قبل تطبيق الوظيفة
    # sports.py: len:"Teams_new":  685955
    # بعد تطبيق الوظيفة
    # sports.py: len:"Teams_new":  114691

    print_put(f'Get_Teams_new team:"{team}"')
    team_lab = ""
    team_lab = sport_lab.Get_New_team_xo(team, fafa_2=fafa2[1])

    if not team_lab:
        for tat, tab_lab in team_work.Teams_new_end_keys.items():
            fafaf = f" {tat}"
            if team.endswith(fafaf) and team_lab == "":
                team_uu = team[: -len(fafaf)]
                print_put(f'team_uu:"{team_uu}", tat:"{tat}" ')
                club_lab = Sports_Keys_For_Jobs.get(team_uu, "")
                if club_lab:
                    if tab_lab.find("%s") != -1:
                        team_lab = tab_lab % club_lab
                    else:
                        team_lab = tab_lab.format(club_lab)
                    break

    if team_lab:
        print_put(f'team_lab:"{team_lab}"')

    if not team_lab:
        team_lab = get_parties_lab(team)

    return team_lab


def test_Lang(cate):
    if cate in test_Lang_Cash:
        if test_Lang_Cash[cate]:
            print_put(f"<<lightblue>>>> ============== test_Lang_Cash : {test_Lang_Cash[cate]}")
        return test_Lang_Cash[cate]

    cnt_la = ""
    cate = cate.lower()
    # test_cate = re.sub(r"(%s)" % Lang_line.lower(), "", cate)
    lang_label = ""
    tyy = ""

    for lan, dsdsd in languages_pop.items():
        if cate.startswith(f"{lan.lower()} "):
            lang_label = dsdsd
            tyy = cate[len(f"{lan} ") :].strip()

    if not cnt_la:
        tyy_lab = lang_ttty.get(tyy, "")
        if tyy_lab and lang_label:
            cnt_la = tyy_lab % lang_label

    if cnt_la:
        print_put(f"<<lightblue>>>> vvvvvvvvvvvv test_Lang cate:{cate} vvvvvvvvvvvv ")
        print_put(f'<<lightblue>>>>>> test_Lang: new_lab  "{cnt_la}" ')
        print_put("<<lightblue>>>> ^^^^^^^^^ test_Lang end ^^^^^^^^^ ")

    test_Lang_Cash[cate] = cnt_la
    return cnt_la
