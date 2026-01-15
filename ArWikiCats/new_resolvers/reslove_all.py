import functools

from ..helps import logger
from ..new.resolve_films_bots import get_films_key_tyty_new, get_films_key_tyty_new_and_time
from .countries_names_resolvers import resolve_countries_names_main
from .jobs_resolvers import resolve_jobs_main
from .nationalities_resolvers import resolve_nationalities_main
from .relations_resolver import new_relations_resolvers
from .sports_resolvers import resolve_sports_main
from .translations_resolvers_v3i import resolve_v3i_main


@functools.lru_cache(maxsize=None)
def new_resolvers_all(category: str) -> str:
    logger.debug(f">> new_resolvers_all: {category}")
    category_lab = (
        # resolve_jobs_main before sports, to avoid mis-resolving like:
        # incorrect:    "Category:American basketball coaches": "تصنيف:مدربو كرة سلة أمريكية"
        # correct:      "Category:American basketball coaches": "تصنيف:مدربو كرة سلة أمريكيون"
        resolve_jobs_main(category)
        or resolve_v3i_main(category)
        or resolve_sports_main(category)
        or resolve_nationalities_main(category)
        or resolve_countries_names_main(category)
        or get_films_key_tyty_new_and_time(category)
        or get_films_key_tyty_new(category)
        or new_relations_resolvers(category)
        or ""
    )
    logger.debug(f"<< new_resolvers_all: {category} => {category_lab}")
    return category_lab
