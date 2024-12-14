from flask import Flask, render_template, request, redirect, session
from db import Database
import api

app = Flask(__name__)

dbo = Database()


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/perform_registration", methods=["post"])
def perform_registration():
    userName = request.form.get("user_name")
    userEmail = request.form.get("user_email")
    userPassword = request.form.get("user_password")
    response = dbo.insert(userName, userEmail, userPassword)

    if response:
        return render_template(
            "login.html", message="Registration Successful login to continue"
        )
    else:
        return render_template(
            "register.html", message="Email already exists, enter new mail"
        )


@app.route("/perform_login", methods=["post"])
def perform_login():
    loginEmail = request.form.get("loginEmail")
    loginPassword = request.form.get("loginPassword")

    response = dbo.search(loginEmail, loginPassword)

    if response:
        return redirect("/profile")
    else:
        return render_template("login.html", loginMessage="Incorrect email or password")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/ner")
def ner():
    return render_template("ner.html")


@app.route("/perform_ner", methods=["post"])
def perform_ner():
    text = request.form.get("ner_text")
    response = api.ner(text)
    return render_template("/ner.html", response=response)


# app.run()
app.run(debug=True)  # when i reload page it will automatically show

"""' 
Connect flask to server --> POST (value not show) & GET (show value in url)
"""
