from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from src.core.database import database as db
from datetime import datetime
from src.core.users.role import user_role


class Institucion(db.Model):
    __tablename__ = "instituciones"  # Nombre de la tabla
    id = Column(Integer, primary_key=True, unique=True)
    nombre = Column(String(50), nullable=False)
    informacion = Column(String(255), nullable=False)
    direccion = Column(String(50), nullable=True)
    localizacion = Column(String(100), nullable=True)
    palabras_claves = Column(String(50), nullable=False)
    horarios = Column(String(50), nullable=True)
    web = Column(String(50), nullable=True)
    contacto = Column(String(50), nullable=False)
    habilitado = Column(Boolean, default=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, nombre, informacion, localizacion, direccion, palabras_claves, horarios, web, contacto, habilitado=False):
        self.nombre = nombre
        self.informacion = informacion
        self.localizacion = localizacion
        self.direccion = direccion
        self.palabras_claves = palabras_claves
        self.horarios = horarios
        self.web = web
        self.contacto = contacto
        self.habilitado = habilitado
