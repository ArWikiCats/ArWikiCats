"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers.languages_resolves import resolve_languages_labels
from ArWikiCats.translations import LANGUAGE_TOPIC_FORMATS, language_key_translations

language_key_translations = {k: language_key_translations[k] for k in list(language_key_translations.keys())[:10]}

# A real language key that exists in language_key_translations
BASE_LANG = "abkhazian-language"
BASE_LANG_OUTPUT = "اللغة الأبخازية"


@pytest.mark.parametrize("suffix,template", LANGUAGE_TOPIC_FORMATS.items())
def testlang_key_m_patterns(suffix: str, template: str) -> None:
    # builds: "<lang> <suffix>"
    category = f"{BASE_LANG} {suffix}"
    result = resolve_languages_labels(category)

    # expected formatting
    expected = template.format(BASE_LANG_OUTPUT)

    assert result == expected, f"LANGUAGE_TOPIC_FORMATS mismatch for '{category}'\n {expected=}\nGot:      {result}"


def test_sample_direct_language() -> None:
    # from _languages_key
    assert resolve_languages_labels("abkhazian language") == "اللغة الأبخازية"
    assert resolve_languages_labels("afrikaans-language") == "اللغة الإفريقية"
    assert resolve_languages_labels("albanian languages") == "اللغات الألبانية"


def test_sample_lang_key_m_albums() -> None:
    # "albums": "ألبومات ب{}",
    result = resolve_languages_labels("abkhazian-language albums")
    assert result == "ألبومات باللغة الأبخازية"


def test_sample_lang_key_m_categories() -> None:
    # "categories": "تصنيفات {}",
    result = resolve_languages_labels("abkhazian-language categories")
    assert result == "تصنيفات اللغة الأبخازية"


def test_sample_lang_key_m_grammar() -> None:
    # "grammar": "قواعد اللغة ال{}",
    result = resolve_languages_labels("abkhazian-language grammar")
    assert result == "قواعد اللغة الأبخازية"


def test_romanization_pattern() -> None:
    # "romanization of"
    result = resolve_languages_labels("romanization of abkhazian")
    assert result == "رومنة اللغة الأبخازية"


def test_no_match() -> None:
    assert resolve_languages_labels("abkhazian-language unknown unknown") == ""
    assert resolve_languages_labels("xyz something") == ""
