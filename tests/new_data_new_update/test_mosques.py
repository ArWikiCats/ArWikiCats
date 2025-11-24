#
import pytest
from src import new_func_lab_final_label

data = {
    "Category:Mosque buildings with domes in India": "تصنيف:مساجد بقباب في الهند",
    "Category:Mosque buildings with domes in Iran": "تصنيف:مساجد بقباب في إيران",
    "Category:Mosque buildings with minarets in India": "تصنيف:مساجد بمنارات في الهند",
    "Category:Mosque buildings with minarets in Iran": "تصنيف:مساجد بمنارات في إيران",
}


@pytest.mark.parametrize("category, expected", data.items(), ids=list(data.keys()))
@pytest.mark.fast
def test_mosques(category, expected) -> None:
    label = new_func_lab_final_label(category)
    assert label.strip() == expected
