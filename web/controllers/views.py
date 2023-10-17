from web import app
from flask import render_template, redirect, url_for, flash
from datetime import datetime
from ..models.forms import registerForm, loginForm, flash_errors
from ..models.models import Users
from web.config.Database import myDatabase as db
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def view_homepage():
    return render_template('homePage.html')


@app.route('/signin_page', methods=['POST', 'GET'])
def signin():
    form = registerForm()
    
    if form.validate_on_submit():
        
        fullname = form.fullname.data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        creationDate = datetime.now()
        
        #Returns a user if user already exist in database
        existing_user = Users.query.filter_by(username = username).first()
        
        if existing_user:
            flash('Username is already in use')
            return redirect(url_for('signin'))
        
        else:
            
            user = Users(fullName = fullname,
                        username = username,
                        email = email,
                        password = generate_password_hash(password, method='sha256'),
                        creationDate = creationDate)
        
            db.session.add(user)
            db.session.commit()
    else:
        flash_errors(form)
    return render_template('signinPage.html', form=form)

@app.route('/login_page', methods = ['POST', 'GET'])
def login(): 
    form = loginForm()
    if form.validate_on_submit():
        username = form.username.data
        psw = form.password.data
        
        user = Users.query.filter_by(username = username).first()
        
        if not user or not check_password_hash(user.password, psw):
            flash('Please check your login details and try again.')
            redirect(url_for('login'))
    
    return render_template('loginPage.html', form = form)


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
    