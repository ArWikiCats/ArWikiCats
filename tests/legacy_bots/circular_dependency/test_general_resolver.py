"""
Tests
"""

import pytest

from ArWikiCats.fix import fixtitle
from ArWikiCats.legacy_bots.circular_dependency.general_resolver import work_separator_names
from ArWikiCats.legacy_bots.circular_dependency.sub_general_resolver import sub_translate_general_category

fast_data = {}


def translate_general_category_wrap(category: str) -> str:
    arlabel = "" or sub_translate_general_category(category) or work_separator_names(category)
    if arlabel:
        arlabel = fixtitle.fixlabel(arlabel, en=category)

    return arlabel


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=fast_data.keys())
@pytest.mark.fast
def test_fast_data(category: str, expected: str) -> None:
    label = translate_general_category_wrap(category)
    assert label == expected


def test_work_separator_names() -> None:
    # Test with a basic input
    result = work_separator_names("test category", True)
    assert isinstance(result, str)

    result_empty = work_separator_names("", False)
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = work_separator_names("sports", True)
    assert isinstance(result_various, str)


def test_translate_general_category() -> None:
    # Test with a basic input
    result = translate_general_category_wrap("test category")
    assert isinstance(result, str)

    result_empty = translate_general_category_wrap("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = translate_general_category_wrap("sports category")
    assert isinstance(result_various, str)
