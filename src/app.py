from flask import Flask, render_template, request, flash, redirect, url_for
import os

# Specify the path to the templates folder
app = Flask(__name__)

# Generate a secure random secret key
app.secret_key = os.urandom(24)

# Sample user data (username: password)
users = {
    "admin": "password123",
    "user1": "mypassword",
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username exists and the password matches
        if username in users and users[username] == password:
            return "Login successful!"
        else:
            flash("Invalid credentials, please try again.")
            return redirect(url_for('login'))

    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
