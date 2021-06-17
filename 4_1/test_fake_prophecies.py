from fake_prophecies import turned_out_number, get_prophecy


def test_turned_out_number_1():
    num = turned_out_number("Берлиоз", 1925)
    assert num == 7


def test_turned_out_number_2():
    num = turned_out_number("Степан", 1999)
    assert num == 24


def test_turned_out_number_3():
    num = turned_out_number("Мастер", 1950)
    assert num == 8


def test_turned_out_number_4():
    num = turned_out_number("Ябвер", 2003)
    assert num == 3


def test_get_prophecy_1():
    option = get_prophecy(7)
    assert option == "\nСегодня вечером вам отрежут голову. " \
                     "Аннушка уже купила подсолнечное масло, и не только купила, но даже разлила."


def test_get_prophecy_2():
    option = get_prophecy(24)
    assert option == "\nВас ждет уважение." \
                     "\nВы будете богаты." \
                     "\nВы проживете долгую жизнь." \
                     "\nВ Вашей жизни будет великая любовь." \
                     "\nВы запишете курс «Python для начинающих»!"


def test_get_prophecy_3():
    option = get_prophecy(8)
    assert option == "\nВас ждет уважение." \
                     "\nВы будете богаты." \
                     "\nВы попадете в сумасшедший дом." \
                     "\nВ Вашей жизни будет великая любовь." \


def test_get_prophecy_4():
    option = get_prophecy(3)
    assert option == "\nЯ не могу предсказать вашу судьбу."
