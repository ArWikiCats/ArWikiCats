import sys
from pathlib import Path

if _Dir := Path(__file__).parent.parent:
    sys.path.append(str(_Dir))

from ArWikiCats.make_bots.films_and_others_bot import get_films_key_tyty_new

from ArWikiCats import resolve_arabic_category_label, logger
from ArWikiCats.genders_resolvers.nat_genders_pattern_multi import resolve_nat_genders_pattern_v2
logger.set_level("DEBUG")

# print(resolve_arabic_category_label("Category:2015 American television"))

# print(resolve_nat_genders_pattern_v2("classical composers"))
# print(resolve_nat_genders_pattern_v2("guitarists"))
# print(resolve_nat_genders_pattern_v2("male guitarists"))
# print(resolve_nat_genders_pattern_v2("yemeni male guitarists"))
# print(resolve_nat_genders_pattern_v2("male yemeni guitarists"))
print(get_films_key_tyty_new("american adult animated television films"))

# python3 -c "from ArWikiCats import resolve_arabic_category_label; print(resolve_arabic_category_label('Category:2015 American television'))"
