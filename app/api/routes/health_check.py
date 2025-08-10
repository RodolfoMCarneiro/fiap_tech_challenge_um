from flask import Flask, jsonify
from app.infra.database.db_config import Books

def init_health_check_route(app):
    @app.route('/api/v1/health', methods=['GET'])
    def health_check():
        try:
            Books.query.first()
            return jsonify({"status": "ok", "database": "connected"}), 200
        except Exception as e:
            return jsonify({"status": "error", "database": "not connected"}), 500