"""
Unit tests for country_resolver module.
"""

import pytest

from ArWikiCats.legacy_bots.resolvers.country_resolver import (
    CountryLabelRetriever,
    Get_country2,
    _get_fallback_label,
    _validate_separators,
    check_historical_prefixes,
    event2_d2,
    fetch_country_term_label,
    get_country_label,
    set_fallback_resolver,
)


# ---------------------------------------------------------------------------
# Tests for set_fallback_resolver and _get_fallback_label
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestFallbackResolver:
    """Tests for fallback resolver functions."""

    def test_get_fallback_label_without_resolver_returns_empty(self) -> None:
        """Should return empty string when no fallback resolver is set."""
        # Save current state
        from ArWikiCats.legacy_bots.resolvers import country_resolver

        original = country_resolver._fallback_resolver

        # Test with None
        country_resolver._fallback_resolver = None
        result = _get_fallback_label("test")
        assert result == ""

        # Restore
        country_resolver._fallback_resolver = original

    def test_set_fallback_resolver_sets_callback(self) -> None:
        """Should set the fallback resolver callback."""
        from ArWikiCats.legacy_bots.resolvers import country_resolver

        original = country_resolver._fallback_resolver

        # Set a test resolver
        def test_resolver(category: str) -> str:
            return f"resolved_{category}"

        set_fallback_resolver(test_resolver)
        result = _get_fallback_label("test")
        assert result == "resolved_test"

        # Restore
        country_resolver._fallback_resolver = original


# ---------------------------------------------------------------------------
# Tests for _validate_separators
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestValidateSeparators:
    """Tests for the _validate_separators function."""

    def test_returns_true_for_no_separators(self) -> None:
        """Should return True when no separators are present."""
        assert _validate_separators("simple text") is True

    def test_returns_false_for_in_separator(self) -> None:
        """Should return False when 'in' separator is present."""
        assert _validate_separators("events in yemen") is False

    def test_returns_false_for_of_separator(self) -> None:
        """Should return False when 'of' separator is present."""
        assert _validate_separators("history of yemen") is False

    def test_returns_false_for_from_separator(self) -> None:
        """Should return False when 'from' separator is present."""
        assert _validate_separators("people from yemen") is False

    def test_returns_false_for_by_separator(self) -> None:
        """Should return False when 'by' separator is present."""
        assert _validate_separators("songs by artist") is False

    def test_returns_true_for_separator_at_start(self) -> None:
        """Separator at start (not surrounded by spaces) should not match."""
        # "in yemen" - 'in' is at start, not surrounded by spaces on both sides
        assert _validate_separators("inyemen") is True

    def test_returns_false_for_at_separator(self) -> None:
        """Should return False when 'at' separator is present."""
        assert _validate_separators("events at location") is False


# ---------------------------------------------------------------------------
# Tests for check_historical_prefixes
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestCheckHistoricalPrefixes:
    """Tests for the check_historical_prefixes function."""

    def test_returns_empty_for_no_prefix(self) -> None:
        """Should return empty when no historical prefix is found."""
        result = check_historical_prefixes("random text")
        assert result == ""

    def test_returns_empty_with_separators(self) -> None:
        """Should return empty when input contains separators."""
        result = check_historical_prefixes("defunct national teams in yemen")
        assert result == ""

    def test_handles_defunct_national_prefix(self) -> None:
        """Should handle 'defunct national' prefix."""
        # Will depend on whether remainder can be resolved
        result = check_historical_prefixes("defunct national something")
        assert isinstance(result, str)


# ---------------------------------------------------------------------------
# Tests for Get_country2
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestGetCountry2:
    """Tests for the Get_country2 function."""

    def test_returns_string(self) -> None:
        """Should return a string."""
        result = Get_country2("test")
        assert isinstance(result, str)

    def test_normalizes_input(self) -> None:
        """Should normalize input to lowercase and strip whitespace."""
        result1 = Get_country2("TEST")
        result2 = Get_country2("test")
        assert result1 == result2

    def test_handles_empty_input(self) -> None:
        """Should handle empty input."""
        result = Get_country2("")
        assert isinstance(result, str)


