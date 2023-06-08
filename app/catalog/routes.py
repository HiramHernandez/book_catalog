from flask import Blueprint
from flask import render_template

main = Blueprint('main', __name__, template_folder="templates")

@main.route('/')
def display_books():
    from app import db
    from app.catalog.models import Book
    books = Book.query.all()
    return render_template('home.html', books=books)


@main.route('/display/publisher/<publisher_id>')
def display_publisher(publisher_id):
    from app import db
    from app.catalog.models import Book, Publication
    publisher = Publication.query.filter_by(id=publisher_id).first()
    publisher_books = Book.query.filter_by(pub_id = publisher.id).all()

    return render_template('publisher.html', publisher=publisher, publisher_books=publisher_books)
