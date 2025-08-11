from flask import Flask, jsonify
from app.infra.database.db_config import Books
from flasgger import swag_from
from sqlalchemy import func

def init_stats_categories_route(app):
    @app.route('/api/v1/stats/categories', methods=['GET'])
    @swag_from('docs/stats_categories.yaml')
    def stats_categories():
        categorias_stats = Books.query.with_entities(
            Books.categoria,
            func.max(Books.preco).label('preco_maximo'),
            func.min(Books.preco).label('preco_minimo'),
            func.avg(Books.preco).label('preco_medio'),
            func.count(Books.id).label('quantidade_livros')
        ).group_by(Books.categoria).all()

        resultado = []
        for cat, max_p, min_p, avg_p, qtd in categorias_stats:
            resultado.append({
                "categoria": cat,
                "preco_maximo": round(float(max_p), 2),
                "preco_minimo": round(float(min_p), 2),
                "preco_medio": round(float(avg_p), 2),
                "quantidade_livros": qtd
            })

        return jsonify(resultado), 200