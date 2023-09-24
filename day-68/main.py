from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    flash,
    send_from_directory,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)

app = Flask(__name__)
app.config["SECRET_KEY"] = "blessedacademy"

# CONNECT TO DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy()
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    log_user = db.session.execute(db.select(User).where(User.id == user_id)).scalar()
    return log_user


@app.route("/")
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route("/register", methods=["POST", "GET"])
def register():
    check_user = db.session.execute(
        db.select(User).where(User.email == request.form.get("email"))
    ).scalar()
    if check_user:
        flash("you have created an account with us already, Log In instead")
        return redirect(url_for("login"))

    if request.method == "POST":
        hashed_password = generate_password_hash(
            request.form.get("password"), method="pbkdf2:sha256", salt_length=8
        )
        new_user = User(
            email=request.form.get("email"),
            password=hashed_password,
            name=request.form.get("name"),
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("secrets"))
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        nn = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if not nn:
            flash("email does not exist. Please try again")
            return redirect(url_for("login"))
        else:
            if check_password_hash(nn.password, password):
                login_user(nn)
                return redirect(url_for("secrets"))
            else:
                flash("Invalid password")
                return redirect(url_for("login"))

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route("/secrets")
@login_required
def secrets():
    # user = db.session.execute(db.select(User).where(User.id == id)).scalar()
    return render_template(
        "secrets.html", name=current_user.name, logged_in=current_user.is_authenticated
    )


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/download")
def download():
    return send_from_directory("./static/files", "cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
