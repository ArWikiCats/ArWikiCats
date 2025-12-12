"""Resolve Arabic labels for army-related categories."""

from __future__ import annotations

import functools
from ..translations_formats import format_multi_data_v2, MultiDataFormatterBaseV2
from ..translations import all_country_with_nat_ar, ministrs_keys


nat_secretaries_mapping = {
    "secretaries of {en} department of {ministry}": "وزراء {singular} {males}",
}

en_secretaries_mapping = {
    "united states secretaries of state": "وزراء خارجية أمريكيون",
    "secretaries of state of {en}": "وزراء خارجية {males}",
    "secretaries of state for {en}": "وزراء خارجية {males}",

    "{en} assistant secretaries of {ministry}": "مساعدو وزير {al} {the_male}",
    "{en} under secretaries of {ministry}": "نواب وزير {al} {the_male} للشؤون المتخصصة",
    "{en} deputy secretaries of {ministry}": "نواب وزير {al} {the_male}",

    "assistant secretaries of {ministry} of {en}": "مساعدو وزير {al} {the_male}",
    "under secretaries of {ministry} of {en}": "نواب وزير {al} {the_male} للشؤون المتخصصة",
    "deputy secretaries of {ministry} of {en}": "نواب وزير {al} {the_male}",

    "{en} secretaries of {ministry}" : "وزراء {singular} {males}",
    "secretaries of {ministry} of {en}" : "وزراء {singular} {males}",
    "secretaries of {ministry}" : "وزراء {singular}",

    "state lieutenant governors of {en}": "نواب حكام الولايات في {ar}",
    "state secretaries of state of {en}": "وزراء خارجية الولايات في {ar}",
    "state cabinet secretaries of {en}" : "أعضاء مجلس وزراء {ar}",

}


def remove_the(text: str) -> str:
    if text.lower().startswith("the "):
        return text[4:]
    return text


@functools.lru_cache(maxsize=1)
def _load_nats_bot() -> MultiDataFormatterBaseV2:
    nats_data = {
        x: v
        for x, v in all_country_with_nat_ar.items()
        if v.get("ar") and v.get("en")
    }

    nat_secretaries_mapping.update({
        x.replace("secretaries of", "secretaries-of"): y
        for x, y in nat_secretaries_mapping.items()
        if "secretaries of" in x
    })

    both_bot = format_multi_data_v2(
        formatted_data=nat_secretaries_mapping,
        data_list=nats_data,
        key_placeholder="{en}",
        data_list2=ministrs_keys,
        key2_placeholder="{ministry}",
        text_after="",
        text_before="the ",
        search_first_part=True,
        use_other_formatted_data=True,
    )
    return both_bot


@functools.lru_cache(maxsize=1)
def _load_countries_names_bot() -> MultiDataFormatterBaseV2:
    countries_data = {
        remove_the(v["en"]): v
        for x, v in all_country_with_nat_ar.items()
        if v.get("ar") and v.get("en")
    }

    countries_data.update({
        "ireland": {
            "male": "أيرلندي",
            "males": "أيرلنديون",
            "female": "أيرلندية",
            "females": "أيرلنديات",
            "en": "ireland",
            "ar": "أيرلندا",
            "the_female": "الأيرلندية",
            "the_male": "الأيرلندي"
        }
    })

    en_secretaries_mapping.update({
        x.replace("secretaries of", "secretaries-of"): y
        for x, y in en_secretaries_mapping.items()
        if "secretaries of" in x
    })

    both_bot = format_multi_data_v2(
        formatted_data=en_secretaries_mapping,
        data_list=countries_data,
        key_placeholder="{en}",
        data_list2=ministrs_keys,
        key2_placeholder="{ministry}",
        text_after="",
        text_before="the ",
        search_first_part=True,
        use_other_formatted_data=True,
    )
    return both_bot


def resolve_secretaries_labels_nats(category: str) -> str:
    _bot = _load_nats_bot()
    result = _bot.search_all_category(category)
    return result


def resolve_secretaries_labels(category: str) -> str:
    both_bot = _load_countries_names_bot()
    result = both_bot.search_all_category(category) or resolve_secretaries_labels_nats(category)
    return result


__all__ = [
    "resolve_secretaries_labels"
]
