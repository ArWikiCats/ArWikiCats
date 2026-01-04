"""
Tests
"""

import pytest

from ArWikiCats.main_processers.main_utils import list_of_cat_func_new


def test_list_of_cat_func() -> None:
    # Test with basic inputs
    result = list_of_cat_func_new("classical musicians with disabilities", "موسيقيون كلاسيكيون", "{} بإعاقات")
    assert isinstance(result, str)
    assert result == "موسيقيون كلاسيكيون بإعاقات"
