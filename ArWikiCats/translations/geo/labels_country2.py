"""Regional translation helpers for administrative areas."""

from ..helps import len_print
from ..utils import open_json_file

REGION_SUFFIXES_EN = [
    " province",
    " district",
    " state",
    " region",
    " division",
    " county",
    " department",
    " municipality",
    " governorate",
    " voivodeship",
]
REGION_PREFIXES_AR = [
    "ولاية ",
    "الشعبة ",
    "شعبة ",
    "القسم ",
    "قسم ",
    "منطقة ",
    "محافظة ",
    "مقاطعة ",
    "إدارة ",
    "بلدية ",
    "إقليم ",
    "اقليم ",
]


def map_region_labels(REGION_SUFFIXES_EN, REGION_PREFIXES_AR, ADDITIONAL_REGION_KEYS):
    """
    Build a mapping from region base keys to Arabic region labels by matching configured English suffixes with Arabic prefixes.

    Parameters:
        REGION_SUFFIXES_EN (list[str]): English suffix strings to detect at the end of region keys (e.g., " province", " district").
        REGION_PREFIXES_AR (list[str]): Arabic prefix strings to detect at the start of labels (e.g., "ولاية ", "محافظة ").
        ADDITIONAL_REGION_KEYS (dict[str, str]): Mapping of region keys to Arabic labels to scan for suffix/prefix pairs.

    Returns:
        dict[str, str]: A dictionary where each key is the lowercased region base (original key with a matched English suffix removed) and each value is the Arabic label with the matched Arabic prefix removed. If multiple suffix/prefix combinations match a source entry, only the first match is used.
    """
    region_suffix_matches = {}

    for cc, lab in ADDITIONAL_REGION_KEYS.items():
        should_update = True
        cc2 = cc.lower()
        for en_k in REGION_SUFFIXES_EN:
            for ar_k in REGION_PREFIXES_AR:
                if should_update and cc2.endswith(en_k) and lab.startswith(ar_k):
                    should_update = False
                    cc3 = cc2[: -len(en_k)]
                    lab_2 = lab[len(ar_k) :]
                    region_suffix_matches[cc3] = lab_2
    return region_suffix_matches


def map_canton_labels_to_arabic(SWISS_CANTON_LABELS) -> dict[str, str]:
    """
    Build a mapping of Swiss canton identifiers to Arabic labels, including "canton-of" prefixed keys.

    Parameters:
        SWISS_CANTON_LABELS (dict[str, str]): Mapping of canton identifiers to their Arabic names.

    Returns:
        dict[str, str]: A new mapping where each original key is lowercased and each canton also has an entry
        of the form "canton-of {lowercased_key}" mapped to "كانتون {ArabicName}".
    """
    data = {k.lower(): v for k, v in SWISS_CANTON_LABELS.items()}

    for canton, value in SWISS_CANTON_LABELS.items():
        data[f"canton-of {canton.lower()}"] = f"كانتون {value}"
    return data


def generate_province_labels(PROVINCE_LABELS) -> dict[str, str]:
    """
    Create province-level Arabic label mappings derived from city labels.

    Parameters:
        PROVINCE_LABELS (dict[str, str]): Mapping of city identifiers to their Arabic labels. Keys may be any case; empty or falsey values are ignored.

    Returns:
        dict[str, str]: A dictionary whose keys are lowercase forms of the city identifier and two province variants
        ("{city} province" and "{city} (province)"), each mapped to the appropriate Arabic label (city label or
        "مقاطعة {city_label}").
    """
    data = {}
    for city, city_lab in PROVINCE_LABELS.items():
        city2 = city.lower()
        if city_lab:
            data[city2] = city_lab
            data[f"{city2} province"] = f"مقاطعة {city_lab}"
            data[f"{city2} (province)"] = f"مقاطعة {city_lab}"
    return data


SWISS_CANTON_LABELS = {
    "aarga": "أرجاو",
    "aargau": "أرجاو",
    "appenzell ausserrhoden": "أبينزيل أوسيرهودن",
    "appenzell innerrhoden": "أبينزيل إينرهودن",
    "basel-landschaft": "ريف بازل",
    "basel-land": "ريف بازل",
    "basel-stadt": "مدينة بازل",
    "bern": "برن",
    "fribourg": "فريبورغ",
    "geneva": "جنيف",
    "glarus": "غلاروس",
    "graubünden": "غراوبوندن",
    "grisons": "غراوبوندن",
    "jura": "جورا",
    "lucerne": "لوسيرن",
    "neuchâtel": "نيوشاتل",
    "nidwalden": "نيدفالدن",
    "obwalden": "أوبفالدن",
    "schaffhausen": "شافهوزن",
    "schwyz": "شفيتس",
    "solothurn": "سولوتورن",
    "st. gallen": "سانت غالن",
    "thurga": "تورغاو",
    "thurgau": "تورغاو",
    "ticino": "تيسينو",
    "uri": "أوري",
    "valais": "فاليز",
    "vaud": "فود",
    "zug": "تسوغ",
    "zürich": "زيورخ",
}

