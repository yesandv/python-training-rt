from modules.discount import calculate_discount_on_geese


def test_calculate_discount_on_geese_1():
    final_price = calculate_discount_on_geese(20, 1)
    assert final_price == 20


def test_calculate_discount_on_geese_2():
    final_price = calculate_discount_on_geese(20, 4)
    assert final_price == 80


def test_calculate_discount_on_geese_3():
    final_price = calculate_discount_on_geese(20, 5)
    assert final_price == 100


def test_calculate_discount_on_geese_4():
    final_price = calculate_discount_on_geese(20, 6)
    assert final_price == 90


def test_calculate_discount_on_geese_5():
    final_price = calculate_discount_on_geese(20, 11)
    assert final_price == 110
