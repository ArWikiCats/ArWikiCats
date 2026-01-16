"""
Tests
"""

import pytest

from ArWikiCats.time_resolvers.labs_years import LabsYears

test_data = {
    "12th-century Indian books": "كتب هندية في القرن 12",
    "1520s censuses": "تعداد السكان في عقد 1520",
    "1630s science fiction works": "أعمال خيال علمي عقد 1630",
    "1650s controversies": "خلافات عقد 1650",
    "1650s floods": "فيضانات عقد 1650",
    "1650s mass shootings": "إطلاق نار عشوائي عقد 1650",
    "1650s murders": "جرائم قتل في عقد 1650",
    "1650s science fiction works": "أعمال خيال علمي عقد 1650",
    "17th-century cookbooks": "كتب طبخ القرن 17",
    "1910s musicals": "مسرحيات غنائية عقد 1910",
    "1910s racehorse deaths": "خيول سباق نفقت في عقد 1910",
    "1914 mining disasters": "كوارث التعدين 1914",
    "1970s albums": "ألبومات عقد 1970",
    "1990s landslides": "انهيارات أرضية عقد 1990",
    "19th-century publications": "منشورات القرن 19",
    "2020s revolutions": "ثورات عقد 2020",
    "2020s transport disasters": "كوارث نقل في عقد 2020",
    "21st-century mosques": "مساجد القرن 21",
    "2nd-millennium texts": "نصوص الألفية 2",
    "15th-century executions": "إعدامات في القرن 15",
}


@pytest.mark.unit
def test_labsyears() -> None:
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


@pytest.mark.unit
def test_lab_from_year_no_year() -> None:
    """Should return empty tuple when no 4-digit year exists."""
    bot = LabsYears()
    result = bot.lab_from_year("Category:Something without year")
    assert result == ("", "")


@pytest.mark.unit
def test_lab_from_year_year_detected_but_no_template() -> None:
    """Should extract the year but return empty second value if template not found."""
    bot = LabsYears()
    result = bot.lab_from_year("Category:Works in 1999")
    assert result == ("1999", "")


@pytest.mark.unit
def test_lab_from_year_add_creates() -> None:
    """Should correctly create the template key/value with year replaced by {year1}."""
    bot = LabsYears()

    # _, label = bot.lab_from_year("Category:1670-related list")
    # assert label == "قوائم متعلقة ب1670"
    bot.category_templates = {}

    added = bot.lab_from_year_add("Category:2020s-related list", "قوائم متعلقة بعقد 2020", en_year="")
    assert added

    assert "{year1}-related list" in bot.category_templates

    _, label2 = bot.lab_from_year("Category:1670s-related list")
    assert label2 == "قوائم متعلقة بعقد 1670"


@pytest.mark.unit
def test_lab_from_year_add_creates_template() -> None:
    """Should correctly create the template key/value with year replaced by {year1}."""
    bot = LabsYears()

    bot.lab_from_year_add(
        category_r="Category:Films in 1999",
        category_lab="أفلام في 1999",
        en_year="1999",
    )

    assert "films in {year1}" in bot.category_templates
    assert bot.category_templates["films in {year1}"] == "أفلام في {year1}"


@pytest.mark.unit
def test_lab_from_year_successful_lookup_and_replacement() -> None:
    """Should return converted label and increment lookup_count."""
    bot = LabsYears()

    # Prepare template
    bot.lab_from_year_add(
        category_r="Category:Events in 2010",
        category_lab="أحداث في 2010",
        en_year="2010",
        ar_year="2010",
    )

    year, label = bot.lab_from_year("Category:Events in 2010")

    assert year == "2010"
    assert label == "أحداث في 2010"
    assert bot.lookup_count == 1


@pytest.mark.unit
def test_lab_from_year_template_exists_with_different_year() -> None:
    """Should correctly replace {year1} back to real year even if category is different year."""
    bot = LabsYears()

    # Add template for {year1}-base
    bot.lab_from_year_add(
        category_r="Category:Sports in 2022",
        category_lab="رياضة في 2022",
        en_year="2022",
        ar_year="2022",
    )

    # Now query for another valid year template
    year, label = bot.lab_from_year("Category:Sports in 2022")

    assert year == "2022"
    assert label == "رياضة في 2022"
    assert bot.lookup_count == 1


@pytest.mark.unit
def test_lab_from_year_add_missing_real_year() -> None:
    """Should do nothing if en_year is not inside category_lab."""
    bot = LabsYears()
    bot.category_templates = {}

    bot.lab_from_year_add(
        category_r="Category:Something in 2015",
        category_lab="شيء ما",  # Does NOT contain 2015
        en_year="2015",
        ar_year="",
    )

    assert bot.category_templates == {}


@pytest.mark.unit
def test_with_decade() -> None:
    bot = LabsYears()

    # Add template for {year1}-base
    bot.lab_from_year_add(
        category_r="Category:1990 works",
        category_lab="أعمال 1990",
        en_year="1990",
        ar_year="1990",
    )

    # Now query for another valid year template
    en_year = bot.match_en_time("Category:1990s works")
    assert en_year == "1990s"

    en_year2, label = bot.lab_from_year("Category:1990s works")

    assert en_year2 == "1990s"
    assert label == "أعمال عقد 1990"
    assert bot.lookup_count == 1
