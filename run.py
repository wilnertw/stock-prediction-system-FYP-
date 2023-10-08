from flask import Flask, render_template, request
from flask_bcrypt import Bcrypt
from datetime import datetime
import mysql.connector

app = Flask(__name__, static_url_path='/static')
bcrypt = Bcrypt(app)

#Database Connection
db = mysql.connector.connect(
  host="localhost",
  user="root",
  database = "fyp"
)
cur = db.cursor()

@app.route('/')
def view_homepage():
    return render_template('homePage.html')

@app.route('/login_page')
def view_login(): 
    return render_template('loginPage.html')
        
@app.route('/register_page')
def view_signin():
    return render_template('registerPage.html') 

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
    

@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
        
        fullname = request.form['fullName']
        username = request.form['username']
        email = request.form['email']
        psw = request.form['psw']
        hashed_psw = bcrypt.generate_password_hash(psw).decode('utf-8')
        cur.execute('''INSERT INTO users
                    (fullName, username, email, password, creationDate) 
                    VALUES(%s,%s,%s,%s,%s) ''', (fullname, username, email, hashed_psw, datetime.now()))
        db.commit()
        cur.close() 
        return f"Sign In Successful"
    else:
        return f"Problem with entry"




if __name__ == "__main__" :
    app.run(debug=True, host='localhost', port=5000)
