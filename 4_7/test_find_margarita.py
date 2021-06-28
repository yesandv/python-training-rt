from find_margarita import find_margarita


def test_find_margarita_combination_1():
    margaritas = find_margarita(0, 5, 23, 22)
    assert margaritas == 121


def test_find_margarita_combination_2():
    margaritas = find_margarita(0, 5, 24, 19)
    assert margaritas == 121


def test_find_margarita_combination_3():
    margaritas = find_margarita(0, 6, 21, 22)
    assert margaritas == 121
