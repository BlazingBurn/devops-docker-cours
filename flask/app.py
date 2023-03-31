from flask import Flask, render_template
from flask_mysqldb import MySQL 

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'  # set the MySQL user
app.config['MYSQL_PASSWORD'] = 'root'  # set the MySQL password
app.config['MYSQL_HOST'] = 'mysql'  # set the MySQL host
app.config['MYSQL_DB'] = 'sampledb'  # set the MySQL database name
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  # set the MySQL cursor class

mysql = MySQL(app)  # create a new instance of the MySQL object using the Flask app

@app.route("/")  # define the root route of the Flask app
def hello_world():
   return "<h1>Hello Mr. Mahamadou Nimaga</h1>"  # return a greeting message as HTML

@app.route('/fruits')  # define a new route for displaying fruits
def index():
   CS = mysql.connection.cursor() 
   CS.execute('''SELECT * FROM fruits''') 
   Executed_DATA = CS.fetchall()  # fetch all the results of the query and store them in a variable
   print(Executed_DATA)  # print the results to the console
   # return str(Executed_DATA)
   return render_template('fruits.html', fruits=Executed_DATA)  # render the fruits.html template with the 'fruits' variable set to the results of the query

if __name__== "__main__":
   app.run('0.0.0.0',port=5000)
