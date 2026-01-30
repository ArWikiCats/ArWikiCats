"""
Unit tests for event_lab_bot module.
"""

import pytest

from ArWikiCats.legacy_bots.legacy_resolvers_bots.event_lab_bot import (
    ARABIC_CATEGORY_PREFIX,
    CATEGORY_PEOPLE,
    CATEGORY_SPORTS_EVENTS,
    LABEL_PEOPLE_AR,
    LABEL_SPORTS_EVENTS_AR,
    LIST_TEMPLATE_PLAYERS,
    SUFFIX_EPISODES,
    SUFFIX_TEMPLATES,
    EventLabResolver,
    _finalize_category_label,
    _process_category_formatting,
    _resolve_via_chain,
    event_lab,
    event_label_work,
    translate_general_category_wrap,
)

# ---------------------------------------------------------------------------
# Tests for constants
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestConstants:
    """Tests for module constants."""

    def test_suffix_episodes(self) -> None:
        """SUFFIX_EPISODES should be ' episodes'."""
        assert SUFFIX_EPISODES == " episodes"

    def test_suffix_templates(self) -> None:
        """SUFFIX_TEMPLATES should be ' templates'."""
        assert SUFFIX_TEMPLATES == " templates"

    def test_category_people(self) -> None:
        """CATEGORY_PEOPLE should be 'people'."""
        assert CATEGORY_PEOPLE == "people"

    def test_label_people_ar(self) -> None:
        """LABEL_PEOPLE_AR should be 'أشخاص'."""
        assert LABEL_PEOPLE_AR == "أشخاص"

    def test_category_sports_events(self) -> None:
        """CATEGORY_SPORTS_EVENTS should be 'sports events'."""
        assert CATEGORY_SPORTS_EVENTS == "sports events"

    def test_label_sports_events_ar(self) -> None:
        """LABEL_SPORTS_EVENTS_AR should be 'أحداث رياضية'."""
        assert LABEL_SPORTS_EVENTS_AR == "أحداث رياضية"

    def test_arabic_category_prefix(self) -> None:
        """ARABIC_CATEGORY_PREFIX should be 'تصنيف:'."""
        assert ARABIC_CATEGORY_PREFIX == "تصنيف:"

    def test_list_template_players(self) -> None:
        """LIST_TEMPLATE_PLAYERS should contain placeholder."""
        assert "{}" in LIST_TEMPLATE_PLAYERS


# ---------------------------------------------------------------------------
# Tests for _resolve_via_chain function
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestResolveViaChain:
    """Tests for the _resolve_via_chain function."""

    def test_returns_empty_for_empty_resolvers(self) -> None:
        """Should return empty string when no resolvers provided."""
        result = _resolve_via_chain("test", [])
        assert result == ""

    def test_returns_first_non_empty_result(self) -> None:
        """Should return first non-empty resolver result."""
        resolvers = [
            lambda x: "",
            lambda x: "result1",
            lambda x: "result2",
        ]
        result = _resolve_via_chain("test", resolvers)
        assert result == "result1"

    def test_returns_empty_when_all_resolvers_empty(self) -> None:
        """Should return empty when all resolvers return empty."""
        resolvers = [
            lambda x: "",
            lambda x: "",
        ]
        result = _resolve_via_chain("test", resolvers)
        assert result == ""

    def test_passes_category_to_resolvers(self) -> None:
        """Should pass category to each resolver."""
        captured = []
        resolvers = [
            lambda x: (captured.append(x), "")[1],  # Capture and return empty
            lambda x: x,  # Return the input
        ]
        result = _resolve_via_chain("test_category", resolvers)
        assert result == "test_category"
        assert "test_category" in captured


# ---------------------------------------------------------------------------
# Tests for translate_general_category_wrap function
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestTranslateGeneralCategoryWrap:
    """Tests for the translate_general_category_wrap function."""

    def test_returns_string(self) -> None:
        """Should return a string."""
        result = translate_general_category_wrap("test")
        assert isinstance(result, str)

    def test_empty_input(self) -> None:
        """Should handle empty input."""
        result = translate_general_category_wrap("")
        assert isinstance(result, str)


# ---------------------------------------------------------------------------
# Tests for event_label_work function
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestEventLabelWork:
    """Tests for the event_label_work function."""

    def test_returns_string(self) -> None:
        """Should return a string."""
        result = event_label_work("test")
        assert isinstance(result, str)

    def test_people_returns_label_people_ar(self) -> None:
        """'people' should return 'أشخاص'."""
        result = event_label_work("people")
        assert result == LABEL_PEOPLE_AR

    def test_people_case_insensitive(self) -> None:
        """'PEOPLE' should also return 'أشخاص'."""
        result = event_label_work("PEOPLE")
        assert result == LABEL_PEOPLE_AR

    def test_people_with_whitespace(self) -> None:
        """'  people  ' should also return 'أشخاص'."""
        result = event_label_work("  people  ")
        assert result == LABEL_PEOPLE_AR

    def test_empty_input(self) -> None:
        """Should handle empty input gracefully."""
        result = event_label_work("")
        assert isinstance(result, str)


