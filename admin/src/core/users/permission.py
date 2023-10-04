from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.core.database import database as db
from src.core.users.role import role_permissions


class Permissions(db.Model):
    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True, unique=True)
    nombre = Column(String(255), nullable=False, unique=True)
    roles = relationship("Roles", secondary=role_permissions, back_populates="permisos")

    def __init__(self, nombre):
        self.nombre = nombre
