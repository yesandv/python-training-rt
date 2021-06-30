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
