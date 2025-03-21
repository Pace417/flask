from flask import Flask, render_template, request, session
import hashlib, sqlite3, datetime
app = Flask(__name__)
app.secret_key = "random"

con = sqlite3.connect("database.db")
cur = con.cursor()
cur.execute("""
            CREATE TABLE IF NOT EXISTS userInfo(
            username VARCHAR(35) NOT NULL PRIMARY KEY,
            password VARCHAR(64) NOT NULL,
            joinedDate DATETIME default CURRENT_TIMESTAMP,
            accStatus BOOLEAN
            )
""")
con = sqlite3.connect("Database.db")
cur = con.cursor()
cur.execute(""" CREATE TABLE IF NOT EXISTS User(
                Username VARCHAR(20) NOT NULL PRIMARY KEY,
                Password VARCHAR(256) NOT NULL);
            """)
con.commit()
con.close()

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        encoded = request.form['Password'].encode()
        hash = hashlib.sha256(encoded).hexdigest()

        con = sqlite3.connect("Database.db")
        cur = con.cursor()
        cur.execute("INSERT INTO User (Username, Password) VALUES (?,?)",
                        (request.form['Username'],hash))
        con.commit()
        con.close()
    return "Signup Successful"

@app.route("/", methods=["GET", "POST"])


def login():
    if request.method == "GET":
        return render_template("index.html")
    else:
        encoded = request.form['Password'].encode()
        hash = hashlib.sha256(encoded).hexdigest()
        con = sqlite3.connect('Database.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM User WHERE Username=? AND Password=?",
                        (request.form['Username'],hash))
        if len(cur.fetchall()) == 0:
            return "Wrong username and password"
        else:
            session['Username'] = request.form['Username']
            return render_template("welcome.html")