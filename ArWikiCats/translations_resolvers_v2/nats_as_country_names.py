"""

This module provides a mapping to handle categories where country names are used as nationalities

Example:
    (Category:New Zealand writers) instead of (Category:New Zealanders writers)

Reference:
    https://en.wikipedia.org/wiki/Wikipedia%3ACategory_names#How_to_name_a_nationality
    https://en.wikipedia.org/wiki/Category:People_by_occupation_and_nationality
    https://en.wikipedia.org/wiki/Category:People_by_nationality_and_occupation
"""

nats_keys_as_country_names = {
    "ireland": {
        # "en_nat": "irish",
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
        # "en_nat": "georgians", #"georgian"
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
        # "en_nat": "new zealanders",
        "male": "نيوزيلندي",
        "males": "نيوزيلنديون",
        "female": "نيوزيلندية",
        "females": "نيوزيلنديات",
        "en": "new zealand",
        "ar": "نيوزيلندا",
        "the_female": "النيوزيلندية",
        "the_male": "النيوزيلندي"
    },
}
