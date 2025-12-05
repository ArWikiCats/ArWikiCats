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
        "{nat_en} {film_key} films": "أفلام {film_ar} {nat_ar}",
        "{nat_en} {film_key} television commercials": "إعلانات تجارية تلفزيونية {film_ar} {nat_ar}",
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


search_multi_cache = {
    "upcoming christmas": "{tyty} قادمة عيد الميلاد",
    "christmas upcoming": "{tyty} قادمة عيد الميلاد",
    "action comedy drama": "{tyty} حركة كوميدية درامية",
    "action comedy fiction": "{tyty} حركة كوميدية خيالية",
    "action comedy thriller": "{tyty} حركة كوميدية إثارة",
    "adult animated supernatural drama": "{tyty} رسوم متحركة خارقة للطبيعة للكبار درامية",
    "animated science fantasy": "{tyty} علمية رسوم متحركة فانتازيا",
    "animated science fiction": "{tyty} علمية رسوم متحركة خيالية",
    "black comedy drama": "{tyty} كوميدية سوداء درامية",
    "black comedy fiction": "{tyty} كوميدية سوداء خيالية",
    "black comedy horror": "{tyty} كوميدية سوداء رعب",
    "black comedy thriller": "{tyty} كوميدية سوداء إثارة",
    "children's animated science": "{tyty} رسوم متحركة أطفال علمية",
    "children's animated short": "{tyty} رسوم متحركة أطفال قصيرة",
    "children's comedy drama": "{tyty} أطفال كوميدية درامية",
    "children's comedy fiction": "{tyty} أطفال كوميدية خيالية",
    "children's comedy thriller": "{tyty} أطفال كوميدية إثارة",
    "crime comedy drama": "{tyty} جنائية كوميدية درامية",
    "crime comedy fiction": "{tyty} جنائية كوميدية خيالية",
    "crime comedy horror": "{tyty} جنائية كوميدية رعب",
    "crime comedy thriller": "{tyty} جنائية كوميدية إثارة",
    "criminal comedy drama": "{tyty} كوميديا الجريمة درامية",
    "criminal comedy fiction": "{tyty} كوميديا الجريمة خيالية",
    "criminal comedy horror": "{tyty} كوميديا الجريمة رعب",
    "criminal comedy thriller": "{tyty} كوميديا الجريمة إثارة",
    "musical comedy thriller": "{tyty} كوميديا موسيقية إثارة",
    "romantic comedy thriller": "{tyty} كوميديا رومانسية إثارة",
    "science fiction action thriller": "{tyty} خيال علمي وحركة إثارة",
}


@functools.lru_cache(maxsize=None)
def search_multi_new(text: str) -> str:
    if search_multi_cache.get(text.lower()):
        return search_multi_cache[text.lower()]

    bot = _make_bot()
    key = bot.other_bot.match_key(text)

    if not key:
        return ""

    label = bot.other_bot.get_key_label(key)

    if not label:
        return ""

    label = f"{{tyty}} {label}"

    return label


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
