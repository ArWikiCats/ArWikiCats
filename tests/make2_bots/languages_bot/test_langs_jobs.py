"""
Tests
"""

import pytest

from ArWikiCats.make_bots.languages_bot.langs_w import (
    Lang_work,
    jobs_mens_data,
)

# from ArWikiCats.make_bots.languages_bot.resolve_languages_new import resolve_languages_labels as Lang_work

# only 10 items from jobs_mens_data
jobs_mens_data = {k: jobs_mens_data[k] for k in list(jobs_mens_data.keys())[:10]}

# A real language key that exists in language_key_translations
BASE_LANG = "abkhazian-language"
BASE_LANG_OUTPUT = "اللغة الأبخازية"


@pytest.mark.parametrize("suffix,expected_label", jobs_mens_data.items())
def testjobs_mens_data_patterns(suffix: str, expected_label: str) -> None:
    category = f"{BASE_LANG} {suffix}"
    result = Lang_work(category)

    expected = f"{expected_label} ب{BASE_LANG_OUTPUT}"

    assert result == expected, f"jobs_mens_data mismatch for '{category}'\n" f" {expected=}\n" f"Got:      {result}"


def test_sample_jobs_mens_data() -> None:
    result = Lang_work("abkhazian-language writers")
    assert result == "كتاب باللغة الأبخازية"
