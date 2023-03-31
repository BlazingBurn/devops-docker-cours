from flask import Flask, render_template
import mysql.connector

config = {
   'user': 'root',
   'password': 'root',
   'host': 'mysql',
   'port': '3306',
   'database': 'sampledb'
}

mydb = mysql.connector.connect(host='mysql', 
                               user ="user",
                               password="user",
                               database="sampledb")

print("DB connected")

mycursor = mydb.cursor()

app = Flask(__name__)

mycursor.execute("SELECT * FROM fruits")

result = mycursor.fetchall()

mydb.close()

@app.route("/")
def hello_world():
   return "<h1>Hello Mr. Mahamadou Nimaga</h1>"

@app.route('/fruits')
def index():
    mycursor.execute("SELECT * FROM fruits")
    fruits = mycursor.fetchall()
    return render_template('fruits.html', fruits=fruits)
 
if __name__== "__main__":

   app.run('0.0.0.0',port=5000)