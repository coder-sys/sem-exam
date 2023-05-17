
import random

def get_currencies(start, stop):
    all_currencies = {
        "USD": 1.0,
        "EUR": 0.85,
        "GBP": 0.72,
        "JPY": 109.66
    }
    result = dict(list(all_currencies.items())[start:stop])
    print("the available convertions are",list(result.keys()))
    return result
currencies = get_currencies(1,3)

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in currencies or to_currency not in currencies:
        print("Invalid currency")
        return

    if from_currency == to_currency:
        return amount

    rate = currencies[to_currency] / currencies[from_currency]
    converted_amount = amount * rate
    return converted_amount

def main():
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the currency to convert from (e.g., USD): ")
    to_currency = input("Enter the currency to convert to (e.g., EUR): ")

    converted_amount = convert_currency(amount, from_currency.upper(), to_currency.upper())
    if converted_amount:
        print(amount, from_currency," is equivalent to", converted_amount, to_currency)

main()
