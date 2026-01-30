#!/usr/bin/python3
""" """

import functools
import logging
import re

from ...translations import (
    COMPLEX_LANGUAGE_TRANSLATIONS,
    PRIMARY_LANGUAGE_TRANSLATIONS,
    TELEVISION_KEYS,
    Films_key_CAO,
    film_keys_for_female,
)
from ...translations_formats import MultiDataFormatterBase, format_films_country_data

logger = logging.getLogger(__name__)

new_data = PRIMARY_LANGUAGE_TRANSLATIONS | COMPLEX_LANGUAGE_TRANSLATIONS


def add_definite_article(label: str) -> str:
    """Prefix each word in ``label`` with the Arabic definite article."""
    label = re.sub(r" ال", " ", f" {label} ").strip()
    label_without_article = re.sub(r" ", " ال", label)
    new_label = f"ال{label_without_article}"
    return new_label


@functools.lru_cache(maxsize=1)
def _make_bot() -> MultiDataFormatterBase:
    films_formatted_data = {
        "{lang_en} language {film_en} films": "أفلام {film_ar} باللغة {lang_al}",
    }
    _put_label_last = {
        "low-budget",
        "supernatural",
        "christmas",
        "lgbtq-related",
        "upcoming",
    }
    to_find = TELEVISION_KEYS | Films_key_CAO

    data = {x: add_definite_article(v) for x, v in new_data.items()}
    bot = format_films_country_data(
        formatted_data=films_formatted_data,
        data_list=data,
        key_placeholder="{lang_en}",
        value_placeholder="{lang_al}",
        data_list2=film_keys_for_female,
        key2_placeholder="{film_en}",
        value2_placeholder="{film_ar}",
        text_after="",
        text_before="",
        data_to_find=to_find,
        # other_formatted_data=other_formatted_data,
    )

    # bot.other_bot.update_put_label_last(put_label_last)

    return bot


def fix_keys(category: str) -> str:
    category = category.lower().replace("category:", "").replace("'", "")
    category = category.replace("-language ", " language ")
    return category


@functools.lru_cache(maxsize=10000)
def resolve_films_languages_labels(category: str) -> str:
    logger.debug(f"<<yellow>> start {category=}")

    category = fix_keys(category)

    result = _make_bot().search_all_category(category)

    logger.info(f"<<yellow>> end {category=}, {result=}")
    return result


__all__ = [
    "resolve_films_languages_labels",
]
