"""Secondary region translation tables."""

from __future__ import annotations

from ._shared import apply_suffix_templates, load_json_mapping, log_mapping_stats, update_with_lowercased

SECONDARY_REGION_TRANSLATIONS: dict[str, str] = {}
INDIA_REGION_TRANSLATIONS: dict[str, str] = {}

india_district_labels = load_json_mapping("India_dd")
update_with_lowercased(INDIA_REGION_TRANSLATIONS, india_district_labels)
apply_suffix_templates(
    INDIA_REGION_TRANSLATIONS,
    india_district_labels,
    ((" district", "مقاطعة %s"),),
)

raw_region_overrides = load_json_mapping("popopo")
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
update_with_lowercased(SECONDARY_REGION_TRANSLATIONS, raw_region_overrides)

update_with_lowercased(SECONDARY_REGION_TRANSLATIONS, EGYPT_GOVERNORATE_TRANSLATIONS)
apply_suffix_templates(
    SECONDARY_REGION_TRANSLATIONS,
    EGYPT_GOVERNORATE_TRANSLATIONS,
    ((" governorate", "محافظة %s"),),
)

update_with_lowercased(SECONDARY_REGION_TRANSLATIONS, DJIBOUTI_REGION_TRANSLATIONS)
apply_suffix_templates(
    SECONDARY_REGION_TRANSLATIONS,
    DJIBOUTI_REGION_TRANSLATIONS,
    ((" region", "منطقة %s"),),
)

update_with_lowercased(SECONDARY_REGION_TRANSLATIONS, GUATEMALA_DEPARTMENT_TRANSLATIONS)
apply_suffix_templates(
    SECONDARY_REGION_TRANSLATIONS,
    GUATEMALA_DEPARTMENT_TRANSLATIONS,
    ((" department", "إدارة %s"),),
)

update_with_lowercased(SECONDARY_REGION_TRANSLATIONS, MONGOLIA_PROVINCE_TRANSLATIONS)
apply_suffix_templates(
    SECONDARY_REGION_TRANSLATIONS,
    MONGOLIA_PROVINCE_TRANSLATIONS,
    ((" province", "محافظة %s"),),
)

update_with_lowercased(SECONDARY_REGION_TRANSLATIONS, CAR_PREFECTURE_TRANSLATIONS)
apply_suffix_templates(
    SECONDARY_REGION_TRANSLATIONS,
    CAR_PREFECTURE_TRANSLATIONS,
    ((" prefecture", "محافظة %s"),),
)

log_mapping_stats(
    "regions2",
    secondary_regions=SECONDARY_REGION_TRANSLATIONS,
    india_regions=INDIA_REGION_TRANSLATIONS,
)


def get_secondary_region_translations() -> dict[str, str]:
    """Return a copy of the secondary region translations."""

    return dict(SECONDARY_REGION_TRANSLATIONS)


def get_india_region_translations() -> dict[str, str]:
    """Return a copy of the India region translations."""

    return dict(INDIA_REGION_TRANSLATIONS)


Main_Table_2 = SECONDARY_REGION_TRANSLATIONS
India_Main_Table = INDIA_REGION_TRANSLATIONS

__all__ = [
    "SECONDARY_REGION_TRANSLATIONS",
    "INDIA_REGION_TRANSLATIONS",
    "get_secondary_region_translations",
    "get_india_region_translations",
    "Main_Table_2",
    "India_Main_Table",
]
