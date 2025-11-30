#
from _collections_abc import dict_items
import pytest
from ArWikiCats import resolve_arabic_category_label

data2 = {
    # "Category:People from Westchester County, New York by _place_holder_": "",
    "Category:People from Westchester County, New York by hamlet": "تصنيف:أشخاص من مقاطعة ويستتشستر (نيويورك) حسب القرية",
    "Category:People from Westchester County, New York": "تصنيف:أشخاص من مقاطعة ويستتشستر (نيويورك)",
    "Category:People from Westchester County, New York by city": "تصنيف:أشخاص من مقاطعة ويستتشستر (نيويورك) حسب المدينة",
}


@pytest.mark.parametrize("category, expected", data2.items(), ids=list(data2.keys()))
@pytest.mark.fast
def test_people_labels_2(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected
