import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", utc_time=datetime.datetime.now(datetime.timezone.utc))

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/comments/')
def comments():
    comment_list = [
        'this is the first comment.',
        'this is the second comment.',
        'this is the third comment.',
        'this is the fourth comment.'
    ]
    return render_template('comments.html', comments=comment_list)
