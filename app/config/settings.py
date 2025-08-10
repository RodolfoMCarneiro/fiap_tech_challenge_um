class Config:
    APP_NAME = "API Scraper de Livros"
    SECRET_KEY = 'book_scraper_rmc_tc_um'
    JWT_ALGORITHM = "HS256"
    JWT_EXP_DELTA_SECONDS = 3600
    CACHE_TYPE = 'simple'
    SWAGGER = {
        'title': 'Catalogo de livros',
        'uiversion': 3
    }
    SQLALCHEMY_DATABASE_URI = 'sqlite:///books.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'sua_chave_jwt_secreta'