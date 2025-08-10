from flask import Flask, jsonify
from app.infra.database.db_config import Books
from flasgger import swag_from

def init_book_detail_route(app):
    @app.route('/api/v1/books/<int:book_id>', methods=['GET'])
    @swag_from('docs\\book_detail.yaml')
    def book_detail(book_id):
        query = Books.query.filter(Books.id == book_id).all()
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