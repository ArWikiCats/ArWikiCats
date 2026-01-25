""" """

from ..geo import (
    CITY_TRANSLATIONS_LOWER,
    COUNTRY_ADMIN_LABELS,
    COUNTRY_LABEL_OVERRIDES,
    INDIA_REGION_TRANSLATIONS,
    MAIN_REGION_TRANSLATIONS,
    SECONDARY_REGION_TRANSLATIONS,
    US_STATES,
    USA_PARTY_DERIVED_KEYS,
    _build_country_label_index,
    raw_region_overrides,
)
from ..helps import len_print
from ..jobs import SINGERS_TAB
from ..mixed import (
    ALBUMS_TYPE,
    NEW_2023,
    generate_key_mappings,
    keys2_py,
    new2019,
    pop_final6,
    pop_final_3,
)

new2019.update(USA_PARTY_DERIVED_KEYS)

from ..mixed import BASE_POP_FINAL_5
from ..nats import all_country_ar
from ..others import (
    MEDIA_CATEGORY_TRANSLATIONS,
    TAXON_TABLE,
    language_key_translations,
)
from ..sports import TENNIS_KEYS
from ..tv import (
    film_keys_for_female,
    film_keys_for_male,
)

pf_keys2 = generate_key_mappings(
    keys2_py,
    pop_final_3,
    SINGERS_TAB,
    film_keys_for_female,
    ALBUMS_TYPE,
    film_keys_for_male,
    TENNIS_KEYS,
    pop_final6,
    MEDIA_CATEGORY_TRANSLATIONS,
    language_key_translations,
    new2019,
    NEW_2023,
)

NEW_P17_FINAL = _build_country_label_index(  # 68,981
    CITY_TRANSLATIONS_LOWER,
    all_country_ar,
    US_STATES,
    COUNTRY_LABEL_OVERRIDES,
    COUNTRY_ADMIN_LABELS,
    MAIN_REGION_TRANSLATIONS,
    raw_region_overrides,
    SECONDARY_REGION_TRANSLATIONS,
    INDIA_REGION_TRANSLATIONS,
    TAXON_TABLE,
    BASE_POP_FINAL_5,
)

len_print.data_len(
    "build_data",
    {
        "pf_keys2": pf_keys2,
        "NEW_P17_FINAL": NEW_P17_FINAL,
    },
)

__all__ = [
    "pf_keys2",
    "NEW_P17_FINAL",
]
