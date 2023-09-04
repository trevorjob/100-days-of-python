from flask import Flask, render_template
import random
from datetime import datetime
app = Flask(__name__)
import requests

get_year = datetime.now()


@app.route('/')
def hello():
    return 'hello'

@app.route('/<check_name>')
def home(check_name):
    response_gender = requests.get(f'https://api.genderize.io?name={check_name}')
    response_age = requests.get(f'https://api.agify.io?name={check_name}')
    return render_template('index.html', year=get_year.year, age=response_age.json()['age'],
                           name=response_gender.json()['name'], gender=response_gender.json()['gender'])


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    URL = ' https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(URL)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)


