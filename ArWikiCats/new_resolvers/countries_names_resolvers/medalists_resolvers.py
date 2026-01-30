#!/usr/bin/python3
"""
Resolve medalists categories translations
"""

import functools
from typing import Dict

import logging
from ...translations import COUNTRY_LABEL_OVERRIDES, countries_from_nat
from ...translations_formats import MultiDataFormatterBaseV2, format_multi_data_v2

logger = logging.getLogger(__name__)

medalists_data = {
    # "central american and caribbean games": "ألعاب أمريكا الوسطى والكاريبي",
    "afc asian cup finals": "نهائيات كأس آسيا",
    "afc asian cup qualification": "تصفيات كأس آسيا",
    "afc asian cup": "كأس آسيا",
    "afc challenge league": "دوري التحدي الآسيوي",
    "afc champions league elite": "دوري نخبة ابطال آسيا",
    "afc champions league two": "دوري أبطال آسيا الثاني",
    "afc champions league": "دوري أبطال آسيا",
    "afc cup participants": "مشاركون في كأس الاتحاد الآسيوي لكرة القدم",
    "afc cup": "كأس الاتحاد الآسيوي",
    "afc elite league": "دوري نخبة ابطال آسيا",
    "afc football": "كرة قدم الاتحاد الآسيوي لكرة القدم",
    "afc futsal asian cup": "كأس آسيا لكرة الصالات",
    "afc futsal championship": "بطولة آسيا لكرة الصالات",
    "afc futsal club championship": "بطولة آسيا لكرة الصالات للأندية",
    "afc president's cup": "كأس رئيس الاتحاد الآسيوي",
    "afc solidarity cup": "كأس التضامن الآسيوي",
    "afc u-16 asian cup": "كأس آسيا للناشئين تحت 16 سنة",
    "afc u-16 championship": "بطولة آسيا للناشئين تحت 16 سنة",
    "afc u-16 women's asian cup": "كأس آسيا للسيدات تحت 16 سنة",
    "afc u-16 women's championship": "بطولة آسيا للسيدات تحت 16 سنة",
    "afc u-17 asian cup": "كأس آسيا للناشئين تحت 17 سنة",
    "afc u-17 championship": "بطولة آسيا للناشئين تحت 17 سنة",
    "afc u-17 women's asian cup": "كأس آسيا للسيدات تحت 17 سنة",
    "afc u-17 women's championship": "بطولة آسيا للسيدات تحت 17 سنة",
    "afc u-19 asian cup": "كأس آسيا للناشئين تحت 19 سنة",
    "afc u-19 championship": "بطولة آسيا للناشئين تحت 19 سنة",
    "afc u-19 women's asian cup": "كأس آسيا للسيدات تحت 19 سنة",
    "afc u-19 women's championship": "بطولة آسيا للسيدات تحت 19 سنة",
    "afc u-20 asian cup": "كأس آسيا للناشئين تحت 20 سنة",
    "afc u-20 championship": "بطولة آسيا للناشئين تحت 20 سنة",
    "afc u-20 women's asian cup": "كأس آسيا للسيدات تحت 20 سنة",
    "afc u-20 women's championship": "بطولة آسيا للسيدات تحت 20 سنة",
    "afc u-22 asian cup": "كأس آسيا للناشئين تحت 22 سنة",
    "afc u-22 championship": "بطولة آسيا للناشئين تحت 22 سنة",
    "afc u-22 women's asian cup": "كأس آسيا للسيدات تحت 22 سنة",
    "afc u-22 women's championship": "بطولة آسيا للسيدات تحت 22 سنة",
    "afc u-23 asian cup": "كأس آسيا تحت 23 سنة",
    "afc u-23 championship": "بطولة آسيا تحت 23 سنة",
    "afc u-23 women's asian cup": "كأس آسيا للسيدات تحت 23 سنة",
    "afc u-23 women's championship": "بطولة آسيا للسيدات تحت 23 سنة",
    "afc women's asian cup": "كأس الأمم الآسيوية لكرة القدم للسيدات",
    "afc women's championship": "بطولة آسيا للسيدات",
    "afc women's futsal championship": "بطولة آسيا لكرة الصالات للسيدات",
    "afc youth championship": "بطولة آسيا للشباب",
    "african games": "الألعاب الإفريقية",
    "all-africa games": "ألعاب عموم إفريقيا",
    "asian beach games": "دورة الألعاب الآسيوية الشاطئية",
    "asian football confederation": "الاتحاد الآسيوي لكرة القدم",
    "asian games": "الألعاب الآسيوية",
    "asian indoor games": "دورة الألعاب الآسيوية داخل الصالات",
    "asian para games": "الألعاب البارالمبية الآسيوية",
    "asian summer games": "الألعاب الآسيوية الصيفية",
    "asian winter games": "الألعاب الآسيوية الشتوية",
    "association football afc": "كرة القدم في الاتحاد الآسيوي لكرة القدم",
    "association-football afc": "كرة القدم في الاتحاد الآسيوي لكرة القدم",
    "bolivarian games": "الألعاب البوليفارية",
    "central american and caribbean games": "ألعاب أمريكا الوسطى والكاريبي",
    "central american games": "ألعاب أمريكا الوسطى",
    "central-american-and-caribbean-games": "ألعاب أمريكا الوسطى والكاريبي",
    "commonwealth games": "ألعاب الكومنولث",
    "commonwealth youth games": "ألعاب الكومنولث الشبابية",
    "deaflympic games": "ألعاب ديفلمبياد",
    "european games": "الألعاب الأوروبية",
    "european youth olympic winter": "الألعاب الأولمبية الشبابية الأوروبية الشتوية",
    "european youth olympic": "الألعاب الأولمبية الشبابية الأوروبية",
    "fifa futsal world cup qualification (afc)": "تصفيات كأس العالم لكرة الصالات (آسيا)",
    "fifa futsal world cup qualification (caf)": "تصفيات كأس العالم لكرة الصالات (إفريقيا)",
    "fifa futsal world cup qualification": "تصفيات كأس العالم لكرة الصالات",
    "fifa futsal world cup": "كأس العالم لكرة الصالات",
    "fifa world cup qualification (afc)": "تصفيات كأس العالم لكرة القدم (آسيا)",
    "fifa world cup qualification (caf)": "تصفيات كأس العالم لكرة القدم (إفريقيا)",
    "fis nordic world ski championships": "بطولة العالم للتزلج النوردي على الثلج",
    "friendship games": "ألعاب الصداقة",
    "goodwill games": "ألعاب النوايا الحسنة",
    "islamic solidarity games": "ألعاب التضامن الإسلامي",
    "jeux de la francophonie": "الألعاب الفرانكوفونية",
    "maccabiah games": "الألعاب المكابيه",
    "mediterranean games": "الألعاب المتوسطية",
    "micronesian games": "الألعاب الميكرونيزية",
    "military world games": "دورة الألعاب العسكرية",
    "olympic games": "الألعاب الأولمبية",
    "olympic": "الألعاب الأولمبية",
    "pan american games": "دورة الألعاب الأمريكية",
    "pan arab games": "دورة الألعاب العربية",
    "pan asian games": "دورة الألعاب الآسيوية",
    "paralympic": "الألعاب البارالمبية",
    "paralympics games": "الألعاب البارالمبية",
    "paralympics": "الألعاب البارالمبية",
    "parapan american games": "ألعاب بارابان الأمريكية",
    "sea games": "ألعاب البحر",
    "south american games": "ألعاب أمريكا الجنوبية",
    "south asian beach games": "دورة ألعاب جنوب أسيا الشاطئية",
    "south asian games": "ألعاب جنوب أسيا",
    "south asian winter games": "ألعاب جنوب آسيا الشتوية",
    # "winter olympic": "الألعاب الأولمبية الشتوية",
    # "winter universiade": "الألعاب الجامعية الشتوية",
    # "winter world university games": "ألعاب الجامعات العالمية الشتوية",
    # "summer olympic": "الألعاب الأولمبية الصيفية",
    # "summer universiade": "الألعاب الجامعية الصيفية",
    # "summer world university games": "ألعاب الجامعات العالمية الصيفية",
    "southeast asian games": "ألعاب جنوب شرق آسيا",
    "the universiade": "الألعاب الجامعية",
    "universiade": "الألعاب الجامعية",
    "world athletics indoor championships": "بطولة العالم لألعاب القوى داخل الصالات",
    "world championships": "بطولات العالم",
    "world games": "دورة الألعاب العالمية",
    "world university games": "ألعاب الجامعات العالمية",
    "youth olympic games": "الألعاب الأولمبية الشبابية",
    "youth olympic": "الألعاب الأولمبية الشبابية",
}


