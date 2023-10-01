from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.core.database import database as db


user_role = db.Table(
    "user_role",
    Column("user_id",
           db.Integer,
           db.ForeignKey("users.id"),
           primary_key=True),
    Column("role_id",
           db.Integer,
           db.ForeignKey("roles.id"),
           primary_key=True
           )
)        # Falta la parte de institucion

role_permissions = db.Table(
    "role_permissions",
    Column("role_id",
           db.Integer,
           db.ForeignKey("roles.id")),
    Column("permission_id",
           db.Integer,
           db.ForeignKey("permissions.id"))
)


class Roles(db.Model):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, unique=True)
    nombre = Column(String(255), nullable=False, unique=True)
    usuarios = relationship("Users", secondary=user_role)
    permisos = relationship("Permissions", secondary=role_permissions)

    def __init__(self, nombre):
        self.nombre = nombre


# Tuve un problema con esta clase,
# la quise poner en otro módulo pero no me salió
# me dice que no encuentra la table Permissions
class Permissions(db.Model):
    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True, unique=True)
    nombre = Column(String(255), nullable=False, unique=True)
    # roles = relationship("Roles", secondary=role_permissions)

    def __init__(self, nombre):
        self.nombre = nombre
