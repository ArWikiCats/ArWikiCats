"""
Tests
"""
import pytest

from src.make2_bots.o_bots.univer import te_universities


def test_te_universities():
    # Test with a basic university category
    result = te_universities("university of california")
    assert isinstance(result, str)

    # Test with empty string
    result_empty = te_universities("")
    assert isinstance(result_empty, str)

    # Test with a specific major
    result_major = te_universities("university of engineering")
    assert isinstance(result_major, str)

    # Test with "the" prefix
    result_the = te_universities("the university of law")
    assert isinstance(result_the, str)
