"""
TODO: write tests
"""

import pytest

from ArWikiCats.legacy_bots.resolvers.arabic_label_builder import add_in_tab, find_ar_label

fast_data = {
    "00s establishments in the Roman Empire": "تأسيسات عقد 00 في الإمبراطورية الرومانية",
    "1000s disestablishments in Asia": "انحلالات عقد 1000 في آسيا",
    "1990s BC disestablishments in Asia": "انحلالات عقد 1990 ق م في آسيا",
    "1990s disestablishments in Europe": "انحلالات عقد 1990 في أوروبا",
    "April 1983 events in Europe": "أحداث أبريل 1983 في أوروبا",
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=fast_data.keys())
@pytest.mark.fast
def test_find_ar_label_fast(category: str, expected: str) -> None:
    label = find_ar_label(category, "in")
    assert label == expected


def test_add_in_tab() -> None:
    # Test with basic inputs
    result = add_in_tab("test label", "test", "from")
    assert isinstance(result, str)

    # Test with different separator value
    result_other = add_in_tab("test label", "test of", "to")
    assert isinstance(result_other, str)

    # Test with empty strings
    result_empty = add_in_tab("", "", "")
    assert isinstance(result_empty, str)


def test_add_in_tab_2() -> None:
    # Test with basic inputs
    result = add_in_tab("test label", "test", "from")
    assert isinstance(result, str)

    # Test with different separator value
    result_other = add_in_tab("test label", "test of", "to")
    assert isinstance(result_other, str)

    # Test with empty strings
    result_empty = add_in_tab("", "", "")
    assert isinstance(result_empty, str)


@pytest.mark.fast
def test_find_ar_label() -> None:
    # Test with basic inputs
    result = find_ar_label("test category", "from")
    assert isinstance(result, str)

    # Test with different parameters
    result_various = find_ar_label("sports category", "in")
    assert isinstance(result_various, str)

    # Test with another valid combination instead of empty strings
    result_safe = find_ar_label("music from france", "from")
    assert isinstance(result_safe, str)
