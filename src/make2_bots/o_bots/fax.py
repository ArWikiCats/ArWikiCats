"""Helpers for resolving sports teams and language categories."""

from __future__ import annotations

import functools
from typing import Dict
from ...helps.print_bot import print_put
from ...translations import lang_ttty, languages_pop


@functools.lru_cache(maxsize=None)
def te_language(category: str) -> str:
    """Return the label for a language-related category.

    Args:
        category: Category name containing a language prefix.

    Returns:
        The resolved Arabic label or an empty string when the category is
        unknown.
    """

    normalized_category = category.lower().strip()

    resolved_label = ""
    language_label = ""
    language_suffix = ""

    for language_key, language_name in languages_pop.items():
        lowercase_key = language_key.lower()
        key_prefix = f"{lowercase_key} "
        if normalized_category.startswith(key_prefix):
            language_label = language_name
            language_suffix = normalized_category[len(key_prefix) :].strip()
            break

    if not resolved_label:
        suffix_template = lang_ttty.get(language_suffix, "")
        if suffix_template and language_label:
            resolved_label = suffix_template % language_label if "%s" in suffix_template else suffix_template.format(language_label)

    if resolved_label:
        print_put(f"<<lightblue>>>> vvvvvvvvvvvv te_language cate:{normalized_category} vvvvvvvvvvvv ")
        print_put(f'<<lightblue>>>>>> te_language: new_lab  "{resolved_label}" ')
        print_put("<<lightblue>>>> ^^^^^^^^^ te_language end ^^^^^^^^^ ")

    return resolved_label


__all__ = [
    "te_language",
]
