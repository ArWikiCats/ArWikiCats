"""
Tests
"""
import pytest

from src.make2_bots.ma_bots.c2_bots.cn_lab import make_cnt_lab

def test_make_cnt_lab():
    # Test with basic inputs
    result = make_cnt_lab("in", "test in country", "country label", "test label", "test", "country", " ")
    assert isinstance(result, str)

    # Test with different parameters
    result_various = make_cnt_lab("from", "test from country", "country label2", "test label2", "test2", "country2", " من ")
    assert isinstance(result_various, str)

    # Test with empty strings
    result_empty = make_cnt_lab("", "", "", "", "", "", "")
    assert isinstance(result_empty, str)