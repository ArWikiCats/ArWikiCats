#!/usr/bin/python3
"""

"""
from ...helps import len_print
from .sports_lists import nat_menstt33, New_Tato_nat
from ..sports_formats_teams.team_job import sf_en_ar_is_p17
from .Sport_key import Sports_Keys_For_Label, Sports_Keys_For_Team

sport_formts_male_nat = {}  # الإنجليزي جنسية والعربي جنسية
sport_formts_female_nat = {}  # الإنجليزي جنسية والعربي جنسية
sport_formts_en_p17_ar_nat = {}  # الإنجليزي إسم البلد والعربي جنسية
sport_formts_en_ar_is_p17 = {}  # الإنجليزي إسم البلد والعربي يكون اسم البلد
sport_formts_new_kkk = {}  # الإنجليزي جنسية والعربي اسم البلد
# ---
sport_formts_enar_p17_team = {}
# ---
# مستخدمة في ملفات أخرى عبر هذا الملف
# ---
sport_formts_en_ar_is_p17.update(sf_en_ar_is_p17)
# ---
YEARS_LIST = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]
# السنة الواحدة تساوي 45,560 مدخلة
# ---
# قبل تعديل national
# sports.py: len:"sport_formts_female_nat":  1359170  , len:"sport_formts_en_ar_is_p17":  1359224  , len:"Teams new":  1496011
# بعد التعديل
# sports.py: len:"sport_formts_female_nat":  559982  , len:"sport_formts_en_ar_is_p17":  564640  , len:"Teams new":  696189
# ---
# YEARS_LIST = [18]
# ---
# sport_formts_en_ar_is_p17#Sports_Format_en_is_P17_ar_P17
# sport_formts_female_nat
# ---
Teams = {
    "national sports teams": "منتخبات رياضية وطنية",
    "national teams": "منتخبات وطنية",
    "teams": "فرق",
    "sports teams": "فرق رياضية",
    "football clubs": "أندية كرة قدم",
    "clubs": "أندية",
}
# ---
sport_formts_en_ar_is_p17["international rules football team"] = "منتخب {} لكرة القدم الدولية"
# ---
sport_formts_en_ar_is_p17["cup"] = "كأس {}"
sport_formts_en_ar_is_p17["presidents"] = "رؤساء {}"
sport_formts_en_ar_is_p17["territorial officials"] = "مسؤولو أقاليم {}"
sport_formts_en_ar_is_p17["territorial judges"] = "قضاة أقاليم {}"
sport_formts_en_ar_is_p17["war"] = "حرب {}"
# sport_formts_en_ar_is_p17["responses"] = "استجابات {}"
# sport_formts_en_ar_is_p17["courts"] = "محاكم {}"
# ---
# ---association football clubs
# Category:Zimbabwe men's A' international footballers
# sport_formts_en_ar_is_p17[modifier + "A' international footballers"] = Lab + " للمحليين"
# sport_formts_en_ar_is_p17[modifier + "B international footballers"] = Lab + " الرديف"
# ---
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
# ---
PLACE_HOLDER = "{}"
# ---
for sport, label in Sports_Keys_For_Label.items():
    # ---
    # sport_formts_female_nat["%s tour" % sport.lower()] = "بطولة %s {nat}" % label
    # sport_formts_female_nat["%s tournament" % sport.lower()] = "بطولة %s {nat}" % label
    # ---
    sport_formts_male_nat[f"{sport.lower()} super league"] = f"دوري السوبر {label} {PLACE_HOLDER}"
    # ---
    # 12 سطر x 666 len(Sports_Keys_For_Label) = 7,992
    # ---
    # tab[Category:yemeni professional Soccer League] = "تصنيف:دوري كرة القدم اليمني للمحترفين"
    sport_formts_male_nat[f"professional {sport.lower()} league"] = f"دوري {label} {PLACE_HOLDER} للمحترفين"
    # ---
    # tab[Category:American Indoor Soccer] = "تصنيف:كرة القدم الأمريكية داخل الصالات"
    sport_formts_female_nat[f"outdoor {sport.lower()}"] = f"{label} {PLACE_HOLDER} في الهواء الطلق"
    sport_formts_female_nat[f"indoor {sport.lower()}"] = f"{label} {PLACE_HOLDER} داخل الصالات"
    # ---
