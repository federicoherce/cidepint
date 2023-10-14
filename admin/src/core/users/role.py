from src.core.database import database as db


user_role = db.Table(
    "user_role",
    db.Column("user_id",
              db.Integer,
              db.ForeignKey("users.id"),
              primary_key=True),
    db.Column("role_id",
              db.Integer,
              db.ForeignKey("roles.id"),
              primary_key=True
              )
)        # Falta la parte de institucion

role_permissions = db.Table(
    "role_permissions",
    db.Column("role_id",
              db.Integer,
              db.ForeignKey("roles.id")),
    db.Column("permission_id",
              db.Integer,
              db.ForeignKey("permissions.id"))
)


class Roles(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nombre = db.Column(db.String(255), nullable=False, unique=True)
    usuarios = db.relationship("Users",
                               secondary=user_role,
                               back_populates="roles")
    permisos = db.relationship("Permissions",
                               secondary=role_permissions,
                               back_populates="roles")

    def __init__(self, nombre):
        self.nombre = nombre
