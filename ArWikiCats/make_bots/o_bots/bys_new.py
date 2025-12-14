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
    CONTEXT_FIELD_LABELS,
)

sports_formatted_data = {
    "by year - {en}": "حسب {ar}",
    "by {en}": "حسب {ar}",
    "by {en} or {en2}": "حسب {ar} أو {ar2}",
    "by {en} and {en2}": "حسب {ar} و{ar2}",
    "by {en} by {en2}": "حسب {ar} حسب {ar2}",
}

by_of_keys = {
    "by {en} of shooting location": "حسب {ar} التصوير",
    "by {en} of developer": "حسب {ar} التطوير",
    "by {en} of location": "حسب {ar} الموقع",
    "by {en} of setting": "حسب {ar} الأحداث",
    "by {en} of disestablishment": "حسب {ar} الانحلال",
    "by {en} of reestablishment": "حسب {ar} إعادة التأسيس",
    "by {en} of establishment": "حسب {ar} التأسيس",
    "by {en} of setting location": "حسب {ar} موقع الأحداث",
    "by {en} of invention": "حسب {ar} الاختراع",
    "by {en} of introduction": "حسب {ar} الاستحداث",
    "by {en} of formal description": "حسب {ar} الوصف",
    "by {en} of photographing": "حسب {ar} التصوير",
    # "by photographing {en} ": "حسب {ar} التصوير",
    "by {en} of completion": "حسب {ar} الانتهاء",
    "by {en} of opening": "حسب {ar} الافتتاح",
}
# sports_formatted_data.update(by_of_keys)

by_of_keys_2 = {
    "by city of {en}": "حسب مدينة {ar}",
    "by date of {en}": "حسب تاريخ {ar}",
    "by country of {en}": "حسب بلد {ar}",
    "by continent of {en}": "حسب قارة {ar}",
    "by location of {en}": "حسب موقع {ar}",
    "by period of {en}": "حسب حقبة {ar}",
    "by time of {en}": "حسب وقت {ar}",
    "by year of {en}": "حسب سنة {ar}",
    "by decade of {en}": "حسب عقد {ar}",
    "by era of {en}": "حسب عصر {ar}",
    "by millennium of {en}": "حسب ألفية {ar}",
    "by century of {en}": "حسب قرن {ar}",
}

sports_formatted_data.update(by_of_keys_2)

data_to_find = dict(BY_TABLE_BASED)
data_to_find.update(by_table_year)
data_to_find.update(Music_By_table)
data_to_find.update(by_under_keys)

by_data_new = PRIMARY_BY_COMPONENTS
by_data_new.update({x: v for x, v in CONTEXT_FIELD_LABELS.items() if x not in PRIMARY_BY_COMPONENTS})


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBase:
    both_bot = format_multi_data(
        formatted_data=sports_formatted_data,
        data_to_find=data_to_find,
        data_list=by_data_new,
        key_placeholder="{en}",
        value_placeholder="{ar}",
        data_list2=by_data_new,
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
