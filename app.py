from flask import Flask, redirect, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)
csrf = CSRFProtect(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(50), unique=True, nullable=False)
    first_name = db.Column(db.String(50), unique=True, nullable=False)
    second_name = db.Column(db.String(50), unique=True, nullable=False)
    number = db.Column(db.String(20), unique=True, nullable=False)


@app.route("/")
def index_page():
    students = Student.query.all()
    return render_template('index.html', objects=students)


@app.route("/form/", methods=['GET', 'POST'])
@app.route("/form/<int:student_id>/", methods=['GET', 'POST'])
def student_form(student_id=None):
    student = Student.query.get_or_404(student_id) if student_id else None
    if request.method == 'POST':
        if student is None:
            student = Student()
        student.last_name = request.form['last_name']
        student.first_name = request.form['first_name']
        student.second_name = request.form['second_name']
        student.number = request.form['number']
        db.session.add(student)
        db.session.commit()
        return redirect('/')
    return render_template('form.html', obj=student)


@app.route("/delete/<int:student_id>/", methods=['GET', 'POST'])
def student_delete(student_id):
    student = Student.query.get_or_404(student_id)
    if request.method == 'POST':
        db.session.delete(student)
        db.session.commit()
        return redirect('/')
    return render_template('delete.html', obj=student)
