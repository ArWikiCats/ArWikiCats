#
from src import new_func_lab

from tests_lists import (
    OIUHNM2,
    Yell,
    indianalist,
    c21st_list,
    shar_list,
    impooor_list,
    manga_list,
    States_list,
    States2_list,
    States3_list,
)

empty = {
    "Category:1960s sex comedy films": "",
    "Category:1970s sex comedy films": "",
    "Category:2004 residency shows": "",
    "Category:American track and field coaches": "",
    "Category:Animals by period of description": "",
    "Category:Association football players by B national team": "",
    "Category:Comics publications": "",
    "Category:County routes in Westchester County, New York": "",
    "Category:Dutch Africanists": "",
    "Category:Dystopian anime and manga": "",
    "Category:EMI Latin artists": "",
    "Category:Ecchi anime and manga": "",
    "Category:Economy of Oceania by country": "",
    "Category:Experimental film festivals": "",
    "Category:Figure skating reality television participants": "",
    "Category:Figure skating reality television series": "",
    "Category:Films about Olympic equestrian sports": "",
    "Category:Films based on works by comic book writers": "",
    "Category:Financial services companies disestablished in 1905": "",
    "Category:Fire departments in Westchester County, New York": "",
    "Category:Geography of Africa by country": "",
    "Category:Harem anime and manga": "",
    "Category:Hentai anime and manga": "",
    "Category:Historians of U.S. states": "",
    "Category:History of association football clubs in the United Kingdom": "",
    "Category:History of companies of the United Kingdom": "",
    "Category:History of organisations based in England": "",
    "Category:History of organisations based in Northern Ireland": "",
    "Category:History of organisations based in Scotland": "",
    "Category:History of organisations based in Wales": "",
    "Category:History of organisations based in the United Kingdom": "",
    "Category:History of rail transport in the United Kingdom": "",
    "Category:Holding companies established in 1942": "",
    "Category:Hong Kong national football team matches": "",
    "Category:Illustrious Citizens of Buenos Aires": "",
    "Category:Ireland international rules football team coaches": "",
    "Category:January 2017 events by continent": "",
    "Category:January 2017 events": "",
    "Category:January 2017 sports events by country": "",
    "Category:January 2017 sports events": "",
    "Category:Labor relations in the United States by state": "",
    "Category:Latin Grammy Lifetime Achievement Award winners": "",
    "Category:Martial arts films by genre": "",
    "Category:Military science fiction films": "",
    "Category:National association football team managers": "",
    "Category:New England states": "",
    "Category:Organists of Ely Cathedral": "",
    "Category:Outlines of U.S. states": "",
    "Category:Peruvian documentary film directors": "",
    "Category:Pre-statehood history of U.S. states": "",
    "Category:Publishing companies disestablished in 1905": "",
    "Category:Recipients of Afghan presidential pardons": "",
    "Category:Residency shows by artist": "",
    "Category:Residency shows in the Las Vegas Valley": "",
    "Category:Rock en Español musicians": "",
    "Category:Slice of life anime and manga": "",
    "Category:State governments of the United States": "",
    "Category:State law in the United States": "",
    "Category:States of the United States history-related lists": "",
    "Category:States of the United States-related lists": "",
    "Category:Streetcar lines in Westchester County, New York": "",
    "Category:Suspense anime and manga": "",
    "Category:Timelines of states of the United States": "",
    "Category:Tragedy anime and manga": "",
    "Category:Ugandan": "",
    "Category:United States Virgin Islands international soccer players": "",
    "Category:United States historical societies by state": "",
    "Category:United States men's international soccer players": "",
    "Category:United States symbols by state": "",
    "Category:United States wars by state": "",
    "Category:Westchester County, New York politicians": "",
    "Category:Western (genre) anime and manga": "",
    "Category:Western (genre) films by genre": "",
    "Category:Wildlife management areas by state": "",
    "Category:Works about taxicabs": "",
    "Category:Yaoi anime and manga": "",
    "Category:Yuri (genre) anime and manga": "",
    "Category:documentary filmmakers by nationality": "",
    "Category:yemeni war filmmakers": ""
}


def new_func_lab_wrap(cat):
    result = new_func_lab(cat)

    if result and not result.startswith("تصنيف:"):
        result = f"تصنيف:{result}"

    return result


def ye_test_one_dataset(dataset):
    print(f"len of dataset: {len(dataset)}")
    org = {}
    diff = {}
    data = {x: v for x, v in dataset.items() if v}
    for cat, ar in data.items():
        result = new_func_lab_wrap(cat)
        if result == ar:
            assert result == ar
        else:
            org[cat] = ar
            diff[cat] = result

    assert org == diff


def test_OIUHNM2():
    ye_test_one_dataset(OIUHNM2)


def test_Yell():
    ye_test_one_dataset(Yell)


def test_indiana():
    ye_test_one_dataset(indianalist)


def test_21():
    ye_test_one_dataset(c21st_list)


def test_sh():
    ye_test_one_dataset(shar_list)


def test_imp():
    ye_test_one_dataset(impooor_list)


def test_manga():
    ye_test_one_dataset(manga_list)


def test_States():
    ye_test_one_dataset(States_list)


def test_States2():
    ye_test_one_dataset(States2_list)


def test_States3():
    ye_test_one_dataset(States3_list)
