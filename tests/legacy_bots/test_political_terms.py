"""
Tests
"""

import pytest

from ArWikiCats.legacy_bots.legacy_resolvers_bots.with_years_bot import handle_political_terms


@pytest.mark.parametrize(
    "text,expected",
    [
        ("100th united states congress", "الكونغرس الأمريكي المئة"),
        ("200th united states congress", "الكونغرس الأمريكي المائتين"),
        ("300th united states congress", "الكونغرس الأمريكي الثلاثمائة"),
        ("45th united states congress", "الكونغرس الأمريكي الخامس والأربعون"),
        ("1st iranian majlis", "المجلس الإيراني الأول"),
    ],
)
@pytest.mark.fast
def test_political_terms_mapped_ordinals(text: str, expected: str) -> None:
    result = handle_political_terms(text)
    assert result == expected


@pytest.mark.fast
def test_political_terms_non_matching_returns_empty() -> None:
    # Does not match the political bodies regex, so whole function should return ""
    assert handle_political_terms("5th something else") == ""
