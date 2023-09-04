from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return '<b>' + function() + '</b>'
    return wrapper
def make_ul(function):
    def wrapper():
        return '<u>' + function() + '</u>'
    return wrapper
def make_em(function):
    def wrapper():
        return '<em>' + function() + '</em>'
    return wrapper
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
@make_bold
@make_em
@make_ul
def say_bye():
    return 'bye'


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"<h1 style='text-align: center'>hello {name} , you are {number} years old</h1>\
    <p>so {name} how was your {number - 2} birthday</p>\
    <img src='https://media2.giphy.com/media/4Zo41lhzKt6iZ8xff9/giphy.webp?cid=ecf05e47wkcnzqtvyp0aq9u86kaxnlzlze8elozfh5h7q4wa&ep=v1_gifs_search&rid=\
           giphy.webp&ct=g '> "


if __name__ == '__main__':
    app.run(debug=True)