# ---
for year in YEARS_LIST:
    sport_formts_en_ar_is_p17[f"under-{year} international managers"] = f"مدربو تحت {year} سنة دوليون من {PLACE_HOLDER}"
    sport_formts_en_ar_is_p17[f"under-{year} international players"] = f"لاعبو تحت {year} سنة دوليون من {PLACE_HOLDER}"
    sport_formts_en_ar_is_p17[f"under-{year} international playerss"] = f"لاعبو تحت {year} سنة دوليون من {PLACE_HOLDER}"
# ---
for modifier, modifier_label in sport_starts.items():
    # sport_formts_en_ar_is_p17["international footballers"] = "لاعبو منتخب {} لكرة القدم"
    # ---
    start = "لاعبات منتخب" if modifier.find("women's") != -1 else "لاعبو منتخب"
    # ---
    Lab = f"{start} {PLACE_HOLDER} لكرة القدم {modifier_label}"
    # ---
    sport_formts_en_ar_is_p17[modifier + "international footballers"] = Lab
    sport_formts_en_ar_is_p17[modifier + "international footballers"] = Lab
    sport_formts_en_ar_is_p17[modifier + "international soccer players"] = Lab
    sport_formts_en_ar_is_p17[modifier + "international soccer playerss"] = Lab
    # print("lab = " + Lab)
    # print(modifier + " B international footballers")
    # ---
    # Category:Australia under-18 international soccer players
    # تصنيف:لاعبو منتخب أستراليا تحت 18 سنة لكرة القدم
    # ---
    # Category:Zimbabwe men's A' international footballers
    # Category:Belgian men's international footballers
    # ---
    for year in YEARS_LIST:
        Lab3 = f"{start} {PLACE_HOLDER} تحت {year} سنة لكرة القدم {modifier_label}"
        sport_formts_en_ar_is_p17[f"{modifier}under-{year} international footballers"] = Lab3
        sport_formts_en_ar_is_p17[f"{modifier}under-{year} international soccer players"] = Lab3
        sport_formts_en_ar_is_p17[f"{modifier}under-{year} international soccer playerss"] = Lab3
