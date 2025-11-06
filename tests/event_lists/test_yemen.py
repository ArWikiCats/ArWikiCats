#
from src import new_func_lab_final_label
from load_one_data import ye_test_one_dataset

data = {
    "Category:Yemen national football team managers": "تصنيف:مدربو منتخب اليمن لكرة القدم",
    "Category:Yemeni national football team managers": "تصنيف:مدربو منتخب اليمن لكرة القدم",

    "Category:Yemen national softball team managers": "تصنيف:مدربو منتخب اليمن للكرة اللينة",
    "Category:Yemeni national softball team managers": "تصنيف:مدربو منتخب اليمن للكرة اللينة",

    "Category:United States national softball team managers": "تصنيف:مدربو منتخب الولايات المتحدة للكرة اللينة",
    "Category:American national softball team managers": "تصنيف:مدربو منتخب الولايات المتحدة للكرة اللينة",

}


def test_yemen():
    print(f"len of data: {len(data)}")
    org, diff = ye_test_one_dataset(data, new_func_lab_final_label)
    assert diff == org
