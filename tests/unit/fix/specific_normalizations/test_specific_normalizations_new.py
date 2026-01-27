import pytest

from ArWikiCats.fix.specific_normalizations import (
    apply_category_specific_normalizations,
    fix_formula,
)


class TestFixFormula:
    """Test the fix_formula function."""

    def test_formula_1_year_pattern(self) -> None:
        """Test that Formula 1 year pattern is correctly normalized."""
        ar_label = "فورمولا 1 2020"
        en_label = "Formula 1 2020"
        result = fix_formula(ar_label, en_label)
        assert result == "فورمولا 1 في سنة 2020"

    def test_formula_1_year_pattern_with_extra_spaces(self) -> None:
        """Test Formula 1 pattern with extra spaces."""
        ar_label = "فورمولا 1   2019"
        en_label = "Formula 1 2019"
        result = fix_formula(ar_label, en_label)
        assert result == "فورمولا 1 في سنة 2019"

    @pytest.mark.parametrize(
        "ar_label,expected",
        [
            ("فورمولا 1 1995", "فورمولا 1 في سنة 1995"),
            ("فورمولا 1 2005", "فورمولا 1 في سنة 2005"),
            ("فورمولا 1 1999", "فورمولا 1 في سنة 1999"),
            ("فورمولا 1 2010", "فورمولا 1 في سنة 2010"),
        ],
    )
    def test_formula_1_with_different_years(self, ar_label: str, expected: str) -> None:
        """Test Formula 1 with different years."""
        en_label = f"Formula 1 {ar_label.split()[-1]}"
        result = fix_formula(ar_label, en_label)
        assert result == expected

    def test_no_formula_1_pattern(self) -> None:
        """Test that non-Formula 1 labels are unchanged."""
        ar_label = "رياضة السيارات"
        en_label = "Auto racing"
        result = fix_formula(ar_label, en_label)
        assert result == "رياضة السيارات"

    def test_invalid_years_not_matched(self) -> None:
        """Test that invalid years are not matched."""
        ar_label = "فورمولا 1 99"  # Should not match as it's not 4 digits starting with 1 or 2
        en_label = "Formula 1 99"
        result = fix_formula(ar_label, en_label)
        assert result == "فورمولا 1 99"


