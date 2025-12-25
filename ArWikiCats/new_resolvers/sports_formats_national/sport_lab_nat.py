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
from ...translations.sports.Sport_key import SPORTS_KEYS_FOR_JOBS
from ...new.handle_suffixes import resolve_sport_category_suffix_with_mapping

# TODO: This all wrong arabic values need to be fixed later
under_data = {
    "{en} xzxz under-13 teams": "فرق xzxz {female}",
    "{en} xzxz under-14 teams": "فرق xzxz {female}",
    "{en} xzxz under-15 teams": "فرق xzxz {female}",
    "{en} xzxz under-16 teams": "فرق xzxz {female}",
    "{en} xzxz under-17 teams": "فرق xzxz {female}",
    "{en} xzxz under-18 teams": "فرق xzxz {female}",
    "{en} xzxz under-19 teams": "فرق xzxz {female}",
    "{en} xzxz under-20 teams": "فرق xzxz {female}",
    "{en} xzxz under-21 teams": "فرق xzxz {female}",
    "{en} xzxz under-23 teams": "فرق xzxz {female}",
    "{en} xzxz under-24 teams": "فرق xzxz {female}",
    "{en} xzxz national amateur teams": "فرق xzxz {female}",
    "{en} xzxz national amateur under-13 teams": "فرق xzxz {female}",
    "{en} xzxz national amateur under-14 teams": "فرق xzxz {female}",
    "{en} xzxz national amateur under-15 teams": "فرق xzxz {female}",
    "{en} xzxz national amateur under-16 teams": "فرق xzxz {female}",
    "{en} xzxz national amateur under-17 teams": "فرق xzxz {female}",
    "{en} xzxz national amateur under-18 teams": "فرق xzxz {female}",
    "{en} xzxz national amateur under-19 teams": "فرق xzxz {female}",
    "{en} xzxz national amateur under-20 teams": "فرق xzxz {female}",
    "{en} xzxz national amateur under-21 teams": "فرق xzxz {female}",
    "{en} xzxz national amateur under-23 teams": "فرق xzxz {female}",
    "{en} xzxz national amateur under-24 teams": "فرق xzxz {female}",
    "{en} xzxz national junior mens teams": "فرق xzxz {female}",
    "{en} xzxz national junior mens under-13 teams": "فرق xzxz {female}",
    "{en} xzxz national junior mens under-14 teams": "فرق xzxz {female}",
    "{en} xzxz national junior mens under-15 teams": "فرق xzxz {female}",
    "{en} xzxz national junior mens under-16 teams": "فرق xzxz {female}",
    "{en} xzxz national junior mens under-17 teams": "فرق xzxz {female}",
    "{en} xzxz national junior mens under-18 teams": "فرق xzxz {female}",
    "{en} xzxz national junior mens under-19 teams": "فرق xzxz {female}",
    "{en} xzxz national junior mens under-20 teams": "فرق xzxz {female}",
    "{en} xzxz national junior mens under-21 teams": "فرق xzxz {female}",
    "{en} xzxz national junior mens under-23 teams": "فرق xzxz {female}",
    "{en} xzxz national junior mens under-24 teams": "فرق xzxz {female}",
    "{en} xzxz national junior womens teams": "فرق xzxz {female}",
    "{en} xzxz national junior womens under-13 teams": "فرق xzxz {female}",
    "{en} xzxz national junior womens under-14 teams": "فرق xzxz {female}",
    "{en} xzxz national junior womens under-15 teams": "فرق xzxz {female}",
    "{en} xzxz national junior womens under-16 teams": "فرق xzxz {female}",
    "{en} xzxz national junior womens under-17 teams": "فرق xzxz {female}",
    "{en} xzxz national junior womens under-18 teams": "فرق xzxz {female}",
    "{en} xzxz national junior womens under-19 teams": "فرق xzxz {female}",
    "{en} xzxz national junior womens under-20 teams": "فرق xzxz {female}",
    "{en} xzxz national junior womens under-21 teams": "فرق xzxz {female}",
    "{en} xzxz national junior womens under-23 teams": "فرق xzxz {female}",
    "{en} xzxz national junior womens under-24 teams": "فرق xzxz {female}",
    "{en} xzxz national mens teams": "فرق xzxz {female}",
    "{en} xzxz national mens under-13 teams": "فرق xzxz {female}",
    "{en} xzxz national mens under-14 teams": "فرق xzxz {female}",
    "{en} xzxz national mens under-15 teams": "فرق xzxz {female}",
    "{en} xzxz national mens under-16 teams": "فرق xzxz {female}",
    "{en} xzxz national mens under-17 teams": "فرق xzxz {female}",
    "{en} xzxz national mens under-18 teams": "فرق xzxz {female}",
    "{en} xzxz national mens under-19 teams": "فرق xzxz {female}",
    "{en} xzxz national mens under-20 teams": "فرق xzxz {female}",
    "{en} xzxz national mens under-21 teams": "فرق xzxz {female}",
    "{en} xzxz national mens under-23 teams": "فرق xzxz {female}",
    "{en} xzxz national mens under-24 teams": "فرق xzxz {female}",
    "{en} xzxz national teams": "فرق xzxz {female}",
    "{en} xzxz national under-13 teams": "فرق xzxz {female}",
    "{en} xzxz national under-14 teams": "فرق xzxz {female}",
    "{en} xzxz national under-15 teams": "فرق xzxz {female}",
    "{en} xzxz national under-16 teams": "فرق xzxz {female}",
    "{en} xzxz national under-17 teams": "فرق xzxz {female}",
    "{en} xzxz national under-18 teams": "فرق xzxz {female}",
    "{en} xzxz national under-19 teams": "فرق xzxz {female}",
    "{en} xzxz national under-20 teams": "فرق xzxz {female}",
    "{en} xzxz national under-21 teams": "فرق xzxz {female}",
    "{en} xzxz national under-23 teams": "فرق xzxz {female}",
    "{en} xzxz national under-24 teams": "فرق xzxz {female}",
    "{en} xzxz national womens teams": "فرق xzxz {female}",
    "{en} xzxz national womens under-13 teams": "فرق xzxz {female}",
    "{en} xzxz national womens under-14 teams": "فرق xzxz {female}",
    "{en} xzxz national womens under-15 teams": "فرق xzxz {female}",
    "{en} xzxz national womens under-16 teams": "فرق xzxz {female}",
    "{en} xzxz national womens under-17 teams": "فرق xzxz {female}",
    "{en} xzxz national womens under-18 teams": "فرق xzxz {female}",
    "{en} xzxz national womens under-19 teams": "فرق xzxz {female}",
    "{en} xzxz national womens under-20 teams": "فرق xzxz {female}",
    "{en} xzxz national womens under-21 teams": "فرق xzxz {female}",
    "{en} xzxz national womens under-23 teams": "فرق xzxz {female}",
    "{en} xzxz national womens under-24 teams": "فرق xzxz {female}",
    "{en} xzxz national youth teams": "فرق xzxz {female}",
    "{en} xzxz national youth under-13 teams": "فرق xzxz {female}",
    "{en} xzxz national youth under-14 teams": "فرق xzxz {female}",
    "{en} xzxz national youth under-15 teams": "فرق xzxz {female}",
    "{en} xzxz national youth under-16 teams": "فرق xzxz {female}",
    "{en} xzxz national youth under-17 teams": "فرق xzxz {female}",
    "{en} xzxz national youth under-18 teams": "فرق xzxz {female}",
    "{en} xzxz national youth under-19 teams": "فرق xzxz {female}",
    "{en} xzxz national youth under-20 teams": "فرق xzxz {female}",
    "{en} xzxz national youth under-21 teams": "فرق xzxz {female}",
    "{en} xzxz national youth under-23 teams": "فرق xzxz {female}",
    "{en} xzxz national youth under-24 teams": "فرق xzxz {female}",
    "{en} xzxz national youth womens teams": "فرق xzxz {female}",
    "{en} xzxz national youth womens under-13 teams": "فرق xzxz {female}",
    "{en} xzxz national youth womens under-14 teams": "فرق xzxz {female}",
    "{en} xzxz national youth womens under-15 teams": "فرق xzxz {female}",
    "{en} xzxz national youth womens under-16 teams": "فرق xzxz {female}",
    "{en} xzxz national youth womens under-17 teams": "فرق xzxz {female}",
    "{en} xzxz national youth womens under-18 teams": "فرق xzxz {female}",
    "{en} xzxz national youth womens under-19 teams": "فرق xzxz {female}",
    "{en} xzxz national youth womens under-20 teams": "فرق xzxz {female}",
    "{en} xzxz national youth womens under-21 teams": "فرق xzxz {female}",
    "{en} xzxz national youth womens under-23 teams": "فرق xzxz {female}",

    # ["softball national youth womens under-24 teams"] = "منتخبات كرة لينة تحت 24 سنة للشابات"
    "{en} xzxz national youth womens under-24 teams": "منتخبات xzxz تحت 24 سنة للشابات",
}

