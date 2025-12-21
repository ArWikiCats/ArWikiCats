#!/usr/bin/python3
"""
Resolve medalists categories translations
"""
from typing import Dict
import functools
from ...helps import logger
from ...translations_formats import format_multi_data_v2, MultiDataFormatterBaseV2
from ...translations import countries_from_nat, COUNTRY_LABEL_OVERRIDES


# TODO: add data from ArWikiCats/translations/sports/olympics_data.py
medalists_data = {
    "central-american-and-caribbean-games": "ألعاب أمريكا الوسطى والكاريبي",
    # "central american and caribbean games": "ألعاب أمريكا الوسطى والكاريبي",
    "african games": "الألعاب الإفريقية",
    "all-africa games": "ألعاب عموم إفريقيا",
    "asian games": "الألعاب الآسيوية",
    "central american games": "ألعاب أمريكا الوسطى",
    "commonwealth games": "ألعاب الكومنولث",
    "deaflympic games": "ألعاب ديفلمبياد",
    "european youth olympic winter": "الألعاب الأولمبية الشبابية الأوروبية الشتوية",
    "european youth olympic": "الألعاب الأولمبية الشبابية الأوروبية",
    "islamic solidarity games": "ألعاب التضامن الإسلامي",
    "jeux de la francophonie": "الألعاب الفرانكوفونية",
    "military world games": "دورة الألعاب العسكرية",
    "olympic games": "الألعاب الأولمبية",
    "olympics": "الألعاب الأولمبية",
    "pan american games": "دورة الألعاب الأمريكية",
    "paralympics games": "الألعاب البارالمبية",
    "south american games": "ألعاب أمريكا الجنوبية",
    "universiade": "الألعاب الجامعية",
    "world games": "دورة الألعاب العالمية",
    "youth olympic games": "الألعاب الأولمبية الشبابية",
    "youth olympics": "الألعاب الأولمبية الشبابية",
}


SUMMER_WINTER_GAMES = {
    "african games": "الألعاب الإفريقية",
    "asian beach games": "دورة الألعاب الآسيوية الشاطئية",
    "asian games": "الألعاب الآسيوية",
    "asian para games": "الألعاب البارالمبية الآسيوية",
    "asian summer games": "الألعاب الآسيوية الصيفية",
    "asian winter games": "الألعاب الآسيوية الشتوية",
    "bolivarian games": "الألعاب البوليفارية",
    "central american and caribbean games": "ألعاب أمريكا الوسطى والكاريبي",
    "central american games": "ألعاب أمريكا الوسطى",
    "commonwealth games": "ألعاب الكومنولث",
    "commonwealth youth games": "ألعاب الكومنولث الشبابية",
    "european games": "الألعاب الأوروبية",
    "european youth olympic winter": "الألعاب الأولمبية الشبابية الأوروبية الشتوية",
    "european youth olympic": "الألعاب الأولمبية الشبابية الأوروبية",
    "fis nordic world ski championships": "بطولة العالم للتزلج النوردي على الثلج",
    "friendship games": "ألعاب الصداقة",
    "goodwill games": "ألعاب النوايا الحسنة",
    "islamic solidarity games": "ألعاب التضامن الإسلامي",
    "maccabiah games": "الألعاب المكابيه",
    "mediterranean games": "الألعاب المتوسطية",
    "micronesian games": "الألعاب الميكرونيزية",
    "military world games": "دورة الألعاب العسكرية",
    "asian indoor games": "دورة الألعاب الآسيوية داخل الصالات",
    "pan american games": "دورة الألعاب الأمريكية",
    "pan arab games": "دورة الألعاب العربية",
    "pan asian games": "دورة الألعاب الآسيوية",
    "paralympic": "الألعاب البارالمبية",
    "paralympics": "الألعاب البارالمبية",
    "parapan american games": "ألعاب بارابان الأمريكية",
    "sea games": "ألعاب البحر",
    "south american games": "ألعاب أمريكا الجنوبية",
    "south asian beach games": "دورة ألعاب جنوب أسيا الشاطئية",
    "south asian games": "ألعاب جنوب أسيا",
    "south asian winter games": "ألعاب جنوب آسيا الشتوية",
    "southeast asian games": "ألعاب جنوب شرق آسيا",
    "summer olympics": "الألعاب الأولمبية الصيفية",
    "summer universiade": "الألعاب الجامعية الصيفية",
    "summer world university games": "ألعاب الجامعات العالمية الصيفية",
    "the universiade": "الألعاب الجامعية",
    "universiade": "الألعاب الجامعية",
    "winter olympics": "الألعاب الأولمبية الشتوية",
    "winter universiade": "الألعاب الجامعية الشتوية",
    "winter world university games": "ألعاب الجامعات العالمية الشتوية",
    "world championships": "بطولات العالم",
    "youth olympic": "الألعاب الأولمبية الشبابية",
    "youth olympics games": "الألعاب الأولمبية الشبابية",
    "youth olympics": "الألعاب الأولمبية الشبابية",
    "deaflympic games": "ألعاب ديفلمبياد",
}

medalists_data.update(SUMMER_WINTER_GAMES)


def _build_formatted_data() -> Dict[str, str]:
    # NOTE: formatted_data used in other resolver
    formatted_data: Dict[str, str] = {
        "olympic gold medalists for {en}": "فائزون بميداليات ذهبية أولمبية من {ar}",
        "olympic gold medalists for {en} in alpine skiing": "فائزون بميداليات ذهبية أولمبية من {ar} في التزلج على المنحدرات الثلجية",
    }

    base_formatted_data = {
        "{game_en}": "{game_ar}",
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
        formatted_data[f"winter {base_key}"] = f"{base_label} الشتوية"
        formatted_data[f"summer {base_key}"] = f"{base_label} الصيفية"
        formatted_data[f"west {base_key}"] = f"{base_label} الغربية"
        formatted_data[f"east {base_key}"] = f"{base_label} الشرقية"

    return formatted_data


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBaseV2:
    countries_from_nat_data = countries_from_nat | COUNTRY_LABEL_OVERRIDES
    countries_data = {
        x: {"ar": v}
        for x, v in countries_from_nat_data.items()
    }
    sports_data = {
        x: {
            "game_ar": v,
        }
        for x, v in medalists_data.items()
    }
    formatted_data = _build_formatted_data()
    both_bot = format_multi_data_v2(
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
    )
    return both_bot


@functools.lru_cache(maxsize=10000)
def resolve_countries_names_medalists(category: str) -> str:
    logger.debug(f"<<yellow>> start resolve_countries_names_medalists: {category=}")

    nat_bot = _load_bot()
    result = nat_bot.search_all_category(category)

    logger.debug(f"<<yellow>> end resolve_countries_names_medalists: {category=}, {result=}")
    return result


__all__ = [
    "resolve_countries_names_medalists",
]
