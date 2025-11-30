"""
Tests
"""

import pytest

from ArWikiCats.make_bots.languages_bot.langs_w import (
    Films_key_For_nat,
    Lang_work,
    jobs_mens_data,
    lang_key_m,
    languages_key,
)

# only 10 items from jobs_mens_data
jobs_mens_data = {k: jobs_mens_data[k] for k in list(jobs_mens_data.keys())[:10]}
Films_key_For_nat = {k: Films_key_For_nat[k] for k in list(Films_key_For_nat.keys())[:10]}
languages_key = {k: languages_key[k] for k in list(languages_key.keys())[:10]}

# A real language key that exists in languages_key
BASE_LANG = "abkhazian-language"
BASE_LANG_OUTPUT = "اللغة الأبخازية"


@pytest.mark.parametrize("suffix,template", lang_key_m.items())
def testlang_key_m_patterns(suffix, template):
    # builds: "<lang> <suffix>"
    category = f"{BASE_LANG} {suffix}"
    result = Lang_work(category)

    # expected formatting
    expected = template.format(BASE_LANG_OUTPUT)

    assert result == expected, f"lang_key_m mismatch for '{suffix}'\n" f"Expected: {expected}\n" f"Got:      {result}"


@pytest.mark.parametrize("suffix,template", Films_key_For_nat.items())
def testFilms_key_For_nat_patterns(suffix, template):
    category = f"{BASE_LANG} {suffix}"
    result = Lang_work(category)

    # Films_key_For_nat templates contain "{}" -> should become "ب<lang>"
    expected = template.format(f"ب{BASE_LANG_OUTPUT}")

    assert result == expected, (
        f"Films_key_For_nat mismatch for '{suffix}'\n" f"Expected: {expected}\n" f"Got:      {result}"
    )


@pytest.mark.parametrize("lang,expected", languages_key.items())
def test_directlanguages_key_lookup(lang, expected) -> None:
    result = Lang_work(lang)
    assert result == expected, (
        f"languages_key lookup mismatch for '{lang}'\n" f"Expected: {expected}\n" f"Got:      {result}"
    )


@pytest.mark.parametrize("suffix,expected_label", jobs_mens_data.items())
def testjobs_mens_data_patterns(suffix, expected_label):
    category = f"{BASE_LANG} {suffix}"
    result = Lang_work(category)

    expected = f"{expected_label} ب{BASE_LANG_OUTPUT}"

    assert result == expected, (
        f"jobs_mens_data mismatch for '{suffix}'\n" f"Expected: {expected}\n" f"Got:      {result}"
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


def test_sample_jobs_mens_data() -> None:
    result = Lang_work("abkhazian-language writers")
    assert result == "كتاب باللغة الأبخازية"


def test_sample_jobs_discuss_throw() -> None:
    # "discus throw umpires": "حكام رمي قرص",
    result = Lang_work("abkhazian-language discus throw umpires")
    assert result == "حكام رمي قرص باللغة الأبخازية"


def test_sample_films_key_for_nat() -> None:
    result = Lang_work("arabic-language 3d anime films")
    assert result == "أفلام ثلاثية الأبعاد أنمي باللغة العربية"


def test_sample_films_drama() -> None:
    # "action drama films": "أفلام حركة درامية {}",
    result = Lang_work("abkhazian-language action drama films")
    assert result == "أفلام حركة درامية باللغة الأبخازية"


def test_romanization_pattern() -> None:
    # "romanization of"
    result = Lang_work("romanization of abkhazian")
    assert result == "رومنة لغة أبخازية"


def test_films_pattern_basic() -> None:
    # "<lang> films" (no suffix)
    result = Lang_work("abkhazian-language films")
    assert result == "أفلام باللغة الأبخازية"


def test_no_match() -> None:
    assert Lang_work("abkhazian-language unknown unknown") == ""
    assert Lang_work("xyz something") == ""
