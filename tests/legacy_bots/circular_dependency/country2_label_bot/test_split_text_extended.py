"""
Extended tests for split_text_by_separator function covering additional edge cases.
"""

import pytest

from ArWikiCats.legacy_bots.legacy_resolvers_bots.country2_label_bot import (
    split_text_by_separator,
)

data_of_dash = {
    "kingdom-of italy (1789–1789)": ("kingdom of", "italy (1789–1789)"),
    "ministers-of foreign affairs of": ("ministers of", "foreign affairs of"),
    "ambassadors of federated states-of micronesia": ("ambassadors of federated states of", "micronesia"),
    "ambassadors of federated states of micronesia": ("", ""),
    "tourism in republic-of ireland": ("tourism in republic of", "ireland"),
}


data_of = {
    "ofyearsof of 16th ofcentury": ("ofyearsof of", "16th ofcentury"),
    "ambassadors of federated states of micronesia": ("ambassadors of", "federated states of micronesia"),
    "tourism in republic of ireland": ("tourism in republic of", "ireland"),
    "11th government of turkey": ("11th government of", "turkey"),
    "ambassadors of afghanistan": ("ambassadors of", "afghanistan"),
    "ambassadors of austria": ("ambassadors of", "austria"),
    "ambassadors of brazil": ("ambassadors of", "brazil"),
    "ambassadors of fiji": ("ambassadors of", "fiji"),
    "ambassadors of south africa": ("ambassadors of", "south africa"),
    "ambassadors of united states": ("ambassadors of", "united states"),
    "archaeology of europe": ("archaeology of", "europe"),
    "battles of napoleonic wars": ("battles of", "napoleonic wars"),
    "battles of vietnam war": ("battles of", "vietnam war"),
    "by province of saudi arabia": ("by province of", "saudi arabia"),
    "city of zagreb": ("city of", "zagreb"),
    "companies of georgia (country)": ("companies of", "georgia (country)"),
    "companies of southeast asia": ("companies of", "southeast asia"),
    "demographics of united states": ("demographics of", "united states"),
    "economy of united states": ("economy of", "united states"),
    "environment of united states": ("environment of", "united states"),
    "fauna of vermont": ("fauna of", "vermont"),
    "federalist party members of united states house-of-representatives": (
        "federalist party members of",
        "united states house-of-representatives",
    ),
    "fishes of europe": ("fishes of", "europe"),
    "former colleges of university of london": ("former colleges of", "university of london"),
    "geography of kansas": ("geography of", "kansas"),
    "geography of united states": ("geography of", "united states"),
    "german novels of 20th century": ("german novels of", "20th century"),
    "government of burkina faso": ("government of", "burkina faso"),
    "heads of universities and colleges": ("heads of", "universities and colleges"),
    "images of united states": ("images of", "united states"),
    "impact of covid-19 pandemic": ("impact of", "covid-19 pandemic"),
    "indigenous peoples of americas": ("indigenous peoples of", "americas"),
    "installations of united states air force": ("installations of", "united states air force"),
    "insular areas of united states": ("insular areas of", "united states"),
    "know-nothing members of united states house-of-representatives": (
        "know-nothing members of",
        "united states house-of-representatives",
    ),
    "lists of 1789 films": ("lists of", "1789 films"),
    "lists of ambassadors": ("lists of", "ambassadors"),
    "lists of bosnia and herzegovina people": ("lists of", "bosnia and herzegovina people"),
    "lists of british television series characters": ("lists of", "british television series characters"),
    "lists of buildings and structures": ("lists of", "buildings and structures"),
    "lists of country subdivisions": ("lists of", "country subdivisions"),
    "lists of football players": ("lists of", "football players"),
    "lists of legislators": ("lists of", "legislators"),
    "lists of mass media": ("lists of", "mass media"),
    "lists of mayors of places": ("lists of", "mayors of places"),
    "lists of roads": ("lists of", "roads"),
    "lists of television characters": ("lists of", "television characters"),
    "lists of universities and colleges": ("lists of", "universities and colleges"),
    "members of maine legislature": ("members of", "maine legislature"),
    "military operations of american civil war": ("military operations of", "american civil war"),
    "military operations of syrian civil war": ("military operations of", "syrian civil war"),
    "military operations of war": ("military operations of", "war"),
    "non-profit organizations of brazil": ("non-profit organizations of", "brazil"),
    "non-profit organizations of canada": ("non-profit organizations of", "canada"),
    "non-profit organizations of chile": ("non-profit organizations of", "chile"),
    "non-profit organizations of colombia": ("non-profit organizations of", "colombia"),
    "non-profit organizations of costa rica": ("non-profit organizations of", "costa rica"),
    "non-profit organizations of united kingdom": ("non-profit organizations of", "united kingdom"),
    "non-profit organizations of united states": ("non-profit organizations of", "united states"),
    "northern ireland of canadian descent": ("northern ireland of", "canadian descent"),
    "order of british empire": ("order of", "british empire"),
    "parliament of barbados": ("parliament of", "barbados"),
    "parliament of england 1789": ("parliament of", "england 1789"),
    "parliament of great britain": ("parliament of", "great britain"),
    "parliament of ireland 1550": ("parliament of", "ireland 1550"),
    "parliament of northern ireland 1789–1789": ("parliament of", "northern ireland 1789–1789"),
    "parliament of united kingdom": ("parliament of", "united kingdom"),
    "people accused of lèse majesté": ("people accused of", "lèse majesté"),
    "people associated with former colleges of university of london": (
        "people associated with former colleges of",
        "university of london",
    ),
    "people of dutch empire": ("people of", "dutch empire"),
    "permanent representatives of bahrain": ("permanent representatives of", "bahrain"),
    "permanent representatives of jamaica": ("permanent representatives of", "jamaica"),
    "permanent representatives of kazakhstan": ("permanent representatives of", "kazakhstan"),
    "permanent representatives of kyrgyzstan": ("permanent representatives of", "kyrgyzstan"),
    "persecution of lgbtq people": ("persecution of", "lgbtq people"),
    "politics of united states": ("politics of", "united states"),
    "prime ministers of japan": ("prime ministers of", "japan"),
    "prime ministers of malaysia": ("prime ministers of", "malaysia"),
    "prime ministers of ukraine": ("prime ministers of", "ukraine"),
    "protected areas of georgia (u.s. state)": ("protected areas of", "georgia (u.s. state)"),
    "protected areas of united states": ("protected areas of", "united states"),
    "rivers of united states": ("rivers of", "united states"),
    "society of united states": ("society of", "united states"),
    "tanks of united states": ("tanks of", "united states"),
    "the parliament of united kingdom": ("the parliament of", "united kingdom"),
    "university of galway": ("university of", "galway"),
    "university of sheffield": ("university of", "sheffield"),
    "verkhovna rada of ukrainian soviet socialist republic": (
        "verkhovna rada of",
        "ukrainian soviet socialist republic",
    ),
    "victims of aviation accidents or incidents": ("victims of", "aviation accidents or incidents"),
    "water of coquimbo region": ("water of", "coquimbo region"),
    "water of hambantota district": ("water of", "hambantota district"),
    "water of matale district": ("water of", "matale district"),
    "water of novosibirsk oblast": ("water of", "novosibirsk oblast"),
    "water of wilkes land": ("water of", "wilkes land"),
    "whig party members of united states house-of-representatives": (
        "whig party members of",
        "united states house-of-representatives",
    ),
    "years of 17th century": ("years of", "17th century"),
    "years of 18th century": ("years of", "18th century"),
    "years of 19th century": ("years of", "19th century"),
    "years of 20th century": ("years of", "20th century"),
    "years of 21st century": ("years of", "21st century"),
}


