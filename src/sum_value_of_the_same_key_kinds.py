def sum_value_of_the_same_key_kinds(d: dict) -> dict:
    summ_dict_year = {}
    for k, v in d.items():
        key = k[-4:]
        summ_dict_year[key] = summ_dict_year.get(key, 0) + v
    return summ_dict_year





