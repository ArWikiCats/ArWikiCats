"""
Integration tests for model_data.py module.

This module provides integration tests for FormatData class which handles
single-placeholder template-driven category translations.
"""

import pytest

from ArWikiCats.translations_formats.DataModel.model_data import FormatData


class TestFormatDataIntegration:
    """Integration tests for FormatData class."""

    @pytest.fixture
    def sport_bot(self):
        """Create a FormatData instance for sport-related categories."""
        formatted_data = {
            "{sport} players": "لاعبو {sport_label}",
            "{sport} coaches": "مدربو {sport_label}",
            "{sport} teams": "فرق {sport_label}",
            "{sport} championships": "بطولات {sport_label}",
        }
        data_list = {
            "football": "كرة القدم",
            "basketball": "كرة السلة",
            "volleyball": "كرة الطائرة",
            "tennis": "التنس",
        }
        return FormatData(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )

    def test_search_football_players(self, sport_bot):
        """Test searching for football players."""
        result = sport_bot.search("football players")
        assert result == "لاعبو كرة القدم"

    def test_search_basketball_coaches(self, sport_bot):
        """Test searching for basketball coaches."""
        result = sport_bot.search("basketball coaches")
        assert result == "مدربو كرة السلة"

    def test_search_volleyball_teams(self, sport_bot):
        """Test searching for volleyball teams."""
        result = sport_bot.search("volleyball teams")
        assert result == "فرق كرة الطائرة"

    def test_search_tennis_championships(self, sport_bot):
        """Test searching for tennis championships."""
        result = sport_bot.search("tennis championships")
        assert result == "بطولات التنس"

    def test_search_no_match(self, sport_bot):
        """Test search returns empty string when no match."""
        result = sport_bot.search("unknown sport")
        assert result == ""

    def test_search_case_insensitive(self, sport_bot):
        """Test that search is case-insensitive."""
        result = sport_bot.search("FOOTBALL PLAYERS")
        assert result == "لاعبو كرة القدم"

    def test_search_all_with_category_prefix(self, sport_bot):
        """Test search_all with Category: prefix - note: search_all doesn't strip prefix."""
        # search_all doesn't strip the Category: prefix, so it won't match directly
        # Use search_all_category for category prefix handling instead
        result = sport_bot.search_all("football players", add_arabic_category_prefix=False)
        assert result == "لاعبو كرة القدم"

    def test_search_all_category_full_flow(self, sport_bot):
        """Test search_all_category full normalization flow."""
        result = sport_bot.search_all_category("Category:basketball coaches")
        assert result == "تصنيف:مدربو كرة السلة"


class TestFormatDataWithTextBeforeAfter:
    """Integration tests for FormatData with text_before and text_after."""

    @pytest.fixture
    def country_bot(self):
        """Create a FormatData instance with text_before and text_after."""
        formatted_data = {
            "{country} people": "شعب {country_label}",
            "{country} cities": "مدن {country_label}",
        }
        data_list = {
            "united states": "الولايات المتحدة",
            "yemen": "اليمن",
            "france": "فرنسا",
        }
        return FormatData(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{country}",
            value_placeholder="{country_label}",
            text_before="the ",
        )

    def test_search_with_text_before(self, country_bot):
        """Test search handles text_before correctly."""
        result = country_bot.search("the yemen people")
        assert result == "شعب اليمن"

    def test_search_without_text_before(self, country_bot):
        """Test search works without the text_before prefix."""
        result = country_bot.search("yemen people")
        assert result == "شعب اليمن"


class TestFormatDataMatchAndNormalize:
    """Integration tests for FormatData match and normalize methods."""

    @pytest.fixture
    def bot(self):
        """Create a FormatData instance for testing."""
        formatted_data = {"{lang} speakers": "متحدثون {lang_label}"}
        data_list = {"arabic": "العربية", "english": "الإنجليزية"}
        return FormatData(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{lang}",
            value_placeholder="{lang_label}",
        )

    def test_match_key_basic(self, bot):
        """Test match_key returns matched key."""
        result = bot.match_key("arabic speakers")
        assert result == "arabic"

    def test_match_key_case_insensitive(self, bot):
        """Test match_key is case-insensitive."""
        result = bot.match_key("ARABIC speakers")
        assert result == "arabic"

    def test_normalize_category(self, bot):
        """Test normalize_category replaces key with placeholder."""
        result = bot.normalize_category("arabic speakers", "arabic")
        assert result == "{lang} speakers"

    def test_normalize_category_with_key(self, bot):
        """Test normalize_category_with_key returns both key and normalized."""
        key, normalized = bot.normalize_category_with_key("english speakers")
        assert key == "english"
        assert normalized == "{lang} speakers"


class TestFormatDataEdgeCases:
    """Integration tests for FormatData edge cases."""

    def test_empty_data_list(self):
        """Test behavior with empty data_list."""
        bot = FormatData(
            formatted_data={"{sport} players": "لاعبو {sport_label}"},
            data_list={},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.search("football players")
        assert result == ""

    def test_empty_formatted_data(self):
        """Test behavior with empty formatted_data."""
        bot = FormatData(
            formatted_data={},
            data_list={"football": "كرة القدم"},
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.search("football players")
        assert result == ""

    def test_multiple_matches_uses_first(self):
        """Test that with overlapping patterns, longer matches are preferred."""
        formatted_data = {"{sport} players": "لاعبو {sport_label}"}
        data_list = {
            "american football": "كرة قدم أمريكية",
            "football": "كرة القدم",
        }
        bot = FormatData(
            formatted_data=formatted_data,
            data_list=data_list,
            key_placeholder="{sport}",
            value_placeholder="{sport_label}",
        )
        result = bot.search("american football players")
        assert result == "لاعبو كرة قدم أمريكية"
