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

AFTER_KEYS_NAT_LEVELS = {
    "premier league": "دوريات {lab} من الدرجة الممتازة",
    "premier leagues": "دوريات {lab} من الدرجة الممتازة",
    "second level league": "دوريات {lab} من الدرجة الثانية",
    "second level leagues": "دوريات {lab} من الدرجة الثانية",
    "second tier league": "دوريات {lab} من الدرجة الثانية",
    "second tier leagues": "دوريات {lab} من الدرجة الثانية",
    "seventh level league": "دوريات {lab} من الدرجة السابعة",
    "seventh level leagues": "دوريات {lab} من الدرجة السابعة",
    "seventh tier league": "دوريات {lab} من الدرجة السابعة",
    "seventh tier leagues": "دوريات {lab} من الدرجة السابعة",
    "sixth level league": "دوريات {lab} من الدرجة السادسة",
    "sixth level leagues": "دوريات {lab} من الدرجة السادسة",
    "sixth tier league": "دوريات {lab} من الدرجة السادسة",
    "sixth tier leagues": "دوريات {lab} من الدرجة السادسة",
    "third level league": "دوريات {lab} من الدرجة الثالثة",
    "third level leagues": "دوريات {lab} من الدرجة الثالثة",
    "third tier league": "دوريات {lab} من الدرجة الثالثة",
    "third tier leagues": "دوريات {lab} من الدرجة الثالثة",
    "top level league": "دوريات {lab} من الدرجة الأولى",
    "top level leagues": "دوريات {lab} من الدرجة الأولى",
    "fifth level league": "دوريات {lab} من الدرجة الخامسة",
    "fifth level leagues": "دوريات {lab} من الدرجة الخامسة",
    "fifth tier league": "دوريات {lab} من الدرجة الخامسة",
    "fifth tier leagues": "دوريات {lab} من الدرجة الخامسة",
    "first level league": "دوريات {lab} من الدرجة الأولى",
    "first level leagues": "دوريات {lab} من الدرجة الأولى",
    "first tier league": "دوريات {lab} من الدرجة الأولى",
    "first tier leagues": "دوريات {lab} من الدرجة الأولى",
    "fourth level league": "دوريات {lab} من الدرجة الرابعة",
    "fourth level leagues": "دوريات {lab} من الدرجة الرابعة",
    "fourth tier league": "دوريات {lab} من الدرجة الرابعة",
    "fourth tier leagues": "دوريات {lab} من الدرجة الرابعة",
}

AFTER_KEYS_NAT = {
    "": "{lab}",
    "champions": "أبطال {lab}",
    "clubs": "أندية {lab}",
    "coaches": "مدربو {lab}",
    "competitions": "منافسات {lab}",
    "events": "أحداث {lab}",
    "films": "أفلام {lab}",
    "finals": "نهائيات {lab}",
    "home stadiums": "ملاعب {lab}",
    "leagues": "دوريات {lab}",
    "lists": "قوائم {lab}",
    "manager history": "تاريخ مدربو {lab}",
    "managers": "مدربو {lab}",
    "matches": "مباريات {lab}",
    "navigational boxes": "صناديق تصفح {lab}",
    "non-profit organizations": "منظمات غير ربحية {lab}",
    "non-profit publishers": "ناشرون غير ربحيون {lab}",
    "organisations": "منظمات {lab}",
    "organizations": "منظمات {lab}",
    "players": "لاعبو {lab}",
    "positions": "مراكز {lab}",
    "records": "سجلات {lab}",
    "records and statistics": "سجلات وإحصائيات {lab}",
    "results": "نتائج {lab}",
    "rivalries": "دربيات {lab}",
    "scouts": "كشافة {lab}",
    "squads": "تشكيلات {lab}",
    "statistics": "إحصائيات {lab}",
    "teams": "فرق {lab}",
    "templates": "قوالب {lab}",
    "tournaments": "بطولات {lab}",
    "trainers": "مدربو {lab}",
    "umpires": "حكام {lab}",
    "venues": "ملاعب {lab}"
}

