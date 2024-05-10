from flask import Flask, render_template, request, g
import sqlite3
from flask_login import LoginManager, UserMixin, login_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'

login_manager = LoginManager(app)

# Function to get the SQLite connection
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('database.db')
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Connect to SQLite database and create tables if not exist
def init_db():
    with app.app_context():
        db = get_db()
        db.execute('''CREATE TABLE IF NOT EXISTS issues
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, building TEXT, issue TEXT, description TEXT, urgency TEXT, contact TEXT)''')
        db.execute('''CREATE TABLE IF NOT EXISTS Personal
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, NetlinkId TEXT, Password TEXT, Status TEXT)''')
        db.commit()

# Remove duplicate entries from the Personal table
def remove_duplicates():
    with app.app_context():
        db = get_db()
        db.execute('''
            DELETE FROM Personal
            WHERE id NOT IN (
                SELECT MIN(id)
                FROM Personal
                GROUP BY NetlinkId, Password, Status
            )
        ''')
        db.commit()

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    with app.app_context():
        db = get_db()
        user = db.execute("SELECT * FROM Personal WHERE NetlinkId = ?", (user_id,)).fetchone()
        if user:
            return User(user[1])  # Assuming NetlinkId is unique and can be used as user ID

@login_manager.unauthorized_handler
def unauthorized():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        with app.app_context():
            db = get_db()
            user = db.execute("SELECT * FROM Personal WHERE NetlinkId = ? AND Password = ?", (username, password)).fetchone()
            if user:
                user_status = user[3]  # Assuming Status is stored in the fourth column
                login_user(User(username))
                if user_status == 'E':
                    return render_template('index3.html')
                elif user_status == 'S':
                    return render_template('index2.html')
            else:
                return console.alert('User Does Not Exist')  # Render login form again if authentication fails
    return render_template('index.html')

@app.route('/submit_issue', methods=['POST'])
def submit_issue():
    building = request.form['building']
    issue = request.form['issue']
    description = request.form['description']
    urgency = request.form['urgency']
    contact = request.form['contact']
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''INSERT INTO issues (building, issue, description, urgency, contact) VALUES (?, ?, ?, ?, ?)''', (building, issue, description, urgency, contact))
        db.commit()
    return render_template('index2.html')

if __name__ == '__main__':
    init_db()
    remove_duplicates()
    app.run(debug=True)
