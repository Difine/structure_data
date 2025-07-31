def fill_missed_years(data: dict[str, int]) -> dict[str, float]:
    if not data:
        return {}

    copy_dict = {int(k): v for k, v in data.items()}

    sorted_dict = sorted(copy_dict.items())
    result_data = {}

    for i in range(len(sorted_dict) - 1):
        year1, value1 = sorted_dict[i]
        year2, value2 = sorted_dict[i+1]

        result_data[year1] = value1
        result_data[year2] = value2
        diff = year2 - year1

        if diff > 0:
            step = (value2 - value1) / diff
            for k in range(1, diff):
                result_data[year1 + k] = value1 + step * k


    return {str(k): v for k, v in sorted(result_data.items())}

yearly_sales = {
        "2015": 50,
        "2018": 65,
        "2019": 120,
        "2023": 160,
        "2025": 200
    }

fill_missed_years(yearly_sales)