data_about = {
    "books about automobiles": ("books", "automobiles"),
    "books about politics": ("books", "politics"),
    "documentary films about the 2011 tōhoku earthquake and tsunami": (
        "documentary films",
        "the 2011 tōhoku earthquake and tsunami",
    ),
    "films about automobiles": ("films", "automobiles"),
    "films about olympic boxing": ("films", "olympic boxing"),
    "films about olympic figure skating": ("films", "olympic figure skating"),
    "films about olympic gymnastics": ("films", "olympic gymnastics"),
    "films about olympic skiing": ("films", "olympic skiing"),
    "films about olympic track and field": ("films", "olympic track and field"),
    "films about the olympic games": ("films", "the olympic games"),
    "films basedon non-fiction books about organized crime": ("films basedon non-fiction books", "organized crime"),
    "non-fiction books about acting": ("non-fiction books", "acting"),
    "non-fiction books about dogs": ("non-fiction books", "dogs"),
    "non-fiction books about the royal air force": ("non-fiction books", "the royal air force"),
    "non-fiction books about the sicilian mafia": ("non-fiction books", "the sicilian mafia"),
    "non-fiction books about the united states air force": ("non-fiction books", "the united states air force"),
    "non-fiction books about the united states navy": ("non-fiction books", "the united states navy"),
    "non-fiction novels about murders": ("non-fiction novels", "murders"),
    "non-fiction writers about organized crime": ("non-fiction writers", "organized crime"),
    "songs about automobiles": ("songs", "automobiles"),
    "songs about busan": ("songs", "busan"),
    "video games about diseases": ("video games", "diseases"),
    "video games about slavery": ("video games", "slavery"),
    "works about automobiles": ("works", "automobiles"),
}


