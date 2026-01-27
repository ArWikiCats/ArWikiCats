"""
"""
import pytest
from ArWikiCats.legacy_bots.resolvers.arabic_label_builder import find_ar_label

data_list2 = [
    ("paralympic competitors for cyprus", " for ", "منافسون بارالمبيون من قبرص"),
    ("african games gold medalists for chad", " for ", "فائزون بميداليات ذهبية في الألعاب الإفريقية من تشاد"),
    ("olympic silver medalists for finland", " for ", "فائزون بميداليات فضية أولمبية من فنلندا"),
    ("summer olympics competitors for peru", " for ", "منافسون أولمبيون صيفيون من بيرو"),
]


@pytest.mark.parametrize("category, separator, output", data_list2, ids=[x[0] for x in data_list2])
@pytest.mark.fast
def test_simple_2(category: str, separator: str, output: str) -> None:
    label = find_ar_label(category, separator, use_event2=False)
    assert label == output
