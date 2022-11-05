from flask import Flask, render_template, request
import sqlite3

def init_app():
    app = Flask(__name__)

    @app.route("/")
    def login():
        return render_template("home.html")

    @app.route("/", methods=["GET", "POST"])
    def checkLogin():
        user = request.form["User"]
        passw = request.form["Password"]
        editDB(user, passw)
        return user+passw

    return app

def editDB(user, password):
    sqlconnect = sqlite3.connect("app/info.db")
    cursor = sqlconnect.cursor()
    cursor.execute("CREATE TABLE login (user TEXT, pass TEXT)")
    cursor.execute(f"INSERT INTO login VALUES ('{user}', '{password}')")

    rows = cursor.execute("SELECT user, pass FROM login").fetchall()
    print(rows)

if __name__ == "__main__":
    init_app().run(debug=True)