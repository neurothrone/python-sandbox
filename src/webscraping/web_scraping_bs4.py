import json
import time

import requests
from bs4 import BeautifulSoup

all_books = []

for page_num in range(1, 4):  # Pages 1-3
    url = f"https://books.toscrape.com/catalogue/page-{page_num}.html"
    print(f"Scraping page {page_num}...")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.find_all('article', class_='product_pod')

    for book in books:
        title = book.find('h3').find('a')['title']
        price = book.find('p', class_='price_color').text.strip()[2:]
        rating = book.find('p', class_='star-rating')['class'][1]

        all_books.append({
            'title': title,
            'price': float(price),
            'rating': rating,
            'page': page_num
        })

    print(f"Scraping page {page_num} done.")
    # time.sleep(1)  # Be respectful - wait between requests

with open("data/books.json", "w") as f:
    json.dump(all_books, f, indent=4)
