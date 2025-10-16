#!/usr/bin/python3
r"""
python3 core8/pwb.py make/others/testmain nosql local testfile:fot
python3 core8/pwb.py make/others/testmain nosql local testfile:most
python3 core8/pwb.py make/others/testmain nosql local testfile:fd
python3 core8/pwb.py make/others/testmain nosql local testfile:uyu
python3 core8/pwb.py make/others/testmain nosql local testfile:nl
python3 core8/pwb.py make/others/testmain nosql local testfile:int
python3 core8/pwb.py make/others/testmain nosql local testfile:Healthcare
python3 core8/pwb.py make/others/testmain nosql local testfile:indor
python3 core8/pwb.py make/others/testmain nosql local testfile:22
python3 core8/pwb.py make/others/testmain nosql local testfile:hindus
python3 core8/pwb.py make/others/testmain nosql local testfile:new1txt
python3 core8/pwb.py make/others/testmain nosql local testfile:blind
python3 core8/pwb.py make/others/testmain nosql local testfile:occ limit:100

python -m cProfile -s ncalls  make/others/testmain.py nosql local testfile:yemen2
python3 core8/pwb.py make/others/testmain nosql file:c18/ennewtocreate.txt

in_\d\d\d\d$
in_2020

_(of|in)_(the united arab emirates|the republic of ireland|trinidad and tobago|the united states|the united kingdom|the soviet union|the sasanian empire|the ottoman empire|the dominican republic|the byzantine empire|republic of nauru|papua new guinea|federated states of micronesia|central african republic|bosnia and herzegovina|zulu people|western sahara|western canada|western asia|west india|west germany|the philippines|the gambia|são toméan|sri lanka|southwest asia|southern europe|southeast asia|south yemen|south sudan|south ossetia|south korea|south america|south africa|sierra leone|seychelles, the|saudi arabia|puerto rico|parthian empire|northern ireland|northern cyprus|north yemen|north macedonia|north korea|north america|north africa|nordic countries|new zealand|nazi germany|middle east|ivory coast|hong kong|georgia (country)|french guiana|faroe islanders|equatorial guinea|el salvador|eastern european|eastern asia|east timor|east germany|dominican republic|czech republic|costa rica|chinese taipei|central asia|central america|cape verde|burkina faso|austria hungary|ancient romania|ancient macedonia|ancient greece|african americans|zimbabwe|zambia|zaire|yugoslavia|yoruba|Rio de Janeiro state|Saarland|Wales|Netherlands|France|Italy)

(yemen|wales|vietnam|victoria australia|venezuela|vatican|vanuata|uzbekistan|uzbek|uruguay|ukraine|uganda|tuvalu|turkmenistan|turkmen|turkey|tunisia|tonga|togo|timor|the republic of the congo|thailand|tanzania|tajikistan|taiwan|syria|switzerland|sweden|swaziland|suriname|sudan|spain|somalia|slovenia|slovakia|singapore|serbia|senegal|scotland|samoa|rwanda|russia|romania|rhodesia|qatar|prussia|portugal|poland|philippines|peru|paraguay|panama|palestine|palau|pakistan|oman|oceania|norway|nigeria|niger|nicaragua|netherlands|nepal|namibia|muslims|mozambique|morocco|moravia|montenegro|mongolia|moldova|mexico|melanesia|mauritius|mauritania|malta|mali|maldives|malaysia|malawi|madagascar|macedonia|luxembourg|lithuania|liechtenstein|libya|liberia|lesotho|lebanon|latvia|laos|kyrgyzstan|kyrgyz|kuwait|kosovo|korea|kiribati|khazars|kenya|kazakhstan|kalmyks|jordan|jerusalem|japan|jamaica|italy|israel|iraq|iran|indonesia|india|iceland|hungary|honduras|hoklo|haiti|guyana|guinea bissau|guinea|guatemala|guam|guadeloupe|grenada|greenland|greece|gothic|gibraltar|ghana|germany|gabon|france|finland|fiji|europe|ethiopia|estonia|eritrea|england|egypt|ecuador|djibouti|denmark|democratic republic of the congo|czechoslovakia|cyprus|cuba|croatia|crimea|copts|congo|comoros|colombia|china|chile|chechens|chad|caucasus|caribbean|canada|cameroon|cambodia|burundi|burma|burkina|bulgaria|brazil|botswana|bolivia|bohemia|bhutan|benin|bengal|belize|belgium|belarus|barbados|bangladesh|bahrain|bahamas|azerbaijan|austria|australia|australasia|assyrian|asia|armenia|argentina|arab|appalachia|antilles|angola|andorra|america|algeria|albania|africa|afghanistan|abkhazia)


_(of|in)_(American Samoa|Angola|Antigua and Barbuda|Armenia|Aruba|Barbados|Bhutan|Botswana|Burkina Faso|Burundi|Cayman Islands|Chinese Taipei|Comoros|Cook Islands|Curaçao|Democratic Republic of the Congo|Dominica|Eswatini|Fiji|Gabon|Georgia \(country\)|Gibraltar|Guam|Guinea-Bissau|Hong Kong|Ivory Coast|Kyrgyzstan|Lesotho|Liechtenstein|Malawi|Maldives|Martinique|Mauritania|Mongolia|Myanmar|North Yemen|Republic of the Congo|Saint Kitts and Nevis|Saint Lucia|Seychelles|Solomon Islands|South Sudan|Suriname|Tahiti|Tajikistan|Tanzania|The Gambia|Togo|Tonga|Trinidad and Tobago|Uruguay|Yemen|United States|Costa Rica|New Zealand|Republic of Ireland|Panama|Afghanistan|Albania|Algeria|Argentina|Australia|Austria|Azerbaijan|Bahrain|Bangladesh|Belarus|Belgium|Bosnia and Herzegovina|Brazil|Bulgaria|Cambodia|Canada|Chile|China|Colombia|Costa Rica|Croatia|Cuba|Cyprus|Czechoslovakia|Denmark|Egypt|Estonia|Ethiopia|Finland|Germany|Greece|Hungary|Iceland|India|Indonesia|Iran|Iraq|Ireland|Israel|Italy|Jamaica|Japan|Jordan|Kenya|Korea|Kosovo|Kuwait|Latvia|Lebanon|Lithuania|Malaysia|Malta|Mauritius|Mexico|Moldova|Montenegro|Morocco|Mozambique|Namibia|Nepal|New Zealand|Nicaragua|Nigeria|North Macedonia|Norway|Pakistan|Peru|Poland|Portugal|Romania|Russia|Rwanda|Saudi Arabia|Senegal|Serbia|Singapore|Slovakia|Slovenia|South Africa|Spain|Sri Lanka|Sweden|Switzerland|Syria|Taiwan|Thailand|the Czech Republic|the Netherlands|the Philippines|the Russian Empire|the Soviet Union|the United Arab Emirates|the United Kingdom|the United States|Tunisia|Turkey|Ukraine|Uzbekistan|Venezuela|Vietnam|Yugoslavia|Zambia|Zimbabwe|England|Qatar)

$1_France

in_(Panama|Afghanistan)_by

in_France_by


"""

import re
import sys

sys.argv.append("printhead")
from pathlib import Path

from .. import printe
from ..memory import print_memory
from ..bot import event  # event(tab, **kwargs)

