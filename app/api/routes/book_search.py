from flask import Flask, jsonify, request
from app.infra.database.db_config import Books
from flasgger import swag_from

def init_book_search_route(app):
    @app.route('/api/v1/books/search', methods=['GET'])
    @swag_from('docs/book_search.yaml')
    def book_search():
        query = Books.query

        title = request.args.get('title')
        category = request.args.get('category')

        if title:
            query = query.filter(Books.titulo.ilike(f'%{title}%'))
        if category:
            query = query.filter(Books.categoria.ilike(f'%{category}%'))
        
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