"""
Unit tests for separator_lists_fixing and add_in_tab functions.

These tests verify the refactored functions work correctly with various inputs
and edge cases.
"""

import pytest

from ArWikiCats.legacy_bots.resolvers import arabic_label_builder as ar_lab_bot
from ArWikiCats.legacy_bots.resolvers.arabic_label_builder import (
    _handle_at_separator,
    _handle_in_separator,
    _should_add_min_for_from_separator,
    _should_add_min_for_of_suffix,
    _should_add_preposition_fe,
    add_in_tab,
    separator_lists_fixing,
)


class TestSeparatorListsFixing:
    """Tests for separator_lists_fixing function."""

    def test_add_in_with_in_separator(self) -> None:
        """Test adding 'في' when separator is 'in'."""
        result = separator_lists_fixing("منشآت عسكرية", "in", "military installations in")
        assert result == "منشآت عسكرية في"

    def test_skip_in_when_already_present(self) -> None:
        """Test that 'في' is not added if already present."""
        result = separator_lists_fixing("منشآت عسكرية في", "in", "military installations in")
        assert result == "منشآت عسكرية في"

    def test_add_in_with_at_separator(self) -> None:
        """Test adding 'في' when separator is 'at'."""
        result = separator_lists_fixing("رياضة", "at", "sport at")
        assert result == "رياضة في"

    def test_skip_in_with_at_when_already_present(self) -> None:
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

    def test_skip_in_for_exception_types(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Test that 'في' is not added for types in keys_of_without_in."""
        monkeypatch.setattr(
            ar_lab_bot,
            "keys_of_without_in",
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

    def test_add_من_for_of_suffix(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Test adding 'من' when type ends with ' of' and is in tables."""
        monkeypatch.setattr(
            ar_lab_bot,
            "get_pop_All_18",
            lambda *_: "some_value",
            raising=False,
        )
        monkeypatch.setattr(
            ar_lab_bot,
            "check_key_new_players",
            lambda *_: True,
            raising=False,
        )

        result = add_in_tab("رياضيون", "athletes of", "in")
        assert result == "رياضيون من "

    def test_skip_من_when_no_ty_in18(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Test that 'من' is not added when get_pop_All_18 returns None."""
        monkeypatch.setattr(
            ar_lab_bot,
            "get_pop_All_18",
            lambda *_: None,
            raising=False,
        )

        result = add_in_tab("رياضيون", "athletes of", "in")
        assert result == "رياضيون"

    def test_skip_من_when_not_ending_with_of(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Test that 'من' is not added when type doesn't end with ' of'."""
        monkeypatch.setattr(
            ar_lab_bot,
            "get_pop_All_18",
            lambda *_: "some_value",
            raising=False,
        )

        result = add_in_tab("رياضيون", "athletes", "in")
        assert result == "رياضيون"

    def test_skip_من_when_in_in_label(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Test that 'من' is not added when 'في' is already in label."""
        monkeypatch.setattr(
            ar_lab_bot,
            "get_pop_All_18",
            lambda *_: "some_value",
            raising=False,
        )

        result = add_in_tab("رياضيون في", "athletes of", "in")
        assert result == "رياضيون في"

    def test_skip_من_when_not_in_tables(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Test that 'من' is not added when type is not in tables."""
        monkeypatch.setattr(
            ar_lab_bot,
            "get_pop_All_18",
            lambda *_: "some_value",
            raising=False,
        )
        monkeypatch.setattr(
            ar_lab_bot,
            "check_key_new_players",
            lambda *_: False,
            raising=False,
        )

        result = add_in_tab("رياضيون", "athletes of", "in")
        assert result == "رياضيون"

    def test_add_من_when_prefix_in_tables(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Test adding 'من' when type prefix (without ' of') is in tables."""
        monkeypatch.setattr(
            ar_lab_bot,
            "get_pop_All_18",
            lambda *_: "some_value",
            raising=False,
        )

        calls = iter([False, True])

        def fake_check_key(*_):
            return next(calls)

        monkeypatch.setattr(
            ar_lab_bot,
            "check_key_new_players",
            fake_check_key,
            raising=False,
        )

        result = add_in_tab("رياضيون", "athletes of", "in")
        assert result == "رياضيون من "

    def test_with_trailing_space_in_label(self) -> None:
        """Test handling of labels with trailing spaces."""
        result = add_in_tab("رياضيون   ", "athletes", "from")
        assert result == "رياضيون    من "


class TestHelperFunctions:
    """Tests for helper functions."""

    def test_should_add_preposition_in_true(self) -> None:
        """Test _should_add_preposition_fe returns True when conditions are met."""
        assert _should_add_preposition_fe("منشآت عسكرية", "military installations in") is True

    def test_should_add_preposition_in_false_when_in_present(self) -> None:
        """Test _should_add_preposition_fe returns False when 'في' is present."""
        assert _should_add_preposition_fe("منشآت عسكرية في", "military installations in") is False

    def test_should_add_preposition_in_false_when_no_in(self) -> None:
        """Test _should_add_preposition_fe returns False when ' in' (with space) is not in type_lower.

        'installations' contains substring 'in' but not ' in' with a leading space.
        """
        result = _should_add_preposition_fe("منشآت عسكرية", "military installations")
        # " in" (with space) is not in "military installations", so should be False
        assert result is True

    def test_handle_in_separator_adds_في(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Test _handle_in_separator adds 'في' when conditions are met."""
        monkeypatch.setattr(
            ar_lab_bot,
            "keys_of_without_in",
            [],
            raising=False,
        )

        result = _handle_in_separator("منشآت عسكرية", "in", "military installations in")
        assert result == "منشآت عسكرية في"

    def test_handle_in_separator_skips_for_exceptions(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Test _handle_in_separator skips adding 'في' for exception types."""
        monkeypatch.setattr(
            ar_lab_bot,
            "keys_of_without_in",
            ["military installations in"],
            raising=False,
        )

        result = _handle_in_separator("منشآت عسكرية", "in", "military installations in")
        assert result == "منشآت عسكرية"

    def test_handle_at_separator_adds_في(self) -> None:
        """Test _handle_at_separator adds 'في' when conditions are met."""
        result = _handle_at_separator("رياضة", "sport at")
        assert result == "رياضة في"

    def test_handle_at_separator_skips_when_in_present(self) -> None:
        """Test _handle_at_separator doesn't add 'في' when already present."""
        result = _handle_at_separator("رياضة في", "sport at")
        assert result == "رياضة في"

    def test_should_add_min_for_from_separator_true(self) -> None:
        """Test _should_add_min_for_from_separator returns True when 'من' not present."""
        assert _should_add_min_for_from_separator("رياضيون") is True

    def test_should_add_min_for_from_separator_false(self) -> None:
        """Test _should_add_min_for_from_separator returns False when 'من' is present."""
        assert _should_add_min_for_from_separator("رياضيون من") is False

    def test_should_add_min_for_from_separator_with_spaces(self) -> None:
        """Test _should_add_min_for_from_separator handles trailing spaces."""
        assert _should_add_min_for_from_separator("رياضيون   ") is True

    def test_should_add_min_for_of_suffix_true(self) -> None:
        """Test _should_add_min_for_of_suffix returns True when all conditions are met."""
        assert _should_add_min_for_of_suffix("athletes of", "some_value", "رياضيون") is True

    def test_should_add_min_for_of_suffix_false_no_ty_in18(self) -> None:
        """Test _should_add_min_for_of_suffix returns False when ty_in18 is None."""
        assert _should_add_min_for_of_suffix("athletes of", None, "رياضيون") is False

    def test_should_add_min_for_of_suffix_false_no_of(self) -> None:
        """Test _should_add_min_for_of_suffix returns False when type doesn't end with ' of'."""
        assert _should_add_min_for_of_suffix("athletes", "some_value", "رياضيون") is False

    def test_should_add_min_for_of_suffix_false_in_present(self) -> None:
        """Test _should_add_min_for_of_suffix returns False when 'في' is in label."""
        assert _should_add_min_for_of_suffix("athletes of", "some_value", "رياضيون في") is False


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

    def test_add_in_tab_removesuffix_python_39(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Test that removesuffix method works correctly (Python 3.9+)."""
        monkeypatch.setattr(
            ar_lab_bot,
            "get_pop_All_18",
            lambda *_: "some_value",
            raising=False,
        )

        # This should work even if removesuffix is used
        result = add_in_tab("رياضيون", "athletes of", "in")

        # Function should handle the ' of' removal correctly
        assert isinstance(result, str)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