data_by = {
    "-endings by year": ("-endings", "by year"),
    "1420 by country": ("1420", "by country"),
    "actors by religion": ("actors", "by religion"),
    "australian open by year – wheelchair ": ("australian open", "by year – wheelchair"),
    "british television series characters by series": ("british television series characters", "by series"),
    "by period by state": ("by period", "by state"),
    "european rugby union by country": ("european rugby union", "by country"),
    "football players by national team": ("football players", "by national team"),
    "french open by year – wheelchair ": ("french open", "by year – wheelchair"),
    "monarchs by country": ("monarchs", "by country"),
    "non-fiction writers by nationality": ("non-fiction writers", "by nationality"),
    "people by religion": ("people", "by religion"),
    "people from westchester county, new york by place holder": (
        "people from westchester county, new york",
        "by place holder",
    ),
    "television characters by series": ("television characters", "by series"),
    "television plays directed by william sterling (director)": (
        "television plays directed",
        "by william sterling (director)",
    ),
    "the united states by state": ("the united states", "by state"),
    "united states by state": ("united states", "by state"),
    "wheelchair sports competitors by nationality": ("wheelchair sports competitors", "by nationality"),
    "wheelchair track and field athletes by nationality": ("wheelchair track and field athletes", "by nationality"),
    "wheelchair users by nationality": ("wheelchair users", "by nationality"),
    "wimbledon championship by year – wheelchair ": ("wimbledon championship", "by year – wheelchair"),
}


data_from = {
    "actresses from ohio": ("actresses", "ohio"),
    "emigrants from the russian empire": ("emigrants", "the russian empire"),
    "expatriates from northern ireland": ("expatriates", "northern ireland"),
    "male actors from the west midlands (county)": ("male actors", "the west midlands (county)"),
    "non-fiction writers from northern ireland": ("non-fiction writers", "northern ireland"),
    "non-fiction writers from the russian empire": ("non-fiction writers", "the russian empire"),
    "people from al-andalus": ("people", "al-andalus"),
    "people from bangkok": ("people", "bangkok"),
    "people from batangas": ("people", "batangas"),
    "people from east lothian": ("people", "east lothian"),
    "people from west sumatra": ("people", "west sumatra"),
    "people from westchester county, new york": ("people", "westchester county, new york"),
    "rugby union players from west yorkshire": ("rugby union players", "west yorkshire"),
    "united kingdom from aden": ("united kingdom", "aden"),
    "united states house-of-representatives from missouri territory": (
        "united states house-of-representatives",
        "missouri territory",
    ),
    "wheelchair users from georgia (country)": ("wheelchair users", "georgia (country)"),
}