class TestApplyCategorySpecificNormalizations:
    """Test the apply_category_specific_normalizations function."""

    @pytest.mark.parametrize(
        "ar_label,expected",
        [
            ("أفلام بواسطة مخرجين", "أفلام مخرجين"),
            ("أعمال بواسطة فنانين", "أعمال فنانين"),
            ("اختراعات بواسطة علماء", "اختراعات علماء"),
            ("لوحات بواسطة رسامين", "لوحات رسامين"),
            ("شعر بواسطة شعراء", "شعر شعراء"),
            ("مسرحيات بواسطة كتاب", "مسرحيات كتاب"),
            ("روايات بواسطة مؤلفين", "روايات مؤلفين"),
            ("كتب بواسطة مؤلفين", "كتب مؤلفين"),
        ],
    )
    def test_fix_bys_replacements(self, ar_label: str, expected: str) -> None:
        """Test removal of 'بواسطة' after certain words."""
        result = apply_category_specific_normalizations(ar_label, "")
        assert result == expected

    @pytest.mark.parametrize(
        "ar_label,expected",
        [
            ("وفيات بواسطة ضربات القلب", "وفيات بضربات القلب"),
            ("ضربات جوية نفذت بواسطة الطائرات", "ضربات جوية نفذتها الطائرات"),
            ("أفلام أنتجت بواسطة شركات", "أفلام أنتجها شركات"),
        ],
    )
    def test_specific_bys_replacements(self, ar_label: str, expected: str) -> None:
        """Test specific 'بواسطة' replacements."""
        result = apply_category_specific_normalizations(ar_label, "")
        assert result == expected

    @pytest.mark.parametrize(
        "ar_label,expected",
        [
            ("كاميرات اخترعت في القرن 20", "كاميرات عرضت في القرن 20"),
            ("هواتف محمولة اخترعت حديثا", "هواتف محمولة عرضت حديثا"),
            ("مركبات اخترعت مستقبلا", "مركبات عرضت مستقبلا"),
            ("منتجات اخترعت الآن", "منتجات عرضت الآن"),
        ],
    )
    def test_invention_replacements(self, ar_label: str, expected: str) -> None:
        """Test replacement of 'اخترعت' with 'عرضت'."""
        result = apply_category_specific_normalizations(ar_label, "")
        assert result == expected

    def test_short_stories_normalization(self) -> None:
        """Test short stories with year normalization."""
        ar_label = "قصص قصيرة 1613"
        en_label = "Short stories 1613"
        result = apply_category_specific_normalizations(ar_label, en_label)
        assert result == "قصص قصيرة كتبت سنة 1613"

    @pytest.mark.parametrize(
        "ar_label,expected",
        [
            ("ردود فعل إلى الأحداث", "ردود فعل على الأحداث"),
            ("مدراء كرة القدم", "مدربو كرة القدم"),
            ("هولوكوستية الأحداث", "الهولوكوست الأحداث"),
            ("في هولوكوست", "في الهولوكوست"),
            ("صدور عظام في الدولة العثمانية", "صدور عظام عثمانيون في"),
            ("أعمال بواسطة الفنان", "أعمال الفنان"),
            ("في فائزون الأولمبي", "فائزون الأولمبي"),
            ("في منافسون السباق", "منافسون السباق"),
            ("على السجل الوطني للأماكن", "في السجل الوطني للأماكن"),
            ("من قبل البلد", "حسب البلد"),
            ("حكم عليهم الموت", "حكم عليهم بالإعدام"),
            ("محررون من منشورات علمية", "محررو منشورات علمية"),
            ("محررات من منشورات أدبية", "محررات منشورات أدبية"),
            ("قديسون صوفيون في الإسلام", "أولياء صوفيون في الإسلام"),
            ("مدربو رياضية مختلفة", "مدربو رياضة مختلفة"),
        ],
    )
    def test_general_replacements(self, ar_label: str, expected: str) -> None:
        """Test general text replacements."""
        result = apply_category_specific_normalizations(ar_label, "")
        assert result == expected

    @pytest.mark.parametrize(
        "ar_label,expected",
        [
            ("من من المنزل", "من المنزل"),
            ("حسب حسب البلد", "حسب البلد"),
            ("حسب بواسطة الحكومة", "بواسطة الحكومة"),
            ("في في المدرسة", "في المدرسة"),
            ("في من الكتاب", "من الكتاب"),
            ("من في الحديقة", "في الحديقة"),
        ],
    )
    def test_duplicate_words_removal(self, ar_label: str, expected: str) -> None:
        """Test removal of duplicate prepositions."""
        result = apply_category_specific_normalizations(ar_label, "")
        assert result == expected

    @pytest.mark.parametrize(
        "ar_label,expected",
        [
            ("العسكري القرن 20", "العسكري في القرن 20"),
            ("ق.م الساعة", "ق م الساعة"),
            ("أحداث رياضية الرياضية", "أحداث رياضية"),
            ("من القرن 19", "في القرن 19"),
            ("من حروب العالم", "في حروب العالم"),
            ("من الحروب النابليونية", "في الحروب النابليونية"),
            ("من حرب الخليج", "في حرب الخليج"),
            ("من الحرب العالمية", "في الحرب العالمية"),
            ("من الثورة الفرنسية", "في الثورة الفرنسية"),
            ("مغتربون الولايات المتحدة", "مغتربون من الولايات المتحدة"),
            ("سفراء إلى فرنسا", "سفراء لدى فرنسا"),
            ("أشخاص أصل عربي", "أشخاص من أصل عربي"),
        ],
    )
    def test_specific_phrase_replacements(self, ar_label: str, expected: str) -> None:
        """Test specific phrase replacements."""
        result = apply_category_specific_normalizations(ar_label, "")
        assert result == expected

    @pytest.mark.parametrize(
        "ar_label,expected",
        [
            ("مسلسلات بدأ عرضها حسب السنة", "مسلسلات حسب سنة بدء العرض"),
            ("أفلام أنتهت حسب السنة", "أفلام حسب سنة انتهاء العرض"),
        ],
    )
    def test_tv_show_year_normalizations(self, ar_label: str, expected: str) -> None:
        """Test TV show year normalization patterns."""
        result = apply_category_specific_normalizations(ar_label, "")
        assert result == expected

    def test_sports_phrase_replacement(self) -> None:
        """Test sports phrase replacement."""
        ar_label = "لاعبون في رياضة في كرة القدم"
        en_label = "Players in sports in football"
        result = apply_category_specific_normalizations(ar_label, en_label)
        assert result == "لاعبون في الرياضة في كرة القدم"

    def test_attacks_on_condition(self) -> None:
        """Test attacks on replacement based on English label."""
        ar_label = "هجمات في المدنيين"
        en_label = "attacks on civilians"
        result = apply_category_specific_normalizations(ar_label, en_label)
        assert result == "هجمات على المدنيين"

    def test_attacks_on_condition_negative(self) -> None:
        """Test that attacks replacement only happens when English contains 'attacks on'."""
        ar_label = "هجمات في المدنيين"
        en_label = "attacks against civilians"
        result = apply_category_specific_normalizations(ar_label, en_label)
        assert result == "هجمات في المدنيين"  # Should remain unchanged

    def test_integration_with_fix_formula(self) -> None:
        """Test that fix_formula is properly integrated."""
        ar_label = "فورمولا 1 2020 وبعض النصوص الأخرى"
        en_label = "Formula 1 2020 and other texts"
        result = apply_category_specific_normalizations(ar_label, en_label)
        assert result == "فورمولا 1 في سنة 2020 وبعض النصوص الأخرى"

    def test_multiple_replacements_chain(self) -> None:
        """Test that multiple replacements can be applied in sequence."""
        ar_label = "أفلام بواسطة مخرجين من قبل البلد"
        en_label = "Films by directors by country"
        result = apply_category_specific_normalizations(ar_label, en_label)
        assert result == "أفلام مخرجين حسب البلد"

    def test_edge_cases(self) -> None:
        """Test edge cases and boundary conditions."""
        # Empty string
        result = apply_category_specific_normalizations("", "")
        assert result == ""

        # String with only whitespace
        result = apply_category_specific_normalizations("   ", "")
        assert result == "   "

        # String with mixed Arabic and Latin
        result = apply_category_specific_normalizations("أفلام بواسطة directors", "")
        assert result == "أفلام directors"
