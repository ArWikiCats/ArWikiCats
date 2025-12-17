
from ...helps import logger
from .rele import work_relations


def resolve_relations_labels(text: str) -> str:
    normalized_text = text.lower().replace("category:", " ")
    logger.debug(f"resolve_relations_labels: {normalized_text=}")

    label = (
        work_relations(normalized_text) or
        ""
    )
    logger.debug(f"resolve_relations_labels: {normalized_text=}, {label=}")
    return label


__all__ = [
    "resolve_relations_labels",
]
