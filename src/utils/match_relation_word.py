

def get_relation_word_new(category, data):
    # Find the first matching tito key in the category
    matched_tito = next(
        (key for key in data if f" {key} " in category),
        None
    )
    # ---
    if matched_tito:
        tito_name = data[matched_tito]
        tito = f" {matched_tito} "
        return tito, tito_name
    # ---
    return "", ""


def get_relation_word(category, data):
    for tito, tito_name in data.items():
        tito = f" {tito} "
        # if Keep_Work and tito in category:
        if tito in category:
            return tito, tito_name
    # ---
    return "", ""


__all__ = [
    "get_relation_word_new",
    "get_relation_word",
]
