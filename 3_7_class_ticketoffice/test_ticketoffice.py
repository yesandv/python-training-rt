from ticketoffice import TicketOffice


def test_set_tickets_pricing():
    office = TicketOffice()
    tickets_pricing = office.get_tickets_pricing(['Дети', 5, 'Соц. работники', 5, 'Молодежь', 10, 'Взрослые', 30])
    assert tickets_pricing == {'Дети': 5, 'Соц. работники': 5, 'Молодежь': 10, 'Взрослые': 30}


def test_calculate_total_amount_by_group_1():
    office = TicketOffice()
    office.get_tickets_pricing(['Дети', 5, 'Соц. работники', 5, 'Молодежь', 10, 'Взрослые', 30])
    total_amount = office.calculate_total_amount_by_group(['Дети', 10])
    assert total_amount == 50


def test_calculate_total_amount_by_group_2():
    office = TicketOffice()
    office.get_tickets_pricing(['Дети', 5, 'Соц. работники', 5, 'Молодежь', 10, 'Взрослые', 30])
    total_amount = office.calculate_total_amount_by_group(['Дети', 10, 'Взрослые', 2])
    assert total_amount == 110


def test_calculate_proceeds_1():
    office = TicketOffice()
    office.get_tickets_pricing(['Дети', 5, 'Соц. работники', 5, 'Молодежь', 10, 'Взрослые', 30])
    office.calculate_total_amount_by_group(['Дети', 7, 'Молодежь', 4])
    proceeds = office.calculate_proceeds()
    assert proceeds == 75


def test_calculate_proceeds_2():
    office = TicketOffice()
    office.get_tickets_pricing(['Дети', 5, 'Соц. работники', 5, 'Молодежь', 10, 'Взрослые', 30])
    office.calculate_total_amount_by_group(['Дети', 10, 'Взрослые', 2])
    office.calculate_total_amount_by_group(['Молодежь', 5, 'Соц. работники', 3])
    proceeds = office.calculate_proceeds()
    assert proceeds == 175
