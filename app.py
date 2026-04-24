from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

# DB connection
def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize DB
def init_db():
    conn = get_db()

    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    ''')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            name TEXT,
            phone TEXT,
            email TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Root route
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/dashboard')
    return redirect('/login')

# ---------------- AUTH ---------------- #

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        u = request.form['username']
        p = request.form['password']

        conn = get_db()
        conn.execute("INSERT INTO users (username, password) VALUES (?, ?)", (u, p))
        conn.commit()
        conn.close()

        return redirect('/login')

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        u = request.form['username']
        p = request.form['password']

        conn = get_db()
        user = conn.execute("SELECT * FROM users WHERE username=? AND password=?", (u, p)).fetchone()
        conn.close()

        if user:
            session['user_id'] = user['id']
            return redirect('/dashboard')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

# ---------------- CONTACTS ---------------- #

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')

    conn = get_db()
    contacts = conn.execute("SELECT * FROM contacts WHERE user_id=?", (session['user_id'],)).fetchall()
    conn.close()

    return render_template('dashboard.html', contacts=contacts)


@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if 'user_id' not in session:
        return redirect('/login')

    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        conn = get_db()
        conn.execute("INSERT INTO contacts (user_id, name, phone, email) VALUES (?, ?, ?, ?)",
                     (session['user_id'], name, phone, email))
        conn.commit()
        conn.close()

        return redirect('/dashboard')

    return render_template('add_contact.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_contact(id):
    if 'user_id' not in session:
        return redirect('/login')

    conn = get_db()

    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        conn.execute("UPDATE contacts SET name=?, phone=?, email=? WHERE id=?",
                     (name, phone, email, id))
        conn.commit()
        conn.close()

        return redirect('/dashboard')

    contact = conn.execute("SELECT * FROM contacts WHERE id=?", (id,)).fetchone()
    conn.close()

    return render_template('edit_contact.html', contact=contact)


@app.route('/delete/<int:id>')
def delete_contact(id):
    if 'user_id' not in session:
        return redirect('/login')

    conn = get_db()
    conn.execute("DELETE FROM contacts WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect('/dashboard')


if __name__ == "__main__":
    init_db()
    app.run(debug=True)