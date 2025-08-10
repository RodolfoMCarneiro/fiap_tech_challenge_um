import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from decimal import Decimal
import re

stars_dict = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}

def get_book_details(book_grid_information, detail_url):

    availability_number = 0
    availability_status = False

    details_response = requests.get(detail_url)
    details_soup = BeautifulSoup(details_response.content, "html.parser")

    category_soup = details_soup.find("ul", {"class": "breadcrumb"})
    category = category_soup.findAll("li")[2].text.strip()
    book_image = urljoin(detail_url, details_soup.find("img")['src'])
    availability = details_soup.find("p", {"class": "instock availability"}).text.strip()
    if 'In stock' in availability:
        availability_digits = re.findall(r'\d+', availability)
        availability_number = int(availability_digits[0])
        availability_status = True

    book_information = {
        'title': book_grid_information.h3.a['title'].strip(),
        'price': Decimal(book_grid_information.find("p", {"class":"price_color"}).text.strip().replace("£", "")),
        'rating': stars_dict[book_grid_information.find("p", {"class":"star-rating"}).get("class")[1]],
        'category': category,
        'availability_number': availability_number,
        'availability_status': availability_status,
        'book_image': book_image
    }
    return book_information

def return_scraped_books():
    books = []
    url = 'https://books.toscrape.com'
    next_page_url = url

    while next_page_url:
        response = requests.get(next_page_url)
        page_soup = BeautifulSoup(response.content, "html.parser")
        bookshelf = page_soup.findAll("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})

        for book in bookshelf:
            books.append(get_book_details(book, urljoin(next_page_url, book.h3.a['href'])))

        next_page_info = page_soup.find("li", {"class": "next"})
        if next_page_info:
            next_page_url = urljoin(next_page_url, next_page_info.a['href'])
        else:
            next_page_url = None
        
    print(books)
    return books