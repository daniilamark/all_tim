# pip install lxml
# pip install requests
# pip install beautifulsoup4

# scraper.py

import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')
#print(soup)

quotes = soup.find_all('span', class_='text')

#print(quotes)

for quote in quotes:
    print(quote.text)
