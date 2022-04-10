import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.technewsworld.com/")

soup = BeautifulSoup(r.content, 'html.parser')

div_title = soup.find_all('div', class_="title")

for element in a_title:
    print(element)