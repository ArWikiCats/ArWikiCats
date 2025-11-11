import pytest
from src.ma_lists.utils.match_sport_keys import match_sport_key, Sports_Keys_For_Jobs

# ---------------------------------------------------------------------
# 1. Realistic category samples per sport key
# ---------------------------------------------------------------------
CATEGORY_SAMPLES = {
    # --- Wheelchair variants ---
    "Category:Wheelchair automobile racing at the 2020 Paralympics": "wheelchair automobile racing",
    "Category:Wheelchair gaelic football world championships": "wheelchair gaelic football",
    "Category:Wheelchair kick boxing tournaments": "wheelchair kick boxing",
    "Category:Wheelchair sport climbing events": "wheelchair sport climbing",
    "Category:Wheelchair aquatic sports athletes": "wheelchair aquatic sports",
    "Category:Wheelchair shooting competitions": "wheelchair shooting",
    "Category:Wheelchair fifa world cup qualifiers": "wheelchair fifa world cup",
    "Category:Wheelchair fifa futsal world cup finals": "wheelchair fifa futsal world cup",
    "Category:Wheelchair beach handball at the European Games": "wheelchair beach handball",
    "Category:Wheelchair shot put at the Paralympics": "wheelchair shot put",
    "Category:Wheelchair multi-sport events": "wheelchair multi-sport",

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
    "Category:Multi-sport racing competition": "multi-sport racing",
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
def test_match_sport_key_detects_all(category: str, expected_key: str):
    """Ensure every key in Sports_Keys_For_Jobs is detectable in sample categories."""
    result = match_sport_key(category)
    assert result.lower() == expected_key.lower(), f"Mismatch for {category}"


# ---------------------------------------------------------------------
# 3. Non-sport unrelated categories
# ---------------------------------------------------------------------
@pytest.mark.parametrize("category", [
    "Category:Ancient history of Rome",
    "Category:Political systems by region",
    "Category:Musical instruments of Africa",
    "Category:Environmental laws in Canada",
    "Category:Writers from Yemen",
])
@pytest.mark.fast
def test_match_sport_key_returns_empty_for_irrelevant(category):
    """Return empty string for non-sport categories."""
    assert match_sport_key(category) == ""

# ---------------------------------------------------------------------
# 5. Case insensitivity
# ---------------------------------------------------------------------


@pytest.mark.parametrize("category", [
    "category:WHEELCHAIR AUTOMOBILE RACING",
    "Category:GAELIC FOOTBALL RACING",
    "CATEGORY:SPORT CLIMBING RACING",
    "Category:ESPORTS world finals",
])
@pytest.mark.fast
def test_case_insensitivity(category):
    """Matching should ignore capitalization."""
    assert match_sport_key(category) != ""


# ---------------------------------------------------------------------
# 6. Longest match wins
# ---------------------------------------------------------------------
@pytest.mark.parametrize("text,longest_key", [
    ("Category:Wheelchair FIFA World Cup", "wheelchair fifa world cup"),
    ("Category:FIFA Futsal World Cup racing", "fifa futsal world cup racing"),
    ("Category:Wheelchair FIFA Futsal World Cup", "wheelchair fifa futsal world cup"),
])
@pytest.mark.fast
def test_longest_match_priority(text, longest_key):
    """When overlap exists, prefer longest key."""
    res = match_sport_key(text)
    assert res.lower() == longest_key.lower()


# ---------------------------------------------------------------------
# 7. Verify all defined keys are searchable
# ---------------------------------------------------------------------
@pytest.mark.fast
def test_all_defined_keys_detectable():
    """Ensure every key in Sports_Keys_For_Jobs dictionary is matchable."""
    for key in Sports_Keys_For_Jobs:
        sample = f"Category:{key.title()} Event"
        assert match_sport_key(sample), f"Key not matched: {key}"


# ---------------------------------------------------------------------
# 8. Edge cases with punctuation or spacing
# ---------------------------------------------------------------------
@pytest.mark.parametrize("category", [
    "Category:Sport climbing, at the 2023 European Games",
    "Category:FIFA Futsal World Cup - qualifiers",
    "Category:Wheelchair Kick Boxing (Asia Championships)",
])
@pytest.mark.fast
def test_tolerates_punctuation(category):
    """Pattern should still detect keywords with punctuation nearby."""
    assert match_sport_key(category) != ""


# ---------------------------------------------------------------------
# 9. Mixed-language and noise tolerance
# ---------------------------------------------------------------------
@pytest.mark.parametrize("category", [
    "تصنيف:FIFA futsal world cup",
    "FIFA Futsal WORLD CUP - نسخة 2016",
    "بطولة Wheelchair Sport Climbing",
])
@pytest.mark.fast
def test_mixed_language_input(category):
    """Mixed Arabic-English text should not break detection."""
    assert match_sport_key(category) != ""


# ---------------------------------------------------------------------
# 10. Sanity check: no false positives on random text
# ---------------------------------------------------------------------
@pytest.mark.parametrize("category", [
    "Category:Poetry readings in Europe",
    "Category:Film directors by nationality",
    "Category:Hospitals in Yemen",
    "Category:Climate change effects",
])
@pytest.mark.fast
def test_no_false_positive(category):
    """Ensure non-related text never matches any sport key."""
    assert match_sport_key(category) == ""
