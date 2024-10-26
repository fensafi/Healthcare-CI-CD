# src/app.py
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os

app = Flask(__name__)

# Connect to XAMPP MySQL Database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="CI-CD"
)

@app.route('/')
def index():
    return "Healthcare CI-CD Pipeline"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        if user:
            return "Login successful!"
        else:
            return "Invalid credentials!"
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
