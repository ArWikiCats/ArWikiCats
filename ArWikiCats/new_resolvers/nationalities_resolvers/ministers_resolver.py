"""Resolve Arabic labels for army-related categories."""

from __future__ import annotations

import functools

import logging
from ...translations import all_country_with_nat_ar, ministers_keys
from ...translations_formats import MultiDataFormatterBaseV2, format_multi_data_v2
from ..nats_as_country_names import nats_keys_as_country_names

logger = logging.getLogger(__name__)

nat_secretaries_mapping = {
    # Category:Secretaries of the Australian Department of Defence
    "secretaries of {en} department of {ministry}": "وزراء {no_al} {males}",
    "{en} secretaries of {ministry}": "وزراء {no_al} {males}",
    "{en} ministers of {ministry}": "وزراء {no_al} {males}",
    "{en} government ministers of {ministry}": "وزراء {no_al} {males}",
    "{en} female secretaries of {ministry}": "وزيرات {no_al} {females}",
    "{en} womens secretaries of {ministry}": "وزيرات {no_al} {females}",
    "{en} women's secretaries of {ministry}": "وزيرات {no_al} {females}",
    "{en} women secretaries of {ministry}": "وزيرات {no_al} {females}",
    "{en} women government ministers of {ministry}": "وزيرات {no_al} {females}",
    "{en} women government ministers": "وزيرات {no_al} {females}",
}

en_secretaries_mapping = {
    "ministers for {ministry} of {en}": "وزراء {no_al} {ar}",
    "ministers of {ministry} for {en}": "وزراء {no_al} {ar}",
    "ministers of {ministry} of {en}": "وزراء {no_al} {ar}",
    "women government ministers of {en}": "وزيرات {females}",
    # "Category:Foreign ministers of Monaco" : "تصنيف:وزراء خارجية موناكو",
    "{ministry} ministers of {en}": "وزراء {no_al} {ar}",
    "ministers of {ministry}": "وزراء {no_al}",
    "ministers for {ministry}": "وزراء {no_al}",
    "secretaries of {ministry}": "وزراء {no_al}",
    "secretaries of {en}": "وزراء {ar}",
    "ministries of the government of {en}": "وزارات حكومة {ar}",
    "united states secretaries of state": "وزراء خارجية أمريكيون",
    "secretaries of state of {en}": "وزراء خارجية {males}",
    "secretaries of state for {en}": "وزراء خارجية {males}",
    # Category:Department of Defence (Australia)
    "department of {ministry} ({en})": "وزارة {with_al} {the_female}",
    # Category:United States Department of Energy National Laboratories personnel
    "{en} department of {ministry}": "وزارة {with_al} {the_female}",
    "{en} department of {ministry} laboratories personnel": "موظفو مختبرات وزارة {with_al} {the_female}",
    "{en} department of {ministry} national laboratories personnel": "موظفو مختبرات وزارة {with_al} {the_female}",
    "{en} department of {ministry} national laboratories": "مختبرات وزارة {with_al} {the_female}",
    # Category:United States Department of Education agencies
    "{en} department of {ministry} officials": "مسؤولو وزارة {with_al} {the_female}",
    "{en} department of {ministry} agencies": "وكالات وزارة {with_al} {the_female}",
    "{en} department of {ministry} facilities": "مرافق وزارة {with_al} {the_female}",
    # Category:Ministry of Defense (Yemen)
    "ministry of {ministry} ({en})": "وزارة {with_al} {the_female}",
    # category:ministries of education
    "ministries of {ministry}": "وزارات {no_al}",
    "{ministry} ministries": "وزارات {no_al}",
    "{en} assistant secretaries of {ministry}": "مساعدو وزير {with_al} {the_male}",
    "{en} under secretaries of {ministry}": "نواب وزير {with_al} {the_male} للشؤون المتخصصة",
    "{en} deputy secretaries of {ministry}": "نواب وزير {with_al} {the_male}",
    "{en} deputy secretaries of state": "نواب وزير الخارجية {the_male}",
    "assistant secretaries of {ministry} of {en}": "مساعدو وزير {with_al} {the_male}",
    "under secretaries of {ministry} of {en}": "نواب وزير {with_al} {the_male} للشؤون المتخصصة",
    "deputy secretaries of {ministry} of {en}": "نواب وزير {with_al} {the_male}",
    "{en} secretaries of {ministry}": "وزراء {no_al} {males}",
    "secretaries of {ministry} of {en}": "وزراء {no_al} {males}",
    "state lieutenant governors of {en}": "نواب حكام الولايات في {ar}",
    "state secretaries of state of {en}": "وزراء خارجية الولايات في {ar}",
    "state cabinet secretaries of {en}": "أعضاء مجلس وزراء {ar}",
}


@functools.lru_cache(maxsize=1)
def _load_nats_bot() -> MultiDataFormatterBaseV2:
    nats_data = {x: v for x, v in all_country_with_nat_ar.items() if v.get("ar") and v.get("en")}

    both_bot = format_multi_data_v2(
        formatted_data=nat_secretaries_mapping,
        data_list=nats_data,
        key_placeholder="{en}",
        data_list2=ministers_keys,
        key2_placeholder="{ministry}",
        text_after="",
        text_before="the ",
        search_first_part=True,
        use_other_formatted_data=True,
    )
    return both_bot


@functools.lru_cache(maxsize=1)
def _load_countries_names_bot() -> MultiDataFormatterBaseV2:
    countries_data = {v["en"]: v for x, v in all_country_with_nat_ar.items() if v.get("ar") and v.get("en")}

    countries_data.update(nats_keys_as_country_names)

    countries_data.update({v["en"]: v for x, v in nats_keys_as_country_names.items() if v.get("ar") and v.get("en")})

    both_bot = format_multi_data_v2(
        formatted_data=en_secretaries_mapping,
        data_list=countries_data,
        key_placeholder="{en}",
        data_list2=ministers_keys,
        key2_placeholder="{ministry}",
        text_after="",
        text_before="the ",
        search_first_part=True,
        use_other_formatted_data=True,
    )
    return both_bot


@functools.lru_cache(maxsize=10000)
def _nats(category: str) -> str:
    _bot = _load_nats_bot()
    result = _bot.search_all_category(category)
    return result


@functools.lru_cache(maxsize=10000)
def _names(category: str) -> str:
    both_bot = _load_countries_names_bot()
    result = both_bot.search_all_category(category)
    return result


def fix_keys(text: str) -> str:
    text = text.replace("'", "")
    text = text.replace("ministers-of", "ministers of").replace("ministers-for", "ministers for")
    text = text.replace("secretaries-of", "secretaries of")
    return text


@functools.lru_cache(maxsize=10000)
def resolve_secretaries_labels(category: str) -> str:
    logger.debug(f"<<yellow>> start resolve_secretaries_labels: {category=}")
    category = fix_keys(category)
    result = _names(category) or _nats(category)
    logger.info_if_or_debug(f"<<yellow>> end resolve_secretaries_labels: {category=}, {result=}", result)
    return result


__all__ = ["resolve_secretaries_labels"]
