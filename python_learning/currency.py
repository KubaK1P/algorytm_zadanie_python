def convert_currency(amount, from_currency, to_currency, exchange_rate):
    converted_amount = amount * exchange_rate
    return converted_amount


amount = int(input("Podaj ilość: "))  
from_currency = str(input("Z jakiej waluty: ")) 
to_currency = str(input("Na jaka walutę: "))  
exchange_rate = float(input("Stosunek zmiany: "))

converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rate)
print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