data_in = {
    "100 metres in the african championships in athletics": ("100 metres", "the african championships in athletics"),
    "100 metres in the iaaf world youth championships in athletics": (
        "100 metres",
        "the iaaf world youth championships in athletics",
    ),
    "100 metres in the world para athletics championships": ("100 metres", "the world para athletics championships"),
    "1550 in antigua and barbuda": ("1550", "antigua and barbuda"),
    "1550 in mexico": ("1550", "mexico"),
    "1550 in south america": ("1550", "south america"),
    "1550 in sports": ("1550", "sports"),
    "1550 in thailand": ("1550", "thailand"),
    "1550 in women's sport": ("1550", "women's sport"),
    "1550s in asia": ("1550s", "asia"),
    "1789 crimes in africa": ("1789 crimes", "africa"),
    "1789 elections in the united states": ("1789 elections", "the united states"),
    "1789 establishments in india": ("1789 establishments", "india"),
    "1789 in asian sport": ("1789", "asian sport"),
    "1789 in brazilian sport": ("1789", "brazilian sport"),
    "1789 in men's football": ("1789", "men's football"),
    "1789 in north america": ("1789", "north america"),
    "1789 in south america": ("1789", "south america"),
    "1789 in south american football": ("1789", "south american football"),
    "1789 in the united kingdom": ("1789", "the united kingdom"),
    "1789 in women's sport": ("1789", "women's sport"),
    "1789 in youth football": ("1789", "youth football"),
    "1994–95 in european rugby union": ("1994–95", "european rugby union"),
    "20th century in iraq": ("20th century", "iraq"),
    "anglican bishops in asia": ("anglican bishops", "asia"),
    "baseball players in florida": ("baseball players", "florida"),
    "baseball players in south korea": ("baseball players", "south korea"),
    "basketball players in lebanon": ("basketball players", "lebanon"),
    "bridges in france": ("bridges", "france"),
    "bridges in wales": ("bridges", "wales"),
    "buildings and structures in africa": ("buildings and structures", "africa"),
    "buildings and structures in georgia (u.s. state)": ("buildings and structures", "georgia (u.s. state)"),
    "buildings and structures in idaho": ("buildings and structures", "idaho"),
    "buildings and structures in prince edward island": ("buildings and structures", "prince edward island"),
    "buildings and structures in the united states": ("buildings and structures", "the united states"),
    "burials in washington (state)": ("burials", "washington (state)"),
    "by city in colombia": ("by city", "colombia"),
    "by city in northern-ireland": ("by city", "northern-ireland"),
    "by county in taiwan": ("by county", "taiwan"),
    "by educational institution in derbyshire": ("by educational institution", "derbyshire"),
    "by league in the united states": ("by league", "the united states"),
    "by newspaper in california": ("by newspaper", "california"),
    "by state in the united states": ("by state", "the united states"),
    "by team in the united states": ("by team", "the united states"),
    "by university or college in beijing": ("by university or college", "beijing"),
    "centuries in the united states": ("centuries", "the united states"),
    "christianity in the united states": ("christianity", "the united states"),
    "college men's wheelchair basketball teams in the united states": (
        "college men's wheelchair basketball teams",
        "the united states",
    ),
    "college women's wheelchair basketball teams in the united states": (
        "college women's wheelchair basketball teams",
        "the united states",
    ),
    "communications in the united states": ("communications", "the united states"),
    "crimes in peru": ("crimes", "peru"),
    "crimes in the united states": ("crimes", "the united states"),
    "decades in the united states": ("decades", "the united states"),
    "disasters in the united states": ("disasters", "the united states"),
    "disestablishments in ecuador": ("disestablishments", "ecuador"),
    "disestablishments in georgia (u.s. state)": ("disestablishments", "georgia (u.s. state)"),
    "disestablishments in yugoslavia": ("disestablishments", "yugoslavia"),
    "education in the united states": ("education", "the united states"),
    "establishments in guernsey": ("establishments", "guernsey"),
    "establishments in southeast asia": ("establishments", "southeast asia"),
    "ethnic groups in china": ("ethnic groups", "china"),
    "field hockey players in germany": ("field hockey players", "germany"),
    "food and drink in europe": ("food and drink", "europe"),
    "forts in the united states": ("forts", "the united states"),
    "health in the united states": ("health", "the united states"),
    "high schools in india": ("high schools", "india"),
    "historic districts in massachusetts": ("historic districts", "massachusetts"),
    "historic sites in the united states": ("historic sites", "the united states"),
    "historic trails and roads in the united states": ("historic trails and roads", "the united states"),
    "iaaf world youth championships in athletics": ("iaaf world youth championships", "athletics"),
    "landmarks in the united states": ("landmarks", "the united states"),
    "local politicians in the united kingdom": ("local politicians", "the united kingdom"),
    "manufacturing in the united states": ("manufacturing", "the united states"),
    "mass media in bosnia and herzegovina": ("mass media", "bosnia and herzegovina"),
    "mass media in morocco": ("mass media", "morocco"),
    "metres in the african championships in athletics": ("metres", "the african championships in athletics"),
    "metres in the iaaf world youth championships in athletics": (
        "metres",
        "the iaaf world youth championships in athletics",
    ),
    "metres in the world para athletics championships": ("metres", "the world para athletics championships"),
    "military operations of war in afghanistan (1789–1789)": ("military operations of war", "afghanistan (1789–1789)"),
    "national-register-of-historic-places in north carolina": (
        "national-register-of-historic-places",
        "north carolina",
    ),
    "nations in the summer olympics": ("nations", "the summer olympics"),
    "nature reserves in the united states": ("nature reserves", "the united states"),
    "netball in north america": ("netball", "north america"),
    "parks in south america": ("parks", "south america"),
    "people accused of lèse majesté in thailand since 2020": ("people accused of lèse majesté", "thailand since 2020"),
    "people accused of lèse majesté in thailand": ("people accused of lèse majesté", "thailand"),
    "populated places in latvia": ("populated places", "latvia"),
    "populated places in portugal": ("populated places", "portugal"),
    "populated places in uruguay": ("populated places", "uruguay"),
    "rail transport in sri lanka": ("rail transport", "sri lanka"),
    "railway stations in albania": ("railway stations", "albania"),
    "railway stations in austria": ("railway stations", "austria"),
    "railway stations in the united states": ("railway stations", "the united states"),
    "religion in the united states": ("religion", "the united states"),
    "riots and civil disorder in the united states": ("riots and civil disorder", "the united states"),
    "road incident deaths in the united states": ("road incident deaths", "the united states"),
    "saint kitts and nevis in the summer olympics": ("saint kitts and nevis", "the summer olympics"),
    "science and technology in the united states": ("science and technology", "the united states"),
    "shopping malls in ukraine": ("shopping malls", "ukraine"),
    "skyscrapers in the united arab emirates": ("skyscrapers", "the united arab emirates"),
    "slavery in the united states": ("slavery", "the united states"),
    "sport in the ottoman empire": ("sport", "the ottoman empire"),
    "sports governing bodies in north america": ("sports governing bodies", "north america"),
    "sports venues in australia": ("sports venues", "australia"),
    "sports-people in ireland": ("sports-people", "ireland"),
    "sports-people in västmanland county": ("sports-people", "västmanland county"),
    "synagogues in switzerland": ("synagogues", "switzerland"),
    "television plays filmed in brisbane": ("television plays filmed", "brisbane"),
    "the iaaf world youth championships in athletics": ("the iaaf world youth championships", "athletics"),
    "tourism in the united kingdom": ("tourism", "the united kingdom"),
    "tourist attractions in the united states": ("tourist attractions", "the united states"),
    "trade unions in the caribbean": ("trade unions", "the caribbean"),
    "transport infrastructure in south america": ("transport infrastructure", "south america"),
    "transportation buildings and structures in new hampshire": (
        "transportation buildings and structures",
        "new hampshire",
    ),
    "transportation in the united states": ("transportation", "the united states"),
    "unincorporated communities in alaska": ("unincorporated communities", "alaska"),
    "united nations in geneva": ("united nations", "geneva"),
    "universities and colleges in andhra pradesh": ("universities and colleges", "andhra pradesh"),
    "universities and colleges in ghana": ("universities and colleges", "ghana"),
    "universities and colleges in texas": ("universities and colleges", "texas"),
    "universities and colleges in ukraine": ("universities and colleges", "ukraine"),
    "universities and colleges in uruguay": ("universities and colleges", "uruguay"),
    "villages in north macedonia": ("villages", "north macedonia"),
    "volleyball competitions in asia": ("volleyball competitions", "asia"),
    "wheelchair basketball in 2020 asean para games": ("wheelchair basketball", "2020 asean para games"),
    "wheelchair basketball in the asean para games": ("wheelchair basketball", "the asean para games"),
    "wheelchair basketball players in turkey": ("wheelchair basketball players", "turkey"),
    "wheelchair fencing in 2020 asean para games": ("wheelchair fencing", "2020 asean para games"),
    "wheelchair fencing in the asean para games": ("wheelchair fencing", "the asean para games"),
    "wheelchair tennis in 2020 asean para games": ("wheelchair tennis", "2020 asean para games"),
    "wheelchair tennis in the asean para games": ("wheelchair tennis", "the asean para games"),
    "women's footballers in ireland": ("women's footballers", "ireland"),
    "years in the united states": ("years", "the united states"),
}

