import bcrypt, sqlite3

def hashedPassword(password):
	"""Recibe una password en texto plano, y devuelve la contraseña 
	hasheada.
	"""
	password = password.encode()

	#La salt, es necesaria para crear un hash mas seguro
	salt = bcrypt.gensalt()
	
	password = bcrypt.hashpw(password, salt)

	return password

def querySqlite(sql, database):
	data = []
	conexion = sqlite3.connect(database)
	cursor = conexion.cursor()

	cursor.execute(sql)
	data = cursor.fetchone()

	cursor.close()
	conexion.close()

	if data:
		return data

	return "NONE", "NONE"