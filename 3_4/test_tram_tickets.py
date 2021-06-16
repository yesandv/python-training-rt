from tram_tickets import verify_lucky_ticket, replace_lucky_ticket


def test_verify_lucky_ticket_1():
    full_number = verify_lucky_ticket('333', '333')
    assert full_number == 'Lucky'


def test_verify_lucky_ticket_2():
    full_number = verify_lucky_ticket('333', '334')
    assert full_number == 'Ordinary'


def test_replace_lucky_ticket_1():
    ordinary_ticket = replace_lucky_ticket('333', '333')
    assert ordinary_ticket == '333334'


def test_replace_lucky_ticket_2():
    ordinary_ticket = replace_lucky_ticket('333', '334')
    assert ordinary_ticket == '333334'


def test_replace_lucky_ticket_3():
    ordinary_ticket = replace_lucky_ticket('999', '999')
    assert ordinary_ticket == '999000'


def test_replace_lucky_ticket_4():
    ordinary_ticket = replace_lucky_ticket('134', '224')
    assert ordinary_ticket == '134225'


def test_replace_lucky_ticket_5():
    ordinary_ticket = replace_lucky_ticket('100', '001')
    assert ordinary_ticket == '100002'


def test_replace_lucky_ticket_6():
    ordinary_ticket = replace_lucky_ticket('101', '001')
    assert ordinary_ticket == '101001'


def test_replace_lucky_ticket_7():
    ordinary_ticket = replace_lucky_ticket('101', '011')
    assert ordinary_ticket == '101012'


def test_replace_lucky_ticket_8():
    ordinary_ticket = replace_lucky_ticket('100', '010')
    assert ordinary_ticket == '100011'
