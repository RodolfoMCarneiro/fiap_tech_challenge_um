from flask import Flask
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy
from app.config.settings import Config
from app.infra.database.db_config import db
from app.api.routes.scraper import init_scraper_routes
from app.api.routes.book_list import init_book_list_route
from app.api.routes.book_detail import init_book_detail_route
from app.api.routes.book_search import init_book_search_route
from app.api.routes.category_list import init_category_list_route
from app.api.routes.health_check import init_health_check_route
from app.api.routes.price_range import init_book_price_range_route
from app.api.routes.stats_overview import init_stats_overview_route
from app.api.routes.book_top_rated import init_book_top_rated_route
from app.api.routes.stats_categories import init_stats_categories_route

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    Swagger(app)

    init_scraper_routes(app)
    init_book_list_route(app)
    init_book_detail_route(app)
    init_book_search_route(app)
    init_category_list_route(app)
    init_health_check_route(app)
    init_book_price_range_route(app)
    init_stats_overview_route(app)
    init_book_top_rated_route(app)
    init_stats_categories_route(app)

    
    return app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Banco de dados criado!")
    app.run(debug=True)