Dir = Path(__file__).parent.parent.parent
# ---
"""
python3 core8/pwb.py make/others/testmain nosql local testfile:Olympics
python3 core8/pwb.py make/others/testmain nosql local testfile:ae
python3 core8/pwb.py make/others/testmain nosql local testfile:nag
python3 core8/pwb.py make/others/testmain nosql local testfile:c2
python3 core8/pwb.py make/others/testmain nosql local testfile:pb
python3 core8/pwb.py make/others/testmain nosql local testfile:
python3 core8/pwb.py make/others/testmain nosql local testfile:yemen
python3 core8/pwb.py make/others/testmain nosql local testfile:yemen2
python3 core8/pwb.py make/others/testmain nosql local testfile:
python3 core8/pwb.py make/others/testmain nosql local testfile:
python3 core8/pwb.py make/others/testmain nosql local testfile:base
python3 core8/pwb.py make/others/testmain nosql local testfile:
python3 core8/pwb.py make/others/testmain nosql local testfile:e
python3 core8/pwb.py make/others/testmain nosql local testfile:in2
python3 core8/pwb.py make/others/testmain nosql local testfile:in
python3 core8/pwb.py make/others/testmain nosql local testfile:ma
python3 core8/pwb.py make/others/testmain nosql local testfile:ru
python3 core8/pwb.py make/others/testmain nosql local testfile:nato
python3 core8/pwb.py make/others/testmain nosql local testfile:covid20
python3 core8/pwb.py make/others/testmain nosql testfile:covid19 local
python3 core8/pwb.py make/others/testmain nosql testfile:ind local
python3 core8/pwb.py make/others/testmain nosql testfile:
python3 core8/pwb.py make/others/testmain nosql testfile:fe
python3 core8/pwb.py make/others/testmain nosql testfile:ws
python3 core8/pwb.py make/others/testmain nosql testfile:
python3 core8/pwb.py make/others/testmain nosql testfile:spo
python3 core8/pwb.py make/others/testmain nosql testfile:
python3 core8/pwb.py make/others/testmain nosql testfile:
python3 core8/pwb.py make/others/testmain nosql testfile:ws
python3 core8/pwb.py make/others/testmain nosql testfile:gaza
python3 core8/pwb.py make/others/testmain nosql testfile:ta
python3 core8/pwb.py make/others/testmain nosql testfile:bai
python3 core8/pwb.py make/others/testmain nosql testfile:nab
python3 core8/pwb.py make/others/testmain nosql testfile:poo
python3 core8/pwb.py make/others/testmain nosql testfile:una local
python3 core8/pwb.py make/others/testmain nosql testfile:2020
python3 core8/pwb.py make/others/testmain nosql testfile:
python3 core8/pwb.py make/others/testmain nosql testfile:player
python3 core8/pwb.py make/others/testmain nosql testfile:
python3 core8/pwb.py make/others/testmain nosql testfile:se
python3 core8/pwb.py make/others/testmain nosql testfile:
python3 core8/pwb.py make/others/testmain nosql testfile:ik
python3 core8/pwb.py make/others/testmain nosql testfile:most
python3 core8/pwb.py make/others/testmain nosql testfile:joe
python3 core8/pwb.py make/others/testmain nosql testfile:by
python3 core8/pwb.py make/others/testmain nosql testfile:ga
python3 core8/pwb.py make/others/testmain nosql testfile:congo
python3 core8/pwb.py make/others/testmain nosql testfile:covid3
python3 core8/pwb.py make/others/testmain nosql testfile:covid2
python3 core8/pwb.py make/others/testmain nosql testfile:covid
python3 core8/pwb.py make/others/testmain nosql testfile:sent
python3 core8/pwb.py make/others/testmain nosql testfile:fr
python3 core8/pwb.py make/others/testmain nosql testfile:fr2
python3 core8/pwb.py make/others/testmain nosql testfile:po
python3 core8/pwb.py make/others/testmain nosql testfile:gh
python3 core8/pwb.py make/others/testmain nosql testfile:z5
python3 core8/pwb.py make/others/testmain nosql testfile:z4
python3 core8/pwb.py make/others/testmain nosql testfile:z
python3 core8/pwb.py make/others/testmain nosql testfile:ddd
python3 core8/pwb.py make/others/testmain nosql testfile:koo5
python3 core8/pwb.py make/others/testmain nosql testfile:koo
python3 core8/pwb.py make/others/testmain nosql testfile:ppp
python3 core8/pwb.py make/others/testmain nosql testfile:fer
python3 core8/pwb.py make/others/testmain nosql testfile:ba
python3 core8/pwb.py make/others/testmain nosql testfile:ttt
python3 core8/pwb.py make/others/testmain nosql testfile:irl
python3 core8/pwb.py make/others/testmain nosql testfile:iq
python3 core8/pwb.py make/others/testmain nosql testfile:iz
python3 core8/pwb.py make/others/testmain nosql testfile:ass
python3 core8/pwb.py make/others/testmain nosql testfile:af
python3 core8/pwb.py make/others/testmain nosql testfile:co
python3 core8/pwb.py make/others/testmain nosql testfile:fan
python3 core8/pwb.py make/others/testmain nosql testfile:sing
python3 core8/pwb.py make/others/testmain nosql testfile:yya
python3 core8/pwb.py make/others/testmain nosql testfile:ya
python3 core8/pwb.py make/others/testmain nosql testfile:multin
python3 core8/pwb.py make/others/testmain nosql testfile:sea
python3 core8/pwb.py make/others/testmain nosql testfile:multi2
python3 core8/pwb.py make/others/testmain nosql testfile:multi
python3 core8/pwb.py make/others/testmain nosql testfile:cyf
python3 core8/pwb.py make/others/testmain nosql testfile:paper
python3 core8/pwb.py make/others/testmain nosql testfile:albums
python3 core8/pwb.py make/others/testmain nosql testfile:Joker
python3 core8/pwb.py make/others/testmain nosql testfile:jud
python3 core8/pwb.py make/others/testmain nosql testfile:ships3
python3 core8/pwb.py make/others/testmain nosql testfile:teams
python3 core8/pwb.py make/others/testmain nosql testfile:crr
python3 core8/pwb.py make/others/testmain nosql testfile:cyc
python3 core8/pwb.py make/others/testmain nosql testfile:muay
python3 core8/pwb.py make/others/testmain nosql testfile:mi
python3 core8/pwb.py make/others/testmain nosql testfile:us
python3 core8/pwb.py make/others/testmain nosql testfile:28
python3 core8/pwb.py make/others/testmain nosql testfile:india
python3 core8/pwb.py make/others/testmain nosql testfile:it
python3 core8/pwb.py make/others/testmain nosql testfile:can
python3 core8/pwb.py make/others/testmain nosql testfile:pro
python3 core8/pwb.py make/others/testmain nosql testfile:mo
python3 core8/pwb.py make/others/testmain nosql testfile:cy
python3 core8/pwb.py make/others/testmain nosql testfile:usa
python3 core8/pwb.py make/others/testmain nosql testfile:vf
python3 core8/pwb.py make/others/testmain nosql testfile:uu
python3 core8/pwb.py make/others/testmain nosql testfile:i
python3 core8/pwb.py make/others/testmain nosql testfile:fis
python3 core8/pwb.py make/others/testmain nosql testfile:mn
python3 core8/pwb.py make/others/testmain nosql testfile:jobs
python3 core8/pwb.py make/others/testmain nosql testfile:un
python3 core8/pwb.py make/others/testmain nosql testfile:rt
python3 core8/pwb.py make/others/testmain nosql testfile:uiu
python3 core8/pwb.py make/others/testmain nosql testfile:sri
python3 core8/pwb.py make/others/testmain nosql testfile:play
python3 core8/pwb.py make/others/testmain nosql testfile:ts
python3 core8/pwb.py make/others/testmain nosql testfile:names
python3 core8/pwb.py make/others/testmain nosql testfile:football
python3 core8/pwb.py make/others/testmain nosql testfile:am
python3 core8/pwb.py make/others/testmain nosql testfile:do
python3 core8/pwb.py make/others/testmain nosql testfile:tax
python3 core8/pwb.py make/others/testmain nosql testfile:c
python3 core8/pwb.py make/others/testmain nosql testfile:works
python3 core8/pwb.py make/others/testmain nosql testfile:ng
python3 core8/pwb.py make/others/testmain nosql testfile:cdcd
python3 core8/pwb.py make/others/testmain nosql testfile:ss
python3 core8/pwb.py make/others/testmain nosql testfile:singers
python3 core8/pwb.py make/others/testmain nosql testfile:so
python3 core8/pwb.py make/others/testmain nosql testfile:fra
python3 core8/pwb.py make/others/testmain nosql testfile:su
python3 core8/pwb.py make/others/testmain nosql testfile:ww
python3 core8/pwb.py make/others/testmain nosql testfile:20
python3 core8/pwb.py make/others/testmain nosql testfile:2018
python3 core8/pwb.py make/others/testmain nosql testfile:xd
python3 core8/pwb.py make/others/testmain nosql testfile:people
python3 core8/pwb.py make/others/testmain nosql testfile:o
python3 core8/pwb.py make/others/testmain nosql testfile:ada
python3 core8/pwb.py make/others/testmain nosql testfile:h
python3 core8/pwb.py make/others/testmain nosql testfile:ii
python3 core8/pwb.py make/others/testmain nosql testfile:films
python3 core8/pwb.py make/others/testmain nosql testfile:sport
python3 core8/pwb.py make/others/testmain nosql testfile:io
python3 core8/pwb.py make/others/testmain nosql testfile:jv
python3 core8/pwb.py make/others/testmain nosql testfile:amr
python3 core8/pwb.py make/others/testmain nosql testfile:ip
python3 core8/pwb.py make/others/testmain nosql testfile:dd
python3 core8/pwb.py make/others/testmain nosql testfile:r
python3 core8/pwb.py make/others/testmain nosql testfile:ff
python3 core8/pwb.py make/others/testmain nosql testfile:j
"""
# ---
# python3 core8/pwb.py make/others/testmain nosql te:Assa
# python3 core8/pwb.py make/others/testmain nosql te:Assa2
# python3 core8/pwb.py make/others/testmain nosql te:am
# python3 core8/pwb.py make/others/testmain nosql te:misic
# python3 core8/pwb.py make/others/testmain nosql te:l
# python3 core8/pwb.py make/others/testmain nosql te:iii
# python3 core8/pwb.py make/others/testmain nosql te:foot
# python3 core8/pwb.py make/others/testmain nosql te:fe
# python3 core8/pwb.py make/others/testmain nosql te:D
# python3 core8/pwb.py make/others/testmain nosql te:mo
# python3 core8/pwb.py make/others/testmain nosql te:op
# python3 core8/pwb.py make/others/testmain nosql te:oil
# python3 core8/pwb.py make/others/testmain nosql te:new
# python3 core8/pwb.py make/others/testmain nosql te:tennis
# python3 core8/pwb.py make/others/testmain nosql te:ye1
# python3 core8/pwb.py make/others/testmain nosql te:19
# python3 core8/pwb.py make/others/testmain nosql te:ye2
# python3 core8/pwb.py make/others/testmain nosql te:ddd
#
# python3 core8/pwb.py make/others/testmain nosql file:textfiles/ennewtocreate.txt
# python3 core8/pwb.py make/others/testmain nosql testfile:yemen
# python3 core8/pwb.py make/others/testmain nosql testfile:india
# python3 core8/pwb.py make/others/testmain nosql testfile:elph2
# python3 core8/pwb.py make/others/testmain nosql testfile:elph
# python3 core8/pwb.py make/others/testmain nosql testfile:military
#
# python3 core8/pwb.py make/others/testmain nosql testfile:winter
# python3 core8/pwb.py make/others/testmain nosql testfile:z
# python3 core8/pwb.py make/others/testmain nosql testfile:nn
# python3 core8/pwb.py make/others/testmain nosql testfile:Businesspeople
# ---
test_table = {}
# ---
oo_list = [
    "Category:Philippine films by subgenre",
    "Category:Action films by genre",
    "Category:Songs_written_by_Bob_Dylan",
    "Category:Adventure films by genre",
    "Category:Comedy films by genre",
    "Category:Crime films by genre",
    "Category:Documentary films by genre",
    "Category:Drama films by genre",
    "Category:Erotic films by genre",
    "Category:Fantasy films by genre",
    "Category:Horror films by genre",
    "Category:LGBT-related films by genre",
    "Category:Martial arts films by genre",
    "Category:Musical films by genre",
    "Category:Mystery films by genre",
    "Category:Political films by genre",
    "Category:Pornographic films by genre",
    "Category:Romance films by genre",
    "Category:Science fiction films by genre",
    "Category:Sports films by genre",
    "Category:Spy films by genre",
    "Category:Teen films by genre",
    "Category:Thriller films by genre",
    "Category:War films by genre",
    "Category:Western (genre) films by genre",
]