YOUTH_TEAM_LABELS = {
    "under-13": "تحت 13 سنة",
    "under-14": "تحت 14 سنة",
    "under-15": "تحت 15 سنة",
    "under-16": "تحت 16 سنة",
    "under-17": "تحت 17 سنة",
    "under-18": "تحت 18 سنة",
    "under-19": "تحت 19 سنة",
    "under-20": "تحت 20 سنة",
    "under-21": "تحت 21 سنة",
    "under-23": "تحت 23 سنة",
    "under-24": "تحت 24 سنة",

    "national amateur": "للهواة",
    "national junior mens": "للناشئين",
    "national junior womens": "للناشئات",
    "national mens": "للرجال",
    "national womens": "للسيدات",
    "national youth": "للشباب",
    "national youth womens": "للشابات",

    "national under-13": "تحت 13 سنة",
    "national under-14": "تحت 14 سنة",
    "national under-15": "تحت 15 سنة",
    "national under-16": "تحت 16 سنة",
    "national under-17": "تحت 17 سنة",
    "national under-18": "تحت 18 سنة",
    "national under-19": "تحت 19 سنة",
    "national under-20": "تحت 20 سنة",
    "national under-21": "تحت 21 سنة",
    "national under-23": "تحت 23 سنة",
    "national under-24": "تحت 24 سنة",

    "national amateur under-13": "تحت 13 سنة للهواة",
    "national amateur under-14": "تحت 14 سنة للهواة",
    "national amateur under-15": "تحت 15 سنة للهواة",
    "national amateur under-16": "تحت 16 سنة للهواة",
    "national amateur under-17": "تحت 17 سنة للهواة",
    "national amateur under-18": "تحت 18 سنة للهواة",
    "national amateur under-19": "تحت 19 سنة للهواة",
    "national amateur under-20": "تحت 20 سنة للهواة",
    "national amateur under-21": "تحت 21 سنة للهواة",
    "national amateur under-23": "تحت 23 سنة للهواة",
    "national amateur under-24": "تحت 24 سنة للهواة",
    "national junior mens under-13": "تحت 13 سنة للناشئين",
    "national junior mens under-14": "تحت 14 سنة للناشئين",
    "national junior mens under-15": "تحت 15 سنة للناشئين",
    "national junior mens under-16": "تحت 16 سنة للناشئين",
    "national junior mens under-17": "تحت 17 سنة للناشئين",
    "national junior mens under-18": "تحت 18 سنة للناشئين",
    "national junior mens under-19": "تحت 19 سنة للناشئين",
    "national junior mens under-20": "تحت 20 سنة للناشئين",
    "national junior mens under-21": "تحت 21 سنة للناشئين",
    "national junior mens under-23": "تحت 23 سنة للناشئين",
    "national junior mens under-24": "تحت 24 سنة للناشئين",
    "national junior womens under-13": "تحت 13 سنة للناشئات",
    "national junior womens under-14": "تحت 14 سنة للناشئات",
    "national junior womens under-15": "تحت 15 سنة للناشئات",
    "national junior womens under-16": "تحت 16 سنة للناشئات",
    "national junior womens under-17": "تحت 17 سنة للناشئات",
    "national junior womens under-18": "تحت 18 سنة للناشئات",
    "national junior womens under-19": "تحت 19 سنة للناشئات",
    "national junior womens under-20": "تحت 20 سنة للناشئات",
    "national junior womens under-21": "تحت 21 سنة للناشئات",
    "national junior womens under-23": "تحت 23 سنة للناشئات",
    "national junior womens under-24": "تحت 24 سنة للناشئات",
    "national mens under-13": "تحت 13 سنة للرجال",
    "national mens under-14": "تحت 14 سنة للرجال",
    "national mens under-15": "تحت 15 سنة للرجال",
    "national mens under-16": "تحت 16 سنة للرجال",
    "national mens under-17": "تحت 17 سنة للرجال",
    "national mens under-18": "تحت 18 سنة للرجال",
    "national mens under-19": "تحت 19 سنة للرجال",
    "national mens under-20": "تحت 20 سنة للرجال",
    "national mens under-21": "تحت 21 سنة للرجال",
    "national mens under-23": "تحت 23 سنة للرجال",
    "national mens under-24": "تحت 24 سنة للرجال",

    "national youth under-13": "تحت 13 سنة للشباب",
    "national youth under-14": "تحت 14 سنة للشباب",
    "national youth under-15": "تحت 15 سنة للشباب",
    "national youth under-16": "تحت 16 سنة للشباب",
    "national youth under-17": "تحت 17 سنة للشباب",
    "national youth under-18": "تحت 18 سنة للشباب",
    "national youth under-19": "تحت 19 سنة للشباب",
    "national youth under-20": "تحت 20 سنة للشباب",
    "national youth under-21": "تحت 21 سنة للشباب",
    "national youth under-23": "تحت 23 سنة للشباب",
    "national youth under-24": "تحت 24 سنة للشباب",

    "national womens under-13": "تحت 13 سنة للسيدات",
    "national womens under-14": "تحت 14 سنة للسيدات",
    "national womens under-15": "تحت 15 سنة للسيدات",
    "national womens under-16": "تحت 16 سنة للسيدات",
    "national womens under-17": "تحت 17 سنة للسيدات",
    "national womens under-18": "تحت 18 سنة للسيدات",
    "national womens under-19": "تحت 19 سنة للسيدات",
    "national womens under-20": "تحت 20 سنة للسيدات",
    "national womens under-21": "تحت 21 سنة للسيدات",
    "national womens under-23": "تحت 23 سنة للسيدات",
    "national womens under-24": "تحت 24 سنة للسيدات",
    "national youth womens under-13": "تحت 13 سنة للشابات",
    "national youth womens under-14": "تحت 14 سنة للشابات",
    "national youth womens under-15": "تحت 15 سنة للشابات",
    "national youth womens under-16": "تحت 16 سنة للشابات",
    "national youth womens under-17": "تحت 17 سنة للشابات",
    "national youth womens under-18": "تحت 18 سنة للشابات",
    "national youth womens under-19": "تحت 19 سنة للشابات",
    "national youth womens under-20": "تحت 20 سنة للشابات",
    "national youth womens under-21": "تحت 21 سنة للشابات",
    "national youth womens under-23": "تحت 23 سنة للشابات",
    "national youth womens under-24": "تحت 24 سنة للشابات"
}


