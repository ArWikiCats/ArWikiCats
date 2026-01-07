#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data1 = {
    "Category:Yemeni football teams": "تصنيف:فرق كرة قدم يمنية",
    "Category:shi'a muslims": "تصنيف:مسلمون شيعة",
    "Category:Yemeni national football teams": "تصنيف:منتخبات كرة قدم وطنية يمنية",
    "Category:Yemeni national football team managers": "تصنيف:مدربو منتخب اليمن لكرة القدم",
    "Category:Yemeni national softball team managers": "تصنيف:مدربو منتخب اليمن للكرة اللينة",
    "Category:American national softball team": "تصنيف:منتخب الولايات المتحدة للكرة اللينة",
    "Category:American national softball team managers": "تصنيف:مدربو منتخب الولايات المتحدة للكرة اللينة",
}

data2 = {
    "Category:Yemen national football team": "تصنيف:منتخب اليمن لكرة القدم",
    "Category:Yemen national football team managers": "تصنيف:مدربو منتخب اليمن لكرة القدم",
    "Category:Yemen national softball team managers": "تصنيف:مدربو منتخب اليمن للكرة اللينة",
    "Category:United States national softball team": "تصنيف:منتخب الولايات المتحدة للكرة اللينة",
    "Category:United States national softball team managers": "تصنيف:مدربو منتخب الولايات المتحدة للكرة اللينة",
}

TEMPORAL_CASES = [
    ("test_yemen_1", data1),
    ("test_yemen_2", data2),
]


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
@pytest.mark.fast
def test_yemen_1(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data2.items(), ids=data2.keys())
@pytest.mark.fast
def test_yemen_2(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected
