#!/usr/bin/python3
"""

"""

import functools

from typing import Dict
from ...helps import len_print
from ...helps.jsonl_dump import dump_data
from ...helps.log import logger
from ...translations import (
    film_Keys_for_female,
    Films_key_333,
    television_keys,
)

from ...translations_formats import MultiDataFormatterBase, format_multi_data

# sorted by len of " " in key
keys_female_sorted = dict(sorted(film_Keys_for_female.items(), key=lambda x: x[0].count(" "), reverse=True))


def _extend_Films_key_333(
    films_key_333: Dict[str, str],
    female_keys: Dict[str, str],
) -> Dict[str, str]:
    """Generate combined female-only film keys based on existing female mappings.

    This function takes a base female mapping (films_key_333) and extends it
    by creating pairwise combinations of the provided female_keys entries.

    Example combination:
        horror + comedy films  ->  "{tyty} أفلام رعب كوميدية"
    """
    data: Dict[str, str] = {}
    films_first = {
        "low-budget",
        "christmas",
        "lgbtq-related",
        "lgbt-related",
        "lgbtqrelated",
        "lgbtrelated",
        "upcoming",
    }

    placeholder = "{tyty}"

    for first_key, first_label in female_keys.items():
        ke_lower = first_key.lower()

        for second_key, second_label in female_keys.items():
            ke2_lower = second_key.lower()
            if ke2_lower == ke_lower:
                continue

            paop_1 = f"{placeholder} {first_label} {second_label}"
            paop_2 = f"{placeholder} {second_label} {first_label}"

            # Adjust order for specific keywords
            if ke_lower in films_first:
                paop_1 = f"{placeholder} {second_label} {first_label}"
                paop_2 = paop_1
            elif ke2_lower in films_first:
                paop_1 = f"{placeholder} {first_label} {second_label}"
                paop_2 = paop_1

            data[f"{first_key} {second_key}"] = paop_1
            data[f"{second_key} {first_key}"] = paop_2

    new_data = {x: v for x, v in data.items() if x not in films_key_333}
    return new_data


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBase:
    return format_multi_data(
        formatted_data={
            "{en1} {en2}": "<ar1> <ar2>"
        },
        data_list=film_Keys_for_female,
        data_list2=film_Keys_for_female,
        key_placeholder="{en1}",
        value_placeholder="<ar1>",
        key2_placeholder="{en2}",
        value2_placeholder="<ar2>",
    )


def search_multi_bot(text: str) -> str:
    bot = _load_bot()
    label = bot.search(text)
    return label


def search_multi(text: str) -> str:
    label = ""
    for suffix, suffix_label in keys_female_sorted.items():
        # ---
        if not text.endswith(suffix.lower()):
            continue
        # ---
        prefix = text[: -len(suffix)].strip()
        # ---
        prefix_label = film_Keys_for_female.get(prefix, "")
        # ---
        logger.debug(f">??? search_multi: {prefix=} ({prefix_label}), {suffix=} ({suffix_label})")
        # ---
        if not prefix_label:
            continue
        # ---

    return label


@functools.lru_cache(maxsize=None)
@dump_data(1)
def get_films_key_tyty(country_identifier: str) -> str:
    """
    Resolve labels for composite television keys used in film lookups.
    TODO: use FormatData
    """

    logger.debug(f'<<lightblue>> get_Films_key_CAO : {country_identifier=} ')
    normalized_identifier = country_identifier.lower().strip()

    # tyty_data = _extend_Films_key_333(Films_key_333, film_Keys_for_female)

    for suffix, suffix_translation in television_keys.items():
        if not normalized_identifier.endswith(suffix.lower()):
            continue

        prefix = normalized_identifier[: -len(suffix)].strip()
        logger.debug(f'<<lightblue>> {prefix=}, endswith:"{suffix}" ')
        # prefix_label = tyty_data.get(prefix.strip(), "")
        prefix_label = search_multi(prefix.strip())

        if prefix_label and "{tyty}" in prefix_label:
            resolved_label = prefix_label.format(tyty=suffix_translation)
            logger.info(f'<<lightblue>> get_Films_key_CAO: new {resolved_label=} ')
            return resolved_label

    return ""


tyty_data = _extend_Films_key_333(Films_key_333, film_Keys_for_female)

len_print.data_len(
    "films_mslslat.py",
    {
        "tyty_data": tyty_data,
    },
)
