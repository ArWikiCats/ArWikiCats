#!/usr/bin/python3
"""
Unit tests for time_patterns_formats.py module.

This module provides tests for LabsYearsFormat and MatchTimes classes
which handle year-based category label generation.
"""

from ArWikiCats.translations_formats.time_patterns_formats import (
    LabsYearsFormat,
    MatchTimes,
)


class TestMatchTimes:
    """Tests for MatchTimes class."""

    def test_init(self):
        """Test initialization of MatchTimes."""
        matcher = MatchTimes()
        assert matcher is not None

    def test_match_en_time_century(self):
        """Test matching English century patterns."""
        matcher = MatchTimes()
        result = matcher.match_en_time("14th-century writers")
        assert result == "14th-century"

    def test_match_en_time_decade(self):
        """Test matching English decade patterns."""
        matcher = MatchTimes()
        result = matcher.match_en_time("1990s films")
        assert result == "1990s"

    def test_match_en_time_year(self):
        """Test matching English year patterns."""
        matcher = MatchTimes()
        result = matcher.match_en_time("2020 events")
        assert result == "2020"

    def test_match_en_time_no_match(self):
        """Test match_en_time returns empty string when no match."""
        matcher = MatchTimes()
        result = matcher.match_en_time("no time pattern here")
        assert result == ""

    def test_match_ar_time_century(self):
        """Test matching Arabic century patterns."""
        matcher = MatchTimes()
        result = matcher.match_ar_time("القرن 14 كتاب")
        assert result == "القرن 14"

    def test_match_ar_time_decade(self):
        """Test matching Arabic decade patterns."""
        matcher = MatchTimes()
        result = matcher.match_ar_time("عقد 1990 أحداث")
        assert result == "عقد 1990"

    def test_match_ar_time_year(self):
        """Test matching Arabic year patterns - plain years without prefix don't match."""
        matcher = MatchTimes()
        # Plain years without a time prefix like "سنة" or "عقد" return empty
        result = matcher.match_ar_time("2020 أحداث")
        assert result == ""