def _load_additional() -> dict[str, str]:
    data = {}
    place_holder = "xzxz"

    AFTER_KEYS_NAT2 = {
        "premier": "{lab} من الدرجة الممتازة",
        "first tier": "{lab} من الدرجة الأولى",
        "top tier": "{lab} من الدرجة الأولى",
        "second tier": "{lab} من الدرجة الثانية",
        "third tier": "{lab} من الدرجة الثالثة",
        "fourth tier": "{lab} من الدرجة الرابعة",
        "fifth tier": "{lab} من الدرجة الخامسة",
        "sixth tier": "{lab} من الدرجة السادسة",
        "seventh tier": "{lab} من الدرجة السابعة",
    }
    for yt_type, yt_name in YOUTH_TEAM_LABELS.items():  # 120
        teams_label = f"منتخبات {place_holder} وطنية {{female}} {yt_name}"

        if "national" not in yt_type:
            teams_label = f"فرق {place_holder} {{female}} {yt_name}"

        Ar_labs = teams_label.format(female="{female}")

        for pr_e, pr_e_Lab in AFTER_KEYS_NAT2.items():       # 67
            key = f"{{en}} {yt_type} {place_holder} teams {pr_e}"
            key = key.replace("  ", " ").strip()
            data[key] = pr_e_Lab.format(lab=Ar_labs)
    return data


