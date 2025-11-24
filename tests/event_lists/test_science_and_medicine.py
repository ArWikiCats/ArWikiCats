#
import pytest

from src import new_func_lab_final_label

data = {
    "Category:Egyptian oncologists": "تصنيف:أطباء أورام مصريون",
    "Category:Fish described in 1995": "تصنيف:أسماك وصفت في 1995",
    "Category:Mammals described in 2017": "تصنيف:ثدييات وصفت في 2017",
    "Category:Pakistani psychiatrists": "تصنيف:أطباء نفسيون باكستانيون",
    "Category:Research institutes established in 1900": "تصنيف:معاهد أبحاث أسست في 1900",
    "Category:Swedish oncologists": "تصنيف:أطباء أورام سويديون",
}


@pytest.mark.parametrize("category, expected", data.items(), ids=list(data.keys()))
@pytest.mark.fast
def test_science_and_medicine(category, expected) -> None:
    label = new_func_lab_final_label(category)
    assert label.strip() == expected
