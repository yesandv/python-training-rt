from admission import get_admission_fee_for_category, calculate_total_admission


def test_get_admission_fee_for_category_1():
    fee = get_admission_fee_for_category('Ребенок')
    assert fee == 5


def test_get_admission_fee_for_category_2():
    fee = get_admission_fee_for_category('Милиционер')
    assert fee == 5


def test_get_admission_fee_for_category_3():
    fee = get_admission_fee_for_category('Член профсоюза')
    assert fee == 10


def test_get_admission_fee_for_category_4():
    fee = get_admission_fee_for_category('Не член профсоюза')
    assert fee == 30


def test_calculate_admission_1():
    admission = calculate_total_admission('Член профсоюза', 'Ребенок', 'Не член профсоюза')
    assert admission == 45


def test_calculate_admission_2():
    admission = calculate_total_admission('Член профсоюза', 'Член профсоюза', 'Член профсоюза')
    assert admission == 30


def test_calculate_admission_3():
    admission = calculate_total_admission('Милиционер', 'Ребенок', 'Милиционер')
    assert admission == 15
