from modules.rook_moves import tell_if_rook_beats_another_rook


def test_tell_if_rook_beats_another_rook_1():
    tip = tell_if_rook_beats_another_rook('B', 5, 'E', 4)
    assert tip == 'No'


def test_tell_if_rook_beats_another_rook_2():
    tip = tell_if_rook_beats_another_rook('B', 5, 'E', 5)
    assert tip == 'Yes'


def test_tell_if_rook_beats_another_rook_3():
    tip = tell_if_rook_beats_another_rook('B', 5, 'B', 8)
    assert tip == 'Yes'
