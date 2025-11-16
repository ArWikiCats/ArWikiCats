
import pytest
from src.make2_bots.ma_bots.dodo_bots.event2bot_dodo import make_lab_dodo
# from load_one_data import ye_test_one_dataset, dump_diff


def test_make_lab_dodo_basic():

    result = make_lab_dodo("sports events 2020 in Yemen")
    assert isinstance(result, str)
    assert "2020" in result or "عام" in result


def test_no_typeo():

    res = make_lab_dodo("2020 Yemen")
    assert res in ("اليمن في 2020", "اليمن 2020")


def test_no_year():

    res = make_lab_dodo("sports events Yemen")
    assert res != ""  # still can generate


def test_in_at_add_fi():

    res = make_lab_dodo("sports events 2020 at Yemen")
    assert "في" in res


def test_unknown_country():

    res = make_lab_dodo("something 2020 Unknownland")
    assert res == ""  # no country_label → fallback fail


def test_cat_test_removal():

    res = make_lab_dodo("2020 films in Yemen")
    assert "أفلام" in res


def test_return_empty_if_nolab():

    assert make_lab_dodo("random") == ""
