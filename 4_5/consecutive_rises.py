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
