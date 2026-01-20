#!/usr/bin/python3
"""
Resolves category labels for religious groups combined with nationalities.
"""

from ...translations import RELIGIOUS_KEYS_PP, Nat_mens, Nat_Womens
from ...translations_formats import FormatData, format_multi_data_v2

# Prepare consolidated dictionaries with gendered values
_rel_data = {k: {"rel_ar": v.get("males"), "rel_ar_f": v.get("females")} for k, v in RELIGIOUS_KEYS_PP.items()}

_nat_data = {}
for k, v in Nat_mens.items():
    _nat_data.setdefault(k.lower(), {})["nat_ar"] = v
for k, v in Nat_Womens.items():
    _nat_data.setdefault(k.lower(), {})["nat_ar_f"] = v

PAINTER_ROLE_LABELS = {
    "painters": {"males": "رسامون", "females": "رسامات"},
    "artists": {"males": "فنانون", "females": "فنانات"},
}

# Extended roles for the test cases
_jobs_data = {k: {"job_ar": v.get("males"), "job_ar_f": v.get("females")} for k, v in PAINTER_ROLE_LABELS.items()}

# Additional nats from test failures
_extra_nats = {
    "ancient roman": "رومان قدماء",
    "ancient-roman": "رومان قدماء",
    "turkish cypriot": "قبرصيون شماليون",
    "arab": "عرب",
    "asian": "آسيويون",
    "yemeni": "يمنيون",
}
for k, v in _extra_nats.items():
    _nat_data.setdefault(k, {})["nat_ar"] = v

# Logic for shared templates
_combined_templates = {
    # Nationality + Religion (Male/General)
    "{nat} {rel}": "{nat_ar} {rel_ar}",
    "{rel} {nat}": "{nat_ar} {rel_ar}",
    "{nat} {rel} male": "{nat_ar} {rel_ar} ذكور",
    "{rel} {nat} male": "{nat_ar} {rel_ar} ذكور",
    "{nat} male {rel}": "{rel_ar} ذكور {nat_ar}",
    "{nat} people {rel}": "{nat_ar} {rel_ar}",
    # Job + Religion (Male/General)
    "{job} {rel}": "{job_ar} {rel_ar}",
    "{rel} {job}": "{job_ar} {rel_ar}",
    "{job} male {rel}": "{job_ar} ذكور {rel_ar}",
    "{job} {rel} male": "{job_ar} ذكور {rel_ar}",
    "{rel} {job} male": "{job_ar} ذكور {rel_ar}",
    "male {job} {rel}": "{job_ar} ذكور {rel_ar}",
    # Nationality + Religion (Female)
    "female {nat} {rel}": "{rel_ar_f} {nat_ar_f}",
    "women's {nat} {rel}": "{rel_ar_f} {nat_ar_f}",
    "{nat} female {rel}": "{rel_ar_f} {nat_ar_f}",
    "{nat} women's {rel}": "{rel_ar_f} {nat_ar_f}",
    "{nat} {rel} female": "{rel_ar_f} {nat_ar_f}",
    "{nat} {rel} women's": "{rel_ar_f} {nat_ar_f}",
    "female {rel} {nat}": "{rel_ar_f} {nat_ar_f}",
    "women's {rel} {nat}": "{rel_ar_f} {nat_ar_f}",
    # Job + Religion (Female)
    "female {job} {rel}": "{job_ar_f} {rel_ar_f}",
    "women's {job} {rel}": "{job_ar_f} {rel_ar_f}",
    "{job} female {rel}": "{job_ar_f} {rel_ar_f}",
    "{job} women's {rel}": "{job_ar_f} {rel_ar_f}",
    "{job} {rel} female": "{job_ar_f} {rel_ar_f}",
    "{job} {rel} women's": "{job_ar_f} {rel_ar_f}",
    "female {rel} {job}": "{job_ar_f} {rel_ar_f}",
    "women's {rel} {job}": "{job_ar_f} {rel_ar_f}",
    # Simple religious labels (Female)
    "female {rel}": "{rel_ar_f}",
    "women's {rel}": "{rel_ar_f}",
    "{rel} female": "{rel_ar_f}",
    "{rel} women's": "{rel_ar_f}",
}

# 1. Main Bot for Nationality + Religion (V2)
_nat_rel_bot_v2 = format_multi_data_v2(
    formatted_data=_combined_templates,
    data_list=_nat_data,
    key_placeholder="{nat}",
    data_list2=_rel_data,
    key2_placeholder="{rel}",
    use_other_formatted_data=True,
)

# 2. Main Bot for Job + Religion (V2)
_job_rel_bot_v2 = format_multi_data_v2(
    formatted_data=_combined_templates,
    data_list=_jobs_data,
    key_placeholder="{job}",
    data_list2=_rel_data,
    key2_placeholder="{rel}",
)

# 3. Simple Fallback Bot for (Male/General)
_simple_m_bot = FormatData(
    formatted_data={"{rel}": "{rel_ar}"},
    data_list={k: v.get("males") for k, v in RELIGIOUS_KEYS_PP.items() if v.get("males")},
    key_placeholder="{rel}",
    value_placeholder="{rel_ar}",
)

# 4. Simple Fallback Bot for (Female)
_simple_f_bot = FormatData(
    formatted_data={"female {rel}": "{rel_ar_f}", "women's {rel}": "{rel_ar_f}"},
    data_list={k: v.get("females") for k, v in RELIGIOUS_KEYS_PP.items() if v.get("females")},
    key_placeholder="{rel}",
    value_placeholder="{rel_ar_f}",
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

    if res := _nat_rel_bot_v2.search(category_lower):
        return res
    if res := _job_rel_bot_v2.search(category_lower):
        return res

    # Check for direct matches in RELIGIOUS_KEYS_PP as a fallback
    for key, labels in RELIGIOUS_KEYS_PP.items():
        if category_lower == key:
            if any(w in category_lower for w in ["female", "women's"]):
                return labels.get("females", "")
            return labels.get("males", "")

    if res := _simple_m_bot.search(category_lower):
        return res

    if res := _simple_f_bot.search(category_lower):
        return res

    return ""
