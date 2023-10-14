import mysql.connector


connection = mysql.connector.connect(
  host="localhost",
  user="root",
  database = "fyp"
)

cursor = connection.cursor()

# app.config['SECRET_KEY'] = 'secretkey'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/fyp'