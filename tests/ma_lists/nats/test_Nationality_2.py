
import pytest

from typing import Dict
from src.ma_lists.nats.Nationality import (
    load_sources,
    normalize_aliases,
    build_american_forms,
    build_lookup_tables,
    NationalityEntry,
)


# -------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------

def make_entry(
    men: str = "",
    mens: str = "",
    women: str = "",
    womens: str = "",
    en: str = "",
    ar: str = "",
) -> NationalityEntry:
    """Helper to build a NationalityEntry quickly."""
    return {
        "men": men,
        "mens": mens,
        "women": women,
        "womens": womens,
        "en": en,
        "ar": ar,
    }


# -------------------------------------------------------------------
# Tests for load_sources
# -------------------------------------------------------------------

def test_load_sources_returns_normalized_entries(monkeypatch):
    """load_sources should return dict of NationalityEntry with all keys present and string values."""

    def fake_open_json_file(name: str):
        if name == "All_Nat_o":
            return {
                "yemeni": {"en": "yemen", "ar": "اليمن", "men": "يمني"},
            }
        if name == "uu_nats":
            return {
                "hindustani": {"en": "hindustani", "ar": "هندوستاني"},
            }
        if name == "Sub_Nat":
            return {
                "italian": {"men": "إيطالي", "en": "italy", "ar": "إيطاليا"},
            }
        return {}

    # Patch open_json_file used inside load_sources
    monkeypatch.setattr("src.ma_lists.nats.Nationality.open_json_file", fake_open_json_file)

    data = load_sources()

    assert isinstance(data, dict)
    assert "yemeni" in data
    assert "hindustan" in data
    assert "italian" in data

    for entry in data.values():
        # Ensure all required keys are present
        assert set(entry.keys()) == {"men", "mens", "women", "womens", "en", "ar"}
        # Ensure all values are strings
        assert all(isinstance(v, str) for v in entry.values())


def test_load_sources_hindustani_mapped_to_hindustan(monkeypatch):
    """hindustani should produce an additional key hindustan in the resulting dict."""

    def fake_open_json_file(name: str):
        if name == "All_Nat_o":
            return {}
        if name == "uu_nats":
            return {
                "hindustani": {"en": "hindustani", "ar": "هندوستاني"},
            }
        if name == "Sub_Nat":
            return {}
        return {}

    monkeypatch.setattr("src.ma_lists.nats.Nationality.open_json_file", fake_open_json_file)

    data = load_sources()
    assert "hindustan" in data
    assert data["hindustan"]["en"] == "hindustani"
    assert data["hindustan"]["ar"] == "هندوستاني"


def test_load_sources_merge_all_sources(monkeypatch):
    """All_Nat_o, uu_nats and Sub_Nat contents should be merged into a single dict."""

    def fake_open_json_file(name: str):
        if name == "All_Nat_o":
            return {"a": {"en": "A", "ar": "أ"}}
        if name == "uu_nats":
            return {"b": {"en": "B", "ar": "ب"}}
        if name == "Sub_Nat":
            return {"c": {"en": "C", "ar": "ج"}}
        return {}

    monkeypatch.setattr("src.ma_lists.nats.Nationality.open_json_file", fake_open_json_file)

    data = load_sources()
    assert set(data.keys()) == {"a", "b", "c"}


# -------------------------------------------------------------------
# Tests for normalize_aliases
# -------------------------------------------------------------------

def test_normalize_aliases_alias_copy():
    """Alias keys (e.g. russians) should reuse target entry (russian)."""

    all_nat_o: Dict[str, NationalityEntry] = {
        "russian": make_entry(men="روسي", en="russia", ar="روسيا"),
        "russians": make_entry(),  # will be overwritten
    }

    out = normalize_aliases(all_nat_o)
    assert out["russians"]["en"] == "russia"
    assert out["russians"]["ar"] == "روسيا"
    assert out["russians"]["men"] == "روسي"


def test_normalize_aliases_adds_southwest_asian():
    """normalize_aliases must always inject 'southwest asian' entry."""

    out = normalize_aliases({})
    assert "southwest asian" in out
    entry = out["southwest asian"]
    assert entry["en"] == "southwest asia"
    assert entry["ar"] == "جنوب غرب آسيا"


def test_normalize_aliases_georgia_country_copy():
    """georgia (country) should be derived from georgian entry and override 'en'."""

    base = {
        "georgian": make_entry(
            men="جورجي", en="georgia", ar="جورجي"
        )
    }

    out = normalize_aliases(base)
    assert "georgia (country)" in out
    g = out["georgia (country)"]
    assert g["en"] == "georgia (country)"
    assert g["ar"] == "جورجي"
    assert g["men"] == "جورجي"


def test_normalize_aliases_papua_new_guinean_added():
    """normalize_aliases must inject 'papua new guinean x ' block."""

    out = normalize_aliases({})
    assert "papua new guinean x " in out
    entry = out["papua new guinean x "]
    assert entry["en"] == "papua new guinea"
    assert entry["ar"] == "بابوا غينيا الجديدة"


# -------------------------------------------------------------------
# Tests for build_american_forms
# -------------------------------------------------------------------

def test_build_american_forms_basic():
    """build_american_forms should create '-american' keys when there is at least one gendered form."""

    all_nat = {}
    all_nat_o = {
        "yemeni": make_entry(men="يمني", en="yemen", ar="اليمن"),
    }

    out, count = build_american_forms(all_nat, all_nat_o)

    assert count == 1
    assert "yemeni-american" in out
    entry = out["yemeni-american"]
    assert entry["men"] == "أمريكي يمني"


