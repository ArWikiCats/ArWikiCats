"""Aggregate translation tables for country and region labels."""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping

from ...helps import len_print
from ..companies import New_Company as COMPANY_LABELS
from ..mixed.all_keys2 import pf_keys2
from ..mixed.all_keys5 import (
    BASE_POP_FINAL_5,  # , pop_final_5 as POPULATION_SUPPLEMENTS
)
from ..tax_table import Taxons_table as TAXON_TABLE
from ._shared import load_json_mapping, normalize_to_lower
from .Cities import CITY_LABEL_PATCHES, CITY_TRANSLATIONS_LOWER
from .labels_country2 import COUNTRY_ADMIN_LABELS
from .regions import MAIN_REGION_TRANSLATIONS
from .regions2 import INDIA_REGION_TRANSLATIONS, SECONDARY_REGION_TRANSLATIONS
from .us_counties import US_COUNTY_TRANSLATIONS

US_STATES = {
    "alabama": "ألاباما",
    "alaska": "ألاسكا",
    "arizona": "أريزونا",
    "arkansas": "أركنساس",
    "california": "كاليفورنيا",
    "colorado": "كولورادو",
    "connecticut": "كونيتيكت",
    "delaware": "ديلاوير",
    "florida": "فلوريدا",
    "georgia (u.s. state)": "ولاية جورجيا",
    "georgia": "جورجيا",
    "hawaii": "هاواي",
    "idaho": "أيداهو",
    "illinois": "إلينوي",
    "indiana": "إنديانا",
    "iowa": "آيوا",
    "kansas": "كانساس",
    "kentucky": "كنتاكي",
    "louisiana": "لويزيانا",
    "maine": "مين",
    "maryland": "ماريلند",
    "massachusetts": "ماساتشوستس",
    "michigan": "ميشيغان",
    "minnesota": "منيسوتا",
    "mississippi": "مسيسيبي",
    "missouri": "ميزوري",
    "montana": "مونتانا",
    "nebraska": "نبراسكا",
    "nevada": "نيفادا",
    "new hampshire": "نيوهامشير",
    "new jersey": "نيوجيرسي",
    "new mexico": "نيومكسيكو",
    "new york (state)": "ولاية نيويورك",
    "new york": "نيويورك",
    "north carolina": "كارولاينا الشمالية",
    "north dakota": "داكوتا الشمالية",
    "ohio": "أوهايو",
    "oklahoma": "أوكلاهوما",
    "oregon": "أوريغون",
    "pennsylvania": "بنسلفانيا",
    "rhode island": "رود آيلاند",
    "south carolina": "كارولاينا الجنوبية",
    "south dakota": "داكوتا الجنوبية",
    "tennessee": "تينيسي",
    "texas": "تكساس",
    "utah": "يوتا",
    "vermont": "فيرمونت",
    "virginia": "فرجينيا",
    "washington (state)": "ولاية واشنطن",
    "washington": "واشنطن",
    "washington, d.c.": "واشنطن العاصمة",
    "west virginia": "فيرجينيا الغربية",
    "wisconsin": "ويسكونسن",
    "wyoming": "وايومنغ",
}

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
raw_region_overrides = load_json_mapping("geography/popopo.json")


def update_with_lowercased(target: MutableMapping[str, str], mapping: Mapping[str, str]) -> None:
    """Update ``target`` with a lower-cased version of ``mapping``."""

    for key, value in mapping.items():
        if not value:
            continue
        target[key.lower()] = value


def _build_country_label_index() -> dict[str, str]:
    """Return the aggregated translation table for countries and regions."""

    label_index: dict[str, str] = {}

    label_index.update(CITY_TRANSLATIONS_LOWER)
    update_with_lowercased(label_index, US_STATES)
    update_with_lowercased(label_index, COUNTRY_LABEL_OVERRIDES)
    update_with_lowercased(label_index, POPULATION_OVERRIDES)
    update_with_lowercased(label_index, COUNTRY_ADMIN_LABELS)
    update_with_lowercased(label_index, MAIN_REGION_TRANSLATIONS)

    update_with_lowercased(label_index, raw_region_overrides)
    update_with_lowercased(label_index, SECONDARY_REGION_TRANSLATIONS)

    update_with_lowercased(label_index, INDIA_REGION_TRANSLATIONS)
    update_with_lowercased(label_index, CITY_LABEL_PATCHES)
    update_with_lowercased(label_index, pf_keys2)
    update_with_lowercased(label_index, US_COUNTY_TRANSLATIONS)

    for city, lal in JAPAN_REGIONAL_LABELS.items():
        city2 = city.lower()
        if lal:
            label_index[f"{city2} prefecture"] = f"محافظة {lal}"
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
        if normalized_company not in pf_keys2 and company_label:
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


New_P17_Finall = _build_country_label_index()

__all__ = [
    "COUNTRY_LABEL_OVERRIDES",
    "POPULATION_OVERRIDES",
    "New_P17_Finall",
]

len_print.data_len(
    "labels_country.py",
    {
        "COUNTRY_LABEL_OVERRIDES": COUNTRY_LABEL_OVERRIDES,
        "POPULATION_OVERRIDES": POPULATION_OVERRIDES,
        "New_P17_Finall": New_P17_Finall,
    },
)