PROVINCE_LABEL_OVERRIDES = {
    "quintana roo": "ولاية كينتانا رو",
    "tamaulipas": "ولاية تاماوليباس",
    "campeche": "ولاية كامبيتشي",
    "helmand": "ولاية هلمند",
    "nuristan": "ولاية نورستان",
    "badghis": "ولاية بادغيس",
    "badakhshan": "ولاية بدخشان",
    "kapisa": "ولاية كابيسا",
    "baghlan": "ولاية بغلان",
    "daykundi": "ولاية دايكندي",
    "kandahar": "ولاية قندهار",
    "bamyan": "ولاية باميان",
    "nangarhar": "ولاية ننكرهار",
    "aklan": "ولاية أكلان",
    "zacatecas": "ولاية زاكاتيكاس",
    "zabul": "ولاية زابل",
    "balkh": "ولاية بلخ",
    "tlaxcala": "ولاية تلاكسكالا",
    "sinaloa": "ولاية سينالوا",
    "nam định": "محافظة نام دنه",
    "malampa": "محافظة مالامبا",
    "đắk lắk": "محافظة داك لاك",
    "lâm đồng": "محافظة لام دونغ",
    "điện biên": "محافظة دين بين",
    "northern province": "المحافظة الشمالية (زامبيا)",
    "central java province": "جاوة الوسطى",
    "south hwanghae province": "جنوب مقاطعة هوانغاي",
    "north sumatra province": "سومطرة الشمالية",
    "sancti spíritus province": "سانكتي سبيريتوس",
    "formosa province": "فورموسا",
    "orientale province": "أوريونتال",
    "western province": "المحافظة الغربية (زامبيا)",
    "papua province": "بابوا",
    "jambi province": "جمبي",
    "east nusa tenggara province": "نوسا تنقارا الشرقية",
    "southeast sulawesi province": "سولاوسي الجنوبية الشرقية",
    "chagang province": "تشاغانغ",
    "gorontalo province": "غورونتالو",
    "riau province": "رياو",
    "chaco province": "شاكو",
    "jujuy province": "خوخوي",
    "holguín province": "هولغوين",
    "north maluku province": "مالوكو الشمالية",
    "central province": "المحافظة الوسطى (زامبيا)",
    "central sulawesi province": "سولاوسي الوسطى",
    "southern province": "المحافظة الجنوبية (زامبيا)",
    "west papua province": "بابوا الغربية",
    "copperbelt province": "كوبربيلت",
    "granma province": "غرانما",
    "cienfuegos province": "سينفويغوس",
    "santiago de cuba province": "سانتياغو دي كوبا",
    "salavan province": "سالافان",
    "équateur province": "إكواتور",
    "entre ríos province": "إنتري ريوس",
    "north pyongan province": "بيونغان الشمالية",
    "west java province": "جاوة الغربية",
    "eastern province": "المحافظة الشرقية (زامبيا)",
    "north hwanghae province": "هوانغهاي الشمالية",
    "northwestern province": "المحافظة الشمالية الغربية (زامبيا)",
    "córdoba province": "كوردوبا",
    "matanzas": "ماتنزاس",
    "matanzas province": "مقاطعة ماتنزاس",
    "north sulawesi province": "سولاوسي الشمالية",
    "osh region": "أوش أوبلاستي",
    "puno region": "بونو",
    "flemish region": "الإقليم الفلامندي",
    "zanzibar urban/west region": "زنجبار الحضرية / المقاطعة الغربية",
    "talas region": "طلاس أوبلاستي",
    "tansift region": "جهة تانسيفت",
    "central region": "الجهة الوسطى",
    "northwestern region": "الجهة الشمالية الغربية",
    "cajamarca region": "كاخاماركا",
    "sacatepéquez department": "ساكاتيبيكيز",
    "escuintla department": "إسكوينتلا",
    "prevalje municipality": "بريفالجه",
    "moravče municipality": "مورافسكه (مورافسكه)",
    "vraneštica municipality": "فرانيستيكا (كيسيفو)",
    "vasilevo municipality": "فاسيليفو",
    "šentjernej municipality": "شينتيرني",
}

