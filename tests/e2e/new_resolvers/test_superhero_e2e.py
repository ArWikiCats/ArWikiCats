#
import pytest

from ArWikiCats import resolve_label_ar
from ArWikiCats.new_resolvers.films_resolvers.resolve_films_labels_and_time import fetch_films_by_category
from utils.dump_runner import make_dump_test_name_data_callback

data_0 = {
    "Superhero television characters by franchise": "أبطال خارقون تلفازيون حسب حق الامتياز",
    "DC Comics superhero teams": "فرق أبطال دي سي كومكس",
    "Superhero film series navigational boxes": "صناديق تصفح سلاسل أفلام أبطال خارقين",
    "Superheroes": "أبطال خارقون",
    "Superheroes in anime and manga": "أنمي ومانغا أبطال خارقين",
    "Superheroes by publisher": "أبطال خارقون حسب الناشر",
    "Superheroes by type": "أبطال خارقون حسب النوع",
    "Animal superheroes": "حيوانات أبطال خارقين",
    "Child superheroes": "أبطال خارقون أطفال",
    "Comics superheroes": "قصص مصورة حول أبطال خارقون",
    "DC Comics female superheroes": "بطلات دي سي كومكس الخارقات",
    "DC Comics superheroes": "أبطال دي سي كومكس",
    "Egyptian superheroes": "أبطال خارقون مصريون",
    "Golden Age superheroes": "أبطال العصر الذهبي",
    "Marvel Comics female superheroes": "بطلات مارفل كومكس الخارقات",
    "Marvel Comics superheroes": "أبطال خارقون في مارفل كومكس",
    "Muslim superheroes": "أبطال خارقون مسلمون",
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
