def check_same_or_opposite_sign(first_particle, second_particle):
    if first_particle > 0 and second_particle > 0:
        return 'Одноименные'
    elif first_particle < 0 and second_particle < 0:
        return 'Одноименные'
    else:
        return 'Разноменные'


if __name__ == "__main__":
    first = int(input())
    second = int(input())

    if first > 0 and second > 0:
        print('Одноименные')
    elif first < 0 and second < 0:
        print('Одноименные')
    else:
        print('Разноменные')
