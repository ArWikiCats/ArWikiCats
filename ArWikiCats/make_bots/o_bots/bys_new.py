#!/usr/bin/python3
"""

"""
import functools
from ...translations_formats import format_multi_data, MultiDataFormatterBase
from ...translations.by_type import (
    PRIMARY_BY_COMPONENTS,
    BY_TABLE_BASED,
)

sports_formatted_data = {
    "by {en}": "حسب {ar}",
    "by {en} or {en2}": "حسب {ar} أو {ar2}",
    "by {en} and {en2}": "حسب {ar} و{ar2}",
    "by {en} by {en2}": "حسب {ar} حسب {ar2}",
}

by_data = PRIMARY_BY_COMPONENTS | BY_TABLE_BASED


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBase:
    both_bot = format_multi_data(
        formatted_data=sports_formatted_data,
        data_list=by_data,
        key_placeholder="{en}",
        value_placeholder="{ar}",
        data_list2=by_data,
        key2_placeholder="{en2}",
        value2_placeholder="{ar2}",
        text_after="",
        text_before="the ",
        search_first_part=True,
        use_other_formatted_data=True,
    )
    return both_bot


def resolve_by_labels(category: str) -> str:
    both_bot = _load_bot()
    result = both_bot.search_all_category(category)
    return result


__all__ = [
    "resolve_by_labels",
]
