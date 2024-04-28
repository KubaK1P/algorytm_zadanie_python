import requests


class CurrencyNotFoundError():
    pass


def get_exchange_rate(from_currency, to_currency):
    req = requests.get(
        f"https://api.coingecko.com/api/v3/simple/price?ids={from_currency}%2C{to_currency}&vs_currencies=USD")
    res = req.json()
    try:
        return res[from_currency]["usd"]/res[to_currency]["usd"]
    except Exception:
        raise CurrencyNotFoundError()


def convert_currency(amount, from_currency, to_currency):
    converted_amount = amount * get_exchange_rate(from_currency, to_currency)
    return converted_amount


amount = int(input("Podaj ilość: "))
from_currency = str(input("Z jakiej waluty: "))
to_currency = str(input("Na jaka walutę: "))

converted_amount = convert_currency(
    amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
