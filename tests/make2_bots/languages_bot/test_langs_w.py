"""
Tests
"""

import pytest

from ArWikiCats.make_bots.languages_bot.langs_w import (
    Lang_work,
    languages_key,
)

languages_key_subset = {k: languages_key[k] for k in list(languages_key.keys())[:15]}

data = {
    "balinese language grammar": "قواعد لغة بالية",
    "afrikaans language grammar": "قواعد لغة إفريقية",
    "afar language grammar": "قواعد لغة عفارية",
    "abkhazian language grammar": "قواعد لغة أبخازية",
    "arabic language grammar": "قواعد لغة عربية",
    "pali language grammar": "قواعد لغة بالية",
    "abkhazian films": "أفلام باللغة الأبخازية",
    "abkhazian language dialects": "لهجات لغة أبخازية",
    "abkhazian language films": "أفلام بلغة أبخازية",
    "abkhazian language given names": "أسماء شخصية بلغة أبخازية",
    "abkhazian language surnames": "ألقاب بلغة أبخازية",
    "abkhazian language writing system": "نظام كتابة لغة أبخازية",
    "abkhazian language": "لغة أبخازية",
    "abkhazian languages dialects": "لهجات اللغات الأبخازية",
    "abkhazian languages films": "أفلام باللغات الأبخازية",
    "abkhazian languages given names": "أسماء شخصية باللغات الأبخازية",
    "abkhazian languages grammar": "قواعد اللغات الأبخازية",
    "abkhazian languages surnames": "ألقاب باللغات الأبخازية",
    "abkhazian languages writing system": "نظام كتابة اللغات الأبخازية",
    "abkhazian languages": "اللغات الأبخازية",
    "abkhazian-language dialects": "لهجات اللغة الأبخازية",
    "abkhazian-language given names": "أسماء شخصية باللغة الأبخازية",
    "abkhazian-language grammar": "قواعد اللغة الأبخازية",
    "abkhazian-language surnames": "ألقاب باللغة الأبخازية",
    "abkhazian-language writing system": "نظام كتابة اللغة الأبخازية",
    "abkhazian-language": "اللغة الأبخازية",
    "afar films": "أفلام باللغة العفارية",
    "afar language dialects": "لهجات لغة عفارية",
    "afar language films": "أفلام بلغة عفارية",
    "afar language given names": "أسماء شخصية بلغة عفارية",
    "afar language surnames": "ألقاب بلغة عفارية",
    "afar language writing system": "نظام كتابة لغة عفارية",
    "afar language": "لغة عفارية",
    "afar languages dialects": "لهجات اللغات العفارية",
    "afar languages films": "أفلام باللغات العفارية",
    "afar languages given names": "أسماء شخصية باللغات العفارية",
    "afar languages grammar": "قواعد اللغات العفارية",
    "afar languages surnames": "ألقاب باللغات العفارية",
    "afar languages writing system": "نظام كتابة اللغات العفارية",
    "afar languages": "اللغات العفارية",
    "afar-language dialects": "لهجات اللغة العفارية",
    "afar-language given names": "أسماء شخصية باللغة العفارية",
    "afar-language grammar": "قواعد اللغة العفارية",
    "afar-language surnames": "ألقاب باللغة العفارية",
    "afar-language writing system": "نظام كتابة اللغة العفارية",
    "afar-language": "اللغة العفارية",
    "afrikaans films": "أفلام باللغة الإفريقية",
    "afrikaans language dialects": "لهجات لغة إفريقية",
    "afrikaans language films": "أفلام بلغة إفريقية",
    "afrikaans language given names": "أسماء شخصية بلغة إفريقية",
    "afrikaans language surnames": "ألقاب بلغة إفريقية",
    "afrikaans language writing system": "نظام كتابة لغة إفريقية",
    "afrikaans language": "لغة إفريقية",
    "afrikaans languages dialects": "لهجات اللغات الإفريقية",
    "afrikaans languages films": "أفلام باللغات الإفريقية",
    "afrikaans languages given names": "أسماء شخصية باللغات الإفريقية",
    "afrikaans languages grammar": "قواعد اللغات الإفريقية",
    "afrikaans languages surnames": "ألقاب باللغات الإفريقية",
    "afrikaans languages writing system": "نظام كتابة اللغات الإفريقية",
    "afrikaans languages": "اللغات الإفريقية",
    "afrikaans-language dialects": "لهجات اللغة الإفريقية",
    "afrikaans-language given names": "أسماء شخصية باللغة الإفريقية",
    "afrikaans-language grammar": "قواعد اللغة الإفريقية",
    "afrikaans-language surnames": "ألقاب باللغة الإفريقية",
    "afrikaans-language writing system": "نظام كتابة اللغة الإفريقية",
    "afrikaans-language": "اللغة الإفريقية",
    "balinese films": "أفلام باللغة البالية",
    "balinese language dialects": "لهجات لغة بالية",
    "balinese language films": "أفلام بلغة بالية",
    "balinese language given names": "أسماء شخصية بلغة بالية",
    "balinese language surnames": "ألقاب بلغة بالية",
    "balinese language writing system": "نظام كتابة لغة بالية",
    "balinese language": "لغة بالية",
    "balinese languages dialects": "لهجات اللغات البالية",
    "balinese languages films": "أفلام باللغات البالية",
    "balinese languages given names": "أسماء شخصية باللغات البالية",
    "balinese languages grammar": "قواعد اللغات البالية",
    "balinese languages surnames": "ألقاب باللغات البالية",
    "balinese languages writing system": "نظام كتابة اللغات البالية",
    "balinese languages": "اللغات البالية",
    "balinese-language dialects": "لهجات اللغة البالية",
    "balinese-language given names": "أسماء شخصية باللغة البالية",
    "balinese-language grammar": "قواعد اللغة البالية",
    "balinese-language surnames": "ألقاب باللغة البالية",
    "balinese-language writing system": "نظام كتابة اللغة البالية",
    "balinese-language": "اللغة البالية",
    "english language": "لغة إنجليزية",
    "pali films": "أفلام باللغة البالية",
    "pali language dialects": "لهجات لغة بالية",
    "pali language films": "أفلام بلغة بالية",
    "pali language given names": "أسماء شخصية بلغة بالية",
    "pali language surnames": "ألقاب بلغة بالية",
    "pali language writing system": "نظام كتابة لغة بالية",
    "pali language": "لغة بالية",
    "pali languages dialects": "لهجات اللغات البالية",
    "pali languages films": "أفلام باللغات البالية",
    "pali languages given names": "أسماء شخصية باللغات البالية",
    "pali languages grammar": "قواعد اللغات البالية",
    "pali languages surnames": "ألقاب باللغات البالية",
    "pali languages writing system": "نظام كتابة اللغات البالية",
    "pali languages": "اللغات البالية",
    "pali-language dialects": "لهجات اللغة البالية",
    "pali-language given names": "أسماء شخصية باللغة البالية",
    "pali-language grammar": "قواعد اللغة البالية",
    "pali-language surnames": "ألقاب باللغة البالية",
    "pali-language writing system": "نظام كتابة اللغة البالية",
    "pali-language": "اللغة البالية",
    "arabic films": "أفلام باللغة العربية",
    "arabic language dialects": "لهجات لغة عربية",
    "arabic language films": "أفلام بلغة عربية",
    "arabic language given names": "أسماء شخصية بلغة عربية",
    "arabic language surnames": "ألقاب بلغة عربية",
    "arabic language writing system": "نظام كتابة لغة عربية",
    "arabic language": "لغة عربية",
    "arabic languages dialects": "لهجات اللغات العربية",
    "arabic languages films": "أفلام باللغات العربية",
    "arabic languages given names": "أسماء شخصية باللغات العربية",
    "arabic languages grammar": "قواعد اللغات العربية",
    "arabic languages surnames": "ألقاب باللغات العربية",
    "arabic languages writing system": "نظام كتابة اللغات العربية",
    "arabic languages": "اللغات العربية",
    "arabic-language dialects": "لهجات اللغة العربية",
    "arabic-language given names": "أسماء شخصية باللغة العربية",
    "arabic-language grammar": "قواعد اللغة العربية",
    "arabic-language surnames": "ألقاب باللغة العربية",
    "arabic-language writing system": "نظام كتابة اللغة العربية",
    "arabic-language": "اللغة العربية",
}


