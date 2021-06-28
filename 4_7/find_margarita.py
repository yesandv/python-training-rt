def find_margarita(x, y, z, a):
    return 9 * x + 6 * y + 3 * z + 1 * a


def check_all_combinations():
    for x in range(25):
        for y in range(25):
            for z in range(25):
                for a in range(25):
                    if find_margarita(x, y, z, a) == 121:
                        print(f'Бегемот: {x}, Коровьев: {y}, Гелла: {z}, Азазелло: {a}')


if __name__ == "__main__":
    check_all_combinations()
