def get_distinct_categories(data):

    distinct_categories = {d.get("category") for d in data}

    return distinct_categories

