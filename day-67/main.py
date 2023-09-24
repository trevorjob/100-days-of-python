from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)

app.config['CKEDITOR_PKG_TYPE'] = 'full'
ckeditor = CKEditor(app)

# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

class NewPost(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    img_url = StringField('Image-URL', validators=[DataRequired()])
    post = CKEditorField('Post', validators= [DataRequired()])
    submit = SubmitField('Submit')

with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)


# TODO: Add a route so that you can click on individual posts.
@app.route('/<post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=['GET',"POST"])
def add_new_post():
    form = NewPost()
    if form.validate_on_submit():
        aut = form.author.data
        tit = form.title.data
        sub = form.subtitle.data
        pst = form.post.data
        img = form.img_url.data
        time = datetime.now()
        
        new_blogpost = BlogPost(author=aut, title=tit, subtitle=sub, img_url=img, body=pst, date=time.strftime('%B %m, %Y'))
        db.session.add(new_blogpost)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
        
        # print(form.author.data)
    return render_template('make-post.html', form=form, do='Make')

# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<post_id>', methods=['POST', "GET"])
def edit_post(post_id):
    old_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    form = NewPost(title=old_post.title, author=old_post.author,subtitle=old_post.subtitle, img_url=old_post.img_url,post=old_post.body)
    if form.validate_on_submit():
        old_post.title = form.title.data
        old_post.subtitle = form.subtitle.data
        old_post.author = form.author.data
        old_post.img_url = form.img_url.data
        old_post.body = form.post.data
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', do='Edit', form=form)


# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<post_id>')
def delete_post(post_id):
    post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('get_all_posts'))
    

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
