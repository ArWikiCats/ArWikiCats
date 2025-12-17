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
        "en": "ireland",
        "ar": "أيرلندا",
        "the_female": "الأيرلندية",
        "the_male": "الأيرلندي"
    },
    "georgia (country)": {
        "en_nat": "georgians",
        "en_nat1": "georgian",
        "male": "جورجي",
        "males": "جورجيون",
        "female": "جورجية",
        "females": "جورجيات",
        "en": "georgia",
        "ar": "جورجيا",
        "the_female": "الجورجية",
        "the_male": "الجورجي"
    },
    "new zealand": {
        "en_nat": "new zealanders",
        "male": "نيوزيلندي",
        "males": "نيوزيلنديون",
        "female": "نيوزيلندية",
        "females": "نيوزيلنديات",
        "en": "new zealand",
        "ar": "نيوزيلندا",
        "the_female": "النيوزيلندية",
        "the_male": "النيوزيلندي"
    },
    "northern ireland": {
        "male": "أيرلندي شمالي",
        "males": "أيرلنديون شماليون",
        "female": "أيرلندية شمالية",
        "females": "أيرلنديات شماليات",
        "en": "northern ireland",
        "ar": "أيرلندا الشمالية",
        "the_female": "الأيرلندية الشمالية",
        "the_male": "الأيرلندي الشمالي"
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
        "the_male": "الأنتيغوي والبربودي"
    },
    "trinidad and tobago": {
        "en_nat": "trinidadian",
        "male": "ترنيدادي",
        "males": "ترنيداديون",
        "female": "ترنيدادية",
        "females": "ترنيداديات",
        "en": "trinidad and tobago",
        "ar": "ترينيداد وتوباغو",
        "the_female": "الترنيدادية",
        "the_male": "الترنيدادي"
    },
}

nats_keys_as_country_names.update(raw_nats_as_en_key)
