from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, Email
import  flask_bootstrap
import email_validator

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


class MyForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('submit')

app = Flask(__name__)
app.secret_key = 'blessedacademy'
bootstrap =flask_bootstrap.Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')

def success():
    return render_template('success.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    my = MyForm()
    if my.validate_on_submit():
        if my.email.data == 'admin@email.com' and my.password.data == '12345678':
            return render_template('success.html', bootstrap=bootstrap)
        else:
            return render_template('denied.html')
    return render_template('login.html', form=my, bootstrap=bootstrap)

if __name__ == '__main__':
    app.run(debug=True)
