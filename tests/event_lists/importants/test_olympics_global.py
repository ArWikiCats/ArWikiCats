"""
Tests
"""

from typing import Callable

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar

for_countries_t = {
    # "Winter Olympics competitors for Algeria by sport": "منافسون في الألعاب الأولمبية الشتوية من الجزائر حسب الرياضة",
    # "Winter Olympics competitors for Algeria by sport": "منافسون أولمبيون شتويون من الجزائر حسب الرياضة",
    "Winter Olympics competitors for Eswatini": "منافسون أولمبيون شتويون من إسواتيني",
    "Winter Olympics competitors by country": "منافسون أولمبيون شتويون حسب البلد",
    "Winter Olympics competitors by sport": "منافسون أولمبيون شتويون حسب الرياضة",
    "Winter Olympics competitors by sport and country": "منافسون أولمبيون شتويون حسب الرياضة والبلد",
    "Winter Olympics competitors by sport and year": "منافسون أولمبيون شتويون حسب الرياضة والسنة",
    "Winter Olympics competitors by year": "منافسون أولمبيون شتويون حسب السنة",
}


@pytest.mark.parametrize("category, expected", for_countries_t.items(), ids=for_countries_t.keys())
@pytest.mark.fast
def test_for_countries_t(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_for_countries_t", for_countries_t, resolve_label_ar),
]


@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name: str, data: dict[str, str], callback: Callable) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
