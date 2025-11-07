"""Convenience exports for geographic translation tables."""

from .Cities import CITY_LABEL_PATCHES, CITY_OVERRIDES, CITY_TRANSLATIONS, CITY_TRANSLATIONS_LOWER, get_city_label_patches, get_city_translations, get_city_translations_lower
from .games_labs import GAME_CATEGORY_LABELS, SEASONAL_GAME_LABELS, SUMMER_WINTER_GAMES, SUMMER_WINTER_TABS, get_game_category_tabs, get_seasonal_game_labels
from .Labels_Contry import COUNTRY_LABEL_INDEX, COUNTRY_LABEL_INDEX_LOWER, COUNTRY_LABEL_OVERRIDES, POPULATION_OVERRIDES, get_country_label_index, get_country_label_index_lower
from .Labels_Contry2 import COUNTRY_ADMIN_LABELS, COUNTRY_ADMIN_LABELS_LOWER, get_country_admin_labels, get_country_admin_labels_lower
from .regions import PRIMARY_REGION_TRANSLATIONS, get_primary_region_translations
from .regions2 import INDIA_REGION_TRANSLATIONS, SECONDARY_REGION_TRANSLATIONS, get_india_region_translations, get_secondary_region_translations
from .us_counties import COUNTY_TRANSLATIONS, STATE_NAME_KEY_MAPPINGS, STATE_NAME_TRANSLATIONS, STATE_NAME_TRANSLATIONS_LOWER, STATE_SUFFIX_TEMPLATES, USA_PARTY_DERIVED_KEYS, USA_PARTY_LABELS, get_county_translations, get_party_labels, get_state_name_translations

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
    "COUNTY_TRANSLATIONS",
    "STATE_NAME_KEY_MAPPINGS",
    "STATE_NAME_TRANSLATIONS",
    "STATE_NAME_TRANSLATIONS_LOWER",
    "STATE_SUFFIX_TEMPLATES",
    "USA_PARTY_DERIVED_KEYS",
    "USA_PARTY_LABELS",
    "GAME_CATEGORY_LABELS",
    "SEASONAL_GAME_LABELS",
    "SUMMER_WINTER_GAMES",
    "SUMMER_WINTER_TABS",
    "get_city_label_patches",
    "get_city_translations",
    "get_city_translations_lower",
    "get_country_label_index",
    "get_country_label_index_lower",
    "get_country_admin_labels",
    "get_country_admin_labels_lower",
    "get_primary_region_translations",
    "get_secondary_region_translations",
    "get_india_region_translations",
    "get_county_translations",
    "get_state_name_translations",
    "get_party_labels",
    "get_game_category_tabs",
    "get_seasonal_game_labels",
]
