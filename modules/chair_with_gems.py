def compare_chairs_weight(chair_1, chair_2, chair_3, chair_4):
    heaviest_chair = max(chair_1, chair_2, chair_3, chair_4)

    if heaviest_chair == chair_1:
        return 1
    elif heaviest_chair == chair_2:
        return 2
    elif heaviest_chair == chair_3:
        return 3
    else:
        return 4


if __name__ == "__main__":
    c1 = int(input())
    c2 = int(input())
    c3 = int(input())
    c4 = int(input())

    x = max(c1, c2, c3, c4)

    if x == c1:
        print(1)
    elif x == c2:
        print(2)
    elif x == c3:
        print(3)
    else:
        print(4)
