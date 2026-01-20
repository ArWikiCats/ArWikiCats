#
import pytest

from ArWikiCats import resolve_label_ar

data2 = {
    "People from Westchester County, New York by _place_holder_": "",
    "People from Westchester county, New York by hamlet": "أشخاص من مقاطعة ويستتشستر (نيويورك) حسب القرية",
    "People from New York": "أشخاص من نيويورك",
    "People from Westchester County, New York": "أشخاص من مقاطعة ويستتشستر (نيويورك)",
    "People from Westchester County, New York by city": "أشخاص من مقاطعة ويستتشستر (نيويورك) حسب المدينة",
    "People from Westchester County, New York by town": "أشخاص من مقاطعة ويستتشستر (نيويورك) حسب البلدة",
    "People from Westchester County, New York by village": "أشخاص من مقاطعة ويستتشستر (نيويورك) حسب القرية",
}


@pytest.mark.parametrize("category, expected", data2.items(), ids=data2.keys())
@pytest.mark.unit
def test_people_labels_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected
