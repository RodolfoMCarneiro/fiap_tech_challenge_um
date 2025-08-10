from flask import Flask, jsonify
from app.infra.database.db_config import Books
from flasgger import swag_from

def init_book_list_route(app):
    @app.route('/api/v1/books', methods=['GET'])
    @swag_from('docs/book_list.yaml')
    def book_list():
        query = Books.query.all()
        return jsonify([
            {
                "id": b.id,
                "titulo": b.titulo

            }
            for b in query]), 200