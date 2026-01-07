import sys
from pathlib import Path

if _Dir := Path(__file__).parent.parent:
    sys.path.append(str(_Dir))

from ArWikiCats.new.resolve_films_bots.resolve_films_labels import _get_films_key_tyty_new
from ArWikiCats.new.resolve_films_bots.resolve_films_labels_and_time import get_films_key_tyty_new_and_time

from ArWikiCats.ma_bots2.year_or_typeo.bot_lab import (
    label_for_startwith_year_or_typeo,
)
from ArWikiCats import resolve_arabic_category_label, logger
from ArWikiCats.genders_resolvers.nat_genders_pattern_multi import resolve_nat_genders_pattern_v2

from ArWikiCats.new_resolvers.nationalities_resolvers.nationalities_v2 import resolve_by_nats

from ArWikiCats.new_resolvers.jobs_resolvers.mens import mens_resolver_labels

logger.set_level("DEBUG")

# print(resolve_arabic_category_label("Category:2015 American television"))

# print(resolve_nat_genders_pattern_v2("classical composers"))
# print(resolve_nat_genders_pattern_v2("guitarists"))
# print(resolve_nat_genders_pattern_v2("male guitarists"))
# print(resolve_nat_genders_pattern_v2("yemeni male guitarists"))
# print(resolve_nat_genders_pattern_v2("male yemeni guitarists"))
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
print(mens_resolver_labels("men writers"))

# python3 D:/categories_bot/make2_new/examples/run.py
# python3 -c "from ArWikiCats import resolve_arabic_category_label; print(resolve_arabic_category_label('Category:2015 American television'))"