# TODO: add data from new_for_nat_female_xo_team_additional
New_For_nat_female_xo_team_2 = {
    "{en} xzxz teams": "فرق xzxz {female}",
    "{en} xzxz national teams": "منتخبات xzxz {female}",
    "{en} xzxz": "xzxz {female}",  # Category:American_basketball
    "{en} domestic xzxz": "xzxz {female} محلية",
    "{en} xzxz championships": "بطولات xzxz {female}",
    "{en} national xzxz championships": "بطولات xzxz وطنية {female}",
    "{en} national xzxz champions": "أبطال بطولات xzxz وطنية {female}",
    "{en} amateur xzxz cup": "كأس {female} xzxz للهواة",
    "{en} youth xzxz cup": "كأس {female} xzxz للشباب",
    "{en} mens xzxz cup": "كأس {female} xzxz للرجال",
    "{en} womens xzxz cup": "كأس {female} xzxz للسيدات",
    "{en} xzxz super leagues": "دوريات سوبر xzxz {female}",
    "{en} womens xzxz": "xzxz {female} نسائية",
    "{en} defunct xzxz cup": "كؤوس xzxz {female} سابقة",
    "{en} xzxz cup": "كؤوس xzxz {female}",
    "{en} domestic xzxz cup": "كؤوس xzxz {female} محلية",
    "{en} current xzxz seasons": "مواسم xzxz {female} حالية",
    # ---
    "{en} professional xzxz": "xzxz {female} للمحترفين",
    "{en} defunct xzxz": "xzxz {female} سابقة",
    "{en} domestic womens xzxz": "xzxz محلية {female} للسيدات",
    "{en} indoor xzxz": "xzxz {female} داخل الصالات",
    "{en} outdoor xzxz": "xzxz {female} في الهواء الطلق",
    "{en} defunct indoor xzxz": "xzxz {female} داخل الصالات سابقة",
    "{en} defunct outdoor xzxz": "xzxz {female} في الهواء الطلق سابقة",
    # tab[Category:Canadian domestic Soccer: "تصنيف:كرة قدم كندية محلية"
    # european national womens volleyball teams
    "{en} national womens xzxz teams": "منتخبات xzxz وطنية {female} للسيدات",
    "{en} national xzxz teams": "منتخبات xzxz وطنية {female}",
    "{en} reserve xzxz teams": "فرق xzxz احتياطية {female}",
    "{en} defunct xzxz teams": "فرق xzxz سابقة {female}",
    "{en} national a xzxz teams": "منتخبات xzxz محليين {female}",
    "{en} national b xzxz teams": "منتخبات xzxz رديفة {female}",
    "{en} national reserve xzxz teams": "منتخبات xzxz وطنية احتياطية {female}",
    "deaths by {en} airstrikes": "وفيات بضربات جوية {female}",
    "{en} airstrikes": "ضربات جوية {female}",
}