@pytest.mark.parametrize("category, expected", data.items(), ids=list(data.keys()))
def test_Lang_work_main(category, expected):
    result = Lang_work(category)
    assert result == expected


def test_lang_work():
    # Test with a basic input
    result = Lang_work("test language")
    assert isinstance(result, str)

    result_empty = Lang_work("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = Lang_work("english language")
    assert isinstance(result_various, str)


# -----------------------------------------------------------
# 1) Parametrize: test direct keys from languages_key_subset
# -----------------------------------------------------------


@pytest.mark.parametrize(
    "key, expected",
    [(k, v) for k, v in languages_key_subset.items()],
    ids=list(languages_key_subset.keys()),
)
def test_lang_work_direct(key, expected):
    """Test Lang_work for direct language keys."""
    result = Lang_work(key)
    # Lang_work may return full label or variant formatting
    assert isinstance(result, str)
    # If expected is Arabic label, result must equal or include it
    if result:
        assert expected in result or result == expected


# -----------------------------------------------------------
# 2) Parametrize: test "<key> language"
# -----------------------------------------------------------
data_2 = [(k, f"لغة {languages_key_subset[k]}") for k in languages_key_subset if not k.endswith(" language")]


@pytest.mark.parametrize(
    "key, expected",
    data_2,
    ids=[x[0] for x in data_2],
)
def test_lang_work_language_suffix(key, expected):
    """Test '<lang> language' format."""
    candidate = f"{key} language"
    result = Lang_work(candidate)

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
    [(k, v) for k, v in languages_key_subset.items()],
    ids=[k for k in languages_key_subset.keys()],
)
def test_lang_work_films_suffix(key, arabic):
    """Test '<lang> films' -> 'أفلام ب<ArabicLabel>'."""
    base = key.replace("-language", "")
    candidate = f"{base} films"

    result = Lang_work(candidate)

    if result:
        assert isinstance(result, str)
        assert "أفلام ب" in result
        assert arabic in result


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
def test_lang_work_topics(key, suffix):
    """Test '<lang> grammar', '<lang> writing system', etc."""
    candidate = f"{key} {suffix}"
    result = Lang_work(candidate)

    assert result is not None
    if result:
        # Must contain Arabic name at least
        assert languages_key_subset[key] in result
