from unique_names import get_unique_names_from_a_list


def test_get_unique_names_from_a_list():
    unique_names_list = get_unique_names_from_a_list(["Баранцев", "Баранцев", "Баранцев", "Баранцев"])
    assert unique_names_list == ["Баранцев"]
