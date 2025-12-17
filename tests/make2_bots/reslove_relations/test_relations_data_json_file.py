import pytest
import json
from pathlib import Path
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.make_bots.reslove_relations.rele import resolve_relations_label

file_path = Path(__file__).parent / "relations_data.json"

big_data = json.loads(file_path.read_text(encoding="utf-8"))

TEMPORAL_CASES = [
]
# split big_data into patches of up to 2000 items each for TEMPORAL_CASES
CHUNK_SIZE = 2000

items = list(big_data.items())
for idx in range(0, len(items), CHUNK_SIZE):
    chunk_dict = dict(items[idx : idx + CHUNK_SIZE])
    name = f"patch_{idx // CHUNK_SIZE + 1}"
    TEMPORAL_CASES.append((name, chunk_dict))


@pytest.mark.parametrize("category, expected", big_data.items(), ids=big_data.keys())
@pytest.mark.slow
def test_resolve_relations_label_big_data(category: str, expected: str) -> None:
    label = resolve_relations_label(category)
    assert label == expected


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name: str, data: str) -> None:
    expected, diff_result = one_dump_test(data, resolve_relations_label)

    dump_diff(diff_result, f"test_resolve_relations_label_big_data_{name}")
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"
