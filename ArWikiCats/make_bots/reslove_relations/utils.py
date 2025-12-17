
def sort_by_empty_space(data) -> dict:
    return dict(sorted(
        data.items(),
        key=lambda k: (-k[0].count(" "), -len(k[0])),
    ))
