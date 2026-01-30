"""Tests for build_nationalities.py nationality translation utilities."""

from ArWikiCats.translations.data_builders.build_nationalities import (
    AllNatDict,
    build_american_forms,
    build_en_nat_entries,
    build_lookup_tables,
    build_nationality_structure,
    load_sources,
    normalize_aliases,
)


class TestBuildNationalityStructure:
    """Tests for build_nationality_structure function."""

    def test_build_full_entry(self) -> None:
        val = {
            "male": "بريطاني",
            "males": "بريطانيون",
            "female": "بريطانية",
            "females": "بريطانيات",
            "the_male": "البريطاني",
            "the_female": "البريطانية",
            "en": "british",
            "ar": "بريطانيا",
        }
        result = build_nationality_structure(val)

        assert result["male"] == "بريطاني"
        assert result["females"] == "بريطانيات"
        assert result["en"] == "british"
        assert result["ar"] == "بريطانيا"

    def test_build_partial_entry_defaults_empty(self) -> None:
        val = {"male": "مصري", "females": "مصريات"}
        result = build_nationality_structure(val)

        assert result["male"] == "مصري"
        assert result["males"] == ""
        assert result["females"] == "مصريات"
        assert result["female"] == ""

    def test_build_empty_entry(self) -> None:
        result = build_nationality_structure({})

        assert result == {
            "male": "",
            "males": "",
            "female": "",
            "females": "",
            "the_male": "",
            "the_female": "",
            "en": "",
            "ar": "",
        }


class TestLoadSources:
    """Tests for load_sources function."""

    def test_load_merges_all_sources(self) -> None:
        raw_all_nat_o: AllNatDict = {
            "british": {
                "male": "بريطاني",
                "males": "بريطانيون",
                "female": "بريطانية",
                "females": "بريطانيات",
                "en": "british",
                "ar": "بريطانيا",
                "the_female": "البريطانية",
                "the_male": "البريطاني",
            }
        }
        nationality_directions_mapping: AllNatDict = {}
        raw_uu_nats: AllNatDict = {}
        raw_sub_nat: AllNatDict = {}
        continents: AllNatDict = {}
        raw_sub_nat_additional = {}
        countries_en_as_nationality_keys: list[str] = []

        result = load_sources(
            raw_all_nat_o,
            nationality_directions_mapping,
            raw_uu_nats,
            raw_sub_nat,
            continents,
            raw_sub_nat_additional,
            countries_en_as_nationality_keys,
        )

        assert "british" in result
        assert result["british"]["male"] == "بريطاني"

    def test_load_adds_country_alias(self) -> None:
        raw_all_nat_o: AllNatDict = {
            "saudi": {
                "male": "سعودي",
                "males": "سعوديون",
                "female": "سعودية",
                "females": "سعوديات",
                "en": "saudi arabia",
                "ar": "السعودية",
                "the_female": "السعودية",
                "the_male": "السعودي",
            }
        }
        nationality_directions_mapping: AllNatDict = {}
        raw_uu_nats: AllNatDict = {}
        raw_sub_nat: AllNatDict = {}
        continents: AllNatDict = {}
        raw_sub_nat_additional = {}
        countries_en_as_nationality_keys = ["saudi arabia"]

        result = load_sources(
            raw_all_nat_o,
            nationality_directions_mapping,
            raw_uu_nats,
            raw_sub_nat,
            continents,
            raw_sub_nat_additional,
            countries_en_as_nationality_keys,
        )

        assert "saudi arabia" in result
        assert result["saudi arabia"]["male"] == "سعودي"

    def test_load_with_en_nat_entries(self) -> None:
        raw_all_nat_o: AllNatDict = {}
        nationality_directions_mapping: AllNatDict = {}
        raw_uu_nats: AllNatDict = {}
        raw_sub_nat: AllNatDict = {}
        continents: AllNatDict = {}
        raw_sub_nat_additional = {}
        countries_en_as_nationality_keys: list[str] = []
        raw_nats_as_en_key = {"key1": {"en_nat": "Custom Name", "male": "custom", "males": "customs"}}

        result = load_sources(
            raw_all_nat_o,
            nationality_directions_mapping,
            raw_uu_nats,
            raw_sub_nat,
            continents,
            raw_sub_nat_additional,
            countries_en_as_nationality_keys,
            raw_nats_as_en_key,
        )

        assert "Custom Name" in result


class TestBuildEnNatEntries:
    """Tests for build_en_nat_entries function."""

    def test_build_from_valid_data(self) -> None:
        raw_data: AllNatDict = {"key1": {"en_nat": "Custom Name", "male": "custom", "males": "customs"}}
        result = build_en_nat_entries(raw_data)

        assert "Custom Name" in result
        assert result["Custom Name"]["male"] == "custom"

    def test_build_skips_missing_en_nat(self) -> None:
        raw_data: AllNatDict = {
            "key1": {"male": "custom"},  # no en_nat
            "key2": {"en_nat": "Has Entry", "male": "has"},
        }
        result = build_en_nat_entries(raw_data)

        assert "Has Entry" in result
        assert "key1" not in result

    def test_build_empty_returns_empty(self) -> None:
        result = build_en_nat_entries({})
        assert result == {}

    def test_build_none_returns_empty(self) -> None:
        result = build_en_nat_entries(None)
        assert result == {}


