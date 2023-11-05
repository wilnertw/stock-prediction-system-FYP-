from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from web import login_manager
from web.config.Database import myDatabase as db
from flask_login import UserMixin

class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    userID = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String, nullable = False)
    username = db.Column(db.String, unique = True, nullable = False)
    email = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable = False)
    creationDate = db.Column(db.DateTime, nullable = False)
    
    def get_id(self):
        return (self.userID)
    
    def is_authenticated(self):
        return super().is_authenticated
    
    def is_active(self):
        return super().is_active
    
    def is_anonymous(self):
        return super().is_anonymous
    
@login_manager.user_loader
def load_user(userID):
    return Users.query.get(int(userID))