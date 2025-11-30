import pytest

from ArWikiCats.translations.utils.json_dir import open_json, open_json_file


def test_open_json_file_loads_from_nested_folder() -> None:
    data = open_json_file("geography/us_counties")

    assert isinstance(data, dict)
    assert data  # sanity check that the fixture data is present


@pytest.mark.parametrize("path", ["people/peoples", "people/peoples.json"])
def test_open_json_appends_missing_suffix(path) -> None:
    assert open_json(path)