AFTER_KEYS_NAT.update(AFTER_KEYS_NAT_LEVELS)

NEW_TATO_NAT = {
    "": "{nat}",
    " under-13": "{nat} تحت 13 سنة",
    " under-14": "{nat} تحت 14 سنة",
    " under-15": "{nat} تحت 15 سنة",
    " under-16": "{nat} تحت 16 سنة",
    " under-17": "{nat} تحت 17 سنة",
    " under-18": "{nat} تحت 18 سنة",
    " under-19": "{nat} تحت 19 سنة",
    " under-20": "{nat} تحت 20 سنة",
    " under-21": "{nat} تحت 21 سنة",
    " under-23": "{nat} تحت 23 سنة",
    " under-24": "{nat} تحت 24 سنة",
    "national": "{nat}",
    "national amateur": "{nat} للهواة",
    "national amateur under-13": "{nat} تحت 13 سنة للهواة",
    "national amateur under-14": "{nat} تحت 14 سنة للهواة",
    "national amateur under-15": "{nat} تحت 15 سنة للهواة",
    "national amateur under-16": "{nat} تحت 16 سنة للهواة",
    "national amateur under-17": "{nat} تحت 17 سنة للهواة",
    "national amateur under-18": "{nat} تحت 18 سنة للهواة",
    "national amateur under-19": "{nat} تحت 19 سنة للهواة",
    "national amateur under-20": "{nat} تحت 20 سنة للهواة",
    "national amateur under-21": "{nat} تحت 21 سنة للهواة",
    "national amateur under-23": "{nat} تحت 23 سنة للهواة",
    "national amateur under-24": "{nat} تحت 24 سنة للهواة",
    "national junior men's": "{nat} للناشئين",
    "national junior men's under-13": "{nat} تحت 13 سنة للناشئين",
    "national junior men's under-14": "{nat} تحت 14 سنة للناشئين",
    "national junior men's under-15": "{nat} تحت 15 سنة للناشئين",
    "national junior men's under-16": "{nat} تحت 16 سنة للناشئين",
    "national junior men's under-17": "{nat} تحت 17 سنة للناشئين",
    "national junior men's under-18": "{nat} تحت 18 سنة للناشئين",
    "national junior men's under-19": "{nat} تحت 19 سنة للناشئين",
    "national junior men's under-20": "{nat} تحت 20 سنة للناشئين",
    "national junior men's under-21": "{nat} تحت 21 سنة للناشئين",
    "national junior men's under-23": "{nat} تحت 23 سنة للناشئين",
    "national junior men's under-24": "{nat} تحت 24 سنة للناشئين",
    "national junior women's": "{nat} للناشئات",
    "national junior women's under-13": "{nat} تحت 13 سنة للناشئات",
    "national junior women's under-14": "{nat} تحت 14 سنة للناشئات",
    "national junior women's under-15": "{nat} تحت 15 سنة للناشئات",
    "national junior women's under-16": "{nat} تحت 16 سنة للناشئات",
    "national junior women's under-17": "{nat} تحت 17 سنة للناشئات",
    "national junior women's under-18": "{nat} تحت 18 سنة للناشئات",
    "national junior women's under-19": "{nat} تحت 19 سنة للناشئات",
    "national junior women's under-20": "{nat} تحت 20 سنة للناشئات",
    "national junior women's under-21": "{nat} تحت 21 سنة للناشئات",
    "national junior women's under-23": "{nat} تحت 23 سنة للناشئات",
    "national junior women's under-24": "{nat} تحت 24 سنة للناشئات",
    "national men's": "{nat} للرجال",
    "national men's under-13": "{nat} تحت 13 سنة للرجال",
    "national men's under-14": "{nat} تحت 14 سنة للرجال",
    "national men's under-15": "{nat} تحت 15 سنة للرجال",
    "national men's under-16": "{nat} تحت 16 سنة للرجال",
    "national men's under-17": "{nat} تحت 17 سنة للرجال",
    "national men's under-18": "{nat} تحت 18 سنة للرجال",
    "national men's under-19": "{nat} تحت 19 سنة للرجال",
    "national men's under-20": "{nat} تحت 20 سنة للرجال",
    "national men's under-21": "{nat} تحت 21 سنة للرجال",
    "national men's under-23": "{nat} تحت 23 سنة للرجال",
    "national men's under-24": "{nat} تحت 24 سنة للرجال",
    "national under-13": "{nat} تحت 13 سنة",
    "national under-14": "{nat} تحت 14 سنة",
    "national under-15": "{nat} تحت 15 سنة",
    "national under-16": "{nat} تحت 16 سنة",
    "national under-17": "{nat} تحت 17 سنة",
    "national under-18": "{nat} تحت 18 سنة",
    "national under-19": "{nat} تحت 19 سنة",
    "national under-20": "{nat} تحت 20 سنة",
    "national under-21": "{nat} تحت 21 سنة",
    "national under-23": "{nat} تحت 23 سنة",
    "national under-24": "{nat} تحت 24 سنة",
    "national women's": "{nat} للسيدات",
    "national women's under-13": "{nat} تحت 13 سنة للسيدات",
    "national women's under-14": "{nat} تحت 14 سنة للسيدات",
    "national women's under-15": "{nat} تحت 15 سنة للسيدات",
    "national women's under-16": "{nat} تحت 16 سنة للسيدات",
    "national women's under-17": "{nat} تحت 17 سنة للسيدات",
    "national women's under-18": "{nat} تحت 18 سنة للسيدات",
    "national women's under-19": "{nat} تحت 19 سنة للسيدات",
    "national women's under-20": "{nat} تحت 20 سنة للسيدات",
    "national women's under-21": "{nat} تحت 21 سنة للسيدات",
    "national women's under-23": "{nat} تحت 23 سنة للسيدات",
    "national women's under-24": "{nat} تحت 24 سنة للسيدات",
    "national youth": "{nat} للشباب",
    "national youth under-13": "{nat} تحت 13 سنة للشباب",
    "national youth under-14": "{nat} تحت 14 سنة للشباب",
    "national youth under-15": "{nat} تحت 15 سنة للشباب",
    "national youth under-16": "{nat} تحت 16 سنة للشباب",
    "national youth under-17": "{nat} تحت 17 سنة للشباب",
    "national youth under-18": "{nat} تحت 18 سنة للشباب",
    "national youth under-19": "{nat} تحت 19 سنة للشباب",
    "national youth under-20": "{nat} تحت 20 سنة للشباب",
    "national youth under-21": "{nat} تحت 21 سنة للشباب",
    "national youth under-23": "{nat} تحت 23 سنة للشباب",
    "national youth under-24": "{nat} تحت 24 سنة للشباب",
    "national youth women's": "{nat} للشابات",
    "national youth women's under-13": "{nat} تحت 13 سنة للشابات",
    "national youth women's under-14": "{nat} تحت 14 سنة للشابات",
    "national youth women's under-15": "{nat} تحت 15 سنة للشابات",
    "national youth women's under-16": "{nat} تحت 16 سنة للشابات",
    "national youth women's under-17": "{nat} تحت 17 سنة للشابات",
    "national youth women's under-18": "{nat} تحت 18 سنة للشابات",
    "national youth women's under-19": "{nat} تحت 19 سنة للشابات",
    "national youth women's under-20": "{nat} تحت 20 سنة للشابات",
    "national youth women's under-21": "{nat} تحت 21 سنة للشابات",
    "national youth women's under-23": "{nat} تحت 23 سنة للشابات",
    "national youth women's under-24": "{nat} تحت 24 سنة للشابات"
}


