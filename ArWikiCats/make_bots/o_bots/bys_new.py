#!/usr/bin/python3
"""
TODO: still has some issues to resolve with some labels

"""
import re
import functools
from ...helps import logger
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
    ADDITIONAL_BY_COMPONENTS,
    CONTEXT_FIELD_LABELS,
)

formatted_data = {
    "by {en} and city of setting": "حسب {ar} ومدينة الأحداث",
    "by {en} and city-of {en2}": "حسب {ar} ومدينة {ar2}",
    "by year - {en}": "حسب {ar}",
    "by {en}": "حسب {ar}",
    "by {en2}": "حسب {ar2}",
    "by {en} or {en2}": "حسب {ar} أو {ar2}",

    "by {en} and {en2}": "حسب {ar} و{ar2}",
    "by {en} and {en}": "حسب {ar} و{ar}",

    "by {en2} and {en}": "حسب {ar2} و{ar}",
    "by {en} by {en2}": "حسب {ar} حسب {ar2}",
}

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

for context_key, context_label in CONTEXT_FIELD_LABELS.items():
    formatted_data[f"by {context_key} of {{en}}"] = f"حسب {context_label} {{ar}}"
    # # formatted_data[f"by {{en2}} and {context_key} of {{en}}"] = f"حسب {{ar2}} و{context_label} {{ar}}"
    # # formatted_data[f"by {{en}} and {context_key} of {{en2}}"] = f"حسب {{ar}} و{context_label} {{ar2}}"
    # ---
    formatted_data[f"by {context_key}-of {{en}}"] = f"حسب {context_label} {{ar}}"
    formatted_data[f"by {{en2}} and {context_key}-of {{en}}"] = f"حسب {{ar2}} و{context_label} {{ar}}"
    formatted_data[f"by {{en}} and {context_key}-of {{en2}}"] = f"حسب {{ar}} و{context_label} {{ar2}}"

# formatted_data.update(by_of_keys_2)

data_to_find = dict(BY_TABLE_BASED)
data_to_find.update(by_table_year)
data_to_find.update(Music_By_table)
data_to_find.update(by_under_keys)

by_data_new = dict(PRIMARY_BY_COMPONENTS)
by_data_new.update(ADDITIONAL_BY_COMPONENTS)
# by_data_new.update({x: v for x, v in CONTEXT_FIELD_LABELS.items() if x not in PRIMARY_BY_COMPONENTS})

by_data_new.update({
    "nonprofit organization": "المؤسسات غير الربحية",
    "shooting location": "موقع التصوير",
    "developer": "التطوير",
    "location": "الموقع",
    "setting": "الأحداث",
    "country of residence": "بلد الإقامة",
    "disestablishment": "الانحلال",
    "reestablishment": "إعادة التأسيس",
    "establishment": "التأسيس",
    "setting location": "موقع الأحداث",
    "invention": "الاختراع",
    "introduction": "الاستحداث",
    "formal description": "الوصف",
    "photographing": "التصوير",
    "completion": "الانتهاء",
    "opening": "الافتتاح",
})


@functools.lru_cache(maxsize=1)
def _load_bot() -> MultiDataFormatterBase:

    both_bot = format_multi_data(
        formatted_data=formatted_data,
        data_list=by_data_new,
        key_placeholder="{en}",
        value_placeholder="{ar}",
        data_list2=dict(by_data_new),
        key2_placeholder="{en2}",
        value2_placeholder="{ar2}",
        text_after="",
        text_before="",
        search_first_part=False,
        use_other_formatted_data=False,
        data_to_find=data_to_find,
        regex_filter=r"[\w-]",
    )
    return both_bot


def fix_keys(label: str) -> str:
    """Fix common issues in keys before processing."""

    context_keys = "|".join(CONTEXT_FIELD_LABELS.keys())
    label = re.sub(f"({context_keys}) of", r"\g<1>-of", label, flags=re.I)

    return label


@functools.lru_cache(maxsize=10000)
def resolve_by_labels(category: str) -> str:
    # if formatted_data.get(category): return formatted_data[category]
    category = fix_keys(category)
    logger.debug(f"<<yellow>> start resolve_by_labels: {category=}")
    both_bot = _load_bot()
    result = both_bot.search_all_category(category)
    logger.debug(f"<<yellow>> end resolve_by_labels: {category=}, {result=}")
    return result


__all__ = [
    "resolve_by_labels",
]
