from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Connect to SQLite database
conn = sqlite3.connect('database.db')
# Create table
conn.execute('''CREATE TABLE IF NOT EXISTS issues
             (id INTEGER PRIMARY KEY AUTOINCREMENT, building TEXT, issue TEXT, description TEXT, urgency TEXT, contact TEXT)''')

conn.execute('''CREATE TABLE IF NOT EXISTS Personal
             (id INTEGER PRIMARY KEY AUTOINCREMENT, NetlinkId TEXT, Password TEXT)''')
conn.commit()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username)
        if username == username and password == password:
            return render_template('index2.html')
        else:
            return render_template('index2.html')
    return render_template('index.html')

@app.route('/submit_issue', methods=['GET', 'POST'])
def submit_issue():
    if request.method == 'POST':
        building = request.form['building']
        issue = request.form['issue']
        description = request.form['description']
        urgency = request.form['urgency']
        contact = request.form['contact']
        print(contact)
        with sqlite3.connect("database.db") as users:
            cursor = users.cursor() 
            cursor.execute('''INSERT INTO issues (building, issue, description, urgency, contact) VALUES (?, ?, ?, ?, ?)''', (building, issue, description, urgency, contact))
            users.commit()
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=True)
