import pytest

from src.translations.nats.Nationality import (
    build_american_forms,
    build_lookup_tables,
    load_sources,
    normalize_aliases,
)


def test_load_sources_return_type():
    data = load_sources()
    assert isinstance(data, dict)
    for v in data.values():
        assert set(v.keys()) == {"men", "mens", "women", "womens", "en", "ar"}
        assert all(isinstance(x, str) for x in v.values())


def test_sources_are_merged(monkeypatch):
    monkeypatch.setattr("src.translations.nats.Nationality.open_json_file", lambda name: {"x": {"en": "test", "ar": "اختبار"}})
    data = load_sources()
    assert "x" in data


def test_hindustani_normalized(monkeypatch):
    monkeypatch.setattr("src.translations.nats.Nationality.open_json_file", lambda name: {"hindustani": {"en": "hindustani", "ar": "هندي"}} if name == "uu_nats" else {})
    data = load_sources()
    assert "hindustan" in data


def test_alias_mapping():
    src = {"russian": {"men": "a", "mens": "", "women": "", "womens": "", "en": "russia", "ar": "روسيا"}}
    src["russians"] = {}  # before normalization
    out = normalize_aliases(src)
    assert out["russians"]["en"] == "russia"


def test_southwest_asian_added():
    out = normalize_aliases({})
    assert "southwest asian" in out


def test_georgia_country_copy():
    src = {"georgian": {"men": "x", "mens": "", "women": "", "womens": "", "en": "georgia", "ar": "جورجي"}}
    out = normalize_aliases(src)
    assert out["georgia (country)"]["en"] == "georgia (country)"
    assert out["georgia (country)"]["men"] == "x"


def test_american_form_created():
    src = {"yemeni": {"men": "يمني", "mens": "", "women": "", "womens": "", "en": "yemen", "ar": "يمني"}}
    out, count = build_american_forms({}, src)
    assert "yemeni-american" in out
    assert count == 1


def test_no_american_if_no_gender():
    src = {"abc": {"men": "", "mens": "", "women": "", "womens": "", "en": "abc", "ar": "abc"}}
    out, count = build_american_forms({}, src)
    assert out == {}
    assert count == 0


def test_jewish_american():
    src = {"jewish": {"men": "يهودي", "mens": "", "women": "", "womens": "", "en": "jews", "ar": "يهود"}}
    out, count = build_american_forms({}, src)
    assert "jewish-american" in out
    assert "jewish american" in out  # special rule


def test_lookup_nat_men():
    nat = {"yemeni": {"men": "يمني", "mens": "", "women": "", "womens": "", "en": "yemen", "ar": "اليمن"}}
    out = build_lookup_tables(nat, nat)
    assert out["Nat_men"]["yemeni"] == "يمني"


def test_country_mapping():
    nat = {"yemeni": {"men": "يمني", "mens": "", "women": "", "womens": "", "en": "yemen", "ar": "اليمن"}}
    out = build_lookup_tables(nat, nat)
    assert out["contries_from_nat"]["yemen"] == "اليمن"


def test_the_country_normalization():
    nat = {"british": {"men": "بريطاني", "mens": "", "women": "", "womens": "", "en": "the uk", "ar": "المملكة المتحدة"}}
    out = build_lookup_tables(nat, nat)
    assert out["contries_from_nat"]["uk"] == "المملكة المتحدة"


def test_full_pipeline():
    raw = {"yemeni": {"men": "يمني", "mens": "", "women": "يمنية", "womens": "", "en": "yemen", "ar": "اليمن"}}

    all_nat = {k.lower(): v for k, v in raw.items()}
    all_nat, cnt = build_american_forms(all_nat, raw)
    out = build_lookup_tables(all_nat, raw)

    assert "yemeni-american" in all_nat
    assert out["Nat_men"]["yemeni"] == "يمني"
    assert out["contries_from_nat"]["yemen"] == "اليمن"


def test_empty_values_handled():
    raw = {"abc": {"men": "", "mens": "", "women": "", "womens": "", "en": "", "ar": ""}}
    all_nat = {"abc": raw["abc"]}
    all_nat2, c = build_american_forms(all_nat, raw)
    assert c == 0


def test_uppercase_english_normalized():
    raw = {"Italian": {"men": "إيطالي", "mens": "", "women": "", "womens": "", "en": "ITALY", "ar": "إيطاليا"}}
    out = build_lookup_tables(raw, raw)
    assert "italy" in out["contries_from_nat"]
