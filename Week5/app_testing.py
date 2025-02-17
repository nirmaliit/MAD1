#pip install Flask
#pip install flask-sqlalchemy
#https://code.visualstudio.com/docs/python/tutorial-flask

from flask import Flask ,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///first.sqlite3'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    
with app.app_context():  
    db.create_all()   


@app.route('/')
def hello_world():
    return 'Hello World from nirmal...!'

@app.route('/index')
def hello_index():
    users = ["Nirmal Kumar Natarajan"]
    items = ["MLP","SC","MAD1","MATHS"]
    return render_template('index.html', name = users, items=items) #'<H1> Nirmal Welcomes you.!</H1>'

if __name__ == '__main__':
    app.run(debug=True)