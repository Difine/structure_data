def merge_two_dicts(first_dict: dict, second_dict: dict) -> dict:
    merges_dict = first_dict.copy()
    merges_dict.update(second_dict)

    return merges_dict