from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)
baseDeDatos = "database.sqlite"

app.secret_key = "secret_key"

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/loguear", methods = ['POST'])
def loguear():
	username = request.form['username']
	password = request.form['password']

	if username == usernamedb and password == passworddb:
		return redirect("/")

	return redirect("/login")

@app.route("/login")
def login():
	return render_template("login.html")

@app.before_request
def middleware():
	path = request.path

	if path != "/login":
		return redirect("/login")

@app.errorhandler(404)
def notFound(e):
	return render_template("notFound.html")

if __name__ == '__main__':
	app.run(host= "127.0.0.1",
		port=5000, debug=True
		)