import pytest

from src.translations.utils.json_dir import open_json, open_json_file


def test_open_json_file_loads_from_nested_folder():
    data = open_json_file("us_counties")

    assert isinstance(data, dict)
    assert data  # sanity check that the fixture data is present


@pytest.mark.parametrize("path", ["peoples", "peoples.json"])
def test_open_json_appends_missing_suffix(path):
    assert open_json(path)
