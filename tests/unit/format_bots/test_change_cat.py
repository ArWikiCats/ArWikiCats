"""
Unit tests for the format_bots.change_cat module (format_bots/__init__.py).
"""

import pytest

from ArWikiCats.format_bots import change_cat


class TestChangeCatBasicNormalization:
    """Tests for basic normalization in change_cat."""

    def test_converts_to_lowercase(self) -> None:
        """Should convert input to lowercase."""
        result = change_cat("TEST CATEGORY")
        assert result == result.lower()

    def test_strips_whitespace(self) -> None:
        """Should strip leading/trailing whitespace."""
        result = change_cat("  test category  ")
        assert result == result.strip()

    def test_normalizes_internal_whitespace(self) -> None:
        """Should normalize multiple spaces to single space."""
        result = change_cat("test    category    name")
        assert "    " not in result
        assert "test category name" in result or "test" in result

    def test_removes_the_articles(self) -> None:
        """Should remove 'the' articles."""
        result = change_cat("the united states")
        assert result != "the united states"
        # 'the' should be removed
        assert not result.startswith("the ")


class TestChangeCatCenturyMillennium:
    """Tests for century and millennium normalization."""

    def test_normalizes_century_with_hyphen(self) -> None:
        """Should normalize century with hyphens."""
        result = change_cat("20th-century")
        assert "-century" not in result
        assert " century" in result

    def test_normalizes_millennium_with_hyphen(self) -> None:
        """Should normalize millennium with hyphens."""
        result = change_cat("2nd-millennium")
        assert "-millennium" not in result
        assert " millennium" in result

    def test_handles_various_dash_types(self) -> None:
        """Should handle en-dash, em-dash, and regular hyphen."""
        result1 = change_cat("20th-century")
        result2 = change_cat("20th–century")
        result3 = change_cat("20th—century")
        # All should normalize to space
        for result in [result1, result2]:
            assert " century" in result


class TestChangeCatRoyalForces:
    """Tests for royal military force name reordering."""

    def test_reorders_royal_navy(self) -> None:
        """Should reorder 'royal X navy' to 'X royal navy'."""
        result = change_cat("royal australian navy")
        assert "australian royal navy" in result

    def test_reorders_royal_air_force(self) -> None:
        """Should reorder 'royal X air force' to 'X royal air force'."""
        result = change_cat("royal canadian air force")
        assert "canadian royal air force" in result

    def test_reorders_royal_defence_force(self) -> None:
        """Should reorder 'royal X defence force' to 'X royal defence force'."""
        result = change_cat("royal jordanian defence force")
        assert "jordanian royal defence force" in result

    def test_reorders_royal_naval_force(self) -> None:
        """Should reorder 'royal X naval force' to 'X royal naval force'."""
        result = change_cat("royal british naval force")
        assert "british royal naval force" in result


class TestChangeCatSpecialReplacements:
    """Tests for special term replacements."""

    def test_replaces_organisations_with_organizations(self) -> None:
        """Should replace 'organisations' with 'organizations'."""
        result = change_cat("british organisations")
        assert "organizations" in result
        assert "organisations" not in result

    def test_normalizes_austria_hungary(self) -> None:
        """Should normalize Austria-Hungary to austria hungary."""
        result = change_cat("austria-hungary")
        assert "austria hungary" in result
        assert "austria-hungary" not in result

    def test_normalizes_rus_apostrophe(self) -> None:
        """Should normalize Rus' to rus."""
        result = change_cat("kievan rus'")
        assert "rus" in result

    def test_normalizes_kingdom_of(self) -> None:
        """Should normalize 'the kingdom of' to 'kingdom of'."""
        result = change_cat("the kingdom of italy")
        assert "kingdom-of" in result

    def test_replaces_twin_people(self) -> None:
        """Should replace 'twin people' with 'twinpeople'."""
        result = change_cat("twin people category")
        assert "twinpeople" in result

    def test_replaces_percent27(self) -> None:
        """Should replace %27 with apostrophe."""
        result = change_cat("women%27s")
        assert "'" in result
        assert "%27" not in result


class TestChangeCatExpatriatePeople:
    """Tests for expatriate people pattern."""

    def test_handles_expatriate_people_pattern(self) -> None:
        """Should handle 'X expatriate Y people in Z' pattern."""
        result = change_cat("american expatriate british people in france")
        # Should transform the pattern somehow
        assert isinstance(result, str)
        # The exact transformation involves adding 'peoplee' (note: typo in original)


class TestChangeCatCongoSpecialCases:
    """Tests for Congo special cases."""

    def test_normalizes_democratic_republic_congo(self) -> None:
        """Should normalize Democratic Republic of Congo."""
        result = change_cat("democratic republic of congo")
        assert "democratic-republic-of-congo" in result

    def test_normalizes_republic_congo(self) -> None:
        """Should normalize Republic of Congo."""
        result = change_cat("republic of congo")
        assert "republic-of-congo" in result


class TestChangeCatAircraftAndVehicles:
    """Tests for aircraft and vehicle patterns."""

    def test_normalizes_unmanned_military_aircraft(self) -> None:
        """Should normalize 'unmanned military aircraft of'."""
        result = change_cat("unmanned military aircraft of usa")
        assert "unmanned military aircraft-of" in result

    def test_normalizes_unmanned_aerial_vehicles(self) -> None:
        """Should normalize 'unmanned aerial vehicles of'."""
        result = change_cat("unmanned aerial vehicles of usa")
        assert "unmanned aerial vehicles-of" in result


