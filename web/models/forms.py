from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, RadioField, validators, EmailField, TextAreaField, SelectField, DateField
from wtforms.validators import InputRequired
from wtforms_alchemy import QuerySelectField
from flask import flash

COUNTRY = ("Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", 
    "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", 
    "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", 
    "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", 
    "Comoros", "Congo", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", 
    "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", 
    "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", 
    "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", 
    "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", 
    "Kiribati", "Korea, North", "Korea, South", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", 
    "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", 
    "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", 
    "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", 
    "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", 
    "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", 
    "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", 
    "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", 
    "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", 
    "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", 
    "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", 
    "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", 
    "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe")

STOCKSEC = ("Technology", "Healthcare", "Financial Services", "Consumer Discretionary", 
    "Consumer Staples", "Energy", "Utilities", "Materials", "Industrials", 
    "Telecommunication Services", "Real Estate")

class registerForm(FlaskForm):
    fullname = StringField('Full Name', [validators.InputRequired()])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = EmailField('Email Address', [validators.Email(), validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('pass_con', message='Passwords must match')
    ])
    pass_con = PasswordField('Repeat Password')
        
class loginForm(FlaskForm):
    username = StringField('Enter Username', [validators.Length(min = 4, max = 25)])
    password = PasswordField('Enter Password', [validators.DataRequired()])
    
class feedbackForm(FlaskForm):
    feedback = TextAreaField('Enter Feedback')
    rating = RadioField('Rating: ', [validators.InputRequired(), validators.DataRequired()],
                        choices=[(1,'1 Star'),(2,'2 Stars'),(3,'3 Stars'),(4,'4 Stars'),(5,'5 Stars')], 
                        default=1)
    
class profileInfo(FlaskForm):
    country = SelectField('Country', 
                           choices=[(country, country) for country in COUNTRY])
    stockSectorPreferences = SelectField('Preferred Stock Sector',
                           choices=[(stockSec, stockSec) for stockSec in STOCKSEC])
    birth_date = DateField('Enter your Birth-Date', format='%Y-%m-%d')

class manageUser(FlaskForm):
    userID = QuerySelectField()
    

def flash_errors(form):
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'error')
    
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
