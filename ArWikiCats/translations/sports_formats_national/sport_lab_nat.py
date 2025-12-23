#!/usr/bin/python3
"""
NOTE: this is has alot of common code with ArWikiCats/translations/sports_formats_teams/team_job.py

TODO: this file has alot of formatted_data
"""

import functools
import re
from ...helps import logger, len_print
from ...translations import Nat_women
from ...translations_formats import format_multi_data
from ..sports.Sport_key import SPORTS_KEYS_FOR_JOBS
from ..sports.sports_lists import AFTER_KEYS_NAT, NEW_TATO_NAT


def _load_new_for_nat_female_xo_team() -> dict[str, str]:
    data = {
        "xzxz": "xzxz {nat}",  # Category:American_basketball
        "xzxz championships": "بطولات xzxz {nat}",
        "national xzxz championships": "بطولات xzxz وطنية {nat}",
        "national xzxz champions": "أبطال بطولات xzxz وطنية {nat}",
        "amateur xzxz cup": "كأس {nat} xzxz للهواة",
        "youth xzxz cup": "كأس {nat} xzxz للشباب",
        "men's xzxz cup": "كأس {nat} xzxz للرجال",
        "women's xzxz cup": "كأس {nat} xzxz للسيدات",
        "xzxz super leagues": "دوريات سوبر xzxz {nat}",
    }
    # ---
    LEVELS: dict[str, str] = {
        "premier": "الدرجة الممتازة",
        "top level": "الدرجة الأولى",
        "first level": "الدرجة الأولى",
        "first tier": "الدرجة الأولى",
        "second level": "الدرجة الثانية",
        "second tier": "الدرجة الثانية",
        "third level": "الدرجة الثالثة",
        "third tier": "الدرجة الثالثة",
        "fourth level": "الدرجة الرابعة",
        "fourth tier": "الدرجة الرابعة",
        "fifth level": "الدرجة الخامسة",
        "fifth tier": "الدرجة الخامسة",
        "sixth level": "الدرجة السادسة",
        "sixth tier": "الدرجة السادسة",
        "seventh level": "الدرجة السابعة",
        "seventh tier": "الدرجة السابعة",
    }
    # ---
    for level, lvl_lab in LEVELS.items():
        data[f"national xzxz {level} league"] = f"دوريات xzxz {{nat}} وطنية من {lvl_lab}"
        data[f"national xzxz {level} leagues"] = f"دوريات xzxz {{nat}} وطنية من {lvl_lab}"

        data[f"defunct xzxz {level} league"] = f"دوريات xzxz {{nat}} سابقة من {lvl_lab}"
        data[f"defunct xzxz {level} leagues"] = f"دوريات xzxz {{nat}} سابقة من {lvl_lab}"

        data[f"{level} xzxz league"] = f"دوريات xzxz {{nat}} من {lvl_lab}"
        data[f"{level} xzxz leagues"] = f"دوريات xzxz {{nat}} من {lvl_lab}"
        data[f"xzxz {level} league"] = f"دوريات xzxz {{nat}} من {lvl_lab}"
        data[f"xzxz {level} leagues"] = f"دوريات xzxz {{nat}} من {lvl_lab}"
    # ---
    # ---
    """

    new way to make keys 2024


    && indoor & outdoor &&
    """
    # ---
    nat_f = "{nat}"
    data["women's xzxz"] = f"xzxz {nat_f} نسائية"
    data["xzxz chairmen and investors"] = f"رؤساء ومسيرو xzxz {nat_f}"
    data["defunct xzxz cup competitions"] = f"منافسات كؤوس xzxz {nat_f} سابقة"
    data["xzxz cup competitions"] = f"منافسات كؤوس xzxz {nat_f}"
    data["domestic xzxz cup"] = f"كؤوس xzxz {nat_f} محلية"
    data["current xzxz seasons"] = f"مواسم xzxz {nat_f} حالية"
    # ---

    typies = {
        "cups": "كؤوس",
        "clubs": "أندية",
        "competitions": "منافسات",
        "leagues": "دوريات",
        "coaches": "مدربو",  # Category:Indoor soccer coaches in the United States by club
    }

    for en, ar in typies.items():
        data[f"xzxz {en}"] = f"{ar} xzxz {nat_f}"
        data[f"professional xzxz {en}"] = f"{ar} xzxz {nat_f} للمحترفين"
        data[f"defunct xzxz {en}"] = f"{ar} xzxz {nat_f} سابقة"
        data[f"domestic xzxz {en}"] = f"{ar} xzxz محلية {nat_f}"
        data[f"domestic women's xzxz {en}"] = f"{ar} xzxz محلية {nat_f} للسيدات"

        data[f"domestic xzxz {en}"] = f"{ar} xzxz {nat_f} محلية"
        data[f"indoor xzxz {en}"] = f"{ar} xzxz {nat_f} داخل الصالات"
        data[f"outdoor xzxz {en}"] = f"{ar} xzxz {nat_f} في الهواء الطلق"
        data[f"defunct indoor xzxz {en}"] = f"{ar} xzxz {nat_f} داخل الصالات سابقة"
        data[f"defunct outdoor xzxz {en}"] = f"{ar} xzxz {nat_f} في الهواء الطلق سابقة"
    # ---
    # ---
    # indoor & outdoor
    # tab[Category:Canadian domestic Soccer] = "تصنيف:كرة قدم كندية محلية"
    data.update({
        # tab[Category:Canadian domestic Soccer: "تصنيف:كرة قدم كندية محلية"
        "domestic xzxz": "xzxz {nat} محلية",
        "indoor xzxz": "xzxz {nat} داخل الصالات",
        "outdoor xzxz": "xzxz {nat} في الهواء الطلق",

        # european national women's volleyball teams
        "national women's xzxz teams": "منتخبات xzxz وطنية {nat} للسيدات",
        "national xzxz teams": "منتخبات xzxz وطنية {nat}",
        # ---
        "reserve xzxz teams": "فرق xzxz احتياطية {nat}",
        "defunct xzxz teams": "فرق xzxz سابقة {nat}",
        # ---
        "national a' xzxz teams": "منتخبات xzxz محليين {nat}",
        "national b xzxz teams": "منتخبات xzxz رديفة {nat}",
        "national reserve xzxz teams": "منتخبات xzxz وطنية احتياطية {nat}",
    })
    # ---
    return data


