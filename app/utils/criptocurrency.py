import requests

COINGECKO_API = 'https://api.coingecko.com/api/v3/simple/price?'
BASE = 10 ** 8

def get_current_price(id):
    response = requests.get(f'{COINGECKO_API}ids={id}&vs_currencies=usd')
    
    if response.status_code == 200:
        return response.json()[id]['usd']

def convert(amount, id):
    try:
        current_price = get_current_crypto_price(id)
        
        return (1.0 / current_price ) * amount
    except Exception as err:
        
        return None