# ---------------------------------------------------------------------------
# Tests for CountryLabelRetriever class
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestCountryLabelRetriever:
    """Tests for the CountryLabelRetriever class."""

    def test_init_creates_instance(self) -> None:
        """Should create an instance."""
        retriever = CountryLabelRetriever()
        assert retriever is not None

    def test_get_country_label_returns_string(self) -> None:
        """get_country_label should return a string."""
        retriever = CountryLabelRetriever()
        result = retriever.get_country_label("test")
        assert isinstance(result, str)

    def test_check_basic_lookups_returns_digits(self) -> None:
        """_check_basic_lookups should return digits unchanged."""
        retriever = CountryLabelRetriever()
        result = retriever._check_basic_lookups("12345")
        assert result == "12345"

    def test_check_basic_lookups_returns_string(self) -> None:
        """_check_basic_lookups should return a string."""
        retriever = CountryLabelRetriever()
        result = retriever._check_basic_lookups("test")
        assert isinstance(result, str)

    def test_fetch_country_term_label_returns_string(self) -> None:
        """fetch_country_term_label should return a string."""
        retriever = CountryLabelRetriever()
        result = retriever.fetch_country_term_label("test", "in")
        assert isinstance(result, str)

    def test_fetch_country_term_label_handles_numeric(self) -> None:
        """fetch_country_term_label should return numeric input unchanged."""
        retriever = CountryLabelRetriever()
        result = retriever.fetch_country_term_label("12345", "")
        assert result == "12345"

    def test_fetch_country_term_label_handles_the_prefix(self) -> None:
        """fetch_country_term_label should handle 'the ' prefix."""
        retriever = CountryLabelRetriever()
        result = retriever.fetch_country_term_label("the test", "")
        assert isinstance(result, str)

    def test_handle_type_lab_logic_returns_string(self) -> None:
        """_handle_type_lab_logic should return a string."""
        retriever = CountryLabelRetriever()
        result = retriever._handle_type_lab_logic("test of", "in")
        assert isinstance(result, str)

    def test_handle_type_lab_logic_handles_of_suffix(self) -> None:
        """_handle_type_lab_logic should handle ' of' suffix."""
        retriever = CountryLabelRetriever()
        result = retriever._handle_type_lab_logic("history of", "")
        assert isinstance(result, str)

    def test_handle_type_lab_logic_handles_in_suffix(self) -> None:
        """_handle_type_lab_logic should handle ' in' suffix."""
        retriever = CountryLabelRetriever()
        result = retriever._handle_type_lab_logic("events in", "")
        assert isinstance(result, str)


# ---------------------------------------------------------------------------
# Tests for event2_d2 function
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestEvent2D2:
    """Tests for the event2_d2 function."""

    def test_returns_string(self) -> None:
        """Should return a string."""
        result = event2_d2("test")
        assert isinstance(result, str)

    def test_returns_empty_for_blocked_words(self) -> None:
        """Should return empty for strings with blocked words."""
        assert event2_d2("events in yemen") == ""
        assert event2_d2("history of yemen") == ""
        assert event2_d2("people from yemen") == ""

    def test_strips_category_prefix(self) -> None:
        """Should strip 'category:' prefix."""
        result1 = event2_d2("category:test")
        result2 = event2_d2("test")
        assert result1 == result2


# ---------------------------------------------------------------------------
# Tests for module-level wrapper functions
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestModuleFunctions:
    """Tests for module-level wrapper functions."""

    def test_get_country_label_returns_string(self) -> None:
        """get_country_label should return a string."""
        result = get_country_label("test")
        assert isinstance(result, str)

    def test_fetch_country_term_label_returns_string(self) -> None:
        """fetch_country_term_label should return a string."""
        result = fetch_country_term_label("test", "in")
        assert isinstance(result, str)

    def test_fetch_country_term_label_with_lab_type(self) -> None:
        """fetch_country_term_label should handle lab_type parameter."""
        result = fetch_country_term_label("test", "in", lab_type="type_label")
        assert isinstance(result, str)
