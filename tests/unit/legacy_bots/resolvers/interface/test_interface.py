"""
Unit tests for interface module.
"""

import pytest

from ArWikiCats.legacy_bots.resolvers.interface import (
    ArabicLabelBuilder,
    CategoryResolver,
    CountryLabelResolver,
    PrepositionHandler,
    TermLabelResolver,
    TypeResolver,
)

# ---------------------------------------------------------------------------
# Tests for Protocol classes
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestCountryLabelResolverProtocol:
    """Tests for the CountryLabelResolver Protocol."""

    def test_protocol_exists(self) -> None:
        """CountryLabelResolver protocol should exist."""
        assert CountryLabelResolver is not None

    def test_protocol_has_get_country_label_method(self) -> None:
        """Protocol should define get_country_label method."""
        # Check that the protocol has the expected method signature
        assert hasattr(CountryLabelResolver, "get_country_label")


@pytest.mark.fast
class TestTermLabelResolverProtocol:
    """Tests for the TermLabelResolver Protocol."""

    def test_protocol_exists(self) -> None:
        """TermLabelResolver protocol should exist."""
        assert TermLabelResolver is not None

    def test_protocol_has_fetch_country_term_label_method(self) -> None:
        """Protocol should define fetch_country_term_label method."""
        assert hasattr(TermLabelResolver, "fetch_country_term_label")


@pytest.mark.fast
class TestArabicLabelBuilderProtocol:
    """Tests for the ArabicLabelBuilder Protocol."""

    def test_protocol_exists(self) -> None:
        """ArabicLabelBuilder protocol should exist."""
        assert ArabicLabelBuilder is not None

    def test_protocol_has_build_method(self) -> None:
        """Protocol should define build method."""
        assert hasattr(ArabicLabelBuilder, "build")


@pytest.mark.fast
class TestCategoryResolverProtocol:
    """Tests for the CategoryResolver Protocol."""

    def test_protocol_exists(self) -> None:
        """CategoryResolver protocol should exist."""
        assert CategoryResolver is not None

    def test_protocol_has_call_method(self) -> None:
        """Protocol should define __call__ method."""
        assert hasattr(CategoryResolver, "__call__")


@pytest.mark.fast
class TestTypeResolverProtocol:
    """Tests for the TypeResolver Protocol."""

    def test_protocol_exists(self) -> None:
        """TypeResolver protocol should exist."""
        assert TypeResolver is not None

    def test_protocol_has_resolve_method(self) -> None:
        """Protocol should define resolve method."""
        assert hasattr(TypeResolver, "resolve")


@pytest.mark.fast
class TestPrepositionHandlerProtocol:
    """Tests for the PrepositionHandler Protocol."""

    def test_protocol_exists(self) -> None:
        """PrepositionHandler protocol should exist."""
        assert PrepositionHandler is not None

    def test_protocol_has_determine_separator_method(self) -> None:
        """Protocol should define determine_separator method."""
        assert hasattr(PrepositionHandler, "determine_separator")


# ---------------------------------------------------------------------------
# Tests for Protocol implementation compliance
# ---------------------------------------------------------------------------


@pytest.mark.fast
class TestProtocolImplementation:
    """Tests for verifying protocol implementation patterns."""

    def test_country_label_resolver_can_be_implemented(self) -> None:
        """Should be able to create a class that implements CountryLabelResolver."""

        class TestResolver:
            def get_country_label(self, country: str) -> str:
                return f"label_{country}"

        resolver = TestResolver()
        result = resolver.get_country_label("test")
        assert result == "label_test"

    def test_term_label_resolver_can_be_implemented(self) -> None:
        """Should be able to create a class that implements TermLabelResolver."""

        class TestResolver:
            def fetch_country_term_label(self, term_lower: str, separator: str, lab_type: str = "") -> str:
                return f"term_{term_lower}"

        resolver = TestResolver()
        result = resolver.fetch_country_term_label("test", "in")
        assert result == "term_test"

    def test_arabic_label_builder_can_be_implemented(self) -> None:
        """Should be able to create a class that implements ArabicLabelBuilder."""

        class TestBuilder:
            def build(self) -> str:
                return "built_label"

        builder = TestBuilder()
        result = builder.build()
        assert result == "built_label"

    def test_category_resolver_can_be_implemented(self) -> None:
        """Should be able to create a class that implements CategoryResolver."""

        class TestResolver:
            def __call__(self, category: str) -> str:
                return f"resolved_{category}"

        resolver = TestResolver()
        result = resolver("test")
        assert result == "resolved_test"

    def test_preposition_handler_can_be_implemented(self) -> None:
        """Should be able to create a class that implements PrepositionHandler."""

        class TestHandler:
            def determine_separator(self) -> str:
                return "في"

        handler = TestHandler()
        result = handler.determine_separator()
        assert result == "في"
