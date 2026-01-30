# test_convert_time_to_arabic.py
import pytest

from ArWikiCats.time_formats.time_to_arabic import (
    convert_time_to_arabic,
    match_time_ar,
    match_time_en,
    match_time_en_first,
)


@pytest.mark.parametrize(
    "en_text, expected",
    [
        # --- Months ---
        ("March 1917", "مارس 1917"),
        ("August 2025", "أغسطس 2025"),
        ("December 1999", "ديسمبر 1999"),
        # --- Decades ---
        ("2020s", "عقد 2020"),
        ("1990s", "عقد 1990"),
        ("10s", "عقد 10"),
        ("10s BC", "عقد 10 ق م"),
        # --- Centuries ---
        ("19th century", "القرن 19"),
        ("2nd century BC", "القرن 2 ق م"),
        ("4th-century BCE", "القرن 4 ق م"),
        ("4th-century BC", "القرن 4 ق م"),
        ("21st century BCE", "القرن 21 ق م"),
        ("1st century", "القرن 1"),
        # --- Millennia ---
        ("2nd millennium", "الألفية 2"),
        ("1st millennium BC", "الألفية 1 ق م"),
        ("2nd millennium BC", "الألفية 2 ق م"),
        ("1st millennium BCE", "الألفية 1 ق م"),
        # --- Misc / fallback ---
        ("1000", "1000"),
        ("1234", "1234"),
        ("Late 20th century", ""),  # no pattern
        ("year 2000", ""),  # should not alter arbitrary text
    ],
)
def test_convert_time_to_arabic_basic(en_text: str, expected: str) -> None:
    """Test various English time expressions for correct Arabic conversion."""
    result = convert_time_to_arabic(en_text)
    assert result == expected, f"{en_text} → {result}, {expected=}"


@pytest.mark.parametrize(
    "en_text, expected",
    [
        # --- Numeric ranges ---
        ("2012–13", "2012–13"),
        ("2012-2013", "2012-2013"),
        ("1990–91", "1990–91"),
        ("1990-1991", "1990-1991"),
        ("1800-1899", "1800-1899"),
        ("1999-2001", "1999-2001"),
        ("1999–01", "1999–01"),
        ("1899–01", "1899–01"),
    ],
)
@pytest.mark.fast
def test_ranges(en_text: str, expected: str) -> None:
    """Test various English time expressions for correct Arabic conversion."""
    result = convert_time_to_arabic(en_text)
    assert result == expected, f"{en_text} → {result}, {expected=}"


@pytest.mark.fast
def test_trim_and_dash_normalization() -> None:
    """Ensure spaces and en dash normalization work."""
    result = convert_time_to_arabic("  March 1917 ")
    assert result == "مارس 1917"

    result = convert_time_to_arabic("2012–13")
    assert result == "2012–13"


@pytest.mark.fast
def test_nonstandard_inputs() -> None:
    """Edge cases and nonstandard input should not crash."""
    assert convert_time_to_arabic("") == ""
    assert convert_time_to_arabic("unknown") == ""
    assert convert_time_to_arabic("123abc") == ""
    assert convert_time_to_arabic("20th-century architecture") == ""


@pytest.mark.fast
def test_century_and_millennium_bc_equivalence() -> None:
    """Verify BC and BCE handled identically."""
    assert convert_time_to_arabic("2nd century BC") == convert_time_to_arabic("2nd century BCE")
    assert convert_time_to_arabic("1st millennium BC") == convert_time_to_arabic("1st millennium BCE")


@pytest.mark.fast
def test_convert_time_to_arabic_decade_bc() -> None:
    # 10s BC should be mapped to عقد 10 ق م
    assert convert_time_to_arabic("10s BC") == "عقد 10 ق م"


@pytest.mark.fast
def test_convert_time_to_arabic_decade_normal() -> None:
    # 1990s should be mapped to عقد 1990
    assert convert_time_to_arabic("1990s") == "عقد 1990"


