
from ..helps import logger
from .translations_resolvers import resolved_translations_resolvers
from .translations_resolvers_v3i import resolved_translations_resolvers_v3i
from .translations_resolvers_v2 import resolved_translations_resolvers_v2
from .new_jobs_resolver import new_jobs_resolver_label


def new_resolvers_all(category: str) -> str:
    logger.debug(f">> new_resolvers_all: {category}")
    category_lab = (
        # jobs before sports, to avoid mis-resolving like:
        # incorrect:    "Category:American basketball coaches": "تصنيف:مدربو كرة سلة أمريكية"
        # correct:      "Category:American basketball coaches": "تصنيف:مدربو كرة سلة أمريكيون"
        new_jobs_resolver_label(category) or
        resolved_translations_resolvers_v3i(category) or
        resolved_translations_resolvers_v2(category) or
        resolved_translations_resolvers(category) or
        ""
    )
    logger.debug(f"<< new_resolvers_all: {category} => {category_lab}")
    return category_lab
