import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

PAGE_URL_PETROL = 'https://www.ndtv.com/fuel-prices/petrol-price-in-india'
PAGE_URL_DIESEL = 'https://www.ndtv.com/fuel-prices/diesel-price-in-india'

PETROL_PRICES_LIST = {}
DIESEL_PRICES_LIST = {}


def create_list(list_for, prices):
    # removing old values
    match list_for:
        case 'petrol':
            PETROL_PRICES_LIST.clear()
        case 'diesel':
            DIESEL_PRICES_LIST.clear()

    for price in prices:
        content = price.text.split('\n')
        '''
        the content consist of city price and change in price
        we will destructure the values after split the content on EOL
        '''

        city, price, change = content

        '''the price is in the form of 109.27 ₹/L,
        splitting on space and storing only the price'''

        price = price.split(' ')[0]
        price_data = {"city": city, "price": price}

        if list_for == 'petrol':
            PETROL_PRICES_LIST[city] = price_data
        elif list_for == 'diesel':
            DIESEL_PRICES_LIST[city] = price_data


def get_petrol_prices():
    page = requests.get(PAGE_URL_PETROL)
    soup = BeautifulSoup(page.content, 'html.parser')

    prices = soup.select('table tbody tr')
    # removing first tr as its not required
    prices.pop(0)

    create_list('petrol', prices=prices)

    return PETROL_PRICES_LIST


def get_diesel_prices():
    page = requests.get(PAGE_URL_DIESEL)
    soup = BeautifulSoup(page.content, 'html.parser')

    prices = soup.select('table tbody tr')
    # removing first tr as its not required
    prices.pop(0)

    create_list('diesel', prices=prices)
    return DIESEL_PRICES_LIST


# print(get_diesel_prices())
