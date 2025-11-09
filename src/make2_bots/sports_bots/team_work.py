#!/usr/bin/python3
"""
from  make.bots import team_work # team_work.Get_Club(cate, out=False) | team_work.Teams_new_end_keys
Category:Sports_commentators_by_sport

"""


import re
from ...helps.log import logger

# ---
from ...ma_lists import Clubs_key_2
from ...ma_lists import Inter_Feds_lower
from ...ma_lists import pop_of_football_lower
from ..jobs_bots import test_4
from ..matables_bots.bot_2018 import Add_to_pop_All_18

# from ...ma_lists import pop_of_football_lower
# ---
from ..fromnet import kooora

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
GET_CLUB_CACHE = {}


def Get_Club(
    category: str,
    out: bool = False,
    return_tab: bool = False,
) -> str | dict[str, str | dict[str, str]]:
    # ---
    new_entries = {}
    # ---
    normalized_category = category.lower()
    # ---
    if normalized_category in GET_CLUB_CACHE:
        return GET_CLUB_CACHE[normalized_category]
    # ---
    category_label = ""
    # ---
    result = {"lab": "", "add": {}}
    # ---
    for suffix, suffix_template in Teams_new_end_keys.items():
        end1 = f" {suffix}"
        end2 = f" team {suffix}"
        club_key = ""
        # ---
        if normalized_category.endswith(end2) and not category_label:
            club_key = normalized_category[: -len(end2)]
        # ---
        elif normalized_category.endswith(end1) and not category_label:
            club_key = normalized_category[: -len(end1)]
        # ---
        if club_key:
            logger.debug(f'club_uu:"{club_key}", tat:"{suffix}" ')
            club_lab = (
                Clubs_key_2.get(club_key)
                or pop_of_football_lower.get(club_key)
                or Inter_Feds_lower.get(club_key)
                or ""
            )
            # ---
            if not club_lab:
                club_lab = test_4.test4_2018_with_nat(club_key)
            # ---
            if not club_lab:
                club_lab = kooora.kooora_team(club_key)
                # ---
                if club_lab:
                    c_test = re.sub(r"[abcdefghijklmnopqrstuvwxyz]", "", club_lab, flags=re.IGNORECASE)
                    if c_test == club_lab:
                        result["add"][club_key.lower()] = club_lab
                        new_entries[club_key.lower()] = club_lab
            # ---
            if club_lab:
                category_label = suffix_template.format(club_lab)
                break
    # ---
    if category_label:
        logger.debug(f'Get_Club cate:"{normalized_category}", catelab:"{category_label}"')
    # ---
    GET_CLUB_CACHE[normalized_category] = category_label
    # ---
    result["lab"] = category_label
    # ---
    Add_to_pop_All_18(new_entries)
    # ---
    return result if return_tab else category_label


def Get_team_work_Club(category: str) -> str:
    label = ""

    slab = Get_Club(category, return_tab=True)

    if isinstance(slab, str):
        return slab

    label = slab.get("lab", "")

    return label
