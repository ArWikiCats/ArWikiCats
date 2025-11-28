"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test
from ArWikiCats.translations.geo.us_counties import (
    _STATE_SUFFIX_TEMPLATES_BASE,
    US_STATES_NAME_TRANSLATIONS,
)
from ArWikiCats.make_bots.p17_bots.us_stat import Work_US_State
from ArWikiCats.translations_resolvers.us_counties_new import resolve_us_states, normalize_state, us_states_new_keys

test_data = {
    "{en} in the War of 1812": "{ar} في حرب 1812",
    "{en} democrats": "ديمقراطيون من ولاية {ar}",
    "{en} lawyers": "محامون من ولاية {ar}",
    "{en} state court judges": "قضاة محكمة ولاية {ar}",
    "{en} state courts": "محكمة ولاية {ar}",
    "{en} state senators": "أعضاء مجلس شيوخ ولاية {ar}",
}

all_test_data = {}

for en, ar in US_STATES_NAME_TRANSLATIONS.items():  # 124 per state
    test_one = {
        x.format(en=en).lower(): normalize_state(v.format(ar=ar))
        for x, v in us_states_new_keys.items()
    }
    all_test_data.update(test_one)
    break

to_test = [
    ("test_Work_US_State_data", all_test_data, Work_US_State),
    # ("test_resolve_us_states", all_test_data, resolve_us_states),
]


@pytest.mark.parametrize("name,data,callback", to_test)
@pytest.mark.dump
def test_all_dump(name, data, callback):

    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"


@pytest.mark.parametrize("category, expected_key", all_test_data.items(), ids=list(all_test_data.keys()))
@pytest.mark.slow
def test_Work_US_State_data(category, expected_key) -> None:
    label1 = Work_US_State(category)
    assert label1.strip() == expected_key


@pytest.mark.parametrize("category, expected_key", all_test_data.items(), ids=list(all_test_data.keys()))
@pytest.mark.skip2
def test_resolve_us_states(category, expected_key) -> None:
    label2 = resolve_us_states(category)
    assert label2.strip() == expected_key
