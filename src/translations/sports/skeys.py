#!/usr/bin/python3
"""
Comprehensive sport template dictionaries used throughout the project.
"""

from typing import Final

from ...helps import len_print
from .Sport_key import SPORTS_KEYS_FOR_LABEL, SPORTS_KEYS_FOR_TEAM

COUNTRY_PLACEHOLDER: Final[str] = "{}"
NAT_PLACEHOLDER: Final[str] = "{nat}"

SPORT_FORMTS_MALE_NAT = {}  # الإنجليزي جنسية والعربي جنسية
SPORT_FORMTS_FEMALE_NAT = {}  # الإنجليزي جنسية والعربي جنسية
SPORT_FORMTS_EN_P17_AR_NAT = {}  # الإنجليزي إسم البلد والعربي جنسية
SPORT_FORMTS_EN_AR_IS_P17 = {}  # الإنجليزي إسم البلد والعربي يكون اسم البلد
SPORT_FORMTS_NEW_KKK = {}  # الإنجليزي جنسية والعربي اسم البلد

YEARS_LIST = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]
# السنة الواحدة تساوي 45,560 مدخلة

# قبل تعديل national
# sports.py: len:"SPORT_FORMTS_FEMALE_NAT":  1359170  , len:"SPORT_FORMTS_EN_AR_IS_P17":  1359224  , len:"Teams new":  1496011
# بعد التعديل
# sports.py: len:"SPORT_FORMTS_FEMALE_NAT":  559982  , len:"SPORT_FORMTS_EN_AR_IS_P17":  564640  , len:"Teams new":  696189

# YEARS_LIST = [18]

# SPORT_FORMTS_EN_AR_IS_P17#Sports_Format_en_is_P17_ar_P17
# SPORT_FORMTS_FEMALE_NAT

Teams = {
    "national sports teams": "منتخبات رياضية وطنية",
    "national teams": "منتخبات وطنية",
    "teams": "فرق",
    "sports teams": "فرق رياضية",
    "football clubs": "أندية كرة قدم",
    "clubs": "أندية",
}

SPORT_FORMTS_EN_AR_IS_P17["international rules football team"] = "منتخب {} لكرة القدم الدولية"

SPORT_FORMTS_EN_AR_IS_P17["cup"] = "كأس {}"
SPORT_FORMTS_EN_AR_IS_P17["presidents"] = "رؤساء {}"
SPORT_FORMTS_EN_AR_IS_P17["territorial officials"] = "مسؤولو أقاليم {}"
SPORT_FORMTS_EN_AR_IS_P17["territorial judges"] = "قضاة أقاليم {}"
SPORT_FORMTS_EN_AR_IS_P17["war"] = "حرب {}"
# SPORT_FORMTS_EN_AR_IS_P17["responses"] = "استجابات {}"
# SPORT_FORMTS_EN_AR_IS_P17["courts"] = "محاكم {}"

# association football clubs
# Category:Zimbabwe men's A' international footballers
# SPORT_FORMTS_EN_AR_IS_P17[modifier + "A' international footballers"] = Lab + " للمحليين"
# SPORT_FORMTS_EN_AR_IS_P17[modifier + "B international footballers"] = Lab + " الرديف"

sport_starts = {
    "": "",
    "men's a' ": " للرجال للمحليين",
    "men's b ": " الرديف للرجال",
    "men's ": " للرجال",
    "women's ": " للسيدات",
    "men's youth ": " للشباب",
    "women's youth ": " للشابات",
    # "professional " : " للمحترفين",
    "amateur ": " للهواة",
    "youth ": " للشباب",
}

for sport, label in SPORTS_KEYS_FOR_LABEL.items():
    # SPORT_FORMTS_FEMALE_NAT["%s tour" % sport.lower()] = "بطولة %s {nat}" % label
    # SPORT_FORMTS_FEMALE_NAT["%s tournament" % sport.lower()] = "بطولة %s {nat}" % label

    SPORT_FORMTS_MALE_NAT[f"{sport.lower()} super league"] = f"دوري السوبر {label} {COUNTRY_PLACEHOLDER}"

    # 12 سطر x 666 len(SPORTS_KEYS_FOR_LABEL) = 7,992

    # tab[Category:yemeni professional Soccer League] = "تصنيف:دوري كرة القدم اليمني للمحترفين"
    SPORT_FORMTS_MALE_NAT[f"professional {sport.lower()} league"] = f"دوري {label} {COUNTRY_PLACEHOLDER} للمحترفين"

    # tab[Category:American Indoor Soccer] = "تصنيف:كرة القدم الأمريكية داخل الصالات"
    SPORT_FORMTS_FEMALE_NAT[f"outdoor {sport.lower()}"] = f"{label} {COUNTRY_PLACEHOLDER} في الهواء الطلق"
    SPORT_FORMTS_FEMALE_NAT[f"indoor {sport.lower()}"] = f"{label} {COUNTRY_PLACEHOLDER} داخل الصالات"


