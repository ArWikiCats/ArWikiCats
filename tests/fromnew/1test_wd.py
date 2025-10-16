#!/usr/bin/python3

from src.make2_bots.fromnet.wd import find_name_from_wikidata

tase = """
fort worth, texas
technical universities and colleges
genoa
the early modern era
corvettes
the sword
football cup competitions
south asia
law alumni
the future
populated coastal places
business
overseas france
disease-related deaths
tribes
lgbt rights
the midwestern united states
arabs
market towns
world rowing championships medalists
athletics (track and field)
social groups
historic sites
arts and letters
isotopes
video gaming
gender
hemiptera
the san francisco bay area
orange-nassau
the peerage
by oblast
colonizer and former colony
screenplays
endemic fauna of
fellows of
event venues
non-profit organizations
the north sea
forest lawn memorial park (hollywood hills)
relations of
by state or union territory
abu dhabi
newfoundland and labrador
ships built
chicago
municipalities
invertebrates
medical and health organisations
ports and harbours
the mediterranean sea
the year winners
sindh
representatives
protostomes
for deletion
music alumni
computer-related introductions
victoria (australia)
broadcasting
films scored
disasters
controversies
mayors of places
songs written
taxa named
terrorism
people educated
fame inductees
the new york metropolitan area
sport
by district
"""
# ---
for t in tase.splitlines():
    if t.strip() :
        find_name_from_wikidata(t.strip())
