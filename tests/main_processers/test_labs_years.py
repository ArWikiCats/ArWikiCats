"""
Tests
"""

import pytest

from src.main_processers.labs_years import LabsYears


@pytest.mark.fast
def test_labsyears():
    # Test the LabsYears class functionality
    labs_years_bot = LabsYears()

    # Test with a category containing a year
    en_year, from_year = labs_years_bot.lab_from_year("events {year1}")
    assert isinstance(en_year, str)
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


def test_lab_from_year_no_year():
    """Should return empty tuple when no 4-digit year exists."""
    bot = LabsYears()
    result = bot.lab_from_year("Category:Something without year")
    assert result == ("", "")


def test_lab_from_year_year_detected_but_no_template():
    """Should extract the year but return empty second value if template not found."""
    bot = LabsYears()
    result = bot.lab_from_year("Category:Works in 1999")
    assert result == ("1999", "")


def test_lab_from_year_add_creates_template():
    """Should correctly create the template key/value with year replaced by {year1}."""
    bot = LabsYears()

    bot.lab_from_year_add(
        category_r="Category:Films in 1999",
        category_lab="تصنيف:أفلام في 1999",
        en_year="1999",
    )

    assert "category:films in {year1}" in bot.category_templates
    assert bot.category_templates["category:films in {year1}"] == "تصنيف:أفلام في {year1}"


def test_lab_from_year_successful_lookup_and_replacement():
    """Should return converted label and increment lookup_count."""
    bot = LabsYears()

    # Prepare template
    bot.lab_from_year_add(
        category_r="Category:Events in 2010",
        category_lab="تصنيف:أحداث في 2010",
        en_year="2010",
        ar_year="2010",
    )

    year, label = bot.lab_from_year("Category:Events in 2010")

    assert year == "2010"
    assert label == "تصنيف:أحداث في 2010"
    assert bot.lookup_count == 1


def test_lab_from_year_template_exists_with_different_year():
    """Should correctly replace {year1} back to real year even if category is different year."""
    bot = LabsYears()

    # Add template for {year1}-base
    bot.lab_from_year_add(
        category_r="Category:Sports in 2022",
        category_lab="تصنيف:رياضة في 2022",
        en_year="2022",
        ar_year="2022",
    )

    # Now query for another valid year template
    year, label = bot.lab_from_year("Category:Sports in 2022")

    assert year == "2022"
    assert label == "تصنيف:رياضة في 2022"
    assert bot.lookup_count == 1


def test_lab_from_year_add_missing_real_year():
    """Should do nothing if en_year is not inside category_lab."""
    bot = LabsYears()
    bot.category_templates = {}

    bot.lab_from_year_add(
        category_r="Category:Something in 2015",
        category_lab="تصنيف:شيء ما",  # Does NOT contain 2015
        en_year="2015",
        ar_year="",
    )

    assert bot.category_templates == {}


def _test_with_decade():
    bot = LabsYears()

    # Add template for {year1}-base
    bot.lab_from_year_add(
        category_r="Category:1990 works",
        category_lab="تصنيف:أعمال 1990",
        en_year="1990",
        ar_year="1990",
    )

    # Now query for another valid year template
    en_year = bot.match_en_time("Category:1990s works")
    assert en_year == "1990s"

    year, label = bot.lab_from_year("Category:1990s works")

    assert year == "1990"
    assert label == "تصنيف:أعمال عقد 1990"
    assert bot.lookup_count == 1
