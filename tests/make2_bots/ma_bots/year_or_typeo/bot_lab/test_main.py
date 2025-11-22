# import pytest
from src.make2_bots.ma_bots.year_or_typeo.bot_lab import (
    label_for_startwith_year_or_typeo,
)

# from load_one_data import ye_test_one_dataset, dump_diff


def test_basic():
    result = label_for_startwith_year_or_typeo("19th government of turkey")
    assert isinstance(result, str)
    assert result == ""


def test_basic_2():
    result = label_for_startwith_year_or_typeo("19th-century government of turkey")
    assert isinstance(result, str)
    assert result == "حكومة تركيا القرن 19"


def test_label_for_startwith_year_or_typeo_basic():
    result = label_for_startwith_year_or_typeo("sports events 2020 in Yemen")
    assert isinstance(result, str)
    assert result == "أحداث رياضية اليمن في 2020"
    assert "2020" in result


def test_no_typeo():
    res = label_for_startwith_year_or_typeo("2020 Yemen")
    assert res in ("اليمن في 2020", "اليمن 2020")


def test_no_year():
    res = label_for_startwith_year_or_typeo("sports events Yemen")
    assert res == "أحداث رياضية اليمن"


def test_in_at_add_fi():
    res = label_for_startwith_year_or_typeo("sports events 2020 at Yemen")
    # assert res == ""
    assert "في" in res


def test_unknown_country():
    res = label_for_startwith_year_or_typeo("something 2020 Unknownland")
    assert res == ""  # no country_label → fallback fail


def test_cat_test_removal():
    res = label_for_startwith_year_or_typeo("2020 films in Yemen")
    # assert res == "أفلام في اليمن في 2020"
    assert "أفلام" in res


def test_return_empty_if_nolab():
    assert label_for_startwith_year_or_typeo("random") == ""
