from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homePage.html')

@app.route('/login')
def login(): 
    return render_template('loginPage.html')

@app.route('/signin')
def signin():
    return render_template('signinPage.html')

if __name__ == "__main__" :
    app.run(debug=True)