from flask import Flask, render_template, request, redirect, session, jsonify
import sqlite3
from functions import *

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
		session['username'] = username
		return redirect("/")

	return redirect("/login")

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/logout")
def logout():
	session.pop("username", None)
	return redirect("/login")

@app.route("/newusername", methods = ['POST'])
def newusername():
	username = request.form['username']
	password = request.form['password']
	password = hashedPassword(password)

	conexion = sqlite3.connect(baseDeDatos)
	cursor = conexion.cursor()

	cursor.execute("INSERT INTO User VALUES (null,'%s','%s')" % (username, password))
	conexion.commit()

	cursor.close()
	conexion.close()

	return jsonify({"Data":"New user added"})


@app.before_request
def middleware():
	path = request.path
	publicPath = ["/login","/static/css/styles.css", "/static/js/main.js"]

	if not 'username' in session and (path not in publicPath):
		return redirect("/login")

@app.errorhandler(404)
def notFound(e):
	return render_template("notFound.html")

if __name__ == '__main__':
	app.run(host= "127.0.0.1",
		port=5000, debug=True
		)