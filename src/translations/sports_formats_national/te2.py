#!/usr/bin/python3
"""
!
"""
import re
from ...helps import len_print
from ..sports.sports_lists import LEVELS, AFTER_KEYS_NAT, NEW_TATO_NAT

sport_formts_enar_p17_jobs = {}
# ---
YEARS_LIST = [13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24]
# السنة الواحدة تساوي 45,560 مدخلة
# ---
team = "xzxz"
job_label = "xzxz"
# ---
New_For_nat_female_xo_team = {
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
# New_For_nat_female_xo_team["amateur xzxz championships"] =  "بطولة {nat} xzxz للهواة"
# New_For_nat_female_xo_team["youth xzxz championships"] =  "بطولة {nat} xzxz للشباب"
# New_For_nat_female_xo_team["men's xzxz championships"] =  "بطولة {nat} xzxz للرجال"
# New_For_nat_female_xo_team["women's xzxz championships"] =  "بطولة {nat} xzxz للسيدات"
# ---
# ---
for level, lvl_lab in LEVELS.items():
    New_For_nat_female_xo_team[f"national xzxz {level} league"] = f"دوريات xzxz {{nat}} وطنية من {lvl_lab}"
    New_For_nat_female_xo_team[f"national xzxz {level} leagues"] = f"دوريات xzxz {{nat}} وطنية من {lvl_lab}"

    New_For_nat_female_xo_team[f"defunct xzxz {level} league"] = f"دوريات xzxz {{nat}} سابقة من {lvl_lab}"
    New_For_nat_female_xo_team[f"defunct xzxz {level} leagues"] = f"دوريات xzxz {{nat}} سابقة من {lvl_lab}"

    New_For_nat_female_xo_team[f"{level} xzxz league"] = f"دوريات xzxz {{nat}} من {lvl_lab}"
    New_For_nat_female_xo_team[f"{level} xzxz leagues"] = f"دوريات xzxz {{nat}} من {lvl_lab}"
    New_For_nat_female_xo_team[f"xzxz {level} league"] = f"دوريات xzxz {{nat}} من {lvl_lab}"
    New_For_nat_female_xo_team[f"xzxz {level} leagues"] = f"دوريات xzxz {{nat}} من {lvl_lab}"
# ---
# ---
"""


new way to make keys 2024


&& indoor & outdoor &&
"""
# ---
nat_f = "{nat}"
New_For_nat_female_xo_team["women's xzxz"] = f"xzxz {nat_f} نسائية"
New_For_nat_female_xo_team["xzxz chairmen and investors"] = f"رؤساء ومسيرو xzxz {nat_f}"
New_For_nat_female_xo_team["defunct xzxz cup competitions"] = f"منافسات كؤوس xzxz {nat_f} سابقة"
New_For_nat_female_xo_team["xzxz cup competitions"] = f"منافسات كؤوس xzxz {nat_f}"
New_For_nat_female_xo_team["domestic xzxz cup"] = f"كؤوس xzxz {nat_f} محلية"
New_For_nat_female_xo_team["current xzxz seasons"] = f"مواسم xzxz {nat_f} حالية"
# ---

typies = {
    "cups": "كؤوس",
    "clubs": "أندية",
    "competitions": "منافسات",
    "leagues": "دوريات",
    "coaches": "مدربو",  # Category:Indoor soccer coaches in the United States by club
}

for en, ar in typies.items():
    New_For_nat_female_xo_team[f"xzxz {en}"] = f"{ar} xzxz {nat_f}"
    New_For_nat_female_xo_team[f"professional xzxz {en}"] = f"{ar} xzxz {nat_f} للمحترفين"
    New_For_nat_female_xo_team[f"defunct xzxz {en}"] = f"{ar} xzxz {nat_f} سابقة"
    New_For_nat_female_xo_team[f"domestic xzxz {en}"] = f"{ar} xzxz محلية {nat_f}"
    New_For_nat_female_xo_team[f"domestic women's xzxz {en}"] = f"{ar} xzxz محلية {nat_f} للسيدات"

    New_For_nat_female_xo_team[f"domestic xzxz {en}"] = f"{ar} xzxz {nat_f} محلية"
    New_For_nat_female_xo_team[f"indoor xzxz {en}"] = f"{ar} xzxz {nat_f} داخل الصالات"
    New_For_nat_female_xo_team[f"outdoor xzxz {en}"] = f"{ar} xzxz {nat_f} في الهواء الطلق"
    New_For_nat_female_xo_team[f"defunct indoor xzxz {en}"] = f"{ar} xzxz {nat_f} داخل الصالات سابقة"
    New_For_nat_female_xo_team[f"defunct outdoor xzxz {en}"] = f"{ar} xzxz {nat_f} في الهواء الطلق سابقة"
# ---
# ---
# indoor & outdoor
# tab[Category:Canadian domestic Soccer] = "تصنيف:كرة قدم كندية محلية"
New_For_nat_female_xo_team["domestic xzxz"] = f"xzxz {nat_f} محلية"
New_For_nat_female_xo_team["indoor xzxz"] = f"xzxz {nat_f} داخل الصالات"
New_For_nat_female_xo_team["outdoor xzxz"] = f"xzxz {nat_f} في الهواء الطلق"
New_For_nat_female_xo_team["national women's xzxz teams"] = "منتخبات xzxz وطنية نسائية {nat}"
New_For_nat_female_xo_team["national xzxz teams"] = "منتخبات xzxz وطنية {nat}"
# ---
New_For_nat_female_xo_team["reserve xzxz teams"] = "فرق xzxz احتياطية {nat}"
New_For_nat_female_xo_team["defunct xzxz teams"] = "فرق xzxz سابقة {nat}"
# ---
New_For_nat_female_xo_team["national a' xzxz teams"] = "منتخبات xzxz محليين {nat}"
New_For_nat_female_xo_team["national b xzxz teams"] = "منتخبات xzxz رديفة {nat}"
New_For_nat_female_xo_team["national reserve xzxz teams"] = "منتخبات xzxz وطنية احتياطية {nat}"
# ---
Att2 = "فرق xzxz {nat}"
for ty_nat, tas in NEW_TATO_NAT.items():
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
    for pr_e, pr_e_Lab in AFTER_KEYS_NAT.items():
        if pr_e in ["players", "playerss"] and "women's" in ty_nat:
            pr_e_Lab = "لاعبات {lab}"
        elif "لاعبو" in pr_e_Lab and "women's" in ty_nat:
            pr_e_Lab = re.sub(r"لاعبو ", "لاعبات ", pr_e_Lab)
        Ab = f"{ty_nat} xzxz teams {pr_e}"
        Ab = Ab.strip()
        New_For_nat_female_xo_team[Ab] = pr_e_Lab.format(lab=Ar_labs)
    New_For_nat_female_xo_team[f"{ty_nat} teams"] = Att2

len_print.data_len(
    "sports_formats_national/te2.py",
    {
        "New_For_nat_female_xo_team": New_For_nat_female_xo_team,
    },
)
