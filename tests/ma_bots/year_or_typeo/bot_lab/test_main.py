# import pytest
from ArWikiCats.ma_bots2.year_or_typeo.bot_lab import (
    label_for_startwith_year_or_typeo,
)


def test_basic() -> None:
    result = label_for_startwith_year_or_typeo("19th government of turkey")
    assert isinstance(result, str)
    assert result == ""


def test_basic_2() -> None:
    result = label_for_startwith_year_or_typeo("19th-century government of turkey")
    assert isinstance(result, str)
    assert result == "حكومة تركيا القرن 19"


def test_label_for_startwith_year_or_typeo_basic() -> None:
    result = label_for_startwith_year_or_typeo("sports events 2020 in Yemen")
    assert isinstance(result, str)
    assert result == "أحداث رياضية اليمن في 2020"
    assert "2020" in result


def test_no_typeo() -> None:
    res = label_for_startwith_year_or_typeo("2020 Yemen")
    assert res in ("اليمن في 2020", "اليمن 2020")


def test_no_year() -> None:
    res = label_for_startwith_year_or_typeo("sports events Yemen")
    assert res == "أحداث رياضية اليمن"


def test_in_at_add_fi() -> None:
    res = label_for_startwith_year_or_typeo("sports events 2020 in Yemen")
    # assert res == ""
    assert "في" in res


def test_unknown_country() -> None:
    res = label_for_startwith_year_or_typeo("something 2020 Unknownland")
    assert res == ""  # no country_label → fallback fail


def test_cat_test_removal() -> None:
    res = label_for_startwith_year_or_typeo("2020 films in Yemen")
    # assert res == "أفلام في اليمن في 2020"
    assert "أفلام" in res


def test_return_empty_if_nolab() -> None:
    assert label_for_startwith_year_or_typeo("random") == ""
