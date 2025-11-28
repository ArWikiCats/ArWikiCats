#
import pytest
from load_one_data import dump_diff, one_dump_test

from src import resolve_arabic_category_label
from src.translations.geo.us_counties import (
    _STATE_SUFFIX_TEMPLATES_BASE,
    STATE_NAME_TRANSLATIONS,
)

test_data = {
    "Category:{en} in the War of 1812": "تصنيف:{ar} في حرب 1812",
    "Category:{en} Democrats": "تصنيف:ديمقراطيون من ولاية {ar}",
    "Category:{en} lawyers": "تصنيف:محامون من ولاية {ar}",
    "Category:{en} state court judges": "تصنيف:قضاة محكمة ولاية {ar}",
    "Category:{en} state courts": "تصنيف:محكمة ولاية {ar}",
    "Category:{en} state senators": "تصنيف:أعضاء مجلس شيوخ ولاية {ar}",
}

test_data2 = {f"Category:{{en}} {x.strip()}": "تصنيف:" + v % "{ar}" for x, v in _STATE_SUFFIX_TEMPLATES_BASE.items()}

data_1 = {
    "north dakota": "داكوتا الشمالية",
    "south carolina": "كارولاينا الجنوبية",
}
# for en in data_1.keys(): # if STATE_NAME_TRANSLATIONS.get(en): ar = STATE_NAME_TRANSLATIONS.get(en)

for en, ar in STATE_NAME_TRANSLATIONS.items():
    data_1[en] = {x.format(en=en): v.format(ar=ar) for x, v in test_data.items()}


to_test = [
    (f"test_us_counties_{x}", v) for x, v in data_1.items()
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.slow
def test_all_dump(name, data):

    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    if diff_result:
        dump_diff(diff_result, name)
        dump_diff(expected, f"{name}_expected")

    assert diff_result == expected, f"Differences found: {len(diff_result)}"


@pytest.mark.parametrize("input,expected", data_1["north dakota"].items(), ids=[x for x in data_1["north dakota"]])
@pytest.mark.slow
def test_north_dakota(input, expected):
    result = resolve_arabic_category_label(input)
    assert result == expected


@pytest.mark.parametrize("input,expected", data_1["south carolina"].items(), ids=[x for x in data_1["south carolina"]])
@pytest.mark.slow
def test_south_carolina(input, expected):
    result = resolve_arabic_category_label(input)
    assert result == expected
