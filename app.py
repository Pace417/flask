from flask import Flask, render_template, request, hashlib

app = Flask(__name__)
h=hashlib.new("SHA256")

@app.route("/signup", methods=["GET", "POST"])
def signUp():
    if request.method== "GET":
        return render_template("signup.html")
    else:
        f = open("login.txt", "w")
        f.write(request.form["name"] + "\n")
        f.write(request.form["password"])
        f.close()
    return "Signup succesful"


@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return render_template("index.html")
    else:
        name = request.form["name"]
        password = request.form["password"]
        f = open("login.txt", "r")
        un = f.readline().strip()
        pw = f.readline()
        if password == "wewq":
            return 'Hello ' + name
        else:
            return "wrong password"
