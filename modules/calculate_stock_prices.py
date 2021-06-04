def calculate_stock_price(start_price, percent):
    increase = 1 + (percent / 100)
    final_price = start_price * (increase ** 12)
    return final_price


def price_in_usd(final_price):
    return f'{final_price} $'


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    price = calculate_stock_price(n, k)
    in_currency = price_in_usd(price)
    print(in_currency)
