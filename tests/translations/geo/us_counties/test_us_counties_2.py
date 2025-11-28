#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label
from ArWikiCats.translations.geo.us_counties import (
    _STATE_SUFFIX_TEMPLATES_BASE,
    US_STATES_NAME_TRANSLATIONS,
    normalize_state,
)

test_data = {
    "Category:{en} in the War of 1812": "تصنيف:{ar} في حرب 1812",
    "Category:{en} Democrats": "تصنيف:ديمقراطيون من ولاية {ar}",
    "Category:{en} lawyers": "تصنيف:محامون من ولاية {ar}",
    "Category:{en} state court judges": "تصنيف:قضاة محكمة ولاية {ar}",
    "Category:{en} state courts": "تصنيف:محكمة ولاية {ar}",
    "Category:{en} state senators": "تصنيف:أعضاء مجلس شيوخ ولاية {ar}",
}


_test_data = {
    f"Category:{{en}} {x.strip()}": "تصنيف:" + v % "{ar}"
    for x, v in _STATE_SUFFIX_TEMPLATES_BASE.items()
}
washington_data = {
    "Category:washington, d.c. Democrats": "تصنيف:ديمقراطيون من واشنطن العاصمة",
    "Category:washington, d.c. lawyers": "تصنيف:محامون من واشنطن العاصمة",
    "Category:washington, d.c. state court judges": "تصنيف:قضاة محكمة واشنطن العاصمة",
    "Category:washington, d.c. state courts": "تصنيف:محكمة واشنطن العاصمة",
    "Category:washington, d.c. state senators": "تصنيف:أعضاء مجلس شيوخ واشنطن العاصمة",
}

data_1 = {}
all_test_data = {}

for en, ar in US_STATES_NAME_TRANSLATIONS.items():
    test_one = {
        x.format(en=en): normalize_state(v.format(ar=ar))
        for x, v in test_data.items()
    }
    data_1.setdefault(en, test_one)
    all_test_data.update(test_one)

data_1["washington, d.c."] = washington_data
all_test_data.update(washington_data)

to_test = [
    (f"test_us_counties_{x}", v) for x, v in data_1.items()
]

to_test.append(("test_all_test_data", all_test_data))


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_all_dump(name, data):

    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    if diff_result:
        dump_diff(diff_result, name)
        dump_diff(expected, f"{name}_expected")

    assert diff_result == expected, f"Differences found: {len(diff_result)}"


@pytest.mark.parametrize("input,expected", all_test_data.items(), ids=[x for x in all_test_data])
@pytest.mark.slow
def test_all_data(input, expected):
    result = resolve_arabic_category_label(input)
    assert result == expected
