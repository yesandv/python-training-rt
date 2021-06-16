def exchange_rub_to_usd(rub_to_gold_rate, usd_to_gold_rate):
    rub_to_usd_rate = rub_to_gold_rate / usd_to_gold_rate
    return rub_to_usd_rate


def exchange_usd_to_rub(rub_to_gold_rate, usd_to_gold_rate):
    usd_to_rub_rate = usd_to_gold_rate / rub_to_gold_rate
    return usd_to_rub_rate


def currency_converter(transfer_type, rub_rate, usd_rate, transfer_amount):
    if transfer_type == 1:
        exchange_rate = exchange_rub_to_usd(rub_rate, usd_rate)
        you_get = exchange_rate * transfer_amount
    elif transfer_type == 2:
        exchange_rate = exchange_usd_to_rub(rub_rate, usd_rate)
        you_get = exchange_rate * transfer_amount
    return you_get


if __name__ == "__main__":
    transfer_type = int(input())
    rub_to_gold = int(input())
    usd_to_gold = int(input())
    amount = int(input())

    if transfer_type == 1:
        exchange_rub_to_usd(rub_to_gold, usd_to_gold)
        final_amount_in = currency_converter(transfer_type, rub_to_gold, usd_to_gold, amount)
        print(f'{amount} руб. это {final_amount_in} $')
    elif transfer_type == 2:
        exchange_usd_to_rub(rub_to_gold, usd_to_gold)
        final_amount_in = currency_converter(transfer_type, rub_to_gold, usd_to_gold, amount)
        print(f'{amount} $ это {final_amount_in} руб.')
