from modules.calculate_sleep_time import calculate_time


def test_calculate_time_1():
    assert calculate_time(57) == "0 ч 28 м"


def test_calculate_time_2():
    assert calculate_time(124) == "1 ч 2 м"
