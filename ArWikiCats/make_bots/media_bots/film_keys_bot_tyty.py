#!/usr/bin/python3
"""
TODO: replaced py ArWikiCats/make_bots/media_bots/tyty_new_format.py
"""

import functools

from ...helps.log import logger
from ...translations import (
    film_keys_for_female,
    Films_key_333,
    television_keys,
)

# sorted by len of " " in key
keys_female_sorted = dict(sorted(
    film_keys_for_female.items(),
    key=lambda k: (-k[0].count(" "), -len(k[0])),
))

put_label_last = {
    "low-budget",
    "christmas",
    "lgbtq-related",
    "upcoming",
}

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
def search_multi(text: str) -> str:
    if search_multi_cache.get(text.lower()):
        return search_multi_cache[text.lower()]

    for second_part, second_label in keys_female_sorted.items():
        # ---
        if not text.endswith(second_part.lower()):
            continue
        # ---
        first_part = text[: -len(second_part)].strip()
        # ---
        second_key_lower = second_part.lower()
        first_key_lower = first_part.lower()
        # ---
        first_label = film_keys_for_female.get(first_part, "")
        # ---
        logger.debug(f">??? search_multi: {first_part=} ({first_label}), {second_part=} ({second_label})")
        # ---
        if not first_label:
            continue

        paop_1 = f"{{tyty}} {first_label} {second_label}"

        # Adjust order for specific keywords
        if first_key_lower in put_label_last and second_key_lower not in put_label_last:
            paop_1 = f"{{tyty}} {second_label} {first_label}"

        search_multi_cache[f"{second_part} {first_part}"] = paop_1

        logger.info(f">??? search_multi: {paop_1=}")

        return paop_1

    return ""


@functools.lru_cache(maxsize=None)
# @dump_data(1)
def get_films_key_tyty(country_identifier: str) -> str:
    """
    Resolve labels for composite television keys used in film lookups.
    TODO: use FormatData
    """

    logger.debug(f'<<lightblue>> get_Films_key_CAO : {country_identifier=} ')
    normalized_identifier = country_identifier.lower().strip()

    for suffix, suffix_translation in television_keys.items():
        if not normalized_identifier.endswith(suffix.lower()):
            continue

        prefix = normalized_identifier[: -len(suffix)].strip()
        logger.debug(f'<<lightblue>> {prefix=}, endswith:"{suffix}" ')

        prefix_label = Films_key_333.get(prefix.strip())

        if prefix_label:
            resolved_label = f"{suffix_translation} {prefix_label}"
            logger.info(f'<<lightblue>> get_films_key_tyty: new {resolved_label=} ')
            return resolved_label

        prefix_label = search_multi(prefix.strip())

        if prefix_label and "{tyty}" in prefix_label:
            resolved_label = prefix_label.format(tyty=suffix_translation)
            logger.info(f'<<lightblue>> get_films_key_tyty: new {resolved_label=} ')
            return resolved_label

    return ""
