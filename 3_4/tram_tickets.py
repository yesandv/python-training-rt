def verify_lucky_ticket(first_half, second_half):
    sum_first_half = int(first_half[0]) + int(first_half[1]) + int(first_half[2])
    sum_second_half = int(second_half[0]) + int(second_half[1]) + int(second_half[2])
    if sum_first_half == sum_second_half:
        return 'Lucky'
    else:
        return 'Ordinary'


def replace_lucky_ticket(first_half, second_half):
    ticket = verify_lucky_ticket(first_half, second_half)
    if ticket == 'Lucky':
        second_half_as_num = int(second_half)
        replaced_second_half_as_num = (second_half_as_num + 1) % 1000
        replaced_second_half = str(replaced_second_half_as_num)
        if len(replaced_second_half) < 3:
            replaced_second_half = '0' + replaced_second_half
        if len(replaced_second_half) < 3:
            replaced_second_half = '0' + replaced_second_half
        return first_half + replaced_second_half
    else:
        return first_half + second_half


if __name__ == "__main__":
    beginning = input('')
    end = input('')

    verified_ticket = verify_lucky_ticket(beginning, end)
    altered_ticket = replace_lucky_ticket(beginning, end)
    print(altered_ticket)
