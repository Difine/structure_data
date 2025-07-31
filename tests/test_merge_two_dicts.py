from src.merge_two_dicts import merge_two_dicts

def test_merge_two_dicts():
    """
        Соединить два словаря
    """
    developed_markets = {
        "USA": 100,
        "Japan": 90,
        "France": 25
    }

    emerging_markets = {
        "China": 80,
        "India": 50,
        "Russia": 5
    }

    assert merge_two_dicts(developed_markets, emerging_markets) == {
        "USA": 100,
        "Japan": 90,
        "France": 25,
        "China": 80,
        "India": 50,
        "Russia": 5
    }