def _load_additional() -> dict[str, str]:
    data = {}

    for ty_nat, tas in NEW_TATO_NAT.items():  # 120
        tas = tas.strip()
        tasf = tas.format(nat="").strip()
        K_at_p = f"منتخبات xzxz وطنية {tas}"
        Ar_labs_3 = f"منتخبات xzxz وطنية {tasf}"
        if "national" not in ty_nat:
            K_at_p = f"فرق xzxz {tas}"
            Ar_labs_3 = f"فرق xzxz {tasf}"
        elif "multi-national" in ty_nat:
            Ar_labs_3 = Ar_labs_3.replace(" وطنية", "")
        Ar_labs = K_at_p.format(nat="{nat}")
        for pr_e, pr_e_Lab in AFTER_KEYS_NAT.items():       # 67
            if pr_e in ["players", "playerss"] and "women's" in ty_nat:
                pr_e_Lab = "لاعبات {lab}"
            elif "لاعبو" in pr_e_Lab and "women's" in ty_nat:
                pr_e_Lab = re.sub(r"لاعبو ", "لاعبات ", pr_e_Lab)
            Ab = f"{ty_nat} xzxz teams {pr_e}"
            Ab = Ab.strip()
            data[Ab] = pr_e_Lab.format(lab=Ar_labs)
        data[f"{ty_nat} teams"] = "فرق xzxz {nat}"
    return data


New_For_nat_female_xo_team = _load_new_for_nat_female_xo_team()
new_for_nat_female_xo_team_additional = _load_additional()  # 8162


# TODO: add data from New_For_nat_female_xo_team and new_for_nat_female_xo_team_additional
New_For_nat_female_xo_team_2 = {
    "deaths by {nat} airstrikes": "وفيات بضربات جوية {nat}",
    "{nat} airstrikes": "ضربات جوية {nat}",
    "{nat} xzxz": "xzxz {nat}",  # Category:American_basketball
    "{nat} xzxz championships": "بطولات xzxz {nat}",
    "{nat} national xzxz championships": "بطولات xzxz وطنية {nat}",
    "{nat} national xzxz champions": "أبطال بطولات xzxz وطنية {nat}",
    "{nat} amateur xzxz cup": "كأس {nat} xzxz للهواة",
    "{nat} youth xzxz cup": "كأس {nat} xzxz للشباب",
    "{nat} men's xzxz cup": "كأس {nat} xzxz للرجال",
    "{nat} women's xzxz cup": "كأس {nat} xzxz للسيدات",
    "{nat} xzxz super leagues": "دوريات سوبر xzxz {nat}",

    # tab[Category:Canadian domestic Soccer: "تصنيف:كرة قدم كندية محلية"
    "{nat} domestic xzxz": "xzxz {nat} محلية",
    "{nat} indoor xzxz": "xzxz {nat} داخل الصالات",
    "{nat} outdoor xzxz": "xzxz {nat} في الهواء الطلق",

    # european national women's volleyball teams
    "{nat} national women's xzxz teams": "منتخبات xzxz وطنية {nat} للسيدات",
    "{nat} national xzxz teams": "منتخبات xzxz وطنية {nat}",
    # ---
    "{nat} reserve xzxz teams": "فرق xzxz احتياطية {nat}",
    "{nat} defunct xzxz teams": "فرق xzxz سابقة {nat}",
    # ---
    "{nat} national a' xzxz teams": "منتخبات xzxz محليين {nat}",
    "{nat} national b xzxz teams": "منتخبات xzxz رديفة {nat}",
    "{nat} national reserve xzxz teams": "منتخبات xzxz وطنية احتياطية {nat}",
}

New_For_nat_female_xo_team_2.update({f"{{nat}} {x}": v for x, v in New_For_nat_female_xo_team.items()})
New_For_nat_female_xo_team_2.update({f"{{nat}} {x}": v for x, v in new_for_nat_female_xo_team_additional.items()})

# remove "the " from the start of all Nat_women_2 keys
Nat_women_2 = {k[4:] if k.startswith("the ") else k: v for k, v in Nat_women.items()}

both_bot = format_multi_data(
    New_For_nat_female_xo_team_2,
    Nat_women_2,
    key_placeholder="{nat}",
    value_placeholder="{nat}",
    data_list2=SPORTS_KEYS_FOR_JOBS,
    key2_placeholder="xzxz",
    value2_placeholder="xzxz",
    text_after=" people",
    text_before="the ",
)


@functools.lru_cache(maxsize=None)
def sport_lab_nat_load_new(category) -> str:
    logger.debug(f"<<yellow>> start sport_lab_nat_load_new: {category=}")
    result = both_bot.create_label(category)
    logger.debug(f"<<yellow>> end sport_lab_nat_load_new: {category=}, {result=}")
    return result


len_print.data_len(
    "sports_formats_national/te2.py",
    {
        "New_For_nat_female_xo_team": New_For_nat_female_xo_team,
        "new_for_nat_female_xo_team_additional": new_for_nat_female_xo_team_additional,
    },
)

__all__ = [
    "sport_lab_nat_load_new",
]
