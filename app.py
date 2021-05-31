from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

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

@app.route('/appointment')
def appointment():
    return render_template('appointment.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug = True)