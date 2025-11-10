#!/usr/bin/python3
"""

"""
from ...helps import len_print
from .sports_lists import nat_menstt33, New_Tato_nat
from ..sports_formats_teams.team_job import sf_en_ar_is_p17
from .Sport_key import Sports_Keys_For_Label, Sports_Keys_For_Team, Sports_Keys_For_Jobs

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
Years_List = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]
# السنة الواحدة تساوي 45,560 مدخلة
# ---
# قبل تعديل national
# sports.py: len:"sport_formts_female_nat":  1359170  , len:"sport_formts_en_ar_is_p17":  1359224  , len:"Teams new":  1496011
# بعد التعديل
# sports.py: len:"sport_formts_female_nat":  559982  , len:"sport_formts_en_ar_is_p17":  564640  , len:"Teams new":  696189
# ---
# Sports_Keys_For_Jobs["judo"] = "جودو"
# ---
# Years_List = [18]
# Sports_Keys_For_Jobs = {}
# Sports_Keys_For_Jobs["association football"] = "هوكي جليد"
# ---
Sports_Keys_For_Jobs["sports"] = "رياضية"
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
# sport_formts_en_ar_is_p17[ttt + "A' international footballers"] = Lab + " للمحليين"
# sport_formts_en_ar_is_p17[ttt + "B international footballers"] = Lab + " الرديف"
# ---
menstts = {
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
for mem, labe in Sports_Keys_For_Label.items():
    # ---
    # sport_formts_female_nat["%s tour" % mem.lower()] = "بطولة %s {nat}" % labe
    # sport_formts_female_nat["%s tournament" % mem.lower()] = "بطولة %s {nat}" % labe
    # ---
    emty_f = "{}"
    # ---
    sport_formts_male_nat[f"{mem.lower()} super league"] = "دوري السوبر %s {}" % labe
    # ---
    # 12 سطر x 666 len(Sports_Keys_For_Label) = 7,992
    # ---
    # tab[Category:yemeni professional Soccer League] = "تصنيف:دوري كرة القدم اليمني للمحترفين"
    sport_formts_male_nat[f"professional {mem.lower()} league"] = f"دوري {labe} {emty_f} للمحترفين"
    # ---
    # tab[Category:American Indoor Soccer] = "تصنيف:كرة القدم الأمريكية داخل الصالات"
    sport_formts_female_nat[f"outdoor {mem.lower()}"] = f"{labe} {emty_f} في الهواء الطلق"
    sport_formts_female_nat[f"indoor {mem.lower()}"] = f"{labe} {emty_f} داخل الصالات"
    # ---
# ---
for year in Years_List:
    sport_formts_en_ar_is_p17["under-%d international managers" % (year)] = "مدربو تحت %d سنة دوليون من {}" % year
    sport_formts_en_ar_is_p17["under-%d international players" % (year)] = "لاعبو تحت %d سنة دوليون من {}" % year
    sport_formts_en_ar_is_p17["under-%d international playerss" % (year)] = "لاعبو تحت %d سنة دوليون من {}" % year
# ---
for ttt in menstts:
    # sport_formts_en_ar_is_p17["international footballers"] = "لاعبو منتخب {} لكرة القدم"
    start = "لاعبو منتخب"
    if ttt.find("women's") != -1:
        start = "لاعبات منتخب"
    Lab = start + " {} " + "لكرة القدم " + menstts[ttt]
    # ---
    sport_formts_en_ar_is_p17[ttt + "international footballers"] = Lab
    sport_formts_en_ar_is_p17[ttt + "international footballers"] = Lab
    sport_formts_en_ar_is_p17[ttt + "international soccer players"] = Lab
    sport_formts_en_ar_is_p17[ttt + "international soccer playerss"] = Lab
    # print("lab = " + Lab)
    # print(ttt + " B international footballers")
    # ---
    # Category:Australia under-18 international soccer players
    # تصنيف:لاعبو منتخب أستراليا تحت 18 سنة لكرة القدم
    # ---
    # Category:Zimbabwe men's A' international footballers
    # Category:Belgian men's international footballers
    # ---
    Lab2 = start + " {} تحت %d سنة " + "لكرة القدم " + menstts[ttt]
    for year in Years_List:
        Lab3 = Lab2 % year
        # print("lab3 = " + Lab3)
        sport_formts_en_ar_is_p17[ttt + "under-%d international footballers" % (year)] = Lab3
        sport_formts_en_ar_is_p17[ttt + "under-%d international soccer players" % (year)] = Lab3
        sport_formts_en_ar_is_p17[ttt + "under-%d international soccer playerss" % (year)] = Lab3
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
    emty_f = "{}"
    # ---
    # sport_formts_male_nat[f"professional {team2.lower()} league"] = f"دوري {team2_lab} {emty_f} للمحترفين"
    sport_formts_male_nat[f"{team2.lower()} federation"] = f"الاتحاد {emty_f} {team2_lab}"
    # ---
    sport_formts_male_nat[f"{team2.lower()} league"] = f"الدوري {emty_f} {team2_lab}"
    # ---

    sport_formts_male_nat[f"women's {team2.lower()} league"] = f"الدوري {emty_f} %s للسيدات" % team2_lab
    sport_formts_male_nat[f"{team2.lower()} league administrators"] = f"مدراء الدوري {emty_f} {team2_lab}"
    sport_formts_male_nat[f"{team2.lower()} league players"] = f"لاعبو الدوري {emty_f} {team2_lab}"
    sport_formts_male_nat[f"{team2.lower()} league playerss"] = f"لاعبو الدوري {emty_f} {team2_lab}"
    # ---
    # tab[Category:American Indoor Soccer League coaches] = "تصنيف:مدربو الدوري الأمريكي لكرة القدم داخل الصالات"
    sport_formts_male_nat[f"indoor {team2.lower()} league"] = f"الدوري {emty_f} {team2_lab} داخل الصالات"
    sport_formts_male_nat[f"outdoor {team2.lower()} league"] = f"الدوري {emty_f} {team2_lab} في الهواء الطلق"
    # ---
    # tab[Category:Canadian Major Indoor Soccer League seasons] = "تصنيف:مواسم الدوري الرئيسي الكندي لكرة القدم داخل الصالات"
    sport_formts_male_nat[f"major indoor {team2.lower()} league"] = f"الدوري الرئيسي {emty_f} {team2_lab} داخل الصالات"

    # Category:National junior women's goalball teams
    # ---
    sport_formts_new_kkk[f"men's {team2} cup"] = "كأس {} %s للرجال" % team2_lab
    sport_formts_new_kkk[f"women's {team2} cup"] = "كأس {} %s للسيدات" % team2_lab
    sport_formts_new_kkk[f"{team2} cup"] = "كأس {} %s" % team2_lab
    sport_formts_new_kkk[f"national junior men's {team2} team"] = "منتخب {} " + team2_lab + " للناشئين"
    sport_formts_new_kkk[f"national junior {team2} team"] = "منتخب {} " + team2_lab + " للناشئين"
    sport_formts_new_kkk[f"national {team2} team"] = "منتخب {} " + team2_lab
    sport_formts_new_kkk[f"national women's {team2} team"] = "منتخب {} " + team2_lab + " للسيدات"
    # ---
    # sport_formts_new_kkk["women's %s league" % team] = "الدوري {} %s للسيدات" % team2_lab
    # ---
    sport_formts_new_kkk[f"national men's {team2} team"] = "منتخب {} " + team2_lab + " للرجال"
    # ---
# sport_formts_female_nat["competitors"] = "منافسون {nat}"

sport_formts_en_ar_is_p17["international rally"] = "رالي {} الدولي"
# ---
Lenth1 = {
    "sport_formts_en_ar_is_p17": sport_formts_en_ar_is_p17,
    "sport_formts_enar_p17_team": sport_formts_enar_p17_team,
    "sport_formts_female_nat": sport_formts_female_nat,
    "sport_formts_male_nat": sport_formts_male_nat,
    "sport_formts_new_kkk": sport_formts_new_kkk,
    "sport_formts_en_p17_ar_nat": sport_formts_en_p17_ar_nat,
    "nat_menstt33": nat_menstt33,
    "New_Tato_nat": New_Tato_nat,
}
# ---
len_print.data_len("sports.py", Lenth1)
# sport_formts_female_nat["road cycling"] = "سباقات {nat} للدراجات على الطريق"
# ---
Facos = [
    "china women's national football team",
    "women's football competitions in china",
    "expatriate women's footballers in china",
    "chinese women's footballers",
    "women's football leagues in china",
    "women's football in china",
]
# Nat_Womens#Nat_mens

__all__ = [
    "sport_formts_en_ar_is_p17",
    "sport_formts_en_p17_ar_nat",
    "sport_formts_enar_p17_team",
    "sport_formts_new_kkk",
    "sport_formts_male_nat",
    "sport_formts_female_nat",
]
