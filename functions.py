import bcrypt

def hashedPassword(password):
	"""Recibe una password en texto plano, y devuelve la contraseña 
	hasheada.
	"""
	password = password.encode()

	#La salt, es necesaria para crear un hash mas seguro
	salt = bcrypt.gensalt()
	
	password = bcrypt.hashpw(password, salt)

	return password
