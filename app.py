from flask import Flask, render_template, request, hashlib

app = Flask(__name__)
h=hashlib.new("SHA256")

@app.route("/signup", methods=["GET", "POST"])
def signUp():
    if request.method== "GET":
        return render_template("signup.html")
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
