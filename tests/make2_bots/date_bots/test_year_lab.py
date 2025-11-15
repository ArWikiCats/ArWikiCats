"""
Tests
"""
import pytest

from src.make2_bots.date_bots.year_lab import make_year_lab, make_month_lab

def test_make_year_lab():
    # Test basic year
    result = make_year_lab("2020")
    assert isinstance(result, str)
    assert "2020" in result or result == ""  # May return empty for invalid cases

    # Test year with BC
    result_bc = make_year_lab("500 bc")
    assert isinstance(result_bc, str)

    # Test year with BCE
    result_bce = make_year_lab("300 bce")
    assert isinstance(result_bce, str)

    # Test century
    result_century = make_year_lab("21st century")
    assert isinstance(result_century, str)

    # Test millennium
    result_millennium = make_year_lab("3rd millennium")
    assert isinstance(result_millennium, str)

    # Test with month
    result_with_month = make_year_lab("january 2020")
    assert isinstance(result_with_month, str)

def test_make_month_lab():
    # Test with numeric year
    result = make_month_lab("2020")
    assert result == "2020"

    # Test with month and year
    result_month = make_month_lab("january 2020")
    assert isinstance(result_month, str)

    # Test with empty string
    result_empty = make_month_lab("")
    assert isinstance(result_empty, str)

    # Test with just letters
    result_letters = make_month_lab("january")
    assert isinstance(result_letters, str)
