#!/usr/bin/python3
"""
# from .india_2 import Main_Table_2

"""

from pathlib import Path
import json

Dir2 = Path(__file__).parent
# ---
India_dd = {}
popopo = {}
Main_Table_2 = {}
India_Main_Table = {}
# India_districts = {}
# India_Citiese = {}
# ---
with open(f"{Dir2}/jsons/India_dd.json", "r", encoding="utf-8") as f:
    India_dd = json.load(f)
# ---
for dd, dd_lab in India_dd.items():
    dd2 = dd.lower()
    India_Main_Table[dd2] = dd_lab
    # ---
    # India_districts[f"{dd2} district"] = f"مقاطعة {dd_lab}"
    # India_Citiese[dd] = dd_lab
    # ---
    India_Main_Table[f"{dd2} district"] = f"مقاطعة {dd_lab}"
    # ---
# ---
del India_dd
# ---
with open(f"{Dir2}/jsons/popopo.json", "r", encoding="utf-8") as f:
    popopo = json.load(f)
# ---
Egypht_t = {
    "alexandria": "الإسكندرية",
    "aswan": "أسوان",
    "asyut": "أسيوط",
    "beheira": "البحيرة",
    "beni suef": "بني سويف",
    "cairo": "القاهرة",
    "dakahlia": "الدقهلية",
    "damietta": "دمياط",
    "faiyum": "الفيوم",
    "gharbia": "الغربية",
    "giza": "الجيزة",
    "ismailia": "الإسماعيلية",
    "kafr el sheikh": "كفر الشيخ",
    "luxor": "الأقصر",
    "matrouh": "مطروح",
    "minya": "المنيا",
    "monufia": "المنوفية",
    "new valley": "الوادي الجديد",
    "north sinai": "شمال سيناء",
    "port said": "بورسعيد",
    "qalyubia": "القليوبية",
    "qena": "قنا",
    "red sea": "البحر الأحمر",
    "sharqia": "الشرقية",
    "sohag": "سوهاج",
    "south sinai": "جنوب سيناء",
    "suez": "السويس",
}
# ---
Regions = {
    "ali sabieh": "علي صبيح",
    "arta": "عرتا",
    "obock": "أوبوك",
    "tadjourah": "تاجورة",
}
# ---
Departments = {
    "chiquimula": "تشيكيمولا",
    "totonicapán": "توتونيكابان",
    "sololá": "سولولا",
    "petén": "بيتين",
    "izabal": "إيزابال",
    "guatemala": "غواتيمالا",
    "alta verapaz": "ألتا فيراباز",
    "baja verapaz": "بايا فيراباز",
    "chimaltenango": "تشيمالتينانغو",
    "jutiapa": "خوتيابا",
    "retalhuleu": "ريتاليوليو",
    "zacapa": "زاكابا",
    "jalapa": "جالابا",
    "sacatepéquez": "ساكاتيبيكيز",
    "quiché": "كويتشي",
    "quetzaltenango": "كويتزالتينانغو",
    "suchitepéquez": "سوشيتبيكيز",
    "san marcos": "سان ماركوس",
    "santa rosa, guatemala": "سانتا روزا",
    "huehuetenango": "هيويتينانغو",
    "escuintla": "إسكوينتلا",
    "el progreso": "البروغريسو",
}
# ---
Provinceies = {
    "arkhangai": "أرخانغاي",
    "bulgan": "بولغان",
    "selenge": "سيلنج",
    "orkhon": "أورخون",
    "darkhan-uul": "درخان-وول",
    "zavkhan": "زافخان",
    "govi-altai": "غوفي-ألتاي",
    "dornod": "دورنود",
    "dundgovi": "دوندغوفي",
    "sükhbaatar": "سوخباتار",
    "töv": "توف",
    "dornogovi": "دورنوغوفي",
    "govisümber": "جوفيسومبر",
    "övörkhangai": "أوفوخاناجي",
    "ömnögovi": "أومنوغوفي",
    "bayankhongor": "بايانخونغور",
    "khentii": "خنتي",
    "khövsgöl": "خوفسغول",
    "bayan-ölgii": "بايان-أولجي",
    "uvs": "أوفس",
}
# ---
Prefecture = {
    "bangui": "بانغي",
    "ombella-m'poko": "أومبلامبوكو",
    "nana-mambéré": "نانا مامبيري",
    "basse-kotto": "باس-كوتو",
    "lobaye": "لوبايه",
    "ouham": "أوهام",
    "bamingui-bangoran": "بامينغوي بانغوران",
    "ouaka": "أواكا",
    "mambéré-kadéï": "مامبرة كاديي",
    "kémo": "كيمو",
    "vakaga": "فاكاجا",
    "haut-mbomou": "هوت مبومو",
    "mbomou": "مبومو",
    "ouham-pendé": "أوهام-بيندي",
    "haute-kotto": "هوت-كوتو",
}
# ---
for dydcd in popopo:
    Main_Table_2[dydcd.lower()] = popopo[dydcd]
# ---
for dyd, dyd_lab in Egypht_t.items():
    dyd2 = dyd.lower()
    Main_Table_2[dyd2] = dyd_lab
    Main_Table_2[f"{dyd2} governorate"] = f"محافظة {dyd_lab}"
# ---
for dyd, dyd_lab in Regions.items():
    dyd2 = dyd.lower()
    Main_Table_2[dyd2] = dyd_lab
    Main_Table_2[f"{dyd2} region"] = f"منطقة {dyd_lab}"
# ---
for dyd, dyd_lab in Departments.items():
    dyd2 = dyd.lower()
    Main_Table_2[dyd2] = dyd_lab
    Main_Table_2[f"{dyd2} department"] = f"إدارة {dyd_lab}"
# ---
for dycd, dycd_lab in Provinceies.items():
    dycd2 = dycd.lower()
    Main_Table_2[dycd2] = dycd_lab
    Main_Table_2[f"{dycd2} province"] = f"محافظة {dycd_lab}"
# ---
for Pref, Pref_lab in Prefecture.items():
    Pref2 = Pref.lower()
    Main_Table_2[Pref2] = Pref_lab
    Main_Table_2[f"{Pref2} Prefecture"] = f"محافظة {Pref_lab}"
# ---
del popopo, Egypht_t, Regions, Departments, Provinceies, Prefecture
