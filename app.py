from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return render_template("index.html")
    else:
        name = request.form["name"]
        password = request.form["password"]        
        if password == "wewq":
            return 'Hello ' + name
        else:
            return "wrong password"