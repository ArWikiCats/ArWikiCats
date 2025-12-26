
from ..helps import logger
from .countries_names_resolvers import resolved_countries_names_main
from .translations_resolvers_v3i import resolved_translations_resolvers_v3i
from .nationalities_resolvers import resolved_translations_resolvers_v2
from .jobs_resolvers import new_jobs_resolver_label


def new_resolvers_all(category: str) -> str:
    logger.debug(f">> new_resolvers_all: {category}")
    category_lab = (
        # jobs before sports, to avoid mis-resolving like:
        # incorrect:    "Category:American basketball coaches": "تصنيف:مدربو كرة سلة أمريكية"
        # correct:      "Category:American basketball coaches": "تصنيف:مدربو كرة سلة أمريكيون"
        new_jobs_resolver_label(category) or
        resolved_translations_resolvers_v3i(category) or
        resolved_translations_resolvers_v2(category) or
        resolved_countries_names_main(category) or
        ""
    )
    logger.debug(f"<< new_resolvers_all: {category} => {category_lab}")
    return category_lab
