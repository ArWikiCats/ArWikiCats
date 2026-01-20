#
import pytest

from ArWikiCats import resolve_label_ar

data = {
    "Egyptian oncologists": "أطباء أورام مصريون",
    "Fish described in 1995": "أسماك وصفت في 1995",
    "Mammals described in 2017": "ثدييات وصفت في 2017",
    "Pakistani psychiatrists": "أطباء نفسيون باكستانيون",
    "Research institutes established in 1900": "معاهد أبحاث أسست في 1900",
    "Swedish oncologists": "أطباء أورام سويديون",
}


@pytest.mark.parametrize("category, expected", data.items(), ids=data.keys())
@pytest.mark.fast
def test_science_and_medicine(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected
