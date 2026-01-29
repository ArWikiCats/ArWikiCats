"""
Unit tests for mk3 module.
"""

import pytest

from ArWikiCats.legacy_bots.legacy_resolvers_bots.mk3 import (
    ARABIC_PREPOSITION_FI,
    PREPOSITION_AT,
    PREPOSITION_IN,
    add_the_in,
    added_in_new,
    check_country_in_tables,
    country_before_year,
    new_func_mk2,
)

# ---------------------------------------------------------------------------
# Tests for check_country_in_tables function
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestCheckCountryInTables:
    """Tests for the check_country_in_tables function."""

    def test_returns_true_for_country_in_country_before_year(self) -> None:
        """Should return True for countries in country_before_year list."""
        assert check_country_in_tables("disasters") is True
        assert check_country_in_tables("sports") is True
        assert check_country_in_tables("discoveries") is True

    def test_returns_false_for_unknown_country(self) -> None:
        """Should return False for countries not in any table."""
        result = check_country_in_tables("unknown_random_country_xyz")
        assert result is False

    def test_returns_false_for_empty_string(self) -> None:
        """Should return False for empty string."""
        result = check_country_in_tables("")
        assert result is False

    def test_motorsport_in_tables(self) -> None:
        """Should return True for motorsport."""
        assert check_country_in_tables("motorsport") is True

    def test_spaceflight_in_tables(self) -> None:
        """Should return True for spaceflight."""
        assert check_country_in_tables("spaceflight") is True


# ---------------------------------------------------------------------------
# Tests for add_the_in function
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestAddTheIn:
    """Tests for the add_the_in function."""

    def test_basic_call_returns_tuple(self) -> None:
        """Should return a tuple with three elements."""
        result = add_the_in(
            in_table=False,
            country="test",
            arlabel="تسمية",
            suf=" ",
            In=" in ",
            typeo="",
            year_labe="1900",
            country_label="البلد",
            cat_test="test in country",
        )
        assert isinstance(result, tuple)
        assert len(result) == 3

    def test_returns_add_in_done_boolean(self) -> None:
        """Should return Add_In_Done as boolean."""
        add_in_done, _, _ = add_the_in(
            in_table=False,
            country="test",
            arlabel="تسمية",
            suf=" ",
            In=" in ",
            typeo="",
            year_labe="1900",
            country_label="البلد",
            cat_test="test",
        )
        assert isinstance(add_in_done, bool)

    def test_returns_arlabel_as_string(self) -> None:
        """Should return arlabel as string."""
        _, arlabel, _ = add_the_in(
            in_table=False,
            country="test",
            arlabel="تسمية",
            suf=" ",
            In="",
            typeo="",
            year_labe="1900",
            country_label="البلد",
            cat_test="test",
        )
        assert isinstance(arlabel, str)

    def test_in_preposition_triggers_addition(self) -> None:
        """Should add 'في' when In is 'in'."""
        add_in_done, arlabel, _ = add_the_in(
            in_table=False,
            country="test",
            arlabel="تسمية",
            suf=" ",
            In=" in ",
            typeo="",
            year_labe="1900",
            country_label="البلد",
            cat_test="test in country",
        )
        assert add_in_done is True
        assert ARABIC_PREPOSITION_FI.strip() in arlabel

    def test_at_preposition_triggers_addition(self) -> None:
        """Should add 'في' when In is 'at'."""
        add_in_done, arlabel, _ = add_the_in(
            in_table=False,
            country="test",
            arlabel="تسمية",
            suf=" ",
            In=" at ",
            typeo="",
            year_labe="1900",
            country_label="البلد",
            cat_test="test at country",
        )
        assert add_in_done is True

    def test_in_table_true_uses_different_order(self) -> None:
        """When in_table is True, label construction order changes."""
        _, arlabel, _ = add_the_in(
            in_table=True,
            country="disasters",
            arlabel="تسمية",
            suf=" ",
            In="",
            typeo="",
            year_labe="1900",
            country_label="البلد",
            cat_test="test",
        )
        assert isinstance(arlabel, str)
        # When in_table is True, country_label comes first
        assert arlabel.startswith("البلد") or "البلد" in arlabel


