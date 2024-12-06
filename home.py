from flask import Flask,render_template,request,redirect,url_for
import sqlite3
app=Flask(__name__)

conn = sqlite3.connect('database.db')  
try:
    conn.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER)''') 
except:
    pass




@app.route('/')
def fun1():
    return "hai"

@app.route('/fun2')
def fun2():
    return "hello"

@app.route('/index',methods=['POST','GET'])
def fun3():
    name = ''
    age = ''
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        conn = sqlite3.connect('database.db')
        conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))  
        conn.commit()
        print(name,age)
        return redirect(url_for('fun3'))
    else:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()
    
        return render_template('index.html',name=name,age=age,users=users)

app.run()