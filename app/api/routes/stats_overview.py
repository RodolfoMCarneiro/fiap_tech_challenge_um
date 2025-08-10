from flask import Flask, jsonify
from app.infra.database.db_config import Books
from flasgger import swag_from
from sqlalchemy import func

def init_stats_overview_route(app):
    @app.route('/api/v1/stats/overview', methods=['GET'])
    @swag_from('docs/stats_overview.yaml')
    def stats_overview():
        preco_medio = round(float(Books.query.with_entities(func.avg(Books.preco)).scalar() or 0), 2)
        total_livros = Books.query.count()
        distribuicao_categorias_query = Books.query.with_entities(Books.rating, func.count(Books.rating)).group_by(Books.rating).all()
        distribuicao_dict = {str(r): c for r, c in distribuicao_categorias_query}
        return jsonify(
            {
                "preco_medio": preco_medio,
                "total_livros": total_livros,
                "livros_por_rating": distribuicao_dict
            }
            ), 200