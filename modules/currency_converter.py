transfer = input()
rub_to_gold = int(input())
usd_to_gold = int(input())
amount = int(input())


if transfer == '1':
    rub_to_usd = rub_to_gold / usd_to_gold
    rub_to_usd *= amount
    print(f'{amount} Руб это {rub_to_usd} $')
else:
    usd_to_rub = usd_to_gold / rub_to_gold
    usd_to_rub *= amount
    print(f'{amount} $ это {usd_to_rub} Руб')
