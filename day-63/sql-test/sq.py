from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String, unique=True, nullable=False)
#     email = db.Column(db.String)
#
# with app.app_context():
#     users = User.query.all()
#     # db.create_all()
#     # user = User(id=3,username='james', email='redeks123456@gmail.com')
#     # db.session.add(user)
#     # db.session.commit()
# #     users = db.session.execute(db.select(User).order_by(User.username)).scalar()
# # # db.session.commit()
# # print(users[0])


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    title = db.Column(db.String, nullable=False, unique=True)
    author = db.Column(db.String, nullable=False, unique=True)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()
    book = Books(id=1, title='harry potter', author='J.K Rowling', rating=9.3)
    db.session.add(book)
    db.session.commit()

# TO CREATE
with app.app_context():
    db.create_all()

# TO READ
with app.app_context():
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars()

# TO UPDATE
with app.app_context():
    book_to_update = db.session.execute(db.select(Books).where(Books.title == "Harry Potter")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

book_id = 1
with app.app_context():
    # book_to_update = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    book_to_update = db.get_or_404(Books, book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()

# TO DELETE
book_id = 1
with app.app_context():
    # book_to_delete = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    book_to_delete = db.get_or_404(Books, book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.delete(book_to_delete)
    db.session.commit()
