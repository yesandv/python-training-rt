def find_number_of_consecutive_rises(altitudes):
    position = 0

    consecutive_rises = 0
    max_consecutive_rises = 0

    for height in altitudes:
        if position < height:
            position = height
            consecutive_rises += 1
            if max_consecutive_rises < consecutive_rises:
                max_consecutive_rises = consecutive_rises
        else:
            consecutive_rises = 0

    return max_consecutive_rises


def calculate_length_of_consecutive_rises(number_of_rises):
    length = number_of_rises * 100
    return length


if __name__ == "__main__":
    mountain_length = int(input("Укажите общую длину горы: "))
    altitude = []
    for i in range(mountain_length // 100):
        rise = int(input("Укажите значение высоты: "))
        altitude.append(rise)
    max_consecutive_rises = find_number_of_consecutive_rises(altitude)
    length_of_max_consecutive_rises = calculate_length_of_consecutive_rises(max_consecutive_rises)
    print(length_of_max_consecutive_rises)
