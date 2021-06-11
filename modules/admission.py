def get_admission_fee_for_category(category):
    if category == 'Ребенок':
        return 5
    elif category == 'Милиционер':
        return 5
    elif category == 'Член профсоюза':
        return 10
    elif category == 'Не член профсоюза':
        return 30


def calculate_total_admission(tourist_1, tourist_2, tourist_3):
    fee_1 = get_admission_fee_for_category(tourist_1)
    fee_2 = get_admission_fee_for_category(tourist_2)
    fee_3 = get_admission_fee_for_category(tourist_3)
    total = fee_1 + fee_2 + fee_3
    return total


if __name__ == "__main__":
    tourist_1 = input('Турист 1: ')
    tourist_2 = input('Турист 2: ')
    tourist_3 = input('Турист 3: ')
    admission = calculate_total_admission(tourist_1, tourist_2, tourist_3)
    print(admission)
