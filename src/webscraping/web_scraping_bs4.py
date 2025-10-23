# Step 1: Import libraries and fetch a page
import requests
from bs4 import BeautifulSoup

# Fetch the books page
url = "https://books.toscrape.com/"
response = requests.get(url)

# Step 2: Create BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Find the page title
title = soup.find('title').text
print(f"Page Title: {title}")

# Find how many books are on the page
books = soup.find_all('article', class_='product_pod')
print(f"\nNumber of books on this page: {len(books)}")