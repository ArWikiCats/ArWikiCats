#!/usr/bin/python3
"""
NOTE: this file has alot of formatted_data

TODO: merge with ArWikiCats/new_resolvers/translations_resolvers_v2/nats_sport_multi_v2.py

"""

import functools
import re
from ...helps import logger, len_print
from ...translations import Nat_women
from ...translations_formats import format_multi_data
from ..sports.Sport_key import SPORTS_KEYS_FOR_JOBS
from ...new.handle_suffixes import resolve_sport_category_suffix_with_mapping

AFTER_KEYS_NAT2 = {
    "": "{lab}",
    "premier leagues": "دوريات {lab} من الدرجة الممتازة",
    "first tier leagues": "دوريات {lab} من الدرجة الأولى",
    "top tier leagues": "دوريات {lab} من الدرجة الأولى",
    "second tier leagues": "دوريات {lab} من الدرجة الثانية",
    "third tier leagues": "دوريات {lab} من الدرجة الثالثة",
    "fourth tier leagues": "دوريات {lab} من الدرجة الرابعة",
    "fifth tier leagues": "دوريات {lab} من الدرجة الخامسة",
    "sixth tier leagues": "دوريات {lab} من الدرجة السادسة",
    "seventh tier leagues": "دوريات {lab} من الدرجة السابعة",
}

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
    "national junior mens": "{nat} للناشئين",
    "national junior mens under-13": "{nat} تحت 13 سنة للناشئين",
    "national junior mens under-14": "{nat} تحت 14 سنة للناشئين",
    "national junior mens under-15": "{nat} تحت 15 سنة للناشئين",
    "national junior mens under-16": "{nat} تحت 16 سنة للناشئين",
    "national junior mens under-17": "{nat} تحت 17 سنة للناشئين",
    "national junior mens under-18": "{nat} تحت 18 سنة للناشئين",
    "national junior mens under-19": "{nat} تحت 19 سنة للناشئين",
    "national junior mens under-20": "{nat} تحت 20 سنة للناشئين",
    "national junior mens under-21": "{nat} تحت 21 سنة للناشئين",
    "national junior mens under-23": "{nat} تحت 23 سنة للناشئين",
    "national junior mens under-24": "{nat} تحت 24 سنة للناشئين",
    "national junior womens": "{nat} للناشئات",
    "national junior womens under-13": "{nat} تحت 13 سنة للناشئات",
    "national junior womens under-14": "{nat} تحت 14 سنة للناشئات",
    "national junior womens under-15": "{nat} تحت 15 سنة للناشئات",
    "national junior womens under-16": "{nat} تحت 16 سنة للناشئات",
    "national junior womens under-17": "{nat} تحت 17 سنة للناشئات",
    "national junior womens under-18": "{nat} تحت 18 سنة للناشئات",
    "national junior womens under-19": "{nat} تحت 19 سنة للناشئات",
    "national junior womens under-20": "{nat} تحت 20 سنة للناشئات",
    "national junior womens under-21": "{nat} تحت 21 سنة للناشئات",
    "national junior womens under-23": "{nat} تحت 23 سنة للناشئات",
    "national junior womens under-24": "{nat} تحت 24 سنة للناشئات",
    "national mens": "{nat} للرجال",
    "national mens under-13": "{nat} تحت 13 سنة للرجال",
    "national mens under-14": "{nat} تحت 14 سنة للرجال",
    "national mens under-15": "{nat} تحت 15 سنة للرجال",
    "national mens under-16": "{nat} تحت 16 سنة للرجال",
    "national mens under-17": "{nat} تحت 17 سنة للرجال",
    "national mens under-18": "{nat} تحت 18 سنة للرجال",
    "national mens under-19": "{nat} تحت 19 سنة للرجال",
    "national mens under-20": "{nat} تحت 20 سنة للرجال",
    "national mens under-21": "{nat} تحت 21 سنة للرجال",
    "national mens under-23": "{nat} تحت 23 سنة للرجال",
    "national mens under-24": "{nat} تحت 24 سنة للرجال",
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
    "national womens": "{nat} للسيدات",
    "national womens under-13": "{nat} تحت 13 سنة للسيدات",
    "national womens under-14": "{nat} تحت 14 سنة للسيدات",
    "national womens under-15": "{nat} تحت 15 سنة للسيدات",
    "national womens under-16": "{nat} تحت 16 سنة للسيدات",
    "national womens under-17": "{nat} تحت 17 سنة للسيدات",
    "national womens under-18": "{nat} تحت 18 سنة للسيدات",
    "national womens under-19": "{nat} تحت 19 سنة للسيدات",
    "national womens under-20": "{nat} تحت 20 سنة للسيدات",
    "national womens under-21": "{nat} تحت 21 سنة للسيدات",
    "national womens under-23": "{nat} تحت 23 سنة للسيدات",
    "national womens under-24": "{nat} تحت 24 سنة للسيدات",
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
    "national youth womens": "{nat} للشابات",
    "national youth womens under-13": "{nat} تحت 13 سنة للشابات",
    "national youth womens under-14": "{nat} تحت 14 سنة للشابات",
    "national youth womens under-15": "{nat} تحت 15 سنة للشابات",
    "national youth womens under-16": "{nat} تحت 16 سنة للشابات",
    "national youth womens under-17": "{nat} تحت 17 سنة للشابات",
    "national youth womens under-18": "{nat} تحت 18 سنة للشابات",
    "national youth womens under-19": "{nat} تحت 19 سنة للشابات",
    "national youth womens under-20": "{nat} تحت 20 سنة للشابات",
    "national youth womens under-21": "{nat} تحت 21 سنة للشابات",
    "national youth womens under-23": "{nat} تحت 23 سنة للشابات",
    "national youth womens under-24": "{nat} تحت 24 سنة للشابات"
}


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

        for pr_e, pr_e_Lab in AFTER_KEYS_NAT2.items():       # 67
            if pr_e in ["players"] and "womens" in ty_nat:
                pr_e_Lab = "لاعبات {lab}"
            elif "لاعبو" in pr_e_Lab and "womens" in ty_nat:
                pr_e_Lab = re.sub(r"لاعبو ", "لاعبات ", pr_e_Lab)

            data[f"{ty_nat} {place_holder} teams {pr_e}".strip()] = pr_e_Lab.format(lab=Ar_labs)

        # data[f"{ty_nat} {place_holder} teams"] = f"فرق {place_holder} {{nat}}"
    return data


