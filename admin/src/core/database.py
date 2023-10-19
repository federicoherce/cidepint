from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()


def init_app(app):
	"""
	Inicialización de la aplicación
	"""
	database.init_app(app)
	config_db(app)


def config_db(app):
	@app.teardown_request
	def close_session(exception=None):
		database.session.close()


def reset_db():
    print("Eliminando DB")
    database.drop_all()
    print("Creando DB")
    database.create_all()
