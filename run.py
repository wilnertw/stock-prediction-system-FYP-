from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, validators
from wtforms.validators import InputRequired
from flask_bcrypt import Bcrypt
from datetime import datetime
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
bcrypt = Bcrypt(app)

#Database Connection
db = mysql.connector.connect(
  host="localhost",
  user="root",
  database = "fyp"
)
cur = db.cursor()

@app.route('/')
def view_homepage():
    return render_template('homePage.html')

@app.route('/login_page')
def view_login(): 
    return render_template('loginPage.html')

class registerForm(FlaskForm):
    fullname = StringField('Full Name', [validators.InputRequired()])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Email(), validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
        
@app.route('/register_page', methods=['POST', 'GET'])
def signin():
    form = registerForm()
    if form.validate_on_submit():
        fullname = form.fullname.data
        username = form.username.data
        email = form.email.data
        psw = form.password.data
        hashed_psw = bcrypt.generate_password_hash(psw).decode('utf-8')
        register(fullname, username, email, hashed_psw)

    return render_template('registerPage.html', form=form)

    

# @app.route('/login', methods = ['POST', 'GET'])
# def login():
    
#     if request.method == 'POST':
#         name = request.form['name']
#         age = request.form['age']
#         cur.execute(''' INSERT INTO people VALUES(%s,%s)''',(name,age))
#         db.commit()
#         cur.close()
#         return f"YAY"
#     else:
#         return "Login via the login Form"


def register(fullname, username, email, hashed_psw):
    cur.execute('''INSERT INTO users
                    (fullName, username, email, password, creationDate) 
                    VALUES(%s,%s,%s,%s,%s) ''', (fullname, username, email, hashed_psw, datetime.now()))
    db.commit()
    cur.close()
    

if __name__ == "__main__" :
    app.run(debug=True, host='localhost', port=5000)
