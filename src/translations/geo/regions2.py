#!/usr/bin/python3
"""
# from .india_2 import SECONDARY_REGION_TRANSLATIONS

"""
from ..utils.json_dir import open_json_file

# ---
india_district_labels = {}
raw_region_overrides = {}
SECONDARY_REGION_TRANSLATIONS = {}
INDIA_REGION_TRANSLATIONS = {}
# India_districts = {}
# India_Citiese = {}
# ---
india_district_labels = open_json_file("India_dd") or {}
# ---
for district_name, district_label in india_district_labels.items():
    normalized_name = district_name.lower()
    INDIA_REGION_TRANSLATIONS[normalized_name] = district_label
    # India_districts[f"{normalized_name} district"] = f"مقاطعة {district_label}"
    # India_Citiese[district_name] = district_label
    INDIA_REGION_TRANSLATIONS[f"{normalized_name} district"] = f"مقاطعة {district_label}"
# ---
del india_district_labels
# ---
raw_region_overrides = open_json_file("popopo") or {}
# ---
EGYPT_GOVERNORATE_TRANSLATIONS = {
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
DJIBOUTI_REGION_TRANSLATIONS = {
    "ali sabieh": "علي صبيح",
    "arta": "عرتا",
    "obock": "أوبوك",
    "tadjourah": "تاجورة",
}
# ---
GUATEMALA_DEPARTMENT_TRANSLATIONS = {
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
MONGOLIA_PROVINCE_TRANSLATIONS = {
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
CAR_PREFECTURE_TRANSLATIONS = {
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
for region_key, region_label in raw_region_overrides.items():
    SECONDARY_REGION_TRANSLATIONS[region_key.lower()] = region_label
# ---
for governorate_name, governorate_label in EGYPT_GOVERNORATE_TRANSLATIONS.items():
    normalized_name = governorate_name.lower()
    SECONDARY_REGION_TRANSLATIONS[normalized_name] = governorate_label
    SECONDARY_REGION_TRANSLATIONS[f"{normalized_name} governorate"] = f"محافظة {governorate_label}"
# ---
for region_name, region_label in DJIBOUTI_REGION_TRANSLATIONS.items():
    normalized_name = region_name.lower()
    SECONDARY_REGION_TRANSLATIONS[normalized_name] = region_label
    SECONDARY_REGION_TRANSLATIONS[f"{normalized_name} region"] = f"منطقة {region_label}"
# ---
for department_name, department_label in GUATEMALA_DEPARTMENT_TRANSLATIONS.items():
    normalized_name = department_name.lower()
    SECONDARY_REGION_TRANSLATIONS[normalized_name] = department_label
    SECONDARY_REGION_TRANSLATIONS[f"{normalized_name} department"] = f"إدارة {department_label}"
# ---
for province_name, province_label in MONGOLIA_PROVINCE_TRANSLATIONS.items():
    normalized_name = province_name.lower()
    SECONDARY_REGION_TRANSLATIONS[normalized_name] = province_label
    SECONDARY_REGION_TRANSLATIONS[f"{normalized_name} province"] = f"محافظة {province_label}"
# ---
for prefecture_name, prefecture_label in CAR_PREFECTURE_TRANSLATIONS.items():
    normalized_name = prefecture_name.lower()
    SECONDARY_REGION_TRANSLATIONS[normalized_name] = prefecture_label
    SECONDARY_REGION_TRANSLATIONS[f"{normalized_name} prefecture"] = f"محافظة {prefecture_label}"
# ---
del (
    raw_region_overrides,
    EGYPT_GOVERNORATE_TRANSLATIONS,
    DJIBOUTI_REGION_TRANSLATIONS,
    GUATEMALA_DEPARTMENT_TRANSLATIONS,
    MONGOLIA_PROVINCE_TRANSLATIONS,
    CAR_PREFECTURE_TRANSLATIONS,
)

Main_Table_2 = SECONDARY_REGION_TRANSLATIONS
India_Main_Table = INDIA_REGION_TRANSLATIONS
