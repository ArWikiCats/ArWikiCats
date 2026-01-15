import json
from pathlib import Path

import pytest
from load_one_data import dump_diff, one_dump_test, dump_same_and_not_same

from ArWikiCats import resolve_label_ar
from ArWikiCats.make_bots import change_cat
from ArWikiCats.make_bots.reslove_relations.rele import resolve_relations_label
# from ArWikiCats.new_resolvers.relations_resolver import new_relations_resolvers


def _load_data(file_name, chunk_size=3000) -> list:
    file_path = Path(__file__).parent / file_name
    big_data = json.loads(file_path.read_text(encoding="utf-8"))

    TEMPORAL_CASES = []
    # split big_data into patches of up to CHUNK_SIZE items each for TEMPORAL_CASES

    items = list(big_data.items())
    for idx in range(0, len(items), chunk_size):
        chunk_dict = dict(items[idx : idx + chunk_size])

        chunk_dict = {change_cat(x): v for x, v in chunk_dict.items()}

        name = f"patch_{chunk_size}_item_number_{idx // chunk_size + 1}"
        TEMPORAL_CASES.append((name, chunk_dict))

    return TEMPORAL_CASES


TEMPORAL_CASES = _load_data("relations_data.json", 15000)


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name: str, data: str) -> None:
    expected, diff_result = one_dump_test(data, resolve_relations_label)
    dump_same_and_not_same(data, diff_result, name)
    dump_diff(diff_result, f"test_resolve_relations_label_big_data_{name}")
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"


TEMPORAL_CASES2 = _load_data("relations_data_empty.json", 4000)


@pytest.mark.parametrize("name,data", TEMPORAL_CASES2)
@pytest.mark.skip2
def test_empty_dump(name: str, data: str) -> None:
    # expected, diff_result = one_dump_test(data, resolve_label_ar)
    expected, diff_result = one_dump_test(data, resolve_relations_label)
    dump_same_and_not_same(data, diff_result, name)

    dump_diff(diff_result, f"test_resolve_relations_label_big_data_{name}")

    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
