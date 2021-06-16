from roles import role_list_to_str


def test_role_list_1():
    roles_as_str = role_list_to_str("Инженер", "Физик", "Ученный", ",")
    assert roles_as_str == 'Инженер,Физик,Ученный'


def test_role_list_2():
    roles_as_str = role_list_to_str("Политик", "Лидер", "Боец", " и ")
    assert roles_as_str == 'Политик и Лидер и Боец'
