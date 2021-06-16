from currency_converter import exchange_rub_to_usd, exchange_usd_to_rub, currency_converter


def test_exchange_rub_to_usd():
    rub_to_usd_rate = exchange_rub_to_usd(100, 100)
    assert rub_to_usd_rate == 1


def test_exchange_usd_to_rub():
    usd_to_rub_rate = exchange_usd_to_rub(1000, 100)
    assert usd_to_rub_rate == 0.1


def test_currency_converter_1():
    exchange_amount = currency_converter(1, 100, 100, 100)
    assert exchange_amount == 100.0


def test_currency_converter_2():
    exchange_amount = currency_converter(1, 100, 1000, 1)
    assert exchange_amount == 0.1


def test_currency_converter_3():
    exchange_amount = currency_converter(2, 1000, 100, 10)
    assert exchange_amount == 1.0


def test_currency_converter_4():
    exchange_amount = currency_converter(2, 1000, 100, 0)
    assert exchange_amount == 0.0