# ---------------------------------------------------------------------------
# Tests for added_in_new function
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestAddedInNew:
    """Tests for the added_in_new function."""

    def test_basic_call_returns_tuple(self) -> None:
        """Should return a tuple with three elements."""
        result = added_in_new(
            country="test",
            arlabel="تسمية",
            suf="",
            year_labe="1900",
            country_label="البلد",
            Add_In=True,
            arlabel2="1900",
        )
        assert isinstance(result, tuple)
        assert len(result) == 3

    def test_returns_arlabel_country_label_and_arlabel2_combined(self) -> None:
        """Should combine country_label, suf, and arlabel2."""
        arlabel, _, _ = added_in_new(
            country="test",
            arlabel="تسمية",
            suf="",
            year_labe="1900",
            country_label="البلد",
            Add_In=True,
            arlabel2="1900",
        )
        assert "البلد" in arlabel
        assert "1900" in arlabel

    def test_suf_fi_added_when_country_label_starts_with_al(self) -> None:
        """Should add 'في' to suf when country_label starts with 'ال'."""
        arlabel, _, _ = added_in_new(
            country="test",
            arlabel="تسمية",
            suf="",
            year_labe="1900",
            country_label="البلد",
            Add_In=True,
            arlabel2="1900",
        )
        # suf becomes " في " when country_label starts with "ال"
        assert ARABIC_PREPOSITION_FI.strip() in arlabel

    def test_add_in_flag_changes(self) -> None:
        """Add_In flag should potentially change during processing."""
        _, Add_In, _ = added_in_new(
            country="test",
            arlabel="تسمية",
            suf="",
            year_labe="1900",
            country_label="البلد",
            Add_In=True,
            arlabel2="1900",
        )
        assert isinstance(Add_In, bool)

    def test_add_in_done_is_boolean(self) -> None:
        """Add_In_Done should be a boolean."""
        _, _, Add_In_Done = added_in_new(
            country="test",
            arlabel="تسمية",
            suf="",
            year_labe="1900",
            country_label="بلد",  # Does not start with "ال"
            Add_In=True,
            arlabel2="1900",
        )
        assert isinstance(Add_In_Done, bool)


# ---------------------------------------------------------------------------
# Tests for new_func_mk2 function
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestNewFuncMk2:
    """Tests for the new_func_mk2 function."""

    def test_basic_call_returns_tuple(self) -> None:
        """Should return a tuple with two elements."""
        result = new_func_mk2(
            category="1900 events",
            cat_test="1900 events",
            year="1900",
            typeo="",
            In="",
            country="events",
            arlabel="أحداث",
            year_labe="1900",
            suf="",
            Add_In=True,
            country_label="الأحداث",
            Add_In_Done=False,
        )
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_returns_cat_test_and_arlabel(self) -> None:
        """Should return cat_test and arlabel as strings."""
        cat_test, arlabel = new_func_mk2(
            category="1900 events",
            cat_test="1900 events",
            year="1900",
            typeo="",
            In="",
            country="events",
            arlabel="أحداث",
            year_labe="1900",
            suf="",
            Add_In=True,
            country_label="الأحداث",
            Add_In_Done=False,
        )
        assert isinstance(cat_test, str)
        assert isinstance(arlabel, str)

    def test_country_removed_from_cat_test(self) -> None:
        """Country should be removed from cat_test."""
        cat_test, _ = new_func_mk2(
            category="1900 disasters",
            cat_test="1900 disasters",
            year="1900",
            typeo="",
            In="",
            country="disasters",
            arlabel="كوارث",
            year_labe="1900",
            suf="",
            Add_In=True,
            country_label="كوارث",
            Add_In_Done=False,
        )
        assert "disasters" not in cat_test

    def test_arlabel_normalized_whitespace(self) -> None:
        """arlabel should have normalized whitespace."""
        _, arlabel = new_func_mk2(
            category="test",
            cat_test="test",
            year="1900",
            typeo="",
            In="",
            country="test",
            arlabel="  multiple   spaces  ",
            year_labe="1900",
            suf="",
            Add_In=True,
            country_label="تسمية",
            Add_In_Done=False,
        )
        assert "  " not in arlabel  # No double spaces

    def test_with_in_preposition(self) -> None:
        """Should handle 'in' preposition correctly."""
        cat_test, arlabel = new_func_mk2(
            category="1900 in yemen",
            cat_test="1900 in yemen",
            year="1900",
            typeo="",
            In=" in ",
            country="yemen",
            arlabel="1900",
            year_labe="1900",
            suf="",
            Add_In=True,
            country_label="اليمن",
            Add_In_Done=False,
        )
        assert isinstance(arlabel, str)
        assert " in " not in cat_test or cat_test.count(" in ") == 0


# ---------------------------------------------------------------------------
# Tests for constants
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestConstants:
    """Tests for module constants."""

    def test_preposition_in_constant(self) -> None:
        """PREPOSITION_IN should be 'in'."""
        assert PREPOSITION_IN == "in"

    def test_preposition_at_constant(self) -> None:
        """PREPOSITION_AT should be 'at'."""
        assert PREPOSITION_AT == "at"

    def test_arabic_preposition_fi_constant(self) -> None:
        """ARABIC_PREPOSITION_FI should contain 'في'."""
        assert "في" in ARABIC_PREPOSITION_FI

    def test_country_before_year_list_not_empty(self) -> None:
        """country_before_year should not be empty."""
        assert len(country_before_year) > 0

    def test_country_before_year_contains_known_entries(self) -> None:
        """country_before_year should contain known entries."""
        assert "disasters" in country_before_year
        assert "sports" in country_before_year
        assert "discoveries" in country_before_year
