from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
db = SQLAlchemy()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-database.db"
db.init_app(app)
all_books = []


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    title = db.Column(db.String, nullable=False, unique=True)
    author = db.Column(db.String, nullable=False, unique=True)
    rating = db.Column(db.Float, nullable=False)

@app.route('/')
def home():
    with app.app_context():
        all_books = db.session.execute(db.select(Books).order_by(Books.id)).scalars().all()
    return render_template('index.html', all_books=all_books)

@app.route('/delete/<num>')
def delete(num):
    with app.app_context():
        new_rate = db.session.execute(db.select(Books).where(Books.id == num)).scalar()
        db.session.delete(new_rate)
        db.session.commit()
        return redirect(url_for('home'))   


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        with app.app_context():
            book = Books(title=request.form['title'],author=request.form['author'], rating=eval(request.form['rate']))
            db.session.add(book)
            db.session.commit()
        # all_books.append({'title': request.form['title'], 'author': request.form['author'], 'rate': eval(request.form['rate'])})
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/change_rate/<num>', methods=['POST', 'GET'])
def change(num):
    if request.method == 'POST':
        with app.app_context():
            new_rate = db.session.execute(db.select(Books).where(Books.id == num)).scalar()
            new_rate.rating = eval(request.form['rate'])
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('change.html', num=num)
if __name__ == "__main__":
    app.run(debug=True)