def _load_new_for_nat_female_xo_team() -> dict[str, str]:
    data = {
        "xzxz": "xzxz {nat}",
        "xzxz championships": "بطولات xzxz {nat}",
        "national xzxz championships": "بطولات xzxz وطنية {nat}",
        "national xzxz champions": "أبطال بطولات xzxz وطنية {nat}",
        "amateur xzxz cup": "كأس {nat} xzxz للهواة",
        "youth xzxz cup": "كأس {nat} xzxz للشباب",
        "men's xzxz cup": "كأس {nat} xzxz للرجال",
        "women's xzxz cup": "كأس {nat} xzxz للسيدات",
        "xzxz super leagues": "دوريات سوبر xzxz {nat}",
    }
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
    place_holder = "xzxz"
    for ty_nat, tas in NEW_TATO_NAT.items():  # 120
        tas = tas.strip()
        tasf = tas.format(nat="").strip()
        teams_label = f"منتخبات {place_holder} وطنية {tas}"
        Ar_labs_3 = f"منتخبات {place_holder} وطنية {tasf}"
        if "national" not in ty_nat:
            teams_label = f"فرق {place_holder} {tas}"
            Ar_labs_3 = f"فرق {place_holder} {tasf}"
        elif "multi-national" in ty_nat:
            Ar_labs_3 = Ar_labs_3.replace(" وطنية", "")
        Ar_labs = teams_label.format(nat="{nat}")

        for pr_e, pr_e_Lab in AFTER_KEYS_NAT.items():       # 67
            if pr_e in ["players"] and "women's" in ty_nat:
                pr_e_Lab = "لاعبات {lab}"
            elif "لاعبو" in pr_e_Lab and "women's" in ty_nat:
                pr_e_Lab = re.sub(r"لاعبو ", "لاعبات ", pr_e_Lab)

            data[f"{ty_nat} {place_holder} teams {pr_e}".strip()] = pr_e_Lab.format(lab=Ar_labs)

        # data[f"{ty_nat} {place_holder} teams"] = f"فرق {place_holder} {{nat}}"
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
New_For_nat_female_xo_team_2.update({
    "{nat} xzxz teams": "فرق xzxz {nat}",
    "{nat} xzxz under-13 teams": "فرق xzxz {nat}",
    "{nat} xzxz under-14 teams": "فرق xzxz {nat}",
    "{nat} xzxz under-15 teams": "فرق xzxz {nat}",
    "{nat} xzxz under-16 teams": "فرق xzxz {nat}",
    "{nat} xzxz under-17 teams": "فرق xzxz {nat}",
    "{nat} xzxz under-18 teams": "فرق xzxz {nat}",
    "{nat} xzxz under-19 teams": "فرق xzxz {nat}",
    "{nat} xzxz under-20 teams": "فرق xzxz {nat}",
    "{nat} xzxz under-21 teams": "فرق xzxz {nat}",
    "{nat} xzxz under-23 teams": "فرق xzxz {nat}",
    "{nat} xzxz under-24 teams": "فرق xzxz {nat}",
    "{nat} xzxz national amateur teams": "فرق xzxz {nat}",
    "{nat} xzxz national amateur under-13 teams": "فرق xzxz {nat}",
    "{nat} xzxz national amateur under-14 teams": "فرق xzxz {nat}",
    "{nat} xzxz national amateur under-15 teams": "فرق xzxz {nat}",
    "{nat} xzxz national amateur under-16 teams": "فرق xzxz {nat}",
    "{nat} xzxz national amateur under-17 teams": "فرق xzxz {nat}",
    "{nat} xzxz national amateur under-18 teams": "فرق xzxz {nat}",
    "{nat} xzxz national amateur under-19 teams": "فرق xzxz {nat}",
    "{nat} xzxz national amateur under-20 teams": "فرق xzxz {nat}",
    "{nat} xzxz national amateur under-21 teams": "فرق xzxz {nat}",
    "{nat} xzxz national amateur under-23 teams": "فرق xzxz {nat}",
    "{nat} xzxz national amateur under-24 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior men's teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior men's under-13 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior men's under-14 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior men's under-15 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior men's under-16 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior men's under-17 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior men's under-18 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior men's under-19 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior men's under-20 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior men's under-21 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior men's under-23 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior men's under-24 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior women's teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior women's under-13 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior women's under-14 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior women's under-15 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior women's under-16 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior women's under-17 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior women's under-18 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior women's under-19 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior women's under-20 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior women's under-21 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior women's under-23 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior women's under-24 teams": "فرق xzxz {nat}",
    "{nat} xzxz national men's teams": "فرق xzxz {nat}",
    "{nat} xzxz national men's under-13 teams": "فرق xzxz {nat}",
    "{nat} xzxz national men's under-14 teams": "فرق xzxz {nat}",
    "{nat} xzxz national men's under-15 teams": "فرق xzxz {nat}",
    "{nat} xzxz national men's under-16 teams": "فرق xzxz {nat}",
    "{nat} xzxz national men's under-17 teams": "فرق xzxz {nat}",
    "{nat} xzxz national men's under-18 teams": "فرق xzxz {nat}",
    "{nat} xzxz national men's under-19 teams": "فرق xzxz {nat}",
    "{nat} xzxz national men's under-20 teams": "فرق xzxz {nat}",
    "{nat} xzxz national men's under-21 teams": "فرق xzxz {nat}",
    "{nat} xzxz national men's under-23 teams": "فرق xzxz {nat}",
    "{nat} xzxz national men's under-24 teams": "فرق xzxz {nat}",
    "{nat} xzxz national teams": "فرق xzxz {nat}",
    "{nat} xzxz national under-13 teams": "فرق xzxz {nat}",
    "{nat} xzxz national under-14 teams": "فرق xzxz {nat}",
    "{nat} xzxz national under-15 teams": "فرق xzxz {nat}",
    "{nat} xzxz national under-16 teams": "فرق xzxz {nat}",
    "{nat} xzxz national under-17 teams": "فرق xzxz {nat}",
    "{nat} xzxz national under-18 teams": "فرق xzxz {nat}",
    "{nat} xzxz national under-19 teams": "فرق xzxz {nat}",
    "{nat} xzxz national under-20 teams": "فرق xzxz {nat}",
    "{nat} xzxz national under-21 teams": "فرق xzxz {nat}",
    "{nat} xzxz national under-23 teams": "فرق xzxz {nat}",
    "{nat} xzxz national under-24 teams": "فرق xzxz {nat}",
    "{nat} xzxz national women's teams": "فرق xzxz {nat}",
    "{nat} xzxz national women's under-13 teams": "فرق xzxz {nat}",
    "{nat} xzxz national women's under-14 teams": "فرق xzxz {nat}",
    "{nat} xzxz national women's under-15 teams": "فرق xzxz {nat}",
    "{nat} xzxz national women's under-16 teams": "فرق xzxz {nat}",
    "{nat} xzxz national women's under-17 teams": "فرق xzxz {nat}",
    "{nat} xzxz national women's under-18 teams": "فرق xzxz {nat}",
    "{nat} xzxz national women's under-19 teams": "فرق xzxz {nat}",
    "{nat} xzxz national women's under-20 teams": "فرق xzxz {nat}",
    "{nat} xzxz national women's under-21 teams": "فرق xzxz {nat}",
    "{nat} xzxz national women's under-23 teams": "فرق xzxz {nat}",
    "{nat} xzxz national women's under-24 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth under-13 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth under-14 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth under-15 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth under-16 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth under-17 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth under-18 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth under-19 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth under-20 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth under-21 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth under-23 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth under-24 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth women's teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth women's under-13 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth women's under-14 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth women's under-15 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth women's under-16 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth women's under-17 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth women's under-18 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth women's under-19 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth women's under-20 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth women's under-21 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth women's under-23 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth women's under-24 teams": "فرق xzxz {nat}"
})
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
