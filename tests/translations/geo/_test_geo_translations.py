from __future__ import annotations

import pytest

from ArWikiCats.translations.geo import (
    Cities,
    labels_country,
    labels_country2,
    regions,
    regions2,
    us_counties,
)


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
        labels = labels_country.get_country_label_index()

        assert labels["indycar"] == "أندي كار"
        assert labels is not labels_country.COUNTRY_LABEL_INDEX

    def test_country_label_index_lower_is_lowercase(self):
        lower_labels = labels_country.get_country_label_index_lower()

        assert all(key == key.lower() for key in lower_labels)
        assert lower_labels is not labels_country.COUNTRY_LABEL_INDEX_LOWER

    def test_country_admin_labels_include_suffix_variants(self):
        admin_labels = labels_country2.get_country_admin_labels()

        assert admin_labels["luanda"] == "لواندا"
        assert admin_labels["luanda province"] == "مقاطعة لواندا"
        assert admin_labels is not labels_country2.COUNTRY_ADMIN_LABELS

    def test_country_admin_labels_lower_is_lowercase(self):
        lower_admin = labels_country2.get_country_admin_labels_lower()

        assert all(key == key.lower() for key in lower_admin)
        assert lower_admin is not labels_country2.COUNTRY_ADMIN_LABELS_LOWER


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
