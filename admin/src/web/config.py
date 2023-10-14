from os import environ


class Config(object):
    #Clase base

    SECRET_KEY = "secret"
    TESTING = False
    SESSION_TYPE = "filesystem"
    
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USERNAME = 'cidepint.proyecto@gmail.com'
    MAIL_PASSWORD = 'tihdtlofndswghxw '
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAINTENANCE_MODE = False

class ProductionConfig(Config):

    DB_USER = environ.get("DB_USER")
    DB_PASS = environ.get("DB_PASS")
    DB_HOST = environ.get("DB_HOST")
    DB_NAME = environ.get("DB_NAME")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    )
    
    URL_REGISTRO = "https://admin-grupo17.proyecto2023.linti.unlp.edu.ar/sesion/confirmar_registro"
    


class DevelopmentConfig(Config):
    #Configuracion de desarollo
    
    DB_USER = "postgres"
    DB_PASS = "postgres"
    DB_HOST = "localhost"
    DB_NAME = "postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    )

    URL_REGISTRO = "http://127.0.0.1:5000/sesion/confirmar_registro"
  
class TestingConfig(Config):
    #Configuracion de testeo

    TESTING = True


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "test": TestingConfig,
}