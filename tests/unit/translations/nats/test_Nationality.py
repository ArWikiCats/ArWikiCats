from ArWikiCats.translations.nats.Nationality import (
    build_american_forms,
    build_lookup_tables,
    normalize_aliases,
)


def test_alias_mapping() -> None:
    ArWikiCats = {"russian": {"male": "a", "males": "", "female": "", "females": "", "en": "russia", "ar": "روسيا"}}
    ArWikiCats["russians"] = {}  # before normalization
    out = normalize_aliases(ArWikiCats)
    assert out["russians"]["en"] == "russia"


def test_georgia_country_copy() -> None:
    ArWikiCats = {"georgian": {"male": "x", "males": "", "female": "", "females": "", "en": "georgia", "ar": "جورجي"}}
    out = normalize_aliases(ArWikiCats)
    assert out["georgia (country)"]["en"] == "georgia (country)"
    assert out["georgia (country)"]["male"] == "x"


def test_american_form_created() -> None:
    ArWikiCats = {"yemeni": {"male": "يمني", "males": "", "female": "", "females": "", "en": "yemen", "ar": "يمني"}}
    out = build_american_forms(ArWikiCats)
    assert "yemeni-american" in out


def test_no_american_if_no_gender() -> None:
    ArWikiCats = {"abc": {"male": "", "males": "", "female": "", "females": "", "en": "abc", "ar": "abc"}}
    out = build_american_forms(ArWikiCats)
    assert out == {}


def test_jewish_american() -> None:
    ArWikiCats = {"jewish": {"male": "يهودي", "males": "", "female": "", "females": "", "en": "jews", "ar": "يهود"}}
    out = build_american_forms(ArWikiCats)
    assert "jewish-american" in out
    assert "jewish american" in out  # special rule


def test_lookup_nat_men() -> None:
    nat = {"yemeni": {"male": "يمني", "males": "", "female": "", "females": "", "en": "yemen", "ar": "اليمن"}}
    out = build_lookup_tables(nat)
    assert out["Nat_men"]["yemeni"] == "يمني"


def test_country_mapping() -> None:
    nat = {"yemeni": {"male": "يمني", "males": "", "female": "", "females": "", "en": "yemen", "ar": "اليمن"}}
    out = build_lookup_tables(nat)
    assert out["countries_from_nat"]["yemen"] == "اليمن"


def test_the_country_normalization() -> None:
    nat = {
        "british": {
            "male": "بريطاني",
            "males": "",
            "female": "",
            "females": "",
            "en": "the uk",
            "ar": "المملكة المتحدة",
        }
    }
    out = build_lookup_tables(nat)
    assert out["countries_from_nat"]["uk"] == "المملكة المتحدة"


def test_full_pipeline() -> None:
    raw = {"yemeni": {"male": "يمني", "males": "", "female": "يمنية", "females": "", "en": "yemen", "ar": "اليمن"}}

    all_nat = build_american_forms(raw)
    out = build_lookup_tables(all_nat)

    assert "yemeni-american" in all_nat
    assert out["countries_from_nat"].get("yemeni-american") is None
    assert out["Nat_men"]["yemeni-american"] == "أمريكي يمني"


def test_empty_values_handled() -> None:
    raw = {"abc": {"male": "", "males": "", "female": "", "females": "", "en": "", "ar": ""}}
    all_nat2 = build_american_forms(raw)
    assert all_nat2 == {}


def test_uppercase_english_normalized() -> None:
    raw = {"Italian": {"male": "إيطالي", "males": "", "female": "", "females": "", "en": "ITALY", "ar": "إيطاليا"}}
    out = build_lookup_tables(raw)
    assert "italy" in out["countries_from_nat"]
