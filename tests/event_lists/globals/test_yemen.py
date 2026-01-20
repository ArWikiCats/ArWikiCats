#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar

data1 = {
    "Yemeni football teams": "فرق كرة قدم يمنية",
    "shi'a muslims": "مسلمون شيعة",
    "Yemeni national football teams": "منتخبات كرة قدم وطنية يمنية",
    "Yemeni national football team managers": "مدربو منتخب اليمن لكرة القدم",
    "Yemeni national softball team managers": "مدربو منتخب اليمن للكرة اللينة",
    "American national softball team": "منتخب الولايات المتحدة للكرة اللينة",
    "American national softball team managers": "مدربو منتخب الولايات المتحدة للكرة اللينة",
}

data2 = {
    "Yemen national football team": "منتخب اليمن لكرة القدم",
    "Yemen national football team managers": "مدربو منتخب اليمن لكرة القدم",
    "Yemen national softball team managers": "مدربو منتخب اليمن للكرة اللينة",
    "United States national softball team": "منتخب الولايات المتحدة للكرة اللينة",
    "United States national softball team managers": "مدربو منتخب الولايات المتحدة للكرة اللينة",
}

TEMPORAL_CASES = [
    ("test_yemen_1", data1),
    ("test_yemen_2", data2),
]


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
@pytest.mark.fast
def test_yemen_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data2.items(), ids=data2.keys())
@pytest.mark.fast
def test_yemen_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected
