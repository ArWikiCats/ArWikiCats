"""Aggregate translation tables for country and region labels."""

from __future__ import annotations
from ...helps import len_print
from collections.abc import Mapping, MutableMapping

from ..companies import New_Company as COMPANY_LABELS
from ..mixed.all_keys2 import pf_keys2 as ADDITIONAL_KEYS
from ..mixed.all_keys5 import BASE_POP_FINAL_5  # , pop_final_5 as POPULATION_SUPPLEMENTS
from ..others.tax_table import Taxons_table as TAXON_TABLE
from ._shared import load_json_mapping, normalize_to_lower
from .Cities import CITY_LABEL_PATCHES, CITY_TRANSLATIONS
from .labels_country2 import COUNTRY_ADMIN_LABELS
from .regions import Main_Table
from .regions2 import India_Main_Table, Main_Table_2
from .us_counties import COUNTY_TRANSLATIONS

JAPAN_REGIONAL_LABELS = {
    "gokishichidō": "",
    "saitama": "سايتاما",
    "tohoku": "توهوكو",
    "shikoku": "شيكوكو",
    "kyushu": "كيوشو",
    "kantō": "كانتو",
    "kansai": "كانساي",
    "hokkaido": "هوكايدو",
    "hokuriku": "هوكوريكو",
    "chūgoku": "تشوغوكو",
    "toyama": "توياما",
    "tokushima": "توكوشيما",
    "chiba": "تشيبا",
    "tottori": "توتوري",
    "tochigi": "توتشيغي",
    "iwate": "إيواته",
    "ibaraki": "إيباراكي",
    "ishikawa": "إيشيكاوا",
    "ōsaka": "أوساكا",
    "okayama": "أوكاياما",
    "ehime": "إهيمه",
    "akita": "أكيتا",
    "aomori": "آوموري",
    "aichi": "آيتشي",
    "ōita": "أويتا",
    "okinawa": "أوكيناوا",
    "saga": "ساغا",
    "shimane": "شيمانه",
    "shiga": "شيغا",
    "shizuoka": "شيزوكا",
    "kanagawa": "كاناغاوا",
    "kagoshima": "كاغوشيما",
    "kagawa": "كاغاوا",
    "fukui": "فوكوي",
    "fukuoka": "فوكوكا",
    "fukushima": "فوكوشيما",
    "gifu": "غيفو",
    "gunma": "غونما",
    "kōchi": "كوتشي",
    "kumamoto": "كوماموتو",
    "kyōto": "كيوتو",
    "nagano": "ناغانو",
    "nagasaki": "ناغاساكي",
    "nara": "نارا",
    "mie": "ميه",
    "miyagi": "مياغي",
    "miyazaki": "ميازاكي",
    "yamanashi": "ياماناشي",
    "yamaguchi": "ياماغوتشي",
    "yamagata": "ياماغاتا",
    "wakayama": "واكاياما",
    "hyōgo": "هيوغو",
    "hiroshima prefecture": "عمالة هيروشيما",
    "niigata": "نييغاتا",
    "hokkaidō": "هوكايدو",
}

TURKEY_PROVINCE_LABELS = {
    "adana": "أضنة",
    "adıyaman": "أديامان",
    "afyonkarahisar": "أفيون قره حصار",
    "ağrı": "أغري",
    "aksaray": "آق سراي",
    "amasya": "أماصيا",
    "ankara": "أنقرة",
    "antalya": "أنطاليا",
    "ardahan": "أردهان",
    "artvin": "أرتوين",
    "aydın": "أيدين",
    "balıkesir": "بالق أسير",
    "bartın": "بارتين",
    "batman": "بطمان",
    "bayburt": "بايبورت",
    "bilecik": "بيله جك",
    "bingöl": "بينكل",
    "bitlis": "بتليس",
    "bolu": "بولو",
    "burdur": "بوردور",
    "bursa": "بورصة",
    "çanakkale": "جاناكالي",
    "çankırı": "جانقري",
    "çorum": "جوروم",
    "denizli": "دنيزلي",
    "diyarbakır": "دياربكر",
    "düzce": "دوزجه",
    "edirne": "أدرنة",
    "elazığ": "إلازيغ",
    "erzincan": "أرزينجان",
    "erzurum": "أرضروم",
    "eskişehir": "إسكيشهر",
    "gaziantep": "عنتاب",
    "giresun": "غيرسون",
    "gümüşhane": "كوموش خانة",
    "hakkâri": "حكاري",
    "hatay": "هاتاي",
    "iğdır": "اغدير",
    "isparta": "إسبرطة",
    "istanbul": "إسطنبول",
    "izmir": "إزمير",
    "kahramanmaraş": "قهرمان مرعش",
    "karabük": "كارابوك",
    "karaman": "كارامان",
    "kars": "كارس",
    "kastamonu": "قسطموني",
    "kayseri": "قيصري",
    "kilis": "كلس",
    "kırıkkale": "قيريقكالي",
    "kırklareli": "قرقلر ايلي",
    "kırşehir": "قرشهر",
    "kocaeli": "قوجه ايلي",
    "konya": "قونية",
    "kütahya": "كوتاهية",
    "malatya": "ملطية",
    "manisa": "مانيسا",
    "mardin": "ماردين",
    "mersin": "مرسين",
    "muğla": "موغلا",
    "muş": "موش",
    "nevşehir": "نوشهر",
    "niğde": "نيدا",
    "ordu": "أردو",
    "osmaniye": "عثمانية",
    "rize": "ريزه",
    "sakarya": "صقاريا",
    "samsun": "سامسون",
    "şanlıurfa": "شانلي أورفة",
    "siirt": "سعرد",
    "sinop": "سينوب",
    "sivas": "سيواس",
    "şırnak": "شرناق",
    "tekirdağ": "تكيرداغ",
    "tokat": "توقات",
    "trabzon": "طرابزون",
    "tunceli": "تونجلي",
    "uşak": "أوشاك",
    "van": "وان",
    "yalova": "يالوفا",
    "yozgat": "يوزغات",
    "zonguldak": "زانغولداك",
}

