"""
Tests
"""
import pytest

from src.make2_bots.bots.tmp_bot import Work_Templates

def test_work_templates():
    # Test with a basic input
    result = Work_Templates("test input")
    assert isinstance(result, str)

    # Test with empty string
    result_empty = Work_Templates("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = Work_Templates("sports category")
    assert isinstance(result_various, str)

    # Test with input that might match a template
    result_template = Work_Templates("football players")
    assert isinstance(result_template, str)
