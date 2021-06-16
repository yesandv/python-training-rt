from calculate_stock_prices import calculate_stock_price, price_in_usd


def test_calculate_stock_price_1():
    final_price = calculate_stock_price(100, 12)
    assert final_price == 389.5975992546981


def test_calculate_stock_price_2():
    final_price = calculate_stock_price(500, 100)
    assert final_price == 2048000.0


def test_calculate_stock_price_3():
    final_price = calculate_stock_price(1, 100)
    assert final_price == 4096.0


def test_calculate_stock_price_4():
    final_price = calculate_stock_price(1, 1)
    assert final_price == 1.1268250301319698


def test_price_in_usd():
    convert = price_in_usd(389.5975992546981)
    assert convert == '389.5975992546981 $'
