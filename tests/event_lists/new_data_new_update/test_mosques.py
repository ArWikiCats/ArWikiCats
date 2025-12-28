#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data = {
    "Category:Mosque buildings with domes in India": "تصنيف:مساجد بقباب في الهند",
    "Category:Mosque buildings with domes in Iran": "تصنيف:مساجد بقباب في إيران",
    "Category:Mosque buildings with minarets in India": "تصنيف:مساجد بمنارات في الهند",
    "Category:Mosque buildings with minarets in Iran": "تصنيف:مساجد بمنارات في إيران",
}


@pytest.mark.parametrize("category, expected", data.items(), ids=data.keys())
@pytest.mark.fast
def test_mosques(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_mosques", data),
]


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
