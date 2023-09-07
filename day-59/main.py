from flask import Flask, render_template
import requests
from pprint import pprint

response = requests.get('https://api.npoint.io/b5bfd648905f38e9e6cd')
all_posts = response.json()
app = Flask(__name__)
@app.route('/')
def start():
    return render_template('index.html', posts=all_posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/posts/<int:id>')
def posts(id):
    for i in all_posts:
        if i["id"] == id:
            break
    return render_template('post.html', post=i)

if __name__ == '__main__':
    app.run(debug=True)