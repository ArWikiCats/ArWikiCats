import pytest

from ArWikiCats.format_bots.relation_mapping import translation_category_relations
from ArWikiCats.utils.match_relation_word import get_relation_word, get_relation_word_new

# ===============================================
# Test: Single relation word detection
# ===============================================

data_test2 = [
    ("Schools for-deaf in New York (state)", "for-deaf", "للصم"),
    ("Cabinets involving the Liberal Party (Norway)", "involving the", "تشمل"),
    ("Television plays directed by William Sterling (director)", "directed by", "أخرجها"),
    ("Television plays filmed in Brisbane", "filmed in", "صورت في"),
    ("Television personalities from Yorkshire", "from", "من"),
    # --- Additional logical examples ---
    ("Works published by Oxford University Press", "published by", "نشرتها"),
    ("Bridges built in 1885", "built in", "بنيت في"),
    ("Ships launched in 1910", "launched in", "أطلقت في"),
    ("Films written by John Doe", "written by", "كتبها"),
    ("Cities established in 1750", "established in", "أسست في"),
]


@pytest.mark.parametrize(
    "category, expected_key, expected_value",
    data_test2,
    ids=[x[0] for x in data_test2],
)
def test_single_relation(category: str, expected_key: str, expected_value: str) -> None:
    key, value = get_relation_word(category, translation_category_relations)
    assert key.strip() == expected_key
    assert value == expected_value


@pytest.mark.parametrize(
    "category, expected_key, expected_value",
    data_test2,
    ids=[x[0] for x in data_test2],
)
def test_single_relation_compare(category: str, expected_key: str, expected_value: str) -> None:
    key1, value1 = get_relation_word(category, translation_category_relations)
    key2, value2 = get_relation_word_new(category, translation_category_relations)
    assert key2 == key1
    assert value2 == value1


# ===============================================
# Test: Multiple relation words in the same line
# ===============================================


@pytest.mark.parametrize(
    "category, first_expected_key, first_expected_value",
    [
        # --- User examples (2 relation words) ---
        ("100 metres at the African Championships by Athletics", "by", "حسب"),
        ("100 metres at the IAAF World Youth Championships by Athletics", "by", "حسب"),
        ("100 metres at the World Para Athletics Championships", "at", ""),
        ("Documentary films about the 2011 Tōhoku earthquake and tsunami", "about", "عن"),
        ("People charged with lèse majesté in Thailand", "charged with", "أتهموا بتهمة"),
        ("People associated with former colleges of the University of London", "associated with", "مرتبطة مع"),
        ("People associated with Nazarene universities and colleges", "associated with", "مرتبطة مع"),
        # --- Extra cases with two relation keys ---
        ("Songs written by John Smith and produced in London", "written by", "كتبها"),
    ],
)
def test_multiple_relations_first_match(category: str, first_expected_key: str, first_expected_value: str) -> None:
    """Ensure that only the first matching relation word is returned."""
    key, value = get_relation_word(category, translation_category_relations)
    assert key.strip() == first_expected_key
    assert value == first_expected_value


def test_multiple_relations() -> None:
    """Ensure that only the first matching relation word is returned."""
    category = "Ships built in Germany and France launched in 1900"
    key, value = get_relation_word(category, translation_category_relations)
    assert key.strip() in ["built in", "launched in"]
    assert value in ["بنيت في", "أطلقت في"]


# ===============================================
# Test: No relation found
# ===============================================


@pytest.mark.parametrize(
    "category",
    [
        "Random topic with no relation word here",
        "Mountain ranges of-the world",
        "Unclassified biological samples",
    ],
)
def test_no_relation(category: str) -> None:
    key, value = get_relation_word(category, translation_category_relations)
    assert key == ""
    assert value == ""


# ===============================================
# Test: Relation word appears but without surrounding spaces
# Should NOT match (because the function requires ' key ' with spaces)
# ===============================================


@pytest.mark.parametrize(
    "category, wrong_rel",
    [
        ("Schools forthedeaf USA", "for-deaf"),
        ("Bridges builtin London", "built in"),
        ("Items producedby students", "produced by"),
    ],
)
def test_relation_not_matched_without_spaces(category: str, wrong_rel: str) -> None:
    key, value = get_relation_word(category, translation_category_relations)
    assert key == ""
    assert value == ""


# ===============================================
# Test: Ensure the search is sensitive to ordering of dict
# The first key in the dict that appears should win.
# ===============================================


def test_first_match_priority() -> None:
    """If both 'in' and 'involving' appear, 'involving' should match first only if it appears first in mapping."""
    cat = "Topic involving science in Europe"

    # mapping order: "involving" comes before "in"
    key, value = get_relation_word(cat, translation_category_relations)
    assert key.strip() == "involving"
    assert value == "تشمل"