# New_For_nat_female_xo_team_2.update(under_data)

new_for_nat_female_xo_team_additional = _load_additional()  # 8162
New_For_nat_female_xo_team_2.update(new_for_nat_female_xo_team_additional)
New_For_nat_female_xo_team_2.update({
    "{en} national xzxz teams fifth tier": "منتخبات xzxz وطنية {female} من الدرجة الخامسة",
    "{en} national xzxz teams first tier": "منتخبات xzxz وطنية {female} من الدرجة الأولى",
    "{en} national xzxz teams fourth tier": "منتخبات xzxz وطنية {female} من الدرجة الرابعة",
    "{en} national xzxz teams premier": "منتخبات xzxz وطنية {female} من الدرجة الممتازة",
    "{en} national xzxz teams second tier": "منتخبات xzxz وطنية {female} من الدرجة الثانية",
    "{en} national xzxz teams seventh tier": "منتخبات xzxz وطنية {female} من الدرجة السابعة",
    "{en} national xzxz teams sixth tier": "منتخبات xzxz وطنية {female} من الدرجة السادسة",
    "{en} national xzxz teams third tier": "منتخبات xzxz وطنية {female} من الدرجة الثالثة",
    "{en} national xzxz teams top tier": "منتخبات xzxz وطنية {female} من الدرجة الأولى",
    "{en} xzxz teams fifth tier": "فرق xzxz {female} من الدرجة الخامسة",
    "{en} xzxz teams first tier": "فرق xzxz {female} من الدرجة الأولى",
    "{en} xzxz teams fourth tier": "فرق xzxz {female} من الدرجة الرابعة",
    "{en} xzxz teams premier": "فرق xzxz {female} من الدرجة الممتازة",
    "{en} xzxz teams second tier": "فرق xzxz {female} من الدرجة الثانية",
    "{en} xzxz teams seventh tier": "فرق xzxz {female} من الدرجة السابعة",
    "{en} xzxz teams sixth tier": "فرق xzxz {female} من الدرجة السادسة",
    "{en} xzxz teams third tier": "فرق xzxz {female} من الدرجة الثالثة",
    "{en} xzxz teams top tier": "فرق xzxz {female} من الدرجة الأولى"
})

both_bot = format_multi_data(
    New_For_nat_female_xo_team_2,
    Nat_women,
    key_placeholder="{en}",
    value_placeholder="{female}",
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
    "chairmen and investors": "رؤساء ومسيرو {lab}",
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
