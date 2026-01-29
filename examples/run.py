import logging
import sys
from pathlib import Path

if _Dir := Path(__file__).parent.parent:
    sys.path.append(str(_Dir))

from ArWikiCats import resolve_arabic_category_label
from ArWikiCats.legacy_bots.legacy_resolvers_bots.bys import make_by_label
from ArWikiCats.legacy_bots.legacy_resolvers_bots.with_years_bot import Try_With_Years
from ArWikiCats.legacy_bots.legacy_resolvers_bots.year_or_typeo import (
    label_for_startwith_year_or_typeo,
)
from ArWikiCats.new_resolvers.films_resolvers.resolve_films_labels import _get_films_key_tyty_new
from ArWikiCats.new_resolvers.films_resolvers.resolve_films_labels_and_time import get_films_key_tyty_new_and_time
from ArWikiCats.new_resolvers.jobs_resolvers.mens import mens_resolver_labels
from ArWikiCats.new_resolvers.nationalities_resolvers.nationalities_v2 import resolve_by_nats
from ArWikiCats.new_resolvers.relations_resolver.nationalities_double_v2 import resolve_by_nats_double_v2
from ArWikiCats.new_resolvers.sports_resolvers.jobs_multi_sports_reslover import jobs_in_multi_sports
from ArWikiCats.new_resolvers.sports_resolvers.raw_sports import resolve_sport_label_unified

logging.getLogger("ArWikiCats").set_level("DEBUG")

# print(resolve_arabic_category_label("Category:2015 American television"))

# print(get_films_key_tyty_new_and_time("american adult animated television films"))
# print(get_films_key_tyty_new_and_time("1960s yemeni comedy films"))
# print("-----"*20)
# print(label_for_startwith_year_or_typeo("1960s yemeni comedy films"))
# print(_get_films_key_tyty_new("animated short film films"))
# print(_get_films_key_tyty_new("American war films"))
# print(_get_films_key_tyty_new("animated short films"))
# print(get_films_key_tyty_new_and_time("2017 American television series debuts"))
# print(resolve_by_nats("Jewish history"))
# print(resolve_by_nats("American history"))
# print(resolve_by_nats("Jewish-American history"))
# print(mens_resolver_labels("men writers"))
# print(jobs_in_multi_sports("paralympic sailors"))
# print(resolve_by_nats_double_v2("jewish german surnames"))
# print(get_con_label("by danish artists"))
# print(make_by_label("by danish artists"))
# print(Try_With_Years("2020s Dutch-language films"))
print(resolve_sport_label_unified("national football"))
# print(resolve_by_nats_double_v2("jewish history"))

# python3 D:/categories_bot/make2_new/examples/run.py
# python3 -c "from ArWikiCats import resolve_arabic_category_label; print(resolve_arabic_category_label('Category:2015 American television'))"
