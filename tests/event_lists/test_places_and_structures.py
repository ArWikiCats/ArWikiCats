#
import pytest

from src import new_func_lab_final_label

data = {
    "Category:Bridges in Wales by type": "تصنيف:جسور في ويلز حسب الفئة",
    "Category:British Rail": "تصنيف:السكك الحديدية البريطانية",
    "Category:History of British Rail": "تصنيف:تاريخ السكك الحديدية البريطانية",
    "Category:design companies disestablished in 1905": "تصنيف:شركات تصميم انحلت في 1905",
    "Category:landmarks in Yemen": "تصنيف:معالم في اليمن",
    "Category:parks in the Roman Empire": "تصنيف:متنزهات في الإمبراطورية الرومانية",
    "Category:Airlines established in 1968": "تصنيف:شركات طيران أسست في 1968",
    "Category:Airlines of Afghanistan": "تصنيف:شركات طيران في أفغانستان",
    "Category:Cargo airlines of the Philippines": "تصنيف:شحن جوي في الفلبين",
    "Category:Vehicle manufacturing companies disestablished in 1904": "تصنيف:شركات تصنيع المركبات انحلت في 1904",
}


@pytest.mark.parametrize("category, expected", data.items(), ids=list(data.keys()))
@pytest.mark.fast
def test_places_and_structures(category, expected) -> None:
    label = new_func_lab_final_label(category)
    assert label.strip() == expected
