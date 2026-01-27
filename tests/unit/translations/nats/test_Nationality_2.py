from typing import Dict

import pytest

from ArWikiCats.translations.nats.Nationality import (
    All_Nat,
    NationalityEntry,
    build_american_forms,
    build_lookup_tables,
    load_sources,
    normalize_aliases,
)

# -------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------


def make_entry(
    male: str = "",
    males: str = "",
    women: str = "",
    females: str = "",
    en: str = "",
    ar: str = "",
) -> NationalityEntry:
    """Helper to build a NationalityEntry quickly."""
    return {
        "male": male,
        "males": males,
        "female": women,
        "females": females,
        "en": en,
        "ar": ar,
    }


# -------------------------------------------------------------------
# Tests for normalize_aliases
# -------------------------------------------------------------------


def test_normalize_aliases_alias_copy() -> None:
    """Alias keys (e.g. russians) should reuse target entry (russian)."""

    all_nat_o: Dict[str, NationalityEntry] = {
        "russian": make_entry(male="روسي", en="russia", ar="روسيا"),
        "russians": make_entry(),  # will be overwritten
    }

    out = normalize_aliases(all_nat_o)
    assert out["russians"]["en"] == "russia"
    assert out["russians"]["ar"] == "روسيا"
    assert out["russians"]["male"] == "روسي"


def test_normalize_aliases_georgia_country_copy() -> None:
    """georgia (country) should be derived from georgian entry and override 'en'."""

    base = {"georgian": make_entry(male="جورجي", en="georgia", ar="جورجي")}

    out = normalize_aliases(base)
    assert "georgia (country)" in out
    g = out["georgia (country)"]
    assert g["en"] == "georgia (country)"
    assert g["ar"] == "جورجي"
    assert g["male"] == "جورجي"


# -------------------------------------------------------------------
# Tests for build_american_forms
# -------------------------------------------------------------------


def test_build_american_forms_basic() -> None:
    """build_american_forms should create '-american' keys when there is at least one gendered form."""

    all_nat_o = {
        "yemeni": make_entry(male="يمني", en="yemen", ar="اليمن"),
    }

    out = build_american_forms(all_nat_o)

    assert "yemeni-american" in out
    entry = out["yemeni-american"]
    assert entry["male"] == "أمريكي يمني"


def test_build_american_forms_skips_if_no_gender() -> None:
    """No american form should be generated when all gender fields are empty."""

    all_nat_o = {
        "abc": make_entry(en="abc", ar="ايه بي سي"),  # all gender fields empty
    }

    out = build_american_forms(all_nat_o)

    assert out == {}


def test_build_american_forms_jewish_special_case() -> None:
    """For 'jewish' key, both 'jewish-american' and 'jewish american' should be created."""

    all_nat_o = {
        "jewish": make_entry(male="يهودي", en="jews", ar="يهود"),
    }

    out = build_american_forms(all_nat_o)

    assert "jewish-american" in out
    assert "jewish american" in out
    assert out["jewish-american"]["male"].startswith("أمريكي")
    assert out["jewish american"]["male"].startswith("أمريكي")


# -------------------------------------------------------------------
# Tests for build_lookup_tables
# -------------------------------------------------------------------


def test_build_lookup_tables_nat_men_and_country() -> None:
    """build_lookup_tables should fill Nat_men and countries_from_nat correctly."""

    all_nat = {
        "yemeni": make_entry(male="يمني", en="yemen", ar="اليمن"),
    }

    result = build_lookup_tables(all_nat)
    Nat_men = result["Nat_men"]
    countries_from_nat = result["countries_from_nat"]
    all_country_ar = result["all_country_ar"]

    assert Nat_men["yemeni"] == "يمني"
    assert countries_from_nat["yemen"] == "اليمن"
    assert all_country_ar["yemen"] == "اليمن"


def test_build_lookup_tables_the_prefix_normalization() -> None:
    """'the X' should be normalized to 'X' in countries_from_nat."""

    all_nat = {
        "british": make_entry(male="بريطاني", en="the uk", ar="المملكة المتحدة"),
    }

    result = build_lookup_tables(all_nat)
    countries_from_nat = result["countries_from_nat"]

    assert countries_from_nat["uk"] == "المملكة المتحدة"


def test_build_lookup_tables_uppercase_en_normalization() -> None:
    """Uppercase English names should be lowercased in mapping keys."""

    all_nat = {
        "italian": make_entry(male="إيطالي", en="ITALY", ar="إيطاليا"),
    }

    result = build_lookup_tables(all_nat)
    countries_from_nat = result["countries_from_nat"]

    assert "italy" in countries_from_nat
    assert countries_from_nat["italy"] == "إيطاليا"


def test_build_lookup_tables_en_nats_to_ar_label() -> None:
    """en_nats_to_ar_label should map nationality keys to Arabic labels."""

    all_nat = {
        "yemeni": make_entry(male="يمني", en="yemen", ar="اليمن"),
    }

    result = build_lookup_tables(all_nat)
    en_nats_to_ar_label = result["en_nats_to_ar_label"]

    assert en_nats_to_ar_label["yemeni"] == "اليمن"


def test_build_lookup_tables_iranian_special_case() -> None:
    """Special case: 'iranian' should create 'islamic republic of iran' key in countries_nat_en_key."""

    all_nat = {
        "iranian": make_entry(male="إيراني", en="iran", ar="إيران"),
    }

    result = build_lookup_tables(all_nat)
    keys_en = result["countries_nat_en_key"]

    assert "islamic republic of iran" in keys_en
    assert keys_en["islamic republic of iran"]["ar"] == "إيران"


# -------------------------------------------------------------------
# Integration tests
# -------------------------------------------------------------------


def test_full_pipeline_minimal() -> None:
    """End-to-end integration: from raw data → All_Nat → american forms → lookup tables."""

    raw = {
        "yemeni": make_entry(
            male="يمني",
            males="يمنيون",
            women="يمنية",
            females="يمنيات",
            en="yemen",
            ar="اليمن",
        )
    }

    # Build All_Nat from raw (simulate what module does)
    all_nat = {k.lower(): v for k, v in raw.items()}

    # Add American forms
    all_nat = build_american_forms(raw)
    assert "yemeni-american" in all_nat

    # Build lookup tables
    result = build_lookup_tables(all_nat)

    assert result["Nat_mens"]["yemeni-american"] == "أمريكيون يمنيون"


def test_full_pipeline_with_alias_and_american() -> None:
    """Integration that includes alias normalization + american forms + lookups."""

    # Start from a minimal nationalities_data-like structure
    all_nat_o = {
        "russian": make_entry(
            male="روسي",
            males="روس",
            women="روسية",
            females="روسيات",
            en="russia",
            ar="روسيا",
        )
    }

    # Apply alias normalization (this will add russians and others)
    all_nat_o = normalize_aliases(all_nat_o)

    # Lower-case main All_Nat dict
    all_nat = {k.lower(): v for k, v in all_nat_o.items()}

    # Lookup tables
    result = build_lookup_tables(all_nat)

    assert "russian" in result["Nat_men"]
    assert result["countries_from_nat"]["russia"] == "روسيا"


def test_normalize_aliases_keys() -> None:
    """Test that alias normalization works correctly for keys."""

    assert "turkish cypriot" in All_Nat
    assert "northern cypriot" in All_Nat
    assert All_Nat["turkish cypriot"] == All_Nat["northern cypriot"]
