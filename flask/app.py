from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_DB'] = 'sampledb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# config = {
#    'user': 'root',
#    'password': 'root',
#    'host': 'mysql',
#    'port': '3306',
#    'database': 'sampledb'
# }

# mydb = mysql.connector.connect(host='mysql', 
#                                user ="user",
#                                password="user",
#                                database="sampledb")

print("DB connected")

# mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM fruits")

# result = mycursor.fetchall()

# mydb.close()

@app.route("/")
def hello_world():
   return "<h1>Hello Mr. Mahamadou Nimaga</h1>"

@app.route('/fruits')
def index():
   CS = mysql.connection.cursor()
   CS.execute('''SELECT * FROM fruits''')
   Executed_DATA = CS.fetchall()
   print(Executed_DATA)
   # return str(Executed_DATA)
   return render_template('fruits.html', fruits=Executed_DATA)
   # mycursor.execute("SELECT * FROM fruits")
   # fruits = mycursor.fetchall()
   # return render_template('fruits.html', fruits=fruits)
 
if __name__== "__main__":

   app.run('0.0.0.0',port=5000)