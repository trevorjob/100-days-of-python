import smtplib
from datetime import date
from functools import wraps

from flask import Flask, abort, flash, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_sqlalchemy import SQLAlchemy

# Import your forms from the forms.py
from forms import CommentForm, CreatePostForm, LoginForm, RegisterForm
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash, generate_password_hash

from twilio.rest import Client

API_KEY = "6e6df90dee7e0103aaf90c6d58b8a226"
account_sid = "AC432d529261c943b35a841d281db3b3d5"
auth_token = "a00c75e55258ee09dfefbb63687624a5"
"""
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
"""

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
ckeditor = CKEditor(app)
Bootstrap5(app)

# TODO: Configure Flask-Login


# CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
db = SQLAlchemy()
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)


# CONFIGURE TABLES
gravatar = Gravatar(app=app, rating="x")


# TODO: Create a User table for all your registered users.
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="user")


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    comms = relationship("Comment", back_populates="bpost")


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    user = db.Column(db.String(250), nullable=False)
    bpost = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    bpost_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    user = relationship("User", back_populates="comments")
    bpost = relationship("BlogPost", back_populates="comms")


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    log_user = db.session.execute(db.select(User).where(User.id == user_id)).scalar()
    return log_user


def admin_only(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        if current_user.id == 1:
            return function(*args, **kwargs)
        else:
            return abort(403)

    return wrapped


# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegisterForm()
    if request.method == "POST":
        if register_form.validate_on_submit:
            name = register_form.data.get("name")
            email = register_form.data.get("email")
            password = register_form.data.get("password")
            new_pass = generate_password_hash(
                password, method="pbkdf2:sha256", salt_length=8
            )
            user = db.session.execute(
                db.select(User).where(User.email == email)
            ).scalar()

            if user:
                flash("you already signed up with this email, login instead")
                return redirect(url_for("login"))
            else:
                new_user = User(name=name, email=email, password=new_pass)
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)

                return redirect(url_for("get_all_posts"))

    return render_template("register.html", form=register_form)


# TODO: Retrieve a user from the database based on their email.
@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = db.session.execute(
            db.select(User).where(User.email == login_form.data.get("email"))
        ).scalar()
        if user is not None:
            if check_password_hash(user.password, login_form.data.get("password")):
                login_user(user)
                return redirect(url_for("get_all_posts"))
            else:
                flash("invalid password, please try again")
                return redirect(url_for("login"))
        else:
            flash("the email address does not exist, please try again")
            return redirect(url_for("login"))
    return render_template("login.html", form=login_form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("get_all_posts"))


@app.route("/")
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, current_user=current_user)


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=["POST", "GET"])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    form = CommentForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            comm = Comment(text=form.body.data, user=current_user, bpost=requested_post)
            db.session.add(comm)
            db.session.commit()
            return redirect(url_for("show_post", post_id=post_id))
        else:
            flash("you need to log in/register to comment")
            return redirect(url_for("login"))

    return render_template(
        "post.html", post=requested_post, current_user=current_user, form=form
    )


# TODO: Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y"),
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, current_user=current_user)


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body,
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template(
        "make-post.html", form=edit_form, is_edit=True, current_user=current_user
    )


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


@app.route("/about")
def about():
    return render_template("about.html", current_user=current_user)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        phone = request.form["phone"]

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"Hello Nandom\nfrom:{name}\n\nEmail: {email}\nphone: {phone}\n\n{message}",
            from_="+17623095622",
            to="+2348104899622",
        )
        print(message.sid)

    return render_template("contact.html", current_user=current_user)


if __name__ == "__main__":
    app.run(debug=True, port=5002)
