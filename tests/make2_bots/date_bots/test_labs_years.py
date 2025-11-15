"""
Tests
"""
import pytest

from src.make2_bots.date_bots.labs_years import LabsYears

def test_labsyears():
    # Test the LabsYears class functionality
    labs_years_bot = LabsYears()

    # Test with a category containing a year
    cat_year, from_year = labs_years_bot.lab_from_year("events 2020")
    assert isinstance(cat_year, str)
    assert isinstance(from_year, str)

    # Test with a category without a year
    cat_year_empty, from_year_empty = labs_years_bot.lab_from_year("events only")
    assert cat_year_empty == ""
    assert from_year_empty == ""

    # Test adding an entry
    labs_years_bot.lab_from_year_add("test 2020", "test label 2020", "2020")

    # Test with another year
    cat_year2, from_year2 = labs_years_bot.lab_from_year("events 2021")
    assert isinstance(cat_year2, str)
    assert isinstance(from_year2, str)
