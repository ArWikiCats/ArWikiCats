#!/usr/bin/python3
"""

TODO:
    - use this file instead of film_keys_bot.py
    - add formated_data from ArWikiCats/translations/tv/films_mslslat.py

"""

import functools
from typing import Dict

from ...helps.log import logger
from ...translations import (
    Nat_women,
    film_keys_for_female,
)
from ...translations_formats import MultiDataFormatterBase, format_films_country_data


def _build_television_cao() -> tuple[Dict[str, str], Dict[str, str]]:
    """
    Build CAO (Characters, Albums, Organizations, etc.) mappings.

    Returns:
        - films_key_cao: translation mapping
        - data_no_nats: translation mapping without nationalities
    """
    data = {}
    data_no_nats = {}

    # Base TV keys with common suffixes
    for suffix, arabic_suffix in [
        ("characters", "شخصيات"),
        ("title cards", "بطاقات عنوان"),
        ("video covers", "أغلفة فيديو"),
        ("posters", "ملصقات"),
        ("images", "صور"),
    ]:
        data_no_nats.update(
            {
                f"{{film_key}} {suffix}": f"{arabic_suffix} {{film_ar}}",
            }
        )
        data.update(
            {
                f"{{nat_en}} {suffix}": f"{arabic_suffix} {{nat_ar}}",
                f"{{nat_en}} {{film_key}} {suffix}": f"{arabic_suffix} {{film_ar}} {{nat_ar}}",
            }
        )

    # Genre-based categories
    genre_categories = [
        ("anime and manga", "أنمي ومانغا"),
        ("compilation albums", "ألبومات تجميعية"),
        ("folk albums", "ألبومات فلكلورية"),
        ("classical albums", "ألبومات كلاسيكية"),
        ("comedy albums", "ألبومات كوميدية"),
        ("mixtape albums", "ألبومات ميكستايب"),
        ("soundtracks", "موسيقى تصويرية"),
        ("terminology", "مصطلحات"),
        ("television series", "مسلسلات تلفزيونية"),
        ("television episodes", "حلقات تلفزيونية"),
        ("television programs", "برامج تلفزيونية"),
        ("television programmes", "برامج تلفزيونية"),
        ("groups", "مجموعات"),
        ("novellas", "روايات قصيرة"),
        ("novels", "روايات"),
        ("films", "أفلام"),
    ]

    # Standard categories
    for suffix, arabic_base in genre_categories:
        data_no_nats.update(
            {
                f"{{film_key}} {suffix}": f"{arabic_base} {{film_ar}}",
                f"superhero {suffix}": f"{arabic_base} عن الأبطال الخارقين",
            }
        )
        data.update(
            {
                f"{{nat_en}} {suffix}": f"{arabic_base} {{nat_ar}}",
                f"{{nat_en}} {{film_key}} {suffix}": f"{arabic_base} {{film_ar}} {{nat_ar}}",
                f"{{nat_en}} superhero {suffix}": f"{arabic_base} {{nat_ar}} عن الأبطال الخارقين",
            }
        )

    return data, data_no_nats


@functools.lru_cache(maxsize=1)
def _make_bot() -> MultiDataFormatterBase:
    # Template data with both nationality and sport placeholders
    formatted_data = {
        # "{nat_en} films": "أفلام {nat_ar}", #  [2000s American films] : "تصنيف:أفلام أمريكية عقد 2000",
        "{nat_en} films": "أفلام {nat_ar}",

        # "Category:yemeni action Teen superhero films" : "تصنيف:أفلام حركة مراهقة يمنية عن الأبطال الخارقين",
        "{nat_en} {film_key} superhero films": "أفلام {film_ar} {nat_ar} عن الأبطال الخارقين",
        "{nat_en} superhero {film_key} films": "أفلام {film_ar} {nat_ar} عن الأبطال الخارقين",

        "{nat_en} television episodes": "حلقات تلفزيونية {nat_ar}",
        "{nat_en} television series": "مسلسلات تلفزيونية {nat_ar}",
        "{nat_en} television-seasons": "مواسم تلفزيونية {nat_ar}",
        "{nat_en} television seasons": "مواسم تلفزيونية {nat_ar}",
        "{nat_en} {film_key} television-seasons": "مواسم تلفزيونية {film_ar} {nat_ar}",
        "{nat_en} {film_key} television seasons": "مواسم تلفزيونية {film_ar} {nat_ar}",
        "{nat_en} {film_key} television series": "مسلسلات تلفزيونية {film_ar} {nat_ar}",
        "{nat_en} {film_key} filmszz": "أفلام {film_ar} {nat_ar}",
        "{nat_en} {film_key} films": "أفلام {film_ar} {nat_ar}",
        "{nat_en} {film_key} television commercials": "إعلانات تجارية تلفزيونية {film_ar} {nat_ar}",
        # TODO: move this to jobs bot?
        # "{nat_en} sports coaches": "مدربو رياضة {nat_ar}",
    }

    _data, data_no_nats = _build_television_cao()

    formatted_data.update(_data)

    other_formatted_data = {
        "{film_key} films": "أفلام {film_ar}",

        # "Category:action Teen superhero films" : "تصنيف:أفلام حركة مراهقة عن الأبطال الخارقين",
        "{film_key} superhero films": "أفلام {film_ar} عن الأبطال الخارقين",
        "superhero {film_key} films": "أفلام {film_ar} عن الأبطال الخارقين",
        "{film_key} television commercials": "إعلانات تجارية تلفزيونية {film_ar}",
    }
    other_formatted_data.update(data_no_nats)

    # film_keys_for_female
    data_list2 = {
        "action comedy": "حركة كوميدية",
        "action thriller": "إثارة حركة",
        "action": "حركة",
        "drama": "درامية",
        "upcoming": "قادمة",
        "horror": "رعب",
        "black-and-white": "أبيض وأسود",
        "psychological horror": "رعب نفسي",
    }

    put_label_last = {
        "low-budget",
        "supernatural",
        "christmas",
        "lgbtq-related",
        "upcoming",
    }
    data_list2 = dict(film_keys_for_female)
    data_list2.pop("television", None)
    data_list2.pop("superhero", None)

    bot = format_films_country_data(
        formatted_data=formatted_data,
        data_list=Nat_women,
        key_placeholder="{nat_en}",
        value_placeholder="{nat_ar}",
        data_list2=data_list2,
        key2_placeholder="{film_key}",
        value2_placeholder="{film_ar}",
        text_after="",
        text_before="",
        other_formatted_data=other_formatted_data,
    )

    bot.other_bot.update_put_label_last(put_label_last)

    return bot


@functools.lru_cache(maxsize=None)
def get_films_key_tyty_new(text: str) -> str:
    """
    Function to generate a films key based on the country identifier.
    Args:
        text (str): The country identifier string to process.
    Returns:
        str: The resolved label string, or empty string if no match is found.
    """
    normalized_text = text.lower().replace("category:", " ").strip()
    logger.debug(f"<<yellow>> start get_films_key_tyty_new: {normalized_text=}")
    bot = _make_bot()

    result = bot.search_all(normalized_text)
    logger.info_if_or_debug(f"<<yellow>> end get_films_key_tyty_new: {normalized_text=}, {result=}", result)
    return result
