from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(250), unique=True, nullable=False)
    categoria = db.Column(db.String(120), nullable=False)
    imagem = db.Column(db.Text, unique=True, nullable=False)
    disponibilidade = db.Column(db.Boolean, default=False, nullable=False)
    qt_disponivel = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Numeric(10, 2), nullable=False)
    rating = db.Column(db.Integer, nullable=False)