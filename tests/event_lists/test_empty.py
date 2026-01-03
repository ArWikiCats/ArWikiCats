#
import pytest

from ArWikiCats import resolve_arabic_category_label

data = {
    "Category:AFC Bournemouth-related lists": "z",
    "Category:Annam (French protectorate)": "z",
    "Category:Battles involving al-Shabaab (militant group)": "z",
    "Category:Bison herds": "z",
    "Category:CD Vitoria footballers": "z",
    "Category:Cenotaphs": "z",
    "Category:Copa Sudamericana–winning players": "z",
    "Category:Crosses by function": "z",
    "Category:Cúcuta Deportivo footballers": "z",
    "Category:Divisiones Regionales de Fútbol players": "z",
    "Category:Duck as food": "z",
    "Category:EC Granollers players": "z",
    "Category:Electricity ministers": "z",
    "Category:Ethnic Somali people": "z",
    "Category:Flora listed on CITES Appendix II": "z",
    "Category:Fula clans": "z",
    "Category:Fula history": "z",
    "Category:GIGN missions": "z",
    "Category:Gujarat Sultanate mosques": "z",
    "Category:Helicopter attacks": "z",
    "Category:Henry Benedict Stuart": "z",
    "Category:HornAfrik Media Inc": "z",
    "Category:Hussain Ahmad Madani": "z",
    "Category:Lake fish of North America": "z",
    "Category:Lakes of Cochrane District": "z",
    "Category:Memorial crosses": "z",
    "Category:Monotypic Tetragnathidae genera": "z",
    "Category:Monuments of National Importance in Gujarat": "z",
    "Category:Nigerian Fula people": "z",
    "Category:Operations involving French special forces": "z",
    "Category:Pahlavi architecture": "z",
    "Category:Pan-Africanist political parties in Africa": "z",
    "Category:Parliamentary elections in Somalia": "z",
    "Category:People from Gopalganj District, Bangladesh": "z",
    "Category:People with sexual sadism disorder": "z",
    "Category:Ports and marine ministers of Somalia": "z",
    "Category:Presidents of Khatumo": "z",
    "Category:Primera Federación players": "z",
    "Category:Prisoners sentenced to life imprisonment by Slovakia": "z",
    "Category:Prodidominae": "z",
    "Category:Royal monuments": "z",
    "Category:Rõuge Parish": "z",
    "Category:SD Eibar C players": "z",
    "Category:Salvelinus": "z",
    "Category:Sculptures by Antonio Canova": "z",
    "Category:Sculptures of angels": "z",
    "Category:Shia mosques in Iran": "z",
    "Category:Skardu District": "z",
    "Category:Slovak prisoners sentenced to life imprisonment": "z",
    "Category:Socialism in the Gambia": "z",
    "Category:Somali Youth League politicians": "z",
    "Category:Syrian individuals subject to United Kingdom sanctions": "z",
    "Category:Syrian individuals subject to the European Union sanctions": "z",
    "Category:Taxa named by Anton Ausserer": "z",
    "Category:Theraphosidae genera": "z",
    "Category:Tongariro National Park": "z",
    "Category:Tram transport in Europe": "z",
    "Category:Women's rights in Slovakia": "z",
}

data_0 = {}


@pytest.mark.parametrize("category, expected", data_0.items(), ids=data_0.keys())
@pytest.mark.skip2
def test_empty(category: str, expected: str) -> None:
    label = resolve_arabic_category_label(category)
    assert label == expected
