from chair_with_gems import compare_chairs_weight


def test_compare_chairs_weight_1():
    heaviest_chair = compare_chairs_weight(33, 21, 11, 32)
    assert heaviest_chair == 1

def test_compare_chairs_weight_2():
    heaviest_chair = compare_chairs_weight(33, 33, 33, 34)
    assert heaviest_chair == 4

def test_compare_chairs_weight_3():
    heaviest_chair = compare_chairs_weight(33, 34, 35, 34)
    assert heaviest_chair == 3
