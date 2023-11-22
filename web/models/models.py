from datetime import datetime
from web import login_manager
from web.config.Database import myDatabase as db
from flask_login import UserMixin, current_user
from sqlalchemy import ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase, relationship, mapped_column


class Base(DeclarativeBase):
    pass

class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    userID = mapped_column(Integer, primary_key=True)
    fullName = mapped_column(String, nullable = False)
    username = mapped_column(String, unique = True, nullable = False)
    email = mapped_column(String, nullable = False)
    password = mapped_column(String, nullable = False)
    creationDate = mapped_column(DateTime, nullable = False)
    userRank = mapped_column(Integer, nullable=True)

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
    
    try:
        return Users.query.get(int(userID))
    except:
        return None
    
class userProfile(db.Model):
    __tablename__ = 'userprofile'
    userID = mapped_column(Integer, primary_key=True)
    stockSectorPreferences = mapped_column(String, nullable = True)
    birth_date = mapped_column(DateTime, nullable = True)
    country = mapped_column(String, nullable = True)


class Feedback(db.Model):
    __tablename__ = 'feedback'
    feedbackID = mapped_column(Integer)
    userID = mapped_column(Integer, primary_key=True)
    rating = mapped_column(Integer, nullable=False)
    feedback = mapped_column(String, nullable=True)
    approved = mapped_column(Integer, nullable=False)
    
    