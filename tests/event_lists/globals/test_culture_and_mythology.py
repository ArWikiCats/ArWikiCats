#
import pytest

from ArWikiCats import resolve_label_ar

data = {
    "Berlin University of Arts": "جامعة برلين للفنون",
    "Celtic mythology in popular culture": "أساطير كلتية في الثقافة الشعبية",
    "Ethnic groups of Dominican Republic": "مجموعات عرقية في جمهورية الدومينيكان",
    "Russian folklore characters": "شخصيات فلكلورية روسية",
    "Scottish popular culture": "ثقافة شعبية إسكتلندية",
    "Scottish traditions": "تراث إسكتلندي",
}


@pytest.mark.parametrize("category, expected", data.items(), ids=data.keys())
@pytest.mark.fast
def test_culture_and_mythology(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected
