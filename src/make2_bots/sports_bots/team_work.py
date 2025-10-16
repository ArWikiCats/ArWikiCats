#!/usr/bin/python3
"""
from  make.bots import team_work # team_work.Get_Club(cate, out=False) | team_work.Teams_new_end_keys
Category:Sports_commentators_by_sport

"""


import re
from ... import printe
import sys

# ---
from ...ma_lists import Clubs_key_2
from ...ma_lists import Inter_Feds_lower
from ...ma_lists import pop_of_football_lower
from ..jobs_bots import test_4
from ..matables_bots.bot_2018 import Add_to_pop_All_18

# from ...ma_lists import pop_of_football_lower
# ---
from ..fromnet import kooora

# kooora.kooora_team(EnName)
# ---
Teams_new_end_keys = {
    # ---
    # "drafts" : " {}",
    "fan clubs": "أندية معجبي {}",
    "broadcasters": "مذيعو {}",
    "commentators": "معلقو {}",
    "commissioners": "مفوضو {}",
    # "executives" : " {}",
    # "fan clubs" : " {}",
    # ---
    "owners and executives": "رؤساء تنفيذيون وملاك {}",
    "personnel": "أفراد {}",
    "owners": "ملاك {}",
    "executives": "مدراء {}",
    "equipment": "معدات {}",
    "culture": "ثقافة {}",
    "logos": "شعارات {}",
    "tactics and skills": "مهارات {}",
    "media": "إعلام {}",
    "people": "أعلام {}",
    "terminology": "مصطلحات {}",
    "occupations": "مهن {}",
    "variants": "أشكال {}",
    # ---
    "bodies": "هيئات {}",
    "governing bodies": "هيئات تنظيم {}",
    "video games": "ألعاب فيديو {}",
    "chairmen and investors": "رؤساء ومسيرو {}",
    "comics": "قصص مصورة {}",
    "cups": "كؤوس {}",
    "records and statistics": "سجلات وإحصائيات {}",
    "leagues": "دوريات {}",
    "leagues seasons": "مواسم دوريات {}",
    "seasons": "مواسم {}",
    # ---
    "competition": "منافسات {}",
    "competitions": "منافسات {}",
    "world competitions": "منافسات {} عالمية",
    "teams": "فرق {}",
    "television series": "مسلسلات تلفزيونية {}",
    "films": "أفلام {}",
    "championships": "بطولات {}",
    "music": "موسيقى {}",
    "clubs": "أندية {}",
    "referees": "حكام {}",
    "organizations": "منظمات {}",
    "non-profit organizations": "منظمات غير ربحية {}",
    "non-profit publishers": "ناشرون غير ربحيون {}",
    # ---
    "stadiums": "ملاعب {}",
    "lists": "قوائم {}",
    "awards": "جوائز {}",
    "songs": "أغاني {}",
    "non-playing staff": "طاقم {} غير اللاعبين",
    "trainers": "مدربو {}",
    "umpires": "حكام {}",
    # ---
    "cup playoffs": "تصفيات كأس {}",
    "cup": "كأس {}",
    # ---
    "coaches": "مدربو {}",
    "managers": "مدربو {}",  # "مدراء {}"
    "manager": "مدربو {}",
    "manager history": "تاريخ مدربو {}",
    "footballers": "لاعبو {}",
    "playerss": "لاعبو {}",
    "players": "لاعبو {}",
    "results": "نتائج {}",
    "matches": "مباريات {}",
    "rivalries": "دربيات {}",
    "champions": "أبطال {}",
    # ---
}
# ---
print_team_w = {1: True}
Get_Club_Cash = {}


def printet(string):
    if print_team_w[1]:
        printe.output(string)


def Get_Club(cate, out=False, return_tab=False):
    # ---
    print_team_w[1] = out
    # ---
    added = {}
    # ---
    cate = cate.lower()
    # ---
    if cate in Get_Club_Cash:
        return Get_Club_Cash[cate]
    # ---
    # printet(')))))))))))))))))))))))))))')
    # printet('Get_Club cate:"%s"' % cate)
    catelab = ""
    # ---
    tab = {"lab": "", "add": {}}
    # ---
    for tat, tat_laab in Teams_new_end_keys.items():
        end1 = f" {tat}"
        end2 = f" team {tat}"
        club_uu = ""
        # ---
        if cate.endswith(end2) and catelab == "":
            club_uu = cate[: -len(end2)]
        # ---
        elif cate.endswith(end1) and catelab == "":
            club_uu = cate[: -len(end1)]
        # ---
        if club_uu:
            printet(f'club_uu:"{club_uu}", tat:"{tat}" ')
            # if not c_t_lab:
            # ---
            club_lab = Clubs_key_2.get(club_uu) or pop_of_football_lower.get(club_uu) or Inter_Feds_lower.get(club_uu) or ""
            # ---
            if not club_lab:
                # sd = ddfer
                club_lab = test_4.test4_2018_with_nat(club_uu)
            # ---
            if not club_lab:
                club_lab = kooora.kooora_team(club_uu)
                # ---
                if club_lab:
                    c_test = re.sub(r"[abcdefghijklmnopqrstuvwxyz]", "", club_lab, flags=re.IGNORECASE)
                    if c_test == club_lab:
                        tab["add"][club_uu.lower()] = club_lab
                        added[club_uu.lower()] = club_lab
            # ---
            if club_lab:
                catelab = tat_laab.format(club_lab)
                break
    # ---
    if catelab:
        printet(f'Get_Club cate:"{cate}", catelab:"{catelab}"')
    # ---
    Get_Club_Cash[cate] = catelab
    # ---
    # printet(')))))))))))))))))))))))))))')
    # ---
    tab["lab"] = catelab
    # ---
    Add_to_pop_All_18(added)
    # ---
    return tab if return_tab else catelab


def Get_team_work_Club(s):
    lab = ""

    slab = Get_Club(s, return_tab=True)

    if isinstance(slab, str):
        return slab

    lab = slab.get("lab", "")

    return lab


# ---
# python3 core8/pwb.py make/team_work Major_League_Soccer_team_manager


def main():
    print_team_w[1] = True
    if sys.argv and sys.argv[1]:
        La = sys.argv[1].lower()
        La = re.sub(r"_", " ", La)
        La = re.sub(r"Category:", "", La)
        so = Get_Club(La)
        # so = priffix_Mens_work(La)
        print(f"Lab: {La}")
        print(f"so :{so}")


# ---
if __name__ == "__main__":
    main()
# ---
