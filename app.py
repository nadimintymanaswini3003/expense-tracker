from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Initialize DB
def init_db():
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  amount REAL,
                  category TEXT,
                  description TEXT,
                  date TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect("expenses.db")
    c = conn.cursor()
    c.execute("SELECT * FROM expenses ORDER BY date DESC")
    expenses = c.fetchall()
    conn.close()

    total = sum([row[1] for row in expenses])

    # Prepare category totals for chart
    category_totals = {}
    for e in expenses:
        category_totals[e[2]] = category_totals.get(e[2], 0) + e[1]

    return render_template("index.html", expenses=expenses, total=total, category_totals=category_totals)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        category = request.form['category']
        description = request.form['description']
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        conn = sqlite3.connect("expenses.db")
        c = conn.cursor()
        c.execute("INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
                  (amount, category, description, date))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template("add_expense.html")

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
