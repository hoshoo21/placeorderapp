from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def greet():
    return "<h1> Wlecome to Flask <h1>"

@app.route("/login/")
def Login():
    return render_template("login.html")

app.run(debug=True)