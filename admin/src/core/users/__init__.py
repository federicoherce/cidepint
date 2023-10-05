from src.core.users.role import Roles
from src.core.users.permission import Permissions
from src.core.database import database as db


def create_role(**kwargs):
    role = Roles(**kwargs)
    db.session.add(role)
    db.session.commit()

    return role


def assign_role_user(user, role):
    user.roles.append(role)
    role.usuarios.append(user)
    db.session.commit()


def create_permission(**kwargs):
    permission = Permissions(**kwargs)
    db.session.add(permission)
    db.session.commit()

    return permission


def assign_permission_role(role, permission):
    role.permisos.append(permission)
    db.session.add(role)
    db.session.commit()


def list_permissions_by_user(user):
    list_permissions = set()
    for role in user.roles:
        for permission in role.permisos:
            list_permissions.add(permission.nombre)

    return list(list_permissions)

def set_permission(permission):
    return Permissions.query.filter_by(nombre=permission).first()