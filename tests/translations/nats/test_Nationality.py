import pytest

from ArWikiCats.translations.nats.Nationality import (
    build_american_forms,
    build_lookup_tables,
    load_sources,
    normalize_aliases,
)


def test_load_sources_return_type() -> None:
    data = load_sources()
    assert isinstance(data, dict)
    for v in data.values():
        assert set(v.keys()) == {"male", "males", "female", "females", "en", "ar"}
        assert all(isinstance(x, str) for x in v.values())


def test_sources_are_merged(monkeypatch) -> None:
    monkeypatch.setattr(
        "ArWikiCats.translations.nats.Nationality.open_json_file", lambda name: {"x": {"en": "test", "ar": "اختبار"}}
    )
    data = load_sources()
    assert "x" in data


def test_hindustani_normalized(monkeypatch) -> None:
    monkeypatch.setattr(
        "ArWikiCats.translations.nats.Nationality.open_json_file",
        lambda name: {"hindustani": {"en": "hindustani", "ar": "هندي"}} if name == "nationalities/uu_nats.json" else {},
    )
    data = load_sources()
    assert "hindustan" in data


def test_alias_mapping() -> None:
    ArWikiCats = {"russian": {"male": "a", "males": "", "female": "", "females": "", "en": "russia", "ar": "روسيا"}}
    ArWikiCats["russians"] = {}  # before normalization
    out = normalize_aliases(ArWikiCats)
    assert out["russians"]["en"] == "russia"


def test_southwest_asian_added() -> None:
    out = normalize_aliases({})
    assert "southwest asian" in out


def test_georgia_country_copy() -> None:
    ArWikiCats = {"georgian": {"male": "x", "males": "", "female": "", "females": "", "en": "georgia", "ar": "جورجي"}}
    out = normalize_aliases(ArWikiCats)
    assert out["georgia (country)"]["en"] == "georgia (country)"
    assert out["georgia (country)"]["male"] == "x"


def test_american_form_created() -> None:
    ArWikiCats = {"yemeni": {"male": "يمني", "males": "", "female": "", "females": "", "en": "yemen", "ar": "يمني"}}
    out, count = build_american_forms({}, ArWikiCats)
    assert "yemeni-american" in out
    assert count == 1


def test_no_american_if_no_gender() -> None:
    ArWikiCats = {"abc": {"male": "", "males": "", "female": "", "females": "", "en": "abc", "ar": "abc"}}
    out, count = build_american_forms({}, ArWikiCats)
    assert out == {}
    assert count == 0


def test_jewish_american() -> None:
    ArWikiCats = {"jewish": {"male": "يهودي", "males": "", "female": "", "females": "", "en": "jews", "ar": "يهود"}}
    out, count = build_american_forms({}, ArWikiCats)
    assert "jewish-american" in out
    assert "jewish american" in out  # special rule


def test_lookup_nat_men() -> None:
    nat = {"yemeni": {"male": "يمني", "males": "", "female": "", "females": "", "en": "yemen", "ar": "اليمن"}}
    out = build_lookup_tables(nat, nat)
    assert out["Nat_men"]["yemeni"] == "يمني"


def test_country_mapping() -> None:
    nat = {"yemeni": {"male": "يمني", "males": "", "female": "", "females": "", "en": "yemen", "ar": "اليمن"}}
    out = build_lookup_tables(nat, nat)
    assert out["countries_from_nat"]["yemen"] == "اليمن"


def test_the_country_normalization() -> None:
    nat = {
        "british": {"male": "بريطاني", "males": "", "female": "", "females": "", "en": "the uk", "ar": "المملكة المتحدة"}
    }
    out = build_lookup_tables(nat, nat)
    assert out["countries_from_nat"]["uk"] == "المملكة المتحدة"


def test_full_pipeline() -> None:
    raw = {"yemeni": {"male": "يمني", "males": "", "female": "يمنية", "females": "", "en": "yemen", "ar": "اليمن"}}

    all_nat = {k.lower(): v for k, v in raw.items()}
    all_nat, cnt = build_american_forms(all_nat, raw)
    out = build_lookup_tables(all_nat, raw)

    assert "yemeni-american" in all_nat
    assert out["Nat_men"]["yemeni"] == "يمني"
    assert out["countries_from_nat"]["yemen"] == "اليمن"


def test_empty_values_handled() -> None:
    raw = {"abc": {"male": "", "males": "", "female": "", "females": "", "en": "", "ar": ""}}
    all_nat = {"abc": raw["abc"]}
    all_nat2, c = build_american_forms(all_nat, raw)
    assert c == 0


def test_uppercase_english_normalized() -> None:
    raw = {"Italian": {"male": "إيطالي", "males": "", "female": "", "females": "", "en": "ITALY", "ar": "إيطاليا"}}
    out = build_lookup_tables(raw, raw)
    assert "italy" in out["countries_from_nat"]