@pytest.mark.parametrize(
    "en_text, expected",
    [
        ("march   1917", "مارس 1917"),
        (" MARCH 1917", "مارس 1917"),
        ("April    2020", "أبريل 2020"),
        ("July  0099", "يوليو 0099"),
    ],
)
@pytest.mark.fast
def test_month_variants(en_text: str, expected: str) -> None:
    assert convert_time_to_arabic(en_text) == expected


@pytest.mark.parametrize(
    "en_text, expected",
    [
        ("0010s", "عقد 0010"),
        ("0010s BC", "عقد 0010 ق م"),
        ("50s", "عقد 50"),
        ("50s BC", "عقد 50 ق م"),
        ("5s", "عقد 5"),
        ("5s BC", "عقد 5 ق م"),
        ("1990S", "عقد 1990"),  # case insensitive
        ("1990S BC", "عقد 1990 ق م"),
    ],
)
@pytest.mark.fast
def test_decade_all_variants(en_text: str, expected: str) -> None:
    assert convert_time_to_arabic(en_text) == expected


@pytest.mark.parametrize(
    "en_text, expected",
    [
        ("20th-century", "القرن 20"),
        ("20th-century BC", "القرن 20 ق م"),
        ("7th centuryBC", "القرن 7 ق م"),
        ("1st-century", "القرن 1"),
        ("1st-century BCE", "القرن 1 ق م"),
        ("25th century", "القرن 25"),  # للتأكد من أرقام كبيرة
    ],
)
@pytest.mark.fast
def test_century_extended(en_text: str, expected: str) -> None:
    assert convert_time_to_arabic(en_text) == expected


@pytest.mark.parametrize(
    "en_text, expected",
    [
        ("1st-millennium", "الألفية 1"),
        ("1st-millennium BC", "الألفية 1 ق م"),
        ("10th millennium", "الألفية 10"),
    ],
)
@pytest.mark.fast
def test_millennium_extended(en_text: str, expected: str) -> None:
    assert convert_time_to_arabic(en_text) == expected


@pytest.mark.parametrize(
    "en_text",
    [
        "1990-91",
        "1990–91",
        "1990−91",
        "1990-91",
        "1990-91",  # non-breaking hyphen
    ],
)
@pytest.mark.fast
def test_ranges_all_dash_forms(en_text) -> None:
    assert convert_time_to_arabic(en_text) == en_text


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Events in 1990s BC", ["1990s BC"]),
        ("From March 1917 to August 2020", ["March 1917", "August 2020"]),
        ("Bridges built in the 4th century BC", ["4th century BC"]),
        ("In the 1st millennium BCE", ["1st millennium BCE"]),
        ("Category:2nd millennium BCE", ["2nd millennium BCE"]),
        ("Category:1st millennium BC", ["1st millennium BC"]),
        ("Category:5th century BCE", ["5th century BCE"]),
        ("10th century bc", ["10th century bc"]),
        # Four-digit year inside parentheses
        ("Category:American Soccer League (1933)", ["1933"]),
        ("Category:American Soccer League (1933–83)", ["1933–83"]),
    ],
)
@pytest.mark.fast
def test_match_time_en(text: str, expected: list[str]) -> None:
    assert match_time_en(text) == expected
    assert match_time_en_first(text) == expected[0]


@pytest.mark.parametrize(
    "text, expected",
    [
        ("مارس 1917", ["مارس 1917"]),
        ("عقد 1990", ["عقد 1990"]),
        ("القرن 5", ["القرن 5"]),
        ("الألفية 2 ق م", ["الألفية 2 ق م"]),
    ],
)
@pytest.mark.fast
def test_match_time_ar(text: str, expected: list[str]) -> None:
    assert match_time_ar(text) == expected


@pytest.mark.parametrize(
    "text",
    [
        "not a date",
        "century-old building",
        "pre-20th century event",
        "late 1990s music",
        "about 2000 people",
        "1948–49 in european football",
    ],
)
@pytest.mark.fast
def test_fallback(text) -> None:
    assert convert_time_to_arabic(text) == ""
