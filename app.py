from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Helper function to easily access the database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Allows accessing columns by name
    return conn

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report-lost", methods=["GET", "POST"])
def report_lost():
    if request.method == "POST":
        item_name = request.form['item_name']
        description = request.form['description']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO lost_items (item_name, description) VALUES (?, ?)',
                     (item_name, description))
        conn.commit()
        conn.close()
        return redirect(url_for('matches'))
        
    return render_template("report_lost.html")

@app.route("/report-found", methods=["GET", "POST"])
def report_found():
    if request.method == "POST":
        item_name = request.form['item_name']
        description = request.form['description']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO found_items (item_name, description) VALUES (?, ?)',
                     (item_name, description))
        conn.commit()
        conn.close()
        return redirect(url_for('matches'))
        
    return render_template("report_found.html")

@app.route("/matches")
def matches():
    conn = get_db_connection()
    lost = conn.execute('SELECT * FROM lost_items').fetchall()
    found = conn.execute('SELECT * FROM found_items').fetchall()
    conn.close()
    return render_template("matches.html", lost_items=lost, found_items=found)

if __name__ == "__main__":
    app.run(debug=True)
