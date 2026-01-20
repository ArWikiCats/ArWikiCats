#
import pytest

from ArWikiCats import resolve_label_ar

data = {
    "Bridges in Wales by type": "جسور في ويلز حسب الفئة",
    "British Rail": "السكك الحديدية البريطانية",
    "History of British Rail": "تاريخ السكك الحديدية البريطانية",
    "design companies disestablished in 1905": "شركات تصميم انحلت في 1905",
    "landmarks in Yemen": "معالم في اليمن",
    "parks in the Roman Empire": "متنزهات في الإمبراطورية الرومانية",
    "Airlines established in 1968": "شركات طيران أسست في 1968",
    "Airlines of Afghanistan": "شركات طيران في أفغانستان",
    "Cargo airlines of the Philippines": "شحن جوي في الفلبين",
    "Vehicle manufacturing companies disestablished in 1904": "شركات تصنيع المركبات انحلت في 1904",
}


@pytest.mark.parametrize("category, expected", data.items(), ids=data.keys())
@pytest.mark.fast
def test_places_and_structures(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected
