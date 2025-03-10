from flask import Flask, render_template, request
import hashlib, sqlite3, datetime
app = Flask(__name__)
h=hashlib.new("SHA256")

con = sqlite3.connect("database.db")
cur = con.cursor()
cur.execute("""
            CREATE TABLE IF NOT EXISTS userInfo(
            username VARCHAR(35) NOT NULL PRIMARY KEY,
            password VARCHAR(20) NOT NULL,
            joinedDate DATETIME default CURRENT_TIMESTAMP,
            accStatus BOOLEAN
            )
""")

@app.route("/signup", methods=["GET", "POST"])
def signUp():
    if request.method== "GET":
        return render_template("signup.html")
    else:
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute(""" INSERT INTO userInfo (username, password, accStatus)
                        VALUES (?, ?, ?)""",
                    (request.form["name"],request.form["password"],1))
        con.commit()
        con.close()
    return "Signup succesful"


@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return render_template("index.html")
    else:
        name = request.form["name"]
        password = request.form["password"]
        if password == "123" and name == "bob":
            return 'Hello ' + name
        else:
            return "wrong password"
