from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()


def init_app(app):
	"""
	Inicialización de la aplicación
	"""
	database.init_app(app)
	config_db(app)


# Configuración de la DB
def config_db(app):
	"""
	Configuración de la app.
	close_session -> Cuando se termina un request (teardown),
	se cierra la conexión
	con la DB que se abrió
	"""
	@app.teardown_request
	def close_session(exception=None):
		database.session.close()


def reset_db():
	"""
	Reseteo de la DB.
	Lo usamos auxiliarmente. Flask me permite hacer comandos,
	ejecutaríamos esto con dicho comando
	"""
	print("Eliminando DB")
	database.drop_all()
	print("Creando DB")
	database.create_all()
