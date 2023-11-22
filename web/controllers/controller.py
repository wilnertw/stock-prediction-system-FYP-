from web import app, admin
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, login_required, current_user, logout_user
from flask_admin.contrib.sqla import ModelView
from datetime import datetime
from ..models.forms import registerForm, loginForm, feedbackForm, profileInfo, flash_errors
from ..models.models import Users, userProfile, Feedback
from web.config.Database import myDatabase as db, cursor as cur, connection as con
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
        existing_username  = Users.query.filter_by(username = username).first()
        existing_email = Users.query.filter_by(email = email).first()
        
        if existing_username:
            flash('Username is already in use')
            return redirect(url_for('signin'))
        
        if existing_email:
            flash('Email is already in use')
            return redirect(url_for('signin'))
        
        else:
            
            user = Users(fullName = fullname,
                        username = username,
                        email = email,
                        password = generate_password_hash(password, method='sha256'), # type: ignore
                        creationDate = creationDate) # type: ignore
            
            db.session.add(user)
            db.session.commit()
            
            login_user(user)
            upProfile(current_user.userID) # type: ignore
            return redirect(url_for('profile'))
            
    else:
        flash_errors(form)
    return render_template('signinPage.html', form=form)

@app.route('/login_page', methods = ['POST', 'GET'])
def login(): 
    form = loginForm()
    user = None
    if form.validate_on_submit():
        username = form.username.data
        psw = form.password.data
        
        if username :
            user = Users.query.filter_by(username = username).first()
        
        
        if (not user or not check_password_hash(user.password, psw)): # type: ignore
            flash('Please check your login details and try again.')
            redirect(url_for('login'))
        
        elif user == None:
            flash('User does not exist. Please register')
            
        if user and check_password_hash(user.password, psw): # type: ignore
            login_user(user)
            return redirect(url_for('profile'))
    
    else:
        flash_errors(form)
    return render_template('loginPage.html', form = form)

@login_required
def upProfile(id):
    if id != None:
        profile = userProfile(userID = current_user.userID) # type: ignore
        db.session.add(profile)
        db.session.commit()
    else:
        return 'profileID not registered'


@app.route('/logged_in')
@login_required
def logged():
    
    return render_template('homePage.html')



@app.route('/profile', methods=['POST', 'GET'])
@login_required
def profile():
    user = userProfile.query.filter_by(userID=current_user.userID).first() # type: ignore
    form = profileInfo(obj=user)
    if request.method == "POST":
        
        birth_date = form.birth_date.data
        stockSectorPreferences = form.stockSectorPreferences.data
        country = form.country.data
        
        user.stockSectorPreferences = stockSectorPreferences
        user.birth_date = birth_date
        user.country = country
        db.session.commit()
        
        return redirect(url_for('profile', form=form))
        
    else:
        flash_errors(form)
    
    return render_template('profile.html', form=form) #type: ignore
    

@app.route('/delAcc', methods=['POST', 'GET'])
@login_required
def del_Acc():
    
    user = Users.query.filter_by(userID=current_user.userID).first() # type: ignore
    
    
    if request.method == "GET":
        db.session.delete(user)
        db.session.commit()
        
    return redirect(url_for('view_homepage'))
    

@app.route('/logout')    
@login_required
def whatever():
    logout_user()
    return redirect(url_for('view_homepage'))

@app.route('/feedback', methods=['POST', 'GET'])
@login_required
def feedback():
    form = feedbackForm()
    if form.validate_on_submit():
        feedback = form.feedback.data
        rating = form.rating.data
        
        if form.validate_on_submit():
            
            fback = Feedback(userID = current_user.userID, # type: ignore
                                feedback = feedback,
                                rating = rating,
                                approved = 0)
            
            db.session.add(fback)
            db.session.commit()
            
            return redirect(url_for('profile'))
            
        else:
            flash('Rating is not given!')
    
    else:
        flash_errors(form)

    return render_template('feedback.html', form=form)

admin.add_view(ModelView(userProfile, db.session))
admin.add_view(ModelView(Feedback, db.session))
admin.add_view(ModelView(Users, db.session))

@app.route('/manageUser', methods=['POST', 'GET'])
@login_required
def mngUser():

    users = Users.query.all()
    profile = userProfile.query.all()
    
    user = zip(users, profile)
    
    return render_template('manageUser.html', users = user)