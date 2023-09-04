from flask import Flask
import random

app = Flask(__name__)
rand_num = random.randint(0, 9)
@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>"


@app.route('/<int:num>')
def detect(num):
    global rand_num
    if num == rand_num:
        rand_num = random.randint(0, 9)
        return "<h1 style=color: green>you found it congratulations</h1>" \
               "<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>"
    elif num > rand_num:
        return "<h1 style=color: red>too high</h1>" \
               "<img src= https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>"
    else:
        return "<h1 style=color: brown>too low</h1>" \
               "<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>"


if __name__ == '__main__':
    app.run(debug=True)