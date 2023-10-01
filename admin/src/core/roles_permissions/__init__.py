from src.core.roles_permissions.role import Roles
from src.core.roles_permissions.permission import Permissions
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
    print(permission.nombre)
    print(permission.id)
    role.permisos.append(permission)
    db.session.add(role)
    db.session.commit()