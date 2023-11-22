from web import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

# connection = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     database = "fyp"
# )

# cursor = connection.cursor()


app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/fyp'

engine = create_engine('mysql://root@localhost:3306/fyp')
connection = engine.raw_connection()
cursor = connection.cursor()

myDatabase = SQLAlchemy(app)





