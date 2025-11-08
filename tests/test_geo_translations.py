from __future__ import annotations

import pytest

from src.ma_lists.geo import Cities, Labels_Contry, Labels_Contry2, games_labs, regions, regions2, us_counties


@pytest.mark.unit
class TestCitiesModule:
    def test_get_city_translations_returns_copy(self):
        translations = Cities.get_city_translations()

        assert translations is not Cities.CITY_TRANSLATIONS
        assert translations == Cities.CITY_TRANSLATIONS

        translations["Jerusalem"] = "test"
        assert Cities.CITY_TRANSLATIONS["Jerusalem"] == "القدس"

    def test_city_label_patches_returns_copy(self):
        patches = Cities.get_city_label_patches()

        assert patches is not Cities.CITY_LABEL_PATCHES
        assert patches == Cities.CITY_LABEL_PATCHES

    def test_city_translations_lower_are_lowercase(self):
        lower_translations = Cities.get_city_translations_lower()

        assert all(key == key.lower() for key in lower_translations)
        assert lower_translations["jerusalem"] == Cities.CITY_TRANSLATIONS_LOWER["jerusalem"]


@pytest.mark.unit
class TestCountryLabels:
    def test_country_label_index_contains_overrides(self):
        labels = Labels_Contry.get_country_label_index()

        assert labels["indycar"] == "أندي كار"
        assert labels is not Labels_Contry.COUNTRY_LABEL_INDEX

    def test_country_label_index_lower_is_lowercase(self):
        lower_labels = Labels_Contry.get_country_label_index_lower()

        assert all(key == key.lower() for key in lower_labels)
        assert lower_labels is not Labels_Contry.COUNTRY_LABEL_INDEX_LOWER

    def test_country_admin_labels_include_suffix_variants(self):
        admin_labels = Labels_Contry2.get_country_admin_labels()

        assert admin_labels["luanda"] == "لواندا"
        assert admin_labels["luanda province"] == "مقاطعة لواندا"
        assert admin_labels is not Labels_Contry2.COUNTRY_ADMIN_LABELS

    def test_country_admin_labels_lower_is_lowercase(self):
        lower_admin = Labels_Contry2.get_country_admin_labels_lower()

        assert all(key == key.lower() for key in lower_admin)
        assert lower_admin is not Labels_Contry2.COUNTRY_ADMIN_LABELS_LOWER


@pytest.mark.unit
class TestGameLabels:
    def test_seasonal_labels_include_variants(self):
        labels = games_labs.get_seasonal_game_labels()

        assert labels["olympic games"] == "الألعاب الأولمبية"
        assert labels["winter olympic games"] == "الألعاب الأولمبية الشتوية"
        assert labels["summer olympic games"] == "الألعاب الأولمبية الصيفية"
        assert labels["west olympic games"] == "الألعاب الأولمبية الغربية"

    def test_game_category_tabs_combine_categories(self):
        tabs = games_labs.get_game_category_tabs()

        assert tabs["olympic games events"] == "أحداث الألعاب الأولمبية"
        assert tabs["winter olympic games templates"] == "قوالب الألعاب الأولمبية الشتوية"
        assert tabs is not games_labs.SUMMER_WINTER_TABS


@pytest.mark.unit
class TestRegionLabels:
    def test_primary_region_translations_include_known_entries(self):
        primary = regions.get_primary_region_translations()

        assert primary["lima region"] == "إقليم ليما"
        assert primary is not regions.PRIMARY_REGION_TRANSLATIONS

    def test_secondary_region_translations_include_suffixes(self):
        secondary = regions2.get_secondary_region_translations()

        assert secondary["bangui"] == "بانغي"
        assert secondary["bangui prefecture"] == "محافظة بانغي"

    def test_india_region_translations_returns_copy(self):
        india = regions2.get_india_region_translations()

        assert india is not regions2.INDIA_REGION_TRANSLATIONS


@pytest.mark.unit
class TestUSCountiesHelpers:
    def test_extend_state_suffix_templates_adds_party_variants(self):
        result = us_counties._extend_state_suffix_templates(
            {" base": "template %s"}, {"Democratic Party": "الحزب الديمقراطي"}
        )

        assert result[" base"] == "template %s"
        assert result[" democratic partys"] == "أعضاء الحزب الديمقراطي في %s"
        assert result[" democratics"] == "أعضاء الحزب الديمقراطي في %s"

    def test_build_party_derived_keys_skips_blank_labels(self):
        derived = us_counties._build_party_derived_keys(
            {"Democratic Party": "الحزب الديمقراطي", "Blank Party": " "}
        )

        assert "democratic party" in derived
        assert derived["democratic party members"] == "أعضاء الحزب الديمقراطي"
        assert "blank party" not in derived

    def test_build_state_key_mappings_handles_templates(self):
        mappings = us_counties._build_state_key_mappings(
            {"California": "كاليفورنيا", "Texas": "ولاية تكساس"}
        )

        assert mappings["california"] == "كاليفورنيا"
        assert mappings["california house of representatives"] == "مجلس نواب ولاية كاليفورنيا"
        assert mappings["texas house of representatives"] == "مجلس نواب ولاية تكساس"
        assert mappings["texas state house of representatives"] == "مجلس نواب ولاية تكساس"

    def test_get_state_name_translations_returns_copy(self):
        states = us_counties.get_state_name_translations()

        assert states is not us_counties.STATE_NAME_TRANSLATIONS
        assert states["ohio"] == "أوهايو"

    def test_get_party_labels_returns_copy(self):
        parties = us_counties.get_party_labels()

        assert parties is not us_counties.USA_PARTY_LABELS
        assert parties["democratic party"] == "الحزب الديمقراطي"

    def test_get_county_translations_returns_copy(self):
        counties = us_counties.get_county_translations()

        assert counties is not us_counties.COUNTY_TRANSLATIONS
        counties["example"] = "test"
        assert "example" not in us_counties.COUNTY_TRANSLATIONS
