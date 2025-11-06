#
from src import new_func_lab_final_label
from load_one_data import ye_test_one_dataset

data = {
    "Category:Yemen national football team managers": "تصنيف:مدربو منتخب اليمن لكرة القدم",
    "Category:Yemeni national football team managers": "تصنيف:مدربو منتخب اليمن لكرة القدم",
}


def test_yemen():
    print(f"len of data: {len(data)}")
    org, diff = ye_test_one_dataset(data, new_func_lab_final_label)
    assert diff == org
