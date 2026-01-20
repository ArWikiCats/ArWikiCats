"""

This module provides a mapping to handle categories where country names are used as nationalities

Example:
    (Category:New Zealand writers) instead of (Category:New Zealanders writers)

Reference:
    https://en.wikipedia.org/wiki/Wikipedia%3ACategory_names#How_to_name_a_nationality
    https://en.wikipedia.org/wiki/Category:People_by_occupation_and_nationality
    https://en.wikipedia.org/wiki/Category:People_by_nationality_and_occupation
"""

from ..helps import len_print
from ..translations import raw_nats_as_en_key

nats_keys_as_country_names = {
    "ireland": {
        "en_nat": "irish",
        "male": "أيرلندي",
        "males": "أيرلنديون",
        "female": "أيرلندية",
        "females": "أيرلنديات",
        "the_male": "الأيرلندي",
        "the_female": "الأيرلندية",
        "en": "ireland",
        "ar": "أيرلندا",
    },
    "georgia-country-nationality": {
        "male": "جورجي",
        "males": "جورجيون",
        "female": "جورجية",
        "females": "جورجيات",
        "the_male": "الجورجي",
        "the_female": "الجورجية",
        "en": "georgia (country)",
        "ar": "جورجيا",
    },
    "new zealand": {
        "en_nat": "new zealanders",
        "male": "نيوزيلندي",
        "males": "نيوزيلنديون",
        "female": "نيوزيلندية",
        "females": "نيوزيلنديات",
        "the_male": "النيوزيلندي",
        "the_female": "النيوزيلندية",
        "en": "new zealand",
        "ar": "نيوزيلندا",
    },
    "northern ireland": {
        "male": "أيرلندي شمالي",
        "males": "أيرلنديون شماليون",
        "female": "أيرلندية شمالية",
        "females": "أيرلنديات شماليات",
        "the_male": "الأيرلندي الشمالي",
        "the_female": "الأيرلندية الشمالية",
        "en": "northern ireland",
        "ar": "أيرلندا الشمالية",
    },
}

nats_keys_as_country_names.update(raw_nats_as_en_key)

len_print.data_len(
    "nats_as_country_names.py",
    {
        "nats_keys_as_country_names": nats_keys_as_country_names,
    },
)
