def calculate_sleep_time(road_time):
    sleep_time = road_time // 2
    hh = sleep_time // 60
    mm = sleep_time % 60
    return hh, mm


def hh_mm_to_str(hh, mm):
    if hh == 0:
        return f'{mm} м'
    else:
        return f'{hh} ч {mm} м'


if __name__ == "__main__":
    t = int(input())
    hh, mm = calculate_sleep_time(t)
    s = hh_mm_to_str(hh, mm)
    print(s)
