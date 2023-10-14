from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, validators
from wtforms.validators import InputRequired
import mysql.connector

class registerForm(FlaskForm):
    fullname = StringField('Full Name', [validators.InputRequired()])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Email(), validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
        
class loginForm(FlaskForm):
    username = StringField('Enter Email', validators.Email())
    password = PasswordField('Enter Password', validators.DataRequired())
    
    
    
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
