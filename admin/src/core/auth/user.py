from sqlalchemy import Column, Integer, String
from src.core.database import database as db
from datetime import datetime



class Users(db.Model):
    __tablename__ = "users"  # Nombre de la tabla
    id = Column(Integer, primary_key=True, unique=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(100), nullable=True)
    token = Column(String(32), unique=True, nullable=True)
    
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, nombre, apellido, email, token, password=None):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.token = token
        self.password = password