class TestLabsYearsFormat:
    """Tests for LabsYearsFormat class."""

    def test_init(self):
        """Test initialization of LabsYearsFormat."""
        templates = {"{year1} events": "أحداث {year1}"}
        formatter = LabsYearsFormat(category_templates=templates)
        assert formatter.category_templates == templates
        assert formatter.lookup_count == 0

    def test_init_custom_placeholders(self):
        """Test initialization with custom placeholders."""
        templates = {"{time} events": "أحداث {time_ar}"}
        formatter = LabsYearsFormat(
            category_templates=templates,
            key_param_placeholder="{time}",
            value_param_placeholder="{time_ar}",
            year_param_name="time_ar",
        )
        assert formatter.key_param_placeholder == "{time}"
        assert formatter.value_param_placeholder == "{time_ar}"
        assert formatter.year_param_name == "time_ar"

    def test_lab_from_year_basic(self):
        """Test lab_from_year with basic year pattern."""
        templates = {"{year1} events": "أحداث {year1}"}
        formatter = LabsYearsFormat(category_templates=templates)

        cat_year, from_year = formatter.lab_from_year("2020 events")

        assert cat_year == "2020"
        assert from_year == "أحداث 2020"

    def test_lab_from_year_century(self):
        """Test lab_from_year with century pattern."""
        templates = {"{year1} writers": "كتاب {year1}"}
        formatter = LabsYearsFormat(category_templates=templates)

        cat_year, from_year = formatter.lab_from_year("14th-century writers")

        assert cat_year == "14th-century"
        assert from_year == "كتاب القرن 14"

    def test_lab_from_year_decade(self):
        """Test lab_from_year with decade pattern."""
        templates = {"{year1} films": "أفلام {year1}"}
        formatter = LabsYearsFormat(category_templates=templates)

        cat_year, from_year = formatter.lab_from_year("1990s films")

        assert cat_year == "1990s"
        assert from_year == "أفلام عقد 1990"

    def test_lab_from_year_no_match(self):
        """Test lab_from_year when no year pattern matches."""
        templates = {"{year1} events": "أحداث {year1}"}
        formatter = LabsYearsFormat(category_templates=templates)

        cat_year, from_year = formatter.lab_from_year("no time pattern")

        assert cat_year == ""
        assert from_year == ""

    def test_lab_from_year_no_template(self):
        """Test lab_from_year when template not found."""
        templates = {"{year1} events": "أحداث {year1}"}
        formatter = LabsYearsFormat(category_templates=templates)

        cat_year, from_year = formatter.lab_from_year("2020 films")

        assert cat_year == "2020"
        assert from_year == ""

    def test_lab_from_year_with_category_prefix(self):
        """Test lab_from_year strips category: prefix."""
        templates = {"{year1} events": "أحداث {year1}"}
        formatter = LabsYearsFormat(category_templates=templates)

        cat_year, from_year = formatter.lab_from_year("Category:2020 events")

        assert cat_year == "2020"
        assert from_year == "أحداث 2020"

    def test_lab_from_year_increments_lookup_count(self):
        """Test that successful lookups increment lookup_count."""
        templates = {"{year1} events": "أحداث {year1}"}
        formatter = LabsYearsFormat(category_templates=templates)

        assert formatter.lookup_count == 0
        formatter.lab_from_year("2020 events")
        assert formatter.lookup_count == 1
        formatter.lab_from_year("2021 events")
        assert formatter.lookup_count == 2

    def test_lab_from_year_with_fixing_callback(self):
        """Test lab_from_year with fixing_callback."""
        templates = {"{year1} events": "أحداث {year1}"}

        def fix_callback(label):
            return label.replace("أحداث", "فعاليات")

        formatter = LabsYearsFormat(
            category_templates=templates,
            fixing_callback=fix_callback,
        )

        cat_year, from_year = formatter.lab_from_year("2020 events")

        assert from_year == "فعاليات 2020"

    def test_lab_from_year_add_basic(self):
        """Test lab_from_year_add adds a new template."""
        templates = {}
        formatter = LabsYearsFormat(category_templates=templates)

        result = formatter.lab_from_year_add(
            category_r="2020 events",
            category_lab="أحداث 2020",
            en_year="2020",
            ar_year="2020",
        )

        assert result is True
        assert "{year1} events" in formatter.category_templates
        assert formatter.category_templates["{year1} events"] == "أحداث {year1}"

    def test_lab_from_year_add_missing_en_year(self):
        """Test lab_from_year_add when en_year not in category_r."""
        templates = {}
        formatter = LabsYearsFormat(category_templates=templates)

        result = formatter.lab_from_year_add(
            category_r="no year events",
            category_lab="أحداث 2020",
            en_year="2020",
            ar_year="2020",
        )

        assert result is False

    def test_lab_from_year_add_missing_ar_year(self):
        """Test lab_from_year_add when ar_year not in category_lab."""
        templates = {}
        formatter = LabsYearsFormat(category_templates=templates)

        result = formatter.lab_from_year_add(
            category_r="2020 events",
            category_lab="أحداث بدون سنة",
            en_year="2020",
            ar_year="2020",
        )

        assert result is False

    def test_lab_from_year_add_strips_category_prefix(self):
        """Test lab_from_year_add strips category: prefix."""
        templates = {}
        formatter = LabsYearsFormat(category_templates=templates)

        result = formatter.lab_from_year_add(
            category_r="Category:2020 events",
            category_lab="أحداث 2020",
            en_year="2020",
            ar_year="2020",
        )

        assert result is True
        assert "{year1} events" in formatter.category_templates

    def test_lab_from_year_add_auto_detect_en_year(self):
        """Test lab_from_year_add auto-detects en_year when not provided."""
        templates = {}
        formatter = LabsYearsFormat(category_templates=templates)

        result = formatter.lab_from_year_add(
            category_r="2020 events",
            category_lab="أحداث 2020",
            en_year="",
            ar_year="2020",
        )

        assert result is True
        assert "{year1} events" in formatter.category_templates

    def test_lab_from_year_add_auto_detect_ar_year(self):
        """Test lab_from_year_add auto-detects ar_year when not provided."""
        templates = {}
        formatter = LabsYearsFormat(category_templates=templates)

        result = formatter.lab_from_year_add(
            category_r="2020 events",
            category_lab="أحداث 2020",
            en_year="2020",
            ar_year="",
        )

        assert result is True
        assert "{year1} events" in formatter.category_templates

    def test_lab_from_year_add_digit_fallback(self):
        """Test lab_from_year_add uses en_year for ar_year when en_year is digit."""
        templates = {}
        formatter = LabsYearsFormat(category_templates=templates)

        result = formatter.lab_from_year_add(
            category_r="2020 events",
            category_lab="أحداث 2020",
            en_year="2020",
            ar_year="",
        )

        assert result is True


class TestLabsYearsFormatInheritance:
    """Tests for LabsYearsFormat inheritance from MatchTimes."""

    def test_inherits_from_match_times(self):
        """Test that LabsYearsFormat inherits from MatchTimes."""
        templates = {"{year1} events": "أحداث {year1}"}
        formatter = LabsYearsFormat(category_templates=templates)

        assert isinstance(formatter, MatchTimes)

    def test_has_match_en_time_method(self):
        """Test that LabsYearsFormat has match_en_time method from MatchTimes."""
        templates = {"{year1} events": "أحداث {year1}"}
        formatter = LabsYearsFormat(category_templates=templates)

        result = formatter.match_en_time("2020 events")
        assert result == "2020"

    def test_has_match_ar_time_method(self):
        """Test that LabsYearsFormat has match_ar_time method from MatchTimes."""
        templates = {"{year1} events": "أحداث {year1}"}
        formatter = LabsYearsFormat(category_templates=templates)

        result = formatter.match_ar_time("أحداث 2020")
        assert result == "2020"