def _build_formatted_data() -> Dict[str, str]:
    # NOTE: formatted_data used in other resolver
    formatted_data: Dict[str, str] = {}

    base_formatted_data = {
        "{en} at {game_en}": "{ar} في {game_ar}",
        "{game_en}": "{game_ar}",
        "{game_en} coaches": "مدربون في {game_ar}",
        "{game_en} managers": "مدربون في {game_ar}",
        "{game_en} competitors": "منافسون في {game_ar}",
        "{game_en} competitors for {en}": "منافسون في {game_ar} من {ar}",
        "{game_en} competitions": "منافسات {game_ar}",
        "{game_en} events": "أحداث {game_ar}",
        "{game_en} festival": "مهرجانات {game_ar}",
        "{game_en} bids": "عروض {game_ar}",
        "{game_en} templates": "قوالب {game_ar}",
        "{game_en} medalists": "فائزون بميداليات {game_ar}",
        "{game_en} bronze medalists": "فائزون بميداليات برونزية في {game_ar}",
        "{game_en} gold medalists": "فائزون بميداليات ذهبية في {game_ar}",
        "{game_en} silver medalists": "فائزون بميداليات فضية في {game_ar}",
        "{game_en} medalists for {en}": "فائزون بميداليات {game_ar} من {ar}",
        "{game_en} bronze medalists for {en}": "فائزون بميداليات برونزية في {game_ar} من {ar}",
        "{game_en} gold medalists for {en}": "فائزون بميداليات ذهبية في {game_ar} من {ar}",
        "{game_en} silver medalists for {en}": "فائزون بميداليات فضية في {game_ar} من {ar}",
    }

    for base_key, base_label in base_formatted_data.items():
        formatted_data[base_key] = base_label
        # formatted_data[f"winter {base_key}"] = f"{base_label} الشتوية"
        formatted_data[f"winter {base_key}"] = base_label.format(game_ar="{game_ar} الشتوية", ar="{ar}")
        formatted_data[f"summer {base_key}"] = base_label.format(game_ar="{game_ar} الصيفية", ar="{ar}")
        formatted_data[f"west {base_key}"] = base_label.format(game_ar="{game_ar} الغربية", ar="{ar}")
        formatted_data[f"east {base_key}"] = base_label.format(game_ar="{game_ar} الشرقية", ar="{ar}")

    _olympic_types = {
        "olympic": "أولمبية",
        "winter olympic": "أولمبية شتوية",
        "summer olympic": "أولمبية صيفية",
        "paralympic": "بارالمبية",
    }
    formatted_data.update(
        {
            "olympic gold medalists for {en} in alpine skiing": "فائزون بميداليات ذهبية أولمبية من {ar} في التزلج على المنحدرات الثلجية",
            # medalists
            "olympic medalists": "فائزون بميداليات أولمبية",
            "olympic gold medalists": "فائزون بميداليات ذهبية أولمبية",
            "olympic silver medalists": "فائزون بميداليات فضية أولمبية",
            "olympic bronze medalists": "فائزون بميداليات برونزية أولمبية",
            "winter olympic medalists": "فائزون بميداليات أولمبية شتوية",
            "summer olympic medalists": "فائزون بميداليات أولمبية صيفية",
            # medalists + countries
            "olympic medalists for {en}": "فائزون بميداليات أولمبية من {ar}",
            "olympic gold medalists for {en}": "فائزون بميداليات ذهبية أولمبية من {ar}",
            "olympic silver medalists for {en}": "فائزون بميداليات فضية أولمبية من {ar}",
            "olympic bronze medalists for {en}": "فائزون بميداليات برونزية أولمبية من {ar}",
            # competitors
            "paralympic competitors": "منافسون بارالمبيون",
            "olympic competitors": "منافسون أولمبيون",
            "winter olympic competitors": "منافسون أولمبيون شتويون",
            "summer olympic competitors": "منافسون أولمبيون صيفيون",
            # competitors + countries
            "paralympic competitors for {en}": "منافسون بارالمبيون من {ar}",
            "olympic competitors for {en}": "منافسون أولمبيون من {ar}",
            "winter olympic competitors for {en}": "منافسون أولمبيون شتويون من {ar}",
            "summer olympic competitors for {en}": "منافسون أولمبيون صيفيون من {ar}",
        }
    )

    return formatted_data


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBaseV2:
    countries_from_nat_data = countries_from_nat | COUNTRY_LABEL_OVERRIDES
    countries_data = {x: {"ar": v} for x, v in countries_from_nat_data.items()}
    sports_data = {
        x: {
            "game_ar": v,
        }
        for x, v in medalists_data.items()
    }
    formatted_data = _build_formatted_data()

    r"""both_bot_ = format_multi_data_v2(
        formatted_data=formatted_data,
        data_list=sports_data,
        key_placeholder="{game_en}",
        data_list2=countries_data,
        key2_placeholder="{en}",
        text_after="",
        text_before="the ",
        regex_filter=r"[\w-]",
        search_first_part=True,
        use_other_formatted_data=True,
    )"""

    both_bot = format_multi_data_v2(
        formatted_data=formatted_data,
        data_list=countries_data,
        key_placeholder="{en}",
        data_list2=sports_data,
        key2_placeholder="{game_en}",
        text_after="",
        text_before="the ",
        regex_filter=r"[\w-]",
        search_first_part=True,
        use_other_formatted_data=True,
    )
    return both_bot


def fix_keys(category: str) -> str:
    normalized_category = category.lower()
    replacements = {
        "medallists": "medalists",
        "olympics": "olympic",
    }

    for old, new in replacements.items():
        normalized_category = normalized_category.replace(old, new)

    return normalized_category


@functools.lru_cache(maxsize=10000)
def resolve_countries_names_medalists(category: str) -> str:
    normalized_category = fix_keys(category)
    logger.debug(f"<<yellow>> start {normalized_category=}")

    nat_bot = _load_bot()
    result = nat_bot.search_all_category(normalized_category)

    logger.info(f"<<yellow>> end {normalized_category=}, {result=}")
    return result


__all__ = [
    "resolve_countries_names_medalists",
]
