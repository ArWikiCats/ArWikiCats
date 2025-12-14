#!/usr/bin/python3
"""

"""
import functools
from ...translations_formats import format_multi_data, MultiDataFormatterBase
from ...translations.by_type import (
    PRIMARY_BY_COMPONENTS,
    BY_TABLE_BASED,
    by_table_year,
    by_of_fields,
    by_and_fields,
    by_or_fields,
    by_by_fields,
    by_musics,
    by_map_table,
    by_under_keys,
    Music_By_table,
)

sports_formatted_data = {
    "by year - {en}": "حسب {ar}",
    "by {en}": "حسب {ar}",
    "by {en} or {en2}": "حسب {ar} أو {ar2}",
    "by {en} and {en2}": "حسب {ar} و{ar2}",
    "by {en} by {en2}": "حسب {ar} حسب {ar2}",
}
data_to_find = dict(BY_TABLE_BASED)
data_to_find.update(by_table_year)
data_to_find.update(Music_By_table)
data_to_find.update(by_under_keys)

by_data = PRIMARY_BY_COMPONENTS


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBase:
    both_bot = format_multi_data(
        formatted_data=sports_formatted_data,
        data_to_find=data_to_find,
        data_list=by_data,
        key_placeholder="{en}",
        value_placeholder="{ar}",
        data_list2=by_data,
        key2_placeholder="{en2}",
        value2_placeholder="{ar2}",
        text_after="",
        text_before="",
        search_first_part=False,
        use_other_formatted_data=False,
    )
    return both_bot


def resolve_by_labels(category: str) -> str:
    if sports_formatted_data.get(category):
        return sports_formatted_data[category]

    both_bot = _load_bot()
    result = both_bot.search_all_category(category)
    return result


__all__ = [
    "resolve_by_labels",
]