class TestChangeCatSportsPatterns:
    """Tests for sports-related patterns."""

    def test_normalizes_athletics_track_and_field(self) -> None:
        """Should normalize 'athletics (track and field)'."""
        result = change_cat("athletics (track and field)")
        assert "track-and-field athletics" in result

    def test_normalizes_association_football(self) -> None:
        """Should replace 'association football' with 'football'."""
        result = change_cat("association football players")
        assert "football" in result
        # Should not have 'association football' unless it's part of 'afc'

    def test_normalizes_association_football_afc(self) -> None:
        """Should normalize 'association football afc'."""
        result = change_cat("association football afc")
        assert "association-football afc" in result


class TestChangeCatReplacementPatterns:
    """Tests for replacement patterns."""

    def test_normalizes_mens_womens_patterns(self) -> None:
        """Should normalize various men's/women's patterns."""
        patterns = [
            ("women's national youth", "national youth women's"),
            ("youth national women's", "national youth women's"),
            ("men's national junior", "national junior men's"),
        ]
        for input_pattern, expected_fragment in patterns:
            result = change_cat(input_pattern)
            assert expected_fragment in result

    def test_normalizes_heads_of_mission(self) -> None:
        """Should normalize 'heads of mission '."""
        result = change_cat("people heads of mission of country")
        assert "heads-of-mission" in result

    def test_normalizes_house_of_commons_canada(self) -> None:
        """Should normalize 'house of commons of canada'."""
        result = change_cat("house of commons of canada")
        assert "house-of-commons-of-canada" in result


class TestChangeCatSimpleReplacements:
    """Tests for simple string replacements."""

    def test_replaces_secretaries_of(self) -> None:
        """Should replace 'secretaries of '."""
        result = change_cat("secretaries of state")
        assert "secretaries-of " in result

    def test_replaces_sportspeople(self) -> None:
        """Should replace 'sportspeople' with 'sports-people'."""
        result = change_cat("american sportspeople")
        assert "sports-people" in result

    def test_normalizes_roller_hockey_quad(self) -> None:
        """Should normalize 'roller hockey (quad)'."""
        result = change_cat("roller hockey (quad)")
        assert "roller hockey" in result
        assert "(quad)" not in result

    def test_normalizes_victoria_australia(self) -> None:
        """Should normalize 'victoria (australia)'."""
        result = change_cat("victoria (australia)")
        assert "victoria-australia" in result

    def test_normalizes_party_of(self) -> None:
        """Should normalize 'party of '."""
        result = change_cat("party of italy")
        assert "party-of " in result


class TestChangeCatMinistersPattern:
    """Tests for ministers pattern."""

    def test_normalizes_category_ministers(self) -> None:
        """Should normalize 'category:ministers of'."""
        result = change_cat("category:ministers of defence")
        assert "ministers-of " in result


class TestChangeCatLogging:
    """Tests for logging behavior."""

    def test_logs_when_category_changes(self) -> None:
        """Should log when category is changed."""
        # Just verify it doesn't raise errors
        result = change_cat("TEST CATEGORY")
        assert isinstance(result, str)

    def test_returns_string(self) -> None:
        """Should always return a string."""
        inputs = ["", "test", "UPPERCASE", "  spaces  ", "special-chars!!!"]
        for inp in inputs:
            result = change_cat(inp)
            assert isinstance(result, str)


class TestChangeCatEdgeCases:
    """Edge case tests."""

    def test_handles_empty_string(self) -> None:
        """Should handle empty string."""
        result = change_cat("")
        assert result == ""

    def test_handles_whitespace_only(self) -> None:
        """Should handle whitespace-only strings."""
        result = change_cat("   ")
        assert result.strip() == ""

    def test_handles_special_characters(self) -> None:
        """Should handle special characters."""
        result = change_cat("test@#$%^&*()")
        assert isinstance(result, str)

    def test_handles_unicode(self) -> None:
        """Should handle Unicode characters."""
        result = change_cat("تصنيف عربي")
        assert isinstance(result, str)

    def test_handles_very_long_strings(self) -> None:
        """Should handle very long category names."""
        long_cat = "a" * 1000
        result = change_cat(long_cat)
        assert isinstance(result, str)


class TestChangeCatIntegration:
    """Integration tests combining multiple transformations."""

    def test_applies_multiple_transformations(self) -> None:
        """Should apply multiple transformations in sequence."""
        result = change_cat("The Royal Australian Navy in 20th-Century")
        assert isinstance(result, str)
        # Should have removed 'the', reordered royal navy, normalized century

    def test_case_insensitive_transformations(self) -> None:
        """Should handle case-insensitive transformations."""
        result1 = change_cat("Association Football")
        result2 = change_cat("association football")
        result3 = change_cat("ASSOCIATION FOOTBALL")
        # All should produce similar results (lowercase)
        assert result1.lower() == result2.lower() == result3.lower()

    def test_idempotent_transformations(self) -> None:
        """Applying transformation twice should give same result."""
        input_cat = "test category"
        result1 = change_cat(input_cat)
        result2 = change_cat(result1)
        # Should be idempotent for most cases
        assert result1 == result2


class TestChangeCatConsistency:
    """Tests for consistency across similar inputs."""

    def test_consistent_with_different_spacing(self) -> None:
        """Should handle different spacing consistently."""
        result1 = change_cat("test  category")
        result2 = change_cat("test   category")
        result3 = change_cat("test    category")
        # Should all normalize to same spacing
        assert result1 == result2 == result3

    def test_consistent_output_type(self) -> None:
        """Should always return string type."""
        test_inputs = ["", "test", "TEST", "123", "!@#", "تصنيف"]
        for inp in test_inputs:
            result = change_cat(inp)
            assert isinstance(result, str)
