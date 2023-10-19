from src.core.database import database as db


class Mantenimiento(db.Model):
    __tablename__ = "mantenimiento"

    id = db.Column(db.Integer, primary_key=True)
    mensaje = db.Column(db.String(255))
    mode = db.Column(db.Boolean, default=False)  # Corregir 'boolean' a 'Boolean'

    # Resto de los campos de la clase

    def __init__(self, mode=False, mensaje=None):
        self.mode = mode
        self.mensaje = mensaje
