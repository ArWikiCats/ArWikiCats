#!/usr/bin/python3
"""
Resolves category labels for religious groups combined with nationalities.
TODO: write code
"""

import functools
import re
from ArWikiCats.translations import RELIGIOUS_KEYS_PP, Nat_mens, Nat_Womens
from ArWikiCats.translations.jobs.jobs_data_basic import PAINTER_ROLE_LABELS
from ArWikiCats.translations_formats import format_multi_data, FormatData

# Prepare dictionaries
_rel_males = {k: v["males"] for k, v in RELIGIOUS_KEYS_PP.items() if v.get("males")}
_rel_females = {k: v["females"] for k, v in RELIGIOUS_KEYS_PP.items() if v.get("females")}

# Extended roles for the test cases
_jobs_males = {k: v["males"] for k, v in PAINTER_ROLE_LABELS.items() if v.get("males")}
_jobs_females = {k: v["females"] for k, v in PAINTER_ROLE_LABELS.items() if v.get("females")}

# Additional nats from test failures
_extra_nats = {
    "ancient roman": "رومان قدماء",
    "ancient-roman": "رومان قدماء",
    "turkish cypriot": "قبرصيون شماليون",
    "arab": "عرب",
    "asian": "آسيويون",
}

# 1. Male Nationality + Religion: {nat} {rel} -> {nat_ar} {rel_ar}
_nat_rel_bot_m = format_multi_data(
    formatted_data={
        "{nat} {rel}": "{nat_ar} {rel_ar}",
        "{rel} {nat}": "{nat_ar} {rel_ar}",
        "{nat} {rel} male": "{nat_ar} {rel_ar} ذكور",
        "{rel} {nat} male": "{nat_ar} {rel_ar} ذكور",
    },
    data_list={**Nat_mens, **_extra_nats},
    data_list2=_rel_males,
    key_placeholder="{nat}",
    value_placeholder="{nat_ar}",
    key2_placeholder="{rel}",
    value2_placeholder="{rel_ar}",
)

# 2. Male Job + Religion: {job} {rel} -> {job_ar} {rel_ar}
_job_rel_bot_m = format_multi_data(
    formatted_data={
        "{job} {rel}": "{job_ar} {rel_ar}",
        "{rel} {job}": "{job_ar} {rel_ar}",
        "{job} male {rel}": "{job_ar} ذكور {rel_ar}",
        "{job} {rel} male": "{job_ar} ذكور {rel_ar}",
        "{rel} {job} male": "{job_ar} ذكور {rel_ar}",
        "male {job} {rel}": "{job_ar} ذكور {rel_ar}",
    },
    data_list=_jobs_males,
    data_list2=_rel_males,
    key_placeholder="{job}",
    value_placeholder="{job_ar}",
    key2_placeholder="{rel}",
    value2_placeholder="{rel_ar}",
)

# 3. Female Nationality + Religion: female {nat} {rel} -> {rel_ar_f} {nat_ar_f}
_nat_rel_bot_f = format_multi_data(
    formatted_data={
        "female {nat} {rel}": "{rel_ar} {nat_ar}",
        "women's {nat} {rel}": "{rel_ar} {nat_ar}",
        "{nat} female {rel}": "{rel_ar} {nat_ar}",
        "{nat} women's {rel}": "{rel_ar} {nat_ar}",
        "{nat} {rel} female": "{rel_ar} {nat_ar}",
        "{nat} {rel} women's": "{rel_ar} {nat_ar}",
        "female {rel} {nat}": "{rel_ar} {nat_ar}",
        "women's {rel} {nat}": "{rel_ar} {nat_ar}",
    },
    data_list=Nat_Womens,
    data_list2=_rel_females,
    key_placeholder="{nat}",
    value_placeholder="{nat_ar}",
    key2_placeholder="{rel}",
    value2_placeholder="{rel_ar}",
)

# 4. Female Job + Religion: female {job} {rel} -> {job_ar_f} {rel_ar_f}
_job_rel_bot_f = format_multi_data(
    formatted_data={
        "female {job} {rel}": "{job_ar} {rel_ar}",
        "women's {job} {rel}": "{job_ar} {rel_ar}",
        "{job} female {rel}": "{job_ar} {rel_ar}",
        "{job} women's {rel}": "{job_ar} {rel_ar}",
        "{job} {rel} female": "{job_ar} {rel_ar}",
        "{job} {rel} women's": "{job_ar} {rel_ar}",
        "female {rel} {job}": "{job_ar} {rel_ar}",
        "women's {rel} {job}": "{job_ar} {rel_ar}",
    },
    data_list=_jobs_females,
    data_list2=_rel_females,
    key_placeholder="{job}",
    value_placeholder="{job_ar}",
    key2_placeholder="{rel}",
    value2_placeholder="{rel_ar}",
)

# 5. Simple Plurals (No combination)
_simple_m_bot = FormatData(formatted_data={"{rel}": "{rel_ar}"}, data_list=_rel_males)
_simple_f_bot = FormatData(
    formatted_data={
        "female {rel}": "{rel_ar}",
        "women's {rel}": "{rel_ar}",
        "{rel} female": "{rel_ar}",
        "{rel} women's": "{rel_ar}",
    },
    data_list=_rel_females,
)


def resolve_nats_jobs(category: str) -> str:
    """
    Resolves the Arabic label for a category string that combines a religious group and a nationality.
    Args:
        category: The input category string.
    Returns:
        The translated Arabic category label, or an empty string if no match is found.
    """
    category_lower = category.lower().strip()

    # Log to verify search attempts (internally)
    if res := _nat_rel_bot_f.search(category_lower):
        return res
    if res := _job_rel_bot_f.search(category_lower):
        return res
    if res := _nat_rel_bot_m.search(category_lower):
        return res
    if res := _job_rel_bot_m.search(category_lower):
        return res
    if res := _simple_f_bot.search(category_lower):
        return res
    if res := _simple_m_bot.search(category_lower):
        return res

    # Check for direct matches in RELIGIOUS_KEYS_PP as a fallback
    # Some religious group combinations might already be defined in the dict
    for key, labels in RELIGIOUS_KEYS_PP.items():
        if category_lower == key:
            # Check gender indicators in category string if any, else default to males
            if any(w in category_lower for w in ["female", "women's"]):
                return labels.get("females", "")
            return labels.get("males", "")

    return ""
