"""
Main entry point for resolving Arabic Wikipedia category names using multiple specialized resolvers.
This function orchestrates the resolution process by attempting to match a category string
against a series of specific resolvers in a predefined priority order to ensure accuracy
and avoid common linguistic conflicts (e.g., distinguishing between job titles and sports,
or nationalities and country names).
Args:
    category (str): The category name (usually in English) to be resolved into its Arabic equivalent.
Returns:
    str: The resolved Arabic category name if any resolver succeeds; otherwise, an empty string.
Note:
    - Results are cached using @functools.lru_cache for performance.
    - The order of execution is critical (e.g., 'jobs' before 'sports', and 'nationalities'
      before 'countries') to prevent incorrect grammatical or semantic translations.
New resolvers for Arabic Wikipedia categories.
"""
import functools

from ..helps import logger
from .countries_names_resolvers import resolve_countries_names_main
from .countries_names_with_sports import resolved_names_with_sports
from .films_resolvers import resolve_films_main
from .jobs_resolvers import main_jobs_resolvers
from .languages_resolves import resolve_languages_labels_with_time
from .nationalities_resolvers import resolve_nationalities_main
from .relations_resolver import new_relations_resolvers
from .sports_resolvers import resolve_sports_main, sport_lab_nat
from .time_and_jobs_resolvers import time_and_jobs_resolvers_main


@functools.lru_cache(maxsize=None)
def all_new_resolvers(category: str) -> str:
    logger.debug(f">> all_new_resolvers: {category}")
    category_lab = (
        # main_jobs_resolvers before sports, to avoid mis-resolving like:
        # incorrect:    "Category:American basketball coaches": "تصنيف:مدربو كرة سلة أمريكية"
        # correct:      "Category:American basketball coaches": "تصنيف:مدربو كرة سلة أمريكيون"
        main_jobs_resolvers(category)
        or time_and_jobs_resolvers_main(category)
        or resolve_sports_main(category)
        # NOTE: resolve_nationalities_main must be before resolve_countries_names_main to avoid conflicts like:
        # resolve_countries_names_main> [Italy political leader]:  "قادة إيطاليا السياسيون"
        # resolve_nationalities_main> [Italy political leader]:  "قادة سياسيون إيطاليون"
        or resolve_nationalities_main(category)
        or resolve_countries_names_main(category)
        or resolve_films_main(category)
        or new_relations_resolvers(category)
        or sport_lab_nat.sport_lab_nat_load_new(category)
        or resolved_names_with_sports(category)
        or resolve_languages_labels_with_time(category)
        or ""
    )
    logger.debug(f"<< all_new_resolvers: {category} => {category_lab}")
    return category_lab
