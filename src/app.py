from flask import Flask, render_template, request, redirect, url_for, flash
import os  # Import the os module

app = Flask(__name__)

# Generate a secure random secret key
app.secret_key = os.urandom(24)  # Generates a random 24-byte string

# Sample user data (username: password)
users = {
    "admin": "password123",
    "user1": "mypassword",
}

@app.route('/')
def index():
    return redirect(url_for('login'))

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
