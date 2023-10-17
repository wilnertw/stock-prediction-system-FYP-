from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, validators, EmailField
from wtforms.validators import InputRequired
from flask import flash

class registerForm(FlaskForm):
    fullname = StringField('Full Name', [validators.InputRequired()])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = EmailField('Email Address', [validators.Email(), validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('pass_con', message='Passwords must match')
    ])
    pass_con = PasswordField('Repeat Password')
        
class loginForm(FlaskForm):
    username = StringField('Enter Email', [validators.Length(min = 4, max = 25)])
    password = PasswordField('Enter Password', [validators.DataRequired()])
    

def flash_errors(form):
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'error')
    
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
