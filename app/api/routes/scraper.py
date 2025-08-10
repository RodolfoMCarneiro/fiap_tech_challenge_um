from flask import Flask
from data.script import return_scraped_books
from data.persist_data import save_books_to_csv, save_books_to_db

def init_scraper_routes(app):
    @app.route('/scrape_to_csv', methods=['GET'])
    def scrape_to_csv():
        book_list = return_scraped_books()
        if not book_list:
            return "No books found", 404
        else:
            save_books_to_csv(book_list)
            return "Scraping finished", 200
        
    @app.route('/scrape_to_database', methods=['GET'])
    def scrape_to_database():
        book_list = return_scraped_books()
        if not book_list:
            return "No books found", 404
        else:
            save_books_to_db(book_list)
            return "Scraping finished", 200