"""Aggregate translation tables for country and region labels."""

from __future__ import annotations

from collections.abc import Mapping, MutableMapping

from ...helps import len_print, logger
from ..mixed.all_keys2 import pf_keys2
from ..mixed.all_keys5 import BASE_POP_FINAL_5
from ..nats.Nationality import all_country_ar
from ..tax_table import Taxons_table as TAXON_TABLE
from ._shared import load_json_mapping
from .Cities import CITY_TRANSLATIONS_LOWER
from .labels_country2 import COUNTRY_ADMIN_LABELS
from .regions import MAIN_REGION_TRANSLATIONS
from .regions2 import INDIA_REGION_TRANSLATIONS, SECONDARY_REGION_TRANSLATIONS
from .us_counties import US_COUNTY_TRANSLATIONS

US_STATES = {
    "georgia (u.s. state)": "ولاية جورجيا",
    "new york (state)": "ولاية نيويورك",
    "washington (state)": "ولاية واشنطن",
    "washington": "واشنطن",
    "washington, d.c.": "واشنطن العاصمة",
    "georgia": "جورجيا",
    "new york": "نيويورك",
    "alabama": "ألاباما",
    "alaska": "ألاسكا",
    "arizona": "أريزونا",
    "arkansas": "أركنساس",
    "california": "كاليفورنيا",
    "colorado": "كولورادو",
    "connecticut": "كونيتيكت",
    "delaware": "ديلاوير",
    "florida": "فلوريدا",
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
    "north carolina": "كارولاينا الشمالية",
    "north dakota": "داكوتا الشمالية",
    "ohio": "أوهايو",
    "oklahoma": "أوكلاهوما",
    "oregon": "أوريغن",
    "pennsylvania": "بنسلفانيا",
    "rhode island": "رود آيلاند",
    "south carolina": "كارولاينا الجنوبية",
    "south dakota": "داكوتا الجنوبية",
    "tennessee": "تينيسي",
    "texas": "تكساس",
    "utah": "يوتا",
    "vermont": "فيرمونت",
    "virginia": "فرجينيا",
    "west virginia": "فرجينيا الغربية",
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


def update_with_lowercased(target: MutableMapping[str, str], mapping: Mapping[str, str]) -> None:
    """Update ``target`` with a lower-cased version of ``mapping``."""

    for key, value in mapping.items():
        if not value:
            continue
        target[key.lower()] = value


def setdefault_with_lowercased(target: MutableMapping[str, str], mapping: Mapping[str, str], name: str = "") -> None:
    """Update ``target`` with a lower-cased version of ``mapping``."""
    added = 0
    for key, value in mapping.items():
        if not value or key.lower() in target:
            continue
        target.setdefault(key.lower(), value)
        added += 1

    logger.debug(f"Added {added} entries to the target mapping, source mapping({name}) {len(mapping)}.")


def _make_japan_labels(data: dict[str, str]) -> dict[str, str]:
    labels_index = {}
    for province_name, province_label in data.items():
        if province_label:
            normalized = province_name.lower()
            labels_index[normalized] = province_label
            labels_index[f"{normalized} prefecture"] = f"محافظة {province_label}"
            labels_index[f"{normalized} region"] = f"منطقة {province_label}"

    return labels_index


def _make_turkey_labels(data: dict[str, str]) -> dict[str, str]:
    labels_index = {}
    for province_name, province_label in data.items():
        if province_label:
            normalized = province_name.lower()
            labels_index[normalized] = province_label
            labels_index[f"{normalized} province"] = f"محافظة {province_label}"
            labels_index[f"districts of {normalized} province"] = f"أقضية محافظة {province_label}"

    return labels_index


COMPANY_LABELS_NEW = {
    "airliner": "طائرات",
    "condiment": "توابل",
    "fraternal service": "خدمات أخوية",
    "health care": "رعاية صحية",
    "internet": "إنترنت",
    "magazine": "مجلات",
    "mass media": "وسائل إعلام",
    "military logistics": "لوجستية عسكرية",
    "rail": "سكك حديدية",
    "submarine": "غواصات",
}

JAPAN_LABELS = _make_japan_labels(JAPAN_REGIONAL_LABELS)
TURKEY_LABELS = _make_turkey_labels(TURKEY_PROVINCE_LABELS)


CITY_LABEL_PATCHES = load_json_mapping("cities/yy2.json")
COUNTRY_LABEL_OVERRIDES = load_json_mapping("geography/P17_2_final_ll.json")
raw_region_overrides = load_json_mapping("geography/popopo.json")


def _handle_the_prefix(label_index: dict[str, str]) -> dict[str, str]:
    """Handle 'the ' prefix in country labels."""
    new_keys = {}
    for key, value in list(label_index.items()):
        if not key.lower().startswith("the ") or not value:
            continue

        trimmed_key = key[len("the ") :].strip()
        if trimmed_key in label_index:
            continue
        new_keys.setdefault(trimmed_key, value)

    logger.debug(f">> _handle_the_prefix() Added {len(new_keys)} entries without 'the ' prefix.")
    return new_keys


def _build_country_label_index() -> dict[str, str]:
    """Return the aggregated translation table for countries and regions."""

    label_index: dict[str, str] = {}

    label_index.update(CITY_TRANSLATIONS_LOWER)  # 10,788

    to_update = {
        "ALL_COUNTRY_AR": all_country_ar,  # 54
        "US_STATES": US_STATES,  # 54
        "COUNTRY_LABEL_OVERRIDES": COUNTRY_LABEL_OVERRIDES,  # 1778
        "COUNTRY_ADMIN_LABELS": COUNTRY_ADMIN_LABELS,  # 1782
        "MAIN_REGION_TRANSLATIONS": MAIN_REGION_TRANSLATIONS,  # 823
        "raw_region_overrides": raw_region_overrides,  # 1782
        "SECONDARY_REGION_TRANSLATIONS": SECONDARY_REGION_TRANSLATIONS,  # 176
        "INDIA_REGION_TRANSLATIONS": INDIA_REGION_TRANSLATIONS,  # 1424
        # "CITY_LABEL_PATCHES": CITY_LABEL_PATCHES,                          # 5191
        # "pf_keys2": pf_keys2,                                              # 35730,
        # "US_COUNTY_TRANSLATIONS": US_COUNTY_TRANSLATIONS,                  # 2998
        # "JAPAN_LABELS": JAPAN_LABELS,                                      # 162
        # "TURKEY_LABELS": TURKEY_LABELS,                                    # 243
        # "COMPANY_LABELS_NEW": COMPANY_LABELS_NEW,                          # 10
    }
    for name, mapping in to_update.items():
        logger.debug(f">> _build_country_label_index() Updating labels for {name}, entries: {len(mapping)}")
        update_with_lowercased(label_index, mapping)

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
    no_prefix = _handle_the_prefix(label_index)  # 276
    label_index.update(no_prefix)

    setdefault_with_lowercased(label_index, TAXON_TABLE, "TAXON_TABLE")  # 5324

    setdefault_with_lowercased(label_index, BASE_POP_FINAL_5, "BASE_POP_FINAL_5")  # 124

    return label_index


NEW_P17_FINAL = _build_country_label_index()  # 68,981


def get_from_new_p17_aliases(text: str, default: str | None = "") -> str:
    """Look up the Arabic label for a term in alias mappings."""
    result = (
        COMPANY_LABELS_NEW.get(text)
        or TURKEY_LABELS.get(text)
        or JAPAN_LABELS.get(text)
        or US_COUNTY_TRANSLATIONS.get(text)
        or pf_keys2.get(text)
        or CITY_LABEL_PATCHES.get(text)
    )
    return result or default


def get_from_new_p17_final(text: str, default: str | None = "") -> str:
    """Look up the Arabic label for a term in the ``NEW_P17_FINAL`` mapping."""

    lower_text = text.lower()
    # result = NEW_P17_FINAL.get(lower_text) or get_from_new_p17_aliases(lower_text)
    result = get_from_new_p17_aliases(lower_text) or NEW_P17_FINAL.get(lower_text)

    return result or default


__all__ = [
    "COUNTRY_LABEL_OVERRIDES",
    "get_from_new_p17_final",
]

len_print.data_len(
    "labels_country.py",
    {
        "COUNTRY_LABEL_OVERRIDES": COUNTRY_LABEL_OVERRIDES,
        "CITY_LABEL_PATCHES": CITY_LABEL_PATCHES,  # 5,191
        "NEW_P17_FINAL": NEW_P17_FINAL,
    },
)
