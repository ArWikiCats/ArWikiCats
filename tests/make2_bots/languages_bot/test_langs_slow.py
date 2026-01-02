"""
Tests
"""

import pytest

from ArWikiCats.make_bots.languages_bot.langs_w import (  # Lang_work,
    LANGUAGE_TOPIC_FORMATS,
    language_key_translations,
)
from ArWikiCats.make_bots.languages_bot.resolve_languages_new import resolve_languages_labels as Lang_work

language_key_translations = {k: language_key_translations[k] for k in list(language_key_translations.keys())[:10]}

# A real language key that exists in language_key_translations
BASE_LANG = "abkhazian-language"
BASE_LANG_OUTPUT = "اللغة الأبخازية"


@pytest.mark.parametrize("suffix,template", LANGUAGE_TOPIC_FORMATS.items())
def testlang_key_m_patterns(suffix: str, template: str) -> None:
    # builds: "<lang> <suffix>"
    category = f"{BASE_LANG} {suffix}"
    result = Lang_work(category)

    # expected formatting
    expected = template.format(BASE_LANG_OUTPUT)

    assert result == expected, (
        f"LANGUAGE_TOPIC_FORMATS mismatch for '{category}'\n" f" {expected=}\n" f"Got:      {result}"
    )


@pytest.mark.parametrize("lang,expected", language_key_translations.items())
def test_directlanguages_key_lookup(lang: str, expected: str) -> None:
    result = Lang_work(lang)
    assert result == expected, (
        f"language_key_translations lookup mismatch for '{lang}'\n" f" {expected=}\n" f"Got:      {result}"
    )


def test_sample_direct_language() -> None:
    # from _languages_key
    assert Lang_work("abkhazian language") == "لغة أبخازية"
    assert Lang_work("afrikaans-language") == "اللغة الإفريقية"
    assert Lang_work("albanian languages") == "اللغات الألبانية"


def test_sample_lang_key_m_albums() -> None:
    # "albums": "ألبومات ب{}",
    result = Lang_work("abkhazian-language albums")
    assert result == "ألبومات باللغة الأبخازية"


def test_sample_lang_key_m_categories() -> None:
    # "categories": "تصنيفات {}",
    result = Lang_work("abkhazian-language categories")
    assert result == "تصنيفات اللغة الأبخازية"


def test_sample_lang_key_m_grammar() -> None:
    # "grammar": "قواعد اللغة ال{}",
    result = Lang_work("abkhazian-language grammar")
    assert result == "قواعد اللغة الأبخازية"


def test_sample_films_drama() -> None:
    # "action drama films": "أفلام حركة درامية {}",
    result = Lang_work("abkhazian-language action drama films")
    assert result == "أفلام حركة درامية باللغة الأبخازية"


def test_romanization_pattern() -> None:
    # "romanization of"
    result = Lang_work("romanization of abkhazian")
    assert result == "رومنة اللغة الأبخازية"


def test_films_pattern_basic() -> None:
    # "<lang> films" (no suffix)
    result = Lang_work("abkhazian-language films")
    assert result == "أفلام باللغة الأبخازية"


def test_no_match() -> None:
    assert Lang_work("abkhazian-language unknown unknown") == ""
    assert Lang_work("xyz something") == ""
