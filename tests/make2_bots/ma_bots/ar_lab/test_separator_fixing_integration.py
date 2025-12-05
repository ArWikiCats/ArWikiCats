"""
Integration tests for separator_lists_fixing and add_in_tab functions.

These tests verify the functions work correctly with real-world scenarios
and actual data dependencies.
"""

import pytest

from ArWikiCats.make_bots.ma_bots.ar_lab.ar_lab import (
    separator_lists_fixing,
    add_in_tab,
)


class TestSeparatorListsFixingIntegration:
    """Integration tests for separator_lists_fixing with real data."""

    @pytest.mark.fast
    def test_military_installations_in(self):
        """Test real-world example: military installations in."""
        result = separator_lists_fixing(
            type_label="منشآت عسكرية",
            separator_stripped="in",
            type_lower="military installations in"
        )
        assert result == "منشآت عسكرية في"
        assert " في" in result
        assert result.endswith("في")

    @pytest.mark.fast
    def test_sport_at_location(self):
        """Test real-world example: sport at location."""
        result = separator_lists_fixing(
            type_label="رياضة",
            separator_stripped="at",
            type_lower="sport at"
        )
        assert result == "رياضة في"

    @pytest.mark.fast
    def test_complex_label_with_in(self):
        """Test complex Arabic label with 'in' separator."""
        result = separator_lists_fixing(
            type_label="أحداث رياضية",
            separator_stripped="in",
            type_lower="sports events in"
        )
        assert result == "أحداث رياضية في"

    @pytest.mark.fast
    def test_preserves_existing_في(self):
        """Test that existing 'في' is preserved."""
        result = separator_lists_fixing(
            type_label="أحداث رياضية في",
            separator_stripped="in",
            type_lower="sports events in"
        )
        # Should not add duplicate في
        assert result.count(" في") == 1

    @pytest.mark.fast
    def test_multiple_word_labels(self):
        """Test with multi-word Arabic labels."""
        result = separator_lists_fixing(
            type_label="المنشآت الرياضية الكبرى",
            separator_stripped="in",
            type_lower="major sports facilities in"
        )
        assert result == "المنشآت الرياضية الكبرى في"


class TestAddInTabIntegration:
    """Integration tests for add_in_tab with real data."""

    @pytest.mark.fast
    def test_athletes_from_country(self):
        """Test real-world example: athletes from country."""
        result = add_in_tab(
            type_label="رياضيون",
            type_lower="athletes",
            separator_stripped="from"
        )
        assert result == "رياضيون من "
        assert " من " in result
        assert result.endswith("من ")

    @pytest.mark.fast
    def test_preserves_existing_من(self):
        """Test that existing 'من' is preserved."""
        result = add_in_tab(
            type_label="رياضيون من",
            type_lower="athletes",
            separator_stripped="from"
        )
        # Should not add duplicate من
        assert result.count(" من") == 1

    @pytest.mark.fast
    @pytest.mark.slow
    def test_footballers_of_team(self):
        """Test real-world example: footballers of team."""
        # This test requires actual data dependencies
        result = add_in_tab(
            type_label="لاعبو كرة قدم",
            type_lower="footballers of",
            separator_stripped="in"
        )
        # Result depends on get_pop_All_18 and check_key_new_players
        assert isinstance(result, str)
        # Should either add 'من' or return unchanged
        assert result.startswith("لاعبو كرة قدم")

    @pytest.mark.fast
    def test_with_real_arabic_labels(self):
        """Test with various real Arabic category labels."""
        test_cases = [
            ("رياضيون", "athletes", "from", "رياضيون من "),
            ("لاعبون", "players", "from", "لاعبون من "),
            ("مدربون", "coaches", "from", "مدربون من "),
        ]

        for type_label, type_lower, separator, expected in test_cases:
            result = add_in_tab(type_label, type_lower, separator)
            assert result == expected, f"Failed for {type_label}"