def Add_tab():
    # ---
    vtittable2 = [
        "Category:films by country",
        "Category:Destroyed churches by country",
        "Category:Nuclear power by country",
        "Category:Handball competitions by country",
        "Category:Road bridges by country",
        "Category:Television stations by country",
        "Category:Mystery films by country",
        "Category:Decades in Oklahoma",
        "Category:Decades by country",
        "Category:parks in the Roman Empire",
        "Category:Economy of Oceania by country",
        "Category:landmarks in Yemen",
        "Category:Geography of Africa by country",
    ]
    # ---
    New_Month_list2 = [
        "Category:films by country",
        "Category:Destroyed churches by country",
        "Category:Mystery films by country",
        "Category:Decades in Oklahoma",
        "Category:2017 sports events",
        "Category:2017 events",
        "Category:January 2017 sports events by country",
        "Category:April 1983 events in Europe",
        "Category:January 2017 events",
        "Category:January 2017 sports events",
        "Category:977 by country",
        "Category:2017 events by country",
        "Category:2006 establishments by country",
        "Category:1000 disestablishments by country",
        "Category:20th-century disestablishments in India",
        "Category:14th-century establishments in India",
    ]
    # ---
    test_ll = [
        "Category:440s bc",
        "Category:440s",
        "Category:ugandan football",
        "Category:Ugandan",
        "Category:IndyCar",
        "Category:1370s conflicts",
        "Category:Drama_films_by_country",
        "Category:2015_American_television",
        "Category:21st-century in Qatar",
        "Category:1270s in the Holy Roman Empire",
        "Category:2017_in_Emirati_football",
        "Category:2017–18_in_Emirati_football",
        "Category:football_in_2050–51",
        "Category:2017_in_Emirati_football",
        "Category:Emirati_football_in_2017–18",
        "Category:Emirati_football_in_2017",
        "Category:2017_in_Emirati_football",
        "Category:2017_in_Emirati_football",
        "Category:November 2006 in Yemen",
        "Category:21st century in the Czech Republic",
        "Category:American_cinema_by_decade",
    ]
    # ---
    tittable2 = [
        "films by country",
        "Category:Destroyed churches by country",
        "Category:Nuclear power by country",
        "Category:Handball competitions by country",
        "Category:Road bridges by country",
        "Category:Television stations by country",
        "Category:Mystery films by country",
        "Category:Decades in Oklahoma",
        "Category:Decades by country",
        "Category:parks in the Roman Empire",
        "Category:Economy of Oceania by country",
        "Category:Geography of Africa by country",
        "Category:2000s in the United States by state",
        "Category:10th millennium in fiction",
        "Category:2017 sports events",
        "Category:2017 events",
        "Category:January 2017 sports events by country",
        "Category:April 1983 sports events",
        "Category:April 1983 events in Europe",
        "Category:January 2017 events",
        "Category:January 2017 events by continent",
        "Category:January 2017 sports events",
        "Category:1980 sports events in Europe",
        "Category:1000 disestablishments in Europe",
        "Category:1990s disestablishments in Europe",
        "Category:1990s BC disestablishments in Asia",
        "Category:1000s disestablishments in Asia",
        "Category:00s establishments in the Roman Empire",
        "Category:13th century establishments in the Roman Empire",
        "Category:977 by country",
        "Category:2017 events by country",
        "Category:2006 establishments by country",
        "Category:1000 disestablishments by country",
    ]
    #
    dd2 = [
        "Category:Films by city",  # ١ ت)
        "Category:Films by country",  # ٢٢٩ ت)
        "Category:Films by language",  # ٢١٦ ت)
        "Category:Films by audience",  # ٣ ت)
        "Category:Films by continent",  # ٩ ت)
        "Category:Films by culture",  # ١٧ ت)
        "Category:Films by date",  # ٦ ت)
        "Category:Films by director",  # ٧٬٠١٧ ت)
        "Category:Films by genre",  # ٨٥ ت)
        "Category:Films by movement",  # ٥ ت)
        "Category:Films by producer",  # ٣١٢ ت)
        "Category:Films by setting",  # ٣٤ ت)
        "Category:Films by shooting location",  # ٦ ت)
        "Category:Films by source",  # ١٧ ت، ١ ص)
        "Category:Films by studio",  # ١١٨ ت، ١ ص)
        "Category:Films by technology",  # ٢٠ ت)
        "Category:Films by topic",  # ٧٨ ت، ٢ ص)
        "Category:Films by type",  # ٤٠ ت، ٩ ص)
    ]
    # ---
    Ambassadors = [
        "Category:Ambassadors_of_Afghanistan",
        "Category:Ambassadors_of_Afghanistan_to_Argentina",
        "Category:Ambassadors_of_Afghanistan_to_Australia",
        "Category:Afghan_diplomats",
        "Category:Ambassadors_by_country_of_origin",
        "Category:Afghan_expatriates",
        "Category:Ivorian_diaspora_by_country",
        "Category:Ivorian_diaspora_in_Asia",
        "Category:People_of_Ivorian_descent",
        "Category:People_of_Ivorian_descent",
        "Category:Ivorian_emigrants",
        "Category:Ivorian_expatriates",
        "Category:Ivorian_American",
        "Category:Ambassadors_to_the_Ottoman_Empire",
        "Category:Ambassadors_of_the_Ottoman_Empire",
        "Category:Ambassadors_by_mission_country",
        "Category:People_by_former_country",
        "Category:Ambassadors_by_mission_country",
        "Category:Attacks_on_diplomatic_missions",
        "",
    ]
    # ---
    ddd = ["Category:2017_American_television_seasons", "Category:2017_American_television_series_endings", "Category:2017_American_television_episodes", "Category:American_television_episodes", "Category:2017_American_television_series_debuts", "Category:Swaziland_at_multi-sport_events", "Category:multi-sport_events_at_Yemen"]
    # ---
    newtest2 = [
        "Category:Multi-sport_events_in_the_Soviet_Union",
        "Category:Soviet_Union_at_multi-sport_events",
        "Category:Ethnic_groups_of_the_Dominican_Republic",
        "Category:women_in_business",
        "Category:Polish_women_in_business",
        "Category:European_women_in_business",
        "Category:Polish_businesspeople",
        "Category:Polish_women_by_occupation",
        "Category:Women_in_business_by_nationality",
        "Category:Immigrants_to_New_Zealand",
        "Category:Immigration_to_New_Zealand",
    ]
    # ---
    msl = [
        "Category:2017 American television seasons",
        "Category:2017 American television series",
        "Category:2017 American television episodes",
        "Category:2017 American television series endings",
        "Category:2017 American television series debuts",
        "Category:Films by city of shooting location",
        "Category:Television_series_by_city_of_location",
        "Category:Television_shows_by_city_of_setting",
        "Category:Television_shows_set_in_Australia_by_city",
        "Category:Television_series_produced_in_Seoul",
        "Category:Television_series_by_country_of_shooting_location",
        "Category:South_Korean_television_series_by_production_location",
        "Category:Television_series_produced_in_Alberta",
        "Category:Television_shows_filmed_in_Algeria",
        "Category:Films_shot_in_China_by_city",
        "Category:Television_series_endings_by_year",
        "Category:Films_based_on_television_series",
        "Category:Television characters by series",
        "Category:Drama_television_characters_by_series",
        "Category:Lists_of_television_characters_by_series",
        "Category:Lists_of_action_television_characters_by_series",
        "Category:Lists_of_British_television_series_characters_by_series",
        "Category:Fantasy_television_characters_by_series",
        "Category:18th-century_people_of_the_Dutch_Empire",
        "Category:18th-century_Dutch_explorers",
        "Category:Television_programs_by_geographic_setting",
        "Category:American_people_of_the_Iraq_War",
        "Category:Historical_comics",
        "Category:Comics_set_in_the_1st_century_BC",
        "Category:French_comic_strips",
        "Category:French_comic",
        "Category:Comics_publications",
        "Category:Publications_by_format",
        "Category:Comics_based_on_films",
        "Category:Publications_by_year_of_establishment",
        "Category:Publications_by_year_of_disestablishment",
        "Category:Cartoonists_by_publication",
        "Category:19th-century_publications",
        "Category:British_editorial_cartoonists",
        "Category:Editorial_cartoonists_from_Northern_Ireland",
        "Category:Female_comics_writers",
        "Category:Films_based_on_works_by_comic_book_writers",
        "Category:Publications_disestablished_in_1946",
        "Category:Comics_adapted_into_films",
        "Category:Films based on comics",
        "Category:Films_based_on_American_comics",
        "Category:Works_adapted_for_other_media",
        "Category:Australian Internet celebrities",
        "Category:Women's_organizations based_in_Cuba",
        "Category:Women's_sports_teams_in_Cuba",
        "Category:Women's_national_sports_teams_of_Cuba",
        "Category:Cuba_women's_national_basketball_team",
        "Category:International_women's_basketball_competitions_hosted_by_Cuba",
        "Category:Cape_Verdean_football_managers",
        "Category:Sports_coaches_by_nationality",
        "Category:Olympic_competitors_for_Cape_Verde",
        "Category:Paralympic_competitors_for_Cape_Verde",
        "Category:Cape_Verde_at_the_Paralympics",
        "Category:Argentina_at_the_Winter_Olympics",
        "Category:Olympic_gold_medalists_for_the_United_States_in_alpine_skiing",
        "Category:Olympic_gold_medalists_for_the_United_States",
        "Category:Olympic_medalists_for_the_United_States",
        "Category:American_award_winners",
        "Category:American_people_by_status",
        "Category:People_by_nationality_and_status",
        "Category:Awards_by_country",
        "Category:Award_winners_by_nationality",
        "Category:Olympic_medalists_in_alpine_skiing",
        "Category:Expatriate_association_football_managers_by_country_of_residence",
        "Category:National_association_football_team_managers",
        "Category:Afghanistan_national_football_team_managers",
        "Category:Afghanistan_women's_national_football_team_coaches",
        "Category:Ireland_international_rules_football_team_coaches",
        "Category:Afghanistan_women's_national_football_team_coaches",
        "Category:20th-century_Albanian_sports_coaches",
        "Category:Equatorial_Guinea_women's_national_football_team",
        "Category:Equatoguinean_women's_footballers",
        "Category:African_women's_national_association_football_teams",
        "Category:Skiing_coaches",
        "Category:American_track_and_field_coaches",
        "Category:Belgian_athletics_coaches",
        "Category:Mammals_described_in_2017",
        "Category:Manufacturing_companies_established_in_the_2nd_millennium",
        "Category:Holding_companies_established_in_1942",
        "",
        "",
    ]
    # ---
    newtest = [
        "Category:Afghan_emigrants",
        "Category:Residency_shows_in_the_Las_Vegas_Valley",
        "Category:2004_residency_shows",
        "Category:Residency_shows_by_artist",
        "Category:Penal_system_in_Afghanistan",
        "Category:People_executed_by_Afghanistan",
        "Category:Recipients_of_Afghan_presidential_pardons",
        "Category:Prisoners_and_detainees_of_Afghanistan",
        "Category:Prisons_in_Afghanistan",
        "Category:Internees_at_the_Sheberghan_Prison",
        "Category:Penal_systems_by_country",
        "Category:Afghan_criminal_law",
        "Category:Films_set_in_national_parks",
        "Category:Categories_by_province_of_Saudi_Arabia",
        "Category:Rail_transport_in_Sri_Lanka_by_province",
        "Category:19th-century_people_by_religion",
        "Category:19th-century_actors_by_religion",
        "Category:Immigrants_to_the_United_Kingdom_from_Aden",
        # , "Category"
        # , "Category"
    ]
    fees = """
        Category:Martial arts films by genre
        Category:Western (genre) films by genre
        Category:Residency shows in the Las Vegas Valley
        Category:2004 residency shows
        Category:Residency shows by artist
        Category:Recipients of Afghan presidential pardons
        Category:Internees at the Sheberghan Prison
        Category:Ugandan
        Category:Historical comics
        Category:French comic strips
        Category:Comics publications
        Category:Female comics writers
        Category:Films based on works by comic book writers
        Category:Award winners by nationality
        Category:Equatoguinean women's footballers
        Category:American track and field coaches
        Category:Holding companies established in 1942
        Category:Polish women by occupation
        Category:Historical_novels
        Category:Holocaust_literature
        Category:Historical_poems
        Category:Historical_webcomics
        Category:Historical_short_stories
        Category:Historical_fiction_by_setting
        Category:Video_games_set_in_prehistory
        Category:Video_games_about_slavery
        Category:Historical_television_series
        Category:Dinosaurs_in_video_games
        Category:Dinosaurs_in_fiction
        Category:Video_games_about_diseases
        Category:Video_games_set_in_the_Byzantine_Empire
        Category:Dark_fantasy_video_games
        Category:Fantasy_video_games
        Category:Video_games_based_on_mythology
        Category:Video_games_based_on_Egyptian_mythology
        Category:Scottish_popular_culture
        Category:Scottish_traditions
        Category:Characters_in_children's_literature
        Category:Celtic_mythology_in_popular_culture
        Category:Celtic_mythology_in_popular_culture
    """
    feeslist = [x.strip() for x in fees.split("\n")]

    poiuygfvb = """
        Category:Lists of association football players by national team
        Category:Association football players by amateur national team
        Category:Association football players by B national team
        Category:Association football players by under-20 national team
        Category:Association football players by under-21 national team
        Category:Association football players by under-23 national team
        Category:Association football players by women's national team
        Category:Association football players by youth national team
        Category:Australia international soccer players
        Category:Canada men's international soccer players
        Category:Nauru international soccer players
        Category:South Africa international soccer players
        Category:United States men's international soccer players
        Category:United States Virgin Islands international soccer players
        Category:European_national_under-21_association_football_teams
        Category:Sports_at_the_Winter_Paralympics
        Category:Women's_national_youth_association_football_teams
        Category:Women's_national_under-18_ice_hockey_teams
        Category:National_under-18_ice_hockey_teams
        Category:Women's_national_ice_hockey_teams
        Category:Expatriate women's association football players
        Category:Expatriate_women's_footballers_by_location
        Category:Algerian_male_sailors_(sport)
        Category:Sailors_by_sailing_team
        Category:Sailors_by_club
        Category:Sailors_in_Denmark_by_club
        Category:Yemen_at_the_Youth_Olympics
        Category:Video_games_developed_in_Australia
        Category:Youth_association_football_by_country
        Category:National_youth_sports_teams_by_country
        Category:Youth_Olympic_Games
        Category:Airports_in_Pennsylvania
        Category:Women_of_the_Hyderabad_State

    """
    hhhhh = [x.strip() for x in poiuygfvb.split("\n")]
    # ---
    Yemen_list = """
        Category:Roman Catholic Church in Yemen
        Category:Roman Catholic churches in Yemen
        Category:Sasanian governors of Yemen
        Category:Saudi Arabia–Yemen military relations
        Category:Seas of Yemen
        Category:Secession in Yemen
        Category:Service industries in Yemen
        Category:Shanty towns in Yemen
        Category:Shia Islam in Yemen
        Category:Ships of Yemen
        Category:Ships of the South Yemen Navy
        Category:Ships of the Yemen Navy
        Category:South Korea–Yemen relations
        Category:South Yemen in World War II
        Category:South Yemeni companies established in 1971
        Category:South Yemeni people
        Category:Spain–Yemen relations
        Category:Speakers of the House of Representatives (Yemen)
        Category:Sports leagues in Yemen
        Category:Suicide car and truck bombings in Yemen
        Category:Suspected Wikipedia sockpuppets of Yemenreform
        Category:Targeted killings in Yemen
        Category:Terrorist incidents in Yemen by perpetrator
        Category:Terrorist incidents in Yemen in 2000
        Category:Terrorist incidents in Yemen in 2001
        Category:Terrorist incidents in Yemen in 2007
        Category:Terrorist incidents in Yemen in 2008
        Category:Terrorist incidents in Yemen in 2009
        Category:Terrorist incidents in Yemen in 2012
        Category:Terrorist incidents in Yemen in 2013
        Category:Terrorist incidents in Yemen in 2014
        Category:Towns in Yemen
        Category:Trade unions in Yemen
        Category:Transport buildings and structures in Yemen
        Category:Turkey–Yemen relations
        Category:Umayyad governors of Yemen
        Category:Vice Presidents of North Yemen
        Category:Water supply and sanitation in Yemen
        Category:Works by Yemeni people
        Category:World Championships in Athletics athletes for Yemen
        Category:Wushu in Yemen
        Category:Years of the 20th century in South Yemen
        Category:Yemen at the Summer Olympics by year
        Category:Yemen at the West Asian Games
        Category:Yemen at the World Aquatics Championships
        Category:Yemen at the World Championships in Athletics
        Category:Yemen communications-related lists
        Category:Yemen diplomacy-related lists
        Category:Yemen governorate templates
        Category:Yemen people
        Category:Yemen political party colour templates
        Category:Yemen political party templates
        Category:Yemen religion-related lists
        Category:Yemen researchers
        Category:Yemen sports navigational boxes
        Category:Yemen transport-related lists
        Category:Yemen under the Abbasid Caliphate
        Category:Yemen user templates
        Category:Yemeni Canadians
        Category:Yemeni Ismailis
        Category:Yemeni League
        Category:Yemeni League seasons
        Category:Yemeni Marxists
        Category:Yemeni Muslim Brotherhood members
        Category:Muslim missionaries
        Category:Yemeni Muslim activists
        Category:Yemeni President Cup
        Category:Yemeni Shi'a Muslims
        Category:Yemeni Shia Muslims
        Category:Yemeni Sufi religious leaders
        Category:Yemeni Sufi saints
        Category:Yemeni christian saints
        Category:Yemeni Sunni Muslims
        Category:Yemeni Unity Cup
        Category:Yemeni Zaydis
        Category:Yemeni artistic gymnasts
        Category:Yemeni clothing
        Category:Yemeni democracy activists
        Category:Yemeni diaspora in the Middle East
        Category:Yemeni executions
        Category:Yemeni female martial artists
        Category:Yemeni film people
        Category:Yemeni football logos
        Category:Yemeni history timelines
        Category:Yemeni human rights activists
        Category:Yemeni legislators
        Category:Yemeni male artistic gymnasts
        Category:Yemeni male martial artists
        Category:Yemeni male sport wrestlers
        Category:Yemeni martial artists
        Category:Yemeni mass murderers
        Category:Yemeni media
        Category:Yemeni monarchy
        Category:Yemeni muftis
        Category:Yemeni murder victims
        Category:Yemeni murderers
        Category:Yemeni nationalists
        Category:Yemeni people convicted of murder
        Category:Yemeni people murdered abroad
        Category:Yemeni people with disabilities
        Category:Yemeni prisoners sentenced to death
        Category:Yemeni sanshou practitioners
        Category:Yemeni scholars of Islam
        Category:Yemeni songs
        Category:Yemeni sportspeople in doping cases
        Category:Yemeni trade unionists
        Category:Yemeni victims of crime
        Category:Yemeni wushu practitioners
        Category:Yemenite Jewish songs
        Category:Death_in_East_Timor
        Category:Deaths_in_East_Timor
    """
    Yemen = [x.strip() for x in Yemen_list.split("\n")]

    oil = """
        Category:Christian_denominations_by_country
        Category:Environmental_issues_by_country
        Category:Environmental_disasters_by_country
        Category:Climate_change_by_country
        Category:Petroleum_industry_by_country
        Category:Hydraulic_fracturing
        Category:Natural_gas_companies_by_country
        Category:Companies_of_Ethiopia_by_industry
        Category:Fossil_fuels_by_country
        Category:Coal_by_country
        Category:Oil_refineries_by_country
        Category:Petroleum_infrastructure_by_country
        Category:Fossil_fuel_power_stations_by_country
        Category:Oil_shale
        Category:Oil_shale_by_country
        Category:Oil_shale_geology
        Category:Fossil_fuel_power_stations_by_country
        Category:Petroleum_by_country
        Category:Man-made_disasters_by_country
        Category:Bauxite_mining_by_country
        Category:Oil shale mining by country
        Category:Companies_by_industry_and_country
        Category:Companies_by_industry_and_country
        Category:Industries_by_country
        Category:Companies_of_the_United_States_by_industry
        Category:Oil_companies_by_country
        Category:Religious_organizations_by_faith_or_belief
        Category:Travel_and_holiday_companies_of_Germany
        Category:Industrial_installations_of_the_United_States_Army
    """

    oil_list = [x.strip() for x in oil.split("\n")]

    Yemen2 = """
        Category:Military installations of Morocco
        Category:Military installations in Morocco
        Category:Military_installations_of_the_United_States_in_Morocco
        Category:Civilians_killed_in_World_War_II_by_nationality
        Category:People_executed_by_England_and_Wales_after_1707_by_burning
        Category:People_executed_by_England_and_Wales_by_burning
        Category:People_executed_by_England_and_Wales_by_hanging
        Category:People_executed_by_England_by_burning
        Category:People_executed_by_England_by_decapitation
        Category:People_executed_by_England_by_firearm

        Category:Prisoners who died in Polish detention
        Category:Capital punishment in Poland
        Category:Prisoners sentenced to death by Poland
        Category:Prisoners who died in Polish detention
        Category:Capital punishment in Poland
        Category:Prisoners sentenced to death by Poland

        Category:20th-century executions by Vietnam
        Category:Sasanian governors of Yemen
        Category:Saudi Arabia–Yemen military relations
        Category:Shanty towns in Yemen
        Category:Ships of the South Yemen Navy
        Category:South Korea–Yemen relations
        Category:South Yemen in World War II
        Category:South Yemeni companies established in 1971
        Category:South Yemeni people
        Category:Spain–Yemen relations
        Category:Speakers of the House of Representatives (Yemen)
        Category:Suicide car and truck bombings in Yemen
        Category:Suspected Wikipedia sockpuppets of Yemenreform
        Category:Targeted killings in Yemen
        Category:Terrorist incidents in Yemen by perpetrator
        Category:Towns in Yemen
        Category:Trade unions in Yemen
        Category:Transport buildings and structures in Yemen
        Category:Turkey–Yemen relations
        Category:Umayyad governors of Yemen
        Category:Vice Presidents of North Yemen
        Category:Water supply and sanitation in Yemen
        Category:Works by Yemeni people
        Category:World Championships in Athletics athletes for Yemen
        Category:Wushu in Yemen
        Category:Years of the 20th century in South Yemen
        Category:Yemen at the Summer Olympics by year
        Category:Yemen at the West Asian Games
        Category:Yemen at the World Aquatics Championships
        Category:Yemen at the World Championships in Athletics
        Category:Yemen communications-related lists
        Category:Yemen diplomacy-related lists
        Category:Yemen governorate templates
        Category:Yemen people
        Category:Yemen political party colour templates
        Category:Yemen political party templates
        Category:Yemen religion-related lists
        Category:Yemen researchers
        Category:Yemen sports navigational boxes
        Category:Yemen transport-related lists
        Category:Yemen under the Abbasid Caliphate
        Category:Yemen user templates
        Category:Yemeni Canadians
        Category:Yemeni League seasons
        Category:Yemeni Muslim Brotherhood members
        Category:Yemeni Sufi religious leaders
        Category:Yemeni Sufi saints
        Category:Yemeni Unity Cup
        Category:Yemeni artistic gymnasts
        Category:Yemeni clothing
        Category:Yemeni democracy activists
        Category:Yemeni diaspora in the Middle East
        Category:Yemeni executions
        Category:Yemeni female martial artists
        Category:Yemeni film people
        Category:Yemeni football logos
        Category:Yemeni history timelines
        Category:Yemeni legislators
        Category:Yemeni male artistic gymnasts
        Category:Yemeni male martial artists
        Category:Yemeni male sport wrestlers
        Category:Yemeni martial artists
        Category:Yemeni media
        Category:Yemeni monarchy
        Category:Yemeni murder victims
        Category:Yemeni murderers
        Category:Yemeni nationalists
        Category:Yemeni people convicted of murder
        Category:Yemeni people murdered abroad
        Category:Yemeni people with disabilities
        Category:Yemeni sanshou practitioners
        Category:Yemeni scholars of Islam
        Category:Yemeni songs
        Category:Yemeni sportspeople in doping cases
        Category:Yemeni trade unionists
        Category:Yemeni victims of crime
        Category:Yemeni wushu practitioners
        Category:Yemenite Jewish songs
    """
    Yemen2_list = [x.strip() for x in Yemen2.split("\n")]

    misic = """
        Category:American music people
        Category:Indian architecture writers
        Category:Indian art writers
        Category:Indian bloggers
        Category:Indian business writers
        Category:Indian critics
        Category:Indian economics writers
        Category:Indian encyclopedists
        Category:Indian essayists
        Category:Indian food writers
        Category:Indian historians
        Category:Indian journalists
        Category:Indian legal writers
        Category:Indian military writers
        Category:Indian nature writers
        Category:Indian non-fiction environmental writers
        Category:Indian non-fiction writers by century
        Category:Indian political writers
        Category:Indian scholars
        Category:Indian science writers
        Category:Indian self-help writers
        Category:Indian social sciences writers
        Category:Indian spiritual writers
        Category:Indian sportswriters
        Category:Indian travel writers
        Category:Indian women non-fiction writers
        Category:Pakistani_film_actors_by_language
        Categories by language of Pakistan
        Category:Austrian music
        Category:Belgian music
        Category:Dutch music
        Category:German music
        Category:Liechtenstein music
        Category:Luxembourgian music
        Category:Nordic music
        Category:Swiss music
        Category:Journalists_killed_in_East_Timor
        Category:Latvian_murder_victims
        Category:Women's rugby union competitions in Europe for national teams
        """

    misic_list = [x.strip() for x in misic.split("\n")]
    # ---
    Assassinated = """
        Category:Assassinated journalists by nationality
        Category:Assassinated politicians by nationality
        Category:Assassinated Afghan people
        Category:Assassinated Albanian people
        Category:Assassinated Algerian people
        Category:Assassinated American people
        Category:Assassinated Angolan people
        Category:Assassinated Argentine people
        Category:Assassinated Armenian people
        Category:Assassinated Australian people
        Category:Assassinated Austrian people
        Category:Assassinated Azerbaijani people
        Category:Assassinated Bangladeshi people
        Category:Assassinated Belgian people
        Category:Assassinated Beninese people
        Category:Assassinated Bissau-Guinean people
        Category:Assassinated Bolivian people
        Category:Assassinated Bosnia and Herzegovina people
        Category:Assassinated Brazilian people
        Category:Assassinated British people
        Category:Assassinated Bulgarian people
        Category:Assassinated Burkinabé people
        Category:Assassinated Burmese people
        Category:Assassinated Burundian people
        Category:Assassinated Byzantine people
        Category:Assassinated Cambodian people
        Category:Assassinated Cameroonian people
        Category:Assassinated Canadian people
        Category:Assassinated Central African Republic people
        Category:Assassinated Chadian people
        Category:Assassinated Chechen people
        Category:Assassinated Chilean people
        Category:Assassinated Chinese people
        Category:Assassinated Colombian people
        Category:Assassinated Comorian people
        Category:Assassinated Democratic Republic of the Congo people
        Category:Assassinated Republic of the Congo people
        Category:Assassinated Costa Rican people
        Category:Assassinated Croatian people
        Category:Assassinated Cuban people
        Category:Assassinated Cypriot people
        Category:Assassinated Czech people
        Category:Assassinated Czechoslovak people
        Category:Assassinated Dominican Republic people
        Category:Assassinated Dutch people
        Category:Assassinated Ecuadorian people
        Category:Assassinated Egyptian people
        Category:Assassinated Ethiopian people
        Category:Assassinated Filipino people
        Category:Assassinated Finnish people
        Category:Assassinated French people
        Category:Assassinated people from Georgia (country)
        Category:Assassinated German people
        Category:Assassinated Gothic people
        Category:Assassinated Greek people
        Category:Assassinated Guatemalan people
        Category:Assassinated Guinean people
        Category:Assassinated Guyanese people
        Category:Assassinated Haitian people
        Category:Assassinated Honduran people
        Category:Assassinated Indian people
        Category:Assassinated Indonesian people
        Category:Assassinated Iranian people
        Category:Assassinated Iraqi people
        Category:Assassinated Irish people
        Category:Assassinated Israeli people
        Category:Assassinated Italian people
        Category:Assassinated Ivorian people
        Category:Assassinated Jamaican people
        Category:Assassinated Japanese people
        Category:Assassinated Jews
        Category:Assassinated Jordanian people
        Category:Assassinated Kenyan people
        Category:Assassinated Korean people
        Category:Assassinated Kosovan people
        Category:Assassinated Kurdish people
        Category:Assassinated Kyrgyzstani people
        Category:Assassinated Laotian people
        Category:Assassinated Latvian people
        Category:Assassinated Lebanese people
        Category:Assassinated Liberian people
        Category:Assassinated Libyan people
        Category:Assassinated Malagasy people
        Category:Assassinated Malawian people
        Category:Assassinated Malaysian people
        Category:Assassinated Mexican people
        Category:Assassinated Monegasque people
        Category:Assassinated Mongolian people
        Category:Assassinated Montenegrin people
        Category:Assassinated Moroccan people
        Category:Assassinated Mozambican people
        Category:Assassinated Namibian people
        Category:Assassinated Nepalese people
        Category:Assassinated Nicaraguan people
        Category:Assassinated Nigerian people
        Category:Assassinated Nigerien people
        Category:Assassinated Norwegian people
        Category:Assassinated Omani people
        Category:Assassinated people of the Ottoman Empire
        Category:Assassinated Pakistani people
        Category:Assassinated Palauan people
        Category:Assassinated Palestinian people
        Category:Assassinated Panamanian people
        Category:Assassinated Paraguayan people
        Category:Assassinated Peruvian people
        Category:Assassinated Polish people
        Category:Assassinated Portuguese people
        Category:Assassinated Puerto Rican people
        Category:Assassinated Rhodesian people
        Category:Assassinated Romanian people
        Category:Assassinated Russian people
        Category:Assassinated Rwandan people
        Category:Assassinated Salvadoran people
        Category:Assassinated Samoan people
        Category:Assassinated Saudi Arabian people
        Category:Assassinated Senegalese people
        Category:Assassinated Serbian people
        Category:Assassinated Seychellois people
        Category:Assassinated Solomon Islands people
        Category:Assassinated Somalian people
        Category:Assassinated South African people
        Category:Assassinated South Korean people
        Category:Assassinated Soviet people
        Category:Assassinated Spanish people
        Category:Assassinated Sri Lankan people
        Category:Assassinated Sudanese people
        Category:Assassinated Surinamese people
        Category:Assassinated Swedish people
        Category:Assassinated Swiss people
        Category:Assassinated Syrian people
        Category:Assassinated Tajikistani people
        Category:Assassinated Tanzanian people
        Category:Assassinated Thai people
        Category:Assassinated Togolese people
        Category:Assassinated Tunisian people
        Category:Assassinated Turkish people
        Category:Assassinated Ugandan people
        Category:Assassinated Ukrainian people
        Category:Assassinated Uruguayan people
        Category:Assassinated Venezuelan people
        Category:Assassinated Vietnamese people
        Category:Assassinated Yemeni people
        Category:Assassinated Yugoslav people
        Category:Assassinated Zimbabwean people
        """
    Assassinated_list = [x.strip() for x in Assassinated.split("\n")]
    # ---
    Assassinated2 = """
        Category:Assassinated journalists by nationality
        Category:Assassinated politicians by nationality
        Category:Assassinated Republic of the Congo people
        Category:people from Georgia (country)
        Category:Assassinated people from Georgia (country)
        Category:Assassinated people of the Ottoman Empire
        Category:Assassinated Bosnia and Herzegovina people
        Category:Assassinated Byzantine people
        Category:Assassinated Chechen people
        Category:people of Democratic Republic of the Congo
        Category:Assassinated Democratic Republic of the Congo people
        Category:people of Republic of the Congo
        Category:Assassinated Republic of the Congo people
        Category:Assassinated Gothic people
        Category:Assassinated Kurdish people
        Category:Assassinated Solomon Islands people
        Category:people of Solomon Islands
        Category:Danish_Confederation_of_Professional_Associations
        Category:National_trade_union_centers_of_Denmark
        Category:Chechen_people
        Category:Peoples_of_the_Caucasus
        Category:Nakh_peoples
        Category:Muslim_communities_of_Russia
        Category:Chechen_national_heroes
        Category:Iranian_peoples_in_the_Caucasus
        Category:Iranian_people_of_Assyrian_descent
        Category:Ancient_peoples
        Category:Works by Argentine people
        Category:Native_American_people
        Category:Iranian_people_of_Assyrian_descent
        Category:Medieval_Irish_people
        Category:Biographies about African-American people
        Category:African-American_autobiographies
        Category:American_non-fiction_books
        Category:People_murdered_by_organized_crime
        Category:People_convicted_of_murder_by_the_Bahamas
        Category:Deaths_by_firearm_in_Algeria
        Category:Deaths_by_firearm
        Category:Deaths_by_improvised_explosive_device
        Category:People executed by Mexico by firearm
        Category:Translators to Esperanto
        Category:Translators_of_the_Quran_into_Esperanto
        Category:Translators_of_the_Quran_into_English
        Category:Expatriates in insular areas of the United States
        Category:French_anti–nuclear_weapons_activists
        Category:United_Kingdom_abortion_law
        Category:English_family_law
        Category:Activities of criminal organizations
        Category:Activities of criminal organizations
        Category:Cultural_depictions_of_Abbott_and_Costello
        Category:Fictional_depictions_of_Abraham_Lincoln_in_literature
    """

    Assassinated2_list = [x.strip() for x in Assassinated2.split("\n")]
    # ---
    iiiiii = """
        Category:European Games competitors for Georgia (country)
        Category:European Games medalists for Georgia (country)
        Category:Georgia (country) at multi-sport events
        Category:Georgia (country) at the European Games
        Category:Georgia (country) at the Olympics
        Category:Georgia (country) at the Paralympics
        Category:Georgia (country) at the Summer Olympics
        Category:Georgia (country) at the Summer Olympics by year
        Category:Georgia (country) at the Winter Olympics
        Category:Georgia (country) at the Winter Olympics by year
        Category:Georgia (country) at the World Aquatics Championships
        Category:Georgia (country) at the World Championships in Athletics
        Category:Georgia (country) at the Youth Olympics
        Category:Georgia (country) international footballers
        Category:Georgia (country) under-21 international footballers
        Category:Georgia (country) women's international footballers
        Category:Georgia (country) youth international footballers
        Category:Georgia international rugby union players
        Category:Georgia national football team
        Category:Georgia national football team managers
        Category:Georgia national football team results
        Category:Georgia national rugby union team
        Category:Georgia national rugby union team matches
        Category:Georgia national rugby union team templates
        Category:Olympic bronze medalists for Georgia (country)
        Category:Olympic competitors for Georgia (country)
        Category:Olympic gold medalists for Georgia (country)
        Category:Olympic medalists for Georgia (country)
        Category:Olympic silver medalists for Georgia (country)
        Category:Paralympic competitors for Georgia (country)
        Category:Paralympic gold medalists for Georgia (country)
        Category:Paralympic medalists for Georgia (country)
        Category:South Ossetia national football team
        Category:Summer Olympics competitors for Georgia (country)
        Category:Winter Olympics competitors for Georgia (country)
        Category:World Championships in Athletics athletes for Georgia (country)
    """
    iiiiii_list = [x.strip() for x in iiiiii.split("\n")]
    # ---
    tennis = """
        Category:Abkhazia–Turkey relations
        Category:Afghanistan–Turkey relations
        Category:Albania–Turkey relations
        Category:Algeria–Turkey relations
        Category:Argentina–Turkey relations
        Category:Armenia–Turkey relations
        Category:Australia–Turkey relations
        Category:Austria–Turkey relations
        Category:Azerbaijan–Turkey relations
        Category:Belgium–Turkey relations
        Category:Bilateral military relations of Turkey
        Category:Bilateral relations of the Ottoman Empire
        Category:Bosnia and Herzegovina–Turkey relations
        Category:Brazil–Turkey relations
        Category:Bulgaria–Turkey relations
        Category:Canada–Turkey relations
        Category:Chile–Turkey relations
        Category:Colombia–Turkey relations
        Category:Croatia–Turkey relations
        Category:Cross-border operations of Turkey
        Category:Cuba–Turkey relations
        Category:Cyprus–Turkey relations
        Category:Denmark–Turkey relations
        Category:Egypt–Turkey relations
        Category:Finland–Turkey relations
        Category:France–Turkey relations
        Category:Georgia (country)–Turkey relations
        Category:Germany–Turkey relations
        Category:Greece–Turkey relations
        Category:Holy See–Turkey relations
        Category:India–Turkey relations
        Category:Iran–Turkey relations
        Category:Iraq–Turkey relations
        Category:Israel–Turkey relations
        Category:Italy–Turkey relations
        Category:Japan–Turkey relations
        Category:Jordan–Turkey relations
        Category:Kazakhstan–Turkey relations
        Category:Kosovo–Turkey relations
        Category:Kuwait–Turkey relations
        Category:Lebanon–Turkey relations
        Category:Lithuania–Turkey relations
        Category:Malaysia–Turkey relations
        Category:Malta–Turkey relations
        Category:Moldova–Turkey relations
        Category:Morocco–Turkey relations
        Category:Netherlands–Turkey relations
        Category:New Zealand–Turkey relations
        Category:Northern Cyprus–Turkey relations
        Category:Norway–Turkey relations
        Category:Pakistan–Turkey relations
        Category:Poland–Turkey relations
        Category:Portugal–Turkey relations
        Category:Qatar–Turkey relations
        Category:Romania–Turkey relations
        Category:Russia–Turkey relations
        Category:Rwanda–Turkey relations
        Category:Saudi Arabia–Turkey relations
        Category:Serbia–Turkey relations
        Category:Singapore–Turkey relations
        Category:Somalia–Turkey relations
        Category:South Korea–Turkey relations
        Category:Soviet Union–Turkey relations
        Category:Spain–Turkey relations
        Category:Sweden–Turkey relations
        Category:Switzerland–Turkey relations
        Category:Syria–Turkey relations
        Category:Tunisia–Turkey relations
        Category:Turkey–Turkmenistan relations
        Category:Turkey–Ukraine relations
        Category:Turkey–United Kingdom relations
        Category:Turkey–United States relations
        Category:Turkey–Uzbekistan relations
        Category:Turkey–Yemen relations
        Category:Turkey–Yugoslavia relations
        Category:Cross-border_operations_of_Turkey into_Iraq
    """
    tennis_list = [x.strip() for x in tennis.split("\n")]

    foot = """
        Category:Amateur association football
        Category:Association football by city
        Category:Association football by continent
        Category:Association football by country
        Category:Association football champions
        Category:Association football competitions
        Category:Association football culture
        Category:Association football equipment
        Category:Association football logos
        Category:Association football media
        Category:Association football occupations
        Category:Association football organisations
        Category:Association football people
        Category:Association football tactics and skills
        Category:Association football teams
        Category:Association football terminology
        Category:Association football trophies and awards
        Category:Association football variants
        Category:Association football venues
        Category:Association football-related lists
        Category:College soccer
        Category:History of association football
        Category:Laws of association football
        Category:Military association football
        Category:Women's association football
        Category:Youth association football
        """
    foot_list = [x.strip() for x in foot.split("\n")]

    # ---
    # ---
    # ---
    te_t = {
        "1": test_ll,
        "2": tittable2,
        "oo": oo_list,
        "vt": vtittable2,
        "nn": New_Month_list2,
        "dd2": dd2,
        "ddd": ddd,
        "am": Ambassadors,
        "new": newtest,
        "new2": newtest2,
        "msl": msl,
        "fe": feeslist,
        "hh": hhhhh,
        "ye1": Yemen,
        "ye2": Yemen2_list,
        "oil": oil_list,
        "misic": misic_list,
        "Assa": Assassinated_list,
        "Assa2": Assassinated2_list,
        "iii": iiiiii_list,
        "tennis": tennis_list,
        "foot": foot_list,
    }
    # ---
    for x in te_t:
        test_table[x] = te_t[x]


