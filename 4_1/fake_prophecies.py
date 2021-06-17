def turned_out_number(name, year_of_birth):
    turned_out_number_as_str = str(year_of_birth * 4)
    turned_out_number_slice = turned_out_number_as_str[1:4]
    turned_out_number = int(turned_out_number_slice[0]) + int(turned_out_number_slice[1]) + int(turned_out_number_slice[2])
    return turned_out_number


def get_prophecy(number):
    prophecy = ""

    if number % 2 == 0:
        prophecy += "\nВас ждет уважение."

    if number % 8 == 0:
        prophecy += "\nВы будете богаты."

    if len(str(number)) == 2:
        prophecy += "\nВы проживете долгую жизнь."

    if number == 7:
        prophecy += "\nСегодня вечером вам отрежут голову. " \
                    "Аннушка уже купила подсолнечное масло, и не только купила, но даже разлила."

    if number == 8:
        prophecy += "\nВы попадете в сумасшедший дом."

    if number % 4 == 0:
        prophecy += "\nВ Вашей жизни будет великая любовь."

    if number == 24:
        prophecy += "\nВы запишете курс «Python для начинающих»!"

    if prophecy == "":
        prophecy += "\nЯ не могу предсказать вашу судьбу."

    return prophecy


if __name__ == "__main__":
    name = input("")
    year = int(input())
    prefix = "Раз, два... Меркурий в четвертом доме... луна ушла... шесть — несчастье... вечер — семь..."
    num = turned_out_number(name, year)
    fake_prophecy = get_prophecy(num)
    print(prefix, fake_prophecy)
