from consecutive_rises import find_number_of_consecutive_rises, calculate_length_of_consecutive_rises


def test_find_number_of_consecutive_rises_1():
	rises = find_number_of_consecutive_rises([10, 13, 15, 7, 19, 15, 9, 15, 14])
	assert rises == 3


def test_calculate_length_of_consecutive_rises_1():
	length = calculate_length_of_consecutive_rises(3)
	assert length == 300


def test_find_number_of_consecutive_rises_2():
	rises = find_number_of_consecutive_rises([1, 1, 1, 1, 1, 1, 1, 1, 1])
	assert rises == 1


def test_calculate_length_of_consecutive_rises_2():
	length = calculate_length_of_consecutive_rises(1)
	assert length == 100


def test_find_number_of_consecutive_rises_3():
	rises = find_number_of_consecutive_rises([1, 1, 1, 2, 5, 5, 4, 1, 7])
	assert rises == 2


def test_calculate_length_of_consecutive_rises_3():
	length = calculate_length_of_consecutive_rises(2)
	assert length == 200


def test_find_number_of_consecutive_rises_4():
	rises = find_number_of_consecutive_rises([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
	assert rises == 10


def test_calculate_length_of_consecutive_rises_4():
	length = calculate_length_of_consecutive_rises(10)
	assert length == 1000
