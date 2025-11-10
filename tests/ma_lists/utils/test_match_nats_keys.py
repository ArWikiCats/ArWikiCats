
import pytest
from src.ma_lists.utils.match_nats_keys import match_nat_key_old, match_nat_key


@pytest.mark.fast
def test_1() -> None:
    match_1 = match_nat_key_old("Yemeni national xoxo teams")
    match_2 = match_nat_key("Yemeni national xoxo teams")
    assert match_1 == "Yemeni"
    assert match_1 == match_2


@pytest.mark.fast
def test_2() -> None:
    match_1 = match_nat_key_old("2020 in South Yemeni national xoxo teams")
    match_2 = match_nat_key("2020 in South Yemeni national xoxo teams")
    assert match_1 == "South Yemeni"
    assert match_1 == match_2


@pytest.mark.fast
def test_3() -> None:
    match_1 = match_nat_key_old("finno-ugric national teams")
    match_2 = match_nat_key("finno-ugric national teams")
    assert match_1 == ""
    assert match_1 == match_2
