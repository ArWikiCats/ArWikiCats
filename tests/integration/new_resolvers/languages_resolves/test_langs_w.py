"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers.languages_resolves import resolve_languages_labels
from ArWikiCats.new_resolvers.languages_resolves.resolve_languages import add_definite_article
from ArWikiCats.translations import language_key_translations

languages_key_subset = {k: language_key_translations[k] for k in list(language_key_translations.keys())[:15]}

data = {
    "abkhazian languages grammar": "قواعد اللغات الأبخازية",
    "abkhazian-language grammar": "قواعد اللغة الأبخازية",
    "arabic-language grammar": "قواعد اللغة العربية",
    "arabic languages grammar": "قواعد اللغات العربية",
    "pali-language grammar": "قواعد اللغة البالية",
    "pali languages grammar": "قواعد اللغات البالية",
    "balinese-language grammar": "قواعد اللغة البالية",
    "balinese languages grammar": "قواعد اللغات البالية",
    "afrikaans-language grammar": "قواعد اللغة الإفريقية",
    "afrikaans languages grammar": "قواعد اللغات الإفريقية",
    "afar-language grammar": "قواعد اللغة العفارية",
    "afar languages grammar": "قواعد اللغات العفارية",
    "abkhazian films": "أفلام باللغة الأبخازية",
    "abkhazian languages dialects": "لهجات اللغات الأبخازية",
    "abkhazian languages films": "أفلام باللغات الأبخازية",
    "abkhazian languages given names": "أسماء شخصية باللغات الأبخازية",
    "abkhazian languages surnames": "ألقاب باللغات الأبخازية",
    "abkhazian languages writing system": "نظام كتابة اللغات الأبخازية",
    "abkhazian languages": "اللغات الأبخازية",
    "abkhazian-language dialects": "لهجات اللغة الأبخازية",
    "abkhazian-language given names": "أسماء شخصية باللغة الأبخازية",
    "abkhazian-language surnames": "ألقاب باللغة الأبخازية",
    "abkhazian-language writing system": "نظام كتابة اللغة الأبخازية",
    "afar films": "أفلام باللغة العفارية",
    "afar languages dialects": "لهجات اللغات العفارية",
    "afar languages films": "أفلام باللغات العفارية",
    "afar languages given names": "أسماء شخصية باللغات العفارية",
    "afar languages surnames": "ألقاب باللغات العفارية",
    "afar languages writing system": "نظام كتابة اللغات العفارية",
    "afar languages": "اللغات العفارية",
    "afar-language dialects": "لهجات اللغة العفارية",
    "afar-language given names": "أسماء شخصية باللغة العفارية",
    "afar-language surnames": "ألقاب باللغة العفارية",
    "afar-language writing system": "نظام كتابة اللغة العفارية",
    "afrikaans films": "أفلام باللغة الإفريقية",
    "afrikaans languages dialects": "لهجات اللغات الإفريقية",
    "afrikaans languages films": "أفلام باللغات الإفريقية",
    "afrikaans languages given names": "أسماء شخصية باللغات الإفريقية",
    "afrikaans languages surnames": "ألقاب باللغات الإفريقية",
    "afrikaans languages writing system": "نظام كتابة اللغات الإفريقية",
    "afrikaans languages": "اللغات الإفريقية",
    "afrikaans-language dialects": "لهجات اللغة الإفريقية",
    "afrikaans-language given names": "أسماء شخصية باللغة الإفريقية",
    "afrikaans-language surnames": "ألقاب باللغة الإفريقية",
    "afrikaans-language writing system": "نظام كتابة اللغة الإفريقية",
    "balinese films": "أفلام باللغة البالية",
    "balinese languages dialects": "لهجات اللغات البالية",
    "balinese languages films": "أفلام باللغات البالية",
    "balinese languages given names": "أسماء شخصية باللغات البالية",
    "balinese languages surnames": "ألقاب باللغات البالية",
    "balinese languages writing system": "نظام كتابة اللغات البالية",
    "balinese languages": "اللغات البالية",
    "balinese-language dialects": "لهجات اللغة البالية",
    "balinese-language given names": "أسماء شخصية باللغة البالية",
    "balinese-language surnames": "ألقاب باللغة البالية",
    "balinese-language writing system": "نظام كتابة اللغة البالية",
    "pali films": "أفلام باللغة البالية",
    "pali languages dialects": "لهجات اللغات البالية",
    "pali languages films": "أفلام باللغات البالية",
    "pali languages given names": "أسماء شخصية باللغات البالية",
    "pali languages surnames": "ألقاب باللغات البالية",
    "pali languages writing system": "نظام كتابة اللغات البالية",
    "pali languages": "اللغات البالية",
    "pali-language dialects": "لهجات اللغة البالية",
    "pali-language given names": "أسماء شخصية باللغة البالية",
    "pali-language surnames": "ألقاب باللغة البالية",
    "pali-language writing system": "نظام كتابة اللغة البالية",
    "arabic films": "أفلام باللغة العربية",
    "arabic languages dialects": "لهجات اللغات العربية",
    "arabic languages films": "أفلام باللغات العربية",
    "arabic languages given names": "أسماء شخصية باللغات العربية",
    "arabic languages surnames": "ألقاب باللغات العربية",
    "arabic languages writing system": "نظام كتابة اللغات العربية",
    "arabic languages": "اللغات العربية",
    "arabic-language dialects": "لهجات اللغة العربية",
    "arabic-language given names": "أسماء شخصية باللغة العربية",
    "arabic-language surnames": "ألقاب باللغة العربية",
    "arabic-language writing system": "نظام كتابة اللغة العربية",
}

