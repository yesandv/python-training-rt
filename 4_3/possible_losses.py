def split_list(general_list):
    list_of_dishes_and_prices = []
    for item in general_list:
        dish = item.split()[0]
        price = int(item.split()[1])
        list_of_dishes_and_prices.append(dish)
        list_of_dishes_and_prices.append(price)
    return list_of_dishes_and_prices
