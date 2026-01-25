"""
Tests for verifying that circular dependencies are properly resolved.

These tests verify that:
1. The lazy import mechanism works correctly
2. All modules can be imported without circular import errors
3. The interfaces module correctly provides resolver functions
"""

import pytest


class TestCircularDependencyResolution:
    """Tests for circular dependency resolution in legacy_bots.circular_dependency module."""

    def test_interfaces_module_imports_cleanly(self) -> None:
        """Test that the interfaces module can be imported without errors."""
        from ArWikiCats.legacy_bots.circular_dependency import interfaces

        assert hasattr(interfaces, "get_country_term_label_resolver")
        assert hasattr(interfaces, "get_event2_d2_resolver")

    def test_ar_lab_bot_imports_and_provides_key_functions(self) -> None:
        """Test that ar_lab_bot can be imported and provides key functions.

        This test verifies the module loads correctly and exposes the expected API.
        The actual circular dependency resolution is tested by the fact that this
        import succeeds without an ImportError.
        """
        import ArWikiCats.legacy_bots.circular_dependency.ar_lab_bot as ar_lab_bot

        # Verify key functions are available
        assert hasattr(ar_lab_bot, "find_ar_label")
        assert hasattr(ar_lab_bot, "CountryResolver")

    def test_lazy_resolver_returns_callable(self) -> None:
        """Test that lazy resolvers return callable functions."""
        from ArWikiCats.legacy_bots.circular_dependency.interfaces import (
            get_country_term_label_resolver,
            get_event2_d2_resolver,
        )

        country_resolver = get_country_term_label_resolver()
        event_resolver = get_event2_d2_resolver()

        assert callable(country_resolver)
        assert callable(event_resolver)

    def test_lazy_resolver_caches_function(self) -> None:
        """Test that lazy resolvers cache the resolved function."""
        from ArWikiCats.legacy_bots.circular_dependency.interfaces import (
            get_country_term_label_resolver,
            get_event2_d2_resolver,
        )

        # First call initializes the resolver
        resolver1 = get_country_term_label_resolver()
        # Second call should return the same cached function
        resolver2 = get_country_term_label_resolver()

        assert resolver1 is resolver2

        # Same for event resolver
        event1 = get_event2_d2_resolver()
        event2 = get_event2_d2_resolver()

        assert event1 is event2

    def test_all_circular_dependency_modules_import(self) -> None:
        """Test that all modules in the circular_dependency package import cleanly."""
        # These imports should not raise any ImportError or circular import issues
        from ArWikiCats.legacy_bots.circular_dependency import (
            ar_lab_bot,
            country_bot,
            general_resolver,
            interfaces,
            sub_general_resolver,
        )

        # Basic sanity checks that key functions exist
        assert hasattr(country_bot, "Get_country2")
        assert hasattr(country_bot, "event2_d2")
        assert hasattr(country_bot, "fetch_country_term_label")
        assert hasattr(general_resolver, "work_separator_names")
        assert hasattr(ar_lab_bot, "find_ar_label")

    def test_find_ar_label_works_with_lazy_imports(self) -> None:
        """Test that find_ar_label works correctly with the lazy import mechanism."""
        from ArWikiCats.legacy_bots.circular_dependency.ar_lab_bot import find_ar_label

        # Test with a simple category that should resolve
        result = find_ar_label(
            category="sports in Germany",
            separator=" in ",
            cate_test="sports in Germany",
        )

        # The result should be a string (even if empty, the function should work)
        assert isinstance(result, str)


@pytest.mark.fast
class TestCircularDependencyIntegration:
    """Integration tests for circular dependency resolution."""

    def test_country_resolver_uses_lazy_import(self) -> None:
        """Test that CountryResolver in ar_lab_bot uses lazy imports correctly."""
        from ArWikiCats.legacy_bots.circular_dependency.ar_lab_bot import CountryResolver

        # This call should work and internally use the lazy import
        result = CountryResolver.resolve_labels("in", "Germany", True)

        # Result should be a string
        assert isinstance(result, str)

    def test_wrap_event2_uses_lazy_import(self) -> None:
        """Test that wrap_event2 uses lazy imports correctly."""
        from ArWikiCats.legacy_bots.circular_dependency.ar_lab_bot import wrap_event2

        # This call should work and internally use the lazy import
        result = wrap_event2("sports")

        # Result should be a string
        assert isinstance(result, str)