data_on = {
    "agricultural buildings and structures on the-national-register-of-historic-places": (
        "agricultural buildings and structures",
        "the-national-register-of-historic-places",
    ),
    "attacks on buildings and structures": ("attacks", "buildings and structures"),
    "attacks on diplomatic missions": ("attacks", "diplomatic missions"),
    "attacks on military installations": ("attacks", "military installations"),
    "bank buildings on the-national-register-of-historic-places": (
        "bank buildings",
        "the-national-register-of-historic-places",
    ),
    "buildings and structures on the-national-register-of-historic-places": (
        "buildings and structures",
        "the-national-register-of-historic-places",
    ),
    "clubhouses on the-national-register-of-historic-places": (
        "clubhouses",
        "the-national-register-of-historic-places",
    ),
    "courthouses on the-national-register-of-historic-places": (
        "courthouses",
        "the-national-register-of-historic-places",
    ),
    "military facilities on the-national-register-of-historic-places": (
        "military facilities",
        "the-national-register-of-historic-places",
    ),
    "opera houses on the-national-register-of-historic-places": (
        "opera houses",
        "the-national-register-of-historic-places",
    ),
    "railway stations on the-national-register-of-historic-places": (
        "railway stations",
        "the-national-register-of-historic-places",
    ),
}


data_to = {
    "ambassadors to the ottoman empire": ("ambassadors", "the ottoman empire"),
    "immigrants to new zealand": ("immigrants", "new zealand"),
    "immigration to europe": ("immigration", "europe"),
    "immigration to new zealand": ("immigration", "new zealand"),
    "immigration to the united states": ("immigration", "the united states"),
    "italian defectors to the soviet union": ("italian defectors", "the soviet union"),
    "treaties extended to curaçao": ("treaties extended", "curaçao"),
    "united states navy to the royal navy": ("united states navy", "the royal navy"),
}


