import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now()
    )
    bio = db.Column(db.Text)

    def __repr__(self):
        return f'<Student {self.firstname}>'
    
@app.route('/')
def index():
    """ Index """
    students = Student.query.all()
    return render_template('index.html', students=students)

@app.route('/<int:student_id>/')
def student(student_id):
    """ Student """
    student = Student.query.get_or_404(student_id)
    return render_template('student.html', student=student)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    """ Create """
    if request.method == 'POST':
        student = Student(
            firstname = request.form['firstname'],
            lastname = request.form['lastname'],
            email = request.form['email'],
            age = request.form['age'],
            bio = request.form['bio']
        )
        db.session.add(student)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/edit/<int:student_id>/', methods=('GET','POST'))
def edit(student_id):
    """ Edit """
    student = Student.query.get_or_404(student_id)

    if request.method == 'POST':
        student.firstname = request.form['firstname']
        student.lastname = request.form['lastname']
        student.email = request.form['email']
        student.age = int(request.form['age'])
        student.bio = request.form['bio']

        db.session.add(student)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit.html', student=student)

@app.post('/delete/<int:student_id>/')
def delete(student_id):
    """ Delete """
    student = Student.query.get_or_404(student_id)

    db.session.delete(student)
    db.session.commit()

    return redirect(url_for('index'))
