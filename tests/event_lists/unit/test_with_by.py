#
import pytest

from ArWikiCats import resolve_arabic_category_label

data2 = {
    "Category:People from Westchester County, New York by _place_holder_": "",
    "Category:People from Westchester county, New York by hamlet": "تصنيف:أشخاص من مقاطعة ويستتشستر (نيويورك) حسب القرية",
    "Category:People from New York": "تصنيف:أشخاص من نيويورك",
    "Category:People from Westchester County, New York": "تصنيف:أشخاص من مقاطعة ويستتشستر (نيويورك)",
    "Category:People from Westchester County, New York by city": "تصنيف:أشخاص من مقاطعة ويستتشستر (نيويورك) حسب المدينة",
    "Category:People from Westchester County, New York by town": "تصنيف:أشخاص من مقاطعة ويستتشستر (نيويورك) حسب البلدة",
    "Category:People from Westchester County, New York by village": "تصنيف:أشخاص من مقاطعة ويستتشستر (نيويورك) حسب القرية",
}


@pytest.mark.parametrize("category, expected", data2.items(), ids=data2.keys())
@pytest.mark.unit
def test_people_labels_2(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected
