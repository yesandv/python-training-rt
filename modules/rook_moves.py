def tell_if_rook_beats_another_rook(letter_1, figure_1, letter_2, figure_2):
    if letter_1 == letter_2 or figure_1 == figure_2:
        return 'Yes'
    else:
        return 'No'


if __name__ == "__main__":
    x1 = input()
    y1 = int(input())
    x2 = input()
    y2 = int(input())
    answer = tell_if_rook_beats_another_rook(x1, y1, x2, y2)
