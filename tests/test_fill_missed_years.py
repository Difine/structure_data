from src.fill_missed_years import fill_missed_years

def test_fill_missed_years():

    yearly_sales = {
        "2015": 50,
        "2018": 65,
        "2019": 120,
        "2023": 160,
        "2025": 200
    }

    assert fill_missed_years(yearly_sales) == {
        "2015": 50,
        "2016": 55,
        "2017": 60,
        "2018": 65,
        "2019": 120,
        "2020": 130,
        "2021": 140,
        "2022": 150,
        "2023": 160,
        "2024": 180,
        "2025": 200
    }

def test_empty_fill_missed_years():
    yearly_sales = {}
    assert fill_missed_years(yearly_sales) == {}

