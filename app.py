from flask import Flask,request,jsonify
from flask_mysqldb import MySQL 

app = Flask(__name__)

app.config['MYSQL_USER'] = 'sql12363905'
app.config['MYSQL_PASSWORD'] = 'v7GXDSTg3h'
app.config['MYSQL_HOST'] = 'sql12.freemysqlhosting.net'
app.config['MYSQL_DB'] = 'sql12363905'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/',methods=['GET'])
def index():
    cur = mysql.connection.cursor()
    # cur.execute('''CREATE TABLE example (id INTEGER, name VARCHAR(20),email VARCHAR(20))''')
    cur.execute('''INSERT INTO example VALUES (1, 'vengi', 'vengi.@gmail.com')''')
    cur.execute('''INSERT INTO example VALUES (2, 'vengat', 'vengat.@yahoo.com')''')
    #mysql.connection.commit()

    # result =  cur.execute('''SELECT * FROM example''')
    # if result>0:
    #     userDetails = cur.fetchall()
    # print(userDetails)
    # return userDetails
    return 'Success'
    #mysql.connection.commit()

@app.route('/users',methods=['GET'])
def users():
    cur = mysql.connection.cursor()
    result =  cur.execute("SELECT * FROM example")
    userDetails = cur.fetchall()
    cur.close()
    return jsonify(userDetails)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        id = request.json['id']
        name = request.json['name']
        email = request.json['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO example (id, name, email) VALUES (%s, %s, %s)", (id, name, email))
        mysql.connection.commit()
        return 'inserted successfully'

@app.route('/delete/<int:id>', methods = ['GET'])
def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM example WHERE id=%s", (id,))
    mysql.connection.commit()
    return 'deleted'


@app.route('/update/<int:id>',methods=['POST'])
def update(id):
    if request.method == 'POST':
        # id = request.json['id']
        name = request.json['name']
        email = request.json['email']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE example
               SET name=%s, email=%s
               WHERE id=%s
            """, (name, email, id))
        mysql.connection.commit()
        return 'updated'

    