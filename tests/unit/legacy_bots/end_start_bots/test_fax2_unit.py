# test_fax2_get_list_of_and_cat3.py
import pytest

from ArWikiCats.legacy_bots.end_start_bots import fax2

# ---------------------------------------------------------------------------
# 1) Patterns handled by to_get_startswith عبر get_from_starts_dict
# ---------------------------------------------------------------------------


@pytest.mark.fast
def test_get_list_of_and_cat3_all_startswith_patterns() -> None:
    """Each key in to_get_startswith should be matched and produce expected label."""
    for key, tab in fax2.to_get_startswith.items():
        # Build a synthetic category that starts with the key
        suffix = "TestTarget"
        category3 = f"{key}{suffix}"
        category3_nolower = category3

        list_of_cat, foot_ballers, rest = fax2.get_list_of_and_cat3(category3, category3_nolower)

        assert list_of_cat == tab["lab"]
        assert foot_ballers is False
        assert rest == suffix  # Remainder after removing prefix


# ---------------------------------------------------------------------------
# 2) women members of ... (fallback بعد startswith)
# ---------------------------------------------------------------------------


@pytest.mark.fast
def test_get_list_of_and_cat3_women_members_fallback() -> None:
    """The 'women members of ' fallback should be applied when no startswith pattern matches."""
    category3 = "women members of Parliament of the United Kingdom"
    category3_nolower = category3

    list_of_cat, foot_ballers, rest = fax2.get_list_of_and_cat3(category3, category3_nolower)

    assert list_of_cat == "عضوات {}"
    assert foot_ballers is False
    assert rest == "Parliament of the United Kingdom"


# ---------------------------------------------------------------------------
# 3) footballers branches + footballers_get_endswith
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "category3, expected_label, expected_rest",
    [
        (
            "Spanish women's footballers",
            "لاعبات {}",
            "Spanish",
        ),
        (
            "Brazilian female footballers",
            "لاعبات {}",
            "Brazilian",
        ),
        (
            "Heartland F.C. footballers",
            "لاعبو {}",
            "Heartland F.C.",
        ),
        (
            "German footballers",
            "لاعبو {}",
            "German",
        ),
    ],
)
@pytest.mark.fast
def test_get_list_of_and_cat3_footballers_variants(category3: str, expected_label: str, expected_rest: str) -> None:
    """All footballers variants should be handled via footballers_get_endswith."""
    category3_nolower = category3

    list_of_cat, foot_ballers, rest = fax2.get_list_of_and_cat3(category3, category3_nolower)

    assert list_of_cat == expected_label
    assert foot_ballers is True
    assert rest == expected_rest


# ---------------------------------------------------------------------------
# 4) players / players branches
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "category3, category3_nolower, expected_rest",
    [
        # Simple players
        (
            "Spanish handball players",
            "Spanish handball players",
            "Spanish handball",
        ),
        # Simple players
        (
            "Spanish handball players",
            "Spanish handball players",
            "Spanish handball",
        ),
        # c. players
        (
            "Heartland F.C. players",
            "Heartland F.C. players",
            "Heartland F.C.",
        ),
        # c. players
        (
            "Heartland F.C. players",
            "Heartland F.C. players",
            "Heartland F.C.",
        ),
        # category3_nolower empty: should fall back to category3
        (
            "Italian basketball players",
            "",
            "Italian basketball",
        ),
    ],
)
@pytest.mark.fast
def test_get_list_of_and_cat3_players_variants(category3: str, category3_nolower: str, expected_rest: str) -> None:
    """All 'players' / 'players' endings should set label and strip suffix correctly."""
    list_of_cat, foot_ballers, rest = fax2.get_list_of_and_cat3(category3, category3_nolower)

    assert list_of_cat == "لاعبو {}"
    assert foot_ballers is False
    assert rest == expected_rest


# ---------------------------------------------------------------------------
# 6) Patterns handled by to_get_endswith عبر get_from_endswith_dict
# ---------------------------------------------------------------------------


@pytest.mark.fast
def test_get_list_of_and_cat3_all_endswith_patterns() -> None:
    """Each key in to_get_endswith should be matched and produce expected label."""
    for key, tab in fax2.to_get_endswith.items():
        if tab.get("example"):
            example = tab["example"]
            # Remove 'Category:' prefix if present to mimic typical category3 usage
            if ":" in example:
                category_body = example.split(":", 1)[1]
            else:
                category_body = example
            category3 = category_body
        else:
            # Generic synthetic category
            category3 = f"Foo {key}"

        category3_nolower = category3

        list_of_cat, foot_ballers, rest = fax2.get_list_of_and_cat3(category3, category3_nolower)

        assert list_of_cat == tab["lab"]
        assert foot_ballers is False

        # Check the stripped remainder where we control the format
        if not tab.get("example"):
            assert rest.strip() == "Foo"
        else:
            # For examples we at least ensure remainder + key reconstructs body
            # and is non-empty.
            assert category3.endswith(key)
            expected_rest = category3[: -len(key)]
            assert rest.strip() == expected_rest.strip()


@pytest.mark.fast
def test_get_list_of_and_cat3_navigational_boxes_specificity() -> None:
    """More specific 'squad/sports navigational boxes' should win over plain 'navigational boxes'."""
    # sports navigational boxes
    category3 = "Yemen sports navigational boxes"
    list_of_cat, foot_ballers, rest = fax2.get_list_of_and_cat3(category3, category3)
    assert list_of_cat == fax2.to_get_endswith["sports navigational boxes"]["lab"]
    assert rest.strip() == "Yemen"

    # squad navigational boxes
    category3 = "1996 Basketball Olympic squad navigational boxes"
    list_of_cat, foot_ballers, rest = fax2.get_list_of_and_cat3(category3, category3)
    assert list_of_cat == fax2.to_get_endswith["squad navigational boxes"]["lab"]
    assert rest.strip() == "1996 Basketball Olympic"


# ---------------------------------------------------------------------------
# 7) لا يوجد أي تطابق مع أي نمط
# ---------------------------------------------------------------------------


@pytest.mark.fast
def test_get_list_of_and_cat3_no_match_returns_defaults() -> None:
    """If no startswith/footballers/players/endswith patterns match, @pytest.mark.fast
    defaults should be returned."""
    category3 = "Completely unmatched category"
    category3_nolower = category3

    list_of_cat, foot_ballers, rest = fax2.get_list_of_and_cat3(category3, category3_nolower)

    assert list_of_cat == ""
    assert foot_ballers is False
    # Leading/trailing whitespace is stripped only
    assert rest == "Completely unmatched category"


# ---------------------------------------------------------------------------
# 8) التأكد من إزالة الفراغات والتعامل مع category3_nolower الفارغ
# ---------------------------------------------------------------------------


@pytest.mark.fast
def test_get_list_of_and_cat3_strips_whitespace_and_handles_empty_nolower() -> None:
    """Whitespace should be stripped and empty category3_nolower handled gracefully."""
    category3 = "  Spanish players  "
    category3_nolower = ""

    list_of_cat, foot_ballers, rest = fax2.get_list_of_and_cat3(category3, category3_nolower)

    assert list_of_cat == "لاعبو {}"
    assert foot_ballers is False
    # Whitespace stripped from both ends
    assert rest == "Spanish"
