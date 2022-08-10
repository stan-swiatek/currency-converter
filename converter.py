from turtle import pensize
from requests import get
from pprint import PrettyPrinter


base_url = 'http://free.currconv.com/'

api_key = '562ddaf40c95f5d58108'


printer = PrettyPrinter()

endpoint = f'api/v7/currencies?apiKey={api_key}'


def get_currencies():
    endpoint = f'api/v7/currencies?apiKey={api_key}'
    url = base_url + endpoint
    data = get(url).json()['results']
    
    data = list(data.items())
    data.sort()
    
    return data


def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get('currencySymbol', '')
        print(f'{_id} - {name} - {symbol}')


    
def exchange_rate(currency1, currency2):
    endpoint = f'api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={api_key}'
    url = base_url + endpoint
    data = get(url).json()


    if len(data) == 0:
        print('Invalid currencies')
        return

    rate =  list(data.values())[0]

    print(f'{currency1} -> {currency2} = {rate} ')

    return rate


def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except:
        print('Invalid amount')
        return

    converted_amount = rate * amount
    print(f'{amount} {currency1} is equal to {converted_amount} {currency2}')
    return converted_amount
 
def main():
    currencies = get_currencies()


    print("This is currency converter")
    print("List - lists avaliable currencies")
    print("Convert - converts currencies")
    print("Rate - exchange rate of given currencies")
    print()

    while True:
        command = input("Provide command(q to quit): ").lower()

        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter base currency: ").upper()
            amount = input(f'Enter amount in {currency1}: ')
            currency2 = input('Enter a currency to convert to: ').upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter base currency: ").upper()
            currency2 = input('Enter a currency to convert to: ').upper()
            exchange_rate(currency1, currency2)
        else:
            print("Command not found")





main()