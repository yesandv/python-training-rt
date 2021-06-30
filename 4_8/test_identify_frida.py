from identify_frida import count_occurrences, identify_frida


def test_count_occurrences():
    number_of_occurrences = count_occurrences(3, [1, 3, 2, 4, 4, 5, 3, 2, 1])
    assert number_of_occurrences == 2


def test_identify_frida():
    frida = identify_frida([1, 3, 2, 4, 4, 5, 3, 2, 1])
    assert frida == 5
