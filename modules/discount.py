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
