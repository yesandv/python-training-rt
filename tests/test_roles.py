from modules.roles import role_list


def test_role_list_1():
    roles = role_list("Инженер", "Физик", "Ученный", ",")
    assert roles == 'Who is John Galt?\nJohn Galt is:\nИнженер,Физик,Ученный'


def test_role_list_2():
    roles = role_list("Политик", "Лидер", "Боец", " и ")
    assert roles == 'Who is John Galt?\nJohn Galt is:\nПолитик и Лидер и Боец'
