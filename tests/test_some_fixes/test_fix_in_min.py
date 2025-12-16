#
import pytest
from load_one_data import dump_diff, one_dump_test, dump_diff_text

from ArWikiCats import resolve_arabic_category_label

data0 = {
}

data_1 = {
}

data_2 = {
}

to_test = [
    ("test_fix_in_min_0", data0),
    ("test_fix_in_min_1", data_1),
    ("test_fix_in_min_2", data_2),
]


@pytest.mark.parametrize("category, expected", data_2.items(), ids=data_2.keys())
@pytest.mark.fast
def test_fix_in_min_2(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    dump_diff(diff_result, name)
    dump_diff_text(expected, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
