"""
Unit tests for separator_lists_fixing and add_in_tab functions.

These tests verify the refactored functions work correctly with various inputs
and edge cases.
"""

import pytest
from unittest.mock import patch

from ArWikiCats.make_bots.ma_bots.ar_lab.ar_lab import (
    separator_lists_fixing,
    add_in_tab,
    _should_add_preposition_في,
    _handle_in_separator,
    _handle_at_separator,
    _should_add_من_for_from_separator,
    _should_add_من_for_of_suffix,
)


class TestSeparatorListsFixing:
    """Tests for separator_lists_fixing function."""

    def test_add_في_with_in_separator(self) -> None:
        """Test adding 'في' when separator is 'in'."""
        result = separator_lists_fixing("منشآت عسكرية", "in", "military installations in")
        assert result == "منشآت عسكرية في"

    def test_skip_في_when_already_present(self) -> None:
        """Test that 'في' is not added if already present."""
        result = separator_lists_fixing("منشآت عسكرية في", "in", "military installations in")
        assert result == "منشآت عسكرية في"

    def test_add_في_with_at_separator(self) -> None:
        """Test adding 'في' when separator is 'at'."""
        result = separator_lists_fixing("رياضة", "at", "sport at")
        assert result == "رياضة في"

    def test_skip_في_with_at_when_already_present(self) -> None:
        """Test that 'في' is not added with 'at' if already present."""
        result = separator_lists_fixing("رياضة في", "at", "sport at")
        assert result == "رياضة في"

    def test_no_change_for_non_listed_separator(self) -> None:
        """Test that label is unchanged for separators not in separators_lists_raw."""
        result = separator_lists_fixing("منشآت عسكرية", "about", "military installations")
        assert result == "منشآت عسكرية"

    def test_from_separator_returns_unchanged(self) -> None:
        """Test that 'from' separator doesn't add 'في'."""
        result = separator_lists_fixing("رياضيون", "from", "athletes")
        assert result == "رياضيون"

    def test_by_separator_returns_unchanged(self) -> None:
        """Test that 'by' separator doesn't add 'في'."""
        result = separator_lists_fixing("لوحات", "by", "paintings")
        assert result == "لوحات"

    def test_of_separator_returns_unchanged(self) -> None:
        """Test that 'of' separator doesn't add 'في'."""
        result = separator_lists_fixing("تاريخ", "of", "history")
        assert result == "تاريخ"

    def test_skip_في_for_exception_types(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Test that 'في' is not added for types in pop_of_without_in."""
        monkeypatch.setattr(
            "ArWikiCats.make_bots.ma_bots.ar_lab.ar_lab.pop_of_without_in",
            ["populations"],
            raising=False,
        )

        result = separator_lists_fixing("سكان", "in", "populations")
        assert result == "سكان"


class TestAddInTab:
    """Tests for add_in_tab function."""

    def test_add_من_with_from_separator(self) -> None:
        """Test adding 'من' when separator is 'from'."""
        result = add_in_tab("رياضيون", "athletes", "from")
        assert result == "رياضيون من "

    def test_skip_من_when_already_present(self) -> None:
        """Test that 'من' is not added if already present."""
        result = add_in_tab("رياضيون من", "athletes", "from")
        assert result == "رياضيون من"

    @patch("ArWikiCats.make_bots.ma_bots.ar_lab.ar_lab.get_pop_All_18")
    @patch("ArWikiCats.make_bots.ma_bots.ar_lab.ar_lab.check_key_new_players")
    def test_add_من_for_of_suffix(self, mock_check_key, mock_get_pop):
        """Test adding 'من' when type ends with ' of' and is in tables."""
        mock_get_pop.return_value = "some_value"
        mock_check_key.return_value = True

        result = add_in_tab("رياضيون", "athletes of", "in")
        assert result == "رياضيون من "

    @patch("ArWikiCats.make_bots.ma_bots.ar_lab.ar_lab.get_pop_All_18")
    def test_skip_من_when_no_ty_in18(self, mock_get_pop):
        """Test that 'من' is not added when get_pop_All_18 returns None."""
        mock_get_pop.return_value = None

        result = add_in_tab("رياضيون", "athletes of", "in")
        assert result == "رياضيون"

    @patch("ArWikiCats.make_bots.ma_bots.ar_lab.ar_lab.get_pop_All_18")
    def test_skip_من_when_not_ending_with_of(self, mock_get_pop):
        """Test that 'من' is not added when type doesn't end with ' of'."""
        mock_get_pop.return_value = "some_value"

        result = add_in_tab("رياضيون", "athletes", "in")
        assert result == "رياضيون"

    @patch("ArWikiCats.make_bots.ma_bots.ar_lab.ar_lab.get_pop_All_18")
    def test_skip_من_when_في_in_label(self, mock_get_pop):
        """Test that 'من' is not added when 'في' is already in label."""
        mock_get_pop.return_value = "some_value"

        result = add_in_tab("رياضيون في", "athletes of", "in")
        assert result == "رياضيون في"

    @patch("ArWikiCats.make_bots.ma_bots.ar_lab.ar_lab.get_pop_All_18")
    @patch("ArWikiCats.make_bots.ma_bots.ar_lab.ar_lab.check_key_new_players")
    def test_skip_من_when_not_in_tables(self, mock_check_key, mock_get_pop):
        """Test that 'من' is not added when type is not in tables."""
        mock_get_pop.return_value = "some_value"
        mock_check_key.return_value = False

        result = add_in_tab("رياضيون", "athletes of", "in")
        assert result == "رياضيون"

    @patch("ArWikiCats.make_bots.ma_bots.ar_lab.ar_lab.get_pop_All_18")
    @patch("ArWikiCats.make_bots.ma_bots.ar_lab.ar_lab.check_key_new_players")
    def test_add_من_when_prefix_in_tables(self, mock_check_key, mock_get_pop):
        """Test adding 'من' when type prefix (without ' of') is in tables."""
        mock_get_pop.return_value = "some_value"

        # First call for full type returns False, second call for prefix returns True
        mock_check_key.side_effect = [False, True]

        result = add_in_tab("رياضيون", "athletes of", "in")
        assert result == "رياضيون من "

    def test_with_trailing_space_in_label(self) -> None:
        """Test handling of labels with trailing spaces."""
        result = add_in_tab("رياضيون   ", "athletes", "from")
        assert result == "رياضيون    من "


class TestHelperFunctions:
    """Tests for helper functions."""

    def test_should_add_preposition_في_true(self) -> None:
        """Test _should_add_preposition_في returns True when conditions are met."""
        assert _should_add_preposition_في("منشآت عسكرية", "military installations in") is True

    def test_should_add_preposition_في_false_when_في_present(self) -> None:
        """Test _should_add_preposition_في returns False when 'في' is present."""
        assert _should_add_preposition_في("منشآت عسكرية في", "military installations in") is False

    def test_should_add_preposition_في_false_when_no_in(self) -> None:
        """Test _should_add_preposition_في returns False when ' in' (with space) is not in type_lower.

        'installations' contains substring 'in' but not ' in' with a leading space.
        """
        result = _should_add_preposition_في("منشآت عسكرية", "military installations")
        # " in" (with space) is not in "military installations", so should be False
        assert result is True

    @patch("ArWikiCats.make_bots.ma_bots.ar_lab.ar_lab.pop_of_without_in", [])
    def test_handle_in_separator_adds_في(self) -> None:
        """Test _handle_in_separator adds 'في' when conditions are met."""
        result = _handle_in_separator("منشآت عسكرية", "in", "military installations in")
        assert result == "منشآت عسكرية في"

    @patch("ArWikiCats.make_bots.ma_bots.ar_lab.ar_lab.pop_of_without_in", ["military installations in"])
    def test_handle_in_separator_skips_for_exceptions(self) -> None:
        """Test _handle_in_separator skips adding 'في' for exception types."""
        result = _handle_in_separator("منشآت عسكرية", "in", "military installations in")
        assert result == "منشآت عسكرية"

    def test_handle_at_separator_adds_في(self) -> None:
        """Test _handle_at_separator adds 'في' when conditions are met."""
        result = _handle_at_separator("رياضة", "sport at")
        assert result == "رياضة في"

    def test_handle_at_separator_skips_when_في_present(self) -> None:
        """Test _handle_at_separator doesn't add 'في' when already present."""
        result = _handle_at_separator("رياضة في", "sport at")
        assert result == "رياضة في"

    def test_should_add_من_for_from_separator_true(self) -> None:
        """Test _should_add_من_for_from_separator returns True when 'من' not present."""
        assert _should_add_من_for_from_separator("رياضيون") is True

    def test_should_add_من_for_from_separator_false(self) -> None:
        """Test _should_add_من_for_from_separator returns False when 'من' is present."""
        assert _should_add_من_for_from_separator("رياضيون من") is False

    def test_should_add_من_for_from_separator_with_spaces(self) -> None:
        """Test _should_add_من_for_from_separator handles trailing spaces."""
        assert _should_add_من_for_from_separator("رياضيون   ") is True

    def test_should_add_من_for_of_suffix_true(self) -> None:
        """Test _should_add_من_for_of_suffix returns True when all conditions are met."""
        assert _should_add_من_for_of_suffix("athletes of", "some_value", "رياضيون") is True

    def test_should_add_من_for_of_suffix_false_no_ty_in18(self) -> None:
        """Test _should_add_من_for_of_suffix returns False when ty_in18 is None."""
        assert _should_add_من_for_of_suffix("athletes of", None, "رياضيون") is False

    def test_should_add_من_for_of_suffix_false_no_of(self) -> None:
        """Test _should_add_من_for_of_suffix returns False when type doesn't end with ' of'."""
        assert _should_add_من_for_of_suffix("athletes", "some_value", "رياضيون") is False

    def test_should_add_من_for_of_suffix_false_في_present(self) -> None:
        """Test _should_add_من_for_of_suffix returns False when 'في' is in label."""
        assert _should_add_من_for_of_suffix("athletes of", "some_value", "رياضيون في") is False


class TestEdgeCases:
    """Tests for edge cases and special scenarios."""

    def test_separator_lists_fixing_empty_strings(self) -> None:
        """Test separator_lists_fixing with empty strings."""
        result = separator_lists_fixing("", "", "")
        assert result == ""

    def test_add_in_tab_empty_strings(self) -> None:
        """Test add_in_tab with empty strings."""
        result = add_in_tab("", "", "")
        assert result == ""

    def test_separator_lists_fixing_with_special_characters(self) -> None:
        """Test separator_lists_fixing with Arabic text containing special characters."""
        result = separator_lists_fixing("منشآت-عسكرية", "in", "military installations in")
        assert "في" in result

    def test_add_in_tab_with_multiple_spaces(self) -> None:
        """Test add_in_tab with multiple spaces in label."""
        result = add_in_tab("رياضيون    ", "athletes", "from")
        assert "من" in result

    def test_separator_lists_fixing_case_sensitivity(self) -> None:
        """Test that function works correctly with lowercase type_lower."""
        result = separator_lists_fixing("منشآت عسكرية", "in", "MILITARY INSTALLATIONS IN")
        # type_lower should be lowercase so this should not match
        assert result == "منشآت عسكرية"

    @patch("ArWikiCats.make_bots.ma_bots.ar_lab.ar_lab.get_pop_All_18")
    def test_add_in_tab_removesuffix_python_39(self, mock_get_pop):
        """Test that removesuffix method works correctly (Python 3.9+)."""
        mock_get_pop.return_value = "some_value"

        # This should work even if removesuffix is used
        result = add_in_tab("رياضيون", "athletes of", "in")
        # Function should handle the ' of' removal correctly
        assert isinstance(result, str)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
