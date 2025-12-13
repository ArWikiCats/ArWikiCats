#
import pytest

from ArWikiCats import resolve_arabic_category_label

data = {
    "Category:Egyptian oncologists": "تصنيف:أطباء أورام مصريون",
    "Category:Fish described in 1995": "تصنيف:أسماك وصفت في 1995",
    "Category:Mammals described in 2017": "تصنيف:ثدييات وصفت في 2017",
    "Category:Pakistani psychiatrists": "تصنيف:أطباء نفسيون باكستانيون",
    "Category:Research institutes established in 1900": "تصنيف:معاهد أبحاث أسست في 1900",
    "Category:Swedish oncologists": "تصنيف:أطباء أورام سويديون",
}


@pytest.mark.parametrize("category, expected", data.items(), ids=data.keys())
@pytest.mark.fast
def test_science_and_medicine(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected
