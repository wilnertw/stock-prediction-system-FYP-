from web import app
from flask import render_template
from datetime import datetime
from ..models.forms import registerForm, loginForm
from ..models.models import Users
from web.config.Database import myDatabase as db
from werkzeug.security import generate_password_hash

@app.route('/')
def view_homepage():
    return render_template('homePage.html')

@app.route('/signin_page', methods=['POST', 'GET'])
def signin():
    form = registerForm()
    if form.validate_on_submit():
        
        
        
        user = Users(fullname = form.fullname.data,
                     username = form.username.data,
                     email = form.email.data,
                     password = form.password.data,
                     creationDate = datetime.now())

        db.session.add(user)
        db.session.commit()
    return render_template('signinPage.html', form=form)

@app.route('/login_page')
def view_login(): 
    f = loginForm()
    if f.validate_on_submit():
        username = f.username.data
        psw = f.password.data
    
    return render_template('loginPage.html')

# @app.route('/signin', methods=["GET", "POST"])
# def register():
#     form = registerForm(request.form, csrf_enabled=False)
#     if form.validate_on_submit():
#         new_user = User(fullname = form.fullname.data,
#                 email=form.email.data,
#                 username=form.username.data,
#                 password=form.password.data)
#         db.session.add(new_user)
#         db.session.commit()
#     return render_template('signinPage.html', form=form)

# @app.route('/signin', methods=['POST', 'GET'])
# def view_signin():
#     f = registerForm()
#     if f.validate_on_submit():
#         fullname = f.fullname.data
#         username = f.username.data
#         email = f.email.data
#         psw = f.password.data

#     return render_template('signinPage.html', form=f)
    