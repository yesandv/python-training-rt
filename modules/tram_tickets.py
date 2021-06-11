def verify_lucky_ticket(first_half, second_half):
    a = int(first_half[0])
    b = int(first_half[1])
    c = int(first_half[2])
    x = int(second_half[0])
    y = int(second_half[1])
    z = int(second_half[2])
    if (a + b + c) == (x + y + z):
        return 'Lucky'
    else:
        return 'Ordinary'


def replace_lucky_ticket(first_half, second_half):
    ticket = verify_lucky_ticket(first_half, second_half)
    if ticket == 'Lucky':
        if second_half == '999':
            replaced_second_half = second_half.replace('999', '000')
            return first_half + replaced_second_half
        else:
            replaced_second_half = int(second_half) + 1
            return first_half + str(replaced_second_half)
    else:
        return first_half + second_half


if __name__ == "__main__":
    part_1 = str(input(''))
    a = int(part_1[0])
    b = int(part_1[1])
    c = int(part_1[2])

    part_2 = str(input(''))
    x = int(part_2[0])
    y = int(part_2[1])
    z = int(part_2[2])


    if (a + b + c) == (x + y + z):
        if part_2 == '999':
            replaced_part_2 = part_2.replace('999', '000')
            print(part_1 + replaced_part_2)
        else:
            replaced_part_2 = int(part_2) + 1
            print(part_1 + str(replaced_part_2))
    else:
        print(part_1 + part_2)
