#
import pytest
from load_one_data import dump_diff, one_dump_test

from src import new_func_lab_final_label

data1 = {
    "Category:Yemeni football teams": "تصنيف:فرق كرة قدم يمنية",
    "Category:Yemeni shi'a muslims": "تصنيف:يمنيون مسلمون شيعة",
    "Category:shi'a muslims": "تصنيف:مسلمون شيعة",
    "Category:shi'a muslims expatriates": "تصنيف:مسلمون شيعة مغتربون",
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
@pytest.mark.slow
def test_all(name, data):
    expected, diff_result = one_dump_test(data, new_func_lab_final_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"


@pytest.mark.parametrize("category, expected", data1.items(), ids=list(data1.keys()))
@pytest.mark.fast
def test_yemen_1(category, expected) -> None:
    label = new_func_lab_final_label(category)
    assert label.strip() == expected


@pytest.mark.parametrize("category, expected", data2.items(), ids=list(data2.keys()))
@pytest.mark.fast
def test_yemen_2(category, expected) -> None:
    label = new_func_lab_final_label(category)
    assert label.strip() == expected