data_based_in = {
    "organizations based in argentina": ("organizations", "argentina"),
    "organizations based in australia": ("organizations", "australia"),
    "organizations based in brazil": ("organizations", "brazil"),
    "organizations based in canada": ("organizations", "canada"),
    "organizations based in gabon": ("organizations", "gabon"),
}


@pytest.mark.fast
@pytest.mark.parametrize("category,expected", data_of_dash.items(), ids=data_of_dash.keys())
def test_data_of_dash(category: str, expected: tuple[str, str]) -> None:
    result: tuple[str, str] = split_text_by_separator(separator="-of ", country=category)

    assert result == expected


@pytest.mark.fast
@pytest.mark.parametrize("category,expected", data_about.items(), ids=data_about.keys())
def test_data_about(category: str, expected: tuple[str, str]) -> None:
    result: tuple[str, str] = split_text_by_separator(separator=" about ", country=category)
    assert result == expected


@pytest.mark.fast
@pytest.mark.parametrize("category,expected", data_by.items(), ids=data_by.keys())
def test_data_by(category: str, expected: tuple[str, str]) -> None:
    result: tuple[str, str] = split_text_by_separator(separator=" by ", country=category)
    assert result == expected


@pytest.mark.fast
@pytest.mark.parametrize("category,expected", data_from.items(), ids=data_from.keys())
def test_data_from(category: str, expected: tuple[str, str]) -> None:
    result: tuple[str, str] = split_text_by_separator(separator=" from ", country=category)
    assert result == expected


@pytest.mark.fast
@pytest.mark.parametrize("category,expected", data_in.items(), ids=data_in.keys())
def test_data_in(category: str, expected: tuple[str, str]) -> None:
    result: tuple[str, str] = split_text_by_separator(separator=" in ", country=category)
    assert result == expected


@pytest.mark.fast
@pytest.mark.parametrize("category,expected", data_of.items(), ids=data_of.keys())
def test_data_of(category: str, expected: tuple[str, str]) -> None:
    result: tuple[str, str] = split_text_by_separator(separator=" of ", country=category)
    assert result == expected


@pytest.mark.fast
@pytest.mark.parametrize("category,expected", data_on.items(), ids=data_on.keys())
def test_data_on(category: str, expected: tuple[str, str]) -> None:
    result: tuple[str, str] = split_text_by_separator(separator=" on ", country=category)
    assert result == expected


@pytest.mark.fast
@pytest.mark.parametrize("category,expected", data_to.items(), ids=data_to.keys())
def test_data_to(category: str, expected: tuple[str, str]) -> None:
    result: tuple[str, str] = split_text_by_separator(separator=" to ", country=category)
    assert result == expected


@pytest.mark.fast
@pytest.mark.parametrize("category,expected", data_based_in.items(), ids=data_based_in.keys())
def test_split_text_by_separator(category: str, expected: tuple[str, str]) -> None:
    result: tuple[str, str] = split_text_by_separator(separator=" based in ", country=category)
    assert result == expected
