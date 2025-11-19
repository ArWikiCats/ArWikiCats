#
from load_one_data import dump_diff, ye_test_one_dataset

from src import new_func_lab_final_label

data = {"Category:Egyptian oncologists": "تصنيف:أطباء أورام مصريون", "Category:Fish described in 1995": "تصنيف:أسماك وصفت في 1995", "Category:Mammals described in 2017": "تصنيف:ثدييات وصفت في 2017", "Category:Pakistani psychiatrists": "تصنيف:أطباء نفسيون باكستانيون", "Category:Research institutes established in 1900": "تصنيف:معاهد أبحاث أسست في 1900", "Category:Swedish oncologists": "تصنيف:أطباء أورام سويديون"}


def test_science_and_medicine():
    print(f"len of data: {len(data)}")
    expected, diff_result = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff_result, "test_science_and_medicine")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"
