#
import pytest
from src import new_func_lab_final_label
from load_one_data import ye_test_one_dataset

data = {
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


def test_yemen():
    print(f"len of data: {len(data)}")
    expected, diff_result = ye_test_one_dataset(data, new_func_lab_final_label)
    assert diff_result == expected


@pytest.mark.skip("Need to be fixed")
def test_yemen2():

    data = {
        "Category:Yemen national football team": "تصنيف:منتخب اليمن لكرة القدم",
        "Category:Yemen national football team managers": "تصنيف:مدربو منتخب اليمن لكرة القدم",
        "Category:Yemen national softball team managers": "تصنيف:مدربو منتخب اليمن للكرة اللينة",
        "Category:United States national softball team": "تصنيف:منتخب الولايات المتحدة للكرة اللينة",
        "Category:United States national softball team managers": "تصنيف:مدربو منتخب الولايات المتحدة للكرة اللينة",
    }

    print(f"len of data: {len(data)}")
    expected, diff_result = ye_test_one_dataset(data, new_func_lab_final_label)
    assert diff_result == expected
