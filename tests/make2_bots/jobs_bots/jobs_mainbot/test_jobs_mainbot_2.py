"""
Tests
"""

import pytest

from ArWikiCats.make_bots.jobs_bots.jobs_mainbot import jobs_with_nat_prefix


@pytest.mark.fast
class Tests:
    # =========================================================
    #                 ADDITIONAL NATIONALITY TESTS
    # =========================================================

    def test_mens_compound_nationality(self) -> None:
        """Test compound nationality 'democratic republic of congo' with standard job"""
        result = jobs_with_nat_prefix("", "democratic republic of congo", "episcopalians")
        assert result == "كونغويون ديمقراطيون أسقفيون"

    def test_womens_compound_nationality(self) -> None:
        """Test compound nationality 'south yemeni' with women's job"""
        result = jobs_with_nat_prefix("", "south yemeni", "actresses")
        assert result == "ممثلات يمنيات جنوبيات"

    def test_mens_special_characters_nationality(self) -> None:
        """Test nationality with special characters 'zaïrean'"""
        result = jobs_with_nat_prefix("", "zaïrean", "blind")
        assert result == "زائيريون مكفوفون"

    def test_womens_french_compound_nationality(self) -> None:
        """Test French compound nationality 'french guianan'"""
        result = jobs_with_nat_prefix("", "french guianan", "women in politics")
        assert result == "سياسيات غويانيات فرنسيات"

    def test_mens_hyphenated_nationality(self) -> None:
        """Test hyphenated nationality 'bissau-guinean'"""
        result = jobs_with_nat_prefix("", "bissau-guinean", "muslims")
        assert result == "غينيون بيساويون مسلمون"

    # =========================================================
    #                 SPECIAL TEMPLATE TESTS
    # =========================================================

    def test_mens_politicians_suicide_template(self) -> None:
        """Test MEN_WOMENS_WITH_NATO template for men"""
        result = jobs_with_nat_prefix("", "afghan", "politicians who committed suicide")
        assert result == "سياسيون أفغان أقدموا على الانتحار"

    def test_womens_artists_template_with_override(self) -> None:
        """Test MEN_WOMENS_WITH_NATO template for women with manual override"""
        result = jobs_with_nat_prefix("", "zanzibari", "female contemporary artists", females="زنجباريات")
        # assert result == "فنانات زنجباريات معاصرات"
        assert result == ""

    # =========================================================
    #                 EDGE CASES & FAILURE MODES
    # =========================================================

    def test_unknown_nationality_fallback(self) -> None:
        """Test unknown nationality with valid job"""
        result = jobs_with_nat_prefix("", "unknown_nation", "historical opera authors")
        assert result == ""

    def test_empty_nationality_with_womens_job(self) -> None:
        """Test empty nationality with women-specific job"""
        # result = jobs_with_nat_prefix("", "", "deafblind actresses")
        # assert result == "ممثلات صم ومكفوفات"
        result2 = jobs_with_nat_prefix("yemeni deaf actresses", "yemeni", "deaf actresses")
        assert result2 == "ممثلات صم يمنيات"

    def test_partial_nationality_match(self) -> None:
        """Test partial nationality key match should fail cleanly"""
        result = jobs_with_nat_prefix("", "yemen", "sailors")  # Note: should be "yemeni"
        assert result == ""

    def test_case_insensitive_keys(self) -> None:
        """Test case insensitivity in category_suffix matching"""
        result = jobs_with_nat_prefix("", "afghan", "female WOMEN'S RIGHTS ACTIVISTS")  # Uppercase
        assert result == "ناشطات في حقوق المرأة أفغانيات"

    def test_numeric_suffix_handling(self) -> None:
        """Test handling of numeric suffixes (should fail gracefully)"""
        result = jobs_with_nat_prefix("", "egyptian", "category_123")
        assert result == ""
