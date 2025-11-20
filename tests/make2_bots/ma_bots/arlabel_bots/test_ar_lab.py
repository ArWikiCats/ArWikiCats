"""
Tests
"""

import pytest

from src.make2_bots.ma_bots.ar_lab import add_in_tab, find_ar_label

fast_data = {
    "00s establishments": "تأسيسات عقد 00",
    "1000s disestablishments": "انحلالات عقد 1000",
    "11th government of": "حكومة",
    "13th century establishments": "تأسيسات القرن 13",
    "14th century establishments": "تأسيسات القرن 14",
    "18th century people of": "أشخاص في القرن 18",
    "1990s bc disestablishments": "انحلالات عقد 1990 ق م",
    "1990s disestablishments": "انحلالات عقد 1990",
    "19th century actors": "ممثلون في القرن 19",
    "19th century people": "أشخاص في القرن 19",
    "19th government of": "حكومة",
    "20th century disestablishments": "انحلالات القرن 20",
    "4th senate of": "مجلس شيوخ",
    "april 1983 events": "أحداث أبريل 1983",
    "july 2018 events": "أحداث يوليو 2018",
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=list(fast_data.keys()))
@pytest.mark.fast
def test_find_ar_label_fast(category, expected) -> None:
    label = find_ar_label(category)
    assert label == expected


def test_add_in_tab():
    # Test with basic inputs
    result = add_in_tab("test label", "test", "from")
    assert isinstance(result, str)

    # Test with different tito value
    result_other = add_in_tab("test label", "test of", "to")
    assert isinstance(result_other, str)

    # Test with empty strings
    result_empty = add_in_tab("", "", "")
    assert isinstance(result_empty, str)


def test_add_in_tab_2():
    # Test with basic inputs
    result = add_in_tab("test label", "test", "from")
    assert isinstance(result, str)

    # Test with different tito value
    result_other = add_in_tab("test label", "test of", "to")
    assert isinstance(result_other, str)

    # Test with empty strings
    result_empty = add_in_tab("", "", "")
    assert isinstance(result_empty, str)


@pytest.mark.skip2
def test_find_ar_label():
    # Test with basic inputs
    result = find_ar_label("test category", "from", "test", "test category")
    assert isinstance(result, str)

    # Test with different parameters
    result_various = find_ar_label("sports category", "in", "sports", "sports category", False)
    assert isinstance(result_various, str)

    # Test with another valid combination instead of empty strings
    result_safe = find_ar_label("music from france", "from", "music", "music from france", True)
    assert isinstance(result_safe, str)
