def sort_dict_values(d: dict) -> dict:
    sorted_dict = dict(sorted(d.items(), key = lambda x: x[1]))

    return sorted_dict