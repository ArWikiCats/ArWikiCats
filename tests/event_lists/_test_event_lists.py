#
from src import new_func_lab_final_label
from load_one_data import ye_test_one_dataset

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
    "category:1960s sex comedy films": "",
    "category:1970s sex comedy films": "",
    "category:2004 residency shows": "",
    "category:American track and field coaches": "",
    "category:Animals by period of description": "",
    "category:Association football players by B national team": "",
    "category:Comics publications": "",
    "category:County routes in Westchester County, New York": "",
    "category:Dutch Africanists": "",
    "category:Dystopian anime and manga": "",
    "category:EMI Latin artists": "",
    "category:Ecchi anime and manga": "",
    "category:Economy of Oceania by country": "",
    "category:Experimental film festivals": "",
    "category:Figure skating reality television participants": "",
    "category:Figure skating reality television series": "",
    "category:Films about Olympic equestrian sports": "",
    "category:Films based on works by comic book writers": "",
    "category:Financial services companies disestablished in 1905": "",
    "category:Fire departments in Westchester County, New York": "",
    "category:Geography of Africa by country": "",
    "category:Harem anime and manga": "",
    "category:Hentai anime and manga": "",
    "category:Historians of U.S. states": "",
    "category:History of association football clubs in the United Kingdom": "",
    "category:History of companies of the United Kingdom": "",
    "category:History of organisations based in England": "",
    "category:History of organisations based in Northern Ireland": "",
    "category:History of organisations based in Scotland": "",
    "category:History of organisations based in Wales": "",
    "category:History of organisations based in the United Kingdom": "",
    "category:History of rail transport in the United Kingdom": "",
    "category:Holding companies established in 1942": "",
    "category:Hong Kong national football team matches": "",
    "category:Illustrious Citizens of Buenos Aires": "",
    "category:Ireland international rules football team coaches": "",
    "category:January 2017 events by continent": "",
    "category:January 2017 events": "",
    "category:January 2017 sports events by country": "",
    "category:January 2017 sports events": "",
    "category:Labor relations in the United States by state": "",
    "category:Latin Grammy Lifetime Achievement Award winners": "",
    "category:Martial arts films by genre": "",
    "category:Military science fiction films": "",
    "category:National association football team managers": "",
    "category:New England states": "",
    "category:Organists of Ely Cathedral": "",
    "category:Outlines of U.S. states": "",
    "category:Peruvian documentary film directors": "",
    "category:Pre-statehood history of U.S. states": "",
    "category:Publishing companies disestablished in 1905": "",
    "category:Recipients of Afghan presidential pardons": "",
    "category:Residency shows by artist": "",
    "category:Residency shows in the Las Vegas Valley": "",
    "category:Rock en Español musicians": "",
    "category:Slice of life anime and manga": "",
    "category:State governments of the United States": "",
    "category:State law in the United States": "",
    "category:States of the United States history-related lists": "",
    "category:States of the United States-related lists": "",
    "category:Streetcar lines in Westchester County, New York": "",
    "category:Suspense anime and manga": "",
    "category:Timelines of states of the United States": "",
    "category:Tragedy anime and manga": "",
    "category:Ugandan": "",
    "category:United States Virgin Islands international soccer players": "",
    "category:United States historical societies by state": "",
    "category:United States men's international soccer players": "",
    "category:United States symbols by state": "",
    "category:United States wars by state": "",
    "category:Westchester County, New York politicians": "",
    "category:Western (genre) anime and manga": "",
    "category:Western (genre) films by genre": "",
    "category:Wildlife management areas by state": "",
    "category:Works about taxicabs": "",
    "category:Yaoi anime and manga": "",
    "category:Yuri (genre) anime and manga": "",
    "category:documentary filmmakers by nationality": "",
    "category:yemeni war filmmakers": ""
}


def new_func_lab_wrap(cat):
    result = new_func_lab_final_label(cat)

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
