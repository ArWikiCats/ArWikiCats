"""
Tests
"""

import pytest

from ArWikiCats.make_bots.jobs_bots.jobs_mainbot import (
    MEN_WOMENS_WITH_NATO,
    Nat_mens,
    jobs_with_nat_prefix,
)
from ArWikiCats.translations import NAT_BEFORE_OCC, RELIGIOUS_KEYS_PP

# =========================================================
#   NEW TESTS – NAT_BEFORE_OCC VIA RELIGIOUS_KEYS_PP EXTENSION
# =========================================================


def test_men_womens_with_nato_matches_source_template() -> None:
    """NATO-labelled entries should retain the placeholder for substitution."""

    assert MEN_WOMENS_WITH_NATO
    for labels in MEN_WOMENS_WITH_NATO.values():
        assert "{nato}" in labels["mens"]
        assert "{nato}" in labels["womens"]


@pytest.mark.parametrize("suffix, forms", RELIGIOUS_KEYS_PP.items())
@pytest.mark.dict
def test_religious_keys_use_nat_and_religious_forms(suffix: str, forms: dict) -> None:
    """
    NAT_BEFORE_OCC was extended with RELIGIOUS_KEYS_PP keys.
    For each religious key, jobs_with_nat_prefix should return a non-empty label that contains:
      - the men's nationality
      - the religious Arabic label from RELIGIOUS_KEYS_PP
    """
    mens_nat = Nat_mens.get("yemeni") or "يمني"

    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "yemeni", suffix)

    error_msg = f"suffix {suffix}, forms: {forms=}"

    # If jobs_with_nat_prefix or priffix_Mens_work does not support a given key, this will fail
    # and show exactly which religious key is missing.

    assert result != "", error_msg
    assert mens_nat in result, error_msg
    assert forms["mens"] in result, error_msg


@pytest.mark.parametrize("suffix", NAT_BEFORE_OCC)
@pytest.mark.dict
def test_NAT_BEFORE_OCC(suffix: str) -> None:
    """ """
    mens_nat = Nat_mens.get("yemeni") or "يمني"

    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "yemeni", suffix)

    assert result != "", f"suffix {suffix}"
    assert mens_nat in result, f"suffix {suffix}"


# --- NAT_BEFORE_OCC Expansion Tests ---


def test_nat_before_occ_deafblind_mens_algerian() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "algerian", "deafblind writers")  # "deafblind" is in NAT_BEFORE_OCC
    assert result == "كتاب صم ومكفوفون جزائريون"  # Assuming priffix_Mens_work would return "كتاب صم ومكفوفون"


def test_nat_before_occ_religious_muslim_mens_afghan() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "afghan", "muslim")
    assert result == "أفغان مسلمون"


def test_nat_before_occ_religious_christian_womens_albanian() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "albanian", "female christian")
    assert result == "مسيحيات ألبانيات"

    result2 = jobs_with_nat_prefix("", "albanian", "christian")
    assert result2 == "ألبان مسيحيون"


def test_nat_before_occ_religious_jews_mens_argentine() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "argentine", "jews")
    assert result == "أرجنتينيون يهود"


def test_nat_before_occ_religious_jews_womens_argentinean() -> None:
    jobs_with_nat_prefix.cache_clear()
    result = jobs_with_nat_prefix("", "argentinean", "female jews")
    assert result == "يهوديات أرجنتينيات"


def test_mens_religious_before_occ() -> None:
    """Test religious key in NAT_BEFORE_OCC list (nationality before religion)"""
    result = jobs_with_nat_prefix("", "yemeni", "sunni muslims")
    assert result == "يمنيون مسلمون سنة"


def test_womens_religious_with_nationality() -> None:
    """Test women's religious affiliation with compound nationality"""
    result = jobs_with_nat_prefix("", "north yemeni", "female coptic")
    assert result == "قبطيات يمنيات شماليات"
