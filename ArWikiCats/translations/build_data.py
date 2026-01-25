""" """

from .geo import USA_PARTY_DERIVED_KEYS
from .helps import len_print
from .jobs import SINGERS_TAB
from .mixed import (
    ALBUMS_TYPE,
    NEW_2023,
    generate_key_mappings,
    keys2_py,
    new2019,
    pop_final6,
    pop_final_3,
)

new2019.update(USA_PARTY_DERIVED_KEYS)

from .others import (
    MEDIA_CATEGORY_TRANSLATIONS,
    language_key_translations,
)
from .sports import TENNIS_KEYS
from .tv import (
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

len_print.data_len(
    "all_keys2.py",
    {
        "pf_keys2": pf_keys2,
    },
)

__all__ = [
    "pf_keys2",
]
