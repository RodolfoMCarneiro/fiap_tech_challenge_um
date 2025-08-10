from flask import Flask, jsonify
from app.infra.database.db_config import Books
from flasgger import swag_from

def init_category_list_route(app):
    @app.route('/api/v1/categories', methods=['GET'])
    @swag_from('docs/category_list.yaml')
    def book_category():
        query = Books.query.with_entities(Books.categoria).distinct().all()
        return jsonify([
            b.categoria
            for b in query]), 200