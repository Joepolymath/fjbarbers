from enum import unique
from flask import Flask, render_template, redirect
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from forms import AppointmentForm, RegistrationForm, LoginForm
from flask import request
import os


app = Flask(__name__)

# file location or directory
project_dir = os.path.dirname(os.path.abspath(__file__))

# database file directory
database_file = "sqlite:///{}".format(os.path.join(project_dir, "appointments.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SECRET_KEY"] = 'bd72b0f78069cb14a807137debda0239'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# connecting the database file
db = SQLAlchemy(app)

class AppointmentBook(db.Model):
    # id = db.Column(db.Integer(), primary_key=True, nullable=False, unique=True, autoincrement=True)
    first_name = db.Column(db.String(30), unique=False, nullable=False, primary_key=True)
    last_name = db.Column(db.String(30), unique=False, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return "<First name: {}>".format(self.first_name)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/barbers')
def barbers():
    return render_template('barbers.html')

@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    # form = AppointmentForm()
    return render_template('appointment.html')

# @app.route('/appointmentlist')
# def appointmentList():
    
    

@app.route('/sub', methods=['GET', 'POST'])
def submitapp():
    if request.form:
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        appointment = AppointmentBook(first_name=first_name, last_name=last_name, email=email)
        db.session.add(appointment)
        db.session.commit()
        appoint = AppointmentBook.query.all()
        return redirect(url_for('home'))
    

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug = True)