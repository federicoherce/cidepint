from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from src.core.database import database as db
from datetime import datetime
from admin.src.core.auth.role_permission import user_role


class Users(db.Model):
    __tablename__ = "users"  # Nombre de la tabla
    id = Column(Integer, primary_key=True, unique=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(100), nullable=True)
    token = Column(String(32), unique=True, nullable=True)
    activo = Column(Boolean, default=False)
    roles = relationship("Roles", secondary=user_role)
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
