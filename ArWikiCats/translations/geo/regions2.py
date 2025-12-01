#!/usr/bin/python3
"""
# from .india_2 import SECONDARY_REGION_TRANSLATIONS

"""

from ...helps import len_print
from ..utils.json_dir import open_json_file


def _load_india_region_translations() -> dict[str, str]:
    index_labels: dict[str, str] = {}

    india_district_labels = open_json_file("geography/India_dd.json") or {}

    for district_name, district_label in india_district_labels.items():
        normalized_name = district_name.lower()
        index_labels[normalized_name] = district_label
        index_labels[f"{normalized_name} district"] = f"مقاطعة {district_label}"

    return index_labels


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

DJIBOUTI_REGION_TRANSLATIONS = {
    "ali sabieh": "علي صبيح",
    "arta": "عرتا",
    "obock": "أوبوك",
    "tadjourah": "تاجورة",
}

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

CENTRAL_AFRICAN_PREFECTURE = {
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

SECONDARY_REGION_TRANSLATIONS: dict[str, str] = {}

for governorate_name, governorate_label in EGYPT_GOVERNORATE_TRANSLATIONS.items():
    normalized_name = governorate_name.lower()
    SECONDARY_REGION_TRANSLATIONS[normalized_name] = governorate_label
    SECONDARY_REGION_TRANSLATIONS[f"{normalized_name} governorate"] = f"محافظة {governorate_label}"

for region_name, region_label in DJIBOUTI_REGION_TRANSLATIONS.items():
    normalized_name = region_name.lower()
    SECONDARY_REGION_TRANSLATIONS[normalized_name] = region_label
    SECONDARY_REGION_TRANSLATIONS[f"{normalized_name} region"] = f"منطقة {region_label}"

for department_name, department_label in GUATEMALA_DEPARTMENT_TRANSLATIONS.items():
    normalized_name = department_name.lower()
    SECONDARY_REGION_TRANSLATIONS[normalized_name] = department_label
    SECONDARY_REGION_TRANSLATIONS[f"{normalized_name} department"] = f"إدارة {department_label}"

for province_name, province_label in MONGOLIA_PROVINCE_TRANSLATIONS.items():
    normalized_name = province_name.lower()
    SECONDARY_REGION_TRANSLATIONS[normalized_name] = province_label
    SECONDARY_REGION_TRANSLATIONS[f"{normalized_name} province"] = f"محافظة {province_label}"

for prefecture_name, prefecture_label in CENTRAL_AFRICAN_PREFECTURE.items():
    normalized_name = prefecture_name.lower()
    SECONDARY_REGION_TRANSLATIONS[normalized_name] = prefecture_label
    SECONDARY_REGION_TRANSLATIONS[f"{normalized_name} prefecture"] = f"محافظة {prefecture_label}"

INDIA_REGION_TRANSLATIONS = _load_india_region_translations()

__all__ = [
    "SECONDARY_REGION_TRANSLATIONS",
    "INDIA_REGION_TRANSLATIONS",
]

len_print.data_len(
    "regions2.py",
    {
        "SECONDARY_REGION_TRANSLATIONS": SECONDARY_REGION_TRANSLATIONS,
        "INDIA_REGION_TRANSLATIONS": INDIA_REGION_TRANSLATIONS,
    },
)