for year in YEARS_LIST:
    SPORT_FORMTS_EN_AR_IS_P17[f"under-{year} international managers"] = f"مدربو تحت {year} سنة دوليون من {COUNTRY_PLACEHOLDER}"
    SPORT_FORMTS_EN_AR_IS_P17[f"under-{year} international players"] = f"لاعبو تحت {year} سنة دوليون من {COUNTRY_PLACEHOLDER}"
    SPORT_FORMTS_EN_AR_IS_P17[f"under-{year} international playerss"] = f"لاعبو تحت {year} سنة دوليون من {COUNTRY_PLACEHOLDER}"

for modifier, modifier_label in sport_starts.items():
    # SPORT_FORMTS_EN_AR_IS_P17["international footballers"] = "لاعبو منتخب {} لكرة القدم"

    start = "لاعبات منتخب" if "women's" in modifier else "لاعبو منتخب"

    Lab = f"{start} {COUNTRY_PLACEHOLDER} لكرة القدم {modifier_label}"

    SPORT_FORMTS_EN_AR_IS_P17[modifier + "international footballers"] = Lab
    SPORT_FORMTS_EN_AR_IS_P17[modifier + "international footballers"] = Lab
    SPORT_FORMTS_EN_AR_IS_P17[modifier + "international soccer players"] = Lab
    SPORT_FORMTS_EN_AR_IS_P17[modifier + "international soccer playerss"] = Lab
    # print("lab = " + Lab)
    # print(modifier + " B international footballers")

    # Category:Australia under-18 international soccer players
    # تصنيف:لاعبو منتخب أستراليا تحت 18 سنة لكرة القدم

    # Category:Zimbabwe men's A' international footballers
    # Category:Belgian men's international footballers

    for year in YEARS_LIST:
        Lab3 = f"{start} {COUNTRY_PLACEHOLDER} تحت {year} سنة لكرة القدم {modifier_label}"
        SPORT_FORMTS_EN_AR_IS_P17[f"{modifier}under-{year} international footballers"] = Lab3
        SPORT_FORMTS_EN_AR_IS_P17[f"{modifier}under-{year} international soccer players"] = Lab3
        SPORT_FORMTS_EN_AR_IS_P17[f"{modifier}under-{year} international soccer playerss"] = Lab3

SPORT_FORMTS_EN_AR_IS_P17["rally championship"] = "بطولة {nat} للراليات"
SPORT_FORMTS_EN_AR_IS_P17["war and conflict"] = "حروب ونزاعات {nat}"
SPORT_FORMTS_EN_AR_IS_P17["governorate"] = "حكومة {nat}"

SPORT_FORMTS_EN_AR_IS_P17["sports templates"] = "قوالب {} الرياضية"
SPORT_FORMTS_EN_AR_IS_P17["national team"] = "منتخبات {} الوطنية"
SPORT_FORMTS_EN_AR_IS_P17["national teams"] = "منتخبات {} الوطنية"
SPORT_FORMTS_EN_AR_IS_P17["national football team managers"] = "مدربو منتخب {} لكرة القدم"

# فرق دول وطنية
# SPORTS_KEYS_FOR_TEAM = {}
# SPORTS_KEYS_FOR_TEAM["association football"] = "لكرة القدم"

