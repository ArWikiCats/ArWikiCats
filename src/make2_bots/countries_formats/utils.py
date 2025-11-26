import re


def add_definite_article(label: str) -> str:
    """Prefix each word in ``label`` with the Arabic definite article."""
    label_without_article = re.sub(r" ", " ال", label)
    new_label = f"ال{label_without_article}"
    return new_label
