def split_list(general_list):
    list_of_dishes_and_prices = []
    for item in general_list:
        dish = item.split()[0]
        price = int(item.split()[1])
        list_of_dishes_and_prices.append(dish)
        list_of_dishes_and_prices.append(price)
    return list_of_dishes_and_prices


def split_list_to_list_of_tuples(dish_price_list):
    list_of_tuples = []
    dishes = dish_price_list[0:len(dish_price_list):2]
    prices = dish_price_list[1:len(dish_price_list):2]
    for i in range(0, len(dishes)):
        dish_price = (dishes[i], prices[i])
        list_of_tuples.append(dish_price)
    return list_of_tuples
