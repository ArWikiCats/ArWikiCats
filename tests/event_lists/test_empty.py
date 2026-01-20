#
import pytest

from ArWikiCats import resolve_arabic_category_label

data = {
    "AFC Bournemouth-related lists": "z",
    "Annam (French protectorate)": "z",
    "Battles involving al-Shabaab (militant group)": "z",
    "Bison herds": "z",
    "CD Vitoria footballers": "z",
    "Cenotaphs": "z",
    "Copa Sudamericana–winning players": "z",
    "Crosses by function": "z",
    "Cúcuta Deportivo footballers": "z",
    "Divisiones Regionales de Fútbol players": "z",
    "Duck as food": "z",
    "EC Granollers players": "z",
    "Electricity ministers": "z",
    "Ethnic Somali people": "z",
    "Flora listed on CITES Appendix II": "z",
    "Fula clans": "z",
    "Fula history": "z",
    "GIGN missions": "z",
    "Gujarat Sultanate mosques": "z",
    "Helicopter attacks": "z",
    "Henry Benedict Stuart": "z",
    "HornAfrik Media Inc": "z",
    "Hussain Ahmad Madani": "z",
    "Lake fish of North America": "z",
    "Lakes of Cochrane District": "z",
    "Memorial crosses": "z",
    "Monotypic Tetragnathidae genera": "z",
    "Monuments of National Importance in Gujarat": "z",
    "Nigerian Fula people": "z",
    "Operations involving French special forces": "z",
    "Pahlavi architecture": "z",
    "Pan-Africanist political parties in Africa": "z",
    "Parliamentary elections in Somalia": "z",
    "People from Gopalganj District, Bangladesh": "z",
    "People with sexual sadism disorder": "z",
    "Ports and marine ministers of Somalia": "z",
    "Presidents of Khatumo": "z",
    "Primera Federación players": "z",
    "Prisoners sentenced to life imprisonment by Slovakia": "z",
    "Prodidominae": "z",
    "Royal monuments": "z",
    "Rõuge Parish": "z",
    "SD Eibar C players": "z",
    "Salvelinus": "z",
    "Sculptures by Antonio Canova": "z",
    "Sculptures of angels": "z",
    "Shia mosques in Iran": "z",
    "Skardu District": "z",
    "Slovak prisoners sentenced to life imprisonment": "z",
    "Socialism in the Gambia": "z",
    "Somali Youth League politicians": "z",
    "Syrian individuals subject to United Kingdom sanctions": "z",
    "Syrian individuals subject to the European Union sanctions": "z",
    "Taxa named by Anton Ausserer": "z",
    "Theraphosidae genera": "z",
    "Tongariro National Park": "z",
    "Tram transport in Europe": "z",
    "Women's rights in Slovakia": "z",
}

data_0 = {}


@pytest.mark.parametrize("category, expected", data_0.items(), ids=data_0.keys())
@pytest.mark.skip2
def test_empty(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected
