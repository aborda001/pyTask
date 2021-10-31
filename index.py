from flask import Flask, render_template, request, redirect, session, jsonify, flash
import sqlite3
from functions import *

app = Flask(__name__)
database = "database.sqlite"

app.secret_key = "secret_key"

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/loguear", methods = ['POST'])
def loguear():
	username = request.form['username']
	password = request.form['password']

	sql = f"SELECT * FROM User WHERE userName = '{username}'"

	data = querySqlite(sql, database)
	if data:
		data = data[0]
		idUser = data[0]
		usernamedb = data[1]
		passworddb = data[2]
	else:
		usernamedb, passworddb = False, False
	
	if username == usernamedb and comprobePassword(password,passworddb):
		session['idUser'] = idUser
		session['username'] = usernamedb
		return redirect("/")
		
	flash("Correo o contraseña incorrectos")
	return redirect('/login')

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/logout")
def logout():
	session.pop("username", None)
	session.pop("idUser", None)
	return redirect("/login")

@app.route("/newusername", methods = ['POST'])
def newusername():
	username = request.form['username']
	password = request.form['password']
	password = hashedPassword(password)

	sql = f"SELECT userName FROM User WHERE userName = '{username}'"
	exist = querySqlite(sql, database)

	if exist:
		return jsonify({"Data":"El usuario ya existe"}),423

	sql = f"""INSERT INTO User VALUES (null,'{username}',"{password}")"""
	exist = querySqlite(sql, database)
	return jsonify({"Data":"Usuario agregado correctamente"}),200

@app.route("/newtask", methods = ['POST'])
def newtask():
	description = request.form['description']
	status = request.form['status']
	idUser = session['idUser']

	sql = f"INSERT INTO Task VALUES (null, {idUser}, '{description}', '{status}')"
	
	data = querySqlite(sql, database)

	flash("Tarea agregada correctamente")
	return redirect("/")

@app.route("/tasksearch", methods = ['POST'])
def tasksearch():
	sql = f"SELECT * FROM Task WHERE idUser = {session['idUser']}"
	tasks = querySqlite(sql, database)

	hacer = []
	haciendo = []
	hecho = []

	for task in tasks:
		if task[3] =="hacer":
			hacer.append(task)
		elif task[3] == "haciendo":
			haciendo.append(task)
		else:
			hecho.append(task)

	filterTasks = [hacer,haciendo,hecho]
	lenTasks = [len(hacer), len(haciendo), len(hecho)]
	lenTasks.append(max(lenTasks))

	return jsonify({'htmlresponse': render_template('tasklist.html', filterTasks = filterTasks, lenTasks = lenTasks)})

@app.before_request
def middleware():
	path = request.path
	publicPath = ["/login", "/loguear", "/newusername"]
	endpoint = request.endpoint

	if endpoint != 'static':
		if not 'username' in session and (path not in publicPath):
			return redirect("/login")

@app.errorhandler(404)
def notFound(e):
	return render_template("notFound.html")

if __name__ == '__main__':
	app.run(host= "127.0.0.1",
		port=5000, debug=True
		)