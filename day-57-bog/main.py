from flask import Flask, render_template
import requests

app = Flask(__name__)
URL = ' https://api.npoint.io/c790b4d5cab58020d391'
response = requests.get(URL)
all_posts = response.json()
@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:num>')
def get_page(num):
    for i in all_posts:
        if i['id'] == num:
            break
    return render_template("post.html", post=i)


if __name__ == "__main__":
    app.run(debug=True)
