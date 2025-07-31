def sum_category_as_tuples(data):
    summ_dict = {}

    usefull_keys = ["category", "price_rub", "count"]

    for sales in data:
        if all(key in sales for key in usefull_keys):
            summ_dict[sales["category"]] = summ_dict.get(sales["category"], 0) + sales["price_rub"] * sales["count"]

    return [(k, v) for k,v in sorted(summ_dict.items(), key = lambda x: x[1])]
