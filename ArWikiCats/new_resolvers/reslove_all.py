import functools

from ..helps import logger
from ..new.resolve_films_bots import get_films_key_tyty_new, get_films_key_tyty_new_and_time
from .countries_names_resolvers import resolve_countries_names_main
from .countries_names_with_sports import resolved_names_with_sports
from .jobs_resolvers import resolve_jobs_main
from .nationalities_resolvers import resolve_nationalities_main
from .relations_resolver import new_relations_resolvers
from .sports_resolvers import resolve_sports_main, sport_lab_nat
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
        # NOTE: resolve_nationalities_main must be before resolve_countries_names_main to avoid conflicts like:
        # resolve_countries_names_main> [Italy political leader]:  "قادة إيطاليا السياسيون"
        # resolve_nationalities_main> [Italy political leader]:  "قادة سياسيون إيطاليون"
        or resolve_nationalities_main(category)
        or resolve_countries_names_main(category)
        or get_films_key_tyty_new_and_time(category)
        or get_films_key_tyty_new(category)
        or new_relations_resolvers(category)
        or sport_lab_nat.sport_lab_nat_load_new(category)
        or resolved_names_with_sports(category)
        or ""
    )
    logger.debug(f"<< new_resolvers_all: {category} => {category_lab}")
    return category_lab
