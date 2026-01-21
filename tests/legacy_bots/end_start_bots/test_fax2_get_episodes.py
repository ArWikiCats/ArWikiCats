"""
Tests
"""

import pytest

from ArWikiCats.legacy_bots.end_start_bots.fax2_episodes import get_episodes

data = [
    ("2016 American television episodes", "2016 American television", "حلقات {}"),
    ("Game of Thrones (season 1) episodes", "Game of Thrones", "حلقات {} الموسم 1"),
    ("Game of Thrones season 2 episodes", "Game of Thrones", "حلقات {} الموسم 2"),
    ("", "", "حلقات {}"),
]

# --- 1. Basic known test cases ---


@pytest.mark.parametrize(
    "text, expected_cat, expected_label",
    data,
    ids=[x[0] for x in data],
)
@pytest.mark.fast
def test_basic_cases(text: str, expected_cat: str, expected_label: str) -> None:
    list_of_cat, category3 = get_episodes(text)
    assert list_of_cat == expected_label
    assert category3 == expected_cat


# --- 2. Test all seasons (1 – 10) for both key patterns ---
@pytest.mark.fast
@pytest.mark.parametrize("i", range(1, 11))
def test_all_seasons_parentheses(i) -> None:
    text = f"My Show (season {i}) episodes"
    list_of_cat, category3 = get_episodes(text)
    assert list_of_cat == f"حلقات {{}} الموسم {i}"
    assert category3 == "My Show"


@pytest.mark.fast
@pytest.mark.parametrize("i", range(1, 11))
def test_all_seasons_no_parentheses(i) -> None:
    text = f"My Show season {i} episodes"
    list_of_cat, category3 = get_episodes(text)
    assert list_of_cat == f"حلقات {{}} الموسم {i}"
    assert category3 == "My Show"


# --- 3. Case-insensitive handling ---
@pytest.mark.fast
def test_case_insensitive() -> None:
    text = "My Show Season 3 Episodes"
    list_of_cat, category3 = get_episodes(text)
    assert list_of_cat == "حلقات {} الموسم 3"
    assert category3 == "My Show"


# --- 4. Ensure extra spaces trimmed properly ---
@pytest.mark.fast
def test_trailing_spaces() -> None:
    text = "My Show season 4 episodes    "
    list_of_cat, category3 = get_episodes(text)
    assert category3 == "My Show"


# --- 5. When `category3_nolower` is provided ---
@pytest.mark.fast
def test_override_category3_nolower() -> None:
    text = "abc season 5 episodes"
    nolower = "XYZ season 5 episodes"
    list_of_cat, category3 = get_episodes(text, nolower)
    assert list_of_cat == "حلقات {} الموسم 5"
    assert category3 == "XYZ"  # must follow nolower


# --- 6. Default fallback when no season pattern is matched ---
@pytest.mark.fast
def test_fallback_no_season() -> None:
    text = "Random episodes"
    list_of_cat, category3 = get_episodes(text)
    assert list_of_cat == "حلقات {}"
    assert category3 == "Random"


# --- 7. Ensure only end is removed, not middle ---
@pytest.mark.fast
def test_does_not_trim_middle_text() -> None:
    text = "Show episodes special"
    list_of_cat, category3 = get_episodes(text)
    assert list_of_cat == "حلقات {}"
    assert category3 == "Show episodes special"  # no trimming because does NOT end with episodes


# --- 8. Ensure correct slicing removal of 'episodes' ---
@pytest.mark.fast
def test_exact_slice_removal() -> None:
    text = "My Series episodes"
    list_of_cat, category3 = get_episodes(text)
    assert category3 == "My Series"


# --- 9. Protect against strings shorter than 'episodes' ---
@pytest.mark.fast
def test_short_string() -> None:
    text = "episodes"
    list_of_cat, category3 = get_episodes(text)
    assert category3 == ""


# --- 10. Weird inputs / robustness ---
@pytest.mark.fast
@pytest.mark.parametrize("text", ["   episodes", "EPISODES", " Episodes"])
def test_weird_inputs(text) -> None:
    list_of_cat, category3 = get_episodes(text)
    assert list_of_cat == "حلقات {}"
    assert isinstance(category3, str)
