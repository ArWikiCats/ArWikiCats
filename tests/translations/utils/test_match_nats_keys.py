
import pytest
from src.translations.utils.match_nats_keys import match_nat_key


@pytest.mark.fast
def test_1() -> None:
    match_1 = match_nat_key("Yemeni national xoxo teams")
    assert match_1 == "Yemeni"


@pytest.mark.fast
def test_2() -> None:
    match_1 = match_nat_key("2020 in South Yemeni national xoxo teams")
    assert match_1 == "South Yemeni"


@pytest.mark.fast
def test_3() -> None:
    match_2 = match_nat_key("finno-ugric national teams")
    assert match_2 == ""