# TODO: add data from new_for_nat_female_xo_team_additional
New_For_nat_female_xo_team_2 = {
    "{nat} xzxz": "xzxz {nat}",  # Category:American_basketball
    "{nat} domestic xzxz": "xzxz {nat} محلية",
    "{nat} xzxz championships": "بطولات xzxz {nat}",
    "{nat} national xzxz championships": "بطولات xzxz وطنية {nat}",
    "{nat} national xzxz champions": "أبطال بطولات xzxz وطنية {nat}",
    "{nat} amateur xzxz cup": "كأس {nat} xzxz للهواة",
    "{nat} youth xzxz cup": "كأس {nat} xzxz للشباب",
    "{nat} mens xzxz cup": "كأس {nat} xzxz للرجال",
    "{nat} womens xzxz cup": "كأس {nat} xzxz للسيدات",
    "{nat} xzxz super leagues": "دوريات سوبر xzxz {nat}",
    "{nat} womens xzxz": "xzxz {nat} نسائية",
    "{nat} xzxz chairmen and investors": "رؤساء ومسيرو xzxz {nat}",
    "{nat} defunct xzxz cup competitions": "منافسات كؤوس xzxz {nat} سابقة",
    "{nat} xzxz cup competitions": "منافسات كؤوس xzxz {nat}",
    "{nat} domestic xzxz cup": "كؤوس xzxz {nat} محلية",
    "{nat} current xzxz seasons": "مواسم xzxz {nat} حالية",
    # ---
    "{nat} professional xzxz": "xzxz {nat} للمحترفين",
    "{nat} defunct xzxz": "xzxz {nat} سابقة",
    "{nat} domestic womens xzxz": "xzxz محلية {nat} للسيدات",
    "{nat} indoor xzxz": "xzxz {nat} داخل الصالات",
    "{nat} outdoor xzxz": "xzxz {nat} في الهواء الطلق",
    "{nat} defunct indoor xzxz": "xzxz {nat} داخل الصالات سابقة",
    "{nat} defunct outdoor xzxz": "xzxz {nat} في الهواء الطلق سابقة",
    # tab[Category:Canadian domestic Soccer: "تصنيف:كرة قدم كندية محلية"
    # european national womens volleyball teams
    "{nat} national womens xzxz teams": "منتخبات xzxz وطنية {nat} للسيدات",
    "{nat} national xzxz teams": "منتخبات xzxz وطنية {nat}",
    "{nat} reserve xzxz teams": "فرق xzxz احتياطية {nat}",
    "{nat} defunct xzxz teams": "فرق xzxz سابقة {nat}",
    "{nat} national a xzxz teams": "منتخبات xzxz محليين {nat}",
    "{nat} national b xzxz teams": "منتخبات xzxz رديفة {nat}",
    "{nat} national reserve xzxz teams": "منتخبات xzxz وطنية احتياطية {nat}",
    "deaths by {nat} airstrikes": "وفيات بضربات جوية {nat}",
    "{nat} airstrikes": "ضربات جوية {nat}",
}

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
    "{nat} xzxz national junior mens teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior mens under-13 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior mens under-14 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior mens under-15 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior mens under-16 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior mens under-17 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior mens under-18 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior mens under-19 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior mens under-20 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior mens under-21 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior mens under-23 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior mens under-24 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior womens teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior womens under-13 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior womens under-14 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior womens under-15 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior womens under-16 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior womens under-17 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior womens under-18 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior womens under-19 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior womens under-20 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior womens under-21 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior womens under-23 teams": "فرق xzxz {nat}",
    "{nat} xzxz national junior womens under-24 teams": "فرق xzxz {nat}",
    "{nat} xzxz national mens teams": "فرق xzxz {nat}",
    "{nat} xzxz national mens under-13 teams": "فرق xzxz {nat}",
    "{nat} xzxz national mens under-14 teams": "فرق xzxz {nat}",
    "{nat} xzxz national mens under-15 teams": "فرق xzxz {nat}",
    "{nat} xzxz national mens under-16 teams": "فرق xzxz {nat}",
    "{nat} xzxz national mens under-17 teams": "فرق xzxz {nat}",
    "{nat} xzxz national mens under-18 teams": "فرق xzxz {nat}",
    "{nat} xzxz national mens under-19 teams": "فرق xzxz {nat}",
    "{nat} xzxz national mens under-20 teams": "فرق xzxz {nat}",
    "{nat} xzxz national mens under-21 teams": "فرق xzxz {nat}",
    "{nat} xzxz national mens under-23 teams": "فرق xzxz {nat}",
    "{nat} xzxz national mens under-24 teams": "فرق xzxz {nat}",
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
    "{nat} xzxz national womens teams": "فرق xzxz {nat}",
    "{nat} xzxz national womens under-13 teams": "فرق xzxz {nat}",
    "{nat} xzxz national womens under-14 teams": "فرق xzxz {nat}",
    "{nat} xzxz national womens under-15 teams": "فرق xzxz {nat}",
    "{nat} xzxz national womens under-16 teams": "فرق xzxz {nat}",
    "{nat} xzxz national womens under-17 teams": "فرق xzxz {nat}",
    "{nat} xzxz national womens under-18 teams": "فرق xzxz {nat}",
    "{nat} xzxz national womens under-19 teams": "فرق xzxz {nat}",
    "{nat} xzxz national womens under-20 teams": "فرق xzxz {nat}",
    "{nat} xzxz national womens under-21 teams": "فرق xzxz {nat}",
    "{nat} xzxz national womens under-23 teams": "فرق xzxz {nat}",
    "{nat} xzxz national womens under-24 teams": "فرق xzxz {nat}",
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
    "{nat} xzxz national youth womens teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth womens under-13 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth womens under-14 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth womens under-15 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth womens under-16 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth womens under-17 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth womens under-18 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth womens under-19 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth womens under-20 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth womens under-21 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth womens under-23 teams": "فرق xzxz {nat}",
    "{nat} xzxz national youth womens under-24 teams": "فرق xzxz {nat}"
})

