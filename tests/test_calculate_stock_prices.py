from modules.calculate_stock_prices import calculate_stock_price


def test_calculate_a_stock_price_1():
    assert calculate_stock_price(100, 12) == "389.5975992546981 $"


def test_calculate_a_stock_price_2():
    assert calculate_stock_price(500, 100) == "2048000.0 $"


def test_calculate_a_stock_price_3():
    assert calculate_stock_price(1, 100) == "4096.0 $"


def test_calculate_a_stock_price_4():
    assert calculate_stock_price(1, 1) == "1.1268250301319698 $"
