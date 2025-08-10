from flask import Flask, jsonify, request
from app.infra.database.db_config import Books
from flasgger import swag_from

def init_book_price_range_route(app):
    @app.route('/api/v1/books/price-range', methods=['GET'])
    @swag_from('docs/price_range.yaml')
    def book_price_range():
        query = Books.query

        min_price = request.args.get('min', type=float)
        max_price = request.args.get('max', type=float)

        if min_price:
            query = query.filter(Books.preco >= min_price)
        if max_price:
            query = query.filter(Books.preco <= max_price)
        
        books_searched = query.all()

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
            for b in books_searched]), 200