from identify_frida import count_occurrences, identify_frida


def test_count_occurrences():
    number_of_occurrences = count_occurrences(3, [1, 3, 2, 4, 4, 5, 3, 2, 1])
    assert number_of_occurrences == 2


def test_identify_frida_1():
    frida = identify_frida([1, 3, 2, 4, 4, 5, 3, 2, 1])
    assert frida == 5


def test_identify_frida_2():
    frida = identify_frida([1, 1000, 1])
    assert frida == 1000


def test_identify_frida_3():
    frida = identify_frida([15, 13, 11, 11, 13, 15, 17])
    assert frida == 17


def test_identify_frida_4():
    frida = identify_frida([1, 2, 3, 4, 5, 4, 3, 2, 1])
    assert frida == 5


def test_identify_frida_5():
    frida = identify_frida([5, 3, 2, 4, 5, 4, 3, 2, 1])
    assert frida == 1
