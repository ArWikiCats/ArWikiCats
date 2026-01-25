""" """

from .helps import len_print
from .jobs import SINGERS_TAB
from .mixed.all_keys2 import (
    generate_key_mappings,
)
from .mixed.all_keys3 import (
    ALBUMS_TYPE,
    pop_final_3,
)
from .mixed.all_keys4 import new2019
from .mixed.keys2 import keys2_py
from .mixed.keys_23 import NEW_2023
from .mixed.Newkey import pop_final6
from .others.languages import (
    MEDIA_CATEGORY_TRANSLATIONS,
    language_key_translations,
)
from .sports import TENNIS_KEYS
from .tv.films_mslslat import (
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
