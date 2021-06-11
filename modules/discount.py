def calculate_discount_on_geese(price, number_of_geese):
    if 10 >= number_of_geese > 5:
        discount = price * number_of_geese * 0.25
        final_price = int(price * number_of_geese - discount)
        return final_price
    elif number_of_geese > 10:
        final_price = int(price * number_of_geese // 2)
        return final_price
    else:
        return price * number_of_geese


if __name__ == "__main__":
    price = int(input())
    goose = int(input())

    if 10 >= goose > 5:
        discount = price * goose * 0.25
        print(int(price * goose - discount))
    elif goose > 10:
        fin = price * goose // 2
        print(fin)
    else:
        print(price * goose)
