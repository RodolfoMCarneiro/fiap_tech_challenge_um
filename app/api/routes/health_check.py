from flask import Flask, jsonify
from app.infra.database.db_config import Books
from flasgger import swag_from

def init_health_check_route(app):
    @app.route('/api/v1/health', methods=['GET'])
    @swag_from('docs/health_check.yaml')
    def health_check():
        try:
            Books.query.first()
            return jsonify({"status": "ok", "database": "Conexão com database ativa"}), 200
        except Exception as e:
            return jsonify({"status": "error", "database": "Falha na conexão ao database"}), 500