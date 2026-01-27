#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar

data = {
    "Mosque buildings with domes in India": "مساجد بقباب في الهند",
    "Mosque buildings with domes in Iran": "مساجد بقباب في إيران",
    "Mosque buildings with minarets in India": "مساجد بمنارات في الهند",
    "Mosque buildings with minarets in Iran": "مساجد بمنارات في إيران",
}


@pytest.mark.parametrize("category, expected", data.items(), ids=data.keys())
@pytest.mark.fast
def test_mosques(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_mosques", data),
]


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
