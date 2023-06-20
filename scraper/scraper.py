import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

PAGE_URL_PETROL = 'https://www.ndtv.com/fuel-prices/petrol-price-in-india'
PAGE_URL_DIESEL = 'https://www.ndtv.com/fuel-prices/diesel-price-in-india'

PETROL_PRICES_LIST = []
DIESEL_PRICES_LIST = []

page = requests.get(PAGE_URL_PETROL)
soup = BeautifulSoup(page.content, 'html.parser')

prices = soup.select('table tbody tr')
prices.pop(0)


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
    price_data = {city, price}
    PETROL_PRICES_LIST.append(price_data)

print(PETROL_PRICES_LIST)
