#
import pytest

from ArWikiCats import resolve_label_ar
from ArWikiCats.new_resolvers.films_resolvers.resolve_films_labels_and_time import fetch_films_by_category
from utils.dump_runner import make_dump_test_name_data_callback

data_0 = {
    "Superhero film series navigational boxes": "صناديق تصفح سلاسل أفلام أبطال خارقين",
}

to_test = [
    ("test_superhero_data_to_fix1", data_0, resolve_label_ar),
]


@pytest.mark.parametrize("category, expected", data_0.items(), ids=data_0.keys())
@pytest.mark.skip2
def test_superhero_data_2(category: str, expected: str) -> None:
    result = fetch_films_by_category(category)
    assert result == expected


test_dump_all = make_dump_test_name_data_callback(to_test, run_same=True)
