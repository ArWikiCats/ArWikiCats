"""

This module provides a mapping to handle categories where country names are used as nationalities

Example:
    (Category:New Zealand writers) instead of (Category:New Zealanders writers)

Reference:
    https://en.wikipedia.org/wiki/Wikipedia%3ACategory_names#How_to_name_a_nationality
    https://en.wikipedia.org/wiki/Category:People_by_occupation_and_nationality
    https://en.wikipedia.org/wiki/Category:People_by_nationality_and_occupation
"""
from ..translations.nats.Nationality import raw_nats_as_en_key

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
    "georgia (country)": {
        "en_nat": "georgians",
        "en_nat1": "georgian",
        "male": "جورجي",
        "males": "جورجيون",
        "female": "جورجية",
        "females": "جورجيات",
        "the_male": "الجورجي",
        "the_female": "الجورجية",
        "en": "georgia",
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
    "antigua and barbuda": {
        "en_nat": "antiguan and barbudan",
        "en": "antigua and barbuda",
        "ar": "أنتيغوا وباربودا",
        "male": "أنتيغوي وبربودي",
        "males": "أنتيغويون وبربوديون",
        "female": "أنتيغوية وبربودية",
        "females": "أنتيغويات وبربوديات",
        "the_female": "الأنتيغوية والبربودية",
        "the_male": "الأنتيغوي والبربودي",
    },
    "trinidad and tobago": {
        "en_nat": "trinidadian",
        "male": "ترنيدادي",
        "males": "ترنيداديون",
        "female": "ترنيدادية",
        "females": "ترنيداديات",
        "the_male": "الترنيدادي",
        "the_female": "الترنيدادية",
        "en": "trinidad and tobago",
        "ar": "ترينيداد وتوباغو",
    },
}

nats_keys_as_country_names.update(raw_nats_as_en_key)

nats_keys_as_country_names_bad_keys = list(nats_keys_as_country_names.keys())

nats_keys_as_country_names_bad_keys.extend(
    [
        "federated states of micronesia",
        "republic of ireland",
        "republic-of ireland",
        "democratic-republic-of-congo",
        "democratic republic of congo",
        "dominican republic",
        "dominican republic",
        "republic of congo",
        "republic of congo",
        "republic-of ireland",
        "republic-of-congo",
        "republic of congo",
    ]
)
