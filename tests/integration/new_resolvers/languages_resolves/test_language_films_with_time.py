"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers.languages_resolves import resolve_languages_labels_with_time

test_data_0 = {
    "2010s French language manga": "مانغا باللغة الفرنسية في عقد 2010",
    "2020 Arabic-language biographical drama films": "أفلام سير ذاتية درامية باللغة العربية في 2020",
    "2020s English-language biographical drama films": "أفلام سير ذاتية درامية باللغة الإنجليزية في عقد 2020",
    "3rd-century Latin-language films": "أفلام باللغة اللاتينية في القرن 3",
    "3rd-century BCE Latin-language films": "أفلام باللغة اللاتينية في القرن 3 ق م",
    "1st-millennium Latin-language films": "أفلام باللغة اللاتينية في الألفية 1",
}


@pytest.mark.parametrize("category, expected", test_data_0.items(), ids=test_data_0.keys())
@pytest.mark.fast
def test_language_films_with_time(category: str, expected: str) -> None:
    label2 = resolve_languages_labels_with_time(category)
    assert label2 == expected