new_for_nat_female_xo_team_additional = _load_additional()  # 8162
New_For_nat_female_xo_team_2.update({f"{{nat}} {x}": v for x, v in new_for_nat_female_xo_team_additional.items()})

both_bot = format_multi_data(
    New_For_nat_female_xo_team_2,
    Nat_women,
    key_placeholder="{nat}",
    value_placeholder="{nat}",
    data_list2=SPORTS_KEYS_FOR_JOBS,
    key2_placeholder="xzxz",
    value2_placeholder="xzxz",
    text_after=" people",
    text_before="the ",
)


def fix_keys(category: str) -> str:
    category = category.replace("'", "").lower()

    replacements = {
        "level": "tier",
        "canadian football": "canadian-football",
    }

    for old, new in replacements.items():
        category = re.sub(rf"\b{re.escape(old)}\b", new, category)

    return category


keys_ending = {
    "cups": "كؤوس {lab}",
    "champions": "أبطال {lab}",
    "clubs": "أندية {lab}",
    "coaches": "مدربو {lab}",  # Category:Indoor soccer coaches in the United States by club
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

keys_ending = dict(sorted(
    keys_ending.items(),
    key=lambda k: (-k[0].count(" "), -len(k[0])),
))


@functools.lru_cache(maxsize=None)
def _sport_lab_nat_load_new(category) -> str:
    logger.debug(f"<<yellow>> start _sport_lab_nat_load_new: {category=}")
    result = both_bot.create_label(category)
    logger.debug(f"<<yellow>> end _sport_lab_nat_load_new: {category=}, {result=}")
    return result


@functools.lru_cache(maxsize=10000)
def sport_lab_nat_load_new(category: str) -> str:
    category = fix_keys(category)

    logger.debug(f"<<yellow>> start sport_lab_nat_load_new: {category=}")

    result = resolve_sport_category_suffix_with_mapping(category, keys_ending, _sport_lab_nat_load_new, format_key="lab")

    if result.startswith("لاعبو ") and "للسيدات" in result:
        result = result.replace("لاعبو ", "لاعبات ")

    logger.debug(f"<<yellow>> end sport_lab_nat_load_new: {category=}, {result=}")
    return result


len_print.data_len(
    "sports_formats_national/te2.py",
    {
        "New_For_nat_female_xo_team_2": New_For_nat_female_xo_team_2,
        "new_for_nat_female_xo_team_additional": new_for_nat_female_xo_team_additional,
    },
)

__all__ = [
    "sport_lab_nat_load_new",
]
