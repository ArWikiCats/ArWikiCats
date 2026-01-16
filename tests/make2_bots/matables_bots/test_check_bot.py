#!/usr/bin/python3
"""

from ..matables_bots.check_bot import check_key_new_players
check_key_new_players(key)
"""

import pytest

from ArWikiCats.legacy_bots.matables_bots.check_bot import check_key_new_players


@pytest.mark.fast
def test_1() -> None:
    result = check_key_new_players("actors")
    assert result is True
