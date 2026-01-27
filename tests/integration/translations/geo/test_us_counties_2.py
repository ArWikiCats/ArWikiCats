#
import pytest

from ArWikiCats import resolve_label_ar
from ArWikiCats.new_resolvers.countries_names_resolvers.us_states import normalize_state
from ArWikiCats.translations import US_STATES
from utils.dump_runner import make_dump_test_name_data

test_data = {
    "{en} in the War of 1812": "{ar} في حرب 1812",
    "{en} Democrats": "ديمقراطيون من ولاية {ar}",
    "{en} lawyers": "محامون من ولاية {ar}",
    "{en} state court judges": "قضاة محكمة ولاية {ar}",
    "{en} state courts": "محكمة ولاية {ar}",
    "{en} state senators": "أعضاء مجلس شيوخ ولاية {ar}",
}


washington_data = {
    "washington, d.c. Democrats": "ديمقراطيون من واشنطن العاصمة",
    "washington, d.c. lawyers": "محامون من واشنطن العاصمة",
    "washington, d.c. state court judges": "قضاة محكمة واشنطن العاصمة",
    "washington, d.c. state courts": "محكمة واشنطن العاصمة",
    "washington, d.c. state senators": "أعضاء مجلس شيوخ واشنطن العاصمة",
}

data_1 = {}
all_test_data = {}

for en, ar in US_STATES.items():
    test_one = {x.format(en=en): normalize_state(v.format(ar=ar)) for x, v in test_data.items()}
    data_1.setdefault(en, test_one)
    all_test_data.update(test_one)

data_1["washington, d.c."] = washington_data
all_test_data.update(washington_data)


@pytest.mark.parametrize("input_text,expected", all_test_data.items(), ids=all_test_data.keys())
@pytest.mark.slow
def test_all_data(input_text: str, expected: str) -> None:
    result = resolve_label_ar(input_text)
    assert result == expected


to_test = [(f"test_us_counties_{x}", v) for x, v in data_1.items()]

to_test.append(("test_all_test_data", all_test_data))

test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=False)
