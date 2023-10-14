import flask_sqlalchemy
import mysql.connector
from datetime import datetime
from web.config.Database import myDatabase as db





class Users(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String, nullable = False)
    username = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable = False)
    creationDate = db.Column(db.DateTime, nullable = False)

