from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from web.config.Database import myDatabase as db
from flask_login import UserMixin

class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    userID = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String, nullable = False)
    username = db.Column(db.String, unique = True, nullable = False)
    email = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable = False)
    creationDate = db.Column(db.DateTime, nullable = False)