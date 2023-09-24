from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired
import requests
from pprint import pprint

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
get_details = 'https://developers.themoviedb.org/3/movies/get-movie-details'
API_KEY = 'c8dd528ea018a6f94c1e99515e6314e7'
API_ACCESS_TOK = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjOGRkNTI4ZWEwMThhNmY5NGMxZTk5NTE1ZTYzMTRlNyIsInN1YiI6IjY0ZmI4YTcxZTBjYTdmMDEyZWI2YWJiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.EyJT7V92G4BacdRwvqo7bNHh6V02g97LF0MtAzkVhgY'
db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///favorite-movies.db"
db.init_app(app)
result = ''

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    title = db.Column(db.String, nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)

class MyForm(FlaskForm):
    rating = DecimalField('rating', validators=[DataRequired()])
    review = StringField('review', validators=[DataRequired()])
    done = SubmitField('done')
    
class AddMovie(FlaskForm):
    movie_name = StringField('movie_name', validators=[DataRequired()])
    done = SubmitField('done')
    
bootstrap = Bootstrap5(app)
def add_movies(movie):
    with app.app_context():
        new_movie = Movies(
            title=movie["title"],
            year=int(movie["release_date"].split('-')[0]),
            description=movie["overview"],
            img_url=f"https://image.tmdb.org/t/p/original{movie['poster_path']}",
            rating=0.0,
            review='',
            ranking=0,
            
        )
        db.session.add(new_movie)
        db.session.commit()
        return new_movie.id

@app.route("/")
def home():
    with app.app_context():
        all_movies = db.session.execute(db.select(Movies).order_by(Movies.rating)).scalars().all()
        all_movies = sorted(all_movies, key=lambda x: x.rating, reverse=True)
        for mov in reversed(all_movies):            
            mov.ranking = all_movies.index(mov) + 1
    return render_template("index.html", all_movies=all_movies)

@app.route('/edit/<num>', methods=['POST', 'GET'])
def edit(num):
    my = MyForm()
    if my.validate_on_submit():
        with app.app_context():
            movie = db.session.execute(db.select(Movies).where(Movies.id == num)).scalar()
            movie.rating = request.form['rating']
            movie.review = request.form['review']
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=my, bootstrap=bootstrap)

@app.route('/delete/<num>')
def delete(num):
    with app.app_context():
        movie = db.session.execute(db.select(Movies).where(Movies.id == num)).scalar()
        db.session.delete(movie)
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods=['POST', 'GET'])
def add():
    global result
    addmovie = AddMovie()
    if addmovie.validate_on_submit():
        movie_name = addmovie.movie_name.data
        url = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}'
        response = requests.get(url).json()
        result = response['results']
        # pprint(result)
        return render_template('select.html', movies=result)
    return render_template('add.html', form=addmovie, bootstrap=bootstrap)
    
@app.route('/added/<id>')
def add_movie(id):
    movie = [mov for mov in result if mov['id'] == int(id)]
    if movie:
        new_id = add_movies(movie[0])
    return redirect(url_for('edit', num=new_id))
    
    
if __name__ == '__main__':
    app.run(debug=True)
