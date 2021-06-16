from charged_particles import check_same_or_opposite_sign


def test_check_same_or_opposite_sign_1():
    result = check_same_or_opposite_sign(3, 10)
    assert result == 'Одноименные'


def test_check_same_or_opposite_sign_2():
    result = check_same_or_opposite_sign(-3, -10)
    assert result == 'Одноименные'


def test_check_same_or_opposite_sign_3():
    result = check_same_or_opposite_sign(-3, 10)
    assert result == 'Разноменные'