for team2 in SPORTS_KEYS_FOR_TEAM:
    team2_lab = SPORTS_KEYS_FOR_TEAM[team2]

    SPORT_FORMTS_EN_P17_AR_NAT[f"{team2} federation"] = f"الاتحاد {NAT_PLACEHOLDER} {team2_lab}"

    # Middle East Rally Championship بطولة الشرق الأوسط للراليات

    # SPORT_FORMTS_FEMALE_NAT["women's %s league" % team] = f"الدوري {NAT_PLACEHOLDER} {team2_lab} للسيدات"

    # SPORT_FORMTS_MALE_NAT[f"professional {team2.lower()} league"] = f"دوري {team2_lab} {COUNTRY_PLACEHOLDER} للمحترفين"
    SPORT_FORMTS_MALE_NAT[f"{team2.lower()} federation"] = f"الاتحاد {COUNTRY_PLACEHOLDER} {team2_lab}"

    SPORT_FORMTS_MALE_NAT[f"{team2.lower()} league"] = f"الدوري {COUNTRY_PLACEHOLDER} {team2_lab}"

    SPORT_FORMTS_MALE_NAT[f"women's {team2.lower()} league"] = f"الدوري {COUNTRY_PLACEHOLDER} {team2_lab} للسيدات"
    SPORT_FORMTS_MALE_NAT[f"{team2.lower()} league administrators"] = f"مدراء الدوري {COUNTRY_PLACEHOLDER} {team2_lab}"
    SPORT_FORMTS_MALE_NAT[f"{team2.lower()} league players"] = f"لاعبو الدوري {COUNTRY_PLACEHOLDER} {team2_lab}"
    SPORT_FORMTS_MALE_NAT[f"{team2.lower()} league playerss"] = f"لاعبو الدوري {COUNTRY_PLACEHOLDER} {team2_lab}"

    # tab[Category:American Indoor Soccer League coaches] = "تصنيف:مدربو الدوري الأمريكي لكرة القدم داخل الصالات"
    SPORT_FORMTS_MALE_NAT[f"indoor {team2.lower()} league"] = f"الدوري {COUNTRY_PLACEHOLDER} {team2_lab} داخل الصالات"
    SPORT_FORMTS_MALE_NAT[f"outdoor {team2.lower()} league"] = f"الدوري {COUNTRY_PLACEHOLDER} {team2_lab} في الهواء الطلق"

    # tab[Category:Canadian Major Indoor Soccer League seasons] = "تصنيف:مواسم الدوري الرئيسي الكندي لكرة القدم داخل الصالات"
    SPORT_FORMTS_MALE_NAT[f"major indoor {team2.lower()} league"] = f"الدوري الرئيسي {COUNTRY_PLACEHOLDER} {team2_lab} داخل الصالات"

    # Category:National junior women's goalball teams

    SPORT_FORMTS_NEW_KKK[f"men's {team2} cup"] = f"كأس {COUNTRY_PLACEHOLDER} {team2_lab} للرجال"
    SPORT_FORMTS_NEW_KKK[f"women's {team2} cup"] = f"كأس {COUNTRY_PLACEHOLDER} {team2_lab} للسيدات"
    SPORT_FORMTS_NEW_KKK[f"{team2} cup"] = f"كأس {COUNTRY_PLACEHOLDER} {team2_lab}"
    SPORT_FORMTS_NEW_KKK[f"national junior men's {team2} team"] = f"منتخب {COUNTRY_PLACEHOLDER} {team2_lab} للناشئين"
    SPORT_FORMTS_NEW_KKK[f"national junior {team2} team"] = f"منتخب {COUNTRY_PLACEHOLDER} {team2_lab} للناشئين"
    SPORT_FORMTS_NEW_KKK[f"national {team2} team"] = f"منتخب {COUNTRY_PLACEHOLDER} " + team2_lab
    SPORT_FORMTS_NEW_KKK[f"national women's {team2} team"] = f"منتخب {COUNTRY_PLACEHOLDER} {team2_lab} للسيدات"

    # SPORT_FORMTS_NEW_KKK[f"women's {team} league"] = f"الدوري {COUNTRY_PLACEHOLDER} {team2_lab} للسيدات"

    SPORT_FORMTS_NEW_KKK[f"national men's {team2} team"] = f"منتخب {COUNTRY_PLACEHOLDER} {team2_lab} للرجال"

# SPORT_FORMTS_FEMALE_NAT["competitors"] = "منافسون {nat}"

SPORT_FORMTS_EN_AR_IS_P17["international rally"] = f"رالي {COUNTRY_PLACEHOLDER} الدولي"

len_print.data_len(
    "sports/skeys.py",
    {
        "SPORT_FORMTS_EN_AR_IS_P17": SPORT_FORMTS_EN_AR_IS_P17,
        "SPORT_FORMTS_FEMALE_NAT": SPORT_FORMTS_FEMALE_NAT,
        "SPORT_FORMTS_MALE_NAT": SPORT_FORMTS_MALE_NAT,
        "SPORT_FORMTS_NEW_KKK": SPORT_FORMTS_NEW_KKK,
        "SPORT_FORMTS_EN_P17_AR_NAT": SPORT_FORMTS_EN_P17_AR_NAT,
    },
)

__all__ = [
    "SPORT_FORMTS_EN_AR_IS_P17",
    "SPORT_FORMTS_EN_P17_AR_NAT",
    "SPORT_FORMTS_FEMALE_NAT",
    "SPORT_FORMTS_MALE_NAT",
    "SPORT_FORMTS_NEW_KKK",
]
