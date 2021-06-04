def calculate_stock_price(start_price, percent):
    i = 1 + (percent / 100)
    x = f"{start_price * (i ** 12)} $"
    return x


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    i = 1 + (k / 100)
    x = n * (i ** 12)
    print(x, '$')
