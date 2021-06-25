def find_number_of_consecutive_rises(altitudes):
    altitudes.insert(0, 0)

    cur_consecutive_rises = 0
    max_consecutive_rises = 0

    for i in range(len(altitudes) - 1):
        if altitudes[i] < altitudes[i+1]:
            cur_consecutive_rises += 1
            if cur_consecutive_rises > max_consecutive_rises:
                max_consecutive_rises = cur_consecutive_rises
        else:
            cur_consecutive_rises = 0

    return max_consecutive_rises


def calculate_length_of_consecutive_rises(number_of_rises):
    length = number_of_rises * 100
    return length
