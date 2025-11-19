#
from load_one_data import dump_diff, ye_test_one_dataset

from src import new_func_lab_final_label

data = {
    "Category:Mosque buildings with domes in India": "تصنيف:مساجد بقباب في الهند",
    "Category:Mosque buildings with domes in Iran": "تصنيف:مساجد بقباب في إيران",
    "Category:Mosque buildings with minarets in India": "تصنيف:مساجد بمنارات في الهند",
    "Category:Mosque buildings with minarets in Iran": "تصنيف:مساجد بمنارات في إيران",
}


def test_mosques():
    expected, diff_result = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff_result, "test_mosques")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