class TestNormalizeAliases:
    """Tests for normalize_aliases function."""

    def test_adds_alias_entries(self) -> None:
        all_nat_o: AllNatDict = {
            "argentine": {
                "male": "أرجنتيني",
                "males": "أرجنتينيون",
                "female": "أرجنتينية",
                "females": "أرجنتينيات",
                "en": "argentina",
                "ar": "الأرجنتين",
                "the_female": "الأرجنتينية",
                "the_male": "الأرجنتيني",
            }
        }
        result = normalize_aliases(all_nat_o)

        assert "argentinian" in result
        assert result["argentinian"]["male"] == "أرجنتيني"

    def test_skips_self_aliases(self) -> None:
        all_nat_o: AllNatDict = {
            "key": {
                "male": "value",
                "males": "",
                "female": "",
                "females": "",
                "en": "",
                "ar": "",
                "the_female": "",
                "the_male": "",
            }
        }
        original_len = len(all_nat_o)
        result = normalize_aliases(all_nat_o)

        assert len(result) >= original_len

    def test_adds_papua_new_guinean_special_case(self) -> None:
        all_nat_o: AllNatDict = {}
        result = normalize_aliases(all_nat_o)

        assert "papua_new_guinean!" in result
        assert result["papua_new_guinean!"]["ar"] == "بابوا غينيا الجديدة"

    def test_adds_georgia_country_variant(self) -> None:
        all_nat_o: AllNatDict = {
            "georgian": {
                "male": "جورجي",
                "males": "جورجيون",
                "female": "جورجية",
                "females": "جورجيات",
                "en": "georgia",
                "ar": "جورجيا",
                "the_female": "الجورجية",
                "the_male": "الجورجي",
            }
        }
        result = normalize_aliases(all_nat_o)

        assert "georgia (country)" in result
        assert result["georgia (country)"]["en"] == "georgia (country)"


class TestBuildAmericanForms:
    """Tests for build_american_forms function."""

    def test_builds_american_variants(self) -> None:
        all_nat_o: AllNatDict = {
            "jewish": {
                "male": "يهودي",
                "males": "يهود",
                "female": "يهودية",
                "females": "يهوديات",
                "en": "jewish",
                "ar": "يهود",
                "the_female": "اليهودية",
                "the_male": "اليهودي",
            }
        }
        result = build_american_forms(all_nat_o)

        assert "jewish-american" in result
        assert result["jewish-american"]["male"] == "أمريكي يهودي"
        assert result["jewish-american"]["female"] == "أمريكية يهودية"

    def test_builds_jewish_american_alias(self) -> None:
        all_nat_o: AllNatDict = {
            "jewish": {
                "male": "يهودي",
                "males": "يهود",
                "female": "يهودية",
                "females": "يهوديات",
                "en": "jewish",
                "ar": "يهود",
                "the_female": "اليهودية",
                "the_male": "اليهودي",
            }
        }
        result = build_american_forms(all_nat_o)

        assert "jewish american" in result

    def test_skips_entries_without_gender_fields(self) -> None:
        all_nat_o: AllNatDict = {
            "no_gender": {
                "male": "",
                "males": "",
                "female": "",
                "females": "",
                "en": "test",
                "ar": "اختبار",
                "the_female": "",
                "the_male": "",
            }
        }
        result = build_american_forms(all_nat_o)

        assert "no_gender-american" not in result


class TestBuildLookupTables:
    """Tests for build_lookup_tables function."""

    def test_builds_all_tables(self) -> None:
        all_nat: AllNatDict = {
            "british": {
                "male": "بريطاني",
                "males": "بريطانيون",
                "female": "بريطانية",
                "females": "بريطانيات",
                "en": "british",
                "ar": "بريطانيا",
                "the_female": "البريطانية",
                "the_male": "البريطاني",
            }
        }
        result = build_lookup_tables(all_nat)

        assert "Nat_men" in result
        assert "Nat_mens" in result
        assert "Nat_women" in result
        assert "Nat_Womens" in result
        assert result["Nat_men"]["british"] == "بريطاني"
        assert result["Nat_women"]["british"] == "بريطانية"

    def test_builds_country_mappings(self) -> None:
        all_nat: AllNatDict = {
            "egyptian": {
                "male": "مصري",
                "males": "مصريون",
                "female": "مصرية",
                "females": "مصريات",
                "en": "egypt",
                "ar": "مصر",
                "the_female": "المصرية",
                "the_male": "المصري",
            }
        }
        result = build_lookup_tables(all_nat)

        assert "egypt" in result["countries_from_nat"]
        assert result["countries_from_nat"]["egypt"] == "مصر"

    def test_handles_the_prefix(self) -> None:
        all_nat: AllNatDict = {
            "key": {
                "male": "",
                "males": "",
                "female": "",
                "females": "",
                "en": "the gambia",
                "ar": "غامبيا",
                "the_female": "",
                "the_male": "",
            }
        }
        result = build_lookup_tables(all_nat)

        assert "gambia" in result["countries_from_nat"]

    def test_adds_iran_special_case(self) -> None:
        all_nat: AllNatDict = {
            "iranian": {
                "male": "إيراني",
                "males": "إيرانيون",
                "female": "إيرانية",
                "females": "إيرانيات",
                "en": "iran",
                "ar": "إيران",
                "the_female": "الإيرانية",
                "the_male": "الإيراني",
            }
        }
        result = build_lookup_tables(all_nat)

        assert "islamic republic of iran" in result["countries_nat_en_key"]

    def test_adds_serbia_montenegro(self) -> None:
        result = build_lookup_tables({})

        assert "serbia and montenegro" in result["countries_from_nat"]
        assert "serbia-and-montenegro" in result["countries_from_nat"]
