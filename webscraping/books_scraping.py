import csv

import requests
from bs4 import BeautifulSoup

data = []


def main():
    url = "https://books.toscrape.com/catalogue/category/books_1/index.html"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
    for book in books:
        link = book.find("a")
        l = url[:36] + link['href'][5:]
        write_book_info(l)

    with open("./webscraping/books.xls", "w", encoding="utf-16", newline='') as file:
        writer = csv.writer(file, dialect="excel-tab")
        writer.writerow(
            [
                'Title',
                'UPC',
                'Product Type',
                'Price (excl. tax)',
                'Price (incl. tax)',
                'Tax',
                'Availability',
                'Number of reviews'
            ]
        )
        writer.writerows(data)


def write_book_info(url):
    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")

    info = s.find_all("td")

    title = s.find("h1").text.strip()
    upc = info[0].text
    product_type = info[1].text
    price_excl = info[2].text[1:]
    price_incl = info[3].text[1:]
    tax = info[4].text[1:]
    availability = info[5].text
    num_of_reviews = info[6].text

    data.append([title, upc, product_type, price_excl, price_incl, tax, availability, num_of_reviews])


if __name__ == '__main__':
    main()
