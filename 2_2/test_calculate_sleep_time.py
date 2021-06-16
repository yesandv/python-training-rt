from calculate_sleep_time import calculate_sleep_time, hh_mm_to_str


def test_calculate_sleep_time_1():
    hh, mm = calculate_sleep_time(57)
    assert (hh, mm) == (0, 28)


def test_calculate_sleep_time_2():
    hh, mm = calculate_sleep_time(124)
    assert (hh, mm) == (1, 2)


def test_hh_mm_to_str_1():
    s = hh_mm_to_str(0, 28)
    assert s == '28 м'


def test_hh_mm_to_str_2():
    s = hh_mm_to_str(1, 2)
    assert s == '1 ч 2 м'