def test_build_american_forms_skips_if_no_gender():
    """No american form should be generated when all gender fields are empty."""

    all_nat = {}
    all_nat_o = {
        "abc": make_entry(en="abc", ar="ايه بي سي"),  # all gender fields empty
    }

    out, count = build_american_forms(all_nat, all_nat_o)

    assert count == 0
    assert out == {}


def test_build_american_forms_jewish_special_case():
    """For 'jewish' key, both 'jewish-american' and 'jewish american' should be created."""

    all_nat = {}
    all_nat_o = {
        "jewish": make_entry(men="يهودي", en="jews", ar="يهود"),
    }

    out, count = build_american_forms(all_nat, all_nat_o)

    assert count == 1
    assert "jewish-american" in out
    assert "jewish american" in out
    assert out["jewish-american"]["men"].startswith("أمريكي")
    assert out["jewish american"]["men"].startswith("أمريكي")


# -------------------------------------------------------------------
# Tests for build_lookup_tables
# -------------------------------------------------------------------

def test_build_lookup_tables_nat_men_and_country():
    """build_lookup_tables should fill Nat_men and contries_from_nat correctly."""

    all_nat = {
        "yemeni": make_entry(men="يمني", en="yemen", ar="اليمن"),
    }

    result = build_lookup_tables(all_nat, all_nat)
    Nat_men = result["Nat_men"]
    contries_from_nat = result["contries_from_nat"]
    all_country_ar = result["all_country_ar"]

    assert Nat_men["yemeni"] == "يمني"
    assert contries_from_nat["yemen"] == "اليمن"
    assert all_country_ar["yemen"] == "اليمن"


def test_build_lookup_tables_the_prefix_normalization():
    """'the X' should be normalized to 'X' in contries_from_nat."""

    all_nat = {
        "british": make_entry(men="بريطاني", en="the uk", ar="المملكة المتحدة"),
    }

    result = build_lookup_tables(all_nat, all_nat)
    contries_from_nat = result["contries_from_nat"]

    assert contries_from_nat["uk"] == "المملكة المتحدة"


def test_build_lookup_tables_uppercase_en_normalization():
    """Uppercase English names should be lowercased in mapping keys."""

    all_nat = {
        "italian": make_entry(men="إيطالي", en="ITALY", ar="إيطاليا"),
    }

    result = build_lookup_tables(all_nat, all_nat)
    contries_from_nat = result["contries_from_nat"]

    assert "italy" in contries_from_nat
    assert contries_from_nat["italy"] == "إيطاليا"


def test_build_lookup_tables_en_nats_to_ar_label():
    """en_nats_to_ar_label should map nationality keys to Arabic labels."""

    all_nat = {
        "yemeni": make_entry(men="يمني", en="yemen", ar="اليمن"),
    }

    result = build_lookup_tables(all_nat, all_nat)
    en_nats_to_ar_label = result["en_nats_to_ar_label"]

    assert en_nats_to_ar_label["yemeni"] == "اليمن"


def test_build_lookup_tables_iranian_special_case():
    """Special case: 'iranian' should create 'islamic republic of iran' key in all_country_with_nat_keys_is_en."""

    all_nat = {
        "iranian": make_entry(men="إيراني", en="iran", ar="إيران"),
    }

    result = build_lookup_tables(all_nat, all_nat)
    keys_en = result["all_country_with_nat_keys_is_en"]

    assert "islamic republic of iran" in keys_en
    assert keys_en["islamic republic of iran"]["ar"] == "إيران"


# -------------------------------------------------------------------
# Integration tests
# -------------------------------------------------------------------

def test_full_pipeline_minimal():
    """End-to-end integration: from raw data → All_Nat → american forms → lookup tables."""

    raw = {
        "yemeni": make_entry(
            men="يمني",
            mens="يمنيون",
            women="يمنية",
            womens="يمنيات",
            en="yemen",
            ar="اليمن",
        )
    }

    # Build All_Nat from raw (simulate what module does)
    all_nat = {k.lower(): v for k, v in raw.items()}

    # Add American forms
    all_nat, count = build_american_forms(all_nat, raw)
    assert count == 1
    assert "yemeni-american" in all_nat

    # Build lookup tables
    result = build_lookup_tables(all_nat, raw)

    assert result["Nat_men"]["yemeni"] == "يمني"
    assert result["contries_from_nat"]["yemen"] == "اليمن"
    assert result["all_country_ar"]["yemen"] == "اليمن"


def test_full_pipeline_with_alias_and_american():
    """Integration that includes alias normalization + american forms + lookups."""

    # Start from a minimal All_Nat_o-like structure
    all_nat_o = {
        "russian": make_entry(
            men="روسي",
            mens="روس",
            women="روسية",
            womens="روسيات",
            en="russia",
            ar="روسيا",
        )
    }

    # Apply alias normalization (this will add russians and others)
    all_nat_o = normalize_aliases(all_nat_o)

    # Lower-case main All_Nat dict
    all_nat = {k.lower(): v for k, v in all_nat_o.items()}

    # American forms
    all_nat, count = build_american_forms(all_nat, all_nat_o)
    assert count >= 1

    # Lookup tables
    result = build_lookup_tables(all_nat, all_nat_o)

    assert "russian" in result["Nat_men"]
    assert result["contries_from_nat"]["russia"] == "روسيا"