# ---
sport_formts_en_ar_is_p17["rally championship"] = "بطولة {nat} للراليات"
sport_formts_en_ar_is_p17["war and conflict"] = "حروب ونزاعات {nat}"
sport_formts_en_ar_is_p17["governorate"] = "حكومة {nat}"
# ---
sport_formts_en_ar_is_p17["sports templates"] = "قوالب {} الرياضية"
sport_formts_en_ar_is_p17["national team"] = "منتخبات {} الوطنية"
sport_formts_en_ar_is_p17["national teams"] = "منتخبات {} الوطنية"
sport_formts_en_ar_is_p17["national football team managers"] = "مدربو منتخب {} لكرة القدم"
# ---
# فرق دول وطنية
# Sports_Keys_For_Team = {}
# Sports_Keys_For_Team["association football"] = "لكرة القدم"
# ---
for team2 in Sports_Keys_For_Team:
    team2_lab = Sports_Keys_For_Team[team2]
    # ---
    nat_f = "{nat}"
    # ---
    sport_formts_en_p17_ar_nat[f"{team2} federation"] = f"الاتحاد {nat_f} {team2_lab}"
    # ---
    # Middle East Rally Championship بطولة الشرق الأوسط للراليات
    # ---
    # sport_formts_female_nat["women's %s league" % team] = f"الدوري {nat_f} {team2_lab} للسيدات"
    # ---
    # sport_formts_male_nat[f"professional {team2.lower()} league"] = f"دوري {team2_lab} {PLACE_HOLDER} للمحترفين"
    sport_formts_male_nat[f"{team2.lower()} federation"] = f"الاتحاد {PLACE_HOLDER} {team2_lab}"
    # ---
    sport_formts_male_nat[f"{team2.lower()} league"] = f"الدوري {PLACE_HOLDER} {team2_lab}"
    # ---

    sport_formts_male_nat[f"women's {team2.lower()} league"] = f"الدوري {PLACE_HOLDER} {team2_lab} للسيدات"
    sport_formts_male_nat[f"{team2.lower()} league administrators"] = f"مدراء الدوري {PLACE_HOLDER} {team2_lab}"
    sport_formts_male_nat[f"{team2.lower()} league players"] = f"لاعبو الدوري {PLACE_HOLDER} {team2_lab}"
    sport_formts_male_nat[f"{team2.lower()} league playerss"] = f"لاعبو الدوري {PLACE_HOLDER} {team2_lab}"
    # ---
    # tab[Category:American Indoor Soccer League coaches] = "تصنيف:مدربو الدوري الأمريكي لكرة القدم داخل الصالات"
    sport_formts_male_nat[f"indoor {team2.lower()} league"] = f"الدوري {PLACE_HOLDER} {team2_lab} داخل الصالات"
    sport_formts_male_nat[f"outdoor {team2.lower()} league"] = f"الدوري {PLACE_HOLDER} {team2_lab} في الهواء الطلق"
    # ---
    # tab[Category:Canadian Major Indoor Soccer League seasons] = "تصنيف:مواسم الدوري الرئيسي الكندي لكرة القدم داخل الصالات"
    sport_formts_male_nat[f"major indoor {team2.lower()} league"] = f"الدوري الرئيسي {PLACE_HOLDER} {team2_lab} داخل الصالات"

    # Category:National junior women's goalball teams
    # ---
    sport_formts_new_kkk[f"men's {team2} cup"] = f"كأس {PLACE_HOLDER} {team2_lab} للرجال"
    sport_formts_new_kkk[f"women's {team2} cup"] = f"كأس {PLACE_HOLDER} {team2_lab} للسيدات"
    sport_formts_new_kkk[f"{team2} cup"] = f"كأس {PLACE_HOLDER} {team2_lab}"
    sport_formts_new_kkk[f"national junior men's {team2} team"] = f"منتخب {PLACE_HOLDER} {team2_lab} للناشئين"
    sport_formts_new_kkk[f"national junior {team2} team"] = f"منتخب {PLACE_HOLDER} {team2_lab} للناشئين"
    sport_formts_new_kkk[f"national {team2} team"] = f"منتخب {PLACE_HOLDER} " + team2_lab
    sport_formts_new_kkk[f"national women's {team2} team"] = f"منتخب {PLACE_HOLDER} {team2_lab} للسيدات"
    # ---
    # sport_formts_new_kkk[f"women's {team} league"] = f"الدوري {PLACE_HOLDER} {team2_lab} للسيدات"
    # ---
    sport_formts_new_kkk[f"national men's {team2} team"] = f"منتخب {PLACE_HOLDER} {team2_lab} للرجال"
    # ---
# sport_formts_female_nat["competitors"] = "منافسون {nat}"

sport_formts_en_ar_is_p17["international rally"] = f"رالي {PLACE_HOLDER} الدولي"
# ---
len_print.data_len("sports/skeys.py", {
    "sport_formts_en_ar_is_p17": sport_formts_en_ar_is_p17,
    "sport_formts_enar_p17_team": sport_formts_enar_p17_team,
    "sport_formts_female_nat": sport_formts_female_nat,
    "sport_formts_male_nat": sport_formts_male_nat,
    "sport_formts_new_kkk": sport_formts_new_kkk,
    "sport_formts_en_p17_ar_nat": sport_formts_en_p17_ar_nat,
    "nat_menstt33": nat_menstt33,
    "New_Tato_nat": New_Tato_nat,
})

__all__ = [
    "sport_formts_en_ar_is_p17",
    "sport_formts_en_p17_ar_nat",
    "sport_formts_enar_p17_team",
    "sport_formts_new_kkk",
    "sport_formts_male_nat",
    "sport_formts_female_nat",
]
