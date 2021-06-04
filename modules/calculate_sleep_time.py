def calculate_time(road_time):
    s = road_time // 2
    h = s // 60
    m = s % 60
    st = f"{h} ч {m} м"
    return st


if __name__ == "__main__":
    t = int(input())
    s = calculate_time(t)
    print(s)