Add_tab()


def maintest():
    # ---
    Test_Again = True
    # ---
    # test_table["iii"] = iiiiii_list
    # TTTT = {}
    TTTT = []
    # ---
    limit = 10000
    # ---
    for arg in sys.argv:
        arg, _, value = arg.partition(":")
        # ---
        if arg == "te":
            if value in test_table:
                Test_Again = False
                TTTT = test_table[value]
        # ---
        if arg == "limit" and value.isdigit():
            limit = int(value)
        # ---
        if arg == "file" or arg == "testfile":
            if arg == "testfile":
                value = f"textfiles/make_test/{value}.txt"
            Test_Again = False
            lala = ""
            # ---
            if not value.startswith(str(Dir)):
                value = f"{str(Dir)}/{value}"
            # ---
            print(value)
            # ---
            with open(value, "r", encoding="utf-8") as f:
                lala = f.read()
            # ---
            File_List = [x.strip() for x in lala.split("\n")]
            # ---
            TTTT = File_List
    # ---
    if Test_Again:
        for kk in test_table:
            for cat in test_table[kk]:
                if cat not in TTTT:
                    TTTT.append(cat)
    # ---
    # remove duplicates
    TTTT = list(set(TTTT))
    # ---
    if len(TTTT) > limit:
        TTTT = TTTT[:limit]
    # ---
    printe.output(f"<<lightblue>> maintest work in {len(TTTT)} items.")
    printe.output(f"<<lightblue>> maintest work in {len(TTTT)} items.")
    # ---
    Fap = event(TTTT, noprint="so", Local=True, printfirst=True, printhead=True)
    iu = sorted([x for x in Fap])
    done = []
    # for cate in Fap:
    for cate in iu:
        # printe.output('    "%s"  = "%s",' % ( cate , Fap[cate])  )
        done.append(cate.lower())
        # else:
        # printe.output('Cat : Fap["%s"] = "%s",' % (cate , Fap.get(cate , ""))  )
    # ---
    for cuy in TTTT:
        cuy2 = re.sub(r"_", " ", cuy)
        cuy2 = cuy2.lower()

        # if cuy2 not in done:
        # printe.output('   "%s"  = "%s",' % ( cuy , ""))
    # ---
    # printe.output('<<lightblue>> find %d same label from %d cat, find %d diffrent.' % (Same , len(TTTT) , Diff))
    # ---


if __name__ == "__main__":
    maintest()
    print_memory()
# ---