PROVINCE_LABELS = {
    "antananarivo": "فيانارانتسوا",
    "antsiranana": "أنتسيرانانا",
    "artemisa": "أرتيميسا",
    "bandundu": "بانداندو",
    "banten": "بنتن",
    "bas-congo": "الكونغو الوسطى",
    "bengkulu": "بنغكولو",
    "bengo": "بنغو",
    "benguela": "بنغيلا",
    "bié": "بيي",
    "buenos aires": "بوينس آيرس",
    "cabinda": "كابيندا",
    "camagüey": "كاماغوي",
    "cuando cubango": "كواندو كوبانغو",
    "cuanza norte": "كوانزا نورت",
    "cunene": "كونيني",
    "fianarantsoa": "فيانارانتسوا",
    "guantánamo": "غوانتانامو",
    "huambo": "هوامبو",
    "kangwon": "كانغوون",
    "katanga": "كاتانغا",
    "lampung": "لامبونغ",
    "las tunas": "لاس توناس",
    "luanda": "لواندا",
    "lunda norte": "لوندا نورتي",
    "lunda sul": "لوندا سول",
    "lusaka": "لوساكا",
    "mahajanga": "ماهاجانجا",
    "malanje": "مالانجي",
    "maluku": "مالوكو",
    "moxico": "موكسيكو",
    "namibe": "ناميبي",
    "ogooué-lolo": "أوغووي-لولو",
    "ogooué-maritime": "أوغووي - البحرية",
    "ryanggang": "ريانغانغ",
    "south pyongan": "بيونغان الجنوبية",
    "toamasina": "تواماسينا",
    "toliara": "توليارا",
    "uíge": "أوجي",
    "woleu-ntem": "وليو-نتم",
    "zaire": "زائير",
}


def generate_complete_label_mapping(
    ADDITIONAL_REGION_KEYS, SWISS_CANTON_LABELS, PROVINCE_LABEL_OVERRIDES, PROVINCE_LABELS, region_suffix_matches
) -> dict[str, str]:
    """
    Builds a consolidated mapping of administrative region keys to Arabic labels.

    Combines a base mapping loaded from "geography/P17_PP.json" with:
    - Arabic canton labels derived from SWISS_CANTON_LABELS,
    - lowercased entries from ADDITIONAL_REGION_KEYS,
    - lowercased entries from PROVINCE_LABEL_OVERRIDES,
    - region entries produced from region_suffix_matches,
    - generated province-level labels from PROVINCE_LABELS.

    Parameters:
        ADDITIONAL_REGION_KEYS (dict): Additional region keys and labels (will be added using lowercased keys).
        SWISS_CANTON_LABELS (dict): Swiss canton identifiers to Arabic names.
        PROVINCE_LABEL_OVERRIDES (dict): Explicit province label overrides (will be added using lowercased keys).
        PROVINCE_LABELS (dict): Province/city labels used to generate province-level entries.
        region_suffix_matches (dict): Mappings derived from suffix/prefix heuristics to add region variants.

    Returns:
        dict[str, str]: Merged mapping of region keys to Arabic labels. Later sources override earlier ones when keys collide.
    """
    COUNTRY_ADMIN_LABELS = open_json_file("geography/P17_PP.json") or {}
    canton_labels_mapping = map_canton_labels_to_arabic(SWISS_CANTON_LABELS)
    province_labels_dictionary = generate_province_labels(PROVINCE_LABELS)

    COUNTRY_ADMIN_LABELS.update(canton_labels_mapping)
    COUNTRY_ADMIN_LABELS.update({k.lower(): v for k, v in ADDITIONAL_REGION_KEYS.items()})
    COUNTRY_ADMIN_LABELS.update({k.lower(): v for k, v in PROVINCE_LABEL_OVERRIDES.items()})
    COUNTRY_ADMIN_LABELS.update(region_suffix_matches)
    COUNTRY_ADMIN_LABELS.update(province_labels_dictionary)

    return COUNTRY_ADMIN_LABELS


ADDITIONAL_REGION_KEYS = open_json_file("geography/New_Keys.json") or {}

region_suffix_matches = map_region_labels(REGION_SUFFIXES_EN, REGION_PREFIXES_AR, ADDITIONAL_REGION_KEYS)

COUNTRY_ADMIN_LABELS = generate_complete_label_mapping(
    ADDITIONAL_REGION_KEYS, SWISS_CANTON_LABELS, PROVINCE_LABEL_OVERRIDES, PROVINCE_LABELS, region_suffix_matches
)

__all__ = [
    "COUNTRY_ADMIN_LABELS",
]

len_print.data_len(
    "labels_country2.py",
    {
        "COUNTRY_ADMIN_LABELS": COUNTRY_ADMIN_LABELS,  # 1,778
        "ADDITIONAL_REGION_KEYS": ADDITIONAL_REGION_KEYS,
        "SWISS_CANTON_LABELS": SWISS_CANTON_LABELS,
        "PROVINCE_LABEL_OVERRIDES": PROVINCE_LABEL_OVERRIDES,
        "PROVINCE_LABELS": PROVINCE_LABELS,
        "region_suffix_matches": region_suffix_matches,
    },
)