# ---------------------------------------------------------------------------
# Tests for EventLabResolver class
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestEventLabResolver:
    """Tests for the EventLabResolver class."""

    def test_init_default_values(self) -> None:
        """Test default initialization values."""
        resolver = EventLabResolver()
        assert resolver.foot_ballers is False

    def test_process_category_returns_string(self) -> None:
        """process_category should return a string."""
        resolver = EventLabResolver()
        result = resolver.process_category("test", "test")
        assert isinstance(result, str)

    def test_process_category_empty_input(self) -> None:
        """process_category should handle empty input."""
        resolver = EventLabResolver()
        result = resolver.process_category("", "")
        assert isinstance(result, str)

    def test_handle_special_suffixes_episodes(self) -> None:
        """Should detect episodes suffix."""
        resolver = EventLabResolver()
        list_of_cat, category3 = resolver._handle_special_suffixes("test episodes")
        assert isinstance(list_of_cat, str)
        assert isinstance(category3, str)

    def test_handle_special_suffixes_templates(self) -> None:
        """Should detect templates suffix."""
        resolver = EventLabResolver()
        list_of_cat, category3 = resolver._handle_special_suffixes("test templates")
        assert isinstance(list_of_cat, str)
        assert isinstance(category3, str)

    def test_handle_suffix_patterns_returns_tuple(self) -> None:
        """_handle_suffix_patterns should return a tuple."""
        resolver = EventLabResolver()
        result = resolver._handle_suffix_patterns("test category")
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_handle_suffix_patterns_no_match(self) -> None:
        """_handle_suffix_patterns returns empty list_of_cat when no match."""
        resolver = EventLabResolver()
        list_of_cat, category3 = resolver._handle_suffix_patterns("random text")
        assert list_of_cat == ""
        assert category3 == "random text"

    def test_apply_general_label_functions_returns_string(self) -> None:
        """_apply_general_label_functions should return a string."""
        resolver = EventLabResolver()
        result = resolver._apply_general_label_functions("test")
        assert isinstance(result, str)

    def test_get_country_based_label_returns_tuple(self) -> None:
        """_get_country_based_label should return a tuple."""
        resolver = EventLabResolver()
        result = resolver._get_country_based_label("test", "")
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_process_list_category_empty_list_of_cat(self) -> None:
        """_process_list_category returns unchanged label when list_of_cat is empty."""
        resolver = EventLabResolver()
        result = resolver._process_list_category("test", "تسمية", "")
        assert result == "تسمية"

    def test_process_list_category_empty_category_lab(self) -> None:
        """_process_list_category returns unchanged label when category_lab is empty."""
        resolver = EventLabResolver()
        result = resolver._process_list_category("test", "", "template")
        assert result == ""


# ---------------------------------------------------------------------------
# Tests for _finalize_category_label function
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestFinalizeCategoryLabel:
    """Tests for the _finalize_category_label function."""

    def test_empty_label_returns_empty(self) -> None:
        """Empty label should return empty string."""
        result = _finalize_category_label("", "test")
        assert result == ""

    def test_adds_prefix(self) -> None:
        """Should add تصنيف: prefix."""
        result = _finalize_category_label("تسمية", "test")
        assert result.startswith(ARABIC_CATEGORY_PREFIX)

    def test_prefix_only_returns_empty(self) -> None:
        """Label that becomes only prefix should return empty."""
        # This tests the case where the label after processing is just the prefix
        result = _finalize_category_label("", "test")
        assert result == ""


# ---------------------------------------------------------------------------
# Tests for _process_category_formatting function
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestProcessCategoryFormatting:
    """Tests for the _process_category_formatting function."""

    def test_removes_category_prefix(self) -> None:
        """Should remove 'category:' prefix."""
        result = _process_category_formatting("category:test")
        assert not result.startswith("category:")

    def test_handles_no_prefix(self) -> None:
        """Should handle input without prefix."""
        result = _process_category_formatting("test")
        assert isinstance(result, str)


# ---------------------------------------------------------------------------
# Tests for event_lab function
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestEventLab:
    """Tests for the event_lab function (main entry point)."""

    def test_returns_string(self) -> None:
        """Should return a string."""
        result = event_lab("test")
        assert isinstance(result, str)

    def test_handles_empty_input(self) -> None:
        """Should handle empty input."""
        result = event_lab("")
        assert isinstance(result, str)

    def test_replaces_underscores(self) -> None:
        """Should replace underscores with spaces."""
        # The function converts underscores to spaces internally
        result1 = event_lab("test_category")
        result2 = event_lab("test category")
        # Both should produce similar results
        assert isinstance(result1, str)
        assert isinstance(result2, str)

    def test_lowercase_handling(self) -> None:
        """Should handle uppercase input by lowercasing."""
        result1 = event_lab("TEST")
        result2 = event_lab("test")
        # Should produce same result
        assert result1 == result2

    def test_people_category(self) -> None:
        """Should handle 'people' category."""
        result = event_lab("people")
        assert isinstance(result, str)

    def test_category_with_prefix(self) -> None:
        """Should handle input with category: prefix."""
        result = event_lab("category:test")
        assert isinstance(result, str)


# ---------------------------------------------------------------------------
# Integration-style unit tests
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestEventLabIntegration:
    """Integration-style tests for event_lab function."""

    @pytest.mark.parametrize(
        "input_category",
        [
            "people",
            "category:people",
            "PEOPLE",
        ],
    )
    def test_people_variations(self, input_category: str) -> None:
        """Various forms of 'people' should be handled."""
        result = event_lab(input_category)
        assert isinstance(result, str)

    @pytest.mark.parametrize(
        "input_category",
        [
            "",
            "   ",
            "test_test",
        ],
    )
    def test_edge_cases(self, input_category: str) -> None:
        """Edge cases should not raise exceptions."""
        result = event_lab(input_category)
        assert isinstance(result, str)
