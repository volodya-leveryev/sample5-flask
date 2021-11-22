from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)


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
