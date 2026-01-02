"""
Tests
"""

import pytest

from ArWikiCats.make_bots.languages_bot.langs_w import (
    Films_key_For_nat,
    Lang_work,
)

# from ArWikiCats.make_bots.languages_bot.resolve_languages_new import resolve_languages_labels as Lang_work

Films_key_For_nat = {k: Films_key_For_nat[k] for k in list(Films_key_For_nat.keys())[:10]}

# A real language key that exists in language_key_translations
BASE_LANG = "abkhazian-language"
BASE_LANG_OUTPUT = "اللغة الأبخازية"


@pytest.mark.parametrize("suffix,template", Films_key_For_nat.items())
def testFilms_key_For_nat_patterns(suffix: str, template: str) -> None:
    category = f"{BASE_LANG} {suffix}"
    result = Lang_work(category)

    # Films_key_For_nat templates contain "{}" -> should become "ب<lang>"
    expected = template.format(f"ب{BASE_LANG_OUTPUT}")

    assert result == expected, f"Films_key_For_nat mismatch for '{category}'\n" f" {expected=}\n" f"Got:      {result}"
