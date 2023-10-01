from sqlalchemy import Column, Integer, String
from src.core.database import database as db


class Permissions(db.Model):
    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True, unique=True)
    nombre = Column(String(255), nullable=False, unique=True)
    # roles = relationship("Roles", secondary=role_permissions)

    def __init__(self, nombre):
        self.nombre = nombre