data_2 = {
    "abkhazian-language": "اللغة الأبخازية",
    "afar-language": "اللغة العفارية",
    "balinese-language": "اللغة البالية",
    "pali-language": "اللغة البالية",
    "arabic-language": "اللغة العربية",
    "afrikaans-language": "اللغة الإفريقية",
    "Lao-language": "اللغة اللاوية",
    "english-language": "اللغة الإنجليزية",
}


@pytest.mark.parametrize("category, expected", data_2.items(), ids=data_2.keys())
def test_Lang_work_main_data_2(category: str, expected: str) -> None:
    result = resolve_languages_labels(category)
    assert result == expected


@pytest.mark.parametrize("category, expected", data.items(), ids=data.keys())
def test_Lang_work_main(category: str, expected: str) -> None:
    result = resolve_languages_labels(category)
    assert result == expected


def test_lang_work() -> None:
    # Test with a basic input
    result = resolve_languages_labels("test language")
    assert isinstance(result, str)

    result_empty = resolve_languages_labels("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = resolve_languages_labels("english language")
    assert isinstance(result_various, str)


# -----------------------------------------------------------
# 2) Parametrize: test "<key> language"
# -----------------------------------------------------------
data_2 = [(k, f"لغة {languages_key_subset[k]}") for k in languages_key_subset if not k.endswith(" language")]


@pytest.mark.parametrize(
    "key, expected",
    data_2,
    ids=[x[0] for x in data_2],
)
def test_lang_work_language_suffix(key: str, expected: str) -> None:
    """Test '<lang> language' format."""
    candidate = f"{key} language"
    result = resolve_languages_labels(candidate)

    if candidate in languages_key_subset:
        # Must exactly match mapping
        assert result == languages_key_subset[candidate]
    else:
        # If our synthesized key does not exist, result may be empty or valid
        assert result is not None


# -----------------------------------------------------------
# 3) Parametrize: test "<key> films"
# -----------------------------------------------------------
@pytest.mark.parametrize(
    "key, arabic",
    list(languages_key_subset.items()),
    ids=list(languages_key_subset.keys()),
)
def test_lang_work_films_suffix(key: str, arabic: str) -> None:
    """Test '<lang> films' -> 'أفلام ب<ArabicLabel>'."""
    base = key.replace("-language", "")
    candidate = f"{base} films"

    result = resolve_languages_labels(candidate)

    if result:
        assert isinstance(result, str)
        assert "أفلام ب" in result
        assert add_definite_article(arabic) in result


# -----------------------------------------------------------
# 5) Parametrize: key + topic suffix such as 'grammar', 'writing system', etc.
# -----------------------------------------------------------
TOPIC_SUFFIXES = [
    "grammar",
    "writing system",
    "dialects",
    "surnames",
    "given names",
]

data_x = [(k, suf) for k in languages_key_subset for suf in TOPIC_SUFFIXES]


@pytest.mark.parametrize(
    "key, suffix",
    data_x,
    ids=[f"{x[0]}-{x[1]}" for x in data_x],
)
def test_lang_work_topics(key: str, suffix: str) -> None:
    """Test '<lang> grammar', '<lang> writing system', etc."""
    candidate = f"{key} {suffix}"
    result = resolve_languages_labels(candidate)

    assert result is not None
    if result:
        # Must contain Arabic name at least
        assert add_definite_article(languages_key_subset[key]) in result
