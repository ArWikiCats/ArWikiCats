"""Convenience exports for geographic translation tables."""

from .Cities import (
    CITY_LABEL_PATCHES,
    CITY_OVERRIDES,
    CITY_TRANSLATIONS,
    CITY_TRANSLATIONS_LOWER,
)
from .labels_country import (
    US_STATES,
    COUNTRY_LABEL_INDEX,
    COUNTRY_LABEL_INDEX_LOWER,
    COUNTRY_LABEL_OVERRIDES,
    POPULATION_OVERRIDES,
    get_country_label_index,
    get_country_label_index_lower,
)
from .labels_country2 import (
    COUNTRY_ADMIN_LABELS,
    COUNTRY_ADMIN_LABELS_LOWER,
    get_country_admin_labels,
    get_country_admin_labels_lower,
)
from .regions import PRIMARY_REGION_TRANSLATIONS, get_primary_region_translations
from .regions2 import (
    INDIA_REGION_TRANSLATIONS,
    SECONDARY_REGION_TRANSLATIONS,
    get_india_region_translations,
    get_secondary_region_translations,
)
from .us_counties import (
    US_COUNTY_TRANSLATIONS,
    USA_PARTY_DERIVED_KEYS,
)

__all__ = [
    "CITY_LABEL_PATCHES",
    "CITY_OVERRIDES",
    "CITY_TRANSLATIONS",
    "CITY_TRANSLATIONS_LOWER",
    "COUNTRY_LABEL_INDEX",
    "COUNTRY_LABEL_INDEX_LOWER",
    "COUNTRY_LABEL_OVERRIDES",
    "POPULATION_OVERRIDES",
    "COUNTRY_ADMIN_LABELS",
    "COUNTRY_ADMIN_LABELS_LOWER",
    "PRIMARY_REGION_TRANSLATIONS",
    "SECONDARY_REGION_TRANSLATIONS",
    "INDIA_REGION_TRANSLATIONS",
    "US_COUNTY_TRANSLATIONS",
    "USA_PARTY_DERIVED_KEYS",
    "get_country_label_index",
    "get_country_label_index_lower",
    "get_country_admin_labels",
    "get_country_admin_labels_lower",
    "get_primary_region_translations",
    "get_secondary_region_translations",
    "get_india_region_translations",
    "US_STATES",
]
