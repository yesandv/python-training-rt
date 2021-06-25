from consecutive_rises import find_number_of_consecutive_rises, calculate_length_of_consecutive_rises


def test_find_number_of_consecutive_rises():
	rises = find_number_of_consecutive_rises(900, [10, 13, 15, 7, 19, 15, 9, 15, 14])
	assert rises == 3


def test_calculate_length_of_consecutive_rises():
	length = calculate_length_of_consecutive_rises(3)
	assert length == 300
