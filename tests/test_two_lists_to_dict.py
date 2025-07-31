from src.two_lists_to_dict import two_lists_to_dict

def test_to_lists_to_dict():
    """
        Соединить два списка в словарь
    """
    keys = ["USA", "Russia", "France"]
    income = [100, 10, 25]
    assert two_lists_to_dict(keys, income) == {
        "USA": 100,
        "Russia": 10,
        "France": 25
    }