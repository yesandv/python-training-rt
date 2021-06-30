def count_occurrences(num, list_of_numbers):
    count_of_occurrences = 0
    for number in list_of_numbers:
        if number == num:
            count_of_occurrences += 1
    return count_of_occurrences


def identify_frida(men_and_women_numbers):
    for number in men_and_women_numbers:
        occurrence = count_occurrences(number, men_and_women_numbers)
        if occurrence == 1:
            return number


if __name__ == "__main__":
    total_number_of_men = int(input("Сколько мужчин на балу? "))

    list_of_numbers = []

    for i in range(total_number_of_men):
        man_number = int(input("Укажите номер мужчины: "))
        list_of_numbers.append(man_number)
    for i in range(total_number_of_men + 1):
        woman_number = int(input("Укажите номер женщины: "))
        list_of_numbers.append(woman_number)

    frida_number = identify_frida(list_of_numbers)
    print(frida_number)
