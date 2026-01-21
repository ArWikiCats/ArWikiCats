"""Arabic label translation for general categories (Legacy Wrapper)."""

from __future__ import annotations
from .. import _resolver


def find_lab(category: str, category_r: str) -> str:

    return _resolver._find_lab(category, category_r)


def work_separator_names(category: str, cate_test: str = "", start_get_country2: bool = False) -> str:

    return _resolver._work_separator_names(category, start_get_country2=start_get_country2)


def translate_general_category(category_r: str, start_get_country2: bool = True, fix_title: bool = True) -> str:

    return _resolver._resolve_general_logic(category_r, start_get_country2=start_get_country2, fix_title=fix_title)
