import pytest

from ArWikiCats.translations.utils.match_sport_keys import (
    SPORTS_KEYS_FOR_JOBS,
    match_sport_key,
)

# ---------------------------------------------------------------------
# 1. Realistic category samples per sport key
# ---------------------------------------------------------------------
CATEGORY_SAMPLES = {
    # --- Wheelchair variants ---
    "Category:Wheelchair beach handball at the European Games": "wheelchair beach handball",
    "Category:automobile racing at the 2020 Paralympics": "automobile racing",
    "Category:gaelic football world championships": "gaelic football",
    "Category:kick boxing tournaments": "kick boxing",
    "Category:sport climbing events": "sport climbing",
    "Category:aquatic sports athletes": "aquatic sports",
    "Category:shooting competitions": "shooting",
    "Category:fifa world cup qualifiers": "fifa world cup",
    "Category:fifa futsal world cup finals": "fifa futsal world cup",
    "Category:shot put at the Paralympics": "shot put",
    # --- Racing variants ---
    "Category:Automobile racing in Japan": "automobile racing",
    "Category:Gaelic football racing cup": "gaelic football racing",
    "Category:Kick boxing racing finals": "kick boxing racing",
    "Category:Sport climbing racing world tour": "sport climbing racing",
    "Category:Aquatic sports racing championship": "aquatic sports racing",
    "Category:Shooting racing event winners": "shooting racing",
    "Category:Motorsports racing in the UK": "motorsports racing",
    "Category:FIFA Futsal World Cup racing series": "fifa futsal world cup racing",
    "Category:FIFA World Cup racing team awards": "fifa world cup racing",
    "Category:Beach handball racing contest": "beach handball racing",
    "Category:Shot put racing in national games": "shot put racing",
    # --- Non-racing base forms ---
    "Category:Futsal players from Spain": "futsal",
    "Category:Darts competitions in 2022": "darts",
    "Category:Basketball tournaments in Asia": "basketball",
    "Category:Esports events in Europe": "esports",
    "Category:Canoeing at the Olympics": "canoeing",
    "Category:Dressage events in France": "dressage",
    "Category:Canoe sprint at the 2019 European Games": "canoe sprint",
    "Category:Gymnastics world championships": "gymnastics",
    "Category:Korfball national teams": "korfball",
}

# ---------------------------------------------------------------------
# 2. Detection by match_sport_key
# ---------------------------------------------------------------------


@pytest.mark.fast
@pytest.mark.parametrize("category,expected_key", CATEGORY_SAMPLES.items())
def test_match_sport_key_detects_all(category: str, expected_key: str) -> None:
    """Ensure every key in SPORTS_KEYS_FOR_JOBS is detectable in sample categories."""
    result = match_sport_key(category)
    assert result.lower() == expected_key.lower(), f"Mismatch for {category}"


# ---------------------------------------------------------------------
# 3. Non-sport unrelated categories
# ---------------------------------------------------------------------
@pytest.mark.parametrize(
    "category",
    [
        "Category:Ancient history of Rome",
        "Category:Political systems by region",
        "Category:Musical instruments of Africa",
        "Category:Environmental laws in Canada",
        "Category:Writers from Yemen",
    ],
)
@pytest.mark.fast
def test_match_sport_key_returns_empty_for_irrelevant(category) -> None:
    """Return empty string for non-sport categories."""
    assert match_sport_key(category) == ""


# ---------------------------------------------------------------------
# 5. Case insensitivity
# ---------------------------------------------------------------------


@pytest.mark.parametrize(
    "category",
    [
        "category:WHEELCHAIR AUTOMOBILE RACING",
        "Category:GAELIC FOOTBALL RACING",
        "CATEGORY:SPORT CLIMBING RACING",
        "Category:ESPORTS world finals",
    ],
)
@pytest.mark.fast
def test_case_insensitivity(category) -> None:
    """Matching should ignore capitalization."""
    assert match_sport_key(category) != ""


# ---------------------------------------------------------------------
# 6. Longest match wins
# ---------------------------------------------------------------------
@pytest.mark.parametrize(
    "text,longest_key",
    [
        ("FIFA shooting racing", "shooting racing"),
        ("FIFA shooting", "shooting"),
        ("Category:FIFA Futsal World Cup racing", "fifa futsal world cup racing"),
        ("Category:FIFA Futsal World Cup", "fifa futsal world cup"),
    ],
)
@pytest.mark.fast
def test_longest_match_priority(text: str, longest_key: str) -> None:
    """When overlap exists, prefer longest key."""
    res = match_sport_key(text)
    assert res.lower() == longest_key.lower()


# ---------------------------------------------------------------------
# 7. Verify all defined keys are searchable
# ---------------------------------------------------------------------
@pytest.mark.fast
def test_all_defined_keys_detectable() -> None:
    """Ensure every key in SPORTS_KEYS_FOR_JOBS dictionary is matchable."""
    for key in SPORTS_KEYS_FOR_JOBS:
        sample = f"Category:{key.title()} Event"
        assert match_sport_key(sample), f"Key not matched: {key}"


# ---------------------------------------------------------------------
# 8. Edge cases with punctuation or spacing
# ---------------------------------------------------------------------
@pytest.mark.parametrize(
    "category",
    [
        "Category:Sport climbing, at the 2023 European Games",
        "Category:FIFA Futsal World Cup - qualifiers",
        "Category:Wheelchair Kick Boxing (Asia Championships)",
    ],
)
@pytest.mark.fast
def test_tolerates_punctuation(category) -> None:
    """Pattern should still detect keywords with punctuation nearby."""
    assert match_sport_key(category) != ""


# ---------------------------------------------------------------------
# 9. Mixed-language and noise tolerance
# ---------------------------------------------------------------------
@pytest.mark.parametrize(
    "category",
    [
        "تصنيف:FIFA futsal world cup",
        "FIFA Futsal WORLD CUP - نسخة 2016",
        "بطولة Wheelchair Sport Climbing",
    ],
)
@pytest.mark.fast
def test_mixed_language_input(category) -> None:
    """Mixed Arabic-English text should not break detection."""
    assert match_sport_key(category) != ""


# ---------------------------------------------------------------------
# 10. Sanity check: no false positives on random text
# ---------------------------------------------------------------------
@pytest.mark.parametrize(
    "category",
    [
        "Category:Poetry readings in Europe",
        "Category:Film directors by nationality",
        "Category:Hospitals in Yemen",
        "Category:Climate change effects",
    ],
)
@pytest.mark.fast
def test_no_false_positive(category) -> None:
    """Ensure non-related text never matches any sport key."""
    assert match_sport_key(category) == ""
