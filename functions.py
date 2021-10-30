import bcrypt, sqlite3

def hashedPassword(password):
	"""Recibe una password en texto plano, y devuelve la contraseña 
	hasheada.
	"""
	password = password.encode()

	#La salt, es necesaria para crear un hash mas seguro
	salt = bcrypt.gensalt()
	
	password = bcrypt.hashpw(password, salt)

	return password.decode()

def querySqlite(sql, database):
	"""Recibe la consulta y la base de datos al cual hacer la consulta,
		si es un 'SELECT' devuelve los datos obtenidos, sino realiza los cambios
		en caso que sea un 'INSERT' o 'UPDATE'
	"""
	data = []
	conexion = sqlite3.connect(database)
	cursor = conexion.cursor()

	cursor.execute(sql)

	if (sql.split()[0].lower() == 'select' ):
		data = cursor.fetchall()
	conexion.commit()

	cursor.close()
	conexion.close()

	return data

def comprobePassword(password, passworddb):
	"""Contrasenas a comparar de tipo 'str', las convierte a bytes
	y luego deuvuelve la comparacion de ambos
	"""
	password = password.encode()
	passworddb = passworddb.encode()
	
	return bcrypt.checkpw(password, passworddb)

	
