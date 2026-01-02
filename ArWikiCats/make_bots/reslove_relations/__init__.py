from ...helps import logger
from .rele import resolve_relations_label


def resolve_category_relations(text: str) -> str:
    normalized_text = text.lower().replace("category:", "")
    logger.debug(f"resolve_category_relations: {normalized_text=}")

    label = resolve_relations_label(normalized_text) or ""
    logger.debug(f"resolve_category_relations: {normalized_text=}, {label=}")
    return label


__all__ = [
    "resolve_category_relations",
]
