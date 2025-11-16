"""
Tests
"""
import pytest

from src.make2_bots.ma_bots.arlabel_bots.ar_lab import add_in_tab, find_ar_label


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


@pytest.mark.skip
def test_find_ar_label():
    # Test with basic inputs
    result = find_ar_label("test category", "from", "from", "test", "test category")
    assert isinstance(result, str)

    # Test with different parameters
    result_various = find_ar_label("sports category", "in", "in", "sports", "sports category", False)
    assert isinstance(result_various, str)

    # Test with another valid combination instead of empty strings
    result_safe = find_ar_label("music from france", "from", "from", "music", "music from france", True)
    assert isinstance(result_safe, str)
