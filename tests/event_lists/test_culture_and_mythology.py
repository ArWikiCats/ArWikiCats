#
import pytest

from ArWikiCats import resolve_arabic_category_label

data = {
    "Category:Berlin University of Arts": "تصنيف:جامعة برلين للفنون",
    "Category:Celtic mythology in popular culture": "تصنيف:أساطير كلتية في الثقافة الشعبية",
    "Category:Ethnic groups of Dominican Republic": "تصنيف:مجموعات عرقية في جمهورية الدومينيكان",
    "Category:Russian folklore characters": "تصنيف:شخصيات فلكلورية روسية",
    "Category:Scottish popular culture": "تصنيف:ثقافة شعبية إسكتلندية",
    "Category:Scottish traditions": "تصنيف:تراث إسكتلندي",
}


@pytest.mark.parametrize("category, expected", data.items(), ids=data.keys())
@pytest.mark.fast
def test_culture_and_mythology(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected
