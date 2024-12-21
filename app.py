import os
from flask import Flask, render_template, request, url_for, flash, redirect
from forms import CourseForm

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

courses_list = [
    {
        'title': 'Python 101',
        'description': 'Learn Python basics',
        'price': 34,
        'available': True,
        'level': 'Beginner'
    }
]

@app.route('/', methods=('GET', 'POST'))
def index():
    form = CourseForm()
    if form.validate_on_submit():
        courses_list.append({
            'title': form.title.data,
            'description': form.description.data,
            'price': form.price.data,
            'available': form.available.data,
            'level': form.level.data
        })
        return redirect(url_for('courses'))
    return render_template("index.html", form=form)

@app.route('/courses/')
def courses():
    return render_template('courses.html', courses_list=courses_list)
