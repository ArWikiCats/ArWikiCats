#!/usr/bin/python3
"""

"""

import functools

from ...helps.log import logger
from ...translations_formats import format_films_country_data, MultiDataFormatterBase
from ...translations import (
    Nat_women,
    film_keys_for_female,
)


@functools.lru_cache(maxsize=1)
def _make_bot() -> MultiDataFormatterBase:
    # Template data with both nationality and sport placeholders
    formatted_data = {
        # "{nat_en} films": "أفلام {nat_ar}", #  [2000s American films] : "تصنيف:أفلام أمريكية عقد 2000",
        "{nat_en} films": "أفلام {nat_ar}",

        "{nat_en} television episodes": "حلقات تلفزيونية {nat_ar}",
        "{nat_en} television series": "مسلسلات تلفزيونية {nat_ar}",

        "{nat_en} television-seasons": "مواسم تلفزيونية {nat_ar}",
        "{nat_en} television seasons": "مواسم تلفزيونية {nat_ar}",

        "{nat_en} {film_key} television-seasons": "مواسم تلفزيونية {film_ar} {nat_ar}",
        "{nat_en} {film_key} television seasons": "مواسم تلفزيونية {film_ar} {nat_ar}",

        "{nat_en} {film_key} films": "أفلام {film_ar} {nat_ar}",
        "{nat_en} {film_key} television commercials": "إعلانات تجارية تلفزيونية {film_ar} {nat_ar}",

        # TODO: move this to jobs bot?
        # "{nat_en} sports coaches": "مدربو رياضة {nat_ar}",
    }
    other_formatted_data = {
        "{film_key} films": "أفلام {film_ar}",
        "{film_key} television commercials": "إعلانات تجارية تلفزيونية {film_ar}",
    }

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
        "christmas",
        "lgbtq-related",
        "upcoming",
    }

    bot = format_films_country_data(
        formatted_data=formatted_data,
        data_list=Nat_women,
        key_placeholder="{nat_en}",
        value_placeholder="{nat_ar}",
        data_list2=film_keys_for_female,
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
    logger.debug(f'<<lightblue>> get_Films_key_CAO : {text=} ')
    normalized_text = text.lower().strip()
    bot = _make_bot()

    return bot.search_all(normalized_text)
