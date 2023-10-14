import mysql.connector
from web.config.Database import connection as db, cursor as cur
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

def new_user(fullname, username, email, psw):
    
    hashed_psw = generate_password_hash(psw)
    
    
    
    cur.execute('''INSERT INTO users
                    (fullName, username, email, password, creationDate) 
                    VALUES(%s,%s,%s,%s,%s) ''', (fullname, username, email, hashed_psw, datetime.now()))
    db.commit()
    cur.close()
    