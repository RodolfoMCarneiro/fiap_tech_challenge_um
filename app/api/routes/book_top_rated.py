from flask import Flask, jsonify
from app.infra.database.db_config import Books
from flasgger import swag_from

def init_book_top_rated_route(app):
    @app.route('/api/v1/books/top-rated', methods=['GET'])
    @swag_from('docs/book_top_rated.yaml')
    def book_top_rated():
        query = Books.query.order_by(Books.rating.desc()).limit(20).all()
        return jsonify([
            {
                "id": b.id,
                "titulo": b.titulo,
                "categoria": b.categoria,
                "imagem": b.imagem,
                "disponibilidade": b.disponibilidade,
                "quantidade_disponivel": b.qt_disponivel,
                "preco": b.preco,
                "rating": b.rating

            }
            for b in query]), 200