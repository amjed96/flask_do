from flask import Flask, abort
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def hello():
    """ Index route """

    return '<h1>Hello, World!</h1>'

@app.route('/about/')
def about():
    """ About route """

    return '<h3>This is a Flask web application.</h3>'

@app.route('/capitalize/<word>/')
def capitalize(word):
    """ Capitalize words """

    return f'<h1>{escape(word.capitalize())}</h1>'

@app.route('/add/<int:x>/<int:y>/')
def add(x, y):
    """ Sum 2 numbers """

    return f'<h1>{x+y}</h1>'

@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    """ Greet User """
    users = ['Bob', 'Jane', 'Adam', 'Leonard']
    try:
        return f'<h2>Hello {users[user_id]}'
    except IndexError:
        abort(404)
