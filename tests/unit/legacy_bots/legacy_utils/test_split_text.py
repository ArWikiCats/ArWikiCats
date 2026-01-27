""" """

import pytest

from ArWikiCats.legacy_bots.legacy_utils import (
    split_text_by_separator,
)


@pytest.mark.fast
def test_split_text_by_separator_unit() -> None:
    # Test with basic inputs
    result = split_text_by_separator("in", "test in country")
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], str)

    # Test with different separator
    result_various = split_text_by_separator("from", "test from country")
    assert isinstance(result_various, tuple)
    assert len(result_various) == 2
    assert isinstance(result_various[0], str)
    assert isinstance(result_various[1], str)

    # Test with another valid separator
    result_other = split_text_by_separator("to", "test to country")
    assert isinstance(result_other, tuple)
    assert len(result_other) == 2
    assert isinstance(result_other[0], str)
    assert isinstance(result_other[1], str)


class TestSplitTextBySeparatorBasic:
    @pytest.mark.parametrize(
        "separator,country,expected",
        [
            # based in
            (" based in ", "Companies based in Yemen", ("companies", "yemen")),
            # in
            (" in ", "Works in France", ("works", "france")),
            # about
            (" about ", "Books about Yemen", ("books", "yemen")),
            # to
            (" to ", "Flights to Yemen", ("flights", "yemen")),
            # from
            (" from ", "Immigrants from Yemen", ("immigrants", "yemen")),
            # at
            (" at ", "Conference at Sana'a", ("conference", "sana'a")),
            # on
            (" on ", "Report on Yemen", ("report", "yemen")),
        ],
    )
    def test_single_separator_standard_cases(self, separator, country, expected):
        """
        Basic sanity checks for a single occurrence of each standard separator.
        """
        part_1, part_2 = split_text_by_separator(separator, country)
        assert (part_1, part_2) == expected


class TestSplitTextBySeparatorByKeyword:
    @pytest.mark.parametrize(
        "separator,country,expected",
        [
            # Single "by"
            (" by ", "Books by Yemeni authors", ("books", "by yemeni authors")),
            # Capitalization in original text
            (" by ", "BOOKS by Yemeni Authors", ("books", "by yemeni authors")),
        ],
    )
    def test_by_special_handling_single(self, separator, country, expected):
        """
        The 'by' separator must keep 'by' inside the second part.
        """
        part_1, part_2 = split_text_by_separator(separator, country)
        assert (part_1, part_2) == expected

    @pytest.mark.parametrize(
        "separator,country,expected",
        [
            # Repeated "by" – should move to using Type_t / country_t (original case)
            (
                " by ",
                "Books by Yemeni authors by local publishers",
                ("Books", "by Yemeni authors by local publishers"),
            ),
            # Trailing "by" (still should keep everything after first 'by' together)
            (
                " by ",
                "Books by Yemeni authors by",
                ("books", "by yemeni authors by"),
            ),
        ],
    )
    def test_by_special_handling_repeated(self, separator, country, expected):
        """
        When 'by' appears multiple times, the function must collapse everything
        from the first 'by' into the second part while preserving original case
        when test_N is non-trivial.
        """
        part_1, part_2 = split_text_by_separator(separator, country)
        assert (part_1, part_2) == expected


class TestSplitTextBySeparatorRepeatedSeparators:
    @pytest.mark.parametrize(
        "separator,country,expected",
        [
            # based in repeated
            (
                " based in ",
                "Companies based in Yemen based in Sana'a",
                ("Companies", "Yemen based in Sana'a"),
            ),
            # in repeated
            (
                " in ",
                "Works in France in 2015",
                ("Works", "France in 2015"),
            ),
            # about repeated
            (
                " about ",
                "Books about Yemen and about its history",
                ("Books", "Yemen and about its history"),
            ),
            # to repeated
            (
                " to ",
                "Flights to Yemen to Sana'a",
                ("Flights", "Yemen to Sana'a"),
            ),
            # from repeated
            (
                " from ",
                "Immigrants from Yemen from Taiz",
                ("Immigrants", "Yemen from Taiz"),
            ),
            # at repeated
            (
                " at ",
                "Conference at Sana'a at University",
                ("Conference", "Sana'a at University"),
            ),
            # on repeated
            (
                " on ",
                "Report on Yemen on TV",
                ("Report", "Yemen on TV"),
            ),
        ],
    )
    def test_repeated_separator_complex_cases(self, separator, country, expected):
        """
        When the separator appears more than once, split_text_by_separator
        should return:
        - First logical part before the first separator (with original casing)
        - Everything after the first separator (including any extra separators)
        """
        part_1, part_2 = split_text_by_separator(separator, country)
        assert (part_1, part_2) == expected


class TestSplitTextBySeparatorEdgeCases:
    def test_case_insensitive_matching(self):
        """
        Ensure the function behaves correctly when the original string
        has mixed / upper-case characters, while the separator is lower-case.
        """
        separator = " in "
        country = "Works IN France"
        part_1, part_2 = split_text_by_separator(separator, country)
        # Function normalizes to lowercase for the split, so the result is lowercased
        assert (part_1, part_2) == ("works", "france")

    @pytest.mark.parametrize(
        "separator,country,expected",
        [
            # Separator near the end
            (" in ", "Works in France in", ("works", "france in")),
            # Separator at the start (non-typical but good to guard)
            (" in ", "in France in Germany", ("in france", "germany")),
            # Double separators back-to-back
            (" in ", "Works in in France", ("works", "in france")),
        ],
    )
    def test_weird_positioning_of_separator(self, separator, country, expected):
        """
        Stress tests around strange placements of the separator. These ensure that
        the combination of split() + regex + test_N logic remains stable.
        """
        part_1, part_2 = split_text_by_separator(separator, country)
        assert (part_1, part_2) == expected