class TestCombinedUsage:
    """Tests for using both functions together as they would be in practice."""

    @pytest.mark.fast
    def test_sequential_application(self):
        """Test applying both functions sequentially."""
        # First apply separator_lists_fixing
        label = "منشآت عسكرية"
        label = separator_lists_fixing(label, "in", "military installations in")
        assert " في" in label

        # Then apply add_in_tab (though في should prevent من from being added)
        label = add_in_tab(label, "military installations", "from")
        # Should not have من because في is present
        assert " من" not in label

    @pytest.mark.fast
    def test_from_then_in_separator(self):
        """Test from separator followed by checking in conditions."""
        label = "رياضيون"

        # Apply from separator
        label = add_in_tab(label, "athletes", "from")
        assert label == "رياضيون من "

        # في should not be added if we use separator_lists_fixing after
        # because it doesn't apply to 'from' separator
        label_with_from = separator_lists_fixing(label, "from", "athletes")
        assert label_with_from == label  # unchanged

    @pytest.mark.fast
    def test_workflow_for_category_processing(self):
        """Test a realistic workflow for processing a category."""
        # Simulate processing "Military installations in France"
        type_label = "منشآت عسكرية"
        type_lower = "military installations in"
        separator = "in"

        # Step 1: Fix separator
        type_label = separator_lists_fixing(type_label, separator, type_lower)
        assert type_label == "منشآت عسكرية في"

        # Step 2: Check if we need to add من
        type_label = add_in_tab(type_label, type_lower, separator)
        # Should not add من because في is already there
        assert " من" not in type_label


class TestRealWorldScenarios:
    """Tests based on actual Wikipedia category patterns."""

    @pytest.mark.fast
    def test_establishments_in_country(self):
        """Test: 'Establishments in country' pattern."""
        result = separator_lists_fixing("تأسيسات", "in", "establishments in")
        assert result == "تأسيسات في"

    @pytest.mark.fast
    def test_people_from_country(self):
        """Test: 'People from country' pattern."""
        result = add_in_tab("أشخاص", "people", "from")
        assert result == "أشخاص من "

    @pytest.mark.fast
    def test_events_at_location(self):
        """Test: 'Events at location' pattern."""
        result = separator_lists_fixing("أحداث", "at", "events at")
        assert result == "أحداث في"

    @pytest.mark.fast
    def test_buildings_and_structures_in(self):
        """Test: 'Buildings and structures in' pattern."""
        result = separator_lists_fixing("مبانٍ ومنشآت", "in", "buildings and structures in")
        assert result == "مبانٍ ومنشآت في"

    @pytest.mark.fast
    def test_organizations_based_in(self):
        """Test: 'Organizations based in' pattern."""
        result = separator_lists_fixing("منظمات", "in", "organizations based in")
        assert result == "منظمات في"


class TestDataConsistency:
    """Tests to ensure data consistency and invariants."""

    @pytest.mark.fast
    def test_idempotency_separator_fixing(self):
        """Test that applying separator_lists_fixing twice gives same result."""
        label = "منشآت عسكرية"
        result1 = separator_lists_fixing(label, "in", "military installations in")
        result2 = separator_lists_fixing(result1, "in", "military installations in")
        assert result1 == result2

    @pytest.mark.fast
    def test_idempotency_add_in_tab(self):
        """Test that applying add_in_tab twice gives same result."""
        label = "رياضيون"
        result1 = add_in_tab(label, "athletes", "from")
        result2 = add_in_tab(result1, "athletes", "from")
        assert result1 == result2

    @pytest.mark.fast
    def test_no_double_spaces(self):
        """Test that functions don't create double spaces."""
        result1 = separator_lists_fixing("منشآت", "in", "installations in")
        assert "  " not in result1

        result2 = add_in_tab("رياضيون", "athletes", "from")
        # Single space before من is expected
        assert result2.count("  ") == 0 or result2.endswith("من ")

    @pytest.mark.fast
    def test_preserves_arabic_text_integrity(self):
        """Test that Arabic text is not corrupted."""
        original = "المنشآت العسكرية الحديثة"
        result = separator_lists_fixing(original, "in", "modern military installations in")
        # Should preserve the original text and only add في
        assert result.startswith(original)
        assert len(result) >= len(original)


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-m", "fast"])
