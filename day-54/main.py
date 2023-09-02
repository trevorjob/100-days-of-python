from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def say_bye():
    return 'bye'

if __name__ == '__main__':
    app.run()
from time import sleep


# def decorator_function(function):
#     def wrapper_function():
#         function()
#         sleep(2)
#         function()
#     return wrapper_function
#
#
# @decorator_function
# def say_hello():
#     print('hello')
#
# @decorator_function
# def say_bye():
#     print('bye')
#
#
# def say_greeting():
#     print('how are u')
#
# decorated = decorator_function(say_greeting)
# decorated()
# #
# # say_hello()
# # say_greeting()
#
