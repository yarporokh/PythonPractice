import time

import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'

for page in range(11):
    response = requests.get(f"{url}page/{page}")
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    for n, quote in enumerate(quotes):
        quote_text = quote.find('span', class_='text')
        quote_author = quote.find('small', class_='author')

        text = quote_text.text.strip()
        author = quote_author.text.strip()

        print(f"{page}.{n + 1}) {text} - {author}")
        time.sleep(0.05)
