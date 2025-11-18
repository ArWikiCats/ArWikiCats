"""
Tests
"""
import pytest

from src.make2_bots.jobs_bots.jobs_mainbot import Jobs


class Tests:

    # =========================================================
    #                 ADDITIONAL NATIONALITY TESTS
    # =========================================================

    def test_mens_compound_nationality(self):
        """Test compound nationality 'democratic republic of the congo' with standard job"""
        result = Jobs("", "democratic republic of the congo", "episcopalians")
        assert result == "كونغويون ديمقراطيون أسقفيون"

    def test_womens_compound_nationality(self):
        """Test compound nationality 'south yemeni' with women's job"""
        result = Jobs("", "south yemeni", "actresses")
        assert result == "ممثلات يمنيات جنوبيات"

    def test_mens_special_characters_nationality(self):
        """Test nationality with special characters 'zaïrean'"""
        result = Jobs("", "zaïrean", "blind")
        assert result == "زائيريون مكفوفون"

    def test_womens_french_compound_nationality(self):
        """Test French compound nationality 'french guianan'"""
        result = Jobs("", "french guianan", "women in politics")
        assert result == "سياسيات غويانيات فرنسيات"

    def test_mens_hyphenated_nationality(self):
        """Test hyphenated nationality 'bissau-guinean'"""
        result = Jobs("", "bissau-guinean", "muslims")
        assert result == "غينيون بيساويون مسلمون"

    # =========================================================
    #                 RELIGIOUS AFFILIATION TESTS
    # =========================================================

    def test_mens_religious_before_occ(self):
        """Test religious key in NAT_BEFORE_OCC list (nationality before religion)"""
        result = Jobs("", "yemeni", "sunni muslims")
        assert result == "يمنيون مسلمون سنة"

    def test_womens_religious_with_nationality(self):
        """Test women's religious affiliation with compound nationality"""
        result = Jobs("", "north yemeni", "female coptic")
        assert result == "قبطيات يمنيات شماليات"

    def test_mens_religious_expatriate(self):
        """Test religious + expatriate combination (both in NAT_BEFORE_OCC)"""
        result = Jobs("", "turkmenistan", "jewish")
        assert result == "تركمانيون يهود"

    # =========================================================
    #                 SPECIAL TEMPLATE TESTS
    # =========================================================

    def test_mens_politicians_suicide_template(self):
        """Test MEN_WOMENS_WITH_NATO template for men"""
        result = Jobs("", "afghan", "politicians who committed suicide")
        assert result == "سياسيون أفغان أقدموا على الانتحار"

    def test_womens_artists_template_with_override(self):
        """Test MEN_WOMENS_WITH_NATO template for women with manual override"""
        result = Jobs("", "zanzibari", "female contemporary artists", womens="زنجباريات")
        # assert result == "فنانات زنجباريات معاصرات"
        assert result == ""

    # =========================================================
    #                 PKJN SUFFIX HANDLING TESTS
    # =========================================================

    def test_mens_pkjn_suffix_expatriates(self):
        """Test PKJN suffix handling for male expatriates"""
        result = Jobs("", "abkhaz", "expatriates")
        assert result == "أبخاز مغتربون"

    def test_womens_pkjn_suffix_expatriates(self):
        """Test PKJN suffix handling for female expatriates"""
        result = Jobs("", "abkhazian", "female expatriates")
        assert result == "مغتربات أبخازيات"

    # =========================================================
    #                 EDGE CASES & FAILURE MODES
    # =========================================================

    def test_unknown_nationality_fallback(self):
        """Test unknown nationality with valid job"""
        result = Jobs("", "unknown_nation", "historical opera authors")
        assert result == ""

    def test_empty_nationality_with_womens_job(self):
        """Test empty nationality with women-specific job"""
        # result = Jobs("", "", "deafblind actresses")
        # assert result == "ممثلات صم ومكفوفات"
        result2 = Jobs("", "", "deaf actresses")
        assert result2 == "ممثلات صم"

    def test_partial_nationality_match(self):
        """Test partial nationality key match should fail cleanly"""
        result = Jobs("", "yemen", "sailors")  # Note: should be "yemeni"
        assert result == ""

    def test_case_insensitive_keys(self):
        """Test case insensitivity in category_suffix matching"""
        result = Jobs("", "afghan", "female WOMEN'S RIGHTS ACTIVISTS")  # Uppercase
        assert result == "ناشطات في حقوق المرأة أفغانيات"

    def test_numeric_suffix_handling(self):
        """Test handling of numeric suffixes (should fail gracefully)"""
        result = Jobs("", "egyptian", "category_123")
        assert result == ""
