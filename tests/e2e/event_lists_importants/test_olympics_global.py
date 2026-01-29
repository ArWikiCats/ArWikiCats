"""
Tests
"""

import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data_callback

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

test_dump_all = make_dump_test_name_data_callback(TEMPORAL_CASES, run_same=False)
