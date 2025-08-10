import csv
from app.infra.database.db_config import db, Books

def save_books_to_csv(books_information, filename='books.csv'):
    if not books_information:
        return

    keys = books_information[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(books_information)
    return

def save_books_to_db(books_information):
    if not books_information:
        return

    for book_info in books_information:
        book = Books.query.filter_by(titulo=book_info['title']).first()
        if book:
            book.categoria = book_info['category']
            book.imagem = book_info['book_image']
            book.disponibilidade = book_info['availability_status']
            book.qt_disponivel = book_info['availability_number']
            book.preco = book_info['price']
            book.rating = book_info['rating']
        else:
            book = Books(
                titulo=book_info['title'],
                categoria=book_info['category'],
                imagem=book_info['book_image'],
                disponibilidade=book_info['availability_status'],
                qt_disponivel=book_info['availability_number'],
                preco=book_info['price'],
                rating=book_info['rating']
            )
            db.session.add(book)
    db.session.commit()
    return