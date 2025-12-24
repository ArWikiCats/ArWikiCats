"""
Tests
"""

from typing import Callable

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

for_countries_t = {
    # "Category:Winter Olympics competitors for Algeria by sport": "تصنيف:منافسون في الألعاب الأولمبية الشتوية من الجزائر حسب الرياضة",
    # "Category:Winter Olympics competitors for Algeria by sport": "تصنيف:منافسون أولمبيون شتويون من الجزائر حسب الرياضة",
    "Category:Winter Olympics competitors for Eswatini": "تصنيف:منافسون أولمبيون شتويون من إسواتيني",
    "Category:Winter Olympics competitors by country": "تصنيف:منافسون أولمبيون شتويون حسب البلد",
    "Category:Winter Olympics competitors by sport": "تصنيف:منافسون أولمبيون شتويون حسب الرياضة",
    "Category:Winter Olympics competitors by sport and country": "تصنيف:منافسون أولمبيون شتويون حسب الرياضة والبلد",
    "Category:Winter Olympics competitors by sport and year": "تصنيف:منافسون أولمبيون شتويون حسب الرياضة والسنة",
    "Category:Winter Olympics competitors by year": "تصنيف:منافسون أولمبيون شتويون حسب السنة",
}


@pytest.mark.parametrize("category, expected", for_countries_t.items(), ids=for_countries_t.keys())
@pytest.mark.fast
def test_for_countries_t(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_for_countries_t", for_countries_t, resolve_arabic_category_label),
]


@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name: str, data: dict[str, str], callback: Callable) -> None:
    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
