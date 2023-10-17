from src.core.database import database as db

class Historial(db.Model):
    __tablename__ = "historial de usuarios"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    id_usuario = db.Column(db.Integer)
    rol = db.Column(db.String(255))
    institucion = db.Column(db.String(255))
    
    def __init__(self ,email, id_usuario, rol, institucion):
        self.email = email
        self.id_usuario = id_usuario
        self.rol = rol
        self.institucion = institucion