COUNTRY_LABEL_OVERRIDES = load_json_mapping("geography/P17_2_final_ll.json")
POPULATION_OVERRIDES = load_json_mapping("geography/opop.json")


def update_with_lowercased(target: MutableMapping[str, str], mapping: Mapping[str, str]) -> None:
    """Update ``target`` with a lower-cased version of ``mapping``."""

    for key, value in mapping.items():
        if not value:
            continue
        target[key.lower()] = value


def _build_country_label_index() -> dict[str, str]:
    """Return the aggregated translation table for countries and regions."""

    label_index: dict[str, str] = {}

    update_with_lowercased(label_index, CITY_TRANSLATIONS)
    update_with_lowercased(label_index, COUNTRY_LABEL_OVERRIDES)
    update_with_lowercased(label_index, POPULATION_OVERRIDES)
    update_with_lowercased(label_index, COUNTRY_ADMIN_LABELS)
    update_with_lowercased(label_index, Main_Table)
    update_with_lowercased(label_index, Main_Table_2)
    update_with_lowercased(label_index, India_Main_Table)
    update_with_lowercased(label_index, CITY_LABEL_PATCHES)
    update_with_lowercased(label_index, ADDITIONAL_KEYS)
    update_with_lowercased(label_index, COUNTY_TRANSLATIONS)

    for city, lal in JAPAN_REGIONAL_LABELS.items():
        city2 = city.lower()
        if lal:
            label_index[f"{city2} Prefecture"] = f"محافظة {lal}"
            label_index[f"{city2} region"] = f"منطقة {lal}"

    update_with_lowercased(label_index, JAPAN_REGIONAL_LABELS)
    update_with_lowercased(label_index, TURKEY_PROVINCE_LABELS)

    for province_name, province_label in TURKEY_PROVINCE_LABELS.items():
        if province_label:
            normalized = province_name.lower()
            label_index[f"{normalized} province"] = f"محافظة {province_label}"
            label_index[f"districts of {normalized} province"] = f"أقضية محافظة {province_label}"

    for company_name, company_label in COMPANY_LABELS.items():
        normalized_company = company_name.lower()
        if normalized_company not in ADDITIONAL_KEYS and company_label:
            label_index[normalized_company] = company_label

    label_index.update(  # Specific overrides used by downstream consumers.
        {
            "indycar": "أندي كار",
            "indiana": "إنديانا",
            "motorsport": "رياضة محركات",
            "indianapolis": "إنديانابوليس",
            "sports in indiana": "الرياضة في إنديانا",
            "igbo": "إغبو",
        }
    )

    for key, value in list(label_index.items()):
        if key.lower().startswith("the ") and value:
            trimmed_key = key[len("the ") :].strip()
            label_index.setdefault(trimmed_key, value)

    for taxon_name, taxon_label in TAXON_TABLE.items():
        normalized_taxon = taxon_name.lower()
        if normalized_taxon not in label_index and taxon_label:
            label_index[normalized_taxon] = taxon_label

    # for population_key, population_label in POPULATION_SUPPLEMENTS.items():
    for population_key, population_label in BASE_POP_FINAL_5.items():
        if not population_label:
            continue
        normalized_population_key = population_key.lower()
        label_index.setdefault(normalized_population_key, population_label)

    return label_index


COUNTRY_LABEL_INDEX = _build_country_label_index()
COUNTRY_LABEL_INDEX_LOWER = normalize_to_lower(COUNTRY_LABEL_INDEX)


def get_country_label_index() -> dict[str, str]:
    """Return a copy of the country label mapping."""

    return dict(COUNTRY_LABEL_INDEX)


def get_country_label_index_lower() -> dict[str, str]:
    """Return a copy of the lower-cased country label mapping."""

    return dict(COUNTRY_LABEL_INDEX_LOWER)


# Backwards compatible aliases
New_P17_Finall = COUNTRY_LABEL_INDEX

__all__ = [
    "COUNTRY_LABEL_OVERRIDES",
    "POPULATION_OVERRIDES",
    "COUNTRY_LABEL_INDEX",
    "COUNTRY_LABEL_INDEX_LOWER",
    "get_country_label_index",
    "get_country_label_index_lower",
    "New_P17_Finall",
]

len_print.data_len(
    "labels_country.py",
    {
        "COUNTRY_LABEL_OVERRIDES": COUNTRY_LABEL_OVERRIDES,
        "POPULATION_OVERRIDES": POPULATION_OVERRIDES,
        "COUNTRY_LABEL_INDEX": COUNTRY_LABEL_INDEX,
        "COUNTRY_LABEL_INDEX_LOWER": COUNTRY_LABEL_INDEX_LOWER,
        "New_P17_Finall": New_P17_Finall,
    },